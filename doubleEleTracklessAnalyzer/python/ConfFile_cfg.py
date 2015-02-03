import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) ) 

process.options = cms.untracked.PSet(
	wantSummary = cms.untracked.bool(True)
)

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		#'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_low_thresholds_1000evts.root'

		'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signalTest.root'
		#DY->ee files
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_1.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_10.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_11.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_2.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_3.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_4.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_5.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_6.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_7.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_8.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_9.root',


		#Neutrino gun with 40 PU files
		
		#the files _5, _6, and _7 each have 1 event which fires both legs of the trackless double electron trigger
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_5.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_6.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_7.root',
		#
		#
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_1.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_10.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_2.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_3.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_4.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_8.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/minBiasWithHLT/outputFULL_MinBias_13TeV_25ns_40PU_RAW_to_HLTObjects_9.root',

    )
)

process.demo = cms.EDAnalyzer('doubleEleTracklessAnalyzer',
    #foutName = cms.untracked.string("testTreeFile.root")
)

process.TFileService = cms.Service("TFileService",
	fileName = cms.string('experiment.root')
	#fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_ALLevts_very_loose_trackless_leg.root')
	#fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/bkgnd_ALLevts_very_loose_trackless_leg.root')
	#fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/unmatched_signal_ALLevts_very_loose_trackless_leg.root')
	
)


process.p = cms.Path(process.demo)
