#!/bin/bash

#max q equals 22, min q equals 1
for q in {1..22} 
do
	eval 'condor_submit request_disk=8000000 request_memory=2500 signalScanJobSubmissionFile_$q'

done

#3, 6, 8, and 18 finished successfully
#all others btwn 1 and 22 did not
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_1'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_2'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_4'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_5'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_7'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_9'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_10'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_11'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_12'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_13'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_14'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_15'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_16'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_17'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_19'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_20'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_21'
#eval 'condor_submit request_disk=15000000 request_memory=25000 signalScanJobSubmissionFile_22'


