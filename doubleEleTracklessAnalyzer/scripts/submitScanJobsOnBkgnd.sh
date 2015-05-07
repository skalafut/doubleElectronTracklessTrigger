#!/bin/bash

# low pt (20 to 30)
for q in {0..282} 
do
	eval 'condor_submit request_disk=5000000 request_memory=2500 bkgndScanJobSubmissionFile_$q'

done

# high pt (30 to 80)
for q in {305..600} 
do
	eval 'condor_submit request_disk=5000000 request_memory=2500 bkgndScanJobSubmissionFile_$q'

done

# very high pt (80 to 170)
for q in {603..977} 
do
	eval 'condor_submit request_disk=5000000 request_memory=2500 bkgndScanJobSubmissionFile_$q'

done



