#!/usr/local/bin/python3

import pandas as pd
import os
from sklearn.model_selection import train_test_split
import pickle
import keras

def get_data_model():
    print("Data Model ....")
    os.chdir("../..")
    home_dir = os.getcwd()

    # File path
    dm_data_folder =  home_dir +'/data/transformed/'
    dm_file_name = 'data_model_kp_sn_sat.csv'
    dm_file_path = dm_data_folder + dm_file_name

    # Ingest data
    dm = pd.read_csv(dm_file_path, delimiter=',', parse_dates=[0], header=0)
    print("The data model has this shape", dm.shape)
    return dm

# Read data model
dm = get_data_model()

#convert it into arrays for our machine to process:
values = dm.values
# 1.- Split our dataset into input features (X= 180 minutes of satellite data) and the feature we wish to predict (Y = kp)
#
# The datamodel has c column zero with a date.
# We remove the date from the date model.

X = values[:,1:9542]
Y = values[:,9542]

train_size= 0.7
test_size = 1 - train_size

## 2.- Split our dataset into a training set, a validation set and a test set.
#
#Our Data set contains 18143 records, from 01/01/2016 till 02/05/2023. There are two intervals of time when satellite did not generated data.
#
#|From       | to     |
#|-----------|--------|
#|14-01-2016|30-06-2021|
#|28-06-2019|24-02-2020|
#
#12 700 records from the Data set for training (70%)
#
#05 443 records form the Data set for testing and validation (30%)
#

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X, Y, test_size=test_size)
print("Train shapes X={} Y={}".format(X_train.shape, Y_train.shape))

#  save splitted array.

with open('data/split/X_train.pkl', 'wb') as f:
    pickle.dump(X_train, f)

with open('data/split/Y_train.pkl', 'wb') as f:
    pickle.dump(Y_train, f)


#### 3.- testing and validation data set 50/50

X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)
print(X_val.shape, Y_test.shape, Y_val.shape, Y_test.shape)
print("Test shapes X={} Y={}".format(X_test.shape, Y_test.shape))
print("Val shapes X={} Y={}".format(X_val.shape, Y_val.shape))

with open('data/split/X_val.pkl', 'wb') as f:
    pickle.dump(X_val, f)

with open('data/split/Y_val.pkl', 'wb') as f:
    pickle.dump(Y_val, f)
with open('data/split/X_test.pkl', 'wb') as f:
    pickle.dump(X_test, f)

with open('data/split/Y_test.pkl', 'wb') as f:
    pickle.dump(X_test, f)
