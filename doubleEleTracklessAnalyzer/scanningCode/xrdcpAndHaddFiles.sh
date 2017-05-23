#!/bin/bash

#provide a directory where many files are stored on CERN EOS
#copy these files to the local dir, hadd them together, remove the individual files
#and copy the hadd'd file back to the CERN EOS directory

#import productionTAG, skimProductionTAG and datasetFile
source configs/2017-v1.conf
mcIdentifier=(`cat $datasetFile | grep -v '#' | awk '{print $1}'`)

eosDir='root://eoscms.cern.ch//eos/cms/store/caf/user/skalafut/HLT/tuples/'
fileNameMiddle='_analyzer_trees_'
fileNameEnd='.root'

#now loop over different MC processes stored in mcIdentifier
for j in ${!mcIdentifier[*]}
do
	for q in {1..3}  #upper value must match number of files in eosDir
	do
		#copy a file from EOS to local dir
		xrdcp $eosDir${mcIdentifier[$j]}$productionTAG/${mcIdentifier[$j]}$fileNameMiddle$q$fileNameEnd .

	done
done


#for r in ${!dir[*]}
#do
#	for q in {1..21}
#	do
#		#rename the TTree files to display the WR and Nu masses
#		#mv $commonDir/${dir[$r]}/analyzedWr_$q.root $commonDir/${dir[$r]}/analyzedWr_WR_M-${wrMass[$r]}_Nu_M-${nuMass[$r]}_$q.root
#		cp $commonDir/${dir[$r]}/analyzedWr_$q.root $commonDir/${dir[$r]}/analyzedWr_WR_M-${wrMass[$r]}_Nu_M-${nuMass[$r]}_$q.root
#	
#	done
#
#	#echo "finished renaming one group of files"
#
#	#execute hadd
#	eval "hadd -k -O $commonDir/${dir[$r]}/all_analyzedWr_WR_M-${wrMass[$r]}_Nu_M-${nuMass[$r]}.root $commonDir/${dir[$r]}/analyzedWr_WR_M-${wrMass[$r]}_Nu_M-${nuMass[$r]}_*.root"
#	#echo "finished hadding one group of files"
#	
#	#move the hadd'd file to copyDir
#	mv $commonDir/${dir[$r]}/all_analyzedWr_WR_M-${wrMass[$r]}_Nu_M-${nuMass[$r]}.root $copyDir/.
#	#echo "finished copying one hadd file to copyDir"
#
#done

