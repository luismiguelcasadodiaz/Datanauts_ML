#!/home/luis/.venv/inquisitor/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Kp_preprocess.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: luicasad <luicasad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/03 10:32:39 by luicasad          #+#    #+#              #
#    Updated: 2023/10/03 10:32:39 by luicasad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# kp Indexr
#Filename: Skp_2016_2023_raw.txt
#Source:https://kp.gfz-potsdam.de/en/data
#LICENSE: CC BY 4.0
#Format: Space Separated values (adapted for import in spreadsheets)
#The separator is the semicolon ';'.
#| Column  | Description|
#|---------|-------------|
#|Column 01|Year Gregorian calendar date.|
#|Column 02|Month Gregorian calendar date.|
#|Column 03|Day Gregorian calendar date.|
#|Column 04|Hour initial for a 3 hours interval for which Kp is given.|
#|Column 05|Hour mid for a 3 hours interval for which ks is given.|
#|Column 06|Days since 1932 to start opterval.|
#|Column 07|Days since 1932 to mid of interval.|
#|Column 08|Kp, Planetary three-hour index for the interval.
#|Column 09|Ap, Planetary amplitud fot the three-hour equivalente interval.|
#|Column 10|Definitive/provisional indicator. '0'= Kp & Ap preliminary, '1'= Kp definitive, Ap Preliminary, '2' = Kp & Ap definitive.|
#

import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# File path
os.chdir("../..")
home_dir = os.getcwd()
data_folder =  home_dir +'/data/Kp_index/'
in_file_name = 'kp_2016_2023_raw.txt'
ou_file_name = 'kp_since_2016.csv'
in_file_path = data_folder + in_file_name
ou_file_path = data_folder + ou_file_name


# Load the data into a DataFrame and set up headers names.
data = pd.read_csv(in_file_path, delim_whitespace=True, comment="#")
columns = ["year", "month", "day", "hour_ini", "hour_avg", "day_ini", "day_ave", "kp", "ap", "definitive"]
data.columns = columns
data['date'] = pd.to_datetime(data[['year','month','day']])
min_data = min(data[data['definitive'] == 0]['date'])
print("Preliminary data starts at {}\n".format(min_data))
#to save memory and speed up the process I keep only tree columns Date, hour_ini and kp
data = data[['date', 'hour_ini', 'kp']]
data.to_csv(ou_file_path, index= False)
print(data.iloc[[0,1, 2,data.index[-3],data.index[-2],data.index[-1]]])


