#!/home/luis/.venv/inquisitor/bin/python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    satellite_transform.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: luicasad <luicasad@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/04 10:04:18 by luicasad          #+#    #+#              #
#    Updated: 2023/10/04 17:07:30 by luicasad         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import pandas as pd
import os
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MinMaxScaler

def	print_head_tail(df):
	print(df.iloc[[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, df.index[-3],df.index[-2],df.index[-1]]])
def save_transformed(df):
	print("Saving transformed data.....")
	home_dir = os.getcwd()

	# File path
	tr_data_folder =  home_dir +'/data/transformed/'
	tr_file_name = 'data_model_kp_sn_sat.csv'
	tr_file_path = tr_data_folder + tr_file_name

	# Save data
	df.to_csv(tr_file_path, index= False)
	


def get_kp_sn():
	print("Reading Kp & sunspots ....")
	home_dir = os.getcwd()

	# File path
	jn_data_folder =  home_dir +'/data/Kp_index/'
	jn_file_name = 'kp_sn_since_2016.csv'
	jn_file_path = jn_data_folder + jn_file_name

	# Ingest data
	kp_sn = pd.read_csv(jn_file_path, delimiter=',', parse_dates=[0], header=0)
	#print_head_tail(kp_sn)
	return kp_sn

def	get_sa():
	print("Reading satellite data ...")
	home_dir = os.getcwd()

	# File path
	sa_data_folder =  home_dir +'/data/PlasMAG/'
	sa_file_name = 'satellite_data.csv'
	sa_file_path = sa_data_folder + sa_file_name

	# Ingest data
	sa = pd.read_csv(sa_file_path, delimiter = ',', parse_dates=[0],  header = 0)

	#print_head_tail(sa)
	return sa

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

def	dataframe_to_row(kp_date,df, kp,sun_spot):
	""" 
	Returns a df_row that concatenates all rows from df
	
	GETS
	df		: A pandas dataframe with 180 Rows from satellite data.
			 One per each minute of the 3 hour kp interval starting
			 at kp_date
	kp_date	: initial time of the 3-hour kp interval
	kp		: kp index for the interval
	sun_spot: Num of sun spots counted by Royal observatory of Belgium

	RETURNS
	df_row	: [kp_date, 180 x 53 = 9540 measures, sun_spot, Kp]
			 
	"""
	row_list = []
	row_list.append(kp_date)
	for row in df.itertuples():
		for column_value in row[2:]:
			row_list.append(column_value)
	row_list.append(sun_spot)
	row_list.append(kp)
	df = pd.DataFrame(row_list)
	return df.T


def prepare_dates(day, hour):
	"""
	GETS
	day		:The Kp files timestamp refering to day start. always 00:00:00
	hour	:The hour of day (0, 3, 6, 9, 12, 15, 18, 21, 24) in which one eight 
			 of the day stars

	RETURNS	:
	start	:The timestamp yyyy-mm-dd 00:00:00 plus a delta time to hour.
			 in case of hour of ini = 9 ==> yyyy-mm-dd 09:00:00
	end		:The timestamp yyyy-mm-dd 00:00:00 plus a delta time to hour ini 
			 plus 3 hours that is the Kp interval Length 
	"""
	start = day + pd.Timedelta(hours=(hour))
	end = day + pd.Timedelta(hours=hour + 3)
	return start, end

def	transform(sa,  kp_sn):
	"""
	GETS:
	sa		:A dataframe with one record per minute
	kp_sn	:A dataframe with one record per each three hours

	RETURNS
	result	:A new dataframe with one record per each three hours, as defined
			 by kp_sn, where each record has 9487 columns resulting of 
			 concatenate 180-record (three hours) from sa.

	OPERATION
			loop Kp index dataframe.
				for each row filter satellite data by proper dates
				concatenate them to get a (9354 x 1) data frame
				append such dataframe into a list of dataframes
			return the concatenation (UNION) of the dataframes in the list
	"""
	print("Transforming data ....")
	counter = 0
	dataframes = []
	for kp_row in kp_sn.itertuples():
		start, end = prepare_dates(day=kp_row.date, hour=kp_row.hour_ini)
		filtered_df = filter_rows_by_date_range(sa, start, end)
		if (len(filtered_df.index) != 0):
			#print(filtered_df)
			row_df = dataframe_to_row(start, filtered_df,kp_row.kp, kp_row.sun_spot_norm)
			#print("============{}=>\n{}".format(counter, row_df))
			dataframes.append(row_df)
			counter = counter + 1
			print(counter)
			#if (counter == 3):
			#	break
		else:
			start = start.strftime('%Y-%m-%d %X')
			end = end.strftime('%Y-%m-%d %X')
			print("No satellite data in [{}, {}[".format(start, end))
	return pd.concat(dataframes)
			
if __name__ == '__main__':
	os.chdir("../..")
	kp_sn = get_kp_sn()
	sa = get_sa()
	transformed = transform(sa, kp_sn)
	save_transformed(transformed)
