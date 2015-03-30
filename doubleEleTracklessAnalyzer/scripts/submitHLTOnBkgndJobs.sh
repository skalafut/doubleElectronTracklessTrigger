#!/bin/bash

for q in {0..112} 
do
	eval 'bsub -R "pool>30000" -q 1nd -J bkgndTuplesWithoutL1_$q < runHLTOnBkgnd_$q.sh'

done

for q in {122..240} 
do
	eval 'bsub -R "pool>30000" -q 1nd -J bkgndTuplesWithoutL1_$q < runHLTOnBkgnd_$q.sh'

done


