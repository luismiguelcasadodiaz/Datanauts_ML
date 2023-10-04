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



def filter_rows_by_date_range(df, start_date, end_date):
  """Filters rows between two dates in a Pandas DataFrame.
	  [start_date,end_date[
	  end_date is not included
  Args:
    df: A Pandas DataFrame.
    start_date: The start date of the date range.
    end_date: The end date of the date range.

  Returns:
    A Pandas DataFrame containing the filtered rows.
  """

  # Convert the start and end dates to datetime objects.
  start_date = pd.to_datetime(start_date)
  end_date = pd.to_datetime(end_date)

  # Create a boolean mask to select rows where the date column is between the start and end dates.
  mask = (df['date'] >= start_date) & (df['date'] < end_date)

  # Select the rows from the DataFrame that match the boolean mask.
  filtered_df = df.loc[mask]

  return filtered_df

def	dataframe_to_row(df):
	""" returns a df_row that concatenates all rows form df
	Args:
	df: A pandas dataframe.
	"""
	for row in df.itertuples():
		print(row.Index)
		for column_value in row[1:]:
			print(column_value)


# File path
os.chdir("../..")
home_dir = os.getcwd()
sa_data_folder =  home_dir +'/data/PlasMAG/'
#sa_file_name = 'sa_2016_2023_raw.csv'
sa_file_name = 'dsc_fc_summed_spectra_2016_v01.csv'
ou_file_name = 'satellite_data.csv'
sa_file_path = sa_data_folder + sa_file_name
ou_file_path = sa_data_folder + ou_file_name
sa = pd.read_csv(sa_file_path, delimiter = ',', parse_dates=[0],  header = None)
columns = ["date", "MF_nT_GSE_x",  "MF_nT_GSE_y", "MF_nT_GSE_z"]
for i in range(4, 54):
	columns.append(f"C_{i:02d}")
sa.columns = columns
sa.fillna(0, inplace=True)
filtered_df = filter_rows_by_date_range(sa, '2016-12-17 23:00:00', '2016-12-17 23:18:00')
print(filtered_df)
row_df = dataframe_to_row(filtered_df)

# Print the filtered dataFrame transformed in a row
#print(row_df)
