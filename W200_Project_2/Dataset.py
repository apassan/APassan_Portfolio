## Imports
# Standard
import urllib
import json

# Third-party
import numpy as np
import pandas as pd

# Local

class Logger:
    """
    Helper superclass to provide concise logging of messages and errors across other classes
    """
    def __log_err__(self,msg):
        self.__log__(f'Error: {msg}')

    def __log__(self,msg):
        if hasattr(self,"datasets"):
            name = "Explorer"
        else:
            name = self.resource_id if not hasattr(self,"raw") or "meta" not in self.raw  or "result" not in self.raw["meta"] else self.raw["meta"]["result"]["name"]
        print(f'[{name}] {msg}')

class Dataset(Logger):
    """
    Handles fetching data and metadata from the Singapore Government data API based on a resource ID (with local data fallback), converts the data into a Pandas DataFrame, and performs basic standardization and cleaning
    
    Inherits logging functionality from Logger

    Parameters
    ----------
    i:
        A resource ID recognizable by the Singapore Government data API
    """

    #Standard API routes set by the Singapore Gov't data API
    API_ROUTES = {
        "data": "https://data.gov.sg/api/action/datastore_search",
        "meta": "https://data.gov.sg/api/action/resource_show"
    }
    #We need to hit the API spoofing a web browser or the request may be blocked
    API_HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
    
    def __init__(self,i):
        self.resource_id = i
        self.__fetch__()
        self.__parse__()
        #Check for successful parsing
        if hasattr(self,"parsed") and "data" in self.parsed:
            self.dataframe = self.__to_DataFrame__(self.parsed['data'])
            #Generate an Explorer to show data details and sanity checks
            Explorer([self])
            self.__log__("Loaded")
        #If parsed data not present, there may be something wrong with the API response
        else: 
            self.__log__("Unable to load data")


    def __fall_back__(self,route="data"):
        #Attempts to load data from a local JSON file - used when the API is not reachable or does not send back data in the expected format
        #Local filename must be in the format [resource_id].[route].json
        #e.g., 12345-67890-12345.data.json or 12345-67890-12345.meta.json
        self.__log__(f'Falling back to local {route} file')
        try:
            f = open(f'{self.resource_id}.{route}.json')
            return json.load(f)
        except Exception as e:
            self.__log_err__(f'No properly formatted local file available. Could not load {route} route.')
        
    def __fetch_route__(self,route="data"):
        #Retrieves a specific API route for the dataset's resource
        #Expects a route parameter, either "data" or "meta"
        self.__log__(f'Fetching {"metadata" if route == "meta" else route} via API')
        try:
            #Build request URL for Singapore data API, auto-limit to 10000 which will capture all of most datasets
            request_url = f'{self.API_ROUTES[route]}?{"resource_id" if route == "data" else "id"}={self.resource_id}&limit=10000'
            if route == "data":
                #For data fetches, request API sort by latest first
                datecols = self._get_datetime_cols()
                if len(datecols):
                    request_url += f'&sort={datecols[0]["name"]}%20desc'
            req = urllib.request.Request(
                url=request_url, 
                headers=self.API_HEADERS
            )
            response = urllib.request.urlopen(req).read() 
            return json.loads(response)
        except urllib.error.URLError as e:
            self.__log_err__(f'({e.code if hasattr(e,"code") else "URL"}) {e.msg if hasattr(e,"msg") else "Error"}')
            #Can't reach API - try to use local version of data file
            return self.__fall_back__(route)
        
    def __fetch__(self):
        #Handles fetching and stashing both metadata and data for the resource
        try:
            self.raw = {}
            #Attempt to fetch raw metadata and data from API
            self.raw["meta"] = self.__fetch_route__('meta')
            self.raw["data"] = self.__fetch_route__('data')
        except Exception as e:
            self.__log_err__(e)
            
    def __parse__(self):
        #Handles verification of fetched records, transformation, and storage
        try:
            self.parsed = {}
            for key in self.raw:
                self.__log__(f'Parsing {"metadata" if key == "meta" else key}')
                subset = self.raw[key]
                #Check meta and data for success condition
                if subset["success"]:
                    #Extract records from data resource or entire package from meta resource
                    self.parsed[key] = subset["result"] if key == "meta" else subset["result"]["records"]
                else:
                    raise Exception(f'Unable to load {key} resource.')
        except Exception as e:
            self.__log_err__(e)
            
    def __to_DataFrame__(self,data):
        #Converts dict created from JSON data to Pandas DataFrame and standard formatting of numeric and date columns 
        self.__log__("Converting data to Pandas DataFrame")
        df = pd.DataFrame.from_dict(data)
        df = df.set_index("_id")
        #Find columns that are apparent dates
        datecols = self._get_datetime_cols()
        datecolnames = [col["name"] for col in datecols]
        for col in df:
            #Handle nulls that aren't really nulls coming from data API
            null_values = self._get_col_nulls(col)
            for null in null_values:
                df[col] = df[col].replace(null,np.NaN)

            if col in datecolnames:
                #Format monthly and quarterly data values in consistent date format
                col_meta = list(filter(lambda c: c["name"] == col,datecols))[0]
                date_format = col_meta["format"].replace("YYYY","%Y").replace("MM","%m").replace("[Q]Q","%m")
                df[col] = df[col].apply(lambda x: x.replace("Q1","03"))
                df[col] = df[col].apply(lambda x: x.replace("Q2","06"))
                df[col] = df[col].apply(lambda x: x.replace("Q3","09"))
                df[col] = df[col].apply(lambda x: x.replace("Q4","12"))
                df[col] = pd.to_datetime(df[col],format=date_format)
            else:
                #Initially, assume column is numeric and try to treat as such
                try:
                    df[col] = pd.to_numeric(df[col])
                except Exception as e:
                    #If it's not numeric, warn - this is probably just a column in non-numeric format, so may not be a problem
                    self.__log__(f'Column "{col}" does not appear to be numeric. Pandas says: "{str(e)}"')
                    pass
        return df

    def _get_meta(self):
        #Returns parsed or unparsed metadata as available
        return self.raw["meta"]["result"] if not hasattr(self,"parsed") else self.parsed["meta"]

    def _get_field_meta(self,field):
        #Returns the metadata for a field with the name string passed to the field param
        meta = self._get_meta()
        if "fields" in meta:
            fields_meta = meta["fields"]
            field_meta_filter = list(filter(lambda meta_field: meta_field["name"] == field,fields_meta))
            if len(field_meta_filter):
                return field_meta_filter[0]
        return None
        

    def _get_col_nulls(self,field):
        #Null values appear with a replacement string in the data API - determines and returns the replacement string for a given field from the metadata
        field_meta = self._get_field_meta(field)
        if field_meta:
            return [char for char in field_meta["null_values"].keys() if char != "count"]
        return []

    def _get_datetime_cols(self):
        #Returns all fields that are in datetime format according to the API
        try:
            meta = self._get_meta()
            return [field for field in meta["fields"] if field["type"] == "datetime"]
        except Exception as e:
            self.__log_err__(e)

#Used in dataset exploration to check datasets in bulk
#In data analysis, this has been incorporated into the Dataset class to automatically show data info on instantiation
class Explorer(Logger):
    """
    Displays basic info for validation and sanity checks for the dataframe within a Dataset object
    
    Inherits logging functionality from Logger

    Parameters
    ----------
    datasets:
        An enumerable containing one or more Dataset objects
    """
    def __init__(self,datasets):
        self.datasets = datasets
        for dataset in self.datasets:
            print("\n")
            self.__log__(f'Analyzing "{dataset.parsed["meta"]["name"]}"')
            print("-"*50)
            print("Describe")
            print("-"*10)
            print(dataset.dataframe.describe(datetime_is_numeric=True))
            print("\n")
            print("Head")
            print("-"*10)
            print(dataset.dataframe.head())
            dataset.dataframe.hist(bins=10)
            datecols = dataset._get_datetime_cols()
            dataset.dataframe.plot(x=datecols[0]["name"])

            
            