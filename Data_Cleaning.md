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
|46M	|2004/ |388|||
|50M	|2005/ |395|||
|50M	|2006/ |406|||
|52M	|2007/ |422|||
|50M	|2008/ |380|In `temp_dir` 10 files with same names than in upper dir. `diff` command show they were equal. I remove it.<br /> diff temp_dir/rdP2008060.01 rdP2008060.01<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008062.01 rdP2008062.02<br /> diff temp_dir/rdP2008063.01 rdP2008063.02<br /> diff temp_dir/rdP2008064.01 rdP2008064.02<br /> diff temp_dir/rdP2008065.01 rdP2008065.02<br /> diff temp_dir/rdP2008066.01 rdP2008066.03<br /> diff temp_dir/rdP2008067.01 rdP2008067.02<br /> diff temp_dir/rdP2008068.02 rdP2008068.03<br /> diff temp_dir/rdP2008069.01 rdP2008069.02 <br/> <br/> `old` file relates to day 353. as ther is an rdP2008353.03 file, I remove olf file. <br/> <br/> for days 28 i found two diffent files on zz code. I keep the higher one.<br /> rm rdP2008028.01 <br />rm rdP2008035.01 <br /> rm rdP2008070.01 <br />rm rdP2008073.02 <br />rm rdP2008074.01 <br />rm rdP2008075.02<br />rm rdP2008076.01 <br />rm rdP2008080.01 <br />rm rdP2008081.01 <br />rm rdP2008082.01 <br />rm rdP2008083.01 <br />rm rdP2008220.01 <br />rm rdP2008254.01 <br />|365|
|48M	|2009/ |369|<br/> rm old <br/> rmrdP2009025.01<br/> rmrdP2009090.01<br/> rmrdP2009208.01|365|
|47M	|2010/ |367|<br/> rm old<br/> rmrdP2010271.01 |365|
|46M	|2011/ |364|Missing file for day 240 224||
|47M	|2012/ |367|Duplicated fiel for day 076. i keep higher version <br/> rm rdP20012076.01|366|
|46M	|2013/ |365||365|
|41M	|2014/ |331|Missing files for day 301..334|331|
|45M	|2015/ |364|Missing file for day 30|364|
|13M	|2016/ |117|Files for days 001..117|117|
|80K	|old/ |1|||

