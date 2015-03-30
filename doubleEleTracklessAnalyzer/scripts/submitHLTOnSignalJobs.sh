#!/bin/bash
fileNumber=(1 2 3 4 5 6 7 8 9 10 11) 

for q in {0..10} 
do
	eval 'bsub -R "pool>30000" -q 1nd -J sigTuplesWithoutL1_${fileNumber[$q]} < runHLTOnSignal_${fileNumber[$q]}.sh'

done


