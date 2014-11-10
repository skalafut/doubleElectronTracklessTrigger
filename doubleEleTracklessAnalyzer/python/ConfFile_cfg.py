import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(50) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_2_0/src/doubleElectronTracklessTrigger/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_RECO_100evts.root'
    )
)

process.demo = cms.EDAnalyzer('doubleEleTracklessAnalyzer'
)

process.TFileService = cms.Service("TFileService",
	fileName = cms.string('/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_2_0/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/analyzedTracklessEvents.root')

)


process.p = cms.Path(process.demo)
