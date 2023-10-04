[back to README](https://github.com/luismiguelcasadodiaz/Helio_Sentinel_Crew/tree/main)
# Data cleaning

# SunSpot Number
Filename: SN_d_tot_V2.0.csv
Format: Comma Separated values (adapted for import in spreadsheets)
The separator is the semicolon ';'.

## Contents:

| Column | Description|
|--------|-------------|
|Column 1|Year Gregorian calendar date.|
|Column 2|Month Gregorian calendar date.|
|Column 3|Day Gregorian calendar date.|
|Column 4|Date in fraction of year.|
|Column 5|Daily total sunspot number. A value of -1 indicates that no number is available for that day (missing value)|
|Column 6|Daily standard deviation of the input sunspot numbers from individual stations.|
|Column 7|Number of observations used to compute the daily value.|
|Column 8|Definitive/provisional indicator. '1' indicates that the value is definitive. '0' indicates that the value is still provisional.|

## Filter data since 2016 

```python
data = data[data['year'] >= 2016]
```
## are there missing values?

count -1 values in column 5 'sun_spot'
```python
count = sum(data['sun_spot'] == -1)
```
there ares 0 missing values

## Not all SunSpot count  is definitive. To know when provisional data starts ...

```python
data["date"] = pd.to_datetime(data[['year','month','day']])
min_data = min(data[data['Definitive'] == 0]['date'])
print("Split date {}\n".format(min_data))
```
Split date 2023-04-01 00:00:00

I will use this data as splitting date to get data set for trainig (2647) and data set for testing (153).
```python
count = sum(data['definitive'] == 1)
print("there are {} definitive values\n".format(count))

count = sum(data['definitive'] == 0)
print("there are {} preliminary values\n".format(count))
```
There are 2647 definitive values.
There are 153 preliminary values.


## Normalization

```python
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
data['sun_spot_norm'] = scaler.fit_transform(data[['sun_spot']])

```

## to save memory and speed up the process I keep only tree columns Date, Spot_num and Std_dev

```python
data = data[['date', 'sun_spot']]
```

|     |      date| sun_spot_norm|
|-----|----------|--------------|
|72317|2016-01-01|      0.154167|
|72318|2016-01-02|      0.166667|
|72319|2016-01-031      0.212500|

## Preprocessed data file

The file to use upfront is `sunspot_since_2016.csv`. it has a weight of 63 KB

# KP

## contents

| Column  | Description|
|---------|-------------|
|Column 01|Year Gregorian calendar date.|
|Column 02|Month Gregorian calendar date.|
|Column 03|Day Gregorian calendar date.|
|Column 04|Hour initial for a 3 hours interval for which Kp is given.|
|Column 05|Hour mid for a 3 hours interval for which ks is given.|
|Column 06|Days since 1932 to start opterval.|
|Column 07|Days since 1932 to mid of interval.|
|Column 08|Kp, Planetary three-hour index for the interval.
|Column 09|Ap, Planetary amplitud fot the three-hour equivalente interval.|
|Column 10|Definitive/provisional indicator. '0'= Kp & Ap preliminary, '1'= Kp definitive, Ap Preliminary, '2' = Kp & Ap definitive.|

## When preliminary data starts

```python
min_data = min(data[data['definitive'] == 0]['date']) 
```
Preliminary data starts at 2023-09-01 00:00:00

## to save memory and speed up the process I keep only tree columns Date, hout_ini and Kp

```python
data = data[['date', 'hour_ini', 'kp']]
```
|idx  |      date| hour_ini|    kp|
|-----|----------|---------|------|
|0    |2016-01-01|      3.0| 5.333|
|1    |2016-01-01|      6.0| 5.000|
|2    |2016-01-01|      9.0| 3.333|
|22652|2023-10-02|     15.0| 1.333|
|22653|2023-10-02|     18.0| 1.333|
122654|2023-10-02|     21.0| 2.333|

## Preprocessed data file

The file to use upfront is `kp_since_2016.csv`. it has a weight of 461KB.



# Merge sunspots into Kp_index File

Both file, kp & sunspot have a commond comlun name `date`. it will be the key to join the dataframes on it.


```python
join = pd.merge(kp, sn, on="date")
```
|idx|      date|hour_ini |    kp|  sun_spot_norm|
|---|----------|---------|------|---------------|
|0  |2016-01-01|      3.0| 5.333|       0.154167|
|1  |2016-01-01|      6.0| 5.000|       0.154167|
|2  12016-01-01|      9.0| 3.333|       0.154167|


## Dataset 
9857 files.

about the file names Pxyyy.zz or rdP199xyyy.zz 

Where 
P stands for plasma, x = 4 for 1994, x = 5 for 1995 and so on.
yyy is the day of year (January 1=001).
zz is the key parameter file version number (typically 02 or higher).

### Is there one file per day?
```bash
#! /bin/bash

for dir in $(ls -d */); do
	files=$(ls $dir -1 | wc)
	size=$(du -hs $dir)
	echo " $dir $files $size "
done
```


|Size| DIR   | Raw Files|Comments|Files cleaned|
|-----|------|------|----------------|-----|
|12M	|1994/ |98|There are files for days 321..365. There was a not_despiked folder i removed.<br/>rm -rf not_despiked<br/>rm temp_plist<br/>rm 000_README_WIND_P_FILES.TXT>|44|
|103M	|1995/ |734|||
|101M	|1996/ |733|||
|107M	|1997/ |734|||
|91M	|1998/ |728|||
|72M	|1999/ |623|||
|46M	|2000/ |390|||
|48M	|2001/ |401|||
|50M	|2002/ |323|||
|45M	|2003/ |377|||
|46M	|2004/ |388|Missing file for day 113.rm -rf old<br/> rm rdP2004063.01<br/>|365|
|50M	|2005/ |395|Missing file for day 21. <br/> rm -rf old|364|
|50M	|2006/ |406|Missing files for days 328..332 rm -xf old<br/> rm rdP2006033.01|360|
|52M	|2007/ |422|rm -rf old|365|
|50M	|2008/ |380|In `temp_dir` 10 files with same names than in upper dir. `diff` command show they were equal. I remove it.<br /> diff temp_dir/rdP2008060.01 rdP2008060.01<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008063.01 rdP2008063.02<br /> diff temp_dir/rdP2008064.01 rdP2008064.02<br /> diff temp_dir/rdP2008065.01 rdP2008065.02<br /> diff temp_dir/rdP2008066.01 rdP2008066.03<br /> diff temp_dir/rdP2008067.01 rdP2008067.02<br /> diff temp_dir/rdP2008068.02 rdP2008068.03<br /> diff temp_dir/rdP2008069.01 rdP2008069.02 <br/> <br/> `old` file relates to day 353. as ther is an rdP2008353.03 file, I remove olf file. <br/> <br/> for days 28 i found two diffent files on zz code. I keep the higher one.<br /> rm rdP2008028.01 <br />rm rdP2008035.01 <br /> rm rdP2008070.01 <br />rm rdP2008073.02 <br />rm rdP2008074.01 <br />rm rdP2008075.02<br />rm rdP2008076.01 <br />rm rdP2008080.01 <br />rm rdP2008081.01 <br />rm rdP2008082.01 <br />rm rdP2008083.01 <br />rm rdP2008220.01 <br />rm rdP2008254.01 <br />|365|
|48M	|2009/ |369|<br/> rm old <br/> rm rdP2009025.01<br/> rm rdP2009090.01<br/> rm rdP2009208.01|365|
|47M	|2010/ |367|<br/> rm old<br/> rmrdP2010271.01 |365|
|46M	|2011/ |364|Missing file for day 240 224||
|47M	|2012/ |367|Duplicated fiel for day 076. i keep higher version <br/> rm rdP20012076.01|366|
|46M	|2013/ |365||365|
|41M	|2014/ |331|Missing files for day 301..334|331|
|45M	|2015/ |364|Missing file for day 30|364|
|13M	|2016/ |117|Files for days 001..117|117|
|80K	|old/ |1|||

