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
		fileName = cms.string('ABCDE_pt_bkgnd_analyzer_trees_NUM_CMSSW_7_4_0_pre9_50ns_40PU.root')
)

process.source = cms.Source( "PoolSource",
    fileNames = cms.untracked.vstring(
	   #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/007E52D7-8D6C-E311-9CB4-0025905A48FC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/0421AE41-946C-E311-8BF6-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/04A0F776-966C-E311-954D-00248C65A3EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/062CFC70-8C6C-E311-A090-003048678B14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/06A58725-056D-E311-9112-0026189438D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/08330926-9E6C-E311-B567-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/085D4327-D46C-E311-9CC7-0025905A6122.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/0892FF80-E36C-E311-B50E-0026189438E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/0EBD4F75-8C6C-E311-AAB6-00304867C034.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/120AA2ED-E36C-E311-A573-0025905A607A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/12234F2E-976C-E311-95CB-003048FF9AA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/12347C5B-956C-E311-8351-003048FFD720.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1278F111-EE6C-E311-90FF-00304867924A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/12A56094-DE6C-E311-8EB3-002618943860.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1482A6F4-906C-E311-9F5F-00248C55CC97.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1A930915-D86C-E311-BA9E-00261894398B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1AC6318F-8F6C-E311-8B8D-002618943934.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1AC72B68-BB6C-E311-84EC-003048678AFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1C22BB59-976C-E311-B6D5-0026189437F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/205E17FF-B96C-E311-9523-003048679294.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/22B60773-D36C-E311-A622-0025905A60EE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2403B89C-966C-E311-930F-003048FFCB6A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/24A10E48-E76C-E311-AD0A-003048FFCC1E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/24B25DA3-C76C-E311-A4A8-003048678B38.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/282B8F74-096F-E311-8441-002354EF3BE3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/286227AE-F86C-E311-9140-003048678F26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2879E1A2-DD6C-E311-BBDE-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2AA379B6-8D6C-E311-8326-00261894396A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2AD69418-8D6C-E311-B0BB-003048678FF8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2CAF2C80-E96C-E311-9AEA-002590596498.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2CB11200-E16C-E311-B60B-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2E091AE9-966C-E311-BA23-0025905A6076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2E26C258-DF6C-E311-9BD7-00261894382A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2E39455B-8D6C-E311-B9C1-003048679188.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2ECA3CF0-0A6D-E311-89F4-0025905A6092.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/301303D2-8B6C-E311-A4D2-0025905A60E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/32A2ED25-996C-E311-9195-003048678B18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/32B989D3-8D6C-E311-BD70-0025905A48FC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/32DC9DD3-E76C-E311-A221-00261894398C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/32DCDEF0-D46C-E311-83E3-0025905A612C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/32EE62AF-076D-E311-9921-003048FFD728.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/341488F2-536D-E311-87CC-0025905A48F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/344DA2ED-8D6C-E311-BFD4-0025905A60BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/363EDD91-8E6C-E311-BB54-003048678AE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/36E45942-936C-E311-BE1A-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3841DB1B-936C-E311-B1C5-0026189438CF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/38BC972C-FA6C-E311-B481-002618FDA262.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3A25E543-946C-E311-9438-0026189438DC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3AC6237C-906C-E311-A0AD-00261894396E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3CBA8145-EB6C-E311-998B-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3CD7CDFA-906C-E311-B69B-002618943864.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3E35290E-EA6C-E311-8993-0025905A48E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/401DF9CD-D46C-E311-9632-003048D15D22.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4035F22C-FB6C-E311-8F9A-003048FF86CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4056C37F-FC6C-E311-9B13-003048678E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/40E76B0F-8E6C-E311-A3BD-00259059391E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/40EF64BC-CB6C-E311-805A-0025905A6092.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/428723A0-116D-E311-831D-003048679182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/42A168AB-066D-E311-B623-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/449BD4CF-8E6C-E311-9610-0025905964C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/46155F92-DE6C-E311-9B76-002618943921.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/46F42A2D-8F6C-E311-8F25-002618943958.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4AC98C1F-8F6C-E311-96DF-0025905A611E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4AD80190-CC6C-E311-85A1-00248C0BE018.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4C97595F-B76C-E311-B3A9-003048678B94.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4CCC5127-956C-E311-92D6-00304867BFF2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4CF7BC5B-E86C-E311-B111-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4EA998E1-F56C-E311-995C-003048FFD79C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/50452B7B-956C-E311-8B01-002618943894.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5216C1CB-0D6D-E311-9444-003048679266.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/521761D8-8D6C-E311-86BB-0025905A60CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/52AF021D-8D6C-E311-8012-00261894388D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/52E23045-8B6C-E311-AABA-00261894389F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5484A1CD-986C-E311-8C02-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/54C891AC-0C6D-E311-9B99-0025905A6076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/54C91A31-716D-E311-9469-0025905A6076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5621624F-076D-E311-BA84-0025905A612C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5645411F-D06C-E311-8DB0-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5680000D-F26C-E311-B02B-002618943918.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/58899FB0-EF6C-E311-8BF5-002618943908.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5A66BDF9-906C-E311-AC6B-00261894386E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5A8F07B0-8F6C-E311-A7F1-0025905A60B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5ED57A2A-8F6C-E311-9A06-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/60738FCF-DA6C-E311-B0A5-0026189438F4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/620C3843-926C-E311-9E7F-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/62146B28-956C-E311-8963-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/62848352-976C-E311-A728-00304867918E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/641CB749-E66C-E311-B4B6-0026189438B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/649FAB37-A96C-E311-9005-0026189438FD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/66B70CED-EB6C-E311-BBBE-002618943868.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/66D609C5-986C-E311-857D-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/66FE9B61-9C6C-E311-B8A8-003048679296.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/688C002C-8D6C-E311-A433-0026189438B9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/68C9725D-936C-E311-8A74-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6A668E9B-8B6C-E311-85A8-003048678B84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6C64F040-986C-E311-B24B-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6C7FDEFA-D96C-E311-AAB1-0026189438EF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6CE7CD6E-9B6C-E311-9DAE-0026189438F7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6E1B3950-8C6C-E311-AF07-0025905A60B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7001B599-8E6C-E311-A559-003048678FAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/726E7693-BE6C-E311-9583-0026189438A5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/741E7C32-036D-E311-862F-001BFCDBD130.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/745BEC46-926C-E311-AD5B-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7811D51B-936C-E311-822E-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7A93E5AC-8B6C-E311-9E46-0026189438CE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7AA1C4D3-036D-E311-9532-00304867926C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7C41042F-956C-E311-B34C-002618FDA237.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7C512E21-8C6C-E311-A48A-00261894397A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7C5F7A5C-8D6C-E311-B5CF-002618943876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7E452D29-996C-E311-9D53-00304867BED8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7E86005D-8D6C-E311-86BF-003048D15E14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7ED62991-FD6C-E311-8D58-00248C0BE016.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/80033920-FE6C-E311-A789-002618943930.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8078D147-926C-E311-BCDC-0026189438DF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/807F22F6-306D-E311-8ED2-0025905A6088.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/808DBC17-906C-E311-B72C-003048D15D22.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/82A89D2D-956C-E311-8C71-00261894386E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/840E10C4-F16C-E311-8F9F-003048678FE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/84875D82-E56C-E311-BE3F-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/863B232B-996C-E311-BF56-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/866036C6-016D-E311-90E2-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8663E62A-9A6C-E311-8B34-0025905A60B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/86F33E68-8D6C-E311-A019-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/88A741CF-F96C-E311-BC7E-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/88ADDBE2-916C-E311-9FBC-00248C55CC3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8E19A411-8D6C-E311-A8C5-0026189438FD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8E5896B2-8D6C-E311-A31C-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8E5D8714-D66C-E311-8504-0025905964C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/92695D84-8F6C-E311-B058-003048679070.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/94299396-946C-E311-BE03-003048D3FC94.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/946079B5-8F6C-E311-8094-0025905A60DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/94BB2179-966C-E311-9B8E-003048679180.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9849DF39-A46C-E311-91C0-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9853DB71-FC6C-E311-BA00-0025905964A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/98C13546-FB6C-E311-A509-003048678FB4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/98E5845A-8D6C-E311-9828-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/98EFF47D-906C-E311-A945-002618943864.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9A7330D9-226D-E311-A6A2-00261894394D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9AC30F6A-1C6D-E311-962B-002618943880.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9AF803BE-B86C-E311-B348-002618943961.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9C09C93E-926C-E311-AE27-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9CEC4A97-8E6C-E311-8BAF-002618943977.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A01D64C7-646D-E311-BB76-002618943834.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A039BD8C-8F6C-E311-AA47-002618943904.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A0EB709A-F36C-E311-AA2D-00304867BFAA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A25EEF96-DB6C-E311-9C33-00261894389E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A4D25414-8D6C-E311-ABFA-0026189438BD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A4D476A0-966C-E311-A211-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A607111E-906C-E311-BE1C-0025905938D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A67CA02E-8F6C-E311-A7E2-002354EF3BE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A69CB350-FD6C-E311-8F8B-002590593872.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A89321F7-D16C-E311-81EF-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/AA0DADDE-976C-E311-963B-0026189438B0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/AA779255-086D-E311-8E5A-00248C55CC7F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/ACAF69C5-966C-E311-9661-0025905A60A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/ACC9040F-F76C-E311-AC44-0025905A612E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/ACD01809-F16C-E311-867F-0025905A60B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/AE2B45DA-186D-E311-980F-00261894398A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B4185EEA-936C-E311-A9A4-0025905A60B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B472FF56-EA6C-E311-B63A-00261894390E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B65E7069-E26C-E311-B3B4-0025905964C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B6D7201D-D36C-E311-A356-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B84442F4-F26C-E311-B3A8-0030486792B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B881D798-8B6C-E311-8ECF-00261894383F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B8B2981C-936C-E311-8FA4-00261894391C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BA06E916-016D-E311-8B95-003048679012.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BAD68C78-956C-E311-B316-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BC0303FB-906C-E311-A59A-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BC88ACD9-976C-E311-BB72-003048678FE0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BE04F889-5E6D-E311-9BDA-003048678FAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C0145DB4-C26C-E311-A3D8-0026189438FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C020047A-956C-E311-BCF0-0026189438E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C02CD113-E16C-E311-895D-0025905A606A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C0A3E69C-8E6D-E311-8D9E-0025905A6122.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C4BB0D22-906C-E311-BB31-003048679266.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C64D2D2E-8F6C-E311-B298-00304867BFBC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C6F42C42-986C-E311-8888-002618943845.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C8F39CDD-9A6C-E311-9737-002618943945.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CC1B46FD-966C-E311-91EA-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CCD866D2-DE6C-E311-B772-002618943923.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CE2A9E6B-046E-E311-B65C-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D0019B4E-936C-E311-9E17-0025905A60B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D0A34BFD-966C-E311-B46A-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D0E37164-0F6D-E311-90DD-0025905A6066.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D287CFC0-DC6C-E311-8C11-0025905A608E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D2B898AA-8F6C-E311-93F8-0025905A48D0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D2FDA04C-916C-E311-A175-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D420AC75-F16C-E311-AAE8-00261894387C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D4B37C98-CF6C-E311-90B4-0025905A48E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D4C2B449-136D-E311-8591-002618FDA279.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D640DC32-EC6C-E311-AE4C-0026189438D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D81C28DE-1A6E-E311-9DFA-0025905A612C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D84E600D-8D6C-E311-B5B4-002618943953.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DA717C5C-ED6C-E311-A7A3-0025905A6094.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DC40BEE2-9A6C-E311-82E6-002618943852.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DCA63FDB-8D6C-E311-9FA5-003048FFCB6A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DCB19294-8A6C-E311-9E50-003048679228.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DE4D734B-916C-E311-BE53-00248C55CC3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DE556143-F86C-E311-A781-0025905964A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DE8F2FF3-FE6C-E311-8D4A-003048679266.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DEAF9451-946C-E311-8579-0025905964BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E008D719-106D-E311-9FB5-003048678B5E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E099E78F-AD6C-E311-A2BC-003048678FDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E431D94A-E16D-E311-BBD1-0030486792B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E48F5D59-976C-E311-8994-0026189438D3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E697020A-8D6C-E311-BF48-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E821D15F-F56C-E311-A669-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E8BBF7DF-916C-E311-8B87-0030486791DC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E8F91BF9-C56C-E311-80E4-0026189438A7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/EAD4769A-CE6C-E311-AE1E-003048FFD720.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/EC7B7E02-D96C-E311-B90F-0026189438EA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/EE46D87F-8F6C-E311-A95A-0026189438E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/EECD5CA4-A56C-E311-95FA-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F01A8CA5-FD6C-E311-8F7E-0026189438BF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F05FCA0B-8D6C-E311-9FE2-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F0F25596-8E6C-E311-884A-002618943904.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F28AD367-A06C-E311-A3B9-002618943876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F600700F-8D6C-E311-91F3-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F6752E59-976C-E311-A2AC-00248C65A3EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F67BF376-956C-E311-A02D-002618943900.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F6D5A78F-096D-E311-A23B-002618943868.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F812FB9B-8E6C-E311-830A-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F82C5E1B-8D6C-E311-8B66-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F8881F77-8C6C-E311-981F-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F89CACFA-C16C-E311-AFAE-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FA41EAD7-C86C-E311-8000-002618943900.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FA49EA80-F46C-E311-81E6-0026189438B5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FA720C8C-8F6C-E311-8799-00304867924E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FC4CA6F6-D66C-E311-8217-0026189438EF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FC86B33E-CA6C-E311-932C-002618943919.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FCD9041E-8D6C-E311-8513-002618943954.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FE658894-C36C-E311-9B57-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/003820AE-F76C-E311-865E-002618943836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0080E717-706C-E311-8523-00261894383F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/009978FF-656C-E311-8077-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/022E842D-5E6C-E311-A26E-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/02626A46-DA6C-E311-9948-00248C0BE014.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0433D0E1-656C-E311-865F-003048678FB4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0435EF39-056D-E311-A25E-0025905A4964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0635FE60-5F6C-E311-AA52-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0A4FD89D-AC6C-E311-8E03-003048679294.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0CFFD524-5D6C-E311-95B0-0026189437EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0E3A0DE3-6B6C-E311-B82A-0026189438A9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0EB27FA4-6A6C-E311-9F86-003048678E8A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0EBA7BE0-666C-E311-92C2-0026189438DE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0ED8A33D-696C-E311-97FB-003048679006.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0EF1371C-6A6C-E311-A90E-003048678F9C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/10576605-6D6C-E311-9722-0025905A48D8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/10B72815-B26D-E311-9ACD-0026189438B1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/127DF042-806E-E311-A59A-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/163A9F68-D36C-E311-B8DA-002618943829.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18027331-F96C-E311-8868-00261894394B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18134F02-646C-E311-ADCC-0025905A60CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18516D4B-6E6C-E311-A626-003048678BF4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/185E7FE4-CE6C-E311-BA2E-0025905A608E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18EC0E8A-6B6C-E311-B680-0026189438D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18F65BE7-6B6C-E311-9FD0-003048678B18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1A61A8EE-C36C-E311-878A-002618943920.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1C2B2368-5E6C-E311-B551-00304867908C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1EED1E17-6D6C-E311-BEAE-002618943821.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1EF67DDB-636C-E311-96C0-003048678FF8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/206DD5CE-636C-E311-A659-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/22494A48-6A6C-E311-A75E-002618943810.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/22E8BCB7-616C-E311-98CE-002590593872.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/247A3EE8-0B6D-E311-B4ED-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/260EFD2D-6D6C-E311-BF49-0026189437FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/26C6C14A-BF6C-E311-875E-0025905964B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/26F8468C-6C6C-E311-A7A7-002618943811.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/28ED142A-136D-E311-80D9-00248C55CC97.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2A3A41AF-A96C-E311-8C49-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2C136554-B56C-E311-8324-002618943870.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2C793AFD-626C-E311-BFBC-0025905A608E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2C84A5C6-696C-E311-A0C7-0026189438AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2E0B13B9-6C6C-E311-B864-003048678E92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2E6B0F21-5D6C-E311-BBC8-003048678FAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2EF0CD31-6D6C-E311-B20B-0026189438A9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3079F9A1-5F6C-E311-A040-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/30BD880D-E96C-E311-934B-003048678B92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/30E477DC-EA6C-E311-B0B0-003048FFCBA4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/30ED59CA-6C6C-E311-B976-0025905A60F4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3261BA0D-626C-E311-9107-003048D15E14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/326CC7CB-636C-E311-9561-0026189438EA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/32BDB84B-EC6C-E311-992C-002354EF3BE1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/32FBFA32-626C-E311-8BFF-00261894389A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/341194C4-A66C-E311-AF48-0025905A60B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/342665E2-7F6C-E311-AA29-0026189438F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3438FFD5-166D-E311-8D04-00261894394A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/34974D18-E66C-E311-9183-003048678BF4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/34E6DA15-076D-E311-AD10-002590593920.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/386914CB-036E-E311-8B78-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3A17E4E5-E16D-E311-BB34-002618943831.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3A93F80E-6B6C-E311-B2CD-0026189438CE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3A9D9F07-B76C-E311-BD42-002618943916.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3E023B8D-EB6C-E311-972A-0030486792A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3E164138-686C-E311-AA5B-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/40505EDE-DB6C-E311-BD5B-00261894391C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/40C70F10-696C-E311-9CEE-002618943904.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/420D8158-6C6C-E311-92A6-002618943974.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/42F6EA93-BA6C-E311-A33D-0025905964B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/449014EF-EE6C-E311-BB24-00248C65A3EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/44A00D18-6D6C-E311-B5C4-0026189438F3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/44BFD281-6F6C-E311-8165-0026189438D9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/44D434F8-CC6C-E311-8BDC-0026189438F6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4600AA82-6D6C-E311-9F4A-0025905A6122.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/46A1BFB0-D86C-E311-8BC4-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/46F3E8CE-CB6C-E311-8214-0026189438B3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4841ED29-D16C-E311-A146-0026189438CE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4866EEF4-626C-E311-8C71-0025905A60AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4A0CE144-C86C-E311-8DDD-003048678B92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4C522F04-BE6C-E311-8210-002618943896.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4C59596F-AE6C-E311-AE99-0025905A60BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4CE4B025-5C6C-E311-97DE-00304867C1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4E3189F8-FC6C-E311-810F-002618943977.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5044200A-686C-E311-BEBE-002618943959.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/52D0CC24-A96C-E311-A128-0025905A60EE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/54483774-CF6C-E311-8528-002590596490.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/54D6C6DF-F46D-E311-9135-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/56129CC1-C96C-E311-8349-003048678A78.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/563D6425-446E-E311-8989-002618FDA216.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5676182B-DF6C-E311-AFDF-00261894397B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/56AA92C6-C26C-E311-9A05-002618943980.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/56B43235-696C-E311-849D-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/56C33F46-226D-E311-906A-0025905964C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/58A1ED91-626C-E311-8217-0025905A48FC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5A1CF3DB-5E6C-E311-AFE2-0030486791DC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5A6735E8-B06C-E311-9804-0025905A60E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5C61A9F0-8D6C-E311-9B64-00261894389F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5C6F8E60-D56C-E311-B187-003048678BEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5C900B9C-656C-E311-81D7-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5C93BDC3-EC6C-E311-A127-003048678BC6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5CBEA47A-F16C-E311-BFB7-00304867BFBC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5CCE1142-5D6C-E311-8F0F-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5E694AD6-666C-E311-88EC-00261894385D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/603655F3-0A6D-E311-A12A-0026189438DF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/60E27A1A-B26D-E311-9572-003048678ADA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/66515BFF-646C-E311-8DEC-002618943905.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6862200A-F56C-E311-B668-0025905964B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6CC8E595-6C6C-E311-9ACA-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6CCC4C6E-E76C-E311-B08C-0025905938D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6E243F7A-6C6C-E311-AE6D-0025905A497A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6E8239E4-686C-E311-BE8E-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7097A784-706C-E311-B6D8-00261894384A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/70A846E4-E66D-E311-9C13-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/70DD66AE-966C-E311-94EC-002618943932.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/70FB4CE8-626C-E311-8946-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/72B455AA-0E6D-E311-9DB3-003048FFD7D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/74268897-676C-E311-8A69-0025905A60BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/74A38D17-656C-E311-9EAA-0025905A60E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/769B759A-5F6C-E311-B33F-00261894397F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/76FDC772-E16C-E311-B3CF-003048FFD7A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/784AE5DC-6F6C-E311-93B4-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/785159E0-6E6C-E311-9508-00261894389A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7A4D1008-656C-E311-B505-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7AFE2BBF-686C-E311-A176-0025905A6122.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7E2DB2A3-936C-E311-98F7-002618FDA250.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7E98EA66-5F6C-E311-8E12-0025905A60B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7E9CF9C5-606C-E311-9625-00261894387C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/80032E81-026D-E311-B2E5-0025905A6122.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/820DCA99-F66C-E311-B832-00304867920C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/842C1604-CA6C-E311-AF64-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/847D7611-E36C-E311-A60F-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/84E0AC89-6D6C-E311-9F30-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/86020643-E16C-E311-ADD8-002618943810.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8614B015-6C6C-E311-BC11-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/867DE8B2-F06C-E311-8C47-00259059642E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8C7A6563-6B6C-E311-ABBD-0025905A60CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8CC9B4B1-FA6D-E311-B27B-003048FFD754.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8CFE9C1F-D06C-E311-A782-00304867920C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8E1C0E4E-CA6C-E311-94F2-00261894397E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/90697A7D-C56D-E311-817C-00261894389F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9241CE08-686C-E311-8DB5-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/92C1B7EF-B26C-E311-B2B4-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9425EDB7-6D6C-E311-8DCA-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/942BAC3D-646C-E311-966F-002618943911.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9446AE07-5F6C-E311-952D-003048FFCC2C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/94D65A2C-676C-E311-BB4F-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/96D5F6FC-5D6C-E311-9A37-00261894382A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9816C0B6-CE6C-E311-9AB0-002354EF3BDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9824063B-FB6C-E311-AF8E-002618943922.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/986BEC11-6B6C-E311-90DD-00304867926C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/987ED7F8-D56C-E311-A443-002618943880.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/98A75C06-DE6C-E311-86AF-003048FFD7A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9A4E8806-C36C-E311-B612-002618943870.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9A6840F5-CA6C-E311-8C20-0026189438EA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9C58D1C6-626C-E311-9DC7-002618943932.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9C5D100F-C76C-E311-90B0-002354EF3BE1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9CAA8C46-676C-E311-9182-0025905964B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9CBA4A53-6E6C-E311-BAB7-002618943949.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9E42C949-656C-E311-9F7F-00261894397A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9EF565B5-6D6C-E311-B90B-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A023D779-BC6C-E311-B4E9-00261894397B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A0CC34DA-3E6F-E311-A200-0025905A60A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A244AE74-6D6C-E311-863B-0026189438A9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A458A29A-6A6C-E311-9D0F-002618943984.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A6739A54-B36D-E311-B3E8-002354EF3BDC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A67A7C26-FE6C-E311-8BC4-00304867BF18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A68CAFDA-D76C-E311-8ECC-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A6B1D888-EA6C-E311-B6A7-002618943946.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A6EB466C-646C-E311-A38F-003048679182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A81E9483-6B6C-E311-B5AB-002618943984.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A8D74B4C-5F6C-E311-B699-00261894394B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ACCC5EAF-6D6C-E311-8B9E-002354EF3BDD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ACDFC68E-FE6C-E311-A7B9-0025905A60B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B06FDCC7-5D6C-E311-BEFC-0025905938D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B08A534C-656C-E311-AB3A-00248C0BE005.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B2E3439C-836C-E311-9FF0-0026189438F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B44905A6-266E-E311-9A0F-002618943904.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B4683A18-ED6D-E311-A865-003048678FE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B468AC8D-6B6C-E311-A97E-002618FDA259.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B6BD03CF-626C-E311-9F2F-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B6DE4421-5E6C-E311-AC87-0025905A610A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B6FF86A0-026D-E311-8140-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B87770B1-516D-E311-89D7-00248C55CC9D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B878C980-606C-E311-8A68-0026189438F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B8803DCD-BA6C-E311-AE07-0025905A6068.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BC02A4C1-C06C-E311-A93F-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BE17781D-616C-E311-BBF0-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BEE28B12-6A6C-E311-9C2C-002618943934.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C031E7EC-606C-E311-9FEF-0025905A610A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C03EE8E4-6E6C-E311-BC6B-0026189437EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C0C7F95A-BD6C-E311-825A-0026189438A9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C0E2DBBC-C26C-E311-BECF-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C2814273-646C-E311-BEEF-002590593876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C2C7AF50-6F6C-E311-8E99-0025905A48D0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C418F291-D36D-E311-9FFF-0025905A6094.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C427B5A7-0F6D-E311-A7E2-0025905A60BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C6597E04-6B6C-E311-824D-00248C0BE014.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C6A64C13-736C-E311-9C28-0025905A6126.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C827510B-C66C-E311-94F6-003048678B86.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C890EE31-AD6C-E311-BD2C-003048FFD71A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C8DE8847-D26C-E311-958F-003048678B5E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C8F7D595-5F6C-E311-BEAC-002618943984.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CA37C2D7-626C-E311-9FA1-0025905A606A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CA570F58-7A6C-E311-8E30-00261894391B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CEE695BC-606C-E311-A805-00261894398B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D01B4B69-086D-E311-9278-002618943858.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D41B7B41-F26C-E311-A1C0-00261894387A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D485FD60-FF6C-E311-91A6-00248C0BE014.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D4EF8BBE-6D6C-E311-BF74-00304867D838.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D632DB50-6A6C-E311-A5E3-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D65C2F36-D46C-E311-90E4-002618943900.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D66A1239-726C-E311-B09A-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D66CACBB-5D6C-E311-89CA-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D6CACB5E-A66C-E311-9B93-0025905A48D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D6F3ABBE-766F-E311-AB7B-0025905A60A6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D880747F-BB6C-E311-BCE1-00261894397B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D8A18608-696C-E311-A38E-0025905A60E4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D8C25DF6-F56C-E311-9246-003048D42D92.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D8C367E5-656C-E311-92F9-00248C0BE005.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DA40E446-F46C-E311-8345-002618943898.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DACE37A7-DA6C-E311-A352-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DC135A8C-646C-E311-88B6-002618943821.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DE18F69D-5F6C-E311-853D-0026189438D3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DE39C96D-C36C-E311-AD43-0025905A612C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DE89B999-BB6C-E311-BDB6-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E00BB3C3-5F6C-E311-96A6-0025905964BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E01A7354-B46C-E311-BD11-002618943983.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E426FBAE-626C-E311-A356-00248C55CC7F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E4884368-A46C-E311-8514-0026189437ED.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E49014A2-6E6C-E311-A55E-00261894398D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E4DD2799-F36C-E311-896A-003048678A6C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E63FD687-666C-E311-8E49-003048679006.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E6FD6308-636C-E311-82AA-003048678DD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E80600F4-666C-E311-8EB5-002590593872.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E84360D0-C46C-E311-9FC4-0026189438E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EABCBAF3-B76C-E311-8D73-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EC2F6D0D-7C6C-E311-B02A-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EC99E38A-AA6C-E311-A80D-0026189438DB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ECC6D569-B16C-E311-9269-003048FFD71A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ECD9EE56-106D-E311-AED7-0025905A6110.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ECEA9D8E-E66C-E311-BB9C-00261894386A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ECF88F94-636C-E311-9816-003048FFD7A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EEF060C5-E46C-E311-B32E-0025905A60B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F058BAA1-686C-E311-A4EB-003048679236.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F093D8C8-6A6C-E311-87A1-0025905A60B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F29AEE62-BA6D-E311-9C73-0026189437EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F437B6A0-5D6C-E311-926D-00304867C1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F44C8647-D66C-E311-86F1-002590596484.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F4886834-6C6C-E311-9ABB-0026189438F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F4B6B20F-C86C-E311-A1FF-003048678C06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F4C6C522-226E-E311-903D-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F659E701-B56D-E311-8505-0026189438DF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F68AB5D8-C66C-E311-BFEE-002618FDA279.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8759E6A-F56C-E311-A8F2-0025905A60D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8CD3637-BB6C-E311-81CF-00261894396F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8EFAFBF-A66C-E311-ABB2-003048678B0C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FA02A823-1C6D-E311-A053-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FC55658D-D76C-E311-B24B-0026189438A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-20to30_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FEE7BC61-0D6D-E311-A32F-0025905A60CA.root'









	   #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/00612F42-FC6E-E311-85D8-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/00FFB32B-976D-E311-9A08-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/020AF207-8E6D-E311-8B84-003048678FEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/023C2C48-C76E-E311-B4B4-0025905A6132.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/04B3C84C-076F-E311-A7E7-003048D3FC94.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/0606BE5C-956D-E311-AB45-00261894395F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/088ABF63-846D-E311-82DD-0026189438CF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/0A1DCC74-9A6D-E311-83EE-00261894391B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/0C50C791-4B6F-E311-A2EA-002618943926.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/120003A3-176E-E311-96EE-0025905A48EC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1216AA4C-936D-E311-BD83-003048D3C010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/12BF66DE-966D-E311-A7B6-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/148C832D-846D-E311-A14E-002618943900.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/14A33DC7-9B6D-E311-828E-003048678BAC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1603425E-F26E-E311-9922-00259059642E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/16D1AD28-956D-E311-A950-003048678ED2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/187B741A-866D-E311-86B6-00261894389D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1A786A06-F56D-E311-B719-0026189438FD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1AB97D35-A96D-E311-8075-00304867C04E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1ABF6607-8E6D-E311-A445-003048D15DDA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1CC3B79D-C86D-E311-82B6-002618943885.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1E5696B7-866D-E311-AED0-002618943858.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1E645317-A16E-E311-8263-003048D15DB6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1EBCD13A-616E-E311-8358-002618943810.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/1EFA66A7-906D-E311-90E4-003048FFD760.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/20991329-F86D-E311-BA0F-0025905A60A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/20C7C41C-B66E-E311-940A-002618943894.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/22698DCE-2E6E-E311-8FE1-00261894396B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/24EECF9C-646E-E311-B71C-0026189438ED.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/283E7D9A-426E-E311-BBD8-0026189438E2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2CAFB0EB-996D-E311-9012-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/2EBCBA05-1B6E-E311-9B25-00261894389F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3051F21E-246E-E311-ABF2-002618943985.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/30F324C3-976D-E311-935D-002618943913.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/32C71624-4B6E-E311-86F4-003048678BB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/346ECEAA-9B6D-E311-93D5-002618943901.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/34714C9E-D06E-E311-BC79-00261894385D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/36B814E8-5C6E-E311-8A7B-00261894386A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/36DA59C4-976D-E311-B068-00261894389E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/382D3A00-866D-E311-A808-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3850E4EA-C76E-E311-B494-0026189438FC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3869CC66-9C6D-E311-9723-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3880F3AE-986D-E311-A62C-0025905964A2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/38B724D7-7A6E-E311-B06E-00261894386B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/3E5C45D4-8A6D-E311-A377-003048678ADA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/421A3655-896D-E311-873E-002354EF3BE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4269FAD7-296E-E311-90BC-003048FFD740.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/487E8BDA-996D-E311-A8CA-003048679248.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4A22FC5A-DA6D-E311-A800-0025905A608E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4C413845-846D-E311-8F2F-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4C5CFCB7-D26D-E311-88A7-00304867C0EA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4CE525E0-9D6D-E311-99F9-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/4E60327D-C66E-E311-9880-00261894385A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5018E1C8-9A6D-E311-AFE4-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5084FB25-856D-E311-B4D9-002618943974.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/527B1829-856D-E311-9905-002618943940.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/52F9CEC3-8D6D-E311-87BA-002618FDA204.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5446C970-006E-E311-8E59-0026189438D3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/546DF589-FD6D-E311-8BCA-00304867915A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5872FF09-3C6F-E311-A56B-0025905A6134.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5A48C029-8F6D-E311-A58B-00304867C034.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5A5E22A3-986D-E311-BDA0-003048678B18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/5E6F65B2-A46D-E311-9E4B-0025905A60B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/621AA342-826D-E311-8F46-003048D15E2C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6235002C-946D-E311-A25B-003048678FEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/62EEAB7C-FC6D-E311-BB11-003048FFD754.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/64387EAB-9B6D-E311-BD64-00304867920C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/64C872EA-A96E-E311-809C-003048678DD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/64E30233-946D-E311-982F-0025905A6126.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6658DD50-986D-E311-9058-002618943923.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/66E06E1F-886D-E311-A506-002618943864.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/68B03A27-976D-E311-8C1F-002618943980.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6AE7F026-946D-E311-9134-00261894386D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6AF555ED-966D-E311-B6C8-003048678B5E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6C8AA37E-C16D-E311-93E7-0026189438A7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6CF1DAA6-FF6D-E311-80D0-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6CF8D3DF-996D-E311-A8DC-00261894386C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6E4C80A2-986D-E311-9196-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/6EA4D329-C96E-E311-8794-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/707E9835-FA6D-E311-842E-0025905A609E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/70BBF4E8-996D-E311-AF23-003048678BAC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/70D1782E-926D-E311-AA63-003048FFD79C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/743F78B2-7E6D-E311-9D30-0025905A613C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7449D344-276E-E311-A62E-00248C0BE005.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/76481165-876D-E311-919D-0026189438A5.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/76DD1146-7D6F-E311-9264-00259059391E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/78C13680-8A6D-E311-8F73-003048678BE8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7C4AD95B-1A6E-E311-AAAF-00304867916E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7C56D6A1-026E-E311-A64D-0026189438D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7CFE56CD-9A6D-E311-94FF-002618943982.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7EEB8A29-166E-E311-BE4C-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/7EF9EA60-8F6D-E311-968D-00261894390C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/80314C96-8C6D-E311-85CD-002618943957.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/80829300-9E6D-E311-A7A4-003048679076.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/80D22F28-946D-E311-B2A3-002618943866.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/825D1984-F36D-E311-BEAC-0025905822B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/825E17FD-8F6D-E311-9977-00261894394A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/84A388C5-9B6D-E311-B4A4-0026189438F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/84B5E61B-996D-E311-AF8E-003048FFCBB0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/882E5559-986D-E311-B3F6-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8833AC97-996D-E311-B38E-002618943908.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8CE6C6B5-7C6D-E311-820B-0026189438F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8E4FA382-9A6D-E311-92F3-002618943898.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/8EE7A11D-AF6D-E311-8063-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/90049B7F-8A6D-E311-9094-003048678BE8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/90544531-846D-E311-B5AA-003048679266.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/92437CA9-936D-E311-8693-0025905A60FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9432B125-B46E-E311-AA1D-003048FFD730.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/944F2093-426E-E311-B9E1-00261894388A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/94F647A6-8E6D-E311-8782-00248C55CC3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/96B5CAE3-5C6E-E311-8686-002618943926.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/986CC0CD-886D-E311-9B73-00261894398A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/98A756A0-996D-E311-A906-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9A7CDAF0-986D-E311-8609-0026189438B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9C074870-886D-E311-B87D-002618943896.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9C38DD81-9C6D-E311-AAE0-002618943900.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9CEFF81F-B36D-E311-AF81-0026189438E2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/9E2B7916-956D-E311-9C9B-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A03E5EA5-896D-E311-8691-002618943978.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A0AD1EBF-086E-E311-90DE-0025905A6122.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A407362D-856D-E311-AC39-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A4643B71-9D6D-E311-9B74-002618943869.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A48ACFF5-956D-E311-8C3A-002618943833.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A6DE9E42-8D6D-E311-AC25-003048FFD760.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A8B1DE92-226E-E311-8562-00248C0BE012.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/A8FCDF46-8B6E-E311-90BD-002618943831.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/AA4FB6C4-976D-E311-888E-0026189438A7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/AAD96CCD-856D-E311-ACBB-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/ACD224C9-9A6D-E311-B436-002618943901.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/ACD3FEF2-866D-E311-9E77-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B0B8F872-886D-E311-A0DB-00261894396E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B23DB0C5-0F6E-E311-8463-002590593902.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B4369CBB-976D-E311-9DC9-002354EF3BDF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B43D9812-ED6D-E311-B710-003048679012.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B457BB5A-8870-E311-848B-00304867D446.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B47B28EC-956D-E311-9B8C-003048678BE8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B47E85D9-986D-E311-9678-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B488034D-E86D-E311-BE09-003048678B0E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B4E2F423-9E6D-E311-91F9-0025905A60E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B603F9F3-9C6D-E311-91C0-0025905A48F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B68A2211-BB6D-E311-89DD-002618943970.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B81EB585-BE6D-E311-AA2C-002618943950.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B82B4CE3-996D-E311-B95A-0026189438E2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B867734A-896D-E311-81DE-0026189438D3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/B8CCEC24-856D-E311-8927-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BA95DBA7-986D-E311-BDEA-00261894397A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BC09D859-AB6D-E311-A3FF-0025905964BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BC16C6EC-716E-E311-9533-003048678C26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BC413267-846D-E311-82DA-0025905A60AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BC777165-566E-E311-953A-0025905A6056.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BCDC9978-CF6D-E311-AC80-0026189437F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/BED6927C-A46D-E311-A04B-0026189438EA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C020AF6B-BF6E-E311-A522-00261894395F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C23F2B9E-1D6E-E311-A29B-0025905A60D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C2566C08-8E6D-E311-ADB5-00261894390C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C2AB2FE6-926D-E311-A1CB-0025905822B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C60DE2EA-896D-E311-9140-00261894386B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C613B24B-CA6E-E311-A8A8-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C8238B47-0C6E-E311-865A-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C86FF39D-B56E-E311-9696-002618943951.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/C87271CF-076F-E311-A319-003048FFD71A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CA4374F9-E06D-E311-A02B-0025905A6090.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CA5668B2-A86D-E311-AD18-0025905A6090.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CAB51CD0-9A6D-E311-9DC2-002618943958.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CC8DC2A0-956D-E311-BC10-003048678B38.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/CEC4AA06-9A6E-E311-99F7-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D215A0BE-936D-E311-9CEB-0025905A607E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D26A60E8-9A6D-E311-A293-003048FF86CA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D4C6DEA4-986D-E311-BEAB-0026189438DC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D63546DD-966D-E311-A687-002618943858.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/D63E4F9B-B26D-E311-AF06-003048679244.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DA00E1FA-9B6D-E311-A8FC-0025905A6136.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DA974E16-8B6D-E311-AA30-002618943961.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DCBE3B00-866D-E311-A313-002618943948.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/DE0A768C-346E-E311-8094-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E03898C5-126E-E311-9250-002618943932.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E2811ECC-8B6D-E311-9204-0026189438E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E6820F74-1F6E-E311-A055-00261894387C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E815E905-9D6D-E311-86C0-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E8227551-8B6D-E311-862A-003048678EE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E847A6FC-986D-E311-9597-003048679248.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/E888E595-896D-E311-8171-0030486792AC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/EAE2CE4A-856D-E311-BB4B-003048678B36.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/EE37ADBC-9A6D-E311-8CA9-002354EF3BE3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F05CE334-846D-E311-AA68-0026189437F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F09A8496-896D-E311-8322-002354EF3BCE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F0A4E82C-856D-E311-8837-002618943838.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F24B2B2E-846D-E311-BAA1-00261894382A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F260992C-8F6D-E311-85D7-00261894390E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F2A0E636-846D-E311-AA7C-00304867BFB2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F2A90AF2-8C6D-E311-97D7-003048FFCBB0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F603766B-FE6D-E311-A258-002618FDA250.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F62AA806-406F-E311-93CD-0026189438E1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F6314095-966D-E311-990B-003048678F26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F8A8A37D-216E-E311-89AE-0025905A612A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/F8D674C4-9A6D-E311-8C28-002618943957.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FC8B179D-896D-E311-AB49-002618943865.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FCE39604-6D6E-E311-8193-002618943935.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FE34BB7F-D56D-E311-8EE7-003048FFCB9E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FE5F83B0-516E-E311-A0D4-002354EF3BE6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FEA513F7-E46D-E311-8EAA-0025905A608E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/00000/FEBBB3F2-8D6D-E311-8F15-0025905A48BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/007DB2D8-366D-E311-98C1-003048678B26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/027EEA9B-AB6D-E311-B3F1-002618943940.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/02B0B42F-026E-E311-AD45-003048679070.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/02EEA42F-986D-E311-9267-0026189438F9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/04659A8B-466D-E311-AD00-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/04BDBFE4-606D-E311-B823-0030486792B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/04F991BB-306D-E311-95C3-0026189438AB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/08805475-D26E-E311-883F-0025905964B2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/08AA8987-D06D-E311-8548-0026189438D2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/08B7C127-5A6D-E311-AE64-003048678B94.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0ACD3C3D-0F6F-E311-8C0E-002618943939.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0C1ABEE0-606D-E311-8642-0026189438E6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0CB91424-646D-E311-B7BA-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0CD7593D-2E6D-E311-93C8-002590596490.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0CFB35F7-226E-E311-836A-002618943973.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0E229D58-0E6E-E311-9C32-003048678FEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0E513D86-586D-E311-8F1D-0026189438CB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/0E95DDFB-3A6D-E311-9F7B-003048FFCC18.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/10BD695F-626D-E311-8F14-0026189438FC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/12130E6A-D36D-E311-84DF-0026189438C9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/12A58014-606E-E311-9A2F-0025905A607A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1406255A-716F-E311-945B-00261894390E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/140E9AFF-506D-E311-9EDF-002618943906.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/142A607F-EE6D-E311-8DB2-0026189438E6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/143036B9-386D-E311-B115-003048678B00.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/16DCEA5E-FD6D-E311-A6E7-0025905964B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18EB0BC7-366D-E311-BE76-0026189438D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/18EF4EBF-CE6D-E311-96A2-003048679010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1A17385E-366D-E311-8CA3-002618943836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1AC14299-466D-E311-897B-00261894389C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1AE881CC-D46D-E311-89D9-003048678BAC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1CCC7594-376E-E311-8795-00261894396D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1E4E1A57-1F6E-E311-83D7-0030486792A8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1E51C721-5F6D-E311-B853-002618943939.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/1EA1F682-CE6D-E311-938B-002618943911.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/22735D17-1B6E-E311-AFC4-00261894393A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/24269477-346D-E311-AAA0-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2475A3DB-4E6D-E311-8298-003048FFCC0A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/24932602-CD6D-E311-A08B-003048678FA6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/24BC0617-466D-E311-9810-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/24E461CE-CE6D-E311-BB90-003048D15E02.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/26AD45F8-326D-E311-AA74-0026189438E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/283A6F7F-2A6D-E311-B971-00261894392C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/28DC314F-AA6D-E311-AB6D-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/28E10B71-CC6D-E311-8636-00261894393E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2A2B5A68-896F-E311-9B9A-00259059642E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2A4BBC7D-D06D-E311-B647-002618943966.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2A5B2836-416E-E311-BD02-002618943894.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2A722684-616D-E311-8B50-003048678E24.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2AAD4B62-966D-E311-A045-002618943927.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2C34E2C4-416D-E311-91F0-003048678F74.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2C52303C-D56E-E311-8662-0025905A605E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2C7C1248-376D-E311-B4DF-0026189438CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2CAC638F-5A6D-E311-999D-002354EF3BE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2CBECFCC-1B6E-E311-9F4A-00261894383E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2E472B30-556D-E311-9C47-003048678E52.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2E4EB354-1E6E-E311-BB48-0026189438B9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2E638DC5-136E-E311-9A4A-00261894394F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2E693716-A06D-E311-9408-002590593878.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/2EEDD98F-556D-E311-A009-003048679150.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/303436CB-336D-E311-9D7B-00304867904E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/30623379-416D-E311-9ED3-003048678EE2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3215FA07-186E-E311-AFE4-003048D3C010.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/329E8BD9-7B6E-E311-847F-0026189438FA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/32DB1862-3D6E-E311-9412-0030486792B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/32E66661-366D-E311-955A-0026189438C4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/32F3665D-956E-E311-A97D-0025905A6132.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/344B283B-616D-E311-ACAA-0026189437F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/347E6AA8-EC6D-E311-A356-003048678E8A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/34AD8645-D26D-E311-B957-00261894394B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3637888D-436D-E311-96B9-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/364D0A29-8C6E-E311-A60C-002618943906.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/36A941A3-8170-E311-8EF3-0025905A60A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/36EAF97B-A86D-E311-A75A-003048678B06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3818AA0C-A66D-E311-9199-0025905822B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/386981CB-966D-E311-9A62-002618943832.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/387434A2-526D-E311-96F7-002618FDA208.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/388D7099-386D-E311-A570-00304867C1BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/38DA27B5-5E6D-E311-B162-0030486792B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3A3C2F06-3E6D-E311-9572-0026189438B0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3A610709-2F6D-E311-B46A-002618943956.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3C311F70-976D-E311-A6E9-002590593920.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3C375524-5C6D-E311-B44A-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3CB3ADB9-F56E-E311-BDF6-0026189438B3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3E548EDE-266D-E311-A3CC-0025905A6056.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/3EDFC03E-226D-E311-861C-0025905964BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4008BAB5-036E-E311-9E60-003048678BEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/40385E89-D96D-E311-B8E1-00261894393D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/40937F9A-426D-E311-91FB-00304867BFF2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4254350C-5D6D-E311-B3BC-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/427F14D6-296D-E311-B937-002618FDA277.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/42E1E036-276D-E311-8185-002354EF3BCE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/441CFFE0-116E-E311-882D-00248C55CC3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/447FA1AC-376D-E311-83CC-002618943970.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/44F8702B-066E-E311-89A6-003048FFD79C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/462EE66E-B16D-E311-81E9-0025905A610A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4631982B-036E-E311-8472-001BFCDBD182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/46DCF5CC-E06D-E311-851D-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/48ECBC81-F86D-E311-BEFD-00261894398C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4A0CBD18-546D-E311-9341-0026189438F3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4A162FAC-586D-E311-9B6B-003048678FEA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4AD35960-2F6E-E311-A971-0026189438AE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4ADC8C7E-D06D-E311-9319-0026189438CF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4C285B14-AB6D-E311-A109-0025905A6080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4CC6FA52-F76D-E311-A6D6-003048678B84.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/4CDB6152-4F6D-E311-A4FD-00304867D446.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/502E9269-3C6E-E311-9400-002618943809.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/505270F2-2F6D-E311-B857-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/50A32EC3-316D-E311-8CDA-0026189438BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/50DD4830-566E-E311-8EC6-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/52577233-D66D-E311-8CB8-00261894393B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5287ACD1-416D-E311-9A59-002618943829.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5299C399-466D-E311-BCAD-00304867D836.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/52E94C8B-D06D-E311-A3D7-0030486790A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/549BCD32-3B6D-E311-8BC1-0025905964CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/549CDD65-476D-E311-BDCF-0026189438AB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/54C96706-A46D-E311-8F00-002590593876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/54D872AA-D16D-E311-A756-002618943832.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/562C7A95-576D-E311-8C4A-00304867920A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5648A632-636D-E311-93A9-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/56D71368-2C6D-E311-A808-00304867BED8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/589D4293-D26D-E311-ABFE-003048678B0C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/58FCBB47-136E-E311-8A2E-0025905964B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5AA8ED69-076E-E311-BCB4-002354EF3BDB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5C8071C6-1E6F-E311-8E84-002618943869.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5CB9F099-CB6D-E311-BB28-003048679248.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5CCF9FA9-A66D-E311-AA4F-002618943894.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5E12D0D5-D76D-E311-B685-0026189438FE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5E22C9B7-566D-E311-A578-0026189437E8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/5E3187BC-9D6D-E311-AF6B-0025905A6066.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6204E2D7-556D-E311-A9F9-00261894393D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/627B2405-976D-E311-8DAF-003048678B08.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/62935661-F56D-E311-AB30-002590596486.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/62BEF967-446D-E311-9C0C-002618943985.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/64023562-316E-E311-A56F-00248C55CC40.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6414E067-DD6D-E311-B1F5-0026189438E1.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/64364D77-E96D-E311-B651-002618FDA287.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/64CF45B9-526D-E311-8669-003048FFD7C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/661D3CBF-606D-E311-86F9-003048FFCB8C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/66A00BE7-276D-E311-9F06-003048FFD770.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/66E9DA5B-D16D-E311-833B-003048678AFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/66F683C7-CD6D-E311-8706-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/687EB59B-3E6D-E311-BD13-002618FDA277.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/68D856E8-966D-E311-ACAA-003048D15DDA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6A481E86-336D-E311-96BB-0026189438BA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6AC24A4D-5C6D-E311-93BA-0026189438FD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6C09E6DF-0C6E-E311-ABB5-001BFCDBD182.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6C76ACC6-426E-E311-BD16-002618943964.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6C8AF72F-296F-E311-8D76-003048678B3C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6CE69759-276E-E311-947F-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6CEE89D3-C76D-E311-A0CA-003048678DA2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6E789953-986D-E311-9F34-003048678FF6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/6EF9D01E-E76D-E311-B87E-0025905A60BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/70341B51-656D-E311-ABC9-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7054130C-516D-E311-BD76-00261894386F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/706B340F-AC6D-E311-94BF-0026189438FF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/70EE6B2E-BE6D-E311-82D2-0025905A60C6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7229D81F-476D-E311-B98B-0026189438D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/727D67D5-D56D-E311-BFF9-002618943869.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/72A4DC87-C36D-E311-808F-0025905A48C0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/72C252A5-256E-E311-989E-00261894380B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/748F92EA-176E-E311-8579-003048678ED4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/74A5EEB9-456D-E311-9F59-00304867916E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/74F97B78-A46E-E311-A509-0026189438C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/760D0AEA-426F-E311-B46F-002618943867.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/768A5618-396D-E311-B496-0025905A609A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/76E79233-436D-E311-A665-002354EF3BD0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7858EE1A-606D-E311-B360-00304867902E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/785DF5A4-4C6D-E311-ABFF-002618943947.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/78731D13-186E-E311-8E2A-0025905A6060.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7886E4E0-AC6D-E311-8C48-0030486790A0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/78975225-026E-E311-B7C9-0025905964C2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/78AC53FA-3E6E-E311-9141-003048678B94.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/78D11199-226D-E311-B2F3-003048678B94.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7A14E85A-EF6D-E311-91A4-002618943908.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7A40AA1A-A06E-E311-B469-003048678C26.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7A752DCE-586D-E311-8C70-003048678C62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7C5C6B68-566D-E311-82C7-002618943856.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7C5F6F38-986D-E311-AE88-00304867902E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7C6C5433-476D-E311-8D00-003048FFD756.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7C74CFB0-966D-E311-A97B-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7E3B14F0-CB6D-E311-BB73-00261894390C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/7E5C729B-5B6D-E311-9A5F-0026189438D7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8019C903-CE6D-E311-BB36-002618943932.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8067C33F-956D-E311-84F0-003048679214.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/82314CC2-4F6D-E311-AE31-002618943966.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/82B4F4C2-5F6D-E311-BD21-0030486792B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/82BD82F8-D86D-E311-8DDA-0025905A611C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/846B0C4B-D46D-E311-A351-00261894396E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/848E9CBE-346E-E311-AD10-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/84B5771F-506D-E311-B644-0026189438CB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/86435B67-446D-E311-8215-002618943834.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/86DAC74A-496D-E311-ADCC-002618943898.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/881D1895-466D-E311-ABB5-003048678AC0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8A1E640E-286E-E311-B14A-001BFCDBD166.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8A6FC65D-496D-E311-BE29-00261894398A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8AB40308-A96D-E311-95DA-002354EF3BDF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8AC43785-566D-E311-927B-002618943972.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8AE2A8E0-986D-E311-ADFA-002590593876.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8C416CA7-536D-E311-8119-003048679266.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8C744DAA-D76D-E311-91C9-0025905A6094.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8E8B8A96-226D-E311-92D5-00248C55CC97.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/8EA006E2-5E6D-E311-A951-003048678B34.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/90311F9F-236D-E311-8BAC-003048678FF6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/90748009-606D-E311-A7B1-00304867929E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/90D6F94F-FA6F-E311-9001-002618943951.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/90F760FA-386D-E311-A938-00261894397B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/92448074-646D-E311-BA7D-00261894389D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9260778A-626E-E311-B742-00261894393C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9285FC26-D56E-E311-9090-0025905964CC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/92F557E6-686E-E311-A3E3-001BFCDBD1BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/943F1B99-5C6D-E311-8E79-002618943875.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9459B450-516D-E311-95F6-002618943896.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/94921B60-516D-E311-9506-00261894393F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/96069ECA-CF6D-E311-ABFA-0025905964BE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/962F320B-CD6D-E311-B29F-002618943865.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9670869F-1B6E-E311-BB1D-003048FFD71A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/987EC65E-626D-E311-911B-00261894383B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9A0628F8-546E-E311-9181-0025905A608C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9A396EAA-CF6D-E311-905D-00304867C04E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9A6867E3-5F6D-E311-9ACF-00261894391C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9A9BB9DB-CD6D-E311-B0B6-0026189438DF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9ABE35B4-AA6E-E311-A859-00261894389D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9AC28D6F-536D-E311-A984-0030486792B6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9AE513C5-3B6D-E311-BB1D-002618FDA279.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9E6772FF-5D6D-E311-9620-003048FFD756.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9E8B0FD5-D06D-E311-B9FD-003048D15E02.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/9EBE0746-206E-E311-A5E3-0026189438E0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A05F27D5-566D-E311-89B3-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A0AAAB7D-5C6D-E311-B872-002618943854.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A0B569C9-336D-E311-A989-003048678B14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A26BA4FA-E16D-E311-A106-003048FFD7D4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A2AA6F1D-2D6E-E311-87BA-003048678B06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A2EDAE42-636D-E311-B340-003048678B06.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A2F1697A-986E-E311-8D6D-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A4041570-346D-E311-B0C4-0026189438D9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A409D5C1-276D-E311-90AE-0030486790B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A4D2C3FD-336D-E311-9E68-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A85B9CAF-206E-E311-9A8A-002590596486.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/A8C61E86-3F6D-E311-B42B-0026189438B0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/AA2343E2-CD6D-E311-AD69-002618943973.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/AA6E4069-D66D-E311-A341-002618943800.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/AA8B6F27-176E-E311-83C0-002618943913.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/AC38E0B6-956D-E311-8F0E-003048678B0C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/AE74392D-386D-E311-9663-0025905A6084.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/AEACBCC7-456E-E311-BD2A-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B044969F-CD6D-E311-BE32-002618943833.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B04725C0-256D-E311-8F7B-002618943914.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B0E83F2B-A96D-E311-8C8B-0025905A6082.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B216ACAB-376D-E311-AFF7-002354EF3BDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B231D7D9-C76D-E311-8C26-0025905A6118.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B24A0C03-AB6D-E311-95FC-002354EF3BE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B24E3000-4F6D-E311-8BE0-003048679168.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B408F6E5-5A6D-E311-9877-003048678BAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B431EFA3-CF6D-E311-A5E5-0026189438CF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B64DD6F5-4F6E-E311-9B78-002618FDA216.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B67A6706-456E-E311-A5B9-003048678B12.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B67F0D8E-4F6D-E311-B84E-002354EF3BDE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B6BFCED3-4E6D-E311-8F97-0030486791F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B85A2ACF-5F6D-E311-A9DD-00261894384F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/B8CB3518-FE6D-E311-A109-0026189438B8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BA00D3E4-626D-E311-B2C1-003048679080.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BA17E646-D16D-E311-B174-002590596486.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BCBA7850-856E-E311-B5E8-00261894387A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BCCECE8D-576D-E311-99E0-003048678F62.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BE587D79-E56D-E311-A64D-00304867D838.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/BEC5DBC9-0F6E-E311-9C7C-003048FFCC1E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C00EA674-AA6D-E311-91B0-0026189437EB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C20E6CED-776E-E311-A648-002618943906.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C21ED768-966D-E311-B92F-002618943933.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C45CF483-D26D-E311-8F6E-003048678B14.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C48781EC-576D-E311-969F-0026189438CB.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C4B98260-926D-E311-95D9-00261894386E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C6FD862F-F66D-E311-812D-0025905964B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C808A5F8-F26D-E311-BBEF-00259059391E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C860C84E-2B6E-E311-AF35-003048678B86.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C8620F75-4E6D-E311-A895-003048FFCB96.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C882BB0C-D56E-E311-A012-0025905A605E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C8EF1867-346D-E311-8767-0026189438AF.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/C8F159EA-4A6D-E311-AAD5-002618943981.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CA85EE3D-536E-E311-BB90-0025905A60F8.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CAA6545A-4C6D-E311-97A7-002618FDA279.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CABA1B8C-3E6E-E311-825A-003048678BF4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CE456543-376D-E311-B48A-0026189438F9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CE75A8F1-7D6E-E311-8075-0026189438B4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CE7A9718-506D-E311-A058-003048FFCC2C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/CEDABD5B-456D-E311-8F4E-002618943975.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D007DA8E-D06D-E311-8FFE-00248C55CC97.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D01575A6-4C6D-E311-B4E7-002618943976.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D20489AF-B56E-E311-A229-002618943867.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D42EA892-0A6E-E311-9B31-00248C55CC97.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D4ACD65F-726E-E311-8C0B-003048678FFA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D6570829-536D-E311-9C41-002618943918.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D66A1C78-906E-E311-B83E-00304867C1BC.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D66C3594-4B6D-E311-BD28-00304867918A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D683F200-4C6D-E311-B77D-0025905A497A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D6C13882-4B6D-E311-8CD0-0026189438FD.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D859657A-556D-E311-A18E-002618943961.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D883C6DE-606D-E311-AEFD-0030486791F2.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D8B45766-356D-E311-B5B6-0026189438B3.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/D8D6E2BF-386D-E311-9919-003048678DD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DA0712D4-496D-E311-81AD-00261894398A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DAB46C22-626D-E311-9404-002618943898.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DCFF1E33-AC6D-E311-AC8E-00261894391B.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DE3A5EC3-406D-E311-BB3A-002618FDA28E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/DE8E4D51-606D-E311-A682-0026189438F9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E02872EE-346D-E311-B290-002618943910.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E0B64669-436D-E311-9452-0025905A608E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E23550DA-AB6D-E311-88A3-003048FFD756.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E24CFAA0-426D-E311-A68E-0025905A610C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E257DC60-D16D-E311-BDAB-002618943958.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E29C7CB2-D16D-E311-A2F9-003048678FAE.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E4697940-D26D-E311-9F36-0026189438E7.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E4BBA459-376D-E311-87FD-0025905A60D6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E6A2DED6-5A6D-E311-B76F-003048678B7C.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E6A65C38-B36D-E311-9CCE-002618943960.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E6B712F8-3A6E-E311-A243-003048679266.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E819129D-E76D-E311-8E6C-003048679228.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E858680D-4C6D-E311-A342-002618943922.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E86E5A08-356D-E311-851F-0026189438D9.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/E8F2BD79-3B6D-E311-860E-00304867903E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EAFDC286-D06D-E311-8EC1-003048679244.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EC6531CA-EB6D-E311-A3A0-002618FDA265.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/EC884DA8-146E-E311-A090-00261894388F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/ECF90F6E-AD6D-E311-9285-002618943911.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F01EBF7E-CE6D-E311-B73D-002618943927.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F22BC842-8E6D-E311-AD27-002618943866.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F4538F09-596D-E311-A59A-0030486792F0.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F60EF980-CE6D-E311-8C8C-003048678FD6.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F62D2148-486D-E311-88EA-002618943915.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F6AF6E4B-486D-E311-AD15-00261894397E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8367F89-8E6D-E311-93F4-003048678B1A.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8A05EB0-376D-E311-AEB3-00261894384F.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8B20481-636D-E311-9CD5-003048678E80.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/F8BD3CA5-476D-E311-B4F0-00261894397E.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FA3082CF-D06D-E311-9E82-0026189438AA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FAA9552F-986D-E311-B0E6-00261894389D.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FAC5FE3B-536D-E311-A70B-003048678E52.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FC6883C1-306D-E311-BEE6-002618943857.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FC8ED0A7-766E-E311-89F1-0025905A60DA.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FE3F2152-976D-E311-B7E8-003048678FE4.root',
       #'root://cms-xrd-global.cern.ch//store/mc/Fall13dr/QCD_Pt-30to80_EMEnriched_Tune4C_13TeV_pythia8/GEN-SIM-RAW/castor_tsg_PU40bx50_POSTLS162_V2-v1/20000/FEAFD4F0-576D-E311-AC31-0026189438BC.root'



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

## load 2015 Run-2 L1 Menu for 25ns (default for GRun, PIon)
#from L1Trigger.Configuration.customise_overwriteL1Menu import L1Menu_Collisions2015_25ns_v2 as loadL1menu
#process = loadL1menu(process)


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
	process.GlobalTag = customiseGlobalTag(process.GlobalTag, globaltag = 'MCRUN2_72_V4A',conditions='TrackerAlignmentExtendedError_2011Realistic_v1_mc,TrackerAlignmentErrorExtendedRcd,frontier://FrontierProd/CMS_CONDITIONS+MuonDTAPEObjectsExtended_v0_mc,DTAlignmentErrorExtendedRcd,frontier://FrontierProd/CMS_CONDITIONS+MuonCSCAPEObjectsExtended_v0_mc,CSCAlignmentErrorExtendedRcd,frontier://FrontierProd/CMS_CONDITIONS+EcalSamplesCorrelation_mc,EcalSamplesCorrelationRcd,frontier://FrontierProd/CMS_CONDITIONS+EcalPulseShapes_mc,EcalPulseShapesRcd,frontier://FrontierProd/CMS_CONDITIONS+EcalPulseCovariances_mc,EcalPulseCovariancesRcd,frontier://FrontierProd/CMS_CONDITIONS')
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
  DefXmlFile = cms.string('L1Menu_Collisions2015_50nsGct_v1_L1T_Scales_20141121_Imp0_0x1030.xml'),
  VmeXmlFile = cms.string('')
)
process.L1GtTriggerMenuRcdSource = cms.ESSource("EmptyESSource",
  recordName = cms.string('L1GtTriggerMenuRcd'),
  iovIsRunNotTime = cms.bool(True),
  firstValid = cms.vuint32(1)
)
process.es_prefer_l1GtParameters = cms.ESPrefer('L1GtTriggerMenuXmlProducer','l1GtTriggerMenuXml') 

# customize the L1 emulator to run customiseL1GtEmulatorFromRaw with HLT to switchToSimGtDigis
process.load( 'Configuration.StandardSequences.RawToDigi_cff' )
process.load( 'Configuration.StandardSequences.SimL1Emulator_cff' )
import L1Trigger.Configuration.L1Trigger_custom
#

# Run1 Emulator
process = L1Trigger.Configuration.L1Trigger_custom.customiseL1GtEmulatorFromRaw( process )

#
process = L1Trigger.Configuration.L1Trigger_custom.customiseResetPrescalesAndMasks( process )
# customize the HLT to use the emulated results
import HLTrigger.Configuration.customizeHLTforL1Emulator
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToL1Emulator( process )
process = HLTrigger.Configuration.customizeHLTforL1Emulator.switchToSimGtDigis( process )

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

