# Data model
We use three dataset.
the general intuition behind our data model is a regression kp index with Satellite measurements and sunspots.
Kp is the dependant variable
Satelite measurements and sunspts ara the independent variables.

Considering that Kp ia a three hours calculation and DSCOVR was register on minute frequency, our model requires the concatenation of 180 records from DSCOVR.



## DSCOVR

## Sunspot
THe royal observatory of Belgium has counte sunspots since 1818. They record the count ion a daily basis in a file.
Nowadays the sunspot number is the average of the sunspot count of a certain number of observatorie

## KP
The GeoForschungsZentrum GFZ proviced The three-hour Kp index. It was developed in 1949 by Julius Bartelsand.
Kp is calculated from the K values or the geomagnetic recordings of the following 13 geomagnetic observatories:
It is designed to measure solar particle radiation by its magnetic effects and today it is considered a proxy for the energy input from the solar wind to Earth.

