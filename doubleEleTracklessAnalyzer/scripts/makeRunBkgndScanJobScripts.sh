#!/bin/bash

#use q from 0 to 282 for low pT (20 to 30) QCD sample
#use q from 305 to 600 for high pT (30 to 80) QCD sample 
#use q from 603 to 977 for very high pT (80 to 170) QCD sample
for q in {0..282} 
do
	#replace ABCDE and NUM in run .csh file and job submission file
	eval "sed 's/NUM/$q/g' runScanOnBkgnd.csh > runScanOnBkgnd_temp.csh"
	eval "sed 's/ABCDE/low_pt/g' runScanOnBkgnd_temp.csh > runScanOnBkgnd_$q.csh"
	
	eval "sed 's/NUM/$q/g' bkgndScanJobSubmissionFile > bkgndScanJobSubmissionFile_temp"
	eval "sed 's/ABCDE/low_pt/g' bkgndScanJobSubmissionFile_temp > bkgndScanJobSubmissionFile_$q"

	rm runScanOnBkgnd_temp.csh bkgndScanJobSubmissionFile_temp

done


for q in {305..600} 
do
	#replace ABCDE and NUM in run .csh file and job submission file
	eval "sed 's/NUM/$q/g' runScanOnBkgnd.csh > runScanOnBkgnd_temp.csh"
	eval "sed 's/ABCDE/high_pt/g' runScanOnBkgnd_temp.csh > runScanOnBkgnd_$q.csh"
	
	eval "sed 's/NUM/$q/g' bkgndScanJobSubmissionFile > bkgndScanJobSubmissionFile_temp"
	eval "sed 's/ABCDE/high_pt/g' bkgndScanJobSubmissionFile_temp > bkgndScanJobSubmissionFile_$q"

	rm runScanOnBkgnd_temp.csh bkgndScanJobSubmissionFile_temp

done

for q in {603..977} 
do
	#replace ABCDE and NUM in run .csh file and job submission file
	eval "sed 's/NUM/$q/g' runScanOnBkgnd.csh > runScanOnBkgnd_temp.csh"
	eval "sed 's/ABCDE/very_high_pt/g' runScanOnBkgnd_temp.csh > runScanOnBkgnd_$q.csh"
	
	eval "sed 's/NUM/$q/g' bkgndScanJobSubmissionFile > bkgndScanJobSubmissionFile_temp"
	eval "sed 's/ABCDE/very_high_pt/g' bkgndScanJobSubmissionFile_temp > bkgndScanJobSubmissionFile_$q"

	rm runScanOnBkgnd_temp.csh bkgndScanJobSubmissionFile_temp

done



