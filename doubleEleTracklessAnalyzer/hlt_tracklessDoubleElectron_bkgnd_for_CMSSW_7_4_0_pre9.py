# /users/sani/AlCa_2015/V9 (CMSSW_7_2_0_pre6_HLT1)

import FWCore.ParameterSet.Config as cms

process = cms.Process( "TEST" )

process.load("setup_cff")

process.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/sani/AlCa_2015/V9')
)

process.HLTIter4PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 6 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter3PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter2PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter1PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.2 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetbJetRegionalTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetTrajectoryFilterL3 = cms.PSet( 
  minPt = cms.double( 0.5 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 1000000000 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetTrajectoryFilterForElectrons = cms.PSet( 
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  minPt = cms.double( 2.0 ),
  minHitsMinPt = cms.int32( -1 ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetMuonCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  nSigmaMinPt = cms.double( 5.0 ),
  minimumNumberOfHits = cms.int32( 5 )
)
process.HLTPSetMuTrackJpsiTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 10.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 8 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetMuTrackJpsiEffTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 1.0 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 9 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetCkfTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetCkf3HitTrajectoryFilter = cms.PSet( 
  minPt = cms.double( 0.9 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( -1 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTIter4PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter4PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter4ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  minNrOfHitsForRebuild = cms.untracked.int32( 4 )
)
process.HLTIter3PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter3PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter3ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter2PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter2ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter1PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetbJetRegionalTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetbJetRegionalTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetTrajectoryBuilderL3 = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterL3" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetTrajectoryBuilderForElectrons = cms.PSet( 
  propagatorAlong = cms.string( "hltESPFwdElectronPropagator" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryFilterForElectrons" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "hltESPBwdElectronPropagator" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 90.0 )
)
process.HLTPSetMuTrackJpsiTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuTrackJpsiEffTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuTrackJpsiEffTrajectoryFilter" ) ),
  maxCand = cms.int32( 1 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetCkf3HitTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetCkf3HitTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuonCkfTrajectoryBuilderSeedHit = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( True ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  maxCand = cms.int32( 5 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  useSeedLayer = cms.bool( False ),
  deltaEta = cms.double( -1.0 ),
  deltaPhi = cms.double( -1.0 ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  rescaleErrorIfFail = cms.double( 1.0 ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  intermediateCleaning = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTPSetPvClusterComparer = cms.PSet( 
  track_pt_min = cms.double( 2.5 ),
  track_pt_max = cms.double( 10.0 ),
  track_chi2_max = cms.double( 9999999.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTIter0PSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter0PSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 1 ),
  minimumNumberOfHits = cms.int32( 3 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetPvClusterComparerForBTag = cms.PSet( 
  track_pt_min = cms.double( 0.1 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)
process.HLTSeedFromConsecutiveHitsTripletOnlyCreator = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTSeedFromConsecutiveHitsCreator = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.HLTIter0HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 4 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( True ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 )
)
process.HLTIter2HighPtTkMuPSetTrajectoryBuilderIT = cms.PSet( 
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2HighPtTkMuPSetTrajectoryFilterIT" ) ),
  maxCand = cms.int32( 2 ),
  ComponentType = cms.string( "CkfTrajectoryBuilder" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  updator = cms.string( "hltESPKFUpdator" ),
  alwaysUseInvalidHits = cms.bool( False ),
  intermediateCleaning = cms.bool( True ),
  lostHitPenalty = cms.double( 30.0 ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" )
)
process.HLTIter2HighPtTkMuPSetTrajectoryFilterIT = cms.PSet( 
  minPt = cms.double( 0.3 ),
  minHitsMinPt = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  maxLostHits = cms.int32( 1 ),
  maxNumberOfHits = cms.int32( 100 ),
  maxConsecLostHits = cms.int32( 3 ),
  minimumNumberOfHits = cms.int32( 5 ),
  nSigmaMinPt = cms.double( 5.0 ),
  chargeSignificance = cms.double( -1.0 )
)
process.HLTPSetPvClusterComparerForIT = cms.PSet( 
  track_pt_min = cms.double( 1.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_chi2_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 )
)

process.CSCChannelMapperESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCChannelMapperRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.CSCINdexerESSource = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "CSCIndexerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.GlobalTag = cms.ESSource( "PoolDBESSource",
    globaltag = cms.string( "GR_H_V39" ),
    RefreshEachRun = cms.untracked.bool( True ),
    RefreshOpenIOVs = cms.untracked.bool( False ),
    toGet = cms.VPSet( 
      cms.PSet(  record = cms.string( "JetCorrectionsRecord" ),
        tag = cms.string( "JetCorrectorParametersCollection_HLT_V1_AK4Calo" ),
        connect = cms.untracked.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS" ),
        label = cms.untracked.string( "AK4CaloHLT" )
      ),
      cms.PSet(  record = cms.string( "JetCorrectionsRecord" ),
        tag = cms.string( "JetCorrectorParametersCollection_HLT_trk1B_V1_AK4PF" ),
        connect = cms.untracked.string( "frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS" ),
        label = cms.untracked.string( "AK4PFHLT" )
      )
    ),
    DBParameters = cms.PSet( 
      authenticationPath = cms.untracked.string( "." ),
      connectionRetrialTimeOut = cms.untracked.int32( 60 ),
      idleConnectionCleanupPeriod = cms.untracked.int32( 10 ),
      messageLevel = cms.untracked.int32( 0 ),
      enablePoolAutomaticCleanUp = cms.untracked.bool( False ),
      enableConnectionSharing = cms.untracked.bool( True ),
      enableReadOnlySessionOnUpdateConnection = cms.untracked.bool( False ),
      connectionTimeOut = cms.untracked.int32( 0 ),
      connectionRetrialPeriod = cms.untracked.int32( 10 )
    ),
    RefreshAlways = cms.untracked.bool( False ),
    connect = cms.string( "frontier://(proxyurl=http://localhost:3128)(serverurl=http://localhost:8000/FrontierOnProd)(serverurl=http://localhost:8000/FrontierOnProd)(retrieve-ziplevel=0)/CMS_CONDITIONS" ),
    ReconnectEachRun = cms.untracked.bool( True ),
    BlobStreamerName = cms.untracked.string( "TBufferBlobStreamingService" )
)
process.HepPDTESSource = cms.ESSource( "HepPDTESSource",
    pdtFileName = cms.FileInPath( "SimGeneral/HepPDTESSource/data/pythiaparticle.tbl" )
)
process.eegeom = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalMappingRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.es_hardcode = cms.ESSource( "HcalHardcodeCalibrations",
    fromDDD = cms.untracked.bool( False ),
    toGet = cms.untracked.vstring( 'GainWidths' )
)
process.hltESSBTagRecord = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "JetTagComputerRecord" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSEcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "EcalSeverityLevelAlgoRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.hltESSHcalSeverityLevel = cms.ESSource( "EmptyESSource",
    iovIsRunNotTime = cms.bool( True ),
    recordName = cms.string( "HcalSeverityLevelComputerRcd" ),
    firstValid = cms.vuint32( 1 )
)
process.magfield = cms.ESSource( "XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring( 'Geometry/CMSCommonData/data/normal/cmsextent.xml',
      'Geometry/CMSCommonData/data/cms.xml',
      'Geometry/CMSCommonData/data/cmsMagneticField.xml',
      'MagneticField/GeomBuilder/data/MagneticFieldVolumes_1103l.xml',
      'Geometry/CMSCommonData/data/materials.xml' ),
    rootNodeName = cms.string( "cmsMagneticField:MAGF" )
)

#process.trackerTopologyConstants = cms.ESProducer( "TrackerTopologyEP",
#  pxb_layerMask = cms.uint32( 15 ),
#  tib_str_int_extStartBit = cms.uint32( 10 ),
#  tib_layerMask = cms.uint32( 7 ),
#  tib_str_fw_bwStartBit = cms.uint32( 12 ),
#  pxf_bladeMask = cms.uint32( 63 ),
#  pxb_moduleStartBit = cms.uint32( 2 ),
#  pxb_ladderStartBit = cms.uint32( 8 ),
#  pxb_layerStartBit = cms.uint32( 16 ),
#  tec_wheelStartBit = cms.uint32( 14 ),
#  tib_str_fw_bwMask = cms.uint32( 3 ),
#  tec_ringStartBit = cms.uint32( 5 ),
#  tib_moduleStartBit = cms.uint32( 2 ),
#  tib_sterMask = cms.uint32( 3 ),
#  tid_sideStartBit = cms.uint32( 13 ),
#  tid_wheelStartBit = cms.uint32( 11 ),
#  tid_ringMask = cms.uint32( 3 ),
#  tid_sterMask = cms.uint32( 3 ),
#  tec_petal_fw_bwStartBit = cms.uint32( 12 ),
#  tec_ringMask = cms.uint32( 7 ),
#  tib_strMask = cms.uint32( 63 ),
#  tec_sterMask = cms.uint32( 3 ),
#  tec_sideStartBit = cms.uint32( 18 ),
#  pxb_moduleMask = cms.uint32( 63 ),
#  pxf_panelStartBit = cms.uint32( 8 ),
#  tid_sideMask = cms.uint32( 3 ),
#  tob_moduleMask = cms.uint32( 7 ),
#  tid_ringStartBit = cms.uint32( 9 ),
#  pxf_sideMask = cms.uint32( 3 ),
#  appendToDataLabel = cms.string( "" ),
#  pxf_diskStartBit = cms.uint32( 16 ),
#  tib_str_int_extMask = cms.uint32( 3 ),
#  tec_moduleMask = cms.uint32( 7 ),
#  tob_sterMask = cms.uint32( 3 ),
#  tob_rod_fw_bwMask = cms.uint32( 3 ),
#  tob_layerStartBit = cms.uint32( 14 ),
#  tec_petal_fw_bwMask = cms.uint32( 3 ),
#  tib_layerStartBit = cms.uint32( 14 ),
#  tec_sterStartBit = cms.uint32( 0 ),
#  tid_moduleMask = cms.uint32( 31 ),
#  tib_sterStartBit = cms.uint32( 0 ),
#  tid_sterStartBit = cms.uint32( 0 ),
#  pxf_moduleStartBit = cms.uint32( 2 ),
#  pxf_diskMask = cms.uint32( 15 ),
#  pxf_sideStartBit = cms.uint32( 23 ),
#  tid_module_fw_bwStartBit = cms.uint32( 7 ),
#  tob_layerMask = cms.uint32( 7 ),
#  tid_module_fw_bwMask = cms.uint32( 3 ),
#  tob_rod_fw_bwStartBit = cms.uint32( 12 ),
#  tec_petalMask = cms.uint32( 15 ),
#  pxb_ladderMask = cms.uint32( 255 ),
#  tec_moduleStartBit = cms.uint32( 2 ),
#  tec_sideMask = cms.uint32( 3 ),
#  tob_rodMask = cms.uint32( 127 ),
#  tib_strStartBit = cms.uint32( 4 ),
#  tec_wheelMask = cms.uint32( 15 ),
#  tob_rodStartBit = cms.uint32( 5 ),
#  pxf_panelMask = cms.uint32( 3 ),
#  tib_moduleMask = cms.uint32( 3 ),
#  pxf_bladeStartBit = cms.uint32( 10 ),
#  tid_wheelMask = cms.uint32( 3 ),
#  tob_sterStartBit = cms.uint32( 0 ),
#  tid_moduleStartBit = cms.uint32( 2 ),
#  tec_petalStartBit = cms.uint32( 8 ),
#  tob_moduleStartBit = cms.uint32( 2 ),
#  pxf_moduleMask = cms.uint32( 63 )
#)

#copy of module above with the module name changed to trackerTopology
#process.trackerTopology = cms.ESProducer( "TrackerTopologyEP",
#  pxb_layerMask = cms.uint32( 15 ),
#  tib_str_int_extStartBit = cms.uint32( 10 ),
#  tib_layerMask = cms.uint32( 7 ),
#  tib_str_fw_bwStartBit = cms.uint32( 12 ),
#  pxf_bladeMask = cms.uint32( 63 ),
#  pxb_moduleStartBit = cms.uint32( 2 ),
#  pxb_ladderStartBit = cms.uint32( 8 ),
#  pxb_layerStartBit = cms.uint32( 16 ),
#  tec_wheelStartBit = cms.uint32( 14 ),
#  tib_str_fw_bwMask = cms.uint32( 3 ),
#  tec_ringStartBit = cms.uint32( 5 ),
#  tib_moduleStartBit = cms.uint32( 2 ),
#  tib_sterMask = cms.uint32( 3 ),
#  tid_sideStartBit = cms.uint32( 13 ),
#  tid_wheelStartBit = cms.uint32( 11 ),
#  tid_ringMask = cms.uint32( 3 ),
#  tid_sterMask = cms.uint32( 3 ),
#  tec_petal_fw_bwStartBit = cms.uint32( 12 ),
#  tec_ringMask = cms.uint32( 7 ),
#  tib_strMask = cms.uint32( 63 ),
#  tec_sterMask = cms.uint32( 3 ),
#  tec_sideStartBit = cms.uint32( 18 ),
#  pxb_moduleMask = cms.uint32( 63 ),
#  pxf_panelStartBit = cms.uint32( 8 ),
#  tid_sideMask = cms.uint32( 3 ),
#  tob_moduleMask = cms.uint32( 7 ),
#  tid_ringStartBit = cms.uint32( 9 ),
#  pxf_sideMask = cms.uint32( 3 ),
#  appendToDataLabel = cms.string( "" ),
#  pxf_diskStartBit = cms.uint32( 16 ),
#  tib_str_int_extMask = cms.uint32( 3 ),
#  tec_moduleMask = cms.uint32( 7 ),
#  tob_sterMask = cms.uint32( 3 ),
#  tob_rod_fw_bwMask = cms.uint32( 3 ),
#  tob_layerStartBit = cms.uint32( 14 ),
#  tec_petal_fw_bwMask = cms.uint32( 3 ),
#  tib_layerStartBit = cms.uint32( 14 ),
#  tec_sterStartBit = cms.uint32( 0 ),
#  tid_moduleMask = cms.uint32( 31 ),
#  tib_sterStartBit = cms.uint32( 0 ),
#  tid_sterStartBit = cms.uint32( 0 ),
#  pxf_moduleStartBit = cms.uint32( 2 ),
#  pxf_diskMask = cms.uint32( 15 ),
#  pxf_sideStartBit = cms.uint32( 23 ),
#  tid_module_fw_bwStartBit = cms.uint32( 7 ),
#  tob_layerMask = cms.uint32( 7 ),
#  tid_module_fw_bwMask = cms.uint32( 3 ),
#  tob_rod_fw_bwStartBit = cms.uint32( 12 ),
#  tec_petalMask = cms.uint32( 15 ),
#  pxb_ladderMask = cms.uint32( 255 ),
#  tec_moduleStartBit = cms.uint32( 2 ),
#  tec_sideMask = cms.uint32( 3 ),
#  tob_rodMask = cms.uint32( 127 ),
#  tib_strStartBit = cms.uint32( 4 ),
#  tec_wheelMask = cms.uint32( 15 ),
#  tob_rodStartBit = cms.uint32( 5 ),
#  pxf_panelMask = cms.uint32( 3 ),
#  tib_moduleMask = cms.uint32( 3 ),
#  pxf_bladeStartBit = cms.uint32( 10 ),
#  tid_wheelMask = cms.uint32( 3 ),
#  tob_sterStartBit = cms.uint32( 0 ),
#  tid_moduleStartBit = cms.uint32( 2 ),
#  tec_petalStartBit = cms.uint32( 8 ),
#  tob_moduleStartBit = cms.uint32( 2 ),
#  pxf_moduleMask = cms.uint32( 63 )
#)

#from under_development hlt .py file
process.trackerTopology = cms.ESProducer( "TrackerTopologyEP",
  pxb_layerMask = cms.uint32( 15 ),
  tib_str_int_extStartBit = cms.uint32( 10 ),
  tib_layerMask = cms.uint32( 7 ),
  tib_str_fw_bwStartBit = cms.uint32( 12 ),
  pxf_bladeMask = cms.uint32( 63 ),
  pxb_moduleStartBit = cms.uint32( 2 ),
  pxb_ladderStartBit = cms.uint32( 8 ),
  pxb_layerStartBit = cms.uint32( 16 ),
  tec_wheelStartBit = cms.uint32( 14 ),
  tib_str_fw_bwMask = cms.uint32( 3 ),
  tec_ringStartBit = cms.uint32( 5 ),
  tib_moduleStartBit = cms.uint32( 2 ),
  tib_sterMask = cms.uint32( 3 ),
  tid_sideStartBit = cms.uint32( 13 ),
  tid_wheelStartBit = cms.uint32( 11 ),
  tid_ringMask = cms.uint32( 3 ),
  tid_sterMask = cms.uint32( 3 ),
  tec_petal_fw_bwStartBit = cms.uint32( 12 ),
  tec_ringMask = cms.uint32( 7 ),
  tib_strMask = cms.uint32( 63 ),
  tec_sterMask = cms.uint32( 3 ),
  tec_sideStartBit = cms.uint32( 18 ),
  pxb_moduleMask = cms.uint32( 63 ),
  pxf_panelStartBit = cms.uint32( 8 ),
  tid_sideMask = cms.uint32( 3 ),
  tob_moduleMask = cms.uint32( 7 ),
  tid_ringStartBit = cms.uint32( 9 ),
  pxf_sideMask = cms.uint32( 3 ),
  appendToDataLabel = cms.string( "" ),
  pxf_diskStartBit = cms.uint32( 16 ),
  tib_str_int_extMask = cms.uint32( 3 ),
  tec_moduleMask = cms.uint32( 7 ),
  tob_sterMask = cms.uint32( 3 ),
  tob_rod_fw_bwMask = cms.uint32( 3 ),
  tob_layerStartBit = cms.uint32( 14 ),
  tec_petal_fw_bwMask = cms.uint32( 3 ),
  tib_layerStartBit = cms.uint32( 14 ),
  tec_sterStartBit = cms.uint32( 0 ),
  tid_moduleMask = cms.uint32( 31 ),
  tib_sterStartBit = cms.uint32( 0 ),
  tid_sterStartBit = cms.uint32( 0 ),
  pxf_moduleStartBit = cms.uint32( 2 ),
  pxf_diskMask = cms.uint32( 15 ),
  pxf_sideStartBit = cms.uint32( 23 ),
  tid_module_fw_bwStartBit = cms.uint32( 7 ),
  tob_layerMask = cms.uint32( 7 ),
  tid_module_fw_bwMask = cms.uint32( 3 ),
  tob_rod_fw_bwStartBit = cms.uint32( 12 ),
  tec_petalMask = cms.uint32( 15 ),
  pxb_ladderMask = cms.uint32( 255 ),
  tec_moduleStartBit = cms.uint32( 2 ),
  tec_sideMask = cms.uint32( 3 ),
  tob_rodMask = cms.uint32( 127 ),
  tib_strStartBit = cms.uint32( 4 ),
  tec_wheelMask = cms.uint32( 15 ),
  tob_rodStartBit = cms.uint32( 5 ),
  pxf_panelMask = cms.uint32( 3 ),
  tib_moduleMask = cms.uint32( 3 ),
  pxf_bladeStartBit = cms.uint32( 10 ),
  tid_wheelMask = cms.uint32( 3 ),
  tob_sterStartBit = cms.uint32( 0 ),
  tid_moduleStartBit = cms.uint32( 2 ),
  tec_petalStartBit = cms.uint32( 8 ),
  tob_moduleStartBit = cms.uint32( 2 ),
  pxf_moduleMask = cms.uint32( 63 )
)



process.sistripconn = cms.ESProducer( "SiStripConnectivity" )
process.siStripLorentzAngleDepESProducer = cms.ESProducer( "SiStripLorentzAngleDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  LorentzAngleDeconvMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  LorentzAnglePeakMode = cms.PSet( 
    record = cms.string( "SiStripLorentzAngleRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer( "SiStripBackPlaneCorrectionDepESProducer",
  LatencyRecord = cms.PSet( 
    record = cms.string( "SiStripLatencyRcd" ),
    label = cms.untracked.string( "" )
  ),
  BackPlaneCorrectionDeconvMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "deconvolution" )
  ),
  BackPlaneCorrectionPeakMode = cms.PSet( 
    record = cms.string( "SiStripBackPlaneCorrectionRcd" ),
    label = cms.untracked.string( "peak" )
  )
)
process.siPixelTemplateDBObjectESProducer = cms.ESProducer( "SiPixelTemplateDBObjectESProducer" )
process.siPixelQualityESProducer = cms.ESProducer( "SiPixelQualityESProducer",
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiPixelQualityFromDbRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiPixelDetVOffRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.preshowerDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "PreshowerDetIdAssociator" ),
  etaBinSize = cms.double( 0.1 ),
  nEta = cms.int32( 60 ),
  nPhi = cms.int32( 30 ),
  includeBadChambers = cms.bool( False )
)
process.navigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "SimpleNavigationSchool" ),
  SimpleMagneticField = cms.string( "ParabolicMf" )
)
process.muonDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "MuonDetIdAssociator" ),
  etaBinSize = cms.double( 0.125 ),
  nEta = cms.int32( 48 ),
  nPhi = cms.int32( 48 ),
  includeBadChambers = cms.bool( False )
)
process.hoDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HODetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 30 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.hltESPTrajectorySmootherRK = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectorySmootherRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTrajectoryFitterRK = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPTrajectoryFitterRK" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPTrajectoryCleanerBySharedSeeds = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedSeeds" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedSeeds" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( True )
)
process.hltESPTrajectoryCleanerBySharedHits = cms.ESProducer( "TrajectoryCleanerESProducer",
  ComponentName = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
  fractionShared = cms.double( 0.5 ),
  ValidHitBonus = cms.double( 100.0 ),
  ComponentType = cms.string( "TrajectoryCleanerBySharedHits" ),
  MissingHitPenalty = cms.double( 0.0 ),
  allowSharedFirstHit = cms.bool( False )
)
process.hltESPTrackerRecoGeometryESProducer = cms.ESProducer( "TrackerRecoGeometryESProducer",
  appendToDataLabel = cms.string( "" ),
  trackerGeometryLabel = cms.untracked.string( "" )
)
process.hltESPTrackCounting3D2nd = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  nthTrack = cms.int32( 2 )
)
process.hltESPTrackCounting3D1st = cms.ESProducer( "TrackCountingESProducer",
  b_pT = cms.double( 0.3684 ),
  deltaR = cms.double( -1.0 ),
  a_dR = cms.double( -0.001053 ),
  min_pT = cms.double( 120.0 ),
  maximumDecayLength = cms.double( 5.0 ),
  max_pT = cms.double( 500.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  useVariableJTA = cms.bool( False ),
  min_pT_dRcut = cms.double( 0.5 ),
  max_pT_trackPTcut = cms.double( 3.0 ),
  max_pT_dRcut = cms.double( 0.1 ),
  b_dR = cms.double( 0.6263 ),
  a_pT = cms.double( 0.005263 ),
  maximumDistanceToJetAxis = cms.double( 0.07 ),
  nthTrack = cms.int32( 1 )
)
process.hltESPTTRHBuilderWithoutAngle4PixelTriplets = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderWithoutAngle4PixelTriplets" )
)
process.hltESPTTRHBuilderPixelOnly = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "Fake" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBuilderPixelOnly" )
)
process.hltESPTTRHBuilderAngleAndTemplate = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPETemplateReco" ),
  ComponentName = cms.string( "hltESPTTRHBuilderAngleAndTemplate" )
)
process.hltESPTTRHBWithTrackAngle = cms.ESProducer( "TkTransientTrackingRecHitBuilderESProducer",
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  Matcher = cms.string( "StandardMatcher" ),
  ComputeCoarseLocalPositionFromDisk = cms.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  ComponentName = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltESPStripCPEfromTrackAngle = cms.ESProducer( "StripCPEESProducer",
  ComponentType = cms.string( "StripCPEfromTrackAngle" ),
  ComponentName = cms.string( "hltESPStripCPEfromTrackAngle" ),
  parameters = cms.PSet( 
    mLC_P2 = cms.double( 0.3 ),
    mLC_P1 = cms.double( 0.618 ),
    mLC_P0 = cms.double( -0.326 ),
    useLegacyError = cms.bool( False ),
    mTEC_P1 = cms.double( 0.471 ),
    mTEC_P0 = cms.double( -1.885 ),
    mTOB_P0 = cms.double( -1.026 ),
    mTOB_P1 = cms.double( 0.253 ),
    mTIB_P0 = cms.double( -0.742 ),
    mTIB_P1 = cms.double( 0.202 ),
    mTID_P0 = cms.double( -1.427 ),
    mTID_P1 = cms.double( 0.433 )
  )
)
process.hltESPStraightLinePropagator = cms.ESProducer( "StraightLinePropagatorESProducer",
  ComponentName = cms.string( "hltESPStraightLinePropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
process.hltESPSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
)
process.hltESPSteppingHelixPropagatorAlong = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "alongMomentum" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPSteppingHelixPropagatorAlong" )
)
process.hltESPSoftLeptonByPt = cms.ESProducer( "LeptonTaggerByPtESProducer",
  ipSign = cms.string( "any" )
)
process.hltESPSoftLeptonByDistance = cms.ESProducer( "LeptonTaggerByDistanceESProducer",
  distance = cms.double( 0.5 )
)
process.hltESPSmartPropagatorOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorOpposite" )
)
process.hltESPSmartPropagatorAnyOpposite = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterialOpposite" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAnyOpposite" )
)
process.hltESPSmartPropagatorAny = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "SteppingHelixPropagatorAny" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagatorAny" )
)
process.hltESPSmartPropagator = cms.ESProducer( "SmartPropagatorESProducer",
  Epsilon = cms.double( 5.0 ),
  TrackerPropagator = cms.string( "PropagatorWithMaterial" ),
  MuonPropagator = cms.string( "hltESPSteppingHelixPropagatorAlong" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPSmartPropagator" )
)
process.hltESPSiStripRegionConnectivity = cms.ESProducer( "SiStripRegionConnectivity",
  EtaDivisions = cms.untracked.uint32( 20 ),
  PhiDivisions = cms.untracked.uint32( 20 ),
  EtaMax = cms.untracked.double( 2.5 )
)
process.hltESPRungeKuttaTrackerPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( True )
)
process.hltESPRKTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKSmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPRKTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPRKFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPPromptTrackCountingESProducer = cms.ESProducer( "PromptTrackCountingESProducer",
  maxImpactParameterSig = cms.double( 999999.0 ),
  deltaR = cms.double( -1.0 ),
  maximumDecayLength = cms.double( 999999.0 ),
  impactParameterType = cms.int32( 0 ),
  trackQualityClass = cms.string( "any" ),
  deltaRmin = cms.double( 0.0 ),
  maxImpactParameter = cms.double( 0.03 ),
  maximumDistanceToJetAxis = cms.double( 999999.0 ),
  nthTrack = cms.int32( -1 )
)
process.hltESPPixelCPETemplateReco = cms.ESProducer( "PixelCPETemplateRecoESProducer",
  DoLorentz = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPETemplateReco" ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  speed = cms.int32( -2 ),
  UseClusterSplitter = cms.bool( False )
)
process.hltESPPixelCPEGeneric = cms.ESProducer( "PixelCPEGenericESProducer",
  useLAAlignmentOffsets = cms.bool( False ),
  DoCosmics = cms.bool( False ),
  eff_charge_cut_highX = cms.double( 1.0 ),
  eff_charge_cut_highY = cms.double( 1.0 ),
  inflate_all_errors_no_trk_angle = cms.bool( False ),
  eff_charge_cut_lowY = cms.double( 0.0 ),
  eff_charge_cut_lowX = cms.double( 0.0 ),
  UseErrorsFromTemplates = cms.bool( True ),
  TruncatePixelCharge = cms.bool( True ),
  size_cutY = cms.double( 3.0 ),
  size_cutX = cms.double( 3.0 ),
  useLAWidthFromDB = cms.bool( False ),
  inflate_errors = cms.bool( False ),
  Alpha2Order = cms.bool( True ),
  ClusterProbComputationFlag = cms.int32( 0 ),
  PixelErrorParametrization = cms.string( "NOTcmsim" ),
  EdgeClusterErrorX = cms.double( 50.0 ),
  EdgeClusterErrorY = cms.double( 85.0 ),
  LoadTemplatesFromDB = cms.bool( True ),
  ComponentName = cms.string( "hltESPPixelCPEGeneric" ),
  IrradiationBiasCorrection = cms.bool( False )
)
process.hltESPMuonTransientTrackingRecHitBuilder = cms.ESProducer( "MuonTransientTrackingRecHitBuilderESProducer",
  ComponentName = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
)
process.hltESPMuonDetLayerGeometryESProducer = cms.ESProducer( "MuonDetLayerGeometryESProducer" )
process.hltESPMeasurementTrackerReg = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTrackerReg" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
process.hltESPMeasurementTracker = cms.ESProducer( "MeasurementTrackerESProducer",
  UseStripStripQualityDB = cms.bool( True ),
  StripCPE = cms.string( "hltESPStripCPEfromTrackAngle" ),
  UsePixelROCQualityDB = cms.bool( True ),
  DebugPixelROCQualityDB = cms.untracked.bool( False ),
  UseStripAPVFiberQualityDB = cms.bool( True ),
  badStripCuts = cms.PSet( 
    TOB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TID = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TEC = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    ),
    TIB = cms.PSet( 
      maxConsecutiveBad = cms.uint32( 9999 ),
      maxBad = cms.uint32( 9999 )
    )
  ),
  DebugStripModuleQualityDB = cms.untracked.bool( False ),
  ComponentName = cms.string( "hltESPMeasurementTracker" ),
  DebugPixelModuleQualityDB = cms.untracked.bool( False ),
  UsePixelModuleQualityDB = cms.bool( True ),
  DebugStripAPVFiberQualityDB = cms.untracked.bool( False ),
  HitMatcher = cms.string( "StandardMatcher" ),
  DebugStripStripQualityDB = cms.untracked.bool( False ),
  PixelCPE = cms.string( "hltESPPixelCPEGeneric" ),
  SiStripQualityLabel = cms.string( "" ),
  UseStripModuleQualityDB = cms.bool( True ),
  MaskBadAPVFibers = cms.bool( True )
)
process.hltESPL3MuKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKullbackLeiblerDistance5D = cms.ESProducer( "DistanceBetweenComponentsESProducer5D",
  ComponentName = cms.string( "hltESPKullbackLeiblerDistance5D" ),
  DistanceMeasure = cms.string( "KullbackLeibler" )
)
process.hltESPKFUpdator = cms.ESProducer( "KFUpdatorESProducer",
  ComponentName = cms.string( "hltESPKFUpdator" )
)
process.hltESPKFTrajectorySmootherForMuonTrackLoader = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 10.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPSmartPropagatorAnyOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmootherForL2Muon = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectorySmoother = cms.ESProducer( "KFTrajectorySmootherESProducer",
  errorRescaling = cms.double( 100.0 ),
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectorySmoother" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitterForL2Muon = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFTrajectoryFitter = cms.ESProducer( "KFTrajectoryFitterESProducer",
  minHits = cms.int32( 3 ),
  ComponentName = cms.string( "hltESPKFTrajectoryFitter" ),
  Estimator = cms.string( "hltESPChi2MeasurementEstimator30" ),
  Updator = cms.string( "hltESPKFUpdator" ),
  Propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  RecoGeometry = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPKFFittingSmootherWithOutliersRejectionAndRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( 20.0 ),
  LogPixelProbabilityCut = cms.double( -14.0 ),
  Fitter = cms.string( "hltESPRKFitter" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPRKSmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmootherForL2Muon = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitterForL2Muon" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmootherForL2Muon" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPKFFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPKFTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPKFTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPKFFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPGsfTrajectorySmoother = cms.ESProducer( "GsfTrajectorySmootherESProducer",
  ErrorRescaling = cms.double( 100.0 ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectorySmoother" ),
  GeometricalPropagator = cms.string( "hltESPBwdAnalyticalPropagator" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" )
)
process.hltESPGsfTrajectoryFitter = cms.ESProducer( "GsfTrajectoryFitterESProducer",
  Merger = cms.string( "hltESPCloseComponentsMerger5D" ),
  ComponentName = cms.string( "hltESPGsfTrajectoryFitter" ),
  MaterialEffectsUpdator = cms.string( "hltESPElectronMaterialEffects" ),
  RecoGeometry = cms.string( "hltESPGlobalDetLayerGeometry" ),
  GeometricalPropagator = cms.string( "hltESPAnalyticalPropagator" )
)
process.hltESPGsfElectronFittingSmoother = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPGsfTrajectoryFitter" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPGsfTrajectorySmoother" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPGsfElectronFittingSmoother" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPGlobalTrackingGeometryESProducer = cms.ESProducer( "GlobalTrackingGeometryESProducer" )
process.hltESPGlobalDetLayerGeometry = cms.ESProducer( "GlobalDetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPGlobalDetLayerGeometry" )
)
process.hltESPFwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "hltESPFwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPFittingSmootherRK = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 5 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( False ),
  ComponentName = cms.string( "hltESPFittingSmootherRK" ),
  NoInvalidHitsBeginEnd = cms.bool( False ),
  RejectTracks = cms.bool( True )
)
process.hltESPFittingSmootherIT = cms.ESProducer( "KFFittingSmootherESProducer",
  EstimateCut = cms.double( -1.0 ),
  LogPixelProbabilityCut = cms.double( -16.0 ),
  Fitter = cms.string( "hltESPTrajectoryFitterRK" ),
  MinNumberOfHits = cms.int32( 3 ),
  Smoother = cms.string( "hltESPTrajectorySmootherRK" ),
  BreakTrajWith2ConsecutiveMissing = cms.bool( True ),
  ComponentName = cms.string( "hltESPFittingSmootherIT" ),
  NoInvalidHitsBeginEnd = cms.bool( True ),
  RejectTracks = cms.bool( True )
)
process.hltESPFastSteppingHelixPropagatorOpposite = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
)
process.hltESPFastSteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( True ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
)
process.hltESPElectronMaterialEffects = cms.ESProducer( "GsfMaterialEffectsESProducer",
  BetheHeitlerParametrization = cms.string( "BetheHeitler_cdfmom_nC6_O5.par" ),
  EnergyLossUpdator = cms.string( "GsfBetheHeitlerUpdator" ),
  ComponentName = cms.string( "hltESPElectronMaterialEffects" ),
  MultipleScatteringUpdator = cms.string( "MultipleScatteringUpdator" ),
  Mass = cms.double( 5.11E-4 ),
  BetheHeitlerCorrection = cms.int32( 2 )
)
process.hltESPElectronChi2 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 2000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPElectronChi2" )
)
process.hltESPEcalTrigTowerConstituentsMapBuilder = cms.ESProducer( "EcalTrigTowerConstituentsMapBuilder",
  MapFile = cms.untracked.string( "Geometry/EcalMapping/data/EndCap_TTMap.txt" )
)
process.hltESPEcalRegionCablingESProducer = cms.ESProducer( "EcalRegionCablingESProducer",
  esMapping = cms.PSet(  LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ) )
)
process.hltESPDummyDetLayerGeometry = cms.ESProducer( "DetLayerGeometryESProducer",
  ComponentName = cms.string( "hltESPDummyDetLayerGeometry" )
)
process.hltESPCloseComponentsMerger5D = cms.ESProducer( "CloseComponentsMergerESProducer5D",
  ComponentName = cms.string( "hltESPCloseComponentsMerger5D" ),
  MaxComponents = cms.int32( 12 ),
  DistanceMeasure = cms.string( "hltESPKullbackLeiblerDistance5D" )
)
process.hltESPChi2MeasurementEstimator9 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 9.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator9" )
)
process.hltESPChi2MeasurementEstimator16 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 16.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator16" )
)
process.hltESPChi2MeasurementEstimator = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator" )
)
process.hltESPChi2EstimatorForRefit = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 100000.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2EstimatorForRefit" )
)
process.hltESPBwdElectronPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "hltESPBwdElectronPropagator" ),
  Mass = cms.double( 5.11E-4 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPBwdAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPBwdAnalyticalPropagator" ),
  PropagationDirection = cms.string( "oppositeToMomentum" )
)
process.hltESPAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "hltESPAnalyticalPropagator" ),
  PropagationDirection = cms.string( "alongMomentum" )
)
process.hltCombinedSecondaryVertex = cms.ESProducer( "CombinedSecondaryVertexESProducer",
  trackPairV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.03 ) ),
  useTrackWeights = cms.bool( True ),
  useCategories = cms.bool( True ),
  pseudoMultiplicityMin = cms.uint32( 2 ),
  categoryVariableName = cms.string( "vertexCategory" ),
  trackSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( -99999.9 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  calibrationRecords = cms.vstring( 'CombinedSVRecoVertex',
    'CombinedSVPseudoVertex',
    'CombinedSVNoVertex' ),
  correctVertexMass = cms.bool( True ),
  charmCut = cms.double( 1.5 ),
  vertexFlip = cms.bool( False ),
  minimumTrackWeight = cms.double( 0.5 ),
  pseudoVertexV0Filter = cms.PSet(  k0sMassWindow = cms.double( 0.05 ) ),
  trackMultiplicityMin = cms.uint32( 3 ),
  trackPseudoSelection = cms.PSet( 
    totalHitsMin = cms.uint32( 0 ),
    jetDeltaRMax = cms.double( 0.3 ),
    qualityClass = cms.string( "any" ),
    pixelHitsMin = cms.uint32( 0 ),
    sip3dSigMin = cms.double( -99999.9 ),
    sip3dSigMax = cms.double( 99999.9 ),
    normChi2Max = cms.double( 99999.9 ),
    maxDistToAxis = cms.double( 0.07 ),
    sip2dValMax = cms.double( 99999.9 ),
    maxDecayLen = cms.double( 5.0 ),
    ptMin = cms.double( 0.0 ),
    sip2dSigMax = cms.double( 99999.9 ),
    sip2dSigMin = cms.double( 2.0 ),
    sip3dValMax = cms.double( 99999.9 ),
    sip2dValMin = cms.double( -99999.9 ),
    sip3dValMin = cms.double( -99999.9 )
  ),
  trackSort = cms.string( "sip2dSig" ),
  trackFlip = cms.bool( False )
)
process.hcal_db_producer = cms.ESProducer( "HcalDbProducer" )
process.hcalRecAlgos = cms.ESProducer( "HcalRecAlgoESProducer",
  RecoveredRecHitBits = cms.vstring( 'TimingAddedBit',
    'TimingSubtractedBit' ),
  SeverityLevels = cms.VPSet( 
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 0 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerProb' ),
      Level = cms.int32( 1 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HSCP_R1R2',
  'HSCP_FracLeader',
  'HSCP_OuterEnergy',
  'HSCP_ExpFit',
  'ADCSaturationBit',
  'HBHEIsolatedNoise',
  'AddedSimHcalNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellExcludeFromHBHENoiseSummary' ),
      Level = cms.int32( 5 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEHpdHitMultiplicity',
  'HBHEPulseShape',
  'HOBit',
  'HFInTimeWindow',
  'ZDCBit',
  'CalibrationBit',
  'TimingErrorBit',
  'HBHETriangleNoise',
  'HBHETS4TS5Noise' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 8 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HFLongShort',
  'HFPET',
  'HFS8S1Ratio',
  'HFDigiTime' ),
      ChannelStatus = cms.vstring(  ),
      Level = cms.int32( 11 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring( 'HBHEFlatNoise',
  'HBHESpikeNoise' ),
      ChannelStatus = cms.vstring( 'HcalCellCaloTowerMask' ),
      Level = cms.int32( 12 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellHot' ),
      Level = cms.int32( 15 )
    ),
    cms.PSet(  RecHitFlags = cms.vstring(  ),
      ChannelStatus = cms.vstring( 'HcalCellOff',
        'HcalCellDead' ),
      Level = cms.int32( 20 )
    )
  ),
  DropChannelStatusBits = cms.vstring( 'HcalCellMask',
    'HcalCellOff',
    'HcalCellDead' )
)
process.hcalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "HcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.ecalSeverityLevel = cms.ESProducer( "EcalSeverityLevelESProducer",
  dbstatusMask = cms.PSet( 
    kGood = cms.vstring( 'kOk' ),
    kProblematic = cms.vstring( 'kDAC',
      'kNoLaser',
      'kNoisy',
      'kNNoisy',
      'kNNNoisy',
      'kNNNNoisy',
      'kNNNNNoisy',
      'kFixedG6',
      'kFixedG1',
      'kFixedG0' ),
    kRecovered = cms.vstring(  ),
    kTime = cms.vstring(  ),
    kWeird = cms.vstring(  ),
    kBad = cms.vstring( 'kNonRespondingIsolated',
      'kDeadVFE',
      'kDeadFE',
      'kNoDataNoTP' )
  ),
  timeThresh = cms.double( 2.0 ),
  flagMask = cms.PSet( 
    kGood = cms.vstring( 'kGood' ),
    kProblematic = cms.vstring( 'kPoorReco',
      'kPoorCalib',
      'kNoisy',
      'kSaturated' ),
    kRecovered = cms.vstring( 'kLeadingEdgeRecovered',
      'kTowerRecovered' ),
    kTime = cms.vstring( 'kOutOfTime' ),
    kWeird = cms.vstring( 'kWeird',
      'kDiWeird' ),
    kBad = cms.vstring( 'kFaultyHardware',
      'kDead',
      'kKilled' )
  )
)
process.ecalDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "EcalDetIdAssociator" ),
  etaBinSize = cms.double( 0.02 ),
  nEta = cms.int32( 300 ),
  nPhi = cms.int32( 360 ),
  includeBadChambers = cms.bool( False )
)
process.cosmicsNavigationSchoolESProducer = cms.ESProducer( "NavigationSchoolESProducer",
  ComponentName = cms.string( "CosmicNavigationSchool" ),
  SimpleMagneticField = cms.string( "" )
)
process.caloDetIdAssociator = cms.ESProducer( "DetIdAssociatorESProducer",
  ComponentName = cms.string( "CaloDetIdAssociator" ),
  etaBinSize = cms.double( 0.087 ),
  nEta = cms.int32( 70 ),
  nPhi = cms.int32( 72 ),
  includeBadChambers = cms.bool( False )
)
process.ZdcGeometryFromDBEP = cms.ESProducer( "ZdcGeometryFromDBEP",
  applyAlignment = cms.bool( False )
)
process.VBF40 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_4t" ),
  version = cms.string( "grid_1103l_071212_4t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_40" ),
  geometryVersion = cms.int32( 71212 ),
  gridFiles = cms.VPSet( 
    cms.PSet(  path = cms.string( "grid.[v].bin" ),
      master = cms.int32( 1 ),
      sectors = cms.string( "0" ),
      volumes = cms.string( "1-312" )
    )
  ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF38 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32( 14100, 14200, 17600, 17800, 17900, 18100, 18300, 18400, 18600, 23100, 23300, 23400, 23600, 23800, 23900, 24100, 28600, 28800, 28900, 29100, 29300, 29400, 29600, 28609, 28809, 28909, 29109, 29309, 29409, 29609, 28610, 28810, 28910, 29110, 29310, 29410, 29610, 28611, 28811, 28911, 29111, 29311, 29411, 29611 ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble( 1.0, 1.0, 0.994, 1.004, 1.004, 1.005, 1.004, 1.004, 0.994, 0.965, 0.958, 0.958, 0.953, 0.958, 0.958, 0.965, 0.918, 0.924, 0.924, 0.906, 0.924, 0.924, 0.918, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991, 0.991, 0.998, 0.998, 0.978, 0.998, 0.998, 0.991 ),
  label = cms.untracked.string( "090322_3_8t" ),
  version = cms.string( "grid_1103l_090322_3_8t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_38" ),
  geometryVersion = cms.int32( 71212 ),
  gridFiles = cms.VPSet( 
    cms.PSet(  path = cms.string( "grid.[v].bin" ),
      master = cms.int32( 1 ),
      sectors = cms.string( "0" ),
      volumes = cms.string( "1-312" )
    ),
    cms.PSet(  path = cms.string( "S3/grid.[v].bin" ),
      master = cms.int32( 3 ),
      sectors = cms.string( "3" ),
      volumes = cms.string( "176-186,231-241,286-296" )
    ),
    cms.PSet(  path = cms.string( "S4/grid.[v].bin" ),
      master = cms.int32( 4 ),
      sectors = cms.string( "4" ),
      volumes = cms.string( "176-186,231-241,286-296" )
    ),
    cms.PSet(  path = cms.string( "S9/grid.[v].bin" ),
      master = cms.int32( 9 ),
      sectors = cms.string( "9" ),
      volumes = cms.string( "14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296" )
    ),
    cms.PSet(  path = cms.string( "S10/grid.[v].bin" ),
      master = cms.int32( 10 ),
      sectors = cms.string( "10" ),
      volumes = cms.string( "14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296" )
    ),
    cms.PSet(  path = cms.string( "S11/grid.[v].bin" ),
      master = cms.int32( 11 ),
      sectors = cms.string( "11" ),
      volumes = cms.string( "14,15,20,21,24-27,32,33,40,41,48,49,56,57,62,63,70,71,286-296" )
    )
  ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF35 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_3_5t" ),
  version = cms.string( "grid_1103l_071212_3_5t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_35" ),
  geometryVersion = cms.int32( 71212 ),
  gridFiles = cms.VPSet( 
    cms.PSet(  path = cms.string( "grid.[v].bin" ),
      master = cms.int32( 1 ),
      sectors = cms.string( "0" ),
      volumes = cms.string( "1-312" )
    )
  ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF30 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_3t" ),
  version = cms.string( "grid_1103l_071212_3t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_30" ),
  geometryVersion = cms.int32( 71212 ),
  gridFiles = cms.VPSet( 
    cms.PSet(  path = cms.string( "grid.[v].bin" ),
      master = cms.int32( 1 ),
      sectors = cms.string( "0" ),
      volumes = cms.string( "1-312" )
    )
  ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF20 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "071212_2t" ),
  version = cms.string( "grid_1103l_071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_20" ),
  geometryVersion = cms.int32( 71212 ),
  gridFiles = cms.VPSet( 
    cms.PSet(  path = cms.string( "grid.[v].bin" ),
      master = cms.int32( 1 ),
      sectors = cms.string( "0" ),
      volumes = cms.string( "1-312" )
    )
  ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.VBF0 = cms.ESProducer( "VolumeBasedMagneticFieldESProducer",
  scalingVolumes = cms.vint32(  ),
  useParametrizedTrackerField = cms.bool( True ),
  scalingFactors = cms.vdouble(  ),
  label = cms.untracked.string( "0t" ),
  version = cms.string( "grid_1103l_071212_2t" ),
  debugBuilder = cms.untracked.bool( False ),
  paramLabel = cms.string( "slave_0" ),
  geometryVersion = cms.int32( 71212 ),
  gridFiles = cms.VPSet( 
    cms.PSet(  path = cms.string( "grid.[v].bin" ),
      master = cms.int32( 1 ),
      sectors = cms.string( "0" ),
      volumes = cms.string( "1-312" )
    )
  ),
  cacheLastVolume = cms.untracked.bool( True )
)
process.TransientTrackBuilderESProducer = cms.ESProducer( "TransientTrackBuilderESProducer",
  ComponentName = cms.string( "TransientTrackBuilder" )
)
process.TrackerGeometricDetESModule = cms.ESProducer( "TrackerGeometricDetESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  #layerNumberPXB = cms.uint32( 16 ),
  #totalBlade = cms.uint32( 24 )
)
process.TrackerDigiGeometryESModule = cms.ESProducer( "TrackerDigiGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  trackerGeometryConstants = cms.PSet( 
    ROCS_X = cms.int32( 0 ),
    ROCS_Y = cms.int32( 0 ),
    upgradeGeometry = cms.bool( False ),
    BIG_PIX_PER_ROC_Y = cms.int32( 2 ),
    BIG_PIX_PER_ROC_X = cms.int32( 1 ),
    ROWS_PER_ROC = cms.int32( 80 ),
    COLS_PER_ROC = cms.int32( 52 )
  ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.SteppingHelixPropagatorAny = cms.ESProducer( "SteppingHelixPropagatorESProducer",
  NoErrorPropagation = cms.bool( False ),
  endcapShiftInZPos = cms.double( 0.0 ),
  PropagationDirection = cms.string( "anyDirection" ),
  useTuningForL2Speed = cms.bool( False ),
  useIsYokeFlag = cms.bool( True ),
  endcapShiftInZNeg = cms.double( 0.0 ),
  SetVBFPointer = cms.bool( False ),
  AssumeNoMaterial = cms.bool( False ),
  returnTangentPlane = cms.bool( True ),
  useInTeslaFromMagField = cms.bool( False ),
  VBFName = cms.string( "VolumeBasedMagneticField" ),
  useEndcapShiftsInZ = cms.bool( False ),
  sendLogWarning = cms.bool( False ),
  useMatVolumes = cms.bool( True ),
  debug = cms.bool( False ),
  ApplyRadX0Correction = cms.bool( True ),
  useMagVolumes = cms.bool( True ),
  ComponentName = cms.string( "SteppingHelixPropagatorAny" )
)
process.SlaveField40 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "4_0T" ) ),
  label = cms.untracked.string( "slave_40" )
)
process.SlaveField38 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_8T" ) ),
  label = cms.untracked.string( "slave_38" )
)
process.SlaveField35 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_5T" ) ),
  label = cms.untracked.string( "slave_35" )
)
process.SlaveField30 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "3_0T" ) ),
  label = cms.untracked.string( "slave_30" )
)
process.SlaveField20 = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "OAE_1103l_071212" ),
  parameters = cms.PSet(  BValue = cms.string( "2_0T" ) ),
  label = cms.untracked.string( "slave_20" )
)
process.SlaveField0 = cms.ESProducer( "UniformMagneticFieldESProducer",
  ZFieldInTesla = cms.double( 0.0 ),
  label = cms.untracked.string( "slave_0" )
)
process.SiStripRecHitMatcherESProducer = cms.ESProducer( "SiStripRecHitMatcherESProducer",
  PreFilter = cms.bool( False ),
  ComponentName = cms.string( "StandardMatcher" ),
  NSigmaInside = cms.double( 3.0 )
)
process.SiStripQualityESProducer = cms.ESProducer( "SiStripQualityESProducer",
  appendToDataLabel = cms.string( "" ),
  PrintDebugOutput = cms.bool( False ),
  ThresholdForReducedGranularity = cms.double( 0.3 ),
  UseEmptyRunInfo = cms.bool( False ),
  ReduceGranularity = cms.bool( False ),
  ListOfRecordToMerge = cms.VPSet( 
    cms.PSet(  record = cms.string( "SiStripDetVOffRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripDetCablingRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadChannelRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadFiberRcd" ),
      tag = cms.string( "" )
    ),
    cms.PSet(  record = cms.string( "SiStripBadModuleRcd" ),
      tag = cms.string( "" )
    )
  )
)
process.SiStripGainESProducer = cms.ESProducer( "SiStripGainESProducer",
  printDebug = cms.untracked.bool( False ),
  appendToDataLabel = cms.string( "" ),
  APVGain = cms.VPSet( 
    cms.PSet(  Record = cms.string( "SiStripApvGainRcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    ),
    cms.PSet(  Record = cms.string( "SiStripApvGain2Rcd" ),
      NormalizationFactor = cms.untracked.double( 1.0 ),
      Label = cms.untracked.string( "" )
    )
  ),
  AutomaticNormalization = cms.bool( False )
)
process.RPCGeometryESModule = cms.ESProducer( "RPCGeometryESModule",
  useDDD = cms.untracked.bool( False ),
  compatibiltyWith11 = cms.untracked.bool( True )
)
process.OppositeMaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.MaterialPropagator = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterial" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.HcalTopologyIdealEP = cms.ESProducer( "HcalTopologyIdealEP",
  Exclude = cms.untracked.string( "" ),
  appendToDataLabel = cms.string( "" ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.HcalGeometryFromDBEP = cms.ESProducer( "HcalGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.hltESPChi2ChargeMeasurementEstimator16 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  #clusterChargeCut replaced minGoodStripCharge
  #minGoodStripCharge = cms.double( 1724.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  pTChargeCutThreshold = cms.double( -1.0 ),
  nSigma = cms.double( 3.0 ),
  MaxChi2 = cms.double( 16.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
)
process.hltESPChi2ChargeMeasurementEstimator9 = cms.ESProducer( "Chi2ChargeMeasurementEstimatorESProducer",
  #minGoodStripCharge = cms.double( 1724.0 ),
  ComponentName = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  pTChargeCutThreshold = cms.double( 15.0 ),
  nSigma = cms.double( 3.0 ),
  MaxChi2 = cms.double( 9.0 ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutLoose" ) ),
)
process.EcalPreshowerGeometryFromDBEP = cms.ESProducer( "EcalPreshowerGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalLaserCorrectionService = cms.ESProducer( "EcalLaserCorrectionService" )
process.EcalEndcapGeometryFromDBEP = cms.ESProducer( "EcalEndcapGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.EcalElectronicsMappingBuilder = cms.ESProducer( "EcalElectronicsMappingBuilder" )
process.EcalBarrelGeometryFromDBEP = cms.ESProducer( "EcalBarrelGeometryFromDBEP",
  applyAlignment = cms.bool( True )
)
process.DTGeometryESModule = cms.ESProducer( "DTGeometryESModule",
  appendToDataLabel = cms.string( "" ),
  fromDDD = cms.bool( False ),
  applyAlignment = cms.bool( True ),
  alignmentsLabel = cms.string( "" )
)
process.ClusterShapeHitFilterESProducer = cms.ESProducer( "ClusterShapeHitFilterESProducer",
  ComponentName = cms.string( "ClusterShapeHitFilter" ),
  clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  PixelShapeFile = cms.string( "RecoPixelVertexing/PixelLowPtUtilities/data/pixelShape.par" ),
)
process.CastorDbProducer = cms.ESProducer( "CastorDbProducer",
  appendToDataLabel = cms.string( "" )
)
process.CaloTowerGeometryFromDBEP = cms.ESProducer( "CaloTowerGeometryFromDBEP",
  applyAlignment = cms.bool( False ),
  hcalTopologyConstants = cms.PSet( 
    maxDepthHE = cms.int32( 3 ),
    maxDepthHB = cms.int32( 2 ),
    mode = cms.string( "HcalTopologyMode::LHC" )
  )
)
process.CaloTowerConstituentsMapBuilder = cms.ESProducer( "CaloTowerConstituentsMapBuilder",
  appendToDataLabel = cms.string( "" ),
  MapFile = cms.untracked.string( "Geometry/CaloTopology/data/CaloTowerEEGeometric.map.gz" )
)
process.CaloTopologyBuilder = cms.ESProducer( "CaloTopologyBuilder" )
process.CaloGeometryBuilder = cms.ESProducer( "CaloGeometryBuilder",
  SelectedCalos = cms.vstring( 'HCAL',
    'ZDC',
    'EcalBarrel',
    'EcalEndcap',
    'EcalPreshower',
    'TOWER' )
)
process.CSCIndexerESProducer = cms.ESProducer( "CSCIndexerESProducer",
  AlgoName = cms.string( "CSCIndexerStartup" )
)
process.CSCGeometryESModule = cms.ESProducer( "CSCGeometryESModule",
  useRealWireGeometry = cms.bool( True ),
  appendToDataLabel = cms.string( "" ),
  alignmentsLabel = cms.string( "" ),
  useGangedStripsInME1a = cms.bool( True ),
  debugV = cms.untracked.bool( False ),
  useOnlyWiresInME1a = cms.bool( False ),
  useDDD = cms.bool( False ),
  useCentreTIOffsets = cms.bool( False ),
  applyAlignment = cms.bool( True )
)
process.CSCChannelMapperESProducer = cms.ESProducer( "CSCChannelMapperESProducer",
  AlgoName = cms.string( "CSCChannelMapperStartup" )
)
process.AutoMagneticFieldESProducer = cms.ESProducer( "AutoMagneticFieldESProducer",
  label = cms.untracked.string( "" ),
  nominalCurrents = cms.untracked.vint32( -1, 0, 9558, 14416, 16819, 18268, 19262 ),
  valueOverride = cms.int32( -1 ),
  mapLabels = cms.untracked.vstring( '090322_3_8t',
    '0t',
    '071212_2t',
    '071212_3t',
    '071212_3_5t',
    '090322_3_8t',
    '071212_4t' )
)
process.AnyDirectionAnalyticalPropagator = cms.ESProducer( "AnalyticalPropagatorESProducer",
  MaxDPhi = cms.double( 1.6 ),
  ComponentName = cms.string( "AnyDirectionAnalyticalPropagator" ),
  PropagationDirection = cms.string( "anyDirection" )
)
process.hltESPChi2MeasurementEstimator30 = cms.ESProducer( "Chi2MeasurementEstimatorESProducer",
  MaxChi2 = cms.double( 30.0 ),
  nSigma = cms.double( 3.0 ),
  ComponentName = cms.string( "hltESPChi2MeasurementEstimator30" )
)
process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer( "ParametrizedMagneticFieldProducer",
  version = cms.string( "Parabolic" ),
  parameters = cms.PSet(  BValue = cms.string( "" ) ),
  label = cms.untracked.string( "ParabolicMf" )
)
process.OppositeMaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "oppositeToMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.MaterialPropagatorParabolicMF = cms.ESProducer( "PropagatorWithMaterialESProducer",
  SimpleMagneticField = cms.string( "ParabolicMf" ),
  PropagationDirection = cms.string( "alongMomentum" ),
  ComponentName = cms.string( "PropagatorWithMaterialParabolicMf" ),
  Mass = cms.double( 0.105 ),
  ptMin = cms.double( -1.0 ),
  MaxDPhi = cms.double( 1.6 ),
  useRungeKutta = cms.bool( False )
)
process.hltESPAK4PFAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4PFHLT" ),
  level = cms.string( "L3Absolute" )
)
process.hltESPAK4CaloAbsoluteCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4CaloHLT" ),
  level = cms.string( "L3Absolute" )
)
process.hltESPAK4CaloRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4CaloHLT" ),
  level = cms.string( "L2Relative" )
)
process.hltESPAK4PFRelativeCorrectionESProducer = cms.ESProducer( "LXXXCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  algorithm = cms.string( "AK4PFHLT" ),
  level = cms.string( "L2Relative" )
)
process.hltESPAK4PFFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
  algorithm = cms.string( "AK4PFHLT" ),
  level = cms.string( "L1FastJet" )
)
process.hltESPAK4CaloFastJetCorrectionESProducer = cms.ESProducer( "L1FastjetCorrectionESProducer",
  appendToDataLabel = cms.string( "" ),
  srcRho = cms.InputTag( "hltFixedGridRhoFastjetAllCalo" ),
  algorithm = cms.string( "AK4CaloHLT" ),
  level = cms.string( "L1FastJet" )
)
process.hltESPAK4PFCorrection = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK4PFFastJetCorrectionESProducer',
    'hltESPAK4PFRelativeCorrectionESProducer',
    'hltESPAK4PFAbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)
process.hltESPAK4CaloCorrection = cms.ESProducer( "JetCorrectionESChain",
  correctors = cms.vstring( 'hltESPAK4CaloFastJetCorrectionESProducer',
    'hltESPAK4CaloRelativeCorrectionESProducer',
    'hltESPAK4CaloAbsoluteCorrectionESProducer' ),
  appendToDataLabel = cms.string( "" )
)

process.MessageLogger = cms.Service( "MessageLogger",
    suppressInfo = cms.untracked.vstring(  ),
    debugs = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    suppressDebug = cms.untracked.vstring(  ),
    cout = cms.untracked.PSet(  placeholder = cms.untracked.bool( True ) ),
    cerr_stats = cms.untracked.PSet( 
      threshold = cms.untracked.string( "WARNING" ),
      output = cms.untracked.string( "cerr" ),
      optionalPSet = cms.untracked.bool( True )
    ),
    warnings = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    statistics = cms.untracked.vstring( 'cerr' ),
    cerr = cms.untracked.PSet( 
      INFO = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      noTimeStamps = cms.untracked.bool( False ),
      FwkReport = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 0 )
      ),
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkSummary = cms.untracked.PSet( 
        reportEvery = cms.untracked.int32( 1 ),
        limit = cms.untracked.int32( 10000000 )
      ),
      threshold = cms.untracked.string( "INFO" ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    FrameworkJobReport = cms.untracked.PSet( 
      default = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      FwkJob = cms.untracked.PSet(  limit = cms.untracked.int32( 10000000 ) )
    ),
    suppressWarning = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltCtf3HitL1SeededWithMaterialTracks',
      'hltL3MuonsOIState',
      'hltPixelTracksForHighMult',
      'hltHITPixelTracksHE',
      'hltHITPixelTracksHB',
      'hltCtfL1SeededWithMaterialTracks',
      'hltRegionalTracksForL3MuonIsolation',
      'hltSiPixelClusters',
      'hltActivityStartUpElectronPixelSeeds',
      'hltLightPFTracks',
      'hltPixelVertices3DbbPhi',
      'hltL3MuonsIOHit',
      'hltPixelTracks',
      'hltSiPixelDigis',
      'hltL3MuonsOIHit',
      'hltL1SeededElectronGsfTracks',
      'hltL1SeededStartUpElectronPixelSeeds',
      'hltBLifetimeRegionalCtfWithMaterialTracksbbPhiL1FastJetFastPV',
      'hltCtfActivityWithMaterialTracks' ),
    errors = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    fwkJobReports = cms.untracked.vstring( 'FrameworkJobReport' ),
    debugModules = cms.untracked.vstring(  ),
    infos = cms.untracked.PSet( 
      threshold = cms.untracked.string( "INFO" ),
      Root_NoDictionary = cms.untracked.PSet(  limit = cms.untracked.int32( 0 ) ),
      placeholder = cms.untracked.bool( True ),
      suppressInfo = cms.untracked.vstring(  ),
      suppressWarning = cms.untracked.vstring(  ),
      suppressDebug = cms.untracked.vstring(  ),
      suppressError = cms.untracked.vstring(  )
    ),
    categories = cms.untracked.vstring( 'FwkJob',
      'FwkReport',
      'FwkSummary',
      'Root_NoDictionary' ),
    destinations = cms.untracked.vstring( 'warnings',
      'errors',
      'infos',
      'debugs',
      'cout',
      'cerr' ),
    threshold = cms.untracked.string( "INFO" ),
    suppressError = cms.untracked.vstring( 'hltOnlineBeamSpot',
      'hltL3MuonCandidates',
      'hltL3TkTracksFromL2OIState',
      'hltPFJetCtfWithMaterialTracks',
      'hltL3TkTracksFromL2IOHit',
      'hltL3TkTracksFromL2OIHit' )
)
process.FastTimerService = cms.Service( "FastTimerService",
    dqmPath = cms.untracked.string( "HLT/TimerService" ),
    dqmModuleTimeRange = cms.untracked.double( 40.0 ),
    useRealTimeClock = cms.untracked.bool( True ),
    enableTimingModules = cms.untracked.bool( True ),
    enableDQM = cms.untracked.bool( True ),
    enableDQMbyModule = cms.untracked.bool( False ),
    enableTimingExclusive = cms.untracked.bool( True ),
    skipFirstPath = cms.untracked.bool( False ),
    enableDQMbyLumiSection = cms.untracked.bool( True ),
    dqmPathTimeResolution = cms.untracked.double( 0.5 ),
    dqmPathTimeRange = cms.untracked.double( 100.0 ),
    dqmTimeRange = cms.untracked.double( 1000.0 ),
    dqmLumiSectionsRange = cms.untracked.uint32( 2500 ),
    enableDQMbyProcesses = cms.untracked.bool( True ),
    enableDQMSummary = cms.untracked.bool( True ),
    enableTimingSummary = cms.untracked.bool( True ),
    enableDQMbyPathTotal = cms.untracked.bool( True ),
    enableTimingPaths = cms.untracked.bool( True ),
    enableDQMbyPathExclusive = cms.untracked.bool( True ),
    dqmTimeResolution = cms.untracked.double( 5.0 ),
    dqmModuleTimeResolution = cms.untracked.double( 0.2 ),
    enableDQMbyPathActive = cms.untracked.bool( True ),
    enableDQMbyPathDetails = cms.untracked.bool( True ),
    enableDQMbyPathOverhead = cms.untracked.bool( False ),
    enableDQMbyPathCounters = cms.untracked.bool( True ),
    enableDQMbyModuleType = cms.untracked.bool( False )
)

process.hltGtDigis = cms.EDProducer( "L1GlobalTriggerRawToDigi",
    DaqGtFedId = cms.untracked.int32( 813 ),
    DaqGtInputTag = cms.InputTag( "rawDataCollector" ),
    UnpackBxInEvent = cms.int32( 5 ),
    ActiveBoardsMask = cms.uint32( 0xffff )
)
process.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
process.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023 )
)
process.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    processName = cms.string( "@" )
)
process.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
process.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet( 
    ),
    verbose = cms.untracked.bool( False )
)
process.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
process.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
process.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
process.hltGctDigis = cms.EDProducer( "GctRawToDigi",
    unpackSharedRegions = cms.bool( False ),
    numberOfGctSamplesToUnpack = cms.uint32( 1 ),
    verbose = cms.untracked.bool( False ),
    numberOfRctSamplesToUnpack = cms.uint32( 1 ),
    inputLabel = cms.InputTag( "rawDataCollector" ),
    unpackerVersion = cms.uint32( 0 ),
    gctFedId = cms.untracked.int32( 745 ),
    hltMode = cms.bool( True )
)
process.hltL1GtObjectMap = cms.EDProducer( "L1GlobalTrigger",
    TechnicalTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlgorithmTriggersUnmasked = cms.bool( False ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    ProduceL1GtDaqRecord = cms.bool( False ),
    ReadTechnicalTriggerRecords = cms.bool( True ),
    RecordLength = cms.vint32( 3, 0 ),
    TechnicalTriggersUnmasked = cms.bool( False ),
    ProduceL1GtEvmRecord = cms.bool( False ),
    GmtInputTag = cms.InputTag( "hltGtDigis" ),
    TechnicalTriggersVetoUnmasked = cms.bool( True ),
    AlternativeNrBxBoardEvm = cms.uint32( 0 ),
    TechnicalTriggersInputTags = cms.VInputTag( 'simBscDigis' ),
    CastorInputTag = cms.InputTag( "castorL1Digis" ),
    GctInputTag = cms.InputTag( "hltGctDigis" ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    WritePsbL1GtDaqRecord = cms.bool( False ),
    BstLengthBytes = cms.int32( -1 )
)
process.hltL1extraParticles = cms.EDProducer( "L1ExtraParticlesProd",
    tauJetSource = cms.InputTag( 'hltGctDigis','tauJets' ),
    etHadSource = cms.InputTag( "hltGctDigis" ),
    etTotalSource = cms.InputTag( "hltGctDigis" ),
    centralBxOnly = cms.bool( True ),
    centralJetSource = cms.InputTag( 'hltGctDigis','cenJets' ),
    etMissSource = cms.InputTag( "hltGctDigis" ),
    hfRingEtSumsSource = cms.InputTag( "hltGctDigis" ),
    produceMuonParticles = cms.bool( True ),
    forwardJetSource = cms.InputTag( 'hltGctDigis','forJets' ),
    ignoreHtMiss = cms.bool( False ),
    htMissSource = cms.InputTag( "hltGctDigis" ),
    produceCaloParticles = cms.bool( True ),
    muonSource = cms.InputTag( "hltGtDigis" ),
    isolatedEmSource = cms.InputTag( 'hltGctDigis','isoEm' ),
    nonIsolatedEmSource = cms.InputTag( 'hltGctDigis','nonIsoEm' ),
    hfRingBitCountsSource = cms.InputTag( "hltGctDigis" )
)
process.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
process.hltL1sL1ZeroBias = cms.EDFilter( "HLTLevel1GTSeed",
    L1SeedsLogicalExpression = cms.string( "L1_ZeroBias" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreAlCaEcalPhiSym = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    tccUnpacking = cms.bool( True ),
    FedLabel = cms.InputTag( "listfeds" ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    feIdCheck = cms.bool( True ),
    silentMode = cms.untracked.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    eventPut = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    numbXtalTSamples = cms.int32( 10 ),
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    DoRegional = cms.bool( False ),
    feUnpacking = cms.bool( True ),
    forceToKeepFRData = cms.bool( False ),
    headerUnpacking = cms.bool( True ),
    memUnpacking = cms.bool( True )
)
process.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    #OLD code, most of which doesn't work in 7_4_0_pre9
	#EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    ##alphaEB = cms.double( 1.138 ),
    ##alphaEE = cms.double( 1.89 ),
    #EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    #EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    ##AlphaBetaFilename = cms.untracked.string( "NOFILE" ),
    ##betaEB = cms.double( 1.655 ),
    ##MinAmplEndcap = cms.double( 14.0 ),
    ##MinAmplBarrel = cms.double( 8.0 ),
    #algo = cms.string( "EcalUncalibRecHitWorkerWeights" ),
    ##betaEE = cms.double( 1.4 ),
    ##UseDynamicPedestal = cms.bool( True ),
    #EBhitCollection = cms.string( "EcalUncalibRecHitsEB" )
	##
	#NEW code which should work in 7_4_0_pre9
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet( 
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeNconst = cms.double( 28.5 ),
      ampErrorCalculation = cms.bool( False ),
      kPoorRecoFlagEB = cms.bool( True ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      useLumiInfoRunHeader = cms.bool( False ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      prefitMaxChiSqEB = cms.double( 100.0 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      timealgo = cms.string( "None" ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      EEtimeNconst = cms.double( 31.8 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      doPrefitEE = cms.bool( True ),
      doPrefitEB = cms.bool( True )
    )
)
process.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeFEToBeRecovered = cms.string( "eeFE" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" )
)
process.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    cleaningConfig = cms.PSet( 
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    recoverEEFE = cms.bool( True ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    EBLaserMAX = cms.double( 3.0 ),
    flagsMapDBReco = cms.PSet( 
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    EELaserMAX = cms.double( 8.0 ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    recoverEEIsolatedChannels = cms.bool( False )
)
process.hltAlCaPhiSymStream = cms.EDFilter( "HLTEcalPhiSymFilter",
    eCut_endcap = cms.double( 0.75 ),
    endcapHitCollection = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    eCut_endcap_high = cms.double( 999999.0 ),
    eCut_barrel = cms.double( 0.15 ),
    eCut_barrel_high = cms.double( 999999.0 ),
    statusThreshold = cms.uint32( 3 ),
    useRecoFlag = cms.bool( False ),
    phiSymBarrelHitCollection = cms.string( "phiSymEcalRecHitsEB" ),
    barrelHitCollection = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    phiSymEndcapHitCollection = cms.string( "phiSymEcalRecHitsEE" )
)
process.hltAlCaPhiSymUncalibrator = cms.EDProducer( "EcalRecalibRecHitProducer",
    doEnergyScale = cms.bool( True ),
    doLaserCorrectionsInverse = cms.bool( True ),
    EERecHitCollection = cms.InputTag( 'hltAlCaPhiSymStream','phiSymEcalRecHitsEE' ),
    doEnergyScaleInverse = cms.bool( True ),
    EBRecHitCollection = cms.InputTag( 'hltAlCaPhiSymStream','phiSymEcalRecHitsEB' ),
    doIntercalibInverse = cms.bool( True ),
    doLaserCorrections = cms.bool( True ),
    EBRecalibRecHitCollection = cms.string( "phiSymEcalRecHitsEB" ),
    doIntercalib = cms.bool( True ),
    EERecalibRecHitCollection = cms.string( "phiSymEcalRecHitsEE" )
)
process.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
process.hltL1sL1SingleEG20ORL1SingleEG22 = cms.EDFilter( "HLTLevel1GTSeed",
    #L1_SingleEG22 does not exist in L1Menu_Collisions2015_25ns_v2
	#L1SeedsLogicalExpression = cms.string( "L1_SingleEG20 OR L1_SingleEG22" ),
    L1SeedsLogicalExpression = cms.string( "L1_SingleEG25" ),
    saveTags = cms.bool( True ),
    L1MuonCollectionTag = cms.InputTag( "hltL1extraParticles" ),
    L1UseL1TriggerObjectMaps = cms.bool( True ),
    L1UseAliasesForSeeding = cms.bool( True ),
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    L1CollectionsTag = cms.InputTag( "hltL1extraParticles" ),
    L1NrBxInEvent = cms.int32( 3 ),
    L1GtObjectMapTag = cms.InputTag( "hltL1GtObjectMap" ),
    L1TechTriggerSeeding = cms.bool( False )
)
process.hltPreEle27WPXXEle15WPYYtrackless = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtDigis" ),
    offset = cms.uint32( 0 )
)
process.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" ),
    ESdigiCollection = cms.string( "" )
)
process.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)
process.hltRechitInRegionsECAL = cms.EDProducer( "EgammaHLTRechitInRegionsProducer",
    l1LowerThr = cms.double( 5.0 ),
    doIsolated = cms.bool( True ),
    useUncalib = cms.bool( False ),
    regionEtaMargin = cms.double( 0.14 ),
    ecalhitLabels = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    regionPhiMargin = cms.double( 0.4 ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles','NonIsolated' ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    productLabels = cms.vstring( 'EcalRecHitsEB',
      'EcalRecHitsEE' ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles','Isolated' )
)
process.hltRechitInRegionsES = cms.EDProducer( "EgammaHLTRechitInRegionsProducer",
    l1LowerThr = cms.double( 5.0 ),
    doIsolated = cms.bool( True ),
    useUncalib = cms.bool( False ),
    regionEtaMargin = cms.double( 0.14 ),
    ecalhitLabels = cms.VInputTag( 'hltEcalPreshowerRecHit:EcalRecHitsES' ),
    regionPhiMargin = cms.double( 0.4 ),
    l1TagNonIsolated = cms.InputTag( 'hltL1extraParticles','NonIsolated' ),
    l1UpperThr = cms.double( 999.0 ),
    l1LowerThrIgnoreIsolation = cms.double( 0.0 ),
    productLabels = cms.vstring( 'EcalRecHitsES' ),
    l1TagIsolated = cms.InputTag( 'hltL1extraParticles','Isolated' )
)
process.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.08 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEBRecHitCreator" )
      ),
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.3 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEERecHitCreator" )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
process.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsES','EcalRecHitsES' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        ),
        name = cms.string( "PFPSRecHitCreator" )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
process.hltParticleFlowClusterPSL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 0.3 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "PS1" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        ),
        cms.PSet(  detector = cms.string( "PS2" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSL1Seeded" )
)
process.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      positionCalcForConvergence = cms.PSet( 
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 ),
        minAllowedNormalization = cms.double( 0.0 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        T0_ES = cms.double( 1.2 ),
        T0_EE = cms.double( 3.1 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 1.5 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "ECAL_BARREL" ),
          recHitEnergyNorm = cms.double( 0.08 )
        ),
        cms.PSet(  detector = cms.string( "ECAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.3 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet( 
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 ),
      minAllowedNormalization = cms.double( 0.0 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      T0_ES = cms.double( 1.2 ),
      T0_EE = cms.double( 3.1 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( 0.04 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 10.0 ),
    minS4S1_b = cms.double( -0.024 ),
    singleSpikeThresh = cms.double( 4.0 ),
    detector = cms.string( "ECAL_BARREL" ),
    minS4S1_a = cms.double( 0.04 ),
    energyThresholdModifier = cms.double( 2.0 )
  ),
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.0125 ),
    singleSpikeThresh = cms.double( 15.0 ),
    detector = cms.string( "ECAL_ENDCAP" ),
    minS4S1_a = cms.double( 0.02 ),
    energyThresholdModifier = cms.double( 2.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 8 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.6 ),
          seedingThresholdPt = cms.double( 0.15 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 0.23 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALL1Seeded" )
)
process.hltParticleFlowClusterECALL1Seeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    minimumPSEnergy = cms.double( 0.0 ),
    inputPS = cms.InputTag( "hltParticleFlowClusterPSL1Seeded" ),
    energyCorrector = cms.PSet( 
      applyCrackCorrections = cms.bool( False ),
      algoName = cms.string( "PFClusterEMEnergyCorrector" )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedL1Seeded" )
)
process.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    thresh_PFClusterBarrel = cms.double( 4.0 ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( False ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    thresh_PFClusterEndcap = cms.double( 4.0 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    verbose = cms.untracked.bool( False ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      regressionKeyEE = cms.string( "pfscecal_EECorrection_offline" ),
      ecalRecHitsEE = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_offline" ),
      vertexCollection = cms.InputTag( "offlinePrimaryVertices" )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    thresh_PFClusterSeedBarrel = cms.double( 4.0 ),
    ClusteringType = cms.string( "Mustache" ),
    EnergyWeight = cms.string( "Raw" ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    thresh_PFClusterSeedEndcap = cms.double( 4.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 5.0 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
process.hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEGL1SingleEG20ORL1SingleEG22Filter = cms.EDFilter( "HLTEgammaL1MatchFilterRegional",
    doIsolated = cms.bool( False ),
    endcap_end = cms.double( 2.65 ),
    saveTags = cms.bool( True ),
    region_eta_size_ecap = cms.double( 1.0 ),
    barrel_end = cms.double( 1.4791 ),
    l1IsolatedTag = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidates" ),
    region_phi_size = cms.double( 1.044 ),
    region_eta_size = cms.double( 0.522 ),
    L1SeedFilterTag = cms.InputTag( "hltL1sL1SingleEG20ORL1SingleEG22" ),
    candNonIsolatedTag = cms.InputTag( "" ),
    l1NonIsolatedTag = cms.InputTag( 'hltL1extraParticles','NonIsolated' ),
    ncandcut = cms.int32( 1 )
)
process.hltEG27WPXXEtFilter = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    inputTag = cms.InputTag( "hltEGL1SingleEG20ORL1SingleEG22Filter" ),
    etcutEB = cms.double( 5.0 ),
    etcutEE = cms.double( 5.0 ),
	#ORIGINAL etcutEB = cms.double( 27.0 ),
    #ORIGINAL etcutEE = cms.double( 27.0 ),
    ncandcut = cms.int32( 1 )
)
process.hltEgammaClusterShape = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    ecalRechitEB = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltEle27WPXXClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEE = cms.double( 0.031 ),
    thrRegularEE = cms.double( 0.31 ),
	thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEB = cms.double( 0.011 ),
    thrRegularEB = cms.double( 0.11 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaClusterShape','sigmaIEtaIEta5x5' ),
    candTag = cms.InputTag( "hltEG27WPXXEtFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    UnpackZDC = cms.untracked.bool( True ),
    FilterDataQuality = cms.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackTTP = cms.untracked.bool( False ),
    lastSample = cms.int32( 9 ),
    firstSample = cms.int32( 0 )
)
process.hltHbhereco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    digistat = cms.PSet(  ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    recoParamsFromDB = cms.bool( True ),
    Subdetector = cms.string( "HBHE" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    setPulseShapeFlags = cms.bool( False ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet( 
      ignorelowest = cms.bool( True ),
      win_offset = cms.double( 0.0 ),
      ignorehighest = cms.bool( False ),
      win_gain = cms.double( 1.0 ),
      tfilterEnvelope = cms.vdouble( 4.0, 12.04, 13.0, 10.56, 23.5, 8.82, 37.0, 7.38, 56.0, 6.3, 81.0, 5.64, 114.5, 5.44, 175.5, 5.38, 350.5, 5.14 )
    ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet( 
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 ),
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet( 
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      )
    ),
    hscpParameters = cms.PSet( 
      slopeMax = cms.double( -0.6 ),
      r1Max = cms.double( 1.0 ),
      r1Min = cms.double( 0.15 ),
      TimingEnergyThreshold = cms.double( 30.0 ),
      slopeMin = cms.double( -1.5 ),
      outerMin = cms.double( 0.0 ),
      outerMax = cms.double( 0.1 ),
      fracLeaderMin = cms.double( 0.4 ),
      r2Min = cms.double( 0.1 ),
      r2Max = cms.double( 0.5 ),
      fracLeaderMax = cms.double( 0.7 )
    )
)
process.hltHfreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 24 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 2 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet( 
      hflongEthresh = cms.double( 40.0 ),
      hflongMinWindowTime = cms.vdouble( -10.0 ),
      hfshortEthresh = cms.double( 40.0 ),
      hflongMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMaxWindowTime = cms.vdouble( 10.0 ),
      hfshortMinWindowTime = cms.vdouble( -12.0 )
    ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 1 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet( 
      hfTimingTrustLevel2 = cms.int32( 4 ),
      hfTimingTrustLevel1 = cms.int32( 1 )
    ),
    PETstat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_R_29 = cms.vdouble( 0.8 ),
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      flagsToSkip = cms.int32( 0 ),
      short_R = cms.vdouble( 0.8 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      long_R = cms.vdouble( 0.98 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    digistat = cms.PSet( 
      HFdigiflagFirstSample = cms.int32( 1 ),
      HFdigiflagMinEthreshold = cms.double( 40.0 ),
      HFdigiflagSamplesToAdd = cms.int32( 3 ),
      HFdigiflagExpectedPeak = cms.int32( 2 ),
      HFdigiflagCoef = cms.vdouble( 0.93, -0.012667, -0.38275 )
    ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet( 
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      flagsToSkip = cms.int32( 16 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    correctForPhaseContainment = cms.bool( False ),
    correctForTimeslew = cms.bool( False ),
    setNoiseFlags = cms.bool( True ),
    correctTiming = cms.bool( False ),
    recoParamsFromDB = cms.bool( True ),
    Subdetector = cms.string( "HF" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    setPulseShapeFlags = cms.bool( False ),
    firstSample = cms.int32( 2 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet(  ),
    hscpParameters = cms.PSet(  )
)
process.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    setSaturationFlags = cms.bool( False ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    digistat = cms.PSet(  ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    recoParamsFromDB = cms.bool( True ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    setPulseShapeFlags = cms.bool( False ),
    firstSample = cms.int32( 4 ),
    setTimingShapedCutsFlags = cms.bool( False ),
    timingshapedcutsParameters = cms.PSet(  ),
    pulseShapeParameters = cms.PSet(  ),
    flagParameters = cms.PSet(  ),
    hscpParameters = cms.PSet(  )
)
process.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HEDWeights = cms.vdouble(  ),
    HEDGrid = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    EBThreshold = cms.double( 0.07 ),
    UseRejectedHitsOnly = cms.bool( False ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
process.hltRegionalTowerForEgamma = cms.EDProducer( "EgammaHLTCaloTowerProducer",
    L1NonIsoCand = cms.InputTag( 'hltL1extraParticles','NonIsolated' ),
    EMin = cms.double( 0.8 ),
    EtMin = cms.double( 0.5 ),
    L1IsoCand = cms.InputTag( 'hltL1extraParticles','Isolated' ),
    useTowersInCone = cms.double( 0.8 ),
    towerCollection = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltParticleFlowRecHitHCALForEgamma = cms.EDProducer( "PFCTRecHitProducer",
    ECAL_Compensate = cms.bool( False ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    weight_HFhad = cms.double( 1.0 ),
    ApplyPulseDPG = cms.bool( False ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitCaloTowerNavigator" ) ),
    ECAL_Threshold = cms.double( 10.0 ),
    ApplyTimeDPG = cms.bool( False ),
    caloTowers = cms.InputTag( "hltRegionalTowerForEgamma" ),
    hcalRecHitsHBHE = cms.InputTag( "hltHbhereco" ),
    LongFibre_Fraction = cms.double( 0.1 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    HcalMaxAllowedHFLongShortSev = cms.int32( 9 ),
    thresh_Barrel = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32( 9 ),
    HF_Calib_29 = cms.double( 1.07 ),
    LongFibre_Cut = cms.double( 120.0 ),
    EM_Depth = cms.double( 22.0 ),
    weight_HFem = cms.double( 1.0 ),
    LongShortFibre_Cut = cms.double( 1.0E9 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    HCAL_Calib = cms.bool( True ),
    thresh_HF = cms.double( 0.4 ),
    HcalMaxAllowedHFDigiTimeSev = cms.int32( 9 ),
    thresh_Endcap = cms.double( 0.4 ),
    HcalMaxAllowedChannelStatusSev = cms.int32( 9 ),
    hcalRecHitsHF = cms.InputTag( "hltHfreco" ),
    ShortFibre_Cut = cms.double( 60.0 ),
    ApplyLongShortDPG = cms.bool( True ),
    HF_Calib = cms.bool( True ),
    HAD_Depth = cms.double( 47.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    HCAL_Calib_29 = cms.double( 1.35 )
)
process.hltParticleFlowClusterHCALForEgamma = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          recHitEnergyNorm = cms.double( 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_BARREL1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  algoName = cms.string( "RBXAndHPDCleaner" )      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.8 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.1 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHCALForEgamma" )
)
process.hltFixedGridRhoFastjetAllCaloForMuons = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 2.5 ),
    pfCandidatesTag = cms.InputTag( "hltTowerMakerForAll" )
)
process.hltEgammaHoverE = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltEle27WPXXHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    #ORIGINAL thrOverEEE = cms.double( 0.075 ),
    thrOverEEE = cms.double( 0.75 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    #ORIGINAL thrOverEEB = cms.double( 0.1 ),
    thrOverEEB = cms.double( 1.0 ),
	thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHoverE" ),
    candTag = cms.InputTag( "hltEle27WPXXClusterShapeFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEgammaEcalPFClusterIso = cms.EDProducer( "EgammaHLTEcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    effectiveAreaBarrel = cms.double( 0.149 ),
    etaStripBarrel = cms.double( 0.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    pfClusterProducer = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( True ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.097 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle27WPXXEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    #ORIGINAL thrOverEEE = cms.double( 0.11 ),
    thrOverEEE = cms.double( 1.1 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    #ORIGINAL thrOverEEB = cms.double( 0.16 ),
    thrOverEEB = cms.double( 1.6 ),
	thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle27WPXXHEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEgammaHcalPFClusterIso = cms.EDProducer( "EgammaHLTHcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    useHF = cms.bool( False ),
    effectiveAreaBarrel = cms.double( 0.06 ),
    etaStripBarrel = cms.double( 0.0 ),
    pfClusterProducerHFHAD = cms.InputTag( "hltParticleFlowClusterHFHADForEgamma" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    pfClusterProducerHCAL = cms.InputTag( "hltParticleFlowClusterHCALForEgamma" ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( True ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.089 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    rhoMax = cms.double( 9.9999999E7 ),
    pfClusterProducerHFEM = cms.InputTag( "hltParticleFlowClusterHFEMForEgamma" ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle27WPXXHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    #ORIGINAL thrOverEEE = cms.double( 0.11 ),
    thrOverEEE = cms.double( 1.1 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    #ORIGINAL thrOverEEB = cms.double( 0.11 ),
    thrOverEEB = cms.double( 1.1 ),
	thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIso" ),
    candTag = cms.InputTag( "hltEle27WPXXEcalIsoFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    CheckPixelOrder = cms.bool( False ),
    IncludeErrors = cms.bool( False ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ErrorList = cms.vint32(  ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    UserErrorList = cms.vint32(  )
)
process.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    maxNumberOfClusters = cms.int32( 20000 ),
    VCaltoElectronGain = cms.int32( 65 ),
    MissCalibrate = cms.untracked.bool( True ),
    SplitClusters = cms.bool( False ),
    VCaltoElectronOffset = cms.int32( -414 ),
    payloadType = cms.string( "HLT" ),
    SeedThreshold = cms.int32( 1000 ),
    ClusterThreshold = cms.double( 4000.0 )
)
process.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
process.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
process.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
process.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    DoAPVEmulatorCheck = cms.bool( False ),
    Algorithms = cms.PSet( 
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      PedestalSubtractionFedMode = cms.bool( True ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      useCMMeanMap = cms.bool( False )
    ),
    Clusterizer = cms.PSet( 
      ChannelThreshold = cms.double( 2.0 ),
      MaxSequentialBad = cms.uint32( 1 ),
      MaxSequentialHoles = cms.uint32( 0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      MaxAdjacentBad = cms.uint32( 0 ),
      QualityLabel = cms.string( "" ),
      SeedThreshold = cms.double( 3.0 ),
      ClusterThreshold = cms.double( 5.0 ),
      setDetId = cms.bool( True ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    onDemand = cms.bool( True )
)
process.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag(  ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" ),
    pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" )
)
process.hltMixedLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix2_pos+TEC1_pos',
      'FPix2_pos+TEC2_pos',
      'TEC1_pos+TEC2_pos',
      'TEC2_pos+TEC3_pos',
      'FPix2_neg+TEC1_neg',
      'FPix2_neg+TEC2_neg',
      'TEC1_neg+TEC2_neg',
      'TEC2_neg+TEC3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet( 
      useRingSlector = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      minRing = cms.int32( 1 ),
      maxRing = cms.int32( 1 ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltEgammaElectronPixelSeeds = cms.EDProducer( "ElectronSeedProducer",
    endcapSuperClusters = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    SeedConfiguration = cms.PSet( 
      searchInTIDTEC = cms.bool( True ),
      HighPtThreshold = cms.double( 35.0 ),
      r2MinF = cms.double( -0.15 ),
      OrderedHitsFactoryPSet = cms.PSet( 
        maxElement = cms.uint32( 0 ),
        ComponentName = cms.string( "StandardHitPairGenerator" ),
        useOnDemandTracker = cms.untracked.int32( 0 ),
        SeedingLayers = cms.InputTag( "hltMixedLayerPairs" )
      ),
      DeltaPhi1Low = cms.double( 0.23 ),
      DeltaPhi1High = cms.double( 0.08 ),
      ePhiMin1 = cms.double( -0.08 ),
      #PhiMin2 = cms.double( -0.004 ),
      LowPtThreshold = cms.double( 3.0 ),
      RegionPSet = cms.PSet( 
        deltaPhiRegion = cms.double( 0.4 ),
        originHalfLength = cms.double( 15.0 ),
        useZInVertex = cms.bool( True ),
        deltaEtaRegion = cms.double( 0.1 ),
        ptMin = cms.double( 1.5 ),
        originRadius = cms.double( 0.2 ),
        VertexProducer = cms.InputTag( "dummyVertices" )
      ),
      #maxHOverE = cms.double( 999999.0 ),
      dynamicPhiRoad = cms.bool( False ),
      ePhiMax1 = cms.double( 0.04 ),
      #DeltaPhi2 = cms.double( 0.004 ),
      measurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
      SizeWindowENeg = cms.double( 0.675 ),
      nSigmasDeltaZ1 = cms.double( 5.0 ),
      rMaxI = cms.double( 0.2 ),
      #PhiMax2 = cms.double( 0.004 ),
      preFilteredSeeds = cms.bool( True ),
      r2MaxF = cms.double( 0.15 ),
      pPhiMin1 = cms.double( -0.04 ),
      initialSeeds = cms.InputTag( "noSeedsHere" ),
      pPhiMax1 = cms.double( 0.08 ),
      #hbheModule = cms.string( "hbhereco" ),
      SCEtCut = cms.double( 3.0 ),
      z2MaxB = cms.double( 0.09 ),
      fromTrackerSeeds = cms.bool( True ),
      hcalRecHits = cms.InputTag( "hltHbhereco" ),
      z2MinB = cms.double( -0.09 ),
      #hbheInstance = cms.string( "" ),
      rMinI = cms.double( -0.2 ),
      hOverEConeSize = cms.double( 0.0 ),
      hOverEHBMinE = cms.double( 999999.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      applyHOverECut = cms.bool( False ),
      hOverEHFMinE = cms.double( 999999.0 ),
      measurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
      #new additions are PhiMin2B to SeedCreatorPSet
	  PhiMin2B = cms.double( -0.004 ),
      PhiMin2F = cms.double( -0.004 ),
      PhiMax2B = cms.double( 0.004 ),
      PhiMax2F = cms.double( 0.004 ),
      DeltaPhi2B = cms.double( 0.004 ),
      DeltaPhi2F = cms.double( 0.004 ),
      SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
    ),
    barrelSuperClusters = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' )
)
process.hltEle27WPXXPixelMatchFilter = cms.EDFilter( "HLTElectronPixelMatchFilter",
    saveTags = cms.bool( True ),
    s2_threshold = cms.double( 0.4 ),
    npixelmatchcut = cms.double( 1.0 ),
    tanhSO10InterThres = cms.double( 1.0 ),
    doIsolated = cms.bool( True ),
    s_a_phi1B = cms.double( 0.0069 ),
    s_a_phi1F = cms.double( 0.0076 ),
    s_a_phi1I = cms.double( 0.0088 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    candTag = cms.InputTag( "hltEle27WPXXHcalIsoFilter" ),
    tanhSO10ForwardThres = cms.double( 1.0 ),
    L1IsoPixelSeedsTag = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    L1NonIsoCand = cms.InputTag( "" ),
    ncandcut = cms.int32( 1 ),
    tanhSO10BarrelThres = cms.double( 0.35 ),
    s_a_rF = cms.double( 0.04 ),
    L1NonIsoPixelSeedsTag = cms.InputTag( "" ),
    s_a_rI = cms.double( 0.027 ),
    s_a_phi2I = cms.double( 7.0E-4 ),
    useS = cms.bool( False ),
    s_a_phi2B = cms.double( 3.7E-4 ),
    s_a_zB = cms.double( 0.012 ),
    s_a_phi2F = cms.double( 0.00906 )
)
process.hltEgammaCkfTrackCandidatesForGSF = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltEgammaElectronPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( True ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 1000000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetTrajectoryBuilderForElectrons" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltEgammaGsfTracks = cms.EDProducer( "GsfTrackProducer",
    src = cms.InputTag( "hltEgammaCkfTrackCandidatesForGSF" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    producer = cms.string( "" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPGsfElectronFittingSmoother" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    AlgorithmName = cms.string( "gsf" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    Propagator = cms.string( "hltESPFwdElectronPropagator" )
)
process.hltEgammaGsfElectrons = cms.EDProducer( "EgammaHLTPixelMatchElectronProducers",
    BSProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    UseGsfTracks = cms.bool( True ),
    TrackProducer = cms.InputTag( "" ),
    GsfTrackProducer = cms.InputTag( "hltEgammaGsfTracks" )
)
process.hltEgammaGsfTrackVars = cms.EDProducer( "EgammaHLTGsfTrackVarProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    upperTrackNrToRemoveCut = cms.int32( 9999 ),
    lowerTrackNrToRemoveCut = cms.int32( -1 ),
    inputCollection = cms.InputTag( "hltEgammaGsfTracks" )
)
process.hltEle27WPXXOneOEMinusOneOPFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEE = cms.double( 0.009 ),
    thrRegularEE = cms.double( 0.3 ),
	thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEB = cms.double( 0.012 ),
    thrRegularEB = cms.double( 0.4 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','OneOESuperMinusOneOP' ),
    candTag = cms.InputTag( "hltEle27WPXXPixelMatchFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEle27WPXXDetaFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEE = cms.double( 0.01 ),
    thrRegularEE = cms.double( 0.1 ),
	thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEB = cms.double( 0.005 ),
    thrRegularEB = cms.double( 0.05 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Deta' ),
    candTag = cms.InputTag( "hltEle27WPXXOneOEMinusOneOPFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEle27WPXXDphiFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEE = cms.double( 0.03 ),
    thrRegularEE = cms.double( 0.3 ),
	thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    thrOverEEB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEB = cms.double( 0.03 ),
    thrRegularEB = cms.double( 0.3 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( 'hltEgammaGsfTrackVars','Dphi' ),
    candTag = cms.InputTag( "hltEle27WPXXDetaFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltElectronsVertex = cms.EDProducer( "VertexFromTrackProducer",
    verbose = cms.untracked.bool( False ),
    useTriggerFilterElectrons = cms.bool( False ),
    beamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
    isRecoCandidate = cms.bool( True ),
    trackLabel = cms.InputTag( "hltEgammaGsfElectrons" ),
    useTriggerFilterMuons = cms.bool( False ),
    useBeamSpot = cms.bool( True ),
    vertexLabel = cms.InputTag( "None" ),
    triggerFilterElectronsSrc = cms.InputTag( "None" ),
    triggerFilterMuonsSrc = cms.InputTag( "None" ),
    useVertex = cms.bool( False )
)
process.hltPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      useErrorsFromParam = cms.bool( True ),
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 )
    ),
    TIB = cms.PSet(  )
)
process.hltPixelTracksElectrons = cms.EDProducer( "PixelTrackProducer",
    FilterPSet = cms.PSet( 
      chi2 = cms.double( 1000.0 ),
      nSigmaTipMaxTolerance = cms.double( 0.0 ),
      ComponentName = cms.string( "PixelTrackFilterByKinematics" ),
      nSigmaInvPtTolerance = cms.double( 0.0 ),
      ptMin = cms.double( 0.1 ),
      tipMax = cms.double( 1.0 )
    ),
    useFilterWithES = cms.bool( False ),
    passLabel = cms.string( "Pixel triplet primary tracks with vertex constraint" ),
    FitterPSet = cms.PSet( 
      ComponentName = cms.string( "PixelFitterByHelixProjections" ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      fixImpactParameter = cms.double( 0.0 )
    ),
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "GlobalTrackingRegionWithVerticesProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.2 ),
        ptMin = cms.double( 0.9 ),
        originHalfLength = cms.double( 0.3 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        useFixedError = cms.bool( True ),
        sigmaZVertex = cms.double( 3.0 ),
        fixedError = cms.double( 0.2 ),
        VertexCollection = cms.InputTag( "hltElectronsVertex" ),
        useFoundVertices = cms.bool( True ),
        nSigmaZ = cms.double( 4.0 ),
        useFakeVertices = cms.bool( True )
      )
    ),
    CleanerPSet = cms.PSet(  ComponentName = cms.string( "PixelTrackCleanerBySharedHits" ) ),
    OrderedHitsFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.06 ),
        useMultScattering = cms.bool( True ),
        SeedComparitorPSet = cms.PSet( 
          ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
          clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
        ),
        extraHitRZtolerance = cms.double( 0.06 ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" )
      ),
      SeedingLayers = cms.InputTag( "hltPixelLayerTriplets" )
    )
)
process.hltPixelVerticesElectrons = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparer" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracksElectrons" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
#HLTSeedFromProtoTracks is a new addition
process.HLTSeedFromProtoTracks = cms.PSet( 
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  MinOneOverPtError = cms.double( 1.0 ),
  magneticField = cms.string( "ParabolicMf" ),
  TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  forceKinematicWithRegionDirection = cms.bool( False )
)
process.hltIter0ElectronsPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( True ),
	#SeedCreatorPSet is a new addition
	SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
	InputVertexCollection = cms.InputTag( "hltPixelVerticesElectrons" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltPixelTracksElectrons" ),
    originRadius = cms.double( 0.1 )
)
process.hltIter0ElectronsCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0ElectronsPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter0ElectronsCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0ElectronsCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "iter0IsoElectron" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter0ElectronsTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter0ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesElectrons" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter1ElectronsClustersRefRemoval = cms.EDProducer( "HLTTrackClusterRemoverNew",
    doStrip = cms.bool( True ),
    doStripChargeCheck = cms.bool( False ),
    trajectories = cms.InputTag( "hltIter0ElectronsTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    Common = cms.PSet(  maxChi2 = cms.double( 9.0 ) ),
    doPixel = cms.bool( True )
)
process.hltIter1ElectronsMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
process.hltIter1ElectronsPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0051 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0027 )
    ),
    TIB = cms.PSet(  )
)
process.hltIter1ElectronsPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.05 ),
        ptMin = cms.double( 0.5 ),
        input = cms.InputTag( "hltEgammaCandidates" ),
        maxNRegions = cms.int32( 10 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        vertexCollection = cms.InputTag( "hltPixelVerticesElectrons" ),
        zErrorBeamSpot = cms.double( 24.2 ),
        deltaEta = cms.double( 0.5 ),
        deltaPhi = cms.double( 0.5 ),
        nSigmaZVertex = cms.double( 3.0 ),
        nSigmaZBeamSpot = cms.double( 4.0 ),
        mode = cms.string( "VerticesFixed" ),
        maxNVertices = cms.int32( 3 ),
        zErrorVetex = cms.double( 0.2 )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitTripletGenerator" ),
      GeneratorPSet = cms.PSet( 
        useBending = cms.bool( True ),
        useFixedPreFiltering = cms.bool( False ),
        maxElement = cms.uint32( 100000 ),
        phiPreFiltering = cms.double( 0.3 ),
        extraHitRPhitolerance = cms.double( 0.032 ),
        useMultScattering = cms.bool( True ),
        ComponentName = cms.string( "PixelTripletHLTGenerator" ),
        extraHitRZtolerance = cms.double( 0.037 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltIter1ElectronsPixelLayerTriplets" )
    ),
    #SeedCreatorPSet = cms.PSet( 
    #  ComponentName = cms.string( "SeedFromConsecutiveHitsTripletOnlyCreator" ),
    #  propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
    #),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsTripletOnlyCreator" ) ),
    #TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
)
process.hltIter1ElectronsCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter1ElectronsPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1ElectronsMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter1ElectronsCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter1ElectronsCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1ElectronsMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "iter1IsoElectron" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter1ElectronsTrackSelectionHighPurityLoose = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.9, 3.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.8, 3.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesElectrons" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.9, 3.0 ),
    d0_par1 = cms.vdouble( 0.85, 3.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter1ElectronsTrackSelectionHighPurityTight = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 5 ),
    chi2n_par = cms.double( 0.4 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 1.0, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 1.0, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter1ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesElectrons" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 1.0, 4.0 ),
    d0_par1 = cms.vdouble( 1.0, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter1ElectronsTrackSelectionHighPurity = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltIter1ElectronsTrackSelectionHighPurityLoose" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltIter1ElectronsTrackSelectionHighPurityTight" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
process.hltIter1MergedForElectrons = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltIter0ElectronsTrackSelectionHighPurity" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltIter1ElectronsTrackSelectionHighPurity" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
process.hltIter2ElectronsClustersRefRemoval = cms.EDProducer( "HLTTrackClusterRemoverNew",
    doStrip = cms.bool( True ),
    doStripChargeCheck = cms.bool( False ),
    trajectories = cms.InputTag( "hltIter1ElectronsTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter1ElectronsClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    Common = cms.PSet(  maxChi2 = cms.double( 16.0 ) ),
    doPixel = cms.bool( True )
)
process.hltIter2ElectronsMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
process.hltIter2ElectronsPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix2+BPix3',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.0036 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0051 )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet( 
      HitProducer = cms.string( "hltSiPixelRecHits" ),
      hitErrorRZ = cms.double( 0.006 ),
      useErrorsFromParam = cms.bool( True ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ElectronsClustersRefRemoval" ),
      hitErrorRPhi = cms.double( 0.0027 )
    ),
    TIB = cms.PSet(  )
)
process.hltIter2ElectronsPixelSeeds = cms.EDProducer( "SeedGeneratorFromRegionHitsEDProducer",
    RegionFactoryPSet = cms.PSet( 
      ComponentName = cms.string( "CandidateSeededTrackingRegionsProducer" ),
      RegionPSet = cms.PSet( 
        precise = cms.bool( True ),
        originRadius = cms.double( 0.05 ),
        ptMin = cms.double( 1.2 ),
        deltaEta = cms.double( 0.5 ),
        deltaPhi = cms.double( 0.5 ),
        vertexCollection = cms.InputTag( "hltPixelVerticesElectrons" ),
        input = cms.InputTag( "hltEgammaCandidates" ),
        mode = cms.string( "VerticesFixed" ),
        maxNRegions = cms.int32( 10 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        maxNVertices = cms.int32( 3 ),
        zErrorBeamSpot = cms.double( 24.2 ),
        nSigmaZVertex = cms.double( 3.0 ),
        nSigmaZBeamSpot = cms.double( 4.0 ),
        zErrorVetex = cms.double( 0.2 )
      )
    ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    ClusterCheckPSet = cms.PSet( 
      PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
      MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
      doClusterCheck = cms.bool( False ),
      ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" ),
      MaxNumberOfPixelClusters = cms.uint32( 10000 )
    ),
    OrderedHitsFactoryPSet = cms.PSet( 
      maxElement = cms.uint32( 0 ),
      ComponentName = cms.string( "StandardHitPairGenerator" ),
      GeneratorPSet = cms.PSet( 
        maxElement = cms.uint32( 100000 ),
        SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) )
      ),
      SeedingLayers = cms.InputTag( "hltIter2ElectronsPixelLayerPairs" )
    ),
    #SeedCreatorPSet = cms.PSet( 
    #  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
    #  propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
    #),
    #TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" )
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromConsecutiveHitsCreator" ) )
)
process.hltIter2ElectronsCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2ElectronsPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet( 
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2ElectronsMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
process.hltIter2ElectronsCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2ElectronsCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2ElectronsMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "iter2IsoElectron" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( True ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
process.hltIter2ElectronsTrackSelectionHighPurity = cms.EDProducer( "AnalyticalTrackSelector",
    max_d0 = cms.double( 100.0 ),
    minNumber3DLayers = cms.uint32( 0 ),
    max_lostHitFraction = cms.double( 1.0 ),
    applyAbsCutsIfNoPV = cms.bool( False ),
    qualityBit = cms.string( "highPurity" ),
    minNumberLayers = cms.uint32( 3 ),
    chi2n_par = cms.double( 0.7 ),
    useVtxError = cms.bool( False ),
    nSigmaZ = cms.double( 3.0 ),
    dz_par2 = cms.vdouble( 0.4, 4.0 ),
    applyAdaptedPVCuts = cms.bool( True ),
    min_eta = cms.double( -9999.0 ),
    dz_par1 = cms.vdouble( 0.35, 4.0 ),
    copyTrajectories = cms.untracked.bool( True ),
    vtxNumber = cms.int32( -1 ),
    max_d0NoPV = cms.double( 100.0 ),
    keepAllTracks = cms.bool( False ),
    maxNumberLostLayers = cms.uint32( 1 ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    max_relpterr = cms.double( 9999.0 ),
    copyExtras = cms.untracked.bool( True ),
    max_z0NoPV = cms.double( 100.0 ),
    vertexCut = cms.string( "tracksSize>=3" ),
    max_z0 = cms.double( 100.0 ),
    useVertices = cms.bool( True ),
    min_nhits = cms.uint32( 0 ),
    src = cms.InputTag( "hltIter2ElectronsCtfWithMaterialTracks" ),
    max_minMissHitOutOrIn = cms.int32( 99 ),
    chi2n_no1Dmod_par = cms.double( 9999.0 ),
    vertices = cms.InputTag( "hltPixelVerticesElectrons" ),
    max_eta = cms.double( 9999.0 ),
    d0_par2 = cms.vdouble( 0.4, 4.0 ),
    d0_par1 = cms.vdouble( 0.3, 4.0 ),
    res_par = cms.vdouble( 0.003, 0.001 ),
    minHitsToBypassChecks = cms.uint32( 20 )
)
process.hltIter2MergedForElectrons = cms.EDProducer( "SimpleTrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    promoteTrackQuality = cms.bool( True ),
    MinPT = cms.double( 0.05 ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    allowFirstHitShare = cms.bool( True ),
    newQuality = cms.string( "confirmed" ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    TrackProducer1 = cms.string( "hltIter1MergedForElectrons" ),
    MinFound = cms.int32( 3 ),
    TrackProducer2 = cms.string( "hltIter2ElectronsTrackSelectionHighPurity" ),
    LostHitPenalty = cms.double( 20.0 ),
    FoundHitBonus = cms.double( 5.0 )
)
process.hltEgammaEleGsfTrackIso = cms.EDProducer( "EgammaHLTElectronTrackIsolationProducers",
    egTrkIsoStripEndcap = cms.double( 0.03 ),
    egTrkIsoVetoConeSizeBarrel = cms.double( 0.03 ),
    useGsfTrack = cms.bool( True ),
    useSCRefs = cms.bool( True ),
    trackProducer = cms.InputTag( "hltIter2MergedForElectrons" ),
    egTrkIsoStripBarrel = cms.double( 0.03 ),
    electronProducer = cms.InputTag( "hltEgammaGsfElectrons" ),
    egTrkIsoConeSize = cms.double( 0.3 ),
    egTrkIsoRSpan = cms.double( 999999.0 ),
    egTrkIsoVetoConeSizeEndcap = cms.double( 0.03 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidates" ),
    beamSpotProducer = cms.InputTag( "hltOnlineBeamSpot" ),
    egTrkIsoPtMin = cms.double( 1.0 ),
    egTrkIsoZSpan = cms.double( 0.15 )
)
process.hltEle27WPXXTrackIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    #ORIGINAL thrOverE2EE = cms.double( 0.125 ),
    thrOverE2EE = cms.double( 1.25 ),
	L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
	#thrOverE2EB = trackIso/(energy in EB)^2
	#it is pointless to have a cut on thrOverE2EB and thrOverEEB
	#with the same cut value
    #ORIGINAL thrOverE2EB = cms.double( 0.125 ),
    thrOverE2EB = cms.double( 1.25 ),
	thrRegularEE = cms.double( -1.0 ),
    #thrOverEEE = trackIso/(energy in EE)
	#ORIGINAL thrOverEEE = cms.double( 0.125 ),
    thrOverEEE = cms.double( 1.25 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidates" ),
    #ORIGINAL thrOverEEB = cms.double( 0.125 ),
    thrOverEEB = cms.double( 1.25 ),
	thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 1 ),
    isoTag = cms.InputTag( "hltEgammaEleGsfTrackIso" ),
    candTag = cms.InputTag( "hltEle27WPXXDphiFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltParticleFlowRecHitECALUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.08 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEBRecHitCreator" )
      ),
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 0.3 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          ),
          cms.PSet(  timingCleaning = cms.bool( True ),
            topologicalCleaning = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            skipTTRecoveredHits = cms.bool( True ),
            name = cms.string( "PFRecHitQTestECAL" )
          )
        ),
        name = cms.string( "PFEERecHitCreator" )
      )
    ),
    navigator = cms.PSet( 
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
process.hltParticleFlowRecHitPSUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet( 
      cms.PSet(  src = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
        qualityTests = cms.VPSet( 
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        ),
        name = cms.string( "PFPSRecHitCreator" )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
process.hltParticleFlowClusterPSUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      minFracTot = cms.double( 1.0E-20 ),
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 0.3 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "PS1" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        ),
        cms.PSet(  detector = cms.string( "PS2" ),
          recHitEnergyNorm = cms.double( 6.0E-5 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.2E-4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSUnseeded" )
)
process.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      positionCalcForConvergence = cms.PSet( 
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 ),
        minAllowedNormalization = cms.double( 0.0 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        T0_ES = cms.double( 1.2 ),
        T0_EE = cms.double( 3.1 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
      ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 1.5 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "ECAL_BARREL" ),
          recHitEnergyNorm = cms.double( 0.08 )
        ),
        cms.PSet(  detector = cms.string( "ECAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.3 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.08 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet( 
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 ),
      minAllowedNormalization = cms.double( 0.0 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      T0_ES = cms.double( 1.2 ),
      T0_EE = cms.double( 3.1 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" )
    ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( 0.04 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 10.0 ),
    minS4S1_b = cms.double( -0.024 ),
    singleSpikeThresh = cms.double( 4.0 ),
    detector = cms.string( "ECAL_BARREL" ),
    minS4S1_a = cms.double( 0.04 ),
    energyThresholdModifier = cms.double( 2.0 )
  ),
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 3.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.0125 ),
    singleSpikeThresh = cms.double( 15.0 ),
    detector = cms.string( "ECAL_ENDCAP" ),
    minS4S1_a = cms.double( 0.02 ),
    energyThresholdModifier = cms.double( 2.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 8 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.6 ),
          seedingThresholdPt = cms.double( 0.15 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 0.23 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALUnseeded" )
)
process.hltParticleFlowClusterECALUnseeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    minimumPSEnergy = cms.double( 0.0 ),
    inputPS = cms.InputTag( "hltParticleFlowClusterPSUnseeded" ),
    energyCorrector = cms.PSet( 
      applyCrackCorrections = cms.bool( False ),
      algoName = cms.string( "PFClusterEMEnergyCorrector" )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedUnseeded" )
)
process.hltParticleFlowSuperClusterECALUnseeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    thresh_PFClusterBarrel = cms.double( 4.0 ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( False ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    thresh_PFClusterEndcap = cms.double( 4.0 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    verbose = cms.untracked.bool( False ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet( 
      regressionKeyEE = cms.string( "pfscecal_EECorrection_offline" ),
      ecalRecHitsEE = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_offline" ),
      vertexCollection = cms.InputTag( "offlinePrimaryVertices" )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
    thresh_PFClusterSeedBarrel = cms.double( 4.0 ),
    ClusteringType = cms.string( "Mustache" ),
    EnergyWeight = cms.string( "Raw" ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    thresh_PFClusterSeedEndcap = cms.double( 4.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 5.0 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
process.hltEgammaCandidatesUnseeded = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALUnseeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALUnseeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)
process.hltEgammaCandidatesWrapperUnseeded = cms.EDFilter( "HLTEgammaTriggerFilterObjectWrapper",
    doIsolated = cms.bool( True ),
    saveTags = cms.bool( True ),
    candIsolatedTag = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    candNonIsolatedTag = cms.InputTag( "" )
)
process.hltEG15WPYYtracklessEtFilterUnseeded = cms.EDFilter( "HLTEgammaEtFilter",
    saveTags = cms.bool( True ),
    L1NonIsoCand = cms.InputTag( "" ),
    relaxed = cms.untracked.bool( False ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    inputTag = cms.InputTag( "hltEgammaCandidatesWrapperUnseeded" ),
    #ORIGINAL etcutEB = cms.double( 15.0 ),
    #ORIGINAL etcutEE = cms.double( 15.0 ),
    etcutEB = cms.double( 2.0 ),
    etcutEE = cms.double( 2.0 ),
	ncandcut = cms.int32( 2 )
)
process.hltEgammaClusterShapeUnseeded = cms.EDProducer( "EgammaHLTClusterShapeProducer",
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    ecalRechitEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
    ecalRechitEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
    isIeta = cms.bool( True )
)
process.hltEle15WPYYtracklessClusterShapeFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEE = cms.double( 0.031 ),
    thrRegularEE = cms.double( 0.15 ),
	thrOverEEE = cms.double( -1.0 ),
    L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    thrOverEEB = cms.double( -1.0 ),
    #ORIGINAL thrRegularEB = cms.double( 0.011 ),
    thrRegularEB = cms.double( 0.15 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaClusterShapeUnseeded" ),
    candTag = cms.InputTag( "hltEG15WPYYtracklessEtFilterUnseeded" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEgammaEcalPFClusterIsoUnseeded = cms.EDProducer( "EgammaHLTEcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    effectiveAreaBarrel = cms.double( 0.149 ),
    etaStripBarrel = cms.double( 0.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    pfClusterProducer = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( True ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.097 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    rhoMax = cms.double( 9.9999999E7 ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15WPYYtracklessEcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    #ORIGINAL thrOverEEE = cms.double( 0.2 ),
    thrOverEEE = cms.double( 1.0 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    #ORIGINAL thrOverEEB = cms.double( 0.2 ),
    thrOverEEB = cms.double( 1.0 ),
    thrRegularEB = cms.double( -1.0 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaEcalPFClusterIsoUnseeded" ),
    candTag = cms.InputTag( "hltEle15WPYYtracklessClusterShapeFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltParticleFlowRecHitHCALForEgammaUnseeded = cms.EDProducer( "PFCTRecHitProducer",
    ECAL_Compensate = cms.bool( False ),
    ECAL_Dead_Code = cms.uint32( 10 ),
    MinLongTiming_Cut = cms.double( -5.0 ),
    ECAL_Compensation = cms.double( 0.5 ),
    MaxLongTiming_Cut = cms.double( 5.0 ),
    weight_HFhad = cms.double( 1.0 ),
    ApplyPulseDPG = cms.bool( False ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitCaloTowerNavigator" ) ),
    ECAL_Threshold = cms.double( 10.0 ),
    ApplyTimeDPG = cms.bool( False ),
    caloTowers = cms.InputTag( "hltTowerMakerForAll" ),
    hcalRecHitsHBHE = cms.InputTag( "hltHbhereco" ),
    LongFibre_Fraction = cms.double( 0.1 ),
    MaxShortTiming_Cut = cms.double( 5.0 ),
    HcalMaxAllowedHFLongShortSev = cms.int32( 9 ),
    thresh_Barrel = cms.double( 0.4 ),
    navigation_HF = cms.bool( True ),
    HcalMaxAllowedHFInTimeWindowSev = cms.int32( 9 ),
    HF_Calib_29 = cms.double( 1.07 ),
    LongFibre_Cut = cms.double( 120.0 ),
    EM_Depth = cms.double( 22.0 ),
    weight_HFem = cms.double( 1.0 ),
    LongShortFibre_Cut = cms.double( 1.0E9 ),
    MinShortTiming_Cut = cms.double( -5.0 ),
    HCAL_Calib = cms.bool( True ),
    thresh_HF = cms.double( 0.4 ),
    HcalMaxAllowedHFDigiTimeSev = cms.int32( 9 ),
    thresh_Endcap = cms.double( 0.4 ),
    HcalMaxAllowedChannelStatusSev = cms.int32( 9 ),
    hcalRecHitsHF = cms.InputTag( "hltHfreco" ),
    ShortFibre_Cut = cms.double( 60.0 ),
    ApplyLongShortDPG = cms.bool( True ),
    HF_Calib = cms.bool( True ),
    HAD_Depth = cms.double( 47.0 ),
    ShortFibre_Fraction = cms.double( 0.01 ),
    HCAL_Calib_29 = cms.double( 1.35 )
)
process.hltParticleFlowClusterHCALForEgammaUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          recHitEnergyNorm = cms.double( 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_BARREL1" ),
          gatheringThresholdPt = cms.double( 0.0 )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HCAL_ENDCAP" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( True ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  algoName = cms.string( "RBXAndHPDCleaner" )      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 4 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 0.8 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_BARREL1" )
        ),
        cms.PSet(  seedingThreshold = cms.double( 1.1 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HCAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHCALForEgammaUnseeded" )
)
process.hltParticleFlowClusterHFEMForEgammaUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_EM" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_EM" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.19 ),
    singleSpikeThresh = cms.double( 80.0 ),
    detector = cms.string( "HF_EM" ),
    minS4S1_a = cms.double( 0.11 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_EM" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCALForEgammaUnseeded','HFEM' )
)
process.hltParticleFlowClusterHFHADForEgammaUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet( 
      positionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      ),
      minFracTot = cms.double( 1.0E-20 ),
      maxIterations = cms.uint32( 50 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      showerSigma = cms.double( 10.0 ),
      recHitEnergyNorms = cms.VPSet( 
        cms.PSet(  detector = cms.string( "HF_HAD" ),
          recHitEnergyNorm = cms.double( 0.8 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      allCellsPositionCalc = cms.PSet( 
        minFractionInCalc = cms.double( 1.0E-9 ),
        logWeightDenominator = cms.double( 0.8 ),
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" )
      )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet( 
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          detector = cms.string( "HF_HAD" ),
          gatheringThresholdPt = cms.double( 0.0 )
        )
      ),
      useCornerCells = cms.bool( False ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet( 
      cms.PSet(  cleaningByDetector = cms.VPSet( 
  cms.PSet(  doubleSpikeS6S2 = cms.double( -1.0 ),
    fractionThresholdModifier = cms.double( 1.0 ),
    doubleSpikeThresh = cms.double( 1.0E9 ),
    minS4S1_b = cms.double( -0.08 ),
    singleSpikeThresh = cms.double( 120.0 ),
    detector = cms.string( "HF_HAD" ),
    minS4S1_a = cms.double( 0.045 ),
    energyThresholdModifier = cms.double( 1.0 )
  )
),
        algoName = cms.string( "SpikeAndDoubleSpikeCleaner" )
      )
    ),
    seedFinder = cms.PSet( 
      nNeighbours = cms.int32( 0 ),
      thresholdsByDetector = cms.VPSet( 
        cms.PSet(  seedingThreshold = cms.double( 1.4 ),
          seedingThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" )
    ),
    recHitsSource = cms.InputTag( 'hltParticleFlowRecHitHCALForEgammaUnseeded','HFHAD' )
)
process.hltEgammaHoverEUnseeded = cms.EDProducer( "EgammaHLTBcHcalIsolationProducersRegional",
    caloTowerProducer = cms.InputTag( "hltTowerMakerForAll" ),
    effectiveAreaBarrel = cms.double( 0.105 ),
    outerCone = cms.double( 0.14 ),
    innerCone = cms.double( 0.0 ),
    useSingleTower = cms.bool( False ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    depth = cms.int32( -1 ),
    doRhoCorrection = cms.bool( False ),
    effectiveAreaEndcap = cms.double( 0.17 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    rhoMax = cms.double( 9.9999999E7 ),
    etMin = cms.double( 0.0 ),
    rhoScale = cms.double( 1.0 ),
    doEtSum = cms.bool( False )
)
process.hltEle15WPYYtracklessHEFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    #ORIGINAL thrOverEEE = cms.double( 0.075 ),
    thrOverEEE = cms.double( 1.2 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    #ORIGINAL thrOverEEB = cms.double( 0.1 ),
    thrOverEEB = cms.double( 1.2 ),
	thrRegularEB = cms.double( -1.0 ),
	lessThan = cms.bool( True ),
    useEt = cms.bool( False ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaHoverEUnseeded" ),
    candTag = cms.InputTag( "hltEle15WPYYtracklessEcalIsoFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEgammaHcalPFClusterIsoUnseeded = cms.EDProducer( "EgammaHLTHcalPFClusterIsolationProducer",
    energyEndcap = cms.double( 0.0 ),
    useHF = cms.bool( False ),
    effectiveAreaBarrel = cms.double( 0.06 ),
    etaStripBarrel = cms.double( 0.0 ),
    pfClusterProducerHFHAD = cms.InputTag( "hltParticleFlowClusterHFHADForEgammaUnseeded" ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    etaStripEndcap = cms.double( 0.0 ),
    drVetoBarrel = cms.double( 0.0 ),
    pfClusterProducerHCAL = cms.InputTag( "hltParticleFlowClusterHCALForEgammaUnseeded" ),
    drMax = cms.double( 0.3 ),
    doRhoCorrection = cms.bool( True ),
    energyBarrel = cms.double( 0.0 ),
    effectiveAreaEndcap = cms.double( 0.089 ),
    drVetoEndcap = cms.double( 0.0 ),
    recoEcalCandidateProducer = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    rhoMax = cms.double( 9.9999999E7 ),
    pfClusterProducerHFEM = cms.InputTag( "hltParticleFlowClusterHFEMForEgammaUnseeded" ),
    rhoScale = cms.double( 1.0 )
)
process.hltEle15WPYYtracklessHcalIsoFilter = cms.EDFilter( "HLTEgammaGenericFilter",
    doIsolated = cms.bool( True ),
    thrOverE2EE = cms.double( -1.0 ),
    L1NonIsoCand = cms.InputTag( "" ),
    saveTags = cms.bool( True ),
    thrOverE2EB = cms.double( -1.0 ),
    thrRegularEE = cms.double( -1.0 ),
    #ORIGINAL thrOverEEE = cms.double( 0.2 ),
    thrOverEEE = cms.double( 2.0 ),
	L1IsoCand = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    #ORIGINAL thrOverEEB = cms.double( 0.2 ),
    thrOverEEB = cms.double( 2.0 ),
	thrRegularEB = cms.double( -1.0 ),
    lessThan = cms.bool( True ),
    useEt = cms.bool( True ),
    ncandcut = cms.int32( 2 ),
    isoTag = cms.InputTag( "hltEgammaHcalPFClusterIsoUnseeded" ),
    candTag = cms.InputTag( "hltEle15WPYYtracklessHEFilter" ),
    nonIsoTag = cms.InputTag( "" )
)
process.hltEgammaNoTrackerCandidates = cms.EDFilter( "CandViewSelector",
    src = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
    cut = cms.string( "abs( eta ) > 2.4" ),
	saveTags = cms.bool( True )
)
process.hltEgammaNoTrackerEtaPtFilter = cms.EDFilter( "EtaPtMinCandViewSelector",
    src = cms.InputTag( "hltEgammaNoTrackerCandidates" ),
    etaMin = cms.double( -3.0 ),
    etaMax = cms.double( 3.0 ),
    ptMin = cms.double( 5.0 ),
	saveTags = cms.bool( True )
)
process.hltEgammaNoTrackerNCandidatesFilter = cms.EDFilter( "CandViewCountFilter",
    src = cms.InputTag( "hltEgammaNoTrackerEtaPtFilter" ),
    minNumber = cms.uint32( 1 ),
	saveTags = cms.bool( True )
)

process.HLTL1UnpackerSequence = cms.Sequence( process.hltGtDigis + process.hltGctDigis + process.hltL1GtObjectMap + process.hltL1extraParticles )
process.HLTBeamSpot = cms.Sequence( process.hltScalersRawToDigi + process.hltOnlineBeamSpot )
process.HLTBeginSequence = cms.Sequence( process.hltTriggerType + process.HLTL1UnpackerSequence + process.HLTBeamSpot )
process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( process.hltEcalDigis + process.hltEcalUncalibRecHit + process.hltEcalDetIdToBeRecovered + process.hltEcalRecHit )
process.HLTEndSequence = cms.Sequence( process.hltBoolEnd )

process.HLTDoFullUnpackingEgammaEcalSequence = cms.Sequence( 
		process.hltEcalDigis 
		+ process.hltEcalPreshowerDigis 
		+ process.hltEcalUncalibRecHit 
		+ process.hltEcalDetIdToBeRecovered 
		+ process.hltEcalRecHit 
		+ process.hltEcalPreshowerRecHit )

#the thresholds which must be passed in hltRechitInRegionsECAL, hltRechitInRegionsES,
#and the other producers could result in events where no RecoEcalCandidate is produced
#in particular, the Et > 4.0 GeV requirement in hltParticleFlowSuperClusterECALL1Seeded
#(see thresh_PFClusterBarrel, thresh_PFClusterEndcap, thresh_SCEt) could result in
#no RecoEcalCandidates being produced by the tracked leg
process.HLTPFClusteringForEgamma = cms.Sequence( 
		process.hltRechitInRegionsECAL 
		+ process.hltRechitInRegionsES 
		+ process.hltParticleFlowRecHitECALL1Seeded 
		+ process.hltParticleFlowRecHitPSL1Seeded 
		+ process.hltParticleFlowClusterPSL1Seeded 
		+ process.hltParticleFlowClusterECALUncorrectedL1Seeded 
		+ process.hltParticleFlowClusterECALL1Seeded 
		+ process.hltParticleFlowSuperClusterECALL1Seeded )

process.HLTDoLocalHcalWithTowerSequence = cms.Sequence( process.hltHcalDigis + process.hltHbhereco + process.hltHfreco + process.hltHoreco + process.hltTowerMakerForAll )
process.HLTPFHcalClusteringForEgamma = cms.Sequence( process.hltRegionalTowerForEgamma + process.hltParticleFlowRecHitHCALForEgamma + process.hltParticleFlowClusterHCALForEgamma )
process.HLTFastJetForEgamma = cms.Sequence( process.hltFixedGridRhoFastjetAllCaloForMuons )
process.HLTDoLocalPixelSequence = cms.Sequence( process.hltSiPixelDigis + process.hltSiPixelClusters + process.hltSiPixelClustersCache + process.hltSiPixelRecHits )
process.HLTDoLocalStripSequence = cms.Sequence( process.hltSiStripExcludedFEDListProducer + process.hltSiStripRawToClustersFacility + process.hltSiStripClusters )

#this is run just before the filters on (1/E)-(1/P), dEta, and dPhi in the tracked leg
process.HLTGsfElectronSequence = cms.Sequence( 
		process.hltEgammaCkfTrackCandidatesForGSF 
		+ process.hltEgammaGsfTracks 
		+ process.hltEgammaGsfElectrons 
		+ process.hltEgammaGsfTrackVars 
		)

process.HLTRecoPixelVertexingForElectronSequence = cms.Sequence( process.hltPixelLayerTriplets + process.hltPixelTracksElectrons + process.hltPixelVerticesElectrons )
process.HLTPixelTrackingForElectron = cms.Sequence( process.hltElectronsVertex + process.HLTDoLocalPixelSequence + process.HLTRecoPixelVertexingForElectronSequence )
process.HLTIterativeTrackingForElectronsIteration0 = cms.Sequence( process.hltIter0ElectronsPixelSeedsFromPixelTracks + process.hltIter0ElectronsCkfTrackCandidates + process.hltIter0ElectronsCtfWithMaterialTracks + process.hltIter0ElectronsTrackSelectionHighPurity )
process.HLTIterativeTrackingForElectronsIteration1 = cms.Sequence( process.hltIter1ElectronsClustersRefRemoval + process.hltIter1ElectronsMaskedMeasurementTrackerEvent + process.hltIter1ElectronsPixelLayerTriplets + process.hltIter1ElectronsPixelSeeds + process.hltIter1ElectronsCkfTrackCandidates + process.hltIter1ElectronsCtfWithMaterialTracks + process.hltIter1ElectronsTrackSelectionHighPurityLoose + process.hltIter1ElectronsTrackSelectionHighPurityTight + process.hltIter1ElectronsTrackSelectionHighPurity )
process.HLTIterativeTrackingForElectronsIteration2 = cms.Sequence( process.hltIter2ElectronsClustersRefRemoval + process.hltIter2ElectronsMaskedMeasurementTrackerEvent + process.hltIter2ElectronsPixelLayerPairs + process.hltIter2ElectronsPixelSeeds + process.hltIter2ElectronsCkfTrackCandidates + process.hltIter2ElectronsCtfWithMaterialTracks + process.hltIter2ElectronsTrackSelectionHighPurity )
process.HLTIterativeTrackingForElectronIter02 = cms.Sequence( process.HLTIterativeTrackingForElectronsIteration0 + process.HLTIterativeTrackingForElectronsIteration1 + process.hltIter1MergedForElectrons + process.HLTIterativeTrackingForElectronsIteration2 + process.hltIter2MergedForElectrons )
process.HLTTrackReconstructionForIsoElectronIter02 = cms.Sequence( process.HLTPixelTrackingForElectron + process.HLTDoLocalStripSequence + process.HLTIterativeTrackingForElectronIter02 )

#tracked leg
process.HLTEle27WPXXSequence = cms.Sequence( 
		process.HLTDoFullUnpackingEgammaEcalSequence 
		+ process.HLTPFClusteringForEgamma 
		+ process.hltEgammaCandidates 
		+ process.hltEGL1SingleEG20ORL1SingleEG22Filter 
		+ process.hltEG27WPXXEtFilter 
		+ process.hltEgammaClusterShape 
		+ process.hltEle27WPXXClusterShapeFilter 
		+ process.HLTDoLocalHcalWithTowerSequence 
		+ process.HLTPFHcalClusteringForEgamma 
		+ process.HLTFastJetForEgamma 
		+ process.hltEgammaHoverE 
		+ process.hltEle27WPXXHEFilter 
		+ process.hltEgammaEcalPFClusterIso 
		+ process.hltEle27WPXXEcalIsoFilter 
		+ process.hltEgammaHcalPFClusterIso 
		+ process.hltEle27WPXXHcalIsoFilter 
		+ process.HLTDoLocalPixelSequence 
		+ process.HLTDoLocalStripSequence 
		+ process.hltMixedLayerPairs 
		+ process.hltEgammaElectronPixelSeeds 
		+ process.hltEle27WPXXPixelMatchFilter 
		+ process.HLTGsfElectronSequence 
		+ process.hltEle27WPXXOneOEMinusOneOPFilter 
		+ process.hltEle27WPXXDetaFilter 
		+ process.hltEle27WPXXDphiFilter 
		+ process.HLTTrackReconstructionForIsoElectronIter02 
		+ process.hltEgammaEleGsfTrackIso 
		+ process.hltEle27WPXXTrackIsoFilter )

process.HLTEle27WPXXSequenceStudy = cms.Sequence( 
		process.HLTDoFullUnpackingEgammaEcalSequence 
		+ process.HLTPFClusteringForEgamma 
		+ process.hltEgammaCandidates 
		#+ process.hltEGL1SingleEG20ORL1SingleEG22Filter 
		#+ process.hltEG27WPXXEtFilter 
		+ process.hltEgammaClusterShape 
		#+ process.hltEle27WPXXClusterShapeFilter 
		+ process.HLTDoLocalHcalWithTowerSequence 
		+ process.HLTPFHcalClusteringForEgamma 
		+ process.HLTFastJetForEgamma 
		+ process.hltEgammaHoverE 
		#+ process.hltEle27WPXXHEFilter 
		+ process.hltEgammaEcalPFClusterIso 
		#+ process.hltEle27WPXXEcalIsoFilter 
		+ process.hltEgammaHcalPFClusterIso 
		#+ process.hltEle27WPXXHcalIsoFilter 
		+ process.HLTDoLocalPixelSequence 
		+ process.HLTDoLocalStripSequence 
		+ process.hltMixedLayerPairs 
		+ process.hltEgammaElectronPixelSeeds 
		#+ process.hltEle27WPXXPixelMatchFilter 
		+ process.HLTGsfElectronSequence 
		#+ process.hltEle27WPXXOneOEMinusOneOPFilter 
		#+ process.hltEle27WPXXDetaFilter 
		#+ process.hltEle27WPXXDphiFilter 
		+ process.HLTTrackReconstructionForIsoElectronIter02 
		+ process.hltEgammaEleGsfTrackIso 
		#+ process.hltEle27WPXXTrackIsoFilter
)

process.HLTEle27WPXXSequenceStudyWithL1Filter = cms.Sequence( 
		process.HLTDoFullUnpackingEgammaEcalSequence 
		+ process.HLTPFClusteringForEgamma 
		+ process.hltEgammaCandidates 
		+ process.hltEGL1SingleEG20ORL1SingleEG22Filter 
		#+ process.hltEG27WPXXEtFilter 
		+ process.hltEgammaClusterShape 
		#+ process.hltEle27WPXXClusterShapeFilter 
		+ process.HLTDoLocalHcalWithTowerSequence 
		+ process.HLTPFHcalClusteringForEgamma 
		+ process.HLTFastJetForEgamma 
		+ process.hltEgammaHoverE 
		#+ process.hltEle27WPXXHEFilter 
		+ process.hltEgammaEcalPFClusterIso 
		#+ process.hltEle27WPXXEcalIsoFilter 
		+ process.hltEgammaHcalPFClusterIso 
		#+ process.hltEle27WPXXHcalIsoFilter 
		+ process.HLTDoLocalPixelSequence 
		+ process.HLTDoLocalStripSequence 
		+ process.hltMixedLayerPairs 
		+ process.hltEgammaElectronPixelSeeds 
		#+ process.hltEle27WPXXPixelMatchFilter 
		+ process.HLTGsfElectronSequence 
		#+ process.hltEle27WPXXOneOEMinusOneOPFilter 
		#+ process.hltEle27WPXXDetaFilter 
		#+ process.hltEle27WPXXDphiFilter 
		+ process.HLTTrackReconstructionForIsoElectronIter02 
		+ process.hltEgammaEleGsfTrackIso 
		#+ process.hltEle27WPXXTrackIsoFilter
)



#similar to HLTPFClusteringForEgamma
#all of the modules in this sequence are producers, and each has
#some threshold requirements
#the Et threshold requirement of 4.0 GeV is used in
#hltParticleFlowSuperClusterECALUnseeded
process.HLTPFClusteringForEgammaUnseeded = cms.Sequence( 
		process.HLTDoFullUnpackingEgammaEcalSequence 
		+ process.hltParticleFlowRecHitECALUnseeded 
		+ process.hltParticleFlowRecHitPSUnseeded 
		+ process.hltParticleFlowClusterPSUnseeded 
		+ process.hltParticleFlowClusterECALUncorrectedUnseeded 
		+ process.hltParticleFlowClusterECALUnseeded 
		+ process.hltParticleFlowSuperClusterECALUnseeded )

process.HLTPFHcalClusteringForEgammaUnseeded = cms.Sequence( process.hltParticleFlowRecHitHCALForEgammaUnseeded + process.hltParticleFlowClusterHCALForEgammaUnseeded + process.hltParticleFlowClusterHFEMForEgammaUnseeded + process.hltParticleFlowClusterHFHADForEgammaUnseeded )

process.HLTEle15WPYYtracklessSequenceStudy = cms.Sequence( 
		process.HLTPFClusteringForEgammaUnseeded 
		+ process.hltEgammaCandidatesUnseeded 
		+ process.hltEgammaCandidatesWrapperUnseeded	#this is an EDFilter, but is not relevant to subsequent producers in the path 
		#+ process.hltEG15WPYYtracklessEtFilterUnseeded 
		+ process.hltEgammaClusterShapeUnseeded 
		#+ process.hltEle15WPYYtracklessClusterShapeFilter 
		+ process.hltEgammaEcalPFClusterIsoUnseeded 
		#+ process.hltEle15WPYYtracklessEcalIsoFilter 
		+ process.HLTPFHcalClusteringForEgammaUnseeded 
		+ process.hltEgammaHoverEUnseeded 
		#+ process.hltEle15WPYYtracklessHEFilter 
		+ process.hltEgammaHcalPFClusterIsoUnseeded 
		#+ process.hltEle15WPYYtracklessHcalIsoFilter 
		+ process.hltEgammaNoTrackerCandidates 
		#+ process.hltEgammaNoTrackerEtaPtFilter 
		#+ process.hltEgammaNoTrackerNCandidatesFilter
)


#trackless leg
process.HLTEle15WPYYtracklessSequence = cms.Sequence( 
		process.HLTPFClusteringForEgammaUnseeded 
		+ process.hltEgammaCandidatesUnseeded 
		+ process.hltEgammaCandidatesWrapperUnseeded 
		+ process.hltEG15WPYYtracklessEtFilterUnseeded 
		+ process.hltEgammaClusterShapeUnseeded 
		+ process.hltEle15WPYYtracklessClusterShapeFilter 
		+ process.hltEgammaEcalPFClusterIsoUnseeded 
		+ process.hltEle15WPYYtracklessEcalIsoFilter 
		+ process.HLTPFHcalClusteringForEgammaUnseeded 
		+ process.hltEgammaHoverEUnseeded 
		+ process.hltEle15WPYYtracklessHEFilter 
		+ process.hltEgammaHcalPFClusterIsoUnseeded 
		+ process.hltEle15WPYYtracklessHcalIsoFilter 
		+ process.hltEgammaNoTrackerCandidates 
		+ process.hltEgammaNoTrackerEtaPtFilter 
		+ process.hltEgammaNoTrackerNCandidatesFilter )



process.HLTriggerFirstPath = cms.Path( 
		process.hltGetConditions 
		+ process.hltGetRaw 
		+ process.hltBoolFalse )


#process.AlCa_EcalPhiSym_v1 = cms.Path( process.HLTBeginSequence + process.hltL1sL1ZeroBias + process.hltPreAlCaEcalPhiSym + process.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + process.hltAlCaPhiSymStream + process.hltAlCaPhiSymUncalibrator + process.HLTEndSequence )


#######################################################################################################
#reco selectors, filters and producers
process.noTrackerCandidates = cms.EDFilter( "CandViewSelector",
    src = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
	cut = cms.string(' (eta > -2.5 && eta < -3.0 ) || ( eta > 2.5 && eta < 3.0 ) ')
)

process.trackerCandidates = cms.EDFilter( "CandViewSelector",
    src = cms.InputTag( "hltEgammaCandidates" ),
	cut = cms.string('eta < 2.5 && eta > -2.5')
)

process.combRecoEleNoCuts = cms.EDProducer("CandViewShallowCloneCombiner",
		decay = cms.string("hltEgammaCandidatesUnseeded hltEgammaCandidates"),
		#checkCharge = cms.bool(False),
		cut = cms.string(""),
		#this name is tied to the CompositeCandidate object
		#name = cms.string('zedToElEl'),
		#roles are relevant to the daughters
		roles = cms.vstring('tracklessRecoEle', 'trackedRecoEle')
		
		)

process.combRecoEle = cms.EDProducer("CandViewShallowCloneCombiner",
		decay = cms.string("noTrackerCandidates trackerCandidates"),
		#checkCharge = cms.bool(False),
		cut = cms.string("mass > 50 && mass < 130"),
		#this name is tied to the CompositeCandidate object
		#name = cms.string('zedToElEl'),
		#roles are relevant to the daughters
		roles = cms.vstring('tracklessRecoEle', 'trackedRecoEle')
		
		)

process.recoZeeFilter = cms.EDFilter("CandViewCountFilter",
		src = cms.InputTag("combRecoEle"),
		minNumber = cms.uint32(1)
		)

process.recoZeeFilterNoCuts = cms.EDFilter("CandViewCountFilter",
		src = cms.InputTag("combRecoEleNoCuts"),
		minNumber = cms.uint32(1)
		)

process.recoDaughterProducer = cms.EDProducer("SeparateCombCandidate",
		zedLabel = cms.InputTag("combRecoEle"),
		tracklessHltEle = cms.InputTag("hltEgammaCandidatesUnseeded"),
		trackedHltEle = cms.InputTag("hltEgammaCandidates"),
		tracklessEleCollectionName = cms.string("tracklessDaughters"),
		trackedEleCollectionName = cms.string("trackedDaughters")

		)

process.recoDaughterProducerNoCuts = cms.EDProducer("SeparateCombCandidate",
		zedLabel = cms.InputTag("combRecoEleNoCuts"),
		tracklessHltEle = cms.InputTag("hltEgammaCandidatesUnseeded"),
		trackedHltEle = cms.InputTag("hltEgammaCandidates"),
		tracklessEleCollectionName = cms.string("tracklessDaughters"),
		trackedEleCollectionName = cms.string("trackedDaughters")

		)

process.noTrackerCandidatesStageTwo = cms.EDFilter( "CandViewSelector",
    src = cms.InputTag( "hltEgammaCandidatesUnseeded" ),
	cut = cms.string('pt>15 && ( (eta > -2.5 && eta < -3.0 ) || ( eta > 2.5 && eta < 3.0 ) )')
)

process.trackerCandidatesStageTwo = cms.EDFilter( "CandViewSelector",
    src = cms.InputTag( "hltEgammaCandidates" ),
	cut = cms.string('pt>27 && eta < 2.5 && eta > -2.5')
)


process.combRecoEleStageTwo = cms.EDProducer("CandViewShallowCloneCombiner",
		decay = cms.string("noTrackerCandidatesStageTwo trackerCandidatesStageTwo"),
		#checkCharge = cms.bool(False),
		cut = cms.string("mass > 50 && mass < 130"),
		#this name is tied to the CompositeCandidate object
		#name = cms.string('zedToElEl'),
		#roles are relevant to the daughters
		roles = cms.vstring('tracklessRecoEle', 'trackedRecoEle')
		
		)

process.recoZeeFilterStageTwo = cms.EDFilter("CandViewCountFilter",
		src = cms.InputTag("combRecoEleStageTwo"),
		minNumber = cms.uint32(1)
		)

process.recoDaughterProducerStageTwo = cms.EDProducer("SeparateCombCandidate",
		zedLabel = cms.InputTag("combRecoEleStageTwo"),
		tracklessHltEle = cms.InputTag("hltEgammaCandidatesUnseeded"),
		trackedHltEle = cms.InputTag("hltEgammaCandidates"),
		tracklessEleCollectionName = cms.string("tracklessDaughters"),
		trackedEleCollectionName = cms.string("trackedDaughters")

		)


#######################################################################################################
#reco analyzers to run in HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study path
#run these after recoDaughterProducer
process.recoAnalyzerTracked = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedBkgnd"),
		recoElectronCollection = cms.InputTag("recoDaughterProducer","trackedDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEle","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

process.recoAnalyzerTrackedNoCuts = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedBkgndNoCuts"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerNoCuts","trackedDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleNoCuts","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

process.recoAnalyzerTrackedNoCutsWithL1Filter = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedBkgndNoCutsWithL1Filter"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerNoCuts","trackedDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleNoCuts","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)



process.recoAnalyzerTrackedWithL1Filter = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter"),
		recoElectronCollection = cms.InputTag("recoDaughterProducer","trackedDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEle","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
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
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessBkgnd"),
		recoElectronCollection = cms.InputTag("recoDaughterProducer","tracklessDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEle","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

process.recoAnalyzerTracklessNoCuts = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessBkgndNoCuts"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerNoCuts","tracklessDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleNoCuts","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

process.recoAnalyzerTracklessNoCutsWithL1Filter = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessBkgndNoCutsWithL1Filter"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerNoCuts","tracklessDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleNoCuts","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)



process.recoAnalyzerTracklessWithL1Filter = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessBkgndWithL1Filter"),
		recoElectronCollection = cms.InputTag("recoDaughterProducer","tracklessDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEle","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)


#stage two analyzers (pt requirements added to tracked and trackless objects)
#run these after recoDaughterProducerStageTwo
process.recoAnalyzerTrackedStageTwo = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedBkgndStageTwo"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerStageTwo","trackedDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleStageTwo","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

process.recoAnalyzerTrackedStageTwoWithL1Filter = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShape","sigmaIEtaIEta5x5","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverE","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIso","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIso","","TEST"),
		Ep=cms.InputTag("hltEgammaGsfTrackVars","OneOESuperMinusOneOP","TEST"),
		Deta=cms.InputTag("hltEgammaGsfTrackVars","Deta","TEST"),
		Dphi=cms.InputTag("hltEgammaGsfTrackVars","Dphi","TEST"),
		TrackIso=cms.InputTag("hltEgammaEleGsfTrackIso","","TEST"),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTrackedBkgndStageTwoWithL1Filter"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerStageTwo","trackedDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(True),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleStageTwo","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)


process.recoAnalyzerTracklessStageTwo = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessBkgndStageTwo"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerStageTwo","tracklessDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleStageTwo","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

process.recoAnalyzerTracklessStageTwoWithL1Filter = cms.EDAnalyzer('recoAnalyzerGeneric',
		SigmaIEIE = cms.InputTag("hltEgammaClusterShapeUnseeded","","TEST"),
		HadEm=cms.InputTag("hltEgammaHoverEUnseeded","","TEST"),
		EcalIso=cms.InputTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST"),
		HcalIso=cms.InputTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST"),
		Ep=cms.InputTag("","",""),
		Deta=cms.InputTag("","",""),
		Dphi=cms.InputTag("","",""),
		TrackIso=cms.InputTag("","",""),
		treeName = cms.string("recoTreeBeforeTriggerFiltersTracklessBkgndStageTwoWithL1Filter"),
		recoElectronCollection = cms.InputTag("recoDaughterProducerStageTwo","tracklessDaughters","TEST"),
		doAnalysisOfTracked = cms.bool(False),
		genCollection = cms.InputTag("","",""),
		dRMatch = cms.double(-1),
		recoZedCollection = cms.InputTag("combRecoEleStageTwo","","TEST"),
		genZedCollection = cms.InputTag("","","")
	
		)

#Paths

process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study = cms.Path( 
		process.HLTBeginSequence 
		#+ process.hltL1sL1SingleEG20ORL1SingleEG22 
		+ process.hltPreEle27WPXXEle15WPYYtrackless 
		+ process.HLTEle27WPXXSequenceStudy 
		+ process.HLTEle15WPYYtracklessSequenceStudy
		+ process.HLTEndSequence
		+ process.noTrackerCandidates
		+ process.trackerCandidates
		+ process.combRecoEle
		*process.recoZeeFilter
		*process.recoDaughterProducer
		*process.recoAnalyzerTracked
		*process.recoAnalyzerTrackless
		)

#the tuples made by this path will be used to 
#count the total number of bkgnd evts before any reco eta, pt, and dilepton mass cuts are applied
process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study_NoCuts = cms.Path( 
		process.HLTBeginSequence 
		#+ process.hltL1sL1SingleEG20ORL1SingleEG22 
		+ process.hltPreEle27WPXXEle15WPYYtrackless 
		+ process.HLTEle27WPXXSequenceStudy 
		+ process.HLTEle15WPYYtracklessSequenceStudy
		+ process.HLTEndSequence
		#+ process.noTrackerCandidates
		#+ process.trackerCandidates
		+ process.combRecoEleNoCuts
		#*process.recoZeeFilterNoCuts
		*process.recoDaughterProducerNoCuts
		*process.recoAnalyzerTrackedNoCuts
		*process.recoAnalyzerTracklessNoCuts
		)

process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study_NoCuts_WithL1Filter = cms.Path( 
		process.HLTBeginSequence 
		+ process.hltL1sL1SingleEG20ORL1SingleEG22 
		+ process.hltPreEle27WPXXEle15WPYYtrackless 
		+ process.HLTEle27WPXXSequenceStudyWithL1Filter 
		+ process.HLTEle15WPYYtracklessSequenceStudy
		+ process.HLTEndSequence
		#+ process.noTrackerCandidates
		#+ process.trackerCandidates
		+ process.combRecoEleNoCuts
		#*process.recoZeeFilterNoCuts
		*process.recoDaughterProducerNoCuts
		*process.recoAnalyzerTrackedNoCutsWithL1Filter
		*process.recoAnalyzerTracklessNoCutsWithL1Filter
		)


process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study_StageTwo = cms.Path( 
		process.HLTBeginSequence 
		#+ process.hltL1sL1SingleEG20ORL1SingleEG22 
		+ process.hltPreEle27WPXXEle15WPYYtrackless 
		+ process.HLTEle27WPXXSequenceStudy 
		+ process.HLTEle15WPYYtracklessSequenceStudy
		+ process.HLTEndSequence
		+ process.noTrackerCandidatesStageTwo
		+ process.trackerCandidatesStageTwo
		+ process.combRecoEleStageTwo
		*process.recoZeeFilterStageTwo
		*process.recoDaughterProducerStageTwo
		*process.recoAnalyzerTrackedStageTwo
		*process.recoAnalyzerTracklessStageTwo
		)

process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study_WithL1Filter = cms.Path( 
		process.HLTBeginSequence 
		+ process.hltL1sL1SingleEG20ORL1SingleEG22 
		+ process.hltPreEle27WPXXEle15WPYYtrackless 
		+ process.HLTEle27WPXXSequenceStudyWithL1Filter 
		+ process.HLTEle15WPYYtracklessSequenceStudy
		+ process.HLTEndSequence
		+ process.noTrackerCandidates
		+ process.trackerCandidates
		+ process.combRecoEle
		*process.recoZeeFilter
		*process.recoDaughterProducer
		*process.recoAnalyzerTrackedWithL1Filter
		*process.recoAnalyzerTracklessWithL1Filter
		)

process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study_StageTwo_WithL1Filter = cms.Path( 
		process.HLTBeginSequence 
		+ process.hltL1sL1SingleEG20ORL1SingleEG22 
		+ process.hltPreEle27WPXXEle15WPYYtrackless 
		+ process.HLTEle27WPXXSequenceStudyWithL1Filter 
		+ process.HLTEle15WPYYtracklessSequenceStudy
		+ process.HLTEndSequence
		+ process.noTrackerCandidatesStageTwo
		+ process.trackerCandidatesStageTwo
		+ process.combRecoEleStageTwo
		*process.recoZeeFilterStageTwo
		*process.recoDaughterProducerStageTwo
		*process.recoAnalyzerTrackedStageTwoWithL1Filter
		*process.recoAnalyzerTracklessStageTwoWithL1Filter
		)



#process.quickGenStudyTwoTracked = cms.Path(
#		process.genEle
#		*process.twoGenFilter
#		*process.genAnalyzerOne
#		*process.genTracked
#		*process.twoGenTrackedFilter
#		)
#
#process.quickGenStudyOneTrackedOneTrackless = cms.Path(
#		process.genEle
#		*process.twoGenFilter
#		*process.genTracked
#		*process.genTrackedFilter
#		*process.genTrackless
#		*process.genTracklessFilter
#		)
#

#process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_v1 = cms.Path( 
#		process.HLTBeginSequence 
#		+ process.hltL1sL1SingleEG20ORL1SingleEG22 
#		+ process.hltPreEle27WPXXEle15WPYYtrackless 
#		+ process.HLTEle27WPXXSequence 
#		+ process.HLTEle15WPYYtracklessSequence
#		+ process.HLTEndSequence )

process.HLTriggerFinalPath = cms.Path( 
		process.hltGtDigis 
		+ process.hltScalersRawToDigi + process.hltFEDSelector + process.hltTriggerSummaryAOD + process.hltTriggerSummaryRAW
		)


#process.schedule = cms.Schedule(process.HLTriggerFirstPath, process.HLT_Ele27_WPXX_Ele15_WPYY_trackless_Study, process.HLTriggerFinalPath)


process.TFileService = cms.Service("TFileService",
		fileName = cms.string('ABCDE_pt_bkgnd_analyzer_trees_NUM_CMSSW_7_4_0_pre9_25ns.root')
)

process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
	   #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/004E6498-8D6F-E311-966A-00261894384A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/009E42C3-026F-E311-9419-003048678BAC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/00D27B22-726F-E311-A7F8-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0206F26C-126F-E311-995B-003048678B8E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0207C698-076F-E311-B5F0-002618943914.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/02309CFA-006F-E311-A7C8-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/026C1C89-1A6F-E311-ACD1-00261894397A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/04218C9C-1C6F-E311-B0D6-0030486792B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/048B5B04-FE6E-E311-A94F-002618943922.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0623D7F2-766F-E311-90D4-00261894391B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/063CB935-206F-E311-8390-00304867918E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/08181581-776F-E311-9672-003048678B12.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0821E5CF-866F-E311-B13A-00261894396B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/084DC238-AB6F-E311-873F-0026189437F9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/086FE2B0-1E6F-E311-B1D2-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/089C0A9B-4D6F-E311-B97A-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0AE25877-036F-E311-A170-0030486792AC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0AED9738-256F-E311-90C1-003048FFCB84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0C26CB8A-7D6F-E311-B082-0025905A6092.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0E3B4036-326F-E311-B2F2-00261894388D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0EA0CDB1-556F-E311-8947-0025905A60E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0EC693E6-A670-E311-B0AF-002618943918.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/103ED675-166F-E311-B493-003048678BEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/108D5429-686F-E311-906A-003048D3C010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/10D591D1-626F-E311-8740-002618943947.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/10E3B22A-216F-E311-B5C4-00248C65A3EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/12403B2F-7B6F-E311-8F13-002618943961.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/126A2479-0F6F-E311-8256-002354EF3BDF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/12F9293A-196F-E311-B2CA-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/140F329B-606F-E311-B3AF-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1433C9DF-6F6F-E311-A565-0025905A60DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/143FEB04-0E6F-E311-BCAF-002618943978.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/149800F3-0B6F-E311-8A51-00304867D446.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/162BDF77-FF6E-E311-89C6-0026189438DB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/167D55DE-5C6F-E311-B2F9-00261894386E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/16B6A020-736F-E311-92D9-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1868A4AE-376F-E311-9817-0026189438F7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/186E2AC6-1B6F-E311-BDDC-0026189438D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1A61801E-0A6F-E311-9769-002618943856.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1A642F88-0C6F-E311-A7C8-00261894397B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1ABAE843-A06F-E311-87FD-003048FFD7D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1CFB9206-966F-E311-824F-003048FFD7D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1E1C181C-5B6F-E311-8308-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1E697402-216F-E311-8F7D-003048678E92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1E86A62C-7A6F-E311-8CA8-00304867920A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1ECC54C4-026F-E311-AE63-00261894398C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/20199C4E-916F-E311-99EA-0025905A60E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/205CFB01-3C6F-E311-821E-00261894398B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/20C29FB1-FF6E-E311-AA95-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2217C9AD-0A6F-E311-88BB-003048679244.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/226B3D2E-216F-E311-9F75-00261894390E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/229A4C8B-1C6F-E311-BD3F-002618FDA277.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/24662B07-806F-E311-ADE1-0025905A6138.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/24D328C8-7C6F-E311-B1BA-002618943933.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/24DAF0C5-0A6F-E311-8AB1-003048FFD728.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/26A77D11-546F-E311-AE94-00261894387C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/26F406C0-106F-E311-BE83-003048678F9C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/26F7FF5A-656F-E311-833C-003048678AFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2860EFF0-106F-E311-B343-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/287B8EFD-586F-E311-BC02-003048679180.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2A7AE6F6-656F-E311-9F0E-003048678AFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2C00EBB0-1F6F-E311-8C47-002618943916.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2E3D3ECF-006F-E311-AB32-002618943956.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2E94E105-346F-E311-B2EB-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2E9BEE30-956F-E311-A60D-0025905A48EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/301157F7-7F6F-E311-864B-002618943925.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3012EF5E-936F-E311-8E59-0026189438FF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/30DF01F6-036F-E311-A471-0025905A6138.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3236CDE4-046F-E311-8852-002618943826.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/388E7953-FA6E-E311-83B8-002618943976.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/38F784FD-036F-E311-853B-0026189438FF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3ABF62C7-5470-E311-B057-002618FDA262.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3AFE9DA8-4970-E311-8720-003048679228.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3C0E7406-A56F-E311-AA21-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3CC1B6E1-516F-E311-BFBF-002618943829.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3E47ADFF-006F-E311-9B37-002618943867.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3E9F0AB5-096F-E311-B239-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/407E9F2D-256F-E311-8955-0030486792F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/40E39ECA-AF6F-E311-AE70-002618FDA26D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/426A7715-186F-E311-BA8E-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/427BF4F2-106F-E311-9902-0025905938A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/42A5F792-4D6F-E311-9B28-00304867BFF2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/42A86602-9E6F-E311-AA43-0025905964BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/440059B6-166F-E311-8FFA-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4423D712-4B6F-E311-A900-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/44479D61-FE6E-E311-A466-00261894385A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/448290BC-6F6F-E311-A848-003048679296.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/44A92EA1-076F-E311-8850-0026189438C9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/460E53E4-066F-E311-B97F-0025905964C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/46A3C997-016F-E311-B4F9-001A92971BB4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/487A57B3-1F6F-E311-AE7A-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/48DE4C2B-F96E-E311-9A7F-002618FDA259.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/48EE06A6-136F-E311-8570-002618943915.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4C8E73CB-646F-E311-AA89-0026189438C1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4CAE3318-156F-E311-A0BA-003048678AFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4CB60347-1D6F-E311-9A15-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4CBC828E-736F-E311-81DF-003048678F84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4CE2BEFE-786F-E311-804A-0026189438DF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4CEC5482-9B6F-E311-9329-002618943829.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4E3DD292-156F-E311-A0FD-002618943958.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4E4ED71F-866F-E311-8DE9-003048678F8C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4E684716-106F-E311-82E2-0026189437F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4E792203-FB6E-E311-9CB7-00261894380A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4ECA342C-0A6F-E311-9063-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/500452C8-826F-E311-BC11-002618FDA216.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/50CB7F71-036F-E311-961C-00261894387C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/50D60CF0-196F-E311-8E73-002618943842.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/50F05A6C-5270-E311-AE61-0026189438ED.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/52191971-976F-E311-B77E-00261894384A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/52F1CB94-076F-E311-8B2A-0030486791DC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/588D5CD5-1B6F-E311-A3CF-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/58CA56A3-986F-E311-B7FB-002618943985.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5A483A46-066F-E311-9E73-003048FFD71E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5A516986-1A6F-E311-9586-0026189438DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5A64D8FB-226F-E311-A119-0025905964CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5A7C303D-0D6F-E311-BE84-0025905822B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5ABD8C24-1F6F-E311-94DF-002618943975.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5AC4A5D9-8F6F-E311-8AF4-002618943971.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5C25BCB8-1E6F-E311-8E13-003048679228.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5C9D6B5B-6D6F-E311-9885-0025905A6068.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5CB6327C-126F-E311-A3E2-002618943915.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5CF053D1-A76F-E311-9C00-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E1A3E64-686F-E311-9576-0025905A6068.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E4F5441-1D6F-E311-A98C-0026189438E6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E560CB8-0F6F-E311-99C1-0025905A613C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E6BC905-136F-E311-B7FC-0026189438EF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5EB8D9F3-8A6F-E311-80D8-0030486792B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5ECB29B8-4F6F-E311-B60F-0025905964A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/60235F56-1D6F-E311-8791-003048678FB8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6253846F-166F-E311-BCF7-0026189438B5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6276897A-0B6F-E311-94FF-0025905A48EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/627703EB-8D6F-E311-8C8C-002618943975.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/62788DFE-0D6F-E311-A42D-0026189438B9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/62C2214B-246F-E311-AFE6-003048678B5E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/64207F49-5E6F-E311-BA9D-0025905A60A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/645D3347-4C6F-E311-AD65-0025905A60A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/648D341F-1B6F-E311-8DDB-00261894397A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6493AE17-1B6F-E311-A943-002618943966.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/64D1A876-FC6E-E311-B4B7-0025905A609A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/64E954CF-486F-E311-BD69-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/667DC0D2-9D6F-E311-A28C-0025905AA9CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/683D15FE-066F-E311-B8D2-00261894396B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/68864DE3-0E6F-E311-A7B5-003048678B06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6891494B-456F-E311-8A26-002618943966.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/68A67D48-9A6F-E311-936E-003048B95B30.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/68B381BA-F96E-E311-B96C-003048678E8A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6A42E589-0C70-E311-BDD4-0025905964C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6C46E36C-6C6F-E311-8F8A-002618943876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6C9B1DD6-196F-E311-9D1E-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6CA7A626-486F-E311-8775-00261894394A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6E6A1F98-396F-E311-9742-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6E747C6F-736F-E311-890A-003048678F26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6E77DF87-096F-E311-BB7F-0030486792B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6ECA5A8C-316F-E311-8C5F-0025905A60CE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6EEA871C-096F-E311-A5CE-003048FFCC2C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/705B9588-AD6F-E311-AE73-003048678B0C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/70729202-846F-E311-BE9F-002618943927.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/707523E3-146F-E311-9851-002618943854.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/723FCCE1-146F-E311-9789-003048FFD754.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7299D7B7-5B6F-E311-80BC-003048678F74.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/72A90CDD-146F-E311-88D2-002618FDA211.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/72BBDCD3-186F-E311-936E-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/72F36640-086F-E311-B57F-0030486791DC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/72F37BF8-3F6F-E311-90D3-002618943842.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/748E0932-7C6F-E311-AF40-003048FFCB6A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/74D0A2FF-006F-E311-9AEB-002354EF3BDD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7616F981-676F-E311-B153-003048FFD720.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7634313C-436F-E311-B515-00261894387A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7670A6CE-366F-E311-83A9-002590596484.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/768AE3D7-8A6F-E311-89CB-0025905964A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/78044E82-BC70-E311-B5DA-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7858C22D-686F-E311-9884-00248C0BE012.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/787B7487-2A6F-E311-99D8-003048678BF4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7A0D142D-6F6F-E311-8EFB-002618943949.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7C0FAB21-3F6F-E311-BD9C-002354EF3BDD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7E64BA52-706F-E311-90F7-002618FDA26D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/80E977D1-846F-E311-89F2-002618FDA216.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/82186D34-566F-E311-B712-0025905A6138.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8219B621-796F-E311-89A7-0025905A613C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/840FCDC3-6D6F-E311-AF9E-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8473703F-1D6F-E311-AF7D-0026189438F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/848BDFB2-906F-E311-8A29-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/84AB3AB9-4971-E311-90B4-0025905A6070.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/84EC08B6-1972-E311-AFDE-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/865681EE-186F-E311-AE74-002618FDA250.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8673A2A2-496F-E311-8421-0026189438CF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/867F7025-2E6F-E311-8EE9-002618943858.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/86F957CC-6570-E311-8F82-002618943970.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/880646B6-0C6F-E311-AF3A-0025905A6110.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/88D9DF65-B36F-E311-99D6-0025905A6134.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8A2D375F-766F-E311-A027-0025905A612E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8A386F47-466F-E311-8FBB-002590596484.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8A704930-696F-E311-9820-0026189438C9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8AFF0CB0-056F-E311-AAAF-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8CA8AAE0-816F-E311-9252-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8E1B60DD-146F-E311-A653-002618943904.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8E2D8B25-126F-E311-8C44-00248C0BE018.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8EDBF53C-646F-E311-9A1F-0030486790A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/90D00A79-446F-E311-B7C6-003048FFCB6A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/90E2228A-8B6F-E311-9729-002618943949.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9214DE5D-236F-E311-AB9F-00248C65A3EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/942E6474-5A70-E311-8A44-0026189438F7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/949260CD-016F-E311-A6B9-003048FFD7D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/94E2C248-296F-E311-9E34-00261894386F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/986B714F-7D6F-E311-A6A3-002618943894.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/98B9B982-046F-E311-B256-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/98E19230-696F-E311-A008-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/98EC0EC9-086F-E311-A70D-002618943856.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9A1E7421-216F-E311-B4D8-002618943966.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9AEFDEC7-616F-E311-8885-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9C076BC8-7E6F-E311-93AB-00261894393B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9C0A1212-9A6F-E311-BD7F-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9E052DA2-0B6F-E311-8DBB-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9E8E59E3-0A6F-E311-AA34-003048FFD754.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9EC8E673-9E6F-E311-8335-003048678FB4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9EDBE3F3-0E6F-E311-9C5E-003048678F8C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A026991D-1F6F-E311-8792-0025905A6056.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A028352E-026F-E311-A346-00248C55CC62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A053BC9E-6B6F-E311-BD46-003048678FB8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A0940E89-846F-E311-BF87-002618FDA204.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A23F4CED-626F-E311-860B-002618943957.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A24C2316-8D6F-E311-BE3C-0025905A6134.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A2507719-1E6F-E311-BAC3-00261894398A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A252775C-0B6F-E311-A340-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A26BCC91-5D6F-E311-9756-0026189438C9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A2C718ED-0E6F-E311-9486-00304867924E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A2E2205F-886F-E311-9453-002618943868.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A451B103-156F-E311-ABD4-002618943963.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A6177557-FE6E-E311-ADA2-003048678BAA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A65F1C35-816F-E311-9D2D-0025905A610A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A698D87A-286F-E311-BC19-00261894391C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A8246841-766F-E311-8D5E-00261894397F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A886D0D2-386F-E311-891E-0026189438AD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A8A5FC49-176F-E311-8A7F-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A8C1A3DA-1D6F-E311-B347-002618943959.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A8D3A8E9-9670-E311-892A-0025905A60BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AA73F4A2-236F-E311-9DE7-0030486792F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AA7F13DB-796F-E311-A7F5-0025905964BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AC351844-046F-E311-8F71-0026189438D7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AC37CA3C-206F-E311-AD02-002618FDA262.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE0A2070-2B6F-E311-8EFD-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE1C3BE6-146F-E311-98CE-003048678E52.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE26E6B7-066F-E311-B60D-002618943963.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE5491E5-276F-E311-AD19-002618943832.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE7DCB5D-3D6F-E311-876F-00261894397B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE8FFCC0-4B6F-E311-A90E-00261894391C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE9C981D-FB6E-E311-9860-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AEC967CC-186F-E311-881D-002618943957.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AEDB0993-0C6F-E311-9496-001BFCDBD1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AEFD50EC-586F-E311-949B-0025905A60CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B06AA9F3-1B6F-E311-88C1-00304867924A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B0E00A94-1C6F-E311-9816-00261894390C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B0E0C3AE-7A6F-E311-8C7D-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B0FBA1EC-666F-E311-90B2-0025905A610A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B26EBCDD-0E6F-E311-9A0D-002618943977.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B2F47147-4570-E311-B6A5-002618943977.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B427CA1D-A16F-E311-98F0-0025905A6132.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B46FCBF6-106F-E311-814F-001A92971B72.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B4A64E79-5070-E311-9397-0030486792A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B4B44693-5D70-E311-8A5F-003048678F9C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B4DBB277-876F-E311-8B6A-002618943896.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B64770C1-5D6F-E311-9A26-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B6C0432B-026F-E311-95CC-003048679010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B6D876A6-2C6F-E311-8E77-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B8C7411A-5B70-E311-8E26-0025905A48D8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BA18DDEE-576F-E311-BB0A-002590593878.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BAAE372C-026F-E311-971D-0026189438FF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BC01202F-E870-E311-8E77-002618943870.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BC0B5BEF-D46F-E311-9731-0026189437F5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BC2064B2-B76F-E311-ABF5-003048FFD76E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BC6EA05C-246F-E311-B1C1-00261894393F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C02412BC-896F-E311-B8EF-0030486792B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C257611A-986F-E311-95EB-002618FDA277.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C2748F7B-0F6F-E311-9C4D-002354EF3BE3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C2EBE09D-C96F-E311-897A-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C40D5893-4C70-E311-9183-003048678F8C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C60023C4-526F-E311-9212-00304866C398.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C60F9A55-226F-E311-B1D9-003048678BEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C63206D4-7D6F-E311-9391-002618943953.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C6343745-2F6F-E311-B5BB-003048678EE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C6D890BB-746F-E311-841F-002618943854.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C6DF6514-AC71-E311-9D57-0026189438F6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CAEFCEC9-086F-E311-B326-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CC3678FF-5270-E311-AA46-00261894387B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CC506FB0-0A6F-E311-8278-0025905A60C6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CC785B22-576F-E311-A78F-0025905A48EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CEBB7F19-6A6F-E311-AA95-003048FFD720.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CECFC4AF-116F-E311-9AC9-002618B27F8A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CEE26F45-A46F-E311-A1BB-00261894389E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D22AC623-746F-E311-A2C5-002618943921.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D25B9C37-E56F-E311-B4EC-0026189438DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D434960D-FF6E-E311-9B00-0025905AA9F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D457B79C-266F-E311-A9FF-0025905964C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D496F11A-6B6F-E311-BA46-00304867D838.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D4BD6CB5-6F6F-E311-8139-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D6266F74-FD6E-E311-8B6C-003048678BAA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D6C5B842-646F-E311-8F46-003048FFD720.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D83E6469-0D6F-E311-BA55-003048FFCB84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D8B806BA-136F-E311-8DE3-003048678B18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D8EA54BE-166F-E311-B200-0025905A48B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DA157BB9-596F-E311-A66E-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DA8F3B4F-936F-E311-BEE5-0025905A60A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DC2B088E-946F-E311-9B9E-0026189438DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DC6C8A3D-0E6F-E311-8AC5-0025905A609A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DC6F9796-136F-E311-8013-0026189438EF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DC9AC216-066F-E311-8F58-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DC9C6DE8-0E6F-E311-9E43-002354EF3BE3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DCDB94A7-116F-E311-A8FE-002618943946.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DEC99606-FD6E-E311-A3C9-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E0200DF5-1B6F-E311-BA50-003048678A7E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E05A6127-FC6E-E311-AB7A-002354EF3BDD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E0DA7AFD-5E6F-E311-908C-003048678B06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E24EF077-6170-E311-8A27-003048679296.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E2691A9C-176F-E311-8700-002618943974.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E29BA21C-506F-E311-AD40-002618943843.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E2CEE6A3-8770-E311-89E5-0026189438DD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E4961568-0D6F-E311-BEE9-00304867BFF2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E4E8657E-096F-E311-AA3B-0026189438E6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E6714D19-066F-E311-A6FD-002618943922.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E69AA930-646F-E311-9223-00261894383E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E6F09B5F-DD6F-E311-A472-0025905938A4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E814151C-1E6F-E311-A093-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E8A40FD5-4D6F-E311-850E-0025905A6090.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E8C22F85-416F-E311-B86F-002618943914.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EA126921-9C6F-E311-AC82-0026189438B3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EA6E6488-1A6F-E311-8A64-002618943833.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EAEB0941-766F-E311-A90D-003048678B00.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EC40219D-156F-E311-9038-002354EF3BD2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/ECEE6D64-FE6E-E311-9D78-001BFCDBD1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F0167FFC-466F-E311-A7FD-00261894393E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F0F2F896-016F-E311-BAE1-002618943862.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F2044B5F-C36F-E311-B958-002590593876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F210AF11-1F6F-E311-A634-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F295316A-556F-E311-83BD-0025905A60C6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F451EA65-656F-E311-A350-0026189438C1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F4AA3EFE-886F-E311-B2E8-0025905A60D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F64EF9E5-226F-E311-B6D2-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F6B241E4-0E6F-E311-AD13-002618943959.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F82CC496-1C6F-E311-B820-003048D15E14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8863E90-0D6F-E311-AA6D-003048FFD754.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FA1C42D1-806F-E311-8121-0030486792B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FC2C3CCB-0C6F-E311-A552-002618943867.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FC39217E-A86F-E311-B504-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FC55BE08-2870-E311-AC25-00261894390B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FC60DFEE-5670-E311-B09D-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FE481AC5-206F-E311-99CC-002618943970.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FE86DD03-0E6F-E311-8B11-002618943945.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FEBB104C-086F-E311-95BA-001BFCDBD130.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FEC330E6-276F-E311-8413-0026189438C9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FED455CC-FC6E-E311-AE9B-0030486790B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0421B5C4-1B6F-E311-963A-003048678FDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/045BE5EF-446F-E311-BC3B-00261894393A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0873DA92-316F-E311-B827-00261894388A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/08F011B5-E26E-E311-B3A7-00248C55CC3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0A8B51DC-D46E-E311-8A5A-002618FDA216.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0AAF30CD-EA6E-E311-BF71-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0AE8174F-0C6F-E311-A374-00248C0BE014.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0C273452-E86E-E311-BDFB-0026189438E1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0E896A3D-EA6E-E311-BDC5-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0EA1EC02-086F-E311-BBFF-00304867920C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/102BA9B7-E76E-E311-9998-0026189437E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/129C2AD4-996F-E311-AF02-003048678B84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/186E5450-EF6E-E311-96AD-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/18D40615-1C6F-E311-A1A1-002618943978.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1C6A528E-EF6E-E311-B54F-003048678FA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1CC9606F-966F-E311-B00C-003048678FAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1CD314F3-0E6F-E311-9061-0026189438F7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1E2E11A0-F96E-E311-B8DB-002618943939.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/228B5CC8-516F-E311-8BAB-002618943862.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/245B83D9-D46E-E311-AB75-002618FDA207.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/24F0194B-EC6E-E311-8402-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2860281C-D56E-E311-B749-002354EF3BDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2A736441-BD6F-E311-B4FC-002590593878.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2CD20178-746F-E311-81A5-00304867916E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2CD7EA87-176F-E311-A592-002618943854.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2CE45C5D-046F-E311-977C-0026189438D9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/301C7673-2871-E311-9520-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/328419B1-3E6F-E311-B9C6-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3470C0EA-D46E-E311-8A11-003048FFD71E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/34C5EFE8-D46E-E311-AA49-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3691F016-556F-E311-93C3-003048D15DB6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/36B7E423-2E6F-E311-88AD-002618943978.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/36D2B46E-3E6F-E311-B5B3-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3836877C-E46E-E311-9FFE-0025905A60C6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3C045D5B-356F-E311-907B-00261894393E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3C30FEDA-D46E-E311-A26B-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3C36C1B8-696F-E311-B57F-0026189438B3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3C695460-E86E-E311-95F3-0026189437E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3C7413D5-6C6F-E311-86AD-002618943800.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3E23BE46-E66E-E311-86C5-00248C0BE013.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3E3F5833-346F-E311-9572-003048D15DB6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3EA1B3C4-1C6F-E311-A5AE-0025905A60D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/404C49B4-F46E-E311-A7DA-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4055959B-676F-E311-913A-003048FFD728.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/40F3C4D3-8E6F-E311-9ACD-002618FDA277.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/42969308-0A6F-E311-8229-003048FFD76E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/44D20407-116F-E311-A6BA-003048678B7C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/44D4EEA4-096F-E311-86AC-002618943838.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/44E3E982-676F-E311-AC20-002618943911.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4621DF30-E46E-E311-BE37-0025905938A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4636E243-1D6F-E311-8496-0026189438B5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/46C94E4D-236F-E311-B4DA-00261894391C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/46D02B72-836F-E311-A07E-002618943896.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/46DDE38D-256F-E311-82F6-003048FFD79C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4834C121-156F-E311-BA23-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/48E59CEA-F16E-E311-BB21-003048678FF4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4A6D3BBC-016F-E311-B920-002618FDA26D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4A6E8746-D56E-E311-9258-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4C10363A-1B6F-E311-8F78-0025905A48F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4CA22196-056F-E311-B326-00261894394B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4CAFC061-E86E-E311-88FC-00261894389F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4CCFA81B-5D6F-E311-A1B7-00261894382D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5020F351-506F-E311-BC40-0025905A613C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/50C6C693-3F6F-E311-9C55-003048679182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/52B436FC-B26F-E311-8592-0025905A6134.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/52BD19BA-F06E-E311-89EE-00261894396B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/54E221C3-5D6F-E311-95D7-0026189438EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/54EC93AB-3A6F-E311-B176-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5839A78B-416F-E311-AEAD-003048678FFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/585BDAAD-0570-E311-964E-0025905A612E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5890BFEA-9F6F-E311-8F1F-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5A22F03B-EA6E-E311-92B1-00261894396F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5ACA42A0-8A6F-E311-B9E5-00261894390B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5C2BEBEE-586F-E311-B7B6-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5C514E58-A26F-E311-B729-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5CD751C2-7C6F-E311-9D3D-0018F3D095F6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5E14DD2B-0D6F-E311-9030-0025905964C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/60132B9B-716F-E311-9B90-0025905A60B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/60E6C893-496F-E311-B873-0030486790A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/60ED93A2-5D70-E311-86A6-0025905964C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/641321C4-0D6F-E311-B31F-0026189438D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/64EF2203-E76E-E311-AECA-002354EF3BDC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/66241750-786F-E311-9099-0025905A606A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/66F8B1E5-0F6F-E311-8CA2-002590593872.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/68D8DD00-E76E-E311-BF37-0026189438A9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6ACF89D9-636F-E311-9819-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6ADBDA8B-4A6F-E311-B25F-0026189438F3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6AE5A40F-116F-E311-9E42-003048678B1A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6CAF3DC9-426F-E311-B8AD-00259059642E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6E51CEB3-556F-E311-8F46-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6EFE9075-926F-E311-A8F7-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/70CC8DD5-D46E-E311-9EC6-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7277B503-3B6F-E311-B4C9-0025905A48E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/72CCDD1D-0D6F-E311-8453-003048FFD730.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7423E953-136F-E311-AA6F-00248C55CC3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/74A10DBF-646F-E311-83CF-003048678FEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/74AF644F-E86E-E311-B9FD-003048D15E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/768A4482-E96E-E311-9461-002618943901.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/76D00898-EC6E-E311-9E86-0030486792B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/76F19FC5-0B6F-E311-8831-00261894386A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/783D7CA0-E86E-E311-AD70-002618943849.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/78734AC9-ED6E-E311-B8CE-00304867BFAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/78DC8D3D-866F-E311-AD1C-002618943854.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7C92117C-466F-E311-A911-00248C55CC40.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/802FEE15-D56E-E311-B87D-0030486792B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/80742211-336F-E311-9DD2-00304867BFF2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/82C6C65F-DD6E-E311-A469-0026189438D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/847328E8-396F-E311-956F-0025905A6068.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/84BD65CE-086F-E311-9B43-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/86D406A4-EC6E-E311-B2ED-0026189438D8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/889EDD1D-EE6E-E311-8C15-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/88DD57D2-1B6F-E311-BABA-003048679296.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8C792F99-826F-E311-B89B-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8CB62461-E86E-E311-99B6-00261894390E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8E3A73D9-686F-E311-BA63-002618943980.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8E79CA92-1E6F-E311-95E2-0025905938D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/94CE09B9-1C6F-E311-BD94-0026189438E6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/94CE4BD8-DE6E-E311-BC1B-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/94DFAB78-F06E-E311-AC79-00261894380A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/96EB4716-446F-E311-BC70-003048678B00.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/96F15FDD-596F-E311-9F18-00304867BED8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/96F5D9C9-EA6E-E311-A9A8-002618FDA207.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9892613E-E16E-E311-A3C3-003048678FA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9A156E55-ED6E-E311-91B5-0025905964CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9A858291-7C6F-E311-8153-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9A95D643-D56E-E311-95B3-0025905A6126.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9AC7BB9D-FF6E-E311-BB56-002618943927.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9C6414A0-9B6F-E311-876B-003048679162.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9C796212-E56E-E311-BFF9-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9CA5F2B4-1C6F-E311-A042-00304867904E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9E3CFD06-EB6E-E311-B6E2-003048678FA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9E8A657F-4D6F-E311-9CAA-002618FDA287.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9EE67A39-316F-E311-A3B0-0025905A6134.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A099B3A8-1F6F-E311-BF7B-002618943920.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A405D15C-5B6F-E311-9D95-002618943918.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A44D85F8-096F-E311-9F29-0030486792B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A4568942-EF6E-E311-A1E7-003048679150.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A4B47723-586F-E311-8342-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A4C35319-2C6F-E311-A682-0025905A60B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A649A342-EA6E-E311-82D1-003048678B12.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A6DCE238-EA6E-E311-B67B-002618943886.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A6E007B9-186F-E311-9D1E-0025905A613C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A8E731F2-886F-E311-A3D9-002618943962.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AAA562DE-D46E-E311-B77F-003048678FFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AC4EAE99-EB6E-E311-9816-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AC784A08-D56E-E311-A3E3-002618FDA210.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AC9690DD-226F-E311-AA41-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/ACC50C20-D66E-E311-BA2E-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AE0B4B4D-776F-E311-8916-0025905A48EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AE19B5B6-F56E-E311-B833-002354EF3BE6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B0446BA1-EB6E-E311-B3B9-001BFCDBD182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B0AE60D1-516F-E311-87C4-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B0B8C05A-0E6F-E311-942A-00261894396A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B0BB93B8-EE6E-E311-8BCB-00261894396F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B0BBA860-D76E-E311-84EF-00304867902E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B2A20DE2-D56E-E311-A63E-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B2CAF478-2F6F-E311-AC97-0026189438D5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B43BC21E-E56E-E311-AE44-003048679294.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B4710EDF-D46E-E311-8E67-002618943865.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B4D9BFE6-3970-E311-AB68-0025905A6126.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B8C6A9C2-0B6F-E311-960A-00304867904E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BC316973-E16E-E311-BB34-0025905A60F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BC4BB403-E76E-E311-88F1-002618943842.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BCABE462-E86E-E311-A447-003048678B86.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BCF7B3D9-0A6F-E311-A126-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE495D3A-D56E-E311-A105-0025905938B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C0493D17-D56E-E311-B173-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C22FDCC5-086F-E311-A62F-002618FDA210.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C43C524B-EA6E-E311-B9EC-003048678B3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C46BA7BA-326F-E311-B882-0030486792A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C4EBD88A-296F-E311-97EC-003048FFD732.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C4FB6370-126F-E311-9B22-003048B835A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CAE4819F-A86F-E311-92B4-0026189438BF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CE8C1624-936F-E311-BFC6-002618FDA262.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CEBC4BDD-D46E-E311-A87B-0026189438C1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D0C7B0D8-DF6E-E311-8127-0025905A60FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D22D4436-276F-E311-8247-002618943870.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D2C4A094-396F-E311-AA23-0025905A60F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D44D0ABF-3D6F-E311-B5F0-0025905A60F4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D4A731E5-816F-E311-B737-00304867C034.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D4CE4796-2A6F-E311-9A02-002590596484.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D60F9326-6B6F-E311-8CC5-002618943980.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D64CA72C-5F6F-E311-BB59-002618943977.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D684A8AE-0D6F-E311-8E83-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D8007B7A-6771-E311-95BB-0025905A48F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D80EBFC4-816F-E311-BA61-003048678B12.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D88970C4-E26E-E311-AD57-002618943886.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D8AC93AD-1C6F-E311-ABBD-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D8AE4E4B-FD6F-E311-9E13-003048678FAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DA64D122-C36F-E311-9608-003048D15DB6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DA8A863C-E36E-E311-B7F4-002618943951.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DE25ADFD-1F6F-E311-9EDE-00259059642A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DE822B6E-DE6E-E311-B547-00261894396F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DE9B0170-066F-E311-97E5-00261894393A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E01AC30D-1C6F-E311-A8BD-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E025D4B7-E76E-E311-B281-0026189437FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E24DE6C2-816F-E311-8022-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E4B2CF61-E86E-E311-B188-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E4CFE23A-206F-E311-9E4D-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E6E12996-876F-E311-AC35-0025905A48F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E89B96FF-726F-E311-8EDA-0026189438AF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E8F1D8E7-E36E-E311-9EB2-00304867BEDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EC24822F-DF6E-E311-BF14-002618FDA210.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EC571F75-376F-E311-98F6-0025905A60B0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EE0FA5A6-936F-E311-A00B-002618943900.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EE76A5EB-F16E-E311-87CC-00248C55CC7F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EEDE7541-906F-E311-9337-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F0C46D4F-986F-E311-8A2B-0026189438B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F241475D-A56F-E311-A832-002618FDA279.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F2F8DFD0-8C6F-E311-8322-002618943934.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F6B7490A-EB6E-E311-B0D8-00261894389F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F83247B9-DF6E-E311-8A98-0026189438DD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F8F0A0CE-616F-E311-BDED-00261894397A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FC73C685-036F-E311-BFB1-002618943937.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FE206DA2-096F-E311-8714-0026189438E2.root',













































       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/007B102C-EA6E-E311-9E60-0025905A613C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/00C6810E-886E-E311-A0F0-003048678C62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/025F7540-3F6F-E311-94B3-00304867903E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/027761B0-856E-E311-9F58-002618943843.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/02A11574-846E-E311-83E8-00261894388D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/02B0DCF1-7F6F-E311-B451-0030486790A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/046AADA3-556F-E311-9255-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/04E00061-846E-E311-9AA7-00261894394D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/04F415DD-896E-E311-A180-003048679182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/064CB810-876E-E311-8CC2-003048D15E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/06BD668E-C16E-E311-8367-00261894383B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/083D97B2-F46E-E311-93B1-0026189438D7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/08844210-876E-E311-8364-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0886CC27-746F-E311-B6D9-00261894389E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/088900EE-BD6E-E311-B00C-002618FDA211.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/08B33092-AB6E-E311-A7B9-0025905938B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0A930FFB-866E-E311-97A3-0025905A60B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0ADA4EF4-896E-E311-B101-00261894390A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0C21C600-866E-E311-A377-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0C45EC86-3C6F-E311-ABD8-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0C6D1D38-886E-E311-8695-00304867C034.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0E5107EC-866E-E311-B0CC-0026189438E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0EA4F2A5-846E-E311-98D0-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0EB2B24B-CA6E-E311-9129-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0EB9C34E-876E-E311-B0DA-0025905A60FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/0ED849D7-866E-E311-AF51-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/101A432D-8A6E-E311-909D-003048FF9AC6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/109AA8A1-3E6F-E311-B7C5-00304867903E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/10B02EF7-896E-E311-A094-00248C0BE013.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1233C5A3-3E6F-E311-9F71-003048678AC0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/128A8AD2-856E-E311-A888-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/129742B8-856E-E311-A687-002618943908.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1469C0BD-A66E-E311-AAD4-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/14AD1B07-406F-E311-97DD-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/14AF6DB2-3B6F-E311-AA60-0025905A60DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/16365081-846E-E311-B4DB-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/165BC24A-886E-E311-9A9C-00304867BF18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/16B30389-0F6F-E311-B4D6-002618943832.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/184FFBF5-856E-E311-89F0-0025905A60D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/18751DB8-A86E-E311-9F95-0025905964A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/187B669A-CC6E-E311-A7A6-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1AA81F6C-766F-E311-BB65-002618943937.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1ADEA52B-886E-E311-8E44-00261894393F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1C7DB6D1-856E-E311-8B0F-002354EF3BE6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1CBD4A2C-3D6F-E311-848C-0026189438A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/1EFA50E2-C96E-E311-B028-003048FFD76E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2052F0E6-856E-E311-90BE-003048678AFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/207044DE-856E-E311-B18F-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/24507F30-2D6F-E311-8B13-00261894393F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/261B8C7B-716F-E311-98DF-00261894389E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/266A122B-D46E-E311-8EF0-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/26B4F148-886E-E311-8AC2-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/26C78D4E-BF6E-E311-9BA0-0025905964C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/284FA5EC-896E-E311-BA10-0026189438CB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/28C9E8DC-866E-E311-9749-003048678E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/28F8690D-BA6E-E311-B7F9-003048FF9AC6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2A5E1195-E66E-E311-B0FE-002618943915.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2A7AABC4-886E-E311-9E60-0025905A48B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2AB37742-886E-E311-8C38-003048679164.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2C7A70E8-9D6E-E311-9D73-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2C93B2CD-D06E-E311-8D03-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2CF5DC66-886E-E311-9EF5-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2E2B7735-696F-E311-A7A3-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2E4A09D0-CD6E-E311-8FD7-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2ECF6CDF-856E-E311-9F9E-002618943954.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/2EDD2330-B06F-E311-A1C8-00304867906C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3093551C-C26E-E311-8239-0025905964C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/32D5A8FE-896E-E311-958C-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/346B9ADD-3E6F-E311-87FB-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3470BF02-876E-E311-B311-002618943880.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/34F66EE6-EA6E-E311-8C7E-00261894382A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3635799B-8B6E-E311-8D5A-002618943869.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/365C4C3C-F56E-E311-A403-0025905A609A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3693E048-AF6E-E311-B9D6-003048FFD736.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/36AAC728-866E-E311-A23D-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3835A6E4-866E-E311-895E-002354EF3BDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/386893DA-9170-E311-B5D1-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/389DB46E-036F-E311-B57E-003048678B8E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3A840544-C76E-E311-B2EB-0025905AA9F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3AFA1736-D86F-E311-A203-0026189438EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3C090A16-886E-E311-8FC8-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3C6A6AE3-856E-E311-BB15-00261894380D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3C736122-886E-E311-B891-002618943870.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3CA9146B-886E-E311-8FA4-003048678AE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3E4EBAD5-856E-E311-8890-002618FDA265.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/3ECC263B-C76E-E311-A71B-0026189438E2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4008ADF3-FE6E-E311-A2D6-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/401D046B-B26E-E311-9810-002590596486.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/42233908-886E-E311-98A8-00261894385A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/428891E7-866E-E311-9B35-003048D15E14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/44102F31-8E6E-E311-98D8-002618943975.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4441EDB8-856E-E311-827A-003048678FB8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4455AF3C-866E-E311-82B3-0025905A60A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/44C37827-3B6F-E311-8332-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/44D2EEDF-8F6E-E311-BDA7-00304867C1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/48101B18-8A6E-E311-A47A-003048FFD76E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/481A979C-936E-E311-950E-002618943962.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/48AA58CC-856E-E311-BC7B-002618FDA248.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/48DFABC2-1F6F-E311-BAEA-002618943939.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4A388D54-0B6F-E311-956E-003048679244.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4A723386-306F-E311-B4F8-002618943916.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4C52FE6D-886E-E311-9D75-002618943845.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4E1B378B-2470-E311-B86B-002618943898.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4E38F1F3-866E-E311-97E1-003048D15DB6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/4EAFB203-8A6E-E311-AA08-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/520924E8-856E-E311-9046-003048D15E14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/52EDDEDB-896E-E311-8095-0026189438A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/541D87A7-986E-E311-A342-0026189438B5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/545896D6-D86E-E311-BBD9-002618943926.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/546F30D9-896E-E311-B858-002618FDA259.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/54C5982E-DF6E-E311-B8C5-003048678FE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/54F9433C-B66E-E311-8260-002618943962.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/560932F0-FC6E-E311-A952-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/56ACE3FF-3D6F-E311-983E-003048678AC0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/580382D4-866E-E311-BB6B-003048D3C010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/585E15C1-B06E-E311-A5DC-00261894384F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5881CC5B-876E-E311-8ACC-0025905A60D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/58DBC2F3-856E-E311-AD31-002618943862.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5A3BB7E2-866E-E311-A10C-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5A7E3AF3-1671-E311-AE1F-002618943860.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5AD06B61-876E-E311-94B1-003048FFD752.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5C69C0EA-D66E-E311-A835-0025905A48D0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5C9CEB34-E86E-E311-A289-00261894389E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E01BA04-656F-E311-9AF6-0025905A60DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E4CC7BA-D46E-E311-9F8A-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/5E528426-886E-E311-A899-003048D15E2C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/606852C6-F76E-E311-BE24-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/609CFCA9-9F6E-E311-ABB3-0030486792B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/60A1B549-886E-E311-9708-00261894387E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6223BC48-956E-E311-9CC0-0030486792AC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6253C747-886E-E311-9FCB-00261894390B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6267DD23-876E-E311-A789-002618943867.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/647C387A-AF6E-E311-8D7D-003048678B34.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/64C96CD7-9E6E-E311-96E5-003048678C26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/64E61600-876E-E311-9EF8-002618FDA216.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/668EAF4E-876E-E311-8FE0-0025905A60FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/66D4DC07-8D6E-E311-91D6-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/681A557B-3F6F-E311-AA00-0025905A60CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6850D562-846E-E311-88F9-002618943937.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/68C60C92-A76E-E311-AD3F-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/68CF4D88-C66E-E311-A8D3-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6A062D9C-A46E-E311-9A75-003048678A78.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6AE8BE57-3D6F-E311-AA83-002618FDA250.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6CC8D479-3C6F-E311-88DD-0026189438A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6E2DBF22-066F-E311-80F9-002618943886.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6E431D64-886E-E311-AAE1-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6E4B3485-846E-E311-AEEB-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/6EAD97B5-066F-E311-8259-0026189438E1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/70D6C57C-096F-E311-AF0D-003048678E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/70F968CB-626F-E311-AC33-00261894395F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/72E9C4ED-C06E-E311-8107-0026189438FF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7480F846-AA6E-E311-814E-00304867BFAA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/74A3D051-AE6E-E311-A7C1-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/74CF64A7-846E-E311-9E54-002618943914.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/760323DE-866E-E311-9B8B-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/76906666-886E-E311-A10C-003048678B06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/769AB40E-886E-E311-9431-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/76B267DC-856E-E311-B3A7-0026189438F6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7853DE78-846E-E311-8466-002354EF3BDF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/785986A2-CA6E-E311-B2BB-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/788061EA-F36E-E311-A354-0025905A60E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/78C7AB5F-846E-E311-863A-002618943963.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/78D6CDEF-866E-E311-9472-00261894390A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7AB1A0EB-856E-E311-96CA-002618943807.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7ADBAEA9-856E-E311-B914-002618943826.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7C42FB69-886E-E311-8212-002618943811.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7E32F08A-0C6F-E311-9310-003048678FA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7E3AA583-846E-E311-BFE9-00261894386D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7EC34B8D-956F-E311-AD8B-00248C55CC7F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7ECEB5C4-116F-E311-BD35-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/7ED0B2A1-EF6E-E311-A179-002618943957.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/80887CFA-866E-E311-B860-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/80D43501-8A6E-E311-8275-002354EF3BDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8237526D-886E-E311-B757-00304867929E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/84CC6D7B-D66E-E311-8D62-002618943832.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/84DF3DF3-856E-E311-B54B-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/86260FD6-F16E-E311-ADD4-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/862B0806-886E-E311-8D2A-00248C55CC40.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/86B6D2E3-866E-E311-A537-00304867929E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/86EAE13E-B66E-E311-8346-00261894393C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/88EEFD3A-B66E-E311-9048-00304867C1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8C7CC5F8-B26E-E311-B5CF-0026189438A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8CF2E127-F66E-E311-8B53-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8E7FF72A-3A6F-E311-8C87-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8E9CE546-226F-E311-9CD8-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8ED082E4-866E-E311-8EA7-003048678C26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/8EF53301-8A6E-E311-9B45-002618943865.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/900CFC1E-BC6F-E311-B81F-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/901A9F20-006F-E311-8F79-0026189438F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9031B1EB-896E-E311-9FB9-00304867924E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/920B91AD-846E-E311-8EF4-003048678FF6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/921EEF51-C96E-E311-B271-003048FF9AC6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/923B5CAC-856E-E311-93DA-00261894393F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/924B440F-8A6E-E311-A032-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/926600EB-866E-E311-A5CD-003048678B8E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/92693365-3F6F-E311-A324-0026189438A5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9421EF9C-A06F-E311-88BA-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9491961C-886E-E311-BD5F-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/94F00B16-886E-E311-B04D-003048678B86.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/963ED9D7-856E-E311-A3A5-002618943886.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9648E045-426F-E311-9315-0025905A607A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/96D1D6F6-856E-E311-AB63-003048D3C010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/96F441EA-866E-E311-8C65-00304867924E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/96FF25D4-856E-E311-912C-003048679244.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9826D144-A56E-E311-A12B-00261894394B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/98651E4A-876E-E311-8CF6-0025905A6070.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/98EABCC8-856E-E311-8735-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9A84AC0D-BA6E-E311-9531-003048FF9AC6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9AA498B1-366F-E311-B28B-002618943986.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9AA4E68C-9A6E-E311-8C0D-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9ADBE33D-886E-E311-8EFB-003048678FF8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9CC5460E-876E-E311-B0FD-0026189438E9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9CF4AFD7-6F6F-E311-883E-003048FFD770.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9E385A05-396F-E311-9F19-001BFCDBD1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9EA9FFDA-896E-E311-82C5-0026189438D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9EB563EB-866E-E311-AD08-0026189438C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9EC4BC64-C36E-E311-9610-0025905822B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/9EF5F996-046F-E311-B7DB-002618943854.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A0D2F74B-876E-E311-91BB-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A2039EE2-856E-E311-B69F-002618FDA211.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A25C2F1E-886E-E311-B7AA-00248C55CC97.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A2FEA8E8-CE6E-E311-AE20-002618943975.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A4331C18-876E-E311-8976-002618943906.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A4BA626C-976E-E311-A5FC-00261894393F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A4F53D16-876E-E311-98E2-0026189438AB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A64BD486-BE6E-E311-957D-00261894390B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/A87D9627-3B6F-E311-9278-0030486792B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AA85A30B-5E6F-E311-8F4A-002618FDA287.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AC2EC14F-336F-E311-9C14-0025905AA9F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AC8E6DE7-856E-E311-8A21-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE84E42C-176F-E311-BF3B-0026189438FF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AE8E354E-686F-E311-A4A3-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/AEE65FE9-B96E-E311-9C02-003048FFD770.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B04ED9B0-C86E-E311-89CE-003048FFD756.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B05BB3BE-FB6E-E311-89FD-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B07FD3D6-866E-E311-872E-00261894386C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B085AFCA-9C6E-E311-8CC6-00304867BFAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B08FC567-026F-E311-83AC-0025905A60D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B09F9372-886E-E311-9191-0026189438FD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B0EA97DB-BB6E-E311-AFD3-00261894387B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B2256B65-C76E-E311-8C47-00259059649C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B29025E5-A96E-E311-84DB-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B2AC3DD4-A96E-E311-9F87-003048679070.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B4CC7123-876E-E311-A380-002618943953.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B6DDF384-4E6F-E311-AEAC-00248C0BE01E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/B84E9654-886E-E311-A1B2-003048678B14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BA346991-6C6F-E311-B4C8-003048678BAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BAB79868-846E-E311-8516-00304867BFAA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BAC4E22D-866E-E311-A1A0-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BC58140F-886E-E311-A8A2-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BE529D55-8F6E-E311-B5B4-002618943976.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BE8718E2-896E-E311-B474-002618943906.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/BEE652BE-966E-E311-9747-002618943976.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C099426E-886E-E311-A3DB-002618943880.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C0AF46D4-A36E-E311-8599-003048FFCBB0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C26D82D6-9B6E-E311-8F8D-003048678B92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C27B82D9-F86E-E311-90A0-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C2901CCF-866E-E311-B896-003048678DD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C2C1CE7C-D26E-E311-A4B5-003048678B92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C4A6A0FD-896E-E311-9F4C-002618FDA207.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C4ADF196-846E-E311-9AF3-003048678FA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C4B4E50B-886E-E311-9CD1-00304867924E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C6804C78-916E-E311-BAD1-00261894398B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C6AD79E8-856E-E311-93C1-0026189438CB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C812A944-A26E-E311-8287-002618943904.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C8371271-886E-E311-95C7-0030486791F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C84D3448-886E-E311-9294-002618943876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C862EAA9-AB6E-E311-A361-00261894388D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C8923EC9-856E-E311-809B-002618943852.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/C8BF46AD-856E-E311-A91B-002354EF3BE1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/CA7941B2-C46E-E311-8D75-002354EF3BD0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D0F59983-A06E-E311-84CB-002618943810.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D0F97592-C96F-E311-BE0C-002618943971.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D27FF2CD-856E-E311-A921-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D2ADA771-A86F-E311-A997-003048FFCC1E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D403E3F5-B36F-E311-9C30-001A928116D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D40714F1-896E-E311-9BCF-0030486790A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D41D68E6-896E-E311-96E3-002354EF3BDF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D42B3B3D-B66E-E311-BA6D-002354EF3BE1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D4B3FE97-C46E-E311-B42E-0025905A607A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D4FABA06-8A6E-E311-AA70-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D4FC733D-EB70-E311-A63B-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D6626069-DB6E-E311-AE56-003048D15E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D66E11AD-076F-E311-9620-00261894380D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D6D5BDDA-856E-E311-8EA2-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D80D3705-8A6E-E311-A0EF-00261894393B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D868065F-886E-E311-846C-002618943943.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D8BCA70F-886E-E311-A9C8-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/D8CD3153-446F-E311-ADD9-002618FDA259.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DA6AFA52-886E-E311-B645-002618FDA26D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DACE0DDD-866E-E311-BC41-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DC09C0F1-3B6F-E311-8AF7-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DCC5F4B2-C06F-E311-A5D5-0026189437FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DCE08977-846E-E311-AA3F-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DE033C06-BA6E-E311-A86E-003048FFD752.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DE33A480-846E-E311-AE48-0026189438AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DE699057-BD6E-E311-B101-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/DE840319-876E-E311-9BB9-002618943979.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E0837A37-876E-E311-B11C-001A92971B72.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E09FDA86-B16E-E311-A7F9-003048FFD730.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E212D2D8-896E-E311-87DA-0026189438F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E2658F47-886E-E311-8A5E-002618943914.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E2E62BFA-856E-E311-84FA-002618943920.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E448AF27-AD6E-E311-9DE6-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E456C529-876E-E311-9527-002618943826.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E46EC8E8-896E-E311-8DD7-003048679236.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E47E5610-886E-E311-A279-002354EF3BDD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E673D7D2-936E-E311-B5A7-0026189438D5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E696283F-866E-E311-8016-003048FFCC2C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E6E7036C-A46F-E311-9600-0025905A60BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/E83FC198-846E-E311-9C50-00261894386C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EA7321BB-CB6E-E311-B9A2-003048678A78.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EAE37DFD-856E-E311-A8B7-002618943901.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/EEA632EC-896E-E311-8352-003048B835A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F014B236-1D6F-E311-A8FB-002618FDA277.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F02DC339-876E-E311-8FC0-002618943845.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F0BC7F70-876E-E311-9236-0025905AA9CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F0BEC932-886E-E311-8995-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F0E41EA2-846E-E311-B275-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F22F7E38-886E-E311-999D-00261894391B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F283951B-256F-E311-A051-002618943906.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F46638F8-896E-E311-B93C-001BFCDBD1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F475C0BF-856E-E311-82D2-002618943867.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F6181905-C56E-E311-B626-002618943986.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F64E69A2-EC6E-E311-B6B6-003048678BAA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F6AA9C05-876E-E311-8EC3-003048678AE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F6C14506-D06E-E311-9722-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F80266CF-856E-E311-A40F-0025905938AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8694D6A-886E-E311-8339-002618943880.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F87D31FD-AC6E-E311-A8CC-003048FFD740.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8843986-146F-E311-A764-003048678B30.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F88E0B8E-8E70-E311-91BC-003048678F9C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8A7D14E-876E-E311-A7AA-0030486791F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8D2CED1-866E-E311-AB52-002618943957.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8E5F824-886E-E311-86C4-0026189438DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8E920E0-E16E-E311-ADE8-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/F8E96F0E-BA6E-E311-93D7-003048FF9AC6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FA3A6EB2-A16E-E311-8858-002618943927.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FA46274D-886E-E311-8CC6-002618943980.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FA6EB50A-BA6E-E311-A005-003048FFD752.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FA86BCC2-CE6E-E311-AA0F-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FA8AF2B4-846E-E311-A08C-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FAE9BC05-BA6E-E311-934E-003048FFD752.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FAEE66A1-886E-E311-A949-0025905A48D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FC223F35-876E-E311-99E6-002618943800.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FC323A06-BA6E-E311-B63F-003048FFD752.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FCD68C0B-0E6F-E311-927D-0026189438C9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/00000/FE3D16F9-BF6E-E311-A6E6-0026189438BF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/000BD8A4-4B6F-E311-9835-002618943911.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0421D77B-BA6F-E311-B97A-002618943866.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/044F85B7-586E-E311-A6B1-003048679296.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/046EE92A-436F-E311-9BD6-0025905A606A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/060D7A8B-246F-E311-B899-0025905A60FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/06E9C3C3-4E6E-E311-87B4-003048679070.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/0ECEBE34-4B6E-E311-9AEA-0025905A6104.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/103068C1-D36E-E311-B9A4-003048679166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/105BBE6E-DC6E-E311-B343-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1255F76D-436F-E311-9705-00261894384F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/125B482A-C66F-E311-B7C1-0025905A60EE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1286E275-F76E-E311-962D-0026189437FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/12ADA5C8-566E-E311-9BB7-003048FFD744.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1662FC08-AC6E-E311-9D51-0026189438AD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/16C1678A-D36E-E311-ADE1-00261894387E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/16CE1734-596E-E311-B28D-0025905938A4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/16D1C275-966E-E311-B859-0026189438E1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/18B0D3E4-4E6E-E311-BFF5-002354EF3BD2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1C0D1FD5-106F-E311-AB3B-0025905A48BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1C178464-4F6E-E311-93C1-0026189438C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1CA37699-506E-E311-A34E-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1CC277A7-5E6E-E311-AB1E-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1CDEFE34-5B6E-E311-9355-0025905A6126.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1CE45E97-D36E-E311-9FFB-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1E93B2B5-926E-E311-BA01-003048FFD7D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/1EEC1452-FE6E-E311-834C-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/201E1320-3A6F-E311-A362-002618943953.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/207D31A8-496E-E311-A53F-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/263B0593-626E-E311-906B-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2A0D6649-FC6E-E311-91FB-002618FDA250.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/2AF516D0-466E-E311-8F9F-003048678B38.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/30477781-AF6E-E311-9801-002618943970.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3073B716-4A6E-E311-9C22-002618FDA287.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/309EC179-3D6F-E311-8AEF-0025905964BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/321D0E18-556E-E311-ABC5-00261894394D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/32277D9A-546E-E311-AD92-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/32D89B24-5A6E-E311-8222-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/32FF9B7B-686E-E311-8844-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/343E08BD-4C6E-E311-9C6F-0025905938B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/34B6CB97-176F-E311-9E33-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/36D3A0D8-476E-E311-8BA3-0025905A60D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/36DF02C2-3A6F-E311-8AE1-0026189438CF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/36FAAE71-D36E-E311-A970-00261894385A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3A57824A-4E6E-E311-97B5-0025905938A4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3AB82162-4A6E-E311-97F4-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3AD36A08-3F6F-E311-B290-0026189438D8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/3EBC4EA1-946E-E311-8E21-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/407BA4F1-D26E-E311-A87A-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/42D82BA5-5C6E-E311-9D57-00261894383B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/446FBB3A-536E-E311-97C7-0025905A609A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/44D03CC5-546E-E311-9A40-0026189438F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4629069A-5F6F-E311-AD54-0026189438A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4CB84F5D-4B6E-E311-8EE7-0026189438F3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4E081B28-AE6E-E311-9A4E-0026189438F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4E908B41-656E-E311-889C-003048678A6C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/4EC1F065-916E-E311-93EC-003048FFD7BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5011FF9F-A66E-E311-BCAD-00261894397F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/524AA27E-496E-E311-B508-003048FFCC1E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/52537ED5-4E6E-E311-ABF3-003048678C62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/52DF15E0-5C6E-E311-BC03-003048678ADA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5481F16C-406F-E311-BC76-0025905A60BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5641E552-9A6F-E311-B992-003048678B84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/58CC1BE2-5C6E-E311-B510-00304867BEDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5A34328B-D36E-E311-90D0-00261894386D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5A3AE188-8A6E-E311-A808-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5A52FAE2-D66E-E311-BD07-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5C579EB9-096F-E311-9405-00248C0BE018.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5C705CEE-536E-E311-866D-002618943924.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5C736468-376F-E311-8EE7-0026189438C1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5C823C4B-9B6E-E311-9013-002618943959.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5E246351-486E-E311-8D1A-00248C55CC7F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5EA02B0E-8D6E-E311-B292-0026189438A7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5ECF39E5-D26E-E311-9D5C-001A928116D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/5EDEC837-AB6E-E311-8EE3-002618943868.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6024334B-4F6E-E311-999F-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/603EF3AD-676E-E311-BF4D-001BFCDBD182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/608C3E03-D36E-E311-ABA6-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/62413028-516E-E311-944B-002618943864.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/641FE6A3-206F-E311-B810-0025905AA9F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/642AB383-506E-E311-A0A9-0025905A6088.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6495DFD7-D26E-E311-B030-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/64DDD2D3-366F-E311-A857-00261894380A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/660EA104-D36E-E311-938A-00261894385A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6683AA16-4D6E-E311-ADEE-0025905A48D0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/68EFAD65-466E-E311-A210-003048FFD732.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6A821BB3-F06E-E311-8015-0026189438A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6C483DC3-5B6E-E311-8AAE-0025905938AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/6E7D33C8-286F-E311-8FA1-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7062A924-526E-E311-8CA7-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/70D38167-526E-E311-8115-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7223F4F9-D26E-E311-876C-0026189438D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/72D95CFC-936E-E311-80A0-00248C0BE013.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/74A7E09E-9D6E-E311-AE47-0026189438D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/76F091EF-556E-E311-9B32-002618943943.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/78194E41-596E-E311-ABB3-002618943984.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7834AD97-A66E-E311-A832-0030486791AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7891A055-336F-E311-B2FD-0030486790A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/78D01621-AE6E-E311-B4BE-0026189437EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7A956722-636E-E311-B671-003048678BB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7A963289-7B6E-E311-A1CD-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7AB272D4-5B6E-E311-A652-003048678B8E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7C99677B-3F6F-E311-8B80-0025905A606A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7CE238C2-666E-E311-B32C-002618943911.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/7E64D0D3-886F-E311-86D6-0025905A48F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/809EB542-5E6E-E311-B59D-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/820EA5A8-456F-E311-ADBF-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/82B3ABE2-566E-E311-89F3-0025905A60B0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/82FFC883-D36E-E311-9E8E-00261894390C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/846059D0-8E6E-E311-810C-003048678B8E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/849A9368-646E-E311-AFD3-0026189438D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8633FD71-A16E-E311-91EA-003048FFCC0A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/88B8C60D-D36E-E311-B335-003048678A7E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8C09AE31-A06E-E311-BA6F-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/8EE0E09B-1E70-E311-AA75-0025905964BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/902B56BC-326F-E311-B870-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/90EF90C3-5A6E-E311-B5DD-00261894386D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/92485E10-726E-E311-86FE-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/94BD1942-B36E-E311-AFAA-002618943962.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/94DD2E5E-586E-E311-B52D-003048679294.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/94E156AF-496E-E311-9825-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/961801BE-5C6E-E311-9030-002354EF3BDD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/965C44A1-D36E-E311-994C-002618943962.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9808DC0D-5E6E-E311-BB45-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/982427FB-636E-E311-86EA-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9A385F86-4E6E-E311-A464-00304867BFAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9A74C534-3E6F-E311-8FC4-0025905A60B0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9A9EE67C-D36E-E311-9E34-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9C3B4496-A96E-E311-962A-002618943945.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9CAAB71F-526E-E311-A323-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9E6011B9-2D6F-E311-8D10-00261894385D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9E7441E8-4C6E-E311-8F35-0025905A6138.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/9E9FFE49-626E-E311-93D2-0026189438DD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A0141662-4D6E-E311-ACA6-0025905A60D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A07571B9-576E-E311-B58B-0026189438EA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A0F1CAB8-4A6F-E311-A35C-0025905A48F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A2D6BB41-766F-E311-8D78-003048678E80.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A2DA6F1A-316F-E311-86BE-002354EF3BE3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A2E185C4-5B6E-E311-A836-00261894398B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A4217058-5F6E-E311-AAA1-0025905938A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A483D8CF-A46E-E311-B5FF-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A652F0EE-516E-E311-AB48-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A6AE7052-076F-E311-84AB-00261894385D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A8074F3B-4A6E-E311-B6D1-00248C0BE012.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/A8571AD8-D26E-E311-88D0-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AC339195-556E-E311-8276-0025905A60C6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/ACE0BBB2-6F6E-E311-B890-0026189437F9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/AED4D234-546E-E311-9297-002618943953.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B00FFAB3-6B6E-E311-8886-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B06E3675-A56E-E311-A8F1-0026189437EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B43E13D5-4E6E-E311-8547-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B6291244-536E-E311-86E0-002618943967.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B6B8FA9B-B56E-E311-B6BD-003048678B08.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B6B99291-E96F-E311-840D-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B8066FE2-4F6F-E311-A7CC-0025905964C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/B858F175-576E-E311-B0D4-002618943842.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BA0D13AD-D36E-E311-919C-003048678A7E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BAD856E0-D26E-E311-A8EC-002618943962.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BAE7EBC6-F26E-E311-BD72-003048B835A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BC78BA06-4D6E-E311-92AE-00259059391E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BCF7227A-D36E-E311-A173-00261894396B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE102F30-5B6E-E311-9699-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE45A1F7-D26E-E311-A92D-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE5885D7-656E-E311-A12E-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE7C377A-D36E-E311-A3C7-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE805E83-4A6E-E311-89D8-002618943901.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/BE8742DB-476F-E311-BC18-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C028903F-A36E-E311-B93A-002618FDA250.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C03900DE-D36E-E311-8740-0025905A60F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C05BA95B-6D6E-E311-9031-002618943866.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C05D0BCB-586E-E311-9445-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C09088EF-976E-E311-AFBC-00304866C398.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C2984B17-5D6E-E311-83DD-0025905A6132.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C4032172-606E-E311-BF8A-003048678E52.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C433167B-AF6E-E311-B295-002618FDA259.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C4A202A1-D36E-E311-A09E-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C6A37990-516E-E311-92EE-00261894383E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C6ECEF0D-D36E-E311-853A-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/C889F937-606E-E311-8650-002354EF3BD0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CACC11EF-9B6E-E311-B4A7-002618943945.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CC97989A-D36E-E311-95AA-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CCB065F8-EE6E-E311-B512-0025905A6104.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CE1A5309-536E-E311-A7C2-002618943800.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/CEFB1665-526E-E311-A015-003048678B84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D0407EC6-B56E-E311-BC48-003048678F84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D048633C-496E-E311-8FBB-0026189437EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D073549F-886E-E311-9D00-00304867C04E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D299EB6A-026F-E311-9B1C-001BFCDBD1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D2D11CF9-5B6E-E311-9B2D-003048678B7C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D2EF6DD6-D26E-E311-A245-00261894386D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D4509811-D36E-E311-BD89-002618FDA210.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D463C5F4-D26E-E311-92B2-0026189437FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D468DA0B-4D6E-E311-8182-0025905A60A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D479F9A6-3F6F-E311-A815-0025905A606A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D4C618E4-D26E-E311-8E49-002618943833.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D6748BAC-D36E-E311-B60F-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D6988B88-A16E-E311-B579-0025905A60D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/D8DE54AF-556E-E311-8D34-0026189437FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DA7F3094-D36E-E311-92EC-003048678B34.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DA82B4EF-D26E-E311-AAE2-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DC0A5CE6-4B6E-E311-A3F9-002618943864.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DCB77FD5-596E-E311-949B-003048678B00.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DCFE578B-576E-E311-969C-0025905A60BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DE453146-526E-E311-ACA0-002590593872.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DE81790A-4B6E-E311-8EC6-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/DE8D1A2C-596E-E311-BBCE-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E062FA7F-586E-E311-8EFE-0026189438F3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E0E9D097-D36E-E311-B458-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E24D9A0C-766E-E311-B9B1-003048678FB4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E27D8CD3-4B6E-E311-9BD1-0025905A611E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E2D42830-5B6E-E311-A8D1-002354EF3BE1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E626077E-836E-E311-B840-002618943970.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E65686BA-B56E-E311-AB75-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E6D3D86E-AE6F-E311-BE4C-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E825C392-486E-E311-A8D8-002618943966.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E84DDE59-616E-E311-AC6F-00261894393E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E876108B-156F-E311-8008-002618943983.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E87A1DC6-516E-E311-97B0-0025905A6064.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E8E2FA66-5C6E-E311-B7BB-0025905964B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E8E94E02-4D6E-E311-9727-00304867C04E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E8E97635-6A6E-E311-AB9B-0026189438F3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/E8F5705E-4F6E-E311-8B80-00304867906C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EA818E0A-426F-E311-AD5A-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/ECB2F63B-496E-E311-BB9B-002618943866.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/ECCC2967-A86E-E311-9305-0026189438DD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/ECFC8855-996E-E311-AF58-00304867C034.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EE068917-4E6E-E311-B4E0-00259059391E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EE522FAB-4F6E-E311-B8C3-00261894387B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EE81F8C4-606E-E311-B807-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EEBE41F9-5A6E-E311-BA83-003048FFD730.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EEF07FB2-546E-E311-B12C-0025905A48B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/EEF414B1-DA6E-E311-8F6F-003048679180.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F0A38A8A-5D6E-E311-B098-002618943842.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F236A7ED-E86E-E311-BB17-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F47733BD-5E6E-E311-856E-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F49E31B1-2B6F-E311-9D39-002618FDA207.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F4C228C6-C270-E311-B279-0025905A48EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F80A65DF-506E-E311-84AA-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F84AB260-5B6E-E311-BD93-0025905A60F4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/F8FF710D-586E-E311-BFE9-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FA0A49AD-976E-E311-913C-0026189438A5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FC0BE71E-8E6F-E311-80E6-002618943934.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FC725694-486E-E311-A4E0-00261894387E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FE4250F5-4C6F-E311-89A6-002618943920.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx25_POSTLS162_V2-v1/20000/FEDFFE23-E16F-E311-8969-003048FFD730.root',






    ),
    inputCommands = cms.untracked.vstring(
        'keep *'
    )
)

# customise the HLT menu for running on MC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC
process = customizeHLTforMC(process)

# add release-specific customizations
#from HLTrigger.Configuration.customizeHLTforCMSSW import customiseHLTforCMSSW
#process = customiseHLTforCMSSW(process,menuType="GRun",fastSim=False)

# load 2015 Run-2 L1 Menu for 25ns (default for GRun, PIon)
from L1Trigger.Configuration.customise_overwriteL1Menu import L1Menu_Collisions2015_25ns_v2 as loadL1menu
process = loadL1menu(process)


# CMSSW version specific customizations
import os
cmsswVersion = os.environ['CMSSW_VERSION']

# none for now

# load PostLS1 customisation
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1
process = customisePostLS1(process)

# adapt HLT modules to the correct process name
if 'hltTrigReport' in process.__dict__:
    process.hltTrigReport.HLTriggerResults                    = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressCosmicsOutputSmart' in process.__dict__:
    process.hltPreExpressCosmicsOutputSmart.hltResults = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreExpressOutputSmart' in process.__dict__:
    process.hltPreExpressOutputSmart.hltResults        = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForHIOutputSmart' in process.__dict__:
    process.hltPreDQMForHIOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreDQMForPPOutputSmart' in process.__dict__:
    process.hltPreDQMForPPOutputSmart.hltResults       = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMResultsOutputSmart' in process.__dict__:
    process.hltPreHLTDQMResultsOutputSmart.hltResults  = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTDQMOutputSmart' in process.__dict__:
    process.hltPreHLTDQMOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltPreHLTMONOutputSmart' in process.__dict__:
    process.hltPreHLTMONOutputSmart.hltResults         = cms.InputTag( 'TriggerResults', '', 'TEST' )

if 'hltDQMHLTScalers' in process.__dict__:
    process.hltDQMHLTScalers.triggerResults                   = cms.InputTag( 'TriggerResults', '', 'TEST' )
    process.hltDQMHLTScalers.processname                      = 'TEST'

if 'hltDQML1SeedLogicScalers' in process.__dict__:
    process.hltDQML1SeedLogicScalers.processname              = 'TEST'

#this is a standalone module to save the output from cmsRun hlt_tracklessDoubleElectron.py into a .root file
#This .root file can then be analyzed by the trigger optimization script
#process.hltOutputFULL = cms.OutputModule( "PoolOutputModule",
#	#fileName = cms.untracked.string("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_sample_with_HLT_objects.root"),
#	#fileName = cms.untracked.string("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_sample_with_HLT_objects_no_filter_refs.root"),
#	fileName = cms.untracked.string("signal_1.root"),
#	fastCloning = cms.untracked.bool( False ),
#    dataset = cms.untracked.PSet(
#        dataTier = cms.untracked.string( 'RECO' ),
#        filterName = cms.untracked.string( '' )
#    ),
#    #Drop l1extra* collections 
#	outputCommands = cms.untracked.vstring( 'keep *' ) + cms.untracked.vstring('drop CrossingFrame*_*_*_*')  + cms.untracked.vstring('drop *_*Digis*_*_*')  + cms.untracked.vstring('drop TrackingRecHits*_*_*_*')  + cms.untracked.vstring('drop *Sorted_*_*_*')  + cms.untracked.vstring('drop recoTrack*_hltIter*_*_*') + cms.untracked.vstring('drop l1extra*_*_*_*') + cms.untracked.vstring('drop floatedmValueMap_hlt*_*_*')  + cms.untracked.vstring('drop SiPixel*_*_*_*')  + cms.untracked.vstring('drop SiStrip*_*_*_*')  + cms.untracked.vstring('drop *DetIdstdset*_*_*_*')  + cms.untracked.vstring('drop TrajectorySeeds_*_*_*')  + cms.untracked.vstring('drop TrackCandidates_*_*_*')  + cms.untracked.vstring('drop recoPFRecHits_*_*_*') 
#    
#	#l1extra* collections are not dropped
#	#outputCommands = cms.untracked.vstring( 'keep *' ) + cms.untracked.vstring('drop CrossingFrame*_*_*_*')  + cms.untracked.vstring('drop *_*Digis*_*_*')  + cms.untracked.vstring('drop TrackingRecHits*_*_*_*')  + cms.untracked.vstring('drop *Sorted_*_*_*')  + cms.untracked.vstring('drop recoTrack*_hltIter*_*_*') + cms.untracked.vstring('drop floatedmValueMap_hlt*_*_*')  + cms.untracked.vstring('drop SiPixel*_*_*_*')  + cms.untracked.vstring('drop SiStrip*_*_*_*')  + cms.untracked.vstring('drop *DetIdstdset*_*_*_*')  + cms.untracked.vstring('drop TrajectorySeeds_*_*_*')  + cms.untracked.vstring('drop TrackCandidates_*_*_*')  + cms.untracked.vstring('drop recoPFRecHits_*_*_*') 
#    
#	#keep all collections
#	#outputCommands = cms.untracked.vstring( 'keep *' ) 
#
#	)
#process.FULLOutput = cms.EndPath( process.hltOutputFULL )


# limit the number of events to be processed
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# enable the TrigReport and TimeReport
process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool( True )
)

# override the GlobalTag, connection string and pfnPrefix
if 'GlobalTag' in process.__dict__:
	from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag as customiseGlobalTag
	process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'MCRUN2_72_V3A',conditions='TrackerAlignmentExtendedError_2011Realistic_v1_mc,TrackerAlignmentErrorExtendedRcd,frontier://FrontierProd/CMS_CONDITIONS+MuonDTAPEObjectsExtended_v0_mc,DTAlignmentErrorExtendedRcd,frontier://FrontierProd/CMS_CONDITIONS+MuonCSCAPEObjectsExtended_v0_mc,CSCAlignmentErrorExtendedRcd,frontier://FrontierProd/CMS_CONDITIONS+EcalSamplesCorrelation_mc,EcalSamplesCorrelationRcd,frontier://FrontierProd/CMS_CONDITIONS+EcalPulseShapes_mc,EcalPulseShapesRcd,frontier://FrontierProd/CMS_CONDITIONS+EcalPulseCovariances_mc,EcalPulseCovariancesRcd,frontier://FrontierProd/CMS_CONDITIONS')
	process.GlobalTag.connect   = 'frontier://FrontierProd/CMS_CONDITIONS'
	process.GlobalTag.pfnPrefix = cms.untracked.string('frontier://FrontierProd/')
	for pset in process.GlobalTag.toGet.value():
		pset.connect = pset.connect.value().replace('frontier://FrontierProd/', 'frontier://FrontierProd/')
	# fix for multi-run processing
	process.GlobalTag.RefreshEachRun = cms.untracked.bool( False )
	process.GlobalTag.ReconnectEachRun = cms.untracked.bool( False )

# override the L1 menu from an Xml file
process.l1GtTriggerMenuXml = cms.ESProducer("L1GtTriggerMenuXmlProducer",
  TriggerMenuLuminosity = cms.string('startup'),
  DefXmlFile = cms.string('L1Menu_Collisions2015_25ns_v2_L1T_Scales_20141121_Imp0_0x1030.xml'),
  VmeXmlFile = cms.string('')
)
process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
  recordName = cms.string('L1GtTriggerMenuRcd'),
  iovIsRunNotTime = cms.bool(True),
  firstValid = cms.vuint32(1)
)
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml') 

# customize the L1 emulator to run customiseL1EmulatorFromRaw with HLT to switchToSimStage1Digis
process.load( 'Configuration.StandardSequences.RawToDigi_cff' )
process.load( 'Configuration.StandardSequences.SimL1Emulator_cff' )
import L1Trigger.Configuration.L1Trigger_custom
#

# 2015 Run2 emulator
import L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT
process = L1Trigger.L1TCalorimeter.L1TCaloStage1_customForHLT.customiseL1EmulatorFromRaw( process )

#
process = L1Trigger.Configuration.L1Trigger_custom.customiseResetPrescalesAndMasks( process )
# customize the HLT to use the emulated results
import HLTrigger.Configuration.customizeHLTforL1Emulator
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToL1Emulator( process )
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToSimStage1Digis( process )

if 'MessageLogger' in process.__dict__:
    process.MessageLogger.categories.append('TriggerSummaryProducerAOD')
    process.MessageLogger.categories.append('L1GtTrigReport')
    process.MessageLogger.categories.append('HLTrigReport')
    process.MessageLogger.categories.append('FastReport')

# load the DQMStore and DQMRootOutputModule
#process.load( "DQMServices.Core.DQMStore_cfi" )
#process.DQMStore.enableMultiThread = True
#
#process.dqmOutput = cms.OutputModule("DQMRootOutputModule",
#    fileName = cms.untracked.string("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/DQMIO_signal_test.root")
#)
#
#process.DQMOutput = cms.EndPath( process.dqmOutput )

