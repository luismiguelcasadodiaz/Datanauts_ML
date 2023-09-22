[back to README](https://github.com/luismiguelcasadodiaz/Helio_Sentinel_Crew/tree/main)
# Data cleaning
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
|12M	|1994/ |47|||
|103M	|1995/ |368|||
|101M	|1996/ |366|||
|107M	|1997/ |368|||
|91M	|1998/ |365|||
|72M	|1999/ |354|||
|46M	|2000/ |358|||
|48M	|2001/ |365|||
|50M	|2002/ |367|||
|45M	|2003/ |366|||
|46M	|2004/ |367|||
|50M	|2005/ |365|||
|50M	|2006/ |362|||
|52M	|2007/ |366|||
|50M	|2008/ |380|In `temp_dir` 10 files with same names than in upper dir. `diff` command show they were equal. I remove it.<br /> diff temp_dir/rdP2008060.01 rdP2008060.01<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008063.01 rdP2008063.02<br /> diff temp_dir/rdP2008064.01 rdP2008064.02<br /> diff temp_dir/rdP2008065.01 rdP2008065.02<br /> diff temp_dir/rdP2008066.01 rdP2008066.03<br /> diff temp_dir/rdP2008067.01 rdP2008067.02<br /> diff temp_dir/rdP2008068.02 rdP2008068.03<br /> diff temp_dir/rdP2008069.01 rdP2008069.02 <br/> <br/> òld`file relates to day 353. as ther is an rdP2008353.03 file, I remove olf file. <br/> <br/> for days 28 i found two diffent files on zz code. I keep the higher one.<br /> rm rdP2008028.01 <br />rm rdP2008035.01 <br /> rm rdP2008070.01 <br />rm rdP2008073.02 <br />rm rdP2008074.01 <br />rm rdP2008075.02<br />rm rdP2008076.01 <br />rm rdP2008080.01 <br />rm rdP2008081.01 <br />rm rdP2008082.01 <br />rm rdP2008083.01 <br />rm rdP2008220.01 <br />rm rdP2008254.01 <br />|379|
|48M	|2009/ |369|||
|47M	|2010/ |367|||
|46M	|2011/ |364|||
|47M	|2012/ |367|||
|46M	|2013/ |365|||
|41M	|2014/ |331|||
|45M	|2015/ |364|||
|13M	|2016/ |117|||
|80K	|old/ |1|||

