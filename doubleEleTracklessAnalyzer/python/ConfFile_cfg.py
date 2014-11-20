import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_2_0/src/doubleElectronTracklessTrigger/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_RECO_100evts.root'
		'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_10000evts.root'
        #'file:/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_2_0/src/doubleElectronTracklessTrigger/step3_DYtoEE_13TeV_25ns_40PU_FEVTDEBUGHLT_32evts.root'

    )
)

process.demo = cms.EDAnalyzer('doubleEleTracklessAnalyzer',
    #foutName = cms.string("outTreeFile.root")
)

process.TFileService = cms.Service("TFileService",
	fileName = cms.string('/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_2_0/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/analyzedTracklessEvents.root')

)


process.p = cms.Path(process.demo)
