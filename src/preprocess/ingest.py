#!/bin/python
import pandas as pd
data = pd.read_csv("dsc_fc_summed_spectra_2016_v01.csv", \
delimiter = ',', parse_dates=[0], \
na_values=0, \
header = None)
columns = ["UTC", "MF_nT_GSE_x",  "MF_nT_GSE_y", "MF_nT_GSE_z"]
for i in range(4, 54):
	columns.append(f"C_{i:02d}")
data.columns = columns
data.fillna(0)
print(data.describe())

