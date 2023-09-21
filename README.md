# Helio_Sentinel_Crew
Nasa Apps Challenge 2023 Develop the Oracle of DSCOVR (**D**eep **S**pace **C**limate **O**bser**v**ato**r**y


 ## Challenge:
 - Use the "raw" data from DSCOVR—faults and all— as input to predict geomagnetic storms on Earth. 
 - Create your own geomagnetic activity forecast
 - Train a neural network on DSCOVR data to forecast the Planetary K-index (Kp).

 DSCOVR measures the **strength** and **speed** of the solar wind in space, which enables us to predict **geomagnetic** storms.

 Ariana: I understand that  kp = f(st, sp).  Where st stands for wind strength, sp stands for Speed, and kp stands for Plenetary K-index or strnght of the geomagnetic storm

 DSCOVR, produces occasional faults that may themselves be indicators of space weather.  ????

 ## One possible approach to solve this challenge:
 This challenge is a natural application for an adaptive neural network (ANN) (Machine learning regression)

 ## Sources of data
 ### proton files 1994..2016 
 - [MIT Space Plasma Group](https://web.mit.edu/space/www/wind/wind_data.html)
 - ftp://space.mit.edu/pub/plasma/wind/kp_files/
   This data set has about 9000 Files (one per day each Missio day. Each file has 360 records of 15 fields each.
#### Fields

  - year  
  - day (January 1 = 1) 
  - fraction_of_day  
  - speed (km/s)  
  - E/W_angle (deg) see below 
  - N/S_angle (deg) see below 
  - proton_density (#/cc) 
  - most probable proton_thermal_speed (km/s)  {=sqrt[2kT/Mp] }  
  - alpha_% = 100*(alpha number dens)/(proton number dens) 
       {fill value (-1.e+31) if not available} 
       {This quantity will be added in future analyses.}
  - Vx (km/s)  (velocity component in GSE)  
  - Vy (km/s)  (velocity component in GSE )
  - Vz (km/s)  (velocity component in GSE)
  - XSE (Re) s/c position
  - YSE (Re) s/c position
  - ZSE (Re) s/c position

### Solar images
[**So**lar & **H**eliospheric **O**bservatory mission -- SOHO --](https://www.nasa.gov/mission_pages/soho/index.html) 

[THE ACE SCIENCE CENTER](https://izw1.caltech.edu/ACE/ASC/)
[SPACE WEATHER PREDICTION CENTER NATIONAL OCEANIC AND ATMOSPHERIC ADMINISTRATION](https://www.swpc.noaa.gov/products/lasco-coronagraph)
