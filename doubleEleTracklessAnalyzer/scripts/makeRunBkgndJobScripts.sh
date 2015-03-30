#!/bin/bash

#use q from 0 to 282 for low pT (20 to 30) QCD sample
#use q from 305 to 600 for high pT (30 to 80) QCD sample 
for q in {0..282} 
do
	#replace NUM in .sh and hlt_trackless double electron .py file
	t=$((2*q + 5210))
	y=$((2*q + 1 + 5210))

	eval "sed 's/NUM/$q/g' runHLTOnBkgnd.sh > runHLTOnBkgnd_$q.sh"
	eval "sed '${t},${y}s/#//' hlt_tracklessDoubleElectron_bkgnd.py > hlt_tracklessDoubleElectron_bkgnd_first_temp_$q.py"
	eval "sed 's/ABCDE/low/' hlt_tracklessDoubleElectron_bkgnd_first_temp_$q.py > hlt_tracklessDoubleElectron_bkgnd_temp_$q.py"
	eval "sed 's/NUM/$q/g' hlt_tracklessDoubleElectron_bkgnd_temp_$q.py > hlt_tracklessDoubleElectron_bkgnd_$q.py"
	mv hlt_tracklessDoubleElectron_bkgnd_$q.py ../CMSSW_7_3_1_patch2/src/.

	rm hlt_tracklessDoubleElectron_bkgnd_first_temp_$q.py hlt_tracklessDoubleElectron_bkgnd_temp_$q.py

done


for q in {305..600} 
do
	#replace NUM in .sh and hlt_trackless double electron .py file
	t=$((2*q + 5210))
	y=$((2*q + 1 + 5210))

	eval "sed 's/NUM/$q/g' runHLTOnBkgnd.sh > runHLTOnBkgnd_$q.sh"
	eval "sed '${t},${y}s/#//' hlt_tracklessDoubleElectron_bkgnd.py > hlt_tracklessDoubleElectron_bkgnd_first_temp_$q.py"
	eval "sed 's/ABCDE/high/' hlt_tracklessDoubleElectron_bkgnd_first_temp_$q.py > hlt_tracklessDoubleElectron_bkgnd_temp_$q.py"
	eval "sed 's/NUM/$q/g' hlt_tracklessDoubleElectron_bkgnd_temp_$q.py > hlt_tracklessDoubleElectron_bkgnd_$q.py"
	mv hlt_tracklessDoubleElectron_bkgnd_$q.py ../CMSSW_7_3_1_patch2/src/.

	rm hlt_tracklessDoubleElectron_bkgnd_first_temp_$q.py hlt_tracklessDoubleElectron_bkgnd_temp_$q.py

done


