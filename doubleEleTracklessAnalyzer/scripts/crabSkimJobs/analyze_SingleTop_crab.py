from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'skim_SingleTop'
config.General.workArea = 'crab_project_skim_SingleTop'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/hlt2017/CMSSW_9_0_2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/test/hltSkimDoubleEle_SingleTop.py'
config.JobType.maxMemoryMB = 2500 #should not need this option for skims

config.Data.inputDataset = '/ST_t-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW'
config.Data.inputDBS = 'global'
#config.Data.splitting = 'EventAwareLumiBased'
#use file based splitting for MC
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 15

#use userInputFiles and primaryDataset when running over a list of input files which have not been published, but are available through xrootd
#config.Data.userInputFiles = open('').readlines()
#config.Data.primaryDataset = 'SMPL_13TeV_25ns_CHNL_skim_low_dilepton_mass_region'
#True allows the jobs to run anywhere, regardless of where the input data is located
#config.Data.ignoreLocality = True

#totalUnits only needs to be specified for GEN-SIM jobs
#config.Data.totalUnits = 200000
config.Data.outLFNDirBase = '/store/group/phys_exotica/leptonsPlusJets/WR/skims/SingleTop_SKv1/'
config.Data.publication = False
#config.Data.publishDataName = 'skimmed'
config.Data.outputDatasetTag = 'SingleTop'

#a list of the only sites at which these jobs can run
#config.Site.whitelist = ["T2_US*"]
config.Site.storageSite = 'T2_CH_CERN'
