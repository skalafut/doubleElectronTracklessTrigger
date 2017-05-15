#!/bin/bash
#run this script from one dir above scripts/

#import productionTAG, skimProductionTAG and datasetFile
source configs/2017-v1.conf

##for all datasets in configs/missing_datasets.dat
##first get all the dataset short names, and save them to a vector
mcIdentifier=(`cat $datasetFile | grep -v '#' | awk '{print $1}'`)
fileTag='SkimFiles.txt'

#these are the dummy names of different input files in the python executable in test/
placeholderFileNames=('FILEA' 'FILEB' 'FILEC' 'FILED' 'FILEE' 'FILEF' 'FILEG' 'FILEH' 'FILEI' 'FILEJ' 'FILEK' 'FILEL' 'FILEM' 'FILEN' 'FILEO' 'FILEP' 'FILEQ' 'FILER' 'FILES' 'FILET' 'FILEU' 'FILEV' 'FILEW' 'FILEX' 'FILEY' 'FILEZ')

#use these two variables to control the submission of jobs
#if too many jobs are running at the same time the local disk space quota
#will be exceeded, and the jobs will fail
maxRunningJobs=100
numSubmitted=0

#now loop over all elements in mcIdentifier
for j in ${!mcIdentifier[*]}
do
	#number used to distinguish different jobs processing the same dataset
	startingCount=1
	fileListIndex=0

	###now get all the files from the dataset linked to mcIdentifier
	fileList=(`cat configs/${mcIdentifier[$j]}$fileTag`)
	fileListLength=${#fileList[@]}

	while [ $fileListIndex -lt $fileListLength ]
	do
		#move into test dir, copy the python file used to make trees, and replace NUM with an int and TAGNAME with the process name, like QCD_emenr_pt30to50 
		eval "cd test"
		#use hltMinitreeWithoutGenMatching.py for QCD, and hltMinitreeWithGenMatching.py for DY
		eval "sed 's@NUM@$startingCount@g' hltMinitreeWithGenMatching.py > tempOne.py"
		eval "sed 's@TAGNAME@${mcIdentifier[$j]}@g' tempOne.py > tempTwo.py"

		#now fill the python file used to make trees with path names to real input files
		for i in ${!placeholderFileNames[*]}
		do
			#no more than 27 input files can be added to the python file used to make trees
			#leave this loop before trying to add a 28th file
			if [ $fileListIndex -eq $fileListLength ]
			then
				break
			fi

			eval "sed -i 's@${placeholderFileNames[$i]}@${fileList[$fileListIndex]}@' tempTwo.py"

			let fileListIndex=fileListIndex+1
		done
		#use hltMinitreeWithoutGenMatching.py for QCD, and hltMinitreeWithGenMatching.py for DY
		eval "mv tempTwo.py hltMinitreeWithGenMatching_${mcIdentifier[$j]}_${startingCount}.py"

		rm tempOne.py

		#leave test dir
		eval "cd .."

		#update runOptimizationTreesJob.sh
		eval "cd scripts"
		eval "sed 's@NUM@$startingCount@g' runOptimizationTreesJob.sh > tempOne.sh"
		eval "sed 's@TAGNAME@${mcIdentifier[$j]}@g' tempOne.sh > runOptimizationTreesJob_${mcIdentifier[$j]}_${startingCount}.sh"
		eval "chmod u+x runOptimizationTreesJob_${mcIdentifier[$j]}_${startingCount}.sh"
		rm tempOne.sh

		#submit the job from scripts/ dir
		echo "bsub -R 'pool>3500' -q 8nh -J runOptimizationTreesJob_${mcIdentifier[$j]}_Part_${startingCount} < runOptimizationTreesJob_${mcIdentifier[$j]}_${startingCount}.sh"
		eval "bsub -R 'pool>3500' -q 8nh -J runOptimizationTreesJob_${mcIdentifier[$j]}_Part_${startingCount} < runOptimizationTreesJob_${mcIdentifier[$j]}_${startingCount}.sh"
		
		#move back to one dir above scripts/
		eval "cd .."

		let startingCount=startingCount+1
		let numSubmitted=numSubmitted+1
		#clean up core dumps regularly
		#eval "rm core.*"
		#eval "rm scripts/core.*"

		if [ $numSubmitted -ge $maxRunningJobs ]; then
			let numSubmitted=0
			eval "sleep 5m"
		fi

	done

done

