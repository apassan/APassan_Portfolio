## model_prep

# Import packages
import csv
import numpy as np
import pandas as pd
import runpy
import math

from sklearn.preprocessing import RobustScaler 

import seaborn as sns
from matplotlib import pyplot as plt

from imblearn.under_sampling import RandomUnderSampler 
from sklearn.model_selection import train_test_split

# Read in files
data_raw = pd.read_csv('data/card_transdata.csv')

# Standardize distance_from home
data_raw['norm_distance_from_home'] = RobustScaler().fit_transform(
    data_raw['distance_from_home'].values.reshape(-1,1)) # standardize

# Standardize distance_from_last_transaction 
data_raw['norm_distance_from_last_transaction'] = RobustScaler().fit_transform(
    data_raw['distance_from_last_transaction'].values.reshape(-1,1)) # standardize

# Standardize ratio_to_median_purchase_price
data_raw['norm_ratio_to_median_purchase_price'] = RobustScaler().fit_transform(
    data_raw['ratio_to_median_purchase_price'].values.reshape(-1,1)) # standardize
    
# Drop unnecessary columns
data_raw = data_raw.drop(['distance_from_home', 
                           'distance_from_last_transaction', 
                           'ratio_to_median_purchase_price'], axis=1)
                           
# Keeping a dataframe version will be useful for any quick checks
data_df = data_raw 

# Now need to prepare the data to get split 

# Create the features and the target variable.
cols = data_df.columns.tolist()
X_features = [c for c in cols if c not in ['fraud']]

X = data_df[X_features] # Features
Y = data_df['fraud'] # Target variable

# Perform undersampling 
us = RandomUnderSampler(random_state=42)
X_us, Y_us = us.fit_resample(X,Y)

# Split the data
X_train, X_test,Y_train, Y_test = train_test_split(X_us, Y_us, test_size=0.2)


