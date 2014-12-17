import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
		'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_10000evts.root'

		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_1.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_10.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_11.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_12.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_13.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_14.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_15.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_16.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_17.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_18.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_19.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_2.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_20.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_21.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_22.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_3.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_4.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_5.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_6.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_7.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_8.root',
		#'root://cmsxrootd.fnal.gov//store/user/skalafut/doubleElectronHLT/rawWithHLT/outputFULL_DYtoEE_13TeV_25ns_40PU_RAW_to_HLTObjects_9.root',


    )
)

process.demo = cms.EDAnalyzer('doubleEleTracklessAnalyzer',
    #foutName = cms.untracked.string("testTreeFile.root")
)

process.TFileService = cms.Service("TFileService",
	fileName = cms.string('test_signal.root')
	
)


process.p = cms.Path(process.demo)
