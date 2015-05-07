#!/bin/bash

for q in {1..22} 
do
	#replace NUM in run .csh and text job submission file
	eval "sed 's/NUM/$q/g' runScanOnSignal.csh > runScanOnSignal_$q.csh"
	eval "sed 's/NUM/$q/g' signalScanJobSubmissionFile > signalScanJobSubmissionFile_$q"

done

