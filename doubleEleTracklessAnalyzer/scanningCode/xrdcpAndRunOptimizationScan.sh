#!/bin/bash

#start in the directory above scanningCode/

#copy files from EOS to local dir
#for each file copied from EOS, run the scanning optimization code, rename
#the output file and move it to a directory with other scan output files

#import productionTAG, skimProductionTAG and datasetFile
source configs/2017-v1.conf
mcIdentifier=(`cat $datasetFile | grep -v '#' | awk '{print $1}'`)

eosDir='root://eoscms.cern.ch//eos/cms/store/caf/user/skalafut/HLT/tuples/'
fileNameMiddle='_analyzer_trees_'
fileNameEnd='.root'
resultsDir='scanResultTrees'

#now loop over different MC processes stored in mcIdentifier
for j in ${!mcIdentifier[*]}
do
	eval "cd scanningCode/"

	for q in {1..10}  #upper value must match number of files in eosDir
	do
		#copy a file from EOS to local dir
		xrdcp $eosDir${mcIdentifier[$j]}$productionTAG/${mcIdentifier[$j]}$fileNameMiddle$q$fileNameEnd .
		eval "./bin/scanning.exe"

		#once scan finishes, rename root file produced by optimization scan and move it to the results directory
		#delete the input file used by the scan
		eval "mv scanned_bkgnd_tree.root scanned_${mcIdentifier[$j]}_tree_${q}.root"
		eval "mv scanned_${mcIdentifier[$j]}_tree_${q}.root $resultsDir/."
		eval "rm ${mcIdentifier[$j]}_*.root"

	done
	
	eval "cd .."

done

