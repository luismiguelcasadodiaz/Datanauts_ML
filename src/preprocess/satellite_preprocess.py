#!/home/luis/.venv/inquisitor/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ingest.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: luicasad <luicasad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/03 12:43:17 by luicasad          #+#    #+#              #
#    Updated: 2023/10/03 12:43:17 by luicasad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import pandas as pd
import os
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

def convert_zero_to_nan(value):
	if value == 0:
		return np.nan
	else:
		return value
def count_NAN(df):
	for col in df.columns:
		count = df[col].isna().sum()
		print("{} = {}".format(col,count))
		

# File path
os.chdir("../..")
home_dir = os.getcwd()
sa_data_folder =  home_dir +'/data/PlasMAG/'
sa_file_name = 'sa_2016_2023_raw.csv'
#sa_file_name = 'dsc_fc_summed_spectra_2016_v01.csv'
ou_file_name = 'satellite_data.csv'
sa_file_path = sa_data_folder + sa_file_name
ou_file_path = sa_data_folder + ou_file_name


#ingest data
sa = pd.read_csv(sa_file_path, delimiter = ',', parse_dates=[0],  header = None, na_values=['0'])
# set headers
columns = ["date", "MF_nT_GSE_x",  "MF_nT_GSE_y", "MF_nT_GSE_z"]
for i in range(4, 54):
	columns.append(f"C_{i:02d}")
sa.columns = columns
print(sa.iloc[[0,1, 2,sa.index[-3],sa.index[-2],sa.index[-1]]])
print(sa.describe())
# Nan Substituion
sa.fillna(0, inplace=True)
print(sa.iloc[[0,1, 2,sa.index[-3],sa.index[-2],sa.index[-1]]])
print(sa.describe())

#Normaliza
integer_columns = columns[1:4]
natural_columns = columns[4:] 
integer_scaler = MinMaxScaler(feature_range=(-1, 1))
natural_scaler = MinMaxScaler(feature_range=( 0, 1))
sa[integer_columns] = integer_scaler.fit_transform(sa[integer_columns])
sa[natural_columns] = natural_scaler.fit_transform(sa[natural_columns])

#save data
print(sa.iloc[[0,1, 2,sa.index[-3],sa.index[-2],sa.index[-1]]])
sa.to_csv(ou_file_path, index=False)

