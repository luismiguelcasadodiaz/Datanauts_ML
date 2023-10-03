#!/home/luis/.venv/inquisitor/bin/python
# Sun Spot Number
#Filename: SN_d_tot_V2.0.csv
#Format: Comma Separated values (adapted for import in spreadsheets)
#The separator is the semicolon ';'.
#
#| Column | Description|
#|--------|-------------|
#|Column 1|Year Gregorian calendar date.|
#|Column 2|Month Gregorian calendar date.|
#|Column 3|Day Gregorian calendar date.|
#|Column 4|Date in fraction of year.|
#|Column 5|Daily total sunspot number. A value of -1 indicates that no number is available for that day (missing value)|
#|Column 6|Daily standard deviation of the input sunspot numbers from individual stations.|
#|Column 7|Number of observations used to compute the daily value.|
#|Column 8|Definitive/provisional indicator. '1' indicates that the value is definitive. '0' indicates that the value is still provisional.|

import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# File path
home_dir = os.path.expanduser("~")
home_dir = os.getcwd()
data_folder = home_dir + '/data/SunSpotNumber/'
in_file_name = 'SN_d_tot_V2.0.csv'
ou_file_name = 'sunspot_since_20162.csv'
in_file_path = data_folder + in_file_name
ou_file_path = data_folder + ou_file_name
# Load the data into a DataFrame
data = pd.read_csv(in_file_path, delimiter= ';')
columns = ["year", "month", "day", "year_fraction", "sun_spot", "std_dvt", "observations","definitive"]
data.columns = columns
data.head()


# Filter the data for entries since 2016
data = data[data['year'] >= 2016]
data["date"] = pd.to_datetime(data[['year','month','day']])

# I to split data between defititive (trining) and preliminary (testing)
min_data = min(data[data['definitive'] == 0]['date'])
print("split date {}\n".format(min_data))

# check if there are missin values counting for '-1' values in columnn 'sun_spot'
count = sum(data['definitive'] == 1)
print("There are {} definitive values\n".format(count))

# check if there are missin values counting for '-1' values in columnn 'sun_spot'
count = sum(data['definitive'] == 0)
print("There are {} preliminary values\n".format(count))


# check if there are missin values counting for '-1' values in columnn 'sun_spot'
count = sum(data['sun_spot'] == -1)
print("there are {} missing values\n".format(count))


# Nata normalization
scaler = MinMaxScaler()
data['sun_spot_norm'] = scaler.fit_transform(data[['sun_spot']])
#to save memory and speed up the process I keep only tree columns Date, Spot_num and Std_dev
data = data[['date', 'sun_spot_norm']]
data.to_csv(ou_file_path, index= False)
data.head()
data.tail()
