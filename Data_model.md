# Data model

We use three dataset.
the general intuition behind our data model is a regression kp index with Satellite measurements and sunspots.
Kp is the dependant variable
Satelite measurements and sunspts ara the independent variables.

Considering that Kp ia a three hours calculation and DSCOVR was register on minute frequency, our model requires the concatenation of 180 records from DSCOVR.

### DSCOVR

Satelitte measurements are recorded each minute. They are kept in a file for year.

     283680 dsc_fc_summed_spectra_2016_v01.csv
     525600 dsc_fc_summed_spectra_2017_v01.csv
     537120 dsc_fc_summed_spectra_2018_v01.csv
     256320 dsc_fc_summed_spectra_2019_v01.csv
     447840 dsc_fc_summed_spectra_2020_v01.csv
     525600 dsc_fc_summed_spectra_2021_v01.csv
     525600 dsc_fc_summed_spectra_2022_v01.csv
     175680 dsc_fc_summed_spectra_2023_v01.csv
	3277440 total


### Sunspot
The royal observatory of Belgium has counte sunspots since 1818. They record the count ion a daily basis in a file.
Nowadays the sunspot number is the average of the sunspot count of a certain number of observatorie

### KP
The GeoForschungsZentrum GFZ proviced The three-hour Kp index. It was developed in 1949 by Julius Bartelsand.
Kp is calculated from the K values or the geomagnetic recordings of the following 13 geomagnetic observatories:
It is designed to measure solar particle radiation by its magnetic effects and today it is considered a proxy for the energy input from the solar wind to Earth.
[data source](https://kp.gfz-potsdam.de/en/data)
Then select date range and Geomagnetic indice option.

[ftp_server](ftp://ftp.gfz-potsdam.de/pub/home/obs/Kp_ap_Ap_SN_F107/)


## Training

#### Split

There is a [script to split](https://github.com/luismiguelcasadodiaz/Helio_Sentinel_Crew/blob/main/src/train/split.py) dataset and save them. Splitting the data set takes time. we prefered to split one time and save the 6 dataframes on disk
train (x, y), test (x, y) val (x, y)

#### Train LR
After reading from files the splitted datasets the [script to train LR](https://github.com/luismiguelcasadodiaz/Helio_Sentinel_Crew/blob/main/src/train/train_LR.py)
makes a basic Linear regression

```python
linear_reg = LinearRegression()
linear_reg.fit(X_train, Y_train)

evaluation = model_evaluation(linear_reg, X_val, Y_val, 'Linear Reg.')
print(evaluation)
```

#### Train RNN (Pending of debuging)

After reading from files the splitted datasets the [script to train RNN](https://github.com/luismiguelcasadodiaz/Helio_Sentinel_Crew/blob/main/src/train/train_RNN.py) configures a basic sequential two layers of 180 neurons RNN with an input shape of 9540 parameters

```python
model = Sequential([
    Dense(180, activation='relu', input_shape=(X_train.shape[1],)),
    Dense(180, activation='relu'),
    Dense(1, activation='sigmoid'),
])
```
