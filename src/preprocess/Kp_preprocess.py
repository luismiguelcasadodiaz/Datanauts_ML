#!/home/luis/.venv/inquisitor/bin/python

import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# File path
home_dir = os.path.expanduser("~")
home_dir = os.getcwd()
data_folder = home_dir + '/data/Kp_index/'
in_file_name = 'Kp_ap_2106.txt'
ou_file_name = 'Kp_since_2016.csv'
in_file_path = data_folder + in_file_name
ou_file_path = data_folder + ou_file_name

data = pd.read_csv(in_file_path, delim_whitespace=True, comment="#")
columns = ["year", "month", "day", "hour_ini", "hour_avg", "day_ini", "day_ave", "Kp", "ap", "definitive"]
data.columns = columns
data['date'] = pd.to_datetime(data[['year','month','day']])
#to save memory and speed up the process I keep only tree columns Date, Spot_num and Std_dev
data = data[['date', 'hour_ini', 'Kp']]
data.to_csv(ou_file_path, index= False)
data.head()
data.tail()
