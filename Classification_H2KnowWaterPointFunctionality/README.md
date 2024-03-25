# H2knOw

H2knOw is a web interface that allows people in water stressed & scarce countries to locate the closest functioning water points to their location. The tool is currently a proof of concept that includes Sierra Leone, Nigeria, and Uganda, where collectively 219 million people lack access to safe water. 

As our global population swells and resource-intensive development surges, many countries have become water scarce or water stressed. They face water demands that outpace supply, and grapple with inadequate infrastructure to meet the growing need[<sup>1</sup>](https://www.unwater.org/water-facts/water-scarcity). Climate change has only exacerbated these issues, leading to unpredictable water availability, diminished terrestrial water storage, and disruptive floods or droughts that threaten societies[<sup>2</sup>](https://archive.ipcc.ch/pdf/technical-papers/climate-change-water-en.pdf).

With 2 billion people lacking access to safe drinking water worldwide[<sup>3</sup>](https://unstats.un.org/sdgs/report/2022/Goal-06/?_gl=1*j65eaj*_ga*NDE4ODEyMzg1LjE2ODU1NjQxMjk.*_ga_TK9BQL5X7Z*MTY4NTU2NDEyOC4xLjAuMTY4NTU2NDEyOC4wLjAuMA..), H2knOw believes that leveraging data-driven solutions has strong potential to lead to a water-secure future for all. 


## Data Sources
The following data sources were used in H2knOw’s model:

- [Water Point Data Exchange (WPdx)](https://www.waterpointdata.org/): A platform that facilitates the standardization, sharing, and access of data related to water points (e.g. wells, boreholes, water pumps, etc.). They collaborate with governments, non-governmental organizations, and researchers to collect data and document functionality status. 
- [World Bank Development Indicators](https://databank.worldbank.org/source/world-development-indicators): An international financial institution that provides assistance to developing countries to reduce poverty, promote sustainable economic growth, and improve living standards. The model incorporates a variety of their national development indicators.
- [Global Data Lab](https://globaldatalab.org/): An independent data and research center at the Nijmegen School of Management of Radboud University. They collect socio-economic, demographic, gender and health subnational  indicators from over 500 household survey datasets for low- and middle-income countries (LMICs).


## Data Science Approach

### Input & Target Variables 
The inputs to the XGBoost model included 259,518 water point observations for Sierra Leone, Nigeria, and Uganda from WPdx, which includes the following water point information: Geo-coordinates, technology/type of waterpoint, management, their proximity to roads and towns, water quality, staleness of the observation, and historical observations

Additional national and subnational contextual data from the World Bank and Global Data Lab were also used to help the model differentiate between different country and regional contexts.  Country level indicators included features such as GDP growth, political stability, rule of law, government effectiveness, percentage of land area for agriculture, and land surface temperature; regional level indicators included human development index, agricultural employment, average years of female schooling, and log GNI per capita

In total there were 54 input features (before encoding categorical features) with information speaking to the individual water points, and country and regional contexts. 

The target variable is a binary variable on whether or not a water point was functional at the time of the observation.

### Algorithm
H2knOw uses an XGBoost classification algorithm to predict whether a water point in question is functional. XGBoost is an ensemble machine learning algorithm that combines multiple weak decision tree learners to form a strong learner. Each new tree attempts to fix the errors of the trees already part of the model until no further improvements can be made[<sup>4</sup>](https://towardsdatascience.com/https-medium-com-vishalmorde-xgboost-algorithm-long-she-may-rein-edd9f99be63d).

This algorithm was chosen as it is known to handle null values well, is robust to multicollinearity, high accuracy, includes measures for regularization to help the model perform better on unseen data, and can scale up easily thanks to parallel processing. Given the context of the water point data where not all fields were mandatory for partner organizations to fill out for WPdx, and the similarity of some features, a model such as XGBoost was a strong fit for this context.

As there are some water points that have multiple observations from different points in time, H2knOw uses XGBoost in the context of time series forecasting to predict water point functionality. An earlier observation of a water point provides helpful context to improve the prediction of the water point’s future functionality. Additionally, temporal attributes such as an observation’s month and day of month help the model extract any yearly or monthly trends that may affect functionality of a water point (e.g. in relation to dry season or any scheduled maintenance).

#### Considerations for COVID-19 Pandemic
It should also be mentioned that the COVID-19 pandemic changed population behavior significantly, and directly impacted the development of time series in many domains because it led to unrepresentative values in data history, which in turn can hinder model learning[<sup>5</sup>](https://cienciadedatos.net/documentos/py45-weighted-time-series-forecasting.html). This was also the case in developing the final H2knOw model. 

The three countries had their highest waves in COVID-19 cases in mid-2020, and in Summer and Winter 2021[<sup>6,</sup>](https://coronavirus.jhu.edu/region/sierra-leone)[<sup>7,</sup>](https://coronavirus.jhu.edu/region/nigeria)[<sup>8</sup>](https://coronavirus.jhu.edu/region/uganda). This timeline affected the frequency of water point observations done during the pandemic.There was a drop in organizations collecting data on water points in 2020 (3,099 observations) and 2021 (4,965 observations) due to the pandemic. Data collection increased significantly in 2022 (17,907 observations) and 2023 (7,416 observations), indicating that much of the information being captured in these two years were a reflection of the large waves of the pandemic in the years just before, and also showed a much higher distribution of non-functional water points compared to previous years -  showing a changed population behavior. It is for this reason that H2knOw decided to only incorporate data until 2021 in this proof of concept model. 

### Training & Testing 
Given this is a time series model, it was very important to ensure that the training, validation, and test data were split properly to avoid data leakage. The H2knOw model was trained on water point observations taken from 2005 until 2020 (229,230 observations), and tested on observations from 2021 (4,965 observations); total 234,195 records including historical observations.

A 5 fold cross validation with a time series split was used in training the XGBoost model. This means that for each fold, the training dataset (ordered by observation date) was split into a training and validation set by selecting a cut off point. Each successive cut off point moves forward in time. 

Data from 2021 was not included in the cross validation. It was held out as the final test set to evaluate our selected model on unseen data. 

Note on model development: the final model was developed via hyperparameter tuning with the help of grid search (which also incorporated a 5-fold cross validation with a time series split in training each potential model).


## Evaluation
Before developing our final model, we established some baselines to serve as a reference for comparison. Our first baseline was based on random guess; i.e. what the probability of a water point being functional is in our training set; this was 58%. Our second baseline was a simple decision tree which had an improved accuracy of 74% and an F1-score of 2%. So while the decision tree had a higher accuracy than the random guess, it had a very weak F-1 score (closer to 100% is ideal) indicating that it was having significant difficulties in correctly classifying the water points. 

The final model outperformed both baselines with an accuracy of 98% and F-1 score of 89%, showing that this model was able to effectively distinguish between functioning and nonfunctioning water points. 

The original WPdx dataset has one observation for a single waterpoint. There is a column in the dataset that has historical data for a portion of the dataset. After retrieving data from the historical data column, we can split the training and testing datasets for the machine learning model by year i.e. 2005-2020 for training and 2021 for testing. This particular split is what occurred in the final model giving us the results listed above. 

The features that were the most predictive included: staleness score (i.e. how old the latest water point observation is), longitude, latitude, installation year, proximity to roads and urban areas, pressure score, crucialness score, and the log gross national income per capita in 1,000 USD (2011 PPP). The pressure (0-100%) score gives a measure of the capacity the water point is functioning at, while the crucialness score (0-100%) is a measure of how important the water point is in a 1km radius; more water points in the 1km radius will lead to a lower score. More information about these scores can be found on the [WPdx data guide](https://www.waterpointdata.org/docs/WPdx_User_Guide.pdf). 


## Moving Forward
The H2knOw team hopes that this proof of concept can help water stressed and water scarce communities access safe water. By working together with organizations such as WPdx, NGO actors (e.g. Water Sanitation and Hygiene Global and National Cluster Coordination Groups), international organizations, and government actors who have developed relationships with local populations, H2knOw is confident it can take this proof of concept into production.

The immediate next step would be to partner with one of the organizations mentioned above in a single country and focus on working with the partner to collect and obtain more granular contextual data, and more up to date water point observations. This would be followed by monitoring the data to see when population behavior will return to how it was pre-pandemic. Once this has been achieved, we would be able to retrain the model, and roll out a pilot version of the application. Depending on how often H2KnOw would be able to access new data, the model would have to be updated and maintained accordingly. 

In the future, H2knOw would like to expand this model to other countries, expand the timeline of the working model, and predict with greater confidence at what point in time a water point’s functionality may change. Working with partners to update water point observations and get more granular contextual data will be key in achieving this goal. Another method will be to work with partner organizations to better streamline data collection processes (e.g. provide QR codes at water points that could be used to crowdsource status updates from the public)

## Acknowledgements
H2knOw greatly appreciates Water Point Data Exchange and the Capstone Instruction Team for their education and insight to make this project a success. 


# Webpage Development Set Up

1. Setup a python virtual environment by entering the following commands for your mac or Linux terminal
- > `$ python -m venv h2know-virtual-environment`
- > `$ source ./h2know-virtual-environment/bin/activate`
- > `$ pip install django`
- > `$ git clone git@github.com:DataScienceKid/h2know-webpage.git`
- > `$ cd h2know-webpage`
- > `$ python manage.py runserver`

2.  At this point, if there aren't any errors, your page will be running from your local.
3.  Navigate on any web browser to the url: http://127.0.0.1:8000/

And voila! You have the webpage ready for development.

# Data and Model Pipeline set up

Once you've set up your local python environment, you can run the following files in the 'code/' folder in order to run the full data and model pipeline. Running the below two notebooks is crucial as they will produce files needed to run the other notebooks.
1. DataPipeline.ipynb
2. DataPipeline_2021.ipynb

Now you can run any of the following notebooks:
- EDA.ipynb
- BaselineModels.ipynb
- FINAL_XGBoost_Model.ipynb
- experiments/FINAL_XGBoost_Test2019.ipynb
- experiments/FINAL_XGBoost_Test2020.ipynb
- experiments/FINAL_XGBoost_Test2021.ipynb

