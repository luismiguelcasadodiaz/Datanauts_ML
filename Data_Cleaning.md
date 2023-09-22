[back to README](https://github.com/luismiguelcasadodiaz/Helio_Sentinel_Crew/tree/main)
# Data cleaning
## Dataset 
9857 files.

### Is there one file per day?
```bash
#! /bin/bash

for dir in $(ls -d */); do
	files=$(ls $dir -1 | wc)
	size=$(du -hs $dir)
	echo " $dir $files $size "
done
```


|Size| DIR   | Files|
|-----|------|------|
|12M	|1994/ |47|
|103M	|1995/ |368|
|101M	|1996/ |366|
|107M	|1997/ |368|
|91M	|1998/ |365|
|72M	|1999/ |354|
|46M	|2000/ |358|
|48M	|2001/ |365|
|50M	|2002/ |367|
|45M	|2003/ |366|
|46M	|2004/ |367|
|50M	|2005/ |365|
|50M	|2006/ |362|
|52M	|2007/ |366|
|50M	|2008/ |380|
|48M	|2009/ |369|
|47M	|2010/ |367|
|46M	|2011/ |364|
|47M	|2012/ |367|
|46M	|2013/ |365|
|41M	|2014/ |331|
|45M	|2015/ |364|
|13M	|2016/ |117|
|80K	|old/ |1|

