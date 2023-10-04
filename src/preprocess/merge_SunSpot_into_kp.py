#!/home/luis/.venv/inquisitor/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    merge_SunSpot_into_kp.py                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: luicasad <luicasad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/03 10:32:13 by luicasad          #+#    #+#              #
#    Updated: 2023/10/03 10:32:13 by luicasad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


# File paths
os.chdir("../..")
home_dir = os.getcwd()

# for sn sunspot number
sn_data_folder = home_dir + '/data/SunSpotNumber/'
sn_file_name = 'sunspot_since_2016.csv'
sn_file_path = sn_data_folder + sn_file_name
sn_columns = ['date', 'sun_spot_norm']

# for kp
kp_data_folder =  home_dir +'/data/Kp_index/'
kp_file_name = 'kp_since_2016.csv'
kp_file_path = kp_data_folder + kp_file_name
kp_columns = ['date', 'hour_ini', 'kp']

# for join dataframe
jn_data_folder =  home_dir +'/data/Kp_index/'
jn_file_name = 'kp_sn_since_2016.csv'
jn_file_path = jn_data_folder + jn_file_name

# Load dataframes
kp = pd.read_csv(kp_file_path)
kp.columns = kp_columns
sn = pd.read_csv(sn_file_path)
sn.columns = sn_columns

# merge dataframes
join = pd.merge(kp, sn, on="date")
print(join.iloc[[0,1,2]])

# Save merged
join.to_csv(jn_file_path, index=False)

