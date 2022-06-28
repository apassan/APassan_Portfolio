## data_prep 

# Import modules
import csv
import math
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 

# Read in files
data_raw = pd.read_csv('data/card_transdata.csv')

# Standardize distance_from home
data_raw['norm_distance_from_home'] = StandardScaler().fit_transform(
    data_raw['distance_from_home'].values.reshape(-1,1)) # standardize

# Standardize distance_from_last_transaction 
data_raw['norm_distance_from_last_transaction'] = StandardScaler().fit_transform(
    data_raw['distance_from_last_transaction'].values.reshape(-1,1)) # standardize

# Standardize ratio_to_median_purchase_price
data_raw['norm_ratio_to_median_purchase_price'] = StandardScaler().fit_transform(
    data_raw['ratio_to_median_purchase_price'].values.reshape(-1,1)) # standardize
    
# Drop unnecessary columns
data_raw = data_raw.drop(['distance_from_home', 
                           'distance_from_last_transaction', 
                           'ratio_to_median_purchase_price'], axis=1)