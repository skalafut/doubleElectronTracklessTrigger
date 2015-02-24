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
		#'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signalTest_contains_HLT_objects.root'
		#'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/Test_signal_contains_HLT_objects.root'
		#'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_sample_with_HLT_objects.root'
		#
		#this input file contains collections made by the modules combEle,
		#combRecoEle, and myProducerLabel (which separates the daughters of
		#reco Z objects)
		'file:/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/SeparateCombCandidate/myOutputFile.root'
		

		#DY->ee files
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_1.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_10.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_11.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_2.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_3.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_4.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_5.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_6.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_7.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_8.root',
		#'root://cms-xrd-global.cern.ch//store/user/skalafut/doubleElectronHLT/dyToEEWithHLT/outputFULL_DYtoEE_13TeV_M_50_25ns_40PU_RAW_to_HLTObjects_9.root',

    )
)

process.recoAnalyzerTracked = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedSignal"),
		recoElectronCollection = cms.InputTag("myProducerLabel","trackedDaughters","OWNPARTICLES"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1)
	
		)


process.recoAnalyzerTrackless = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessSignal"),
		recoElectronCollection = cms.InputTag("myProducerLabel","tracklessDaughters","OWNPARTICLES"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1)
	
		)

process.recoAnalyzerMatchedTracked = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersMatchedTrackedSignal"),
		recoElectronCollection = cms.InputTag("myProducerLabel","trackedDaughters","OWNPARTICLES"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("genEleTrack","","TEST"),
		dRMatch = cms.double(0.1)
		
		)


process.recoAnalyzerMatchedTrackless = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersMatchedTracklessSignal"),
		recoElectronCollection = cms.InputTag("myProducerLabel","tracklessDaughters","OWNPARTICLES"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("genUntrack","","TEST"),
		dRMatch = cms.double(0.1)
	
		)



#these two modules aren't needed.  I can do the same work in the plugin recoAnalyzerGeneric
#with less code.  Using these modules would require me to make my own EDFilter (but a very basic one)
#and an analyzer plugin which is very similar to recoAnalyzerGeneric, but only analyzes
#the RecoEcalCandidate objects which are matched to GEN electrons.
#the TrivialDeltaRViewMatcher module produces a map 
#run these two modules after applying the recoZeeFilter and ZeeFilter (gen requirements) 
#process.trackedRecoToGenMatching = cms.EDProducer("TrivialDeltaRViewMatcher",
#		src = cms.InputTag("myProducerLabel","trackedDaughters","OWNPARTICLES"),
#		matched = cms.InputTag("genEleTrack","","TEST"),
#		distMin = cms.double(0.1)
#
#		)

#process.tracklessRecoToGenMatching = cms.EDProducer("TrivialDeltaRViewMatcher",
#		src = cms.InputTag("myProducerLabel","tracklessDaughters","OWNPARTICLES"),
#		matched = cms.InputTag("genUntrack","","TEST"),
#		distMin = cms.double(0.1)
#
#		)


#enforces all of the GEN level Z->ee requirements (tracked e- + trackless e-, sufficient dilepton mass)
process.ZeeFilter = cms.EDFilter("CandViewCountFilter",
		src = cms.InputTag("combEle","","TEST"),
		minNumber = cms.uint32(1)
		)


process.TFileService = cms.Service("TFileService",
	fileName = cms.string('trialGenericRecoAnalyzer.root')
	#fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_ALLevts_very_loose_trackless_leg.root')
	#fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/bkgnd_ALLevts_very_loose_trackless_leg.root')
	#fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/unmatched_signal_ALLevts_very_loose_trackless_leg.root')
	
)

process.p = cms.Path(
		process.recoAnalyzerTracked
		+process.recoAnalyzerTrackless
		#+process.ZeeFilter
		+process.recoAnalyzerMatchedTracked
		+process.recoAnalyzerMatchedTrackless
		)



