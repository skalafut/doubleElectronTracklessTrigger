#!/bin/bash
cd /afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/CMSSW_7_3_1_patch2/src
eval `scram r -sh`
eval 'scram b -j 8'
export X509_USER_PROXY=/afs/cern.ch/user/s/skalafut/x509up_u38430 

cmsRun hlt_tracklessDoubleElectron_bkgnd_NUM.py 

