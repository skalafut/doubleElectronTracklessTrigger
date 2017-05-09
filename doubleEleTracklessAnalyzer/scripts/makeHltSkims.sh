#!/bin/bash
#run this script from one dir above scripts/

#import productionTAG, skimProductionTAG and datasetFile
source configs/2017-v1.conf

##for all datasets in configs/missing_datasets.dat
##first get all the dataset short names, and save them to a vector
mcIdentifier=(`cat $datasetFile | grep -v '#' | awk '{print $1}'`)
fileTag='Files.txt'

#these are the dummy names of different input files in the hltSkim...py executable
#placeholderFileNames=('FILEA' 'FILEB' 'FILEC' 'FILED' 'FILEE' 'FILEF' 'FILEG' 'FILEH' 'FILEI' 'FILEJ' 'FILEK' 'FILEL' 'FILEM' 'FILEN' 'FILEO' 'FILEP' 'FILEQ' 'FILER' 'FILES' 'FILET' 'FILEU' 'FILEV' 'FILEW' 'FILEX' 'FILEY' 'FILEZ' 'FILE0' 'FILE1' 'FILE2' 'FILE3' 'FILE4' 'FILE5' 'FILE6' 'FILE7' 'FILE8' 'FILE9' 'FILEa' 'FILEb' 'FILEc' 'FILEd' 'FILEe' 'FILEf' 'FILEg' 'FILEh' 'FILEi' 'FILEj' 'FILEk')
placeholderFileNames=('FILEA')

placeholderLength=${#placeholderFileNames[@]}

#use these two variables to control the submission of jobs
#if too many jobs are running at the same time the local disk space quota
#will be exceeded, and the jobs will fail
maxRunningJobs=20
numSubmitted=0

#now loop over all elements in mcIdentifier
for j in ${!mcIdentifier[*]}
do
	#number used to distinguish different jobs processing the same dataset
	startingCount=1
	fileListIndex=0

	###now get all the files from the dataset linked to mcIdentifier
	fileList=(`cat ${mcIdentifier[$j]}$fileTag`)
	fileListLength=${#fileList[@]}

	while [ $fileListIndex -lt $fileListLength ]
	do
		#move into test dir
		eval "cd test"
		eval "sed 's@PartNNN@Part$startingCount@g' hltSkimDoubleEle.py > tempOne.py"
		eval "sed 's@TAGNAME@${mcIdentifier[$j]}@g' tempOne.py > tempTwo.py"

		#now loop over all elements in placeholderFileNames, and replace each element with a full path to a real file

		for i in ${!placeholderFileNames[*]}
		do
			#leave this loop if fileListIndex is equal to fileListLength
			if [ $fileListIndex -eq $fileListLength ]
			then
				break
			fi

			eval "sed -i 's@${placeholderFileNames[$i]}@${fileList[$fileListIndex]}@' tempTwo.py"

			let fileListIndex=fileListIndex+1
		done
		eval "mv tempTwo.py hltSkimDoubleEle_${mcIdentifier[$j]}_${startingCount}.py"

		rm tempOne.py

		#leave test dir
		eval "cd .."

		#update runSkimJob.sh
		eval "cd scripts"
		eval "sed 's@NNN@$startingCount@g' runSkimJob.sh > tempOne.sh"
		eval "sed 's@TAGNAME@${mcIdentifier[$j]}@g' tempOne.sh > runSkimJob_${mcIdentifier[$j]}_${startingCount}.sh"
		eval "chmod u+x runSkimJob_${mcIdentifier[$j]}_${startingCount}.sh"
		rm tempOne.sh

		#submit the job from scripts/ dir
		#echo "bsub -R 'pool>1500' -q 1nh -J runSkimJob_${mcIdentifier[$j]}_Part_${startingCount} < runSkimJob_${mcIdentifier[$j]}_${startingCount}.sh"
		eval "bsub -R 'pool>1500' -q 1nh -J runSkimJob_${mcIdentifier[$j]}_Part_${startingCount} < runSkimJob_${mcIdentifier[$j]}_${startingCount}.sh"
		
		#move back to one dir above scripts/
		eval "cd .."

		let startingCount=startingCount+1
		let numSubmitted=numSubmitted+1
		#clean up core dumps regularly
		eval "rm core.*"
		eval "rm scripts/core.*"

		if [ $numSubmitted -ge $maxRunningJobs ]; then
			let numSubmitted=0
			eval "sleep 35m"
		fi

	done

done

