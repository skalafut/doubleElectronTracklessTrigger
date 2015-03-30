#!/bin/bash
fileNumber=(1 2 3 4 5 6 7 8 9 10 11) 

#max q = 10   min q = 0   
for q in {0..10} 
do
	#replace NUM in .csh, job submission file, and hlt_trackless double electron .py file

	#use y and z to uncomment blocks of file names in hlt_trackless python file
	y=$((6*q+5440))
	z=$((6*q + 5 + 5440))

	eval "sed 's/NUM/${fileNumber[$q]}/g' runHLTOnSignal.sh > runHLTOnSignal_${fileNumber[$q]}.sh"
	eval "sed 's/NUM/${fileNumber[$q]}/g' hlt_tracklessDoubleElectron_signal.py > hlt_tracklessDoubleElectron_signal_temp.py"
	eval "sed '${y},${z}s/#//' hlt_tracklessDoubleElectron_signal_temp.py > hlt_tracklessDoubleElectron_signal_${fileNumber[$q]}.py"
	mv hlt_tracklessDoubleElectron_signal_${fileNumber[$q]}.py ../CMSSW_7_3_1_patch2/src/.
	
	rm hlt_tracklessDoubleElectron_signal_temp.py

done

