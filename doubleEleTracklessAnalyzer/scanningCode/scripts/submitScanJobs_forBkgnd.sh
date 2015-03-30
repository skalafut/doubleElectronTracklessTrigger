#!/bin/bash

for q in {0..282} 
do
	eval 'bsub -R "pool>20000" -q 1nd -J bkgndTuplesWithoutL1_$q < runHLTOnBkgnd_$q.sh'

done

for q in {305..600} 
do
	eval 'bsub -R "pool>20000" -q 1nd -J bkgndTuplesWithoutL1_$q < runHLTOnBkgnd_$q.sh'

done


