from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core.cache import cache
import os
import csv
import json
import logging
import random 
import numpy as np
import pandas as pd


logging.basicConfig(level=logging.info)

def home(request):
    return render(request, 'h2know/home.html')

def index(request):

    country_csv_path = {
            "Nigeria": "h2know/static/data/nigeria_water_points.csv",
            "Sierra Leone": "h2know/static/data/sierraleone_water_points.csv",
            "Uganda": "h2know/static/data/uganda_water_points.csv",
        }
            
    for country in country_csv_path.keys():
        get_cached_dataframe(country_csv_path[country], country)

    return render(request, 'h2know/index.html')
    
def map_view(request):
    return render(request, 'h2know/map.html')
    
def application_view(request):
    country_csv_path = {
            "Nigeria": "h2know/static/data/nigeria_water_points.csv",
            "Sierra Leone": "h2know/static/data/sierraleone_water_points.csv",
            "Uganda": "h2know/static/data/uganda_water_points.csv",
        }
            
    for country in country_csv_path.keys():
        get_cached_dataframe(country_csv_path[country], country)
    return render(request, 'h2know/application.html')

def load_dataframe_from_csv(path):
    # Load the DataFrame from the CSV file
    dataframe = pd.read_csv(path, low_memory=False).fillna("unknown")
    
    return dataframe
    
    
def get_cached_dataframe(path, country):
    # Check if the DataFrame is already cached
    cached_dataframe = cache.get(f'{country}_dataframe')

    if cached_dataframe is None:
        # If not cached, load it from the CSV and store in the cache
        dataframe = load_dataframe_from_csv(path)
        cache.set(f'{country}_dataframe', dataframe)
        return dataframe
    else:
        return cached_dataframe
        
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6372.8  # Earth radius in kilometers

    lat1_rad = np.radians(lat1)
    lon1_rad = np.radians(lon1)
    lat2_rad = np.radians(lat2)
    lon2_rad = np.radians(lon2)

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = np.sin(dlat / 2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2)**2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c

def calculate_distance_from_dataframe_haversine(dataframe, lat1, lon1, n=25):
    lat2 = dataframe['#lat_deg'].values.astype(float)
    lon2 = dataframe['#lon_deg'].values.astype(float)

    # Replicate lat1 and lon1 to match the length of lat2 and lon2
    lat1_repeated = np.repeat(lat1, len(lat2)).astype(float)
    lon1_repeated = np.repeat(lon1, len(lon2)).astype(float)
    
    distances = haversine_distance(lat1_repeated, lon1_repeated, lat2, lon2)
    top_working_water_points = dataframe
    top_working_water_points['calculated_distances'] = np.round(distances, 2)
    top_n_working_water_points = top_working_water_points.sort_values(by=['calculated_distances']).head(n)
    
    return top_n_working_water_points

def populate_water_points(request):
    cwd = os.getcwd()
    logging.info(f"Current working directory: {cwd}")
    #csv_file_path = "h2know/static/data/water_points.csv"
    markers = []

    

    if request.method == 'POST':
        country = request.POST.get('country') # Get the selected country from the POST data

        country_csv_path = {
            "Nigeria": "h2know/static/data/nigeria_water_points.csv",
            "Sierra Leone": "h2know/static/data/sierraleone_water_points.csv",
            "Uganda": "h2know/static/data/uganda_water_points.csv",
        }
        logging.info(f"Selected country: {country}")
        df = get_cached_dataframe(country_csv_path[country], country)
        
        markers = []
        
        for index, row in df.iterrows():
            lat = float(row[1])
            lon = float(row[2])
            tooltip_text = f"Water Point ID: {row[0]}<br> Location: ({row[1]}, {row[2]})<br>Water Source: {row[9]}<br> Water Tech: {row[10]}<br> Water Quality: {row[11]}"
            
            
            marker = {
                "lat": lat,
                "lon": lon,
                "tooltip": tooltip_text,
            }

            markers.append(marker)
            if index == 1500:
                break
        
    response_data = {
        'markers': markers
    }

    return JsonResponse(response_data) 

def process_location(request):
    if request.method == 'POST':
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        country = request.POST.get('country')
        
        country_csv_path = {
            "Nigeria": "h2know/static/data/nigeria_water_points.csv",
            "Sierra Leone": "h2know/static/data/sierraleone_water_points.csv",
            "Uganda": "h2know/static/data/uganda_water_points.csv",
        }
        
        df = get_cached_dataframe(country_csv_path[country], country)

        top_n_working_water_points = calculate_distance_from_dataframe_haversine(df, latitude, longitude)
        
        response_data = {}
        for column in top_n_working_water_points.columns:
            response_data[column] = top_n_working_water_points[column].tolist()
            
       
        logging.info(response_data)

        return JsonResponse(response_data)

    # Return an error response if the request method is not POST
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

def process_country(request):
    if request.method == 'POST':
        country = request.POST.get('country') # Get the selected country from the POST data

        country_to_csv = {
            "Nigeria": "nigeria_water_points.csv",
            "Sierra Leone": "sierraleone_water_points.csv",
            "Uganda": "uganda_water_points.csv",
        }

        if country and country in country_to_csv:
            # Get the CSV filename for the selected country
            csv_filename = country_to_csv[country]
            csv_file_path = os.path.join("h2know/static/data/", csv_filename)

            # Check if the CSV file exists
            if os.path.exists(csv_file_path):
                # Open the CSV file and read its contents
                with open(csv_file_path, 'r') as file:
                    csv_data = csv.reader(file)


                response_data = {
                    'message': 'Selected country CSV file located and opened.',
                    'country': country,
                    'country_plus_caps': country.upper()  
                }
            else:
                response_data = {
                    'message': 'CSV file not found for the selected country.',
                    'country': country,
                    'country_plus_caps': country.upper()  
                }
        else:
            response_data = {
                'message': 'something went wrong',
                'country': country,
                'country_plus_caps': country.upper() 
            }
         

        return JsonResponse(response_data)

    # Return an error response if the request method is not POST
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

