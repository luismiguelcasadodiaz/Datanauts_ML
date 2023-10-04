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




# File path
os.chdir("../..")
home_dir = os.getcwd()
sa_data_folder =  home_dir +'/data/PlasMAG/'
sa_file_name = 'sa_2016_2023_raw.csv'
#sa_file_name = 'dsc_fc_summed_spectra_2016_v01.csv'
ou_file_name = 'satellite_data.csv'
sa_file_path = sa_data_folder + sa_file_name
ou_file_path = sa_data_folder + ou_file_name
sa = pd.read_csv(sa_file_path, delimiter = ',', parse_dates=[0],  header = None)
columns = ["date", "MF_nT_GSE_x",  "MF_nT_GSE_y", "MF_nT_GSE_z"]
for i in range(4, 54):
	columns.append(f"C_{i:02d}")
sa.columns = columns
sa.fillna(0, inplace=True)
print(sa.iloc[[0,1, 2,sa.index[-3],sa.index[-2],sa.index[-1]]])
sa.to_csv(ou_file_path, index=False)

