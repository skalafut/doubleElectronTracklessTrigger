// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/recoAnalyzerGeneric
// Class:      recoAnalyzerGeneric
// 
/**\class recoAnalyzerGeneric recoAnalyzerGeneric.cc doubleElectronTracklessTrigger/recoAnalyzerGeneric/plugins/recoAnalyzerGeneric.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Sean Kalafut
//         Created:  Thu, 06 Nov 2014 23:16:33 GMT
//
//


// system include files
#include <memory>
#include <map>
#include <utility>
#include <cstring>
#include <string>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <array>



// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/getRef.h"

#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateFwd.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateIsolation.h"
#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"


#include "DataFormats/EgammaReco/interface/SuperCluster.h"
//#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EgammaReco/interface/ClusterShape.h"
#include "DataFormats/EgammaReco/interface/ClusterShapeFwd.h"
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaCandidates/interface/Electron.h"
//#include "DataFormats/EgammaCandidates/interface/ElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
//#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
//#include "DataFormats/HLTReco/interface/TriggerEvent.h" // trigger::TriggerEvent
#include "DataFormats/HLTReco/interface/TriggerObject.h" 
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h" 
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h" 
#include "DataFormats/HLTReco/interface/TriggerRefsCollections.h" 
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h" 



#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"

#include "DataFormats/ParticleFlowReco/interface/PFCluster.h"
#include "DataFormats/ParticleFlowReco/interface/PFClusterFwd.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecHitFraction.h"
#include "DataFormats/ParticleFlowReco/interface/PFLayer.h"

#include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecHitFwd.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/CaloRecHit/interface/CaloRecHit.h"
#include "DataFormats/CaloRecHit/interface/CaloCluster.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TMath.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TAttFill.h"
#include "TAttMarker.h"
#include <TString.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TStyle.h>
#include <TROOT.h>
#include "TTree.h"

#define NELE 400 


//
// class declaration
//

class recoAnalyzerGeneric : public edm::EDAnalyzer {
   public:
      explicit recoAnalyzerGeneric(const edm::ParameterSet&);
      ~recoAnalyzerGeneric();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
     

void getTriggerObjectsInfo(const edm::Event& iEvent){
	if(analyzingTracked && maxDeltaR < 0){
		iEvent.getByLabel(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByLabel(HadEmTag,HadEmHandle);
		iEvent.getByLabel(HcalIsoTag,HcalIsoHandle);
		iEvent.getByLabel(EcalIsoTag,EcalIsoHandle);
		iEvent.getByLabel(TrackIsoTag,TrackIsoHandle);
		iEvent.getByLabel(DphiTag,DphiHandle);
		iEvent.getByLabel(DetaTag,DetaHandle);
		iEvent.getByLabel(EpTag,EpHandle);

		iEvent.getByLabel(hltObjectsTag, hltObjectsHandle);

		//std::cout<<"setup handles to tracked leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid()) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() || !TrackIsoHandle.isValid() || !DphiHandle.isValid() || !DetaHandle.isValid() || !EpHandle.isValid()) return;

		//std::cout<<"all tracked leg handles are valid"<<std::endl;

		for(unsigned int h=0; h<hltObjectsHandle->size(); h++){
			nHltEle += 1;
		}

		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt, TrackIsoIt, DphiIt, DetaIt, EpIt;
		unsigned int j=0;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			etaHltEle[j] = (*refIt)->eta();
			//std::cout<<"eta = "<< (*refIt)->eta() << std::endl;
			ptHltEle[j] = (*refIt)->pt();
			phiHltEle[j] = (*refIt)->phi();

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
			clusterShapeHltEle[j] = SigmaIEIEIt->val;
			HadEmIt = (*HadEmHandle).find(*refIt);
			hadEmHltEle[j] = (HadEmIt->val)/(ptHltEle[j]*(TMath::CosH(etaHltEle[j]) ));
			HcalIsoIt = (*HcalIsoHandle).find(*refIt);
			hcalIsoHltEle[j] = (HcalIsoIt->val)/ptHltEle[j];
			EcalIsoIt = (*EcalIsoHandle).find(*refIt);
			ecalIsoHltEle[j] = (EcalIsoIt->val)/ptHltEle[j];

			TrackIsoIt = (*TrackIsoHandle).find(*refIt);
			trackIsoHltEle[j] = (TrackIsoIt->val)/ptHltEle[j];
			DphiIt = (*DphiHandle).find(*refIt);
			dPhiHltEle[j] = DphiIt->val;
			DetaIt = (*DetaHandle).find(*refIt);
			dEtaHltEle[j] = DetaIt->val;
			EpIt = (*EpHandle).find(*refIt);
			epHltEle[j] = EpIt->val;
			j += 1;
		}//end loop over all entries in hltObjectsHandle

	}//end filter on tracked leg objects 
	
	if(!analyzingTracked && maxDeltaR < 0){
		iEvent.getByLabel(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByLabel(HadEmTag,HadEmHandle);
		iEvent.getByLabel(HcalIsoTag,HcalIsoHandle);
		iEvent.getByLabel(EcalIsoTag,EcalIsoHandle);
	
		iEvent.getByLabel(hltObjectsTag, hltObjectsHandle);
		
		//std::cout<<"setup handles to trackless leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid()) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() ) return;
	
		//std::cout<<"all trackless leg handles are valid"<<std::endl;

		for(unsigned int h=0; h<hltObjectsHandle->size(); h++){
			nHltEle += 1;
		}

		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt;
		unsigned int j=0;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			etaHltEle[j] = (*refIt)->eta();
			//std::cout<<"eta = "<< (*refIt)->eta() << std::endl;
			ptHltEle[j] = (*refIt)->pt();
			phiHltEle[j] = (*refIt)->phi();

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
			clusterShapeHltEle[j] = SigmaIEIEIt->val;
			HadEmIt = (*HadEmHandle).find(*refIt);
			hadEmHltEle[j] = (HadEmIt->val)/(ptHltEle[j]*(TMath::CosH(etaHltEle[j]) ));
			HcalIsoIt = (*HcalIsoHandle).find(*refIt);
			hcalIsoHltEle[j] = (HcalIsoIt->val)/ptHltEle[j];
			EcalIsoIt = (*EcalIsoHandle).find(*refIt);
			ecalIsoHltEle[j] = (EcalIsoIt->val)/ptHltEle[j];
			j += 1;
		}//end loop over all entries in hltObjectsHandle

	}//end filter on trackless leg objects 

	if(analyzingTracked && maxDeltaR > 0){
		iEvent.getByLabel(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByLabel(HadEmTag,HadEmHandle);
		iEvent.getByLabel(HcalIsoTag,HcalIsoHandle);
		iEvent.getByLabel(EcalIsoTag,EcalIsoHandle);
		iEvent.getByLabel(TrackIsoTag,TrackIsoHandle);
		iEvent.getByLabel(DphiTag,DphiHandle);
		iEvent.getByLabel(DetaTag,DetaHandle);
		iEvent.getByLabel(EpTag,EpHandle);

		iEvent.getByLabel(hltObjectsTag, hltObjectsHandle);
		iEvent.getByLabel(genObjectsTag, genObjectsHandle);

		std::cout<<"setup handles to tracked leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid() || !genObjectsHandle.isValid() || genObjectsHandle->size()==0 ) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() || !TrackIsoHandle.isValid() || !DphiHandle.isValid() || !DetaHandle.isValid() || !EpHandle.isValid()) return;

		std::cout<<"all tracked leg handles are valid"<<std::endl;

		edm::OwnVector<reco::Candidate>::const_iterator genIt = genObjectsHandle->begin();
		etaGenEle = genIt->eta();
		ptGenEle = genIt->pt();
		phiGenEle = genIt->phi();
		std::cout<<"obtained eta, pt, phi of tracked gen electron"<<std::endl;
		
		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt, TrackIsoIt, DphiIt, DetaIt, EpIt;
		unsigned int j=0;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			Float_t hltEta = (*refIt)->eta();
			Float_t hltPhi = (*refIt)->phi();
			
			if(deltaR(hltEta, hltPhi, etaGenEle, phiGenEle) <= maxDeltaR){
				etaHltEle[j] = (*refIt)->eta();
				ptHltEle[j] = (*refIt)->pt();
				phiHltEle[j] = (*refIt)->phi();

				//initialize const_iterators to maps inside for loop using find(edm::Ref)
				SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
				clusterShapeHltEle[j] = SigmaIEIEIt->val;
				HadEmIt = (*HadEmHandle).find(*refIt);
				hadEmHltEle[j] = (HadEmIt->val)/(ptHltEle[j]*(TMath::CosH(etaHltEle[j]) ));
				HcalIsoIt = (*HcalIsoHandle).find(*refIt);
				hcalIsoHltEle[j] = (HcalIsoIt->val)/ptHltEle[j];
				EcalIsoIt = (*EcalIsoHandle).find(*refIt);
				ecalIsoHltEle[j] = (EcalIsoIt->val)/ptHltEle[j];

				TrackIsoIt = (*TrackIsoHandle).find(*refIt);
				trackIsoHltEle[j] = (TrackIsoIt->val)/ptHltEle[j];
				DphiIt = (*DphiHandle).find(*refIt);
				dPhiHltEle[j] = DphiIt->val;
				DetaIt = (*DetaHandle).find(*refIt);
				dEtaHltEle[j] = DetaIt->val;
				EpIt = (*EpHandle).find(*refIt);
				epHltEle[j] = EpIt->val;
				j += 1;
				nHltEle += 1;

			}//end deltaR filter
			if(j==1) break;//leave loop over hltObjectsHandle once a match has been found
		
		}//end loop over all entries in hltObjectsHandle

	}//end filter on tracked leg objects which should be matched to one GEN tracked electron 
	
	if(!analyzingTracked && maxDeltaR > 0){
		iEvent.getByLabel(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByLabel(HadEmTag,HadEmHandle);
		iEvent.getByLabel(HcalIsoTag,HcalIsoHandle);
		iEvent.getByLabel(EcalIsoTag,EcalIsoHandle);
	
		iEvent.getByLabel(hltObjectsTag, hltObjectsHandle);
		iEvent.getByLabel(genObjectsTag, genObjectsHandle);


		std::cout<<"setup handles to trackless leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid() || !genObjectsHandle.isValid() || genObjectsHandle->size()==0 ) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() ) return;
	
		std::cout<<"all trackless leg handles are valid"<<std::endl;

		edm::OwnVector<reco::Candidate>::const_iterator genIt = genObjectsHandle->begin();
		etaGenEle = genIt->eta();
		ptGenEle = genIt->pt();
		phiGenEle = genIt->phi();
		std::cout<<"obtained eta, pt, phi of gen trackless electron"<<std::endl;
		
		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt;
		unsigned int j=0;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			Float_t hltEta = (*refIt)->eta();
			Float_t hltPhi = (*refIt)->phi();

			if(deltaR(hltEta, hltPhi, etaGenEle, phiGenEle) <= maxDeltaR){
				etaHltEle[j] = (*refIt)->eta();
				ptHltEle[j] = (*refIt)->pt();
				phiHltEle[j] = (*refIt)->phi();

				//initialize const_iterators to maps inside for loop using find(edm::Ref)
				SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
				clusterShapeHltEle[j] = SigmaIEIEIt->val;
				HadEmIt = (*HadEmHandle).find(*refIt);
				hadEmHltEle[j] = (HadEmIt->val)/(ptHltEle[j]*(TMath::CosH(etaHltEle[j]) ));
				HcalIsoIt = (*HcalIsoHandle).find(*refIt);
				hcalIsoHltEle[j] = (HcalIsoIt->val)/ptHltEle[j];
				EcalIsoIt = (*EcalIsoHandle).find(*refIt);
				ecalIsoHltEle[j] = (EcalIsoIt->val)/ptHltEle[j];
				j += 1;
				nHltEle += 1;
			}//end deltaR filter
			if(j==1) break;

		}//end loop over all entries in hltObjectsHandle

	}//end filter on trackless leg objects which should be matched to one trackless GEN electron 

}//end getTriggerObjectsInfo()

/*
void GetTrackedTriggerObjects(const edm::Event& iEvent, const Float_t genTrackedEta, const Float_t genTrackedPhi, const Float_t maxDrForMatch){

	//fill handles to edm::AssociationMap objects which store additional information about
	//RecoEcalCandidate objects made by the tracked leg
	iEvent.getByLabel(trackedSigmaIEIETag,trackedSigmaIEIEHandle);
	iEvent.getByLabel(trackedHadEmTag,trackedHadEmHandle);
	iEvent.getByLabel(trackedHcalIsoTag,trackedHcalIsoHandle);
	iEvent.getByLabel(trackedEcalIsoTag,trackedEcalIsoHandle);
	iEvent.getByLabel(trackedTrackIsoTag,trackedTrackIsoHandle);
	iEvent.getByLabel(trackedDphiTag,trackedDphiHandle);
	iEvent.getByLabel(trackedDetaTag,trackedDetaHandle);
	iEvent.getByLabel(trackedEpTag,trackedEpHandle);


	//fill handle to RecoEcalCandidate object collection made by tracked leg
	iEvent.getByLabel(hltTrackedLegTag, trackedLegHltObjectsHandle);
	
	if(!trackedLegHltObjectsHandle.isValid()) return;

	if(!trackedSigmaIEIEHandle.isValid() || !trackedHadEmHandle.isValid() || !trackedHcalIsoHandle.isValid() || !trackedEcalIsoHandle.isValid() || !trackedTrackIsoHandle.isValid() || !trackedDphiHandle.isValid() || !trackedDetaHandle.isValid() || !trackedEpHandle.isValid()) return;

	for(unsigned int h=0; h<trackedLegHltObjectsHandle->size(); h++){
		if( std::fabs( (getRef(trackedLegHltObjectsHandle, h))->eta()) < 2.5){
			trackedLegHltRefs.push_back( getRef(trackedLegHltObjectsHandle, h) );
		}
	}

	if(trackedLegHltRefs.size() == 0) return; //there is a chance there may not be any REC which passes the |eta|<2.5 requirement in one evt

	for(unsigned int i=0; i<trackedLegHltRefs.size(); i++){
		if(std::fabs(trackedLegHltRefs[i]->eta()) < 1.4791) nTrackedBarrelHltEle += 1;
		if(std::fabs(trackedLegHltRefs[i]->eta()) > 1.4791 && std::fabs(trackedLegHltRefs[i]->eta()) < 2.5) nTrackedEndcapHltEle += 1;
	}


	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;
	
	//declare const_iterators to maps outside for loop
	forMapIt::const_iterator trackedSigmaIEIEIt, trackedHadEmIt, trackedHcalIsoIt, trackedEcalIsoIt, trackedTrackIsoIt, trackedDphiIt, trackedDetaIt, trackedEpIt;
	Int_t indexBarrel = -1;
	Int_t indexEndcap = -1;
	for(unsigned int j=0; j<trackedLegHltRefs.size(); j++){
		if(std::fabs(trackedLegHltRefs[j]->eta()) < 1.4791){
			indexBarrel += 1;
			etaTrackedBarrelHltEle[indexBarrel] = trackedLegHltRefs[j]->eta();
			ptTrackedBarrelHltEle[indexBarrel] = trackedLegHltRefs[j]->pt();
			phiTrackedBarrelHltEle[indexBarrel] = trackedLegHltRefs[j]->phi();

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			trackedSigmaIEIEIt = (*trackedSigmaIEIEHandle).find(trackedLegHltRefs[j]);
			clusterShapeTrackedBarrelHltEle[indexBarrel] = trackedSigmaIEIEIt->val;
			trackedHadEmIt = (*trackedHadEmHandle).find(trackedLegHltRefs[j]);
			hadEmTrackedBarrelHltEle[indexBarrel] = (trackedHadEmIt->val)/(ptTrackedBarrelHltEle[indexBarrel]*(TMath::CosH(etaTrackedBarrelHltEle[indexBarrel]) ));
			trackedHcalIsoIt = (*trackedHcalIsoHandle).find(trackedLegHltRefs[j]);
			hcalIsoTrackedBarrelHltEle[indexBarrel] = (trackedHcalIsoIt->val)/ptTrackedBarrelHltEle[indexBarrel];
			trackedEcalIsoIt = (*trackedEcalIsoHandle).find(trackedLegHltRefs[j]);
			ecalIsoTrackedBarrelHltEle[indexBarrel] = (trackedEcalIsoIt->val)/ptTrackedBarrelHltEle[indexBarrel];

			trackedTrackIsoIt = (*trackedTrackIsoHandle).find(trackedLegHltRefs[j]);
			trackIsoTrackedBarrelHltEle[indexBarrel] = (trackedTrackIsoIt->val)/ptTrackedBarrelHltEle[indexBarrel];
			trackedDphiIt = (*trackedDphiHandle).find(trackedLegHltRefs[j]);
			dPhiTrackedBarrelHltEle[indexBarrel] = trackedDphiIt->val;
			trackedDetaIt = (*trackedDetaHandle).find(trackedLegHltRefs[j]);
			dEtaTrackedBarrelHltEle[indexBarrel] = trackedDetaIt->val;
			trackedEpIt = (*trackedEpHandle).find(trackedLegHltRefs[j]);
			epTrackedBarrelHltEle[indexBarrel] = trackedEpIt->val;
		}//end barrel eta filter
		
		if(std::fabs(trackedLegHltRefs[j]->eta()) > 1.4791 && std::fabs(trackedLegHltRefs[j]->eta()) < 2.5){
			indexEndcap += 1;
			etaTrackedEndcapHltEle[indexEndcap] = trackedLegHltRefs[j]->eta();
			ptTrackedEndcapHltEle[indexEndcap] = trackedLegHltRefs[j]->pt();
			phiTrackedEndcapHltEle[indexEndcap] = trackedLegHltRefs[j]->phi();

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			trackedSigmaIEIEIt = (*trackedSigmaIEIEHandle).find(trackedLegHltRefs[j]);
			clusterShapeTrackedEndcapHltEle[indexEndcap] = trackedSigmaIEIEIt->val;
			trackedHadEmIt = (*trackedHadEmHandle).find(trackedLegHltRefs[j]);
			hadEmTrackedEndcapHltEle[indexEndcap] = (trackedHadEmIt->val)/(ptTrackedEndcapHltEle[indexEndcap]*(TMath::CosH(etaTrackedEndcapHltEle[indexEndcap]) ));
			trackedHcalIsoIt = (*trackedHcalIsoHandle).find(trackedLegHltRefs[j]);
			hcalIsoTrackedEndcapHltEle[indexEndcap] = (trackedHcalIsoIt->val)/ptTrackedEndcapHltEle[indexEndcap];
			trackedEcalIsoIt = (*trackedEcalIsoHandle).find(trackedLegHltRefs[j]);
			ecalIsoTrackedEndcapHltEle[indexEndcap] = (trackedEcalIsoIt->val)/ptTrackedEndcapHltEle[indexEndcap];

			trackedTrackIsoIt = (*trackedTrackIsoHandle).find(trackedLegHltRefs[j]);
			trackIsoTrackedEndcapHltEle[indexEndcap] = (trackedTrackIsoIt->val)/ptTrackedEndcapHltEle[indexEndcap];
			trackedDphiIt = (*trackedDphiHandle).find(trackedLegHltRefs[j]);
			dPhiTrackedEndcapHltEle[indexEndcap] = trackedDphiIt->val;
			trackedDetaIt = (*trackedDetaHandle).find(trackedLegHltRefs[j]);
			dEtaTrackedEndcapHltEle[indexEndcap] = trackedDetaIt->val;
			trackedEpIt = (*trackedEpHandle).find(trackedLegHltRefs[j]);
			epTrackedEndcapHltEle[indexEndcap] = trackedEpIt->val;
		}//end endcap eta requirement

	}//end loop over all entries in trackedLegHltRefs

}//end GetTrackedTriggerObjects()


void GetMatchedTriggerObjects(
		const edm::Event& iEvent,
		const Float_t eta, const Float_t phi, const Float_t dRForMatch){

	//fill handles to edm::AssociationMap objects which store additional information about
	//RecoEcalCandidate objects made by the trackless leg
	iEvent.getByLabel(tracklessEcalIsoTag,tracklessEcalIsoHandle);
	iEvent.getByLabel(tracklessHcalIsoTag,tracklessHcalIsoHandle);
	iEvent.getByLabel(tracklessHadEmTag,tracklessHadEmHandle);
	iEvent.getByLabel(tracklessClusterShapeTag,tracklessClusterShapeHandle);
	//iEvent.getByLabel(hltTracklessLegTag, tracklessHcalIsoFilterHandle);

	if(!tracklessEcalIsoHandle.isValid() || !tracklessHcalIsoHandle.isValid() || !tracklessHadEmHandle.isValid() || !tracklessClusterShapeHandle.isValid() ) return;

	//fill handle to RecoEcalCandidate object collection made by the trackless leg
	iEvent.getByLabel(hltTracklessLegTag, tracklessLegHltObjectsHandle);
	if(!tracklessLegHltObjectsHandle.isValid()) return;


	for(unsigned int h=0; h<tracklessLegHltObjectsHandle->size(); h++){
		if(std::fabs( (getRef(tracklessLegHltObjectsHandle, h))->eta() ) > 2.4 && std::fabs( (getRef(tracklessLegHltObjectsHandle, h))->eta() ) < 3.0){
			tracklessLegHltRefs.push_back( getRef(tracklessLegHltObjectsHandle, h) );
		}
	}

	if(tracklessLegHltRefs.size() == 0) return;

	for(unsigned int i=0; i<tracklessLegHltRefs.size(); i++){
		if(std::fabs(tracklessLegHltRefs[i]->eta()) > 2.4 && std::fabs(tracklessLegHltRefs[i]->eta()) < 3.0 ) nTracklessHltEle += 1;
	}

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;
	
	//declare const_iterators to maps outside for loop
	forMapIt::const_iterator tracklessClusterShapeIt, tracklessHadEmIt, tracklessHcalIsoIt, tracklessEcalIsoIt;
	Int_t index = -1;
	for(unsigned int j=0; j<tracklessLegHltRefs.size(); j++){
		if(std::fabs(tracklessLegHltRefs[j]->eta()) > 2.4 && std::fabs(tracklessLegHltRefs[j]->eta()) < 3.0 ){
			index += 1;
			etaTracklessHltEle[index] = tracklessLegHltRefs[j]->eta();
			ptTracklessHltEle[index] = tracklessLegHltRefs[j]->pt();
			phiTracklessHltEle[index] = tracklessLegHltRefs[j]->phi();

			//initialize map iterators inside for loop with find(edm::Ref)
			tracklessClusterShapeIt = (*tracklessClusterShapeHandle).find(tracklessLegHltRefs[j]);
			clusterShapeTracklessHltEle[index] = tracklessClusterShapeIt->val;
			tracklessHadEmIt = (*tracklessHadEmHandle).find(tracklessLegHltRefs[j]);
			hadEmTracklessHltEle[index] = (tracklessHadEmIt->val)/(ptTracklessHltEle[index]*(TMath::CosH(etaTracklessHltEle[index])) );
			tracklessHcalIsoIt = (*tracklessHcalIsoHandle).find(tracklessLegHltRefs[j]);
			hcalIsoTracklessHltEle[index] = (tracklessHcalIsoIt->val)/ptTracklessHltEle[index];
			tracklessEcalIsoIt = (*tracklessEcalIsoHandle).find(tracklessLegHltRefs[j]);
			ecalIsoTracklessHltEle[index] = (tracklessEcalIsoIt->val)/ptTracklessHltEle[index];
		}//trackless eta filter	
		
	}//end loop over all entries in tracklessLegHltRefs

}//end GetMatchedTriggerObjects()
*/

private:
virtual void beginJob() override;
virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
virtual void endJob() override;


//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

// ----------member data ---------------------------

typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> > ecalCandToValMap;

//handles and inputTags to AssociationMaps for RecoEcalCandidate objects 
edm::Handle<ecalCandToValMap> SigmaIEIEHandle;
edm::InputTag SigmaIEIETag;

edm::Handle<ecalCandToValMap> HadEmHandle;
edm::InputTag HadEmTag;

edm::Handle<ecalCandToValMap> EcalIsoHandle;
edm::InputTag EcalIsoTag;

edm::Handle<ecalCandToValMap> HcalIsoHandle;
edm::InputTag HcalIsoTag;

edm::Handle<ecalCandToValMap> EpHandle;
edm::InputTag EpTag;

edm::Handle<ecalCandToValMap> DetaHandle;
edm::InputTag DetaTag;

edm::Handle<ecalCandToValMap> DphiHandle;
edm::InputTag DphiTag;

edm::Handle<ecalCandToValMap> TrackIsoHandle;
edm::InputTag TrackIsoTag;


//RecoEcalCandidate and reco::Candidate handles, relevant InputTags, and tree variables
//edm::Handle<std::vector<reco::RecoEcalCandidate> > hltObjectsHandle;
edm::Handle<reco::RecoEcalCandidateRefVector> hltObjectsHandle;
//original std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > hltRefs;
//equivalent to original const edm::RefVector<std::vector<reco::RecoEcalCandidate>> hltRefs;

edm::Handle<edm::OwnVector<reco::Candidate> > genObjectsHandle;

std::string tName;

edm::InputTag hltObjectsTag;

bool analyzingTracked;
edm::InputTag genObjectsTag;
double maxDeltaR;

TTree * tree;

Int_t nHltEle;
Float_t etaHltEle[NELE];
Float_t ptHltEle[NELE];
Float_t phiHltEle[NELE];
Float_t clusterShapeHltEle[NELE];
Float_t hadEmHltEle[NELE];
Float_t ecalIsoHltEle[NELE];
Float_t hcalIsoHltEle[NELE];
Float_t epHltEle[NELE];
Float_t dEtaHltEle[NELE];
Float_t dPhiHltEle[NELE];
Float_t trackIsoHltEle[NELE];

//GEN electron eta, pt, phi
//there will only be one GEN electron relevant to each entry in the tree
Float_t etaGenEle;
Float_t ptGenEle;
Float_t phiGenEle;

Int_t runNumber;
Long64_t evtNumber;


};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
//the order of private member vars which are initialized using iConfig.getParameter<>() is important!
recoAnalyzerGeneric::recoAnalyzerGeneric(const edm::ParameterSet& iConfig):
	SigmaIEIETag(iConfig.getParameter<edm::InputTag>("SigmaIEIE")),
	HadEmTag(iConfig.getParameter<edm::InputTag>("HadEm")),
	EcalIsoTag(iConfig.getParameter<edm::InputTag>("EcalIso")),
	HcalIsoTag(iConfig.getParameter<edm::InputTag>("HcalIso")),
	EpTag(iConfig.getParameter<edm::InputTag>("Ep")),
	DetaTag(iConfig.getParameter<edm::InputTag>("Deta")),
	DphiTag(iConfig.getParameter<edm::InputTag>("Dphi")),
	TrackIsoTag(iConfig.getParameter<edm::InputTag>("TrackIso")),
	tName(iConfig.getParameter<std::string>("treeName")),
	hltObjectsTag(iConfig.getParameter<edm::InputTag>("recoElectronCollection")),
	analyzingTracked(iConfig.getParameter<bool>("doAnalysisOfTracked")),
	genObjectsTag(iConfig.getParameter<edm::InputTag>("genCollection")),
	maxDeltaR(iConfig.getParameter<double>("dRMatch"))

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   
   tree=fs->make<TTree>(tName.c_str(),"RecoEcalCandidate object information before any trigger filters are applied");
  
   //RecoEcalCandidate object branches
   tree->Branch("nHltEle",&nHltEle,"nHltEle/I");
   tree->Branch("etaHltEle",etaHltEle,"etaHltEle[nHltEle]/F");
   tree->Branch("ptHltEle",ptHltEle,"ptHltEle[nHltEle]/F");
   tree->Branch("phiHltEle",phiHltEle,"phiHltEle[nHltEle]/F");
   tree->Branch("clusterShapeHltEle",clusterShapeHltEle,"clusterShapeHltEle[nHltEle]/F");
   tree->Branch("hadEmHltEle",hadEmHltEle,"hadEmHltEle[nHltEle]/F");
   tree->Branch("ecalIsoHltEle",ecalIsoHltEle,"ecalIsoHltEle[nHltEle]/F");
   tree->Branch("hcalIsoHltEle",hcalIsoHltEle,"hcalIsoHltEle[nHltEle]/F");
   tree->Branch("epHltEle",epHltEle,"epHltEle[nHltEle]/F");
   tree->Branch("dEtaHltEle",dEtaHltEle,"dEtaHltEle[nHltEle]/F");
   tree->Branch("dPhiHltEle",dPhiHltEle,"dPhiHltEle[nHltEle]/F");
   tree->Branch("trackIsoHltEle",trackIsoHltEle,"trackIsoHltEle[nHltEle]/F");
  
   //GEN electron branches
   tree->Branch("etaGenEle",&etaGenEle,"etaGenEle/F");
   tree->Branch("ptGenEle",&ptGenEle,"ptGenEle/F");
   tree->Branch("phiGenEle",&phiGenEle,"phiGenEle/F");

   //branches unrelated to REC objects
   tree->Branch("evtNumber",&evtNumber,"evtNumber/l");
   tree->Branch("runNumber",&runNumber,"runNumber/I");

}


recoAnalyzerGeneric::~recoAnalyzerGeneric()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
recoAnalyzerGeneric::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;

	/*
	 * reference code for computing di-object mass, using the two RecoEcalCandidate objects which fired the trigger
	if(matched_tracked_pT_ > 1. && matched_pT_ > 1.){
		//if this is true then compute the dilepton mass of the two HLT objects which fired the trigger
		double hlt_mLLSqd = 2*matched_tracked_pT_*matched_pT_*(TMath::CosH(matched_tracked_eta_ - matched_eta_) - TMath::Cos(matched_tracked_phi_ - matched_phi_) );
		if(hlt_mLLSqd > 0.) hlt_mLL_ = TMath::Sqrt(hlt_mLLSqd);

	}
	*/

	evtNumber = iEvent.id().event();
	runNumber = iEvent.id().run();

	nHltEle = 0;
	
	for(Int_t r=0; r<NELE; r++){
		//set all entries in arrays to zero
		etaHltEle[r]=1000;
		ptHltEle[r]=1000;
		phiHltEle[r]=1000;
		clusterShapeHltEle[r]=1000;
		hadEmHltEle[r]=1000;
		ecalIsoHltEle[r]=1000;
		hcalIsoHltEle[r]=1000;
		epHltEle[r]=1000;
		dEtaHltEle[r]=1000;
		dPhiHltEle[r]=1000;
		trackIsoHltEle[r]=1000;
		
		etaGenEle=1000;
		ptGenEle=1000;
		phiGenEle=1000;
	}

	getTriggerObjectsInfo(iEvent);

	//that's all folks!
	tree->Fill();


#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
recoAnalyzerGeneric::beginJob()
{
/*
  tree_file = new TFile(foutName.c_str(), "recreate");
  if(tree_file->IsZombie()){
    throw cms::Exception("OutputError") <<  "Output tree not created (Zombie): " << foutName;
    return;
  }
  tree_file->cd();
  
  //now do what ever initialization is needed
  tree = new TTree("selected","selected");
  tree->SetDirectory(tree_file);

  //InitNewTree();
*/

}

// ------------ method called once each job just after ending the event loop  ------------
void 
recoAnalyzerGeneric::endJob() 
{
	//loop over bins of "EventFraction", divide each bin content by totalNumEvents, then reset the bin content to the old content divided by totalNumEvents

	/*
	for(int i=1; i<=getXBins("EventFraction"); i++){
		if( getXBins("EventFraction") < 3) break;	//shouldn't need this, but just in case
	
		std::cout<<"bin # "<< i <<" content equals "<< get1DBinContents("EventFraction",i) <<std::endl;
		set1DBinContents("EventFraction",i, (get1DBinContents("EventFraction",i)/getTotalNumEvents() ) );
		std::cout<<"bin # "<< i <<" content equals "<< get1DBinContents("EventFraction",i) <<std::endl;
	
	}

   std::cout<< "the trackless leg of trigger fired on "<< getNumTriggeredEvents() << " events out of "<< getEfficiencyDenominator() << " total events which should have fired trackless leg of trigger" <<std::endl;
   set1DBinContents("HLTRecoEff",1, getNumTriggeredEvents()/getEfficiencyDenominator());

   */


	/*
  //save the tree into the file
  tree_file->cd();
  tree->Write();
  tree_file->Close();
*/

}

// ------------ method called when starting to processes a run  ------------
/*
void 
recoAnalyzerGeneric::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
recoAnalyzerGeneric::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
recoAnalyzerGeneric::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
recoAnalyzerGeneric::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
recoAnalyzerGeneric::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(recoAnalyzerGeneric);
