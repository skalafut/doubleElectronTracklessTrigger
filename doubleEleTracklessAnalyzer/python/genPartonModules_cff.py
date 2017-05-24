import FWCore.ParameterSet.Config as cms

genQuark = cms.EDFilter("CandViewSelector",
		src = cms.InputTag("genParticles"),
		cut = cms.string("abs(pdgId) < 7 && status == 23")
		)

genGluon = genQuark.clone(
		cut = cms.string("abs(pdgId) == 21 && status == 23")
		)

genPartonsSeq = cms.Sequence( genQuark+genGluon)

#CandViewMerger will work if one of the input collections is empty
mergeGenPartons = cms.EDProducer("CandViewMerger",
		src = cms.VInputTag("genQuark","genGluon")
		)

mergeGenPartonsFilter = cms.EDFilter("CandViewCountFilter",
		src = cms.InputTag("mergeGenPartons"),
		minNumber = cms.uint32(1)
		)

mergeGenPartonsSeq = cms.Sequence(mergeGenPartons+mergeGenPartonsFilter)


