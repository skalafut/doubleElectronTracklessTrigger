#!/bin/bash
#use this file with a command like
#bsub -R "pool>2000" -q 1nh -J runAnalysisDYMCPart_NNN < runAnalysisDYMC_NNN.sh
CMSSW_PROJECT_SRC=CMSSW_9_0_2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer
UP=/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/hlt2017
export X509_USER_PROXY=/afs/cern.ch/user/s/skalafut/x509up_u38430
WRITEDIR='/eos/cms/store/caf/user/skalafut/HLT/tuples/TAGNAME_SKv1'
eosReadingTag='root://eoscms.cern.ch/'

cd $UP/$CMSSW_PROJECT_SRC
eval `scramv1 runtime -sh`
#for trees with GEN matching (signal)
eval "cmsRun test/hltMinitreeWithGenMatching_TAGNAME_NUM.py"

#for trees without GEN matching (bkgnds)
#eval "cmsRun test/hltMinitreeWithoutGenMatching_TAGNAME_NUM.py"

#after the tree production finishes, move the tree file to a pre-existing directory in the my caf user space on CERN EOS
eval "xrdcp TAGNAME_analyzer_trees_NUM.root $eosReadingTag$WRITEDIR/."
rm TAGNAME_analyzer_trees_NUM.root

#for trees with GEN matching (signal)
eval "rm test/hltMinitreeWithGenMatching_TAGNAME_NUM.py"

#for trees without GEN matching (bkgnds)
#eval "rm test/hltMinitreeWithoutGenMatching_TAGNAME_NUM.py"

