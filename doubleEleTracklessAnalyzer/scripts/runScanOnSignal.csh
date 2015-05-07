#!/bin/csh

setenv HOME /eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/signal
setenv PATH /bin:/usr/bin:/usr/local/bin:/usr/krb5/bin:/usr/afsws/bin:/usr/krb5/bin/aklog

#source /uscmst1/prod/sw/cms/cshrc prod
source /cvmfs/cms.cern.ch/cmsset_default.csh prod
setenv SCRAM_ARCH slc6_amd64_gcc481

cmsrel CMSSW_7_4_0_pre9

#move input files into src/ directory
mv scanCode.tar signal_analyzer_trees_NUM_CMSSW_7_4_0_pre9_25ns_DoubleEG_22_10.root CMSSW_7_4_0_pre9/src/.

cd CMSSW_7_4_0_pre9/src/
tar -xvf scanCode.tar
rm scanCode.tar
mv signal_analyzer_trees_NUM_CMSSW_7_4_0_pre9_25ns_DoubleEG_22_10.root scanningCode/.
cd scanningCode/

#uncomment lines 16 and 17 in bin/scanning.cpp so that the scan looks for signal trees
eval "sed '16,17s@//@@' bin/scanning_temp.cpp > bin/scanning.cpp"
rm bin/scanning_temp.cpp 

cmsenv
eval `scramv1 runtime -csh`
eval 'scram b -j 8'

#run everything from scanningCode/ directory, and not the scanningCode/bin/ subdirectory
eval 'make && ./bin/scanning.exe'

mv scanned_signal_tree.root scanned_signal_tree_NUM_DoubleEG_22_10.root
mv scanned_signal_tree_NUM_DoubleEG_22_10.root $HOME/.
 
