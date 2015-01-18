import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        ###
		#for accessing files with absolute path names
		#'file:myfile.root'
		###

		#accessing AODSIM DY->ee files via xrootd
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/00000/58AE190A-E46B-E311-84A9-00266CFFA5AC.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/00000/5C931CCA-4270-E311-A365-00266CF32920.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/00000/8CAAC606-E16C-E311-A732-003048C69328.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/129FCD8E-E86A-E311-9B54-002481E10D3E.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/54199612-DB6A-E311-95E8-0025904FE658.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/54D89312-F16A-E311-B6D1-003048C68A98.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/5883D09D-E86A-E311-B7B3-0025904B0FE4.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/96DB3740-E96A-E311-B87C-003048D4DEAE.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/9C9DCDF8-F06A-E311-BBE4-0025904B0FB4.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/9EE55710-646B-E311-B674-00266CF32E78.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/A4B35998-F26A-E311-857A-002481E0D50C.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/B2F87F6E-E96A-E311-A218-002481E0DDBE.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/C0CD8BAE-F66A-E311-B71E-00266CF25E44.root',
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/C4F46EDA-E46A-E311-B9B7-00266CFFB868.root',
		
		##BAD file, causes segfault at evt num 80144
		#'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/CA703AD5-F16A-E311-B62A-0025901D4936.root',
		
		'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/DC0B23D9-E46A-E311-B9E4-0025907DC9B0.root',
		'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/E29B1CD8-F16A-E311-AE23-0025907BAD4A.root',
		'root://xrootd.ba.infn.it//store/mc/Fall13dr/DYToEE_Tune4C_13TeV-pythia8/AODSIM/tsg_PU40bx25_POSTLS162_V2-v1/20000/EE2BE2F9-F06A-E311-A3A3-0025907BAD4A.root'


    )
)

process.demo = cms.EDAnalyzer('doubleEleAODAnalyzer'
)

process.TFileService = cms.Service("TFileService",
	#fileName = cms.string('trial.root')
	fileName = cms.string('/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_additional_evts_after_80143_AOD_data.root')
	
)

process.p = cms.Path(process.demo)
