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

## To save memory and speed up the process I keep only tree columns Date, Spot_num, and Std_dev

```python
data = data[['date', 'sun_spot']]
```

|     |      date| sun_spot_norm|
|-----|----------|--------------|
|72317|2016-01-01|      0.154167|
|72318|2016-01-02|      0.166667|
|72319|2016-01-03|      0.212500|

## Preprocessed data file

The file to use upfront is `sunspot_since_2016.csv`. it has a weight of 63 KB

# KP

## contents

| Column  | Description|
|---------|-------------|
|Column 01|Year Gregorian calendar date.|
|Column 02|Month Gregorian calendar date.|
|Column 03|Day Gregorian calendar date.|
|Column 04|Hour initial for a 3-hour interval for which Kp is given.|
|Column 05|Hour mid for a 3-hour interval for which ks is given.|
|Column 06|Days from 1932 to start interval.|
|Column 07|Days from 1932 to mid of interval.|
|Column 08|Kp, Planetary three-hour index for the interval.
|Column 09|Ap, Planetary amplitude for the three-hour equivalent interval.|
|Column 10|Definitive/provisional indicator. '0'= Kp & Ap preliminary, '1'= Kp definitive, Ap Preliminary, '2' = Kp & Ap definitive.|

## When preliminary data starts

```python
min_data = min(data[data['definitive'] == 0]['date']) 
```
Preliminary data starts at 2023-09-01 00:00:00



## To save memory and speed up the process I keep only tree columns Date, hout_ini, and Kp

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
|22654|2023-10-02|     21.0| 2.333|

## Preprocessed data file

The file to use upfront is `kp_since_2016.csv`. it has a weight of 461KB.



# Merge sunspots into Kp_index File

Both files, kp & sunspot, have a common column name `date`. it will be the key to joining the data frames on it.


```python
join = pd.merge(kp, sn, on="date")
```
|idx|      date|hour_ini |    kp|  sun_spot_norm|
|---|----------|---------|------|---------------|
|0  |2016-01-01|      3.0| 5.333|       0.154167|
|1  |2016-01-01|      6.0| 5.000|       0.154167|
|2  |2016-01-01|      9.0| 3.333|       0.154167|

---
 # DSCOVR
[data source](https://www.spaceappschallenge.org/develop-the-oracle-of-dscovr-experimental-data-repository/)

The data files in this repository contain measurements from the DSCOVR PlasMAG instrument suite, recorded in the solar wind near the Earth-Sun L1 Lagrange Point between 2016 and the present day.

Each file corresponds to one year of measurements. The measurements themselves have been condensed and decimated to a cadence of one measurement set per minute.


|lines    | File name for a year 
|:-------:|:---------------------------------|
|   283680|dsc_fc_summed_spectra_2016_v01.csv|
|   525600|dsc_fc_summed_spectra_2017_v01.csv|
|   537120|dsc_fc_summed_spectra_2018_v01.csv|
|   256320|dsc_fc_summed_spectra_2019_v01.csv|
|   447840|dsc_fc_summed_spectra_2020_v01.csv|
|   525600|dsc_fc_summed_spectra_2021_v01.csv|
|   525600|dsc_fc_summed_spectra_2022_v01.csv|
|   175680|dsc_fc_summed_spectra_2023_v01.csv|


Total lines 3277440 with 54 columns


|column | Description|
|---------|:--------------------------|
|column 00| A date and time in Coordinated Universal Time (UTC), formatted like YYYY-MM-DD hh:mm:ss.|
|column 01| Components of the magnetic field vector that was measured at this time. They are expressed in units of nanoTesla (nT) and provided in the Geocentric Solar Ecliptic reference frame (GSE).
|column 02| Components of the magnetic field vector that was measured at this time. They are expressed in units of nanoTesla (nT) and provided in the Geocentric Solar Ecliptic reference frame (GSE).
|column 03| Components of the magnetic field vector that was measured at this time. They are expressed in units of nanoTesla (nT) and provided in the Geocentric Solar Ecliptic reference frame (GSE).
|column 04..53|A "raw" measurement spectrum from the Faraday cup plasma detector. Each value corresponds to the flux, or flow strength, of the solar wind in a particular range of energies (or flow speeds). These numbers are not calibrated or converted-- they are dimensionless numbers as encoded in the instrument computer.|



```python 
sa = pd.read_csv(sa_file_path, delimiter = ',', parse_dates=[0],  header = None, na_values=['0'])
```

## Setting headers

```python
columns = ["date", "MF_nT_GSE_x",  "MF_nT_GSE_y", "MF_nT_GSE_z"]
for i in range(4, 54):
	columns.append(f"C_{i:02d}")
sa.columns = columns
```

||date|MF_nT_GSE_x|MF_nT_GSE_y|MF_nT_GSE_z|C_04|C_05|C_06|C_07|C_08|C_09|...|C_44|C_45|C_46|C_47|C_48|C_49|C_50|C_51|C_52|C_53|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|2016-01-01 00:00:00|6.83609|-3.37934|-12.920500|NaN|NaN|NaN|NaN|NaN|NaN|...|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|
|1|2016-01-01 00:01:00|6.76732|-3.30194|-12.996700|NaN|NaN|NaN|NaN|NaN|NaN|...|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|
|2|2016-01-01 00:02:00|6.39107|-2.61173|-13.327100|NaN|NaN|NaN|NaN|NaN|NaN|...|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|
|3277437|2023-05-02 23:57:00|4.28322|3.02154|0.927773|0.854185|0.231726|8.10454|2.02580|4.22000|0.231726|...|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|
|3277438|2023-05-02 23:58:00|4.31376|2.67727|1.723270|0.801559|0.231726|12.76210|2.81855|4.82242|0.301864|...|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|
|3277439|2023-05-02 23:59:00|4.51542|2.30317|1.832570|2.265740|0.231726|11.68700|1.89290|2.39384|0.231726|...|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|NaN|


## Zero Substitutions
The PlasMAG detectors do not take data all of the time, and the Faraday cup does not make measurements over its full range every minute. Whenever and wherever no data are available, the field is filled in with an integer 0. We recommend converting these to "NaN" in your computing environment after you load the data.


This table shows per column, how many rows have NaN values.
|              |              |              |              |              |
|--------------|--------------|--------------|--------------|--------------|
|MF_nT_GSE_x = 17442|MF_nT_GSE_y = 17442|MF_nT_GSE_z = 17442|C_04 = 1757636|C_05 = 1695129|
|C_06 = 1556408|C_07 = 1467449|C_08 = 1355341|C_09 = 1268964|C_10 = 1148804|
|C_11 = 1053137|C_12 = 921593 |C_13 = 853886 |C_14 = 732934 |C_15 = 682399 |
|C_16 = 623358 |C_17 = 554684 |C_18 = 506961 |C_19 = 472456 |C_20 = 425829 |
|C_21 = 425497 |C_22 = 434438 |C_23 = 521356 |C_24 = 573915 |C_25 = 749402 |
|C_26 = 846987 |C_27 = 1001870|C_28 = 1124509|C_29 = 1315618|C_30 = 1457869|
|C_31 = 1690322|C_32 = 1784844|C_33 = 2032300|C_34 = 2114747|C_35 = 2218250|
|C_36 = 2396398|C_37 = 2499624|C_38 = 2570894|C_39 = 2726544|C_40 = 2775096|
|C_41 = 2936463|C_42 = 2979187|C_43 = 3035621|C_44 = 3098005|C_45 = 3145790|
|C_46 = 3173983|C_47 = 3207326|C_48 = 3216033|C_49 = 3239739|C_50 = 3243152|
|C_51 = 3247843|C_52 = 3248982|C_53 = 3251170|||

In total, there are  89 413 068 NaN values in a data set of 3 277 439 x 53 = 173 704 267 data points.
A 51,47% of Satellite dataset data points are NaN values, ergo zeroes. Maybe I have to think about a sparse matrix.

## Nan Substitution

```python
sa.fillna(0, inplace = True)
```
||date|MF_nT_GSE_x|MF_nT_GSE_y|MF_nT_GSE_z|C_04|C_05|C_06|C_07|C_08|C_09|...|C_44|C_45|C_46|C_47|C_48|C_49|C_50|C_51|C_52|C_53|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|2016-01-01 00:00:00|6.83609|-3.37934|-12.920500|0.000000|0.000000|0.00000|0.00000|0.00000|0.000000|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|1|2016-01-01 00:01:00|6.76732|-3.30194|-12.996700|0.000000|0.000000|0.00000|0.00000|0.00000|0.000000|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|2|2016-01-01 00:02:00|6.39107|-2.61173|-13.327100|0.000000|0.000000|0.00000|0.00000|0.00000|0.000000|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|3277437|2023-05-02 23:57:00|4.28322|3.02154|0.927773|0.854185|0.231726|8.10454|2.02580|4.22000|0.231726|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|3277438|2023-05-02 23:58:00|4.31376|2.67727|1.723270|0.801559|0.231726|12.76210|2.81855|4.82242|0.301864|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|3277439|2023-05-02 23:59:00|4.51542|2.30317|1.832570|2.265740|0.231726|11.68700|1.89290|2.39384|0.231726|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|

[6 rows x 54 columns]


## Normalization

We can appreciate that three columns have negative values. 

|     |date                         |MF_nT_GSE_x  |MF_nT_GSE_y  |MF_nT_GSE_z  |C_04        |...|        C_49|        C_50|        C_51|        C_52|C_53        |
|-----|-----------------------------|-------------|-------------|-------------|------------|---|------------|------------|------------|------------|------------|
|count|3277440                      | 3.277440e+06| 3.277440e+06| 3.277440e+06|3.277440e+06|...|3.277440e+06|3.277440e+06|3.277440e+06|3.277440e+06|3.277440e+06|
|mea n|2019-11-24 16:42:18.717038592| 7.972786e-02|-1.248412e-01| 2.159501e-02|3.201943e+01|...|4.196891e+00|3.816626e+00|3.062619e+00|3.362869e+00|2.718429e+00|
|min  |2016-01-01 00:00:00          |-2.014280e+01|-3.178510e+01|-3.332440e+01|0.000000e+00|...|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|
|25%  |2018-01-04 11:59:45          |-2.519810e+00|-2.627630e+00|-1.511620e+00|0.000000e+00|...|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|
|50%  |2020-03-20 23:59:30          | 1.384060e-01|-1.851820e-01| 1.646555e-02|0.000000e+00|...|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|
|75%  |2021-10-10 23:59:15          | 2.660292e+00| 2.381362e+00| 1.542450e+00|5.360380e+01|...|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|0.000000e+00|
|max  |2023-05-02 23:59:00          | 3.304940e+01| 2.789380e+01| 3.483770e+01|1.675760e+03|...|1.719110e+03|1.939020e+03|1.852740e+03|1.875050e+03|1.866960e+03|
|std  |NaN                          | 3.401187e+00| 3.755768e+00| 2.974669e+00|5.610893e+01|...|4.033789e+01|3.864041e+01|3.373489e+01|3.760109e+01|3.188347e+01|

So we normalize differently natural comuns than integer column 
```python
integer_columns = columns[1:4]
natural_columns = columns[4:]
integer_scaler = MinMaxScaler(feature_range=(-1, 1))
natural_scaler = MInMaxScaler(feature_range=( 0, 1))
sa[integer_columns] = integer_scaler.fit_transform(sa[integer_columns])
sa[natural_columns] = natural_scaler.fit_transform(sa[natural_columns])
```
||date|MF_nT_GSE_x|MF_nT_GSE_y|MF_nT_GSE_z|C_04|C_05|C_06|C_07|C_08|C_09|...|C_44|C_45|C_46|C_47|C_48|C_49|C_50|C_51|C_52|C_53|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|0|2016-01-01 00:00:00|0.014393|-0.048047|-0.401312|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|1|2016-01-01 00:01:00|0.011807|-0.045453|-0.403548|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|2|2016-01-01 00:02:00|-0.002340|-0.022322|-0.413243|0.000000|0.000000|0.000000|0.000000|0.000000|0.000000|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|3277437|2023-05-02 23:57:00|-0.081594|0.166464|0.005021|0.000510|0.000146|0.004668|0.001354|0.002483|0.000125|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|3277438|2023-05-02 23:58:00|-0.080446|0.154926|0.028362|0.000478|0.000146|0.007351|0.001883|0.002838|0.000163|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|
|3277439|2023-05-02 23:59:00|-0.072863|0.142389|0.031569|0.001352|0.000146|0.006732|0.001265|0.001409|0.000125|...|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|0.0|

[6 rows x 54 columns]

## Missing days

There are no satellite data in 3 periods
|From       | to     |
|-----------|--------|
|04-01-2016|30-06-2021|
|28-06-2019|24-02-2020|
|03-05-2023|31-08-2023|

This is the equivalent of  4256 3-hour intervals from Kp file.

## Preprocessed data file

The file to use upfront is `data_model_kp_sn_sat.csv`. it has a weight of 2130MB


---

## Dataset 
9857 files.

about the file names Pxyyy.zz or rdP199xyyy.zz 

Where 
P stands for plasma, x = 4 for 1994, x = 5 for 1995 and so on.
yyy is the day of the year (January 1=001).
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
|50M	|2008/ |380|In `temp_dir` 10 files with the same names as in the upper dir. `diff` command show they were equal. I remove it.<br /> diff temp_dir/rdP2008060.01 rdP2008060.01<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008063.01 rdP2008063.02<br /> diff temp_dir/rdP2008064.01 rdP2008064.02<br /> diff temp_dir/rdP2008065.01 rdP2008065.02<br /> diff temp_dir/rdP2008066.01 rdP2008066.03<br /> diff temp_dir/rdP2008067.01 rdP2008067.02<br /> diff temp_dir/rdP2008068.02 rdP2008068.03<br /> diff temp_dir/rdP2008069.01 rdP2008069.02 <br/> <br/> `old` file relates to day 353. as there is an rdP2008353.03 file, I remove the old file. <br/> <br/> For day 28 I found two different files on ZZ code. I keep the higher one.<br /> rm rdP2008028.01 <br />rm rdP2008035.01 <br /> rm rdP2008070.01 <br />rm rdP2008073.02 <br />rm rdP2008074.01 <br />rm rdP2008075.02<br />rm rdP2008076.01 <br />rm rdP2008080.01 <br />rm rdP2008081.01 <br />rm rdP2008082.01 <br />rm rdP2008083.01 <br />rm rdP2008220.01 <br />rm rdP2008254.01 <br />|365|
|48M	|2009/ |369|<br/> rm old <br/> rm rdP2009025.01<br/> rm rdP2009090.01<br/> rm rdP2009208.01|365|
|47M	|2010/ |367|<br/> rm old<br/> rmrdP2010271.01 |365|
|46M	|2011/ |364|Missing file for day 240 224||
|47M	|2012/ |367|Duplicated fiel for day 076. i keep higher version <br/> rm rdP20012076.01|366|
|46M	|2013/ |365||365|
|41M	|2014/ |331|Missing files for day 301..334|331|
|45M	|2015/ |364|Missing file for day 30|364|
|13M	|2016/ |117|Files for days 001..117|117|
|80K	|old/ |1|||

