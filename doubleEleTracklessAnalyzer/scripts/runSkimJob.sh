#!/bin/bash
#use this file with a command like
#bsub -R "pool>2000" -q 1nh -J runAnalysisDYMCPart_NNN < runAnalysisDYMC_NNN.sh
CMSSW_PROJECT_SRC=CMSSW_9_0_2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer
UP=/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/hlt2017
export X509_USER_PROXY=/afs/cern.ch/user/s/skalafut/x509up_u38430
WRITEDIR='/eos/cms/store/caf/user/skalafut/HLT/skims/TAGNAME_SKv1'
eosReadingTag='root://eoscms.cern.ch/'

cd $UP/$CMSSW_PROJECT_SRC
eval `scramv1 runtime -sh`
eval "cmsRun test/hltSkimDoubleEle_TAGNAME_NNN.py"

#after the skim finishes, move the skim file to a pre-existing directory in the WR group space on eos
eval "xrdcp TAGNAME_skimPartNNN.root $eosReadingTag$WRITEDIR/."
rm TAGNAME_skimPartNNN.root

