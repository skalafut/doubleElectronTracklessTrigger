import FWCore.ParameterSet.Config as cms

process = cms.Process("OWNPARTICLES")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        #'file:myfile.root'
		'file:/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/omit.root'
	
    )
)

process.recoZeeFilter = cms.EDFilter("CandViewCountFilter",
		src = cms.InputTag("combRecoEle"),
		minNumber = cms.uint32(1)
		)

process.myProducerLabel = cms.EDProducer('SeparateCombCandidate',
		zedLabel = cms.InputTag("combRecoEle"),
		#tracklessHltEle = cms.InputTag("hltEgammaCandidatesUnseeded","","TEST"),
		#trackedHltEle = cms.InputTag("hltEgammaCandidates","","TEST"),
		tracklessHltEle = cms.InputTag("hltEgammaCandidatesUnseeded"),
		trackedHltEle = cms.InputTag("hltEgammaCandidates"),
		tracklessEleCollectionName = cms.string("tracklessDaughters"),
		trackedEleCollectionName = cms.string("trackedDaughters")

		)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('myOutputFile.root')
)

  
process.p = cms.Path(process.recoZeeFilter*process.myProducerLabel)

process.e = cms.EndPath(process.out)
