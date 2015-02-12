// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/recoAnalyzerZero
// Class:      recoAnalyzerZero
// 
/**\class recoAnalyzerZero recoAnalyzerZero.cc doubleElectronTracklessTrigger/recoAnalyzerZero/plugins/recoAnalyzerZero.cc

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

#define NELE 100


//
// class declaration
//

class recoAnalyzerZero : public edm::EDAnalyzer {
   public:
      explicit recoAnalyzerZero(const edm::ParameterSet&);
      ~recoAnalyzerZero();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
     

void GetTrackedTriggerObjects(const edm::Event& iEvent, const Float_t genTrackedEta, const Float_t genTrackedPhi, const Float_t maxDrForMatch){

	//std::cout<<"entered GetTrackedTriggerObjects"<<std::endl;
	iEvent.getByLabel(hltTrackedLegTag, trackedLegHltObjectsHandle);
	
	if(!trackedLegHltObjectsHandle.isValid() || trackedLegHltObjectsHandle->size() == 0 ) return;
	//std::cout<<"have a valid handle to the collection of tracked leg RecoEcalCandidate objects"<<std::endl;

	for(unsigned int h=0; h<trackedLegHltObjectsHandle->size(); h++){
		trackedLegHltRefs.push_back( getRef(trackedLegHltObjectsHandle, h) );

	}
	//std::cout<<"added something to trackedLegHltRefs"<<std::endl;


	for(unsigned int i=0; i<trackedLegHltRefs.size(); i++){
		nTrackedHltEle += 1;
	}
	
	//std::cout<<"there are  "<< nTrackedHltEle <<"  tracked leg RecoEcalCandidate objects in this event"<<std::endl;

	for(Int_t j=0; j< nTrackedHltEle; j++){
		etaTrackedHltEle[j] = trackedLegHltRefs[j]->eta();
		ptTrackedHltEle[j] = trackedLegHltRefs[j]->pt();
		phiTrackedHltEle[j] = trackedLegHltRefs[j]->phi();
	
	}

	/*
	std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > recoRefs;	//will be filled by calling hcalIsoFilterHandle->getObjects()
	tracklessHcalIsoFilterHandle->getObjects(trigger::TriggerCluster, recoRefs);
	if(recoRefs.empty() ) tracklessHcalIsoFilterHandle->getObjects(trigger::TriggerPhoton, recoRefs);

	if(recoRefs.empty() ) return;

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> > ecalCandToValMap;

	edm::InputTag hltNoTrackEcalClusterShapeSigmaIEtaIEtaTag("hltEgammaClusterShapeUnseeded","sigmaIEtaIEta5x5","TEST");
	edm::Handle<ecalCandToValMap> untrackedEcalClusterShapeSigmaIEtaIEtaHandle;
	iEvent.getByLabel(hltNoTrackEcalClusterShapeSigmaIEtaIEtaTag, untrackedEcalClusterShapeSigmaIEtaIEtaHandle);

	edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> >::const_iterator untrackedSigmaIEIEMapIt = (*untrackedEcalClusterShapeSigmaIEtaIEtaHandle).find(recoRefs[best]);
	matched_ecalClusterShape_SigmaIEtaIEta_ = untrackedSigmaIEIEMapIt->val;
	*/

	//declare handles to maps of seeded (tracked leg) sigmaIEIE, ecalIso, HE
	//typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> > ecalCandToValMap;

	/*
	//use recoTrackedRefs to study variables used in tracked leg filters
	//call recoTrackedRefs.clear() before accessing the recoEcalCandidate ref objects which passed a different filter
	std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > recoTrackedRefs;
	FILTHandle->getObjects(trigger::TriggerCluster, recoTrackedRefs);
	if(recoTrackedRefs.empty() ) FILTHandle->getObjects(trigger::TriggerPhoton, recoTrackedRefs);

	if(recoTrackedRefs.size() > 0){
		//fill the pT, eta, sigmaIEIE, H/E, ecalIso, hcalIso, and (1/E)-(1/P) histos
		//with all objects in recoTrackedRefs

	}//end if(recoTrackedRefs.size() > 0 )

	*/


	/*
	edm::InputTag l1SeedTag("hltL1sL1SingleEG20ORL1SingleEG22","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> l1SeedHandle;
	iEvent.getByLabel(l1SeedTag, l1SeedHandle);

	if(!l1SeedHandle.isValid() ){
		return;
	}

	if( (l1SeedHandle->l1emRefs()).size() > 0) numEvts_passing_L1Seed_ += 1;


	edm::InputTag l1FiltTag("hltEGL1SingleEG20ORL1SingleEG22Filter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> l1FiltHandle;
	iEvent.getByLabel(l1FiltTag, l1FiltHandle);

	if(!l1FiltHandle.isValid() ){
		return;
	}
	if( (l1FiltHandle->l1emRefs()).size() > 0) numEvts_passing_L1Filter_ += 1;

	
	edm::InputTag EtFilterTag("hltEG27WPXXEtFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> EtFilterHandle;
	iEvent.getByLabel(EtFilterTag, EtFilterHandle);

	if(!EtFilterHandle.isValid() ){
		return;
	}
	if((EtFilterHandle->photonRefs()).size() > 0 || (EtFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_EtFilter_ += 1;


	edm::InputTag ClusterShapeFilterTag("hltEle27WPXXClusterShapeFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> ClusterShapeFilterHandle;
	iEvent.getByLabel(ClusterShapeFilterTag, ClusterShapeFilterHandle);

	if(!ClusterShapeFilterHandle.isValid() ){
		return;
	}
	if( (ClusterShapeFilterHandle->photonRefs()).size() > 0 || (ClusterShapeFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_ClusterShapeFilter_ += 1;


	edm::InputTag HEFilterTag("hltEle27WPXXHEFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> HEFilterHandle;
	iEvent.getByLabel(HEFilterTag, HEFilterHandle);

	if(!HEFilterHandle.isValid() ){
		return;
	}
	if( (HEFilterHandle->photonRefs()).size() > 0 || (HEFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_HEFilter_ += 1;


	edm::InputTag EcalIsoFilterTag("hltEle27WPXXEcalIsoFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> EcalIsoFilterHandle;
	iEvent.getByLabel(EcalIsoFilterTag, EcalIsoFilterHandle);

	if(!EcalIsoFilterHandle.isValid() ){
		return;
	}
	if( (EcalIsoFilterHandle->photonRefs()).size() > 0 || (EcalIsoFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_EcalIsoFilter_ += 1;


	edm::InputTag HcalIsoFilterTag("hltEle27WPXXHcalIsoFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> HcalIsoFilterHandle;
	iEvent.getByLabel(HcalIsoFilterTag, HcalIsoFilterHandle);

	if(!HcalIsoFilterHandle.isValid() ){
		return;
	}
	if( (HcalIsoFilterHandle->photonRefs()).size() > 0 || (HcalIsoFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_HcalIsoFilter_ += 1;
	

	edm::InputTag PixelMatchFilterTag("hltEle27WPXXPixelMatchFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> PixelMatchFilterHandle;
	iEvent.getByLabel(PixelMatchFilterTag, PixelMatchFilterHandle);

	if(!PixelMatchFilterHandle.isValid() ){
		return;
	}
	if( (PixelMatchFilterHandle->photonRefs()).size() > 0 || (PixelMatchFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_PixelMatchFilter_ += 1;
	

	edm::InputTag E_P_FilterTag("hltEle27WPXXOneOEMinusOneOPFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> E_P_FilterHandle;
	iEvent.getByLabel(E_P_FilterTag, E_P_FilterHandle);

	if(!E_P_FilterHandle.isValid() ){
		return;
	}
	if( (E_P_FilterHandle->photonRefs()).size() > 0 || (E_P_FilterHandle->electronRefs()).size() > 0 ) numEvts_passing_E_P_Filter_ += 1;
	

	edm::InputTag DetaFilterTag("hltEle27WPXXDetaFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> DetaFilterHandle;
	iEvent.getByLabel(DetaFilterTag, DetaFilterHandle);

	if(!DetaFilterHandle.isValid() ){
		return;
	}
	if( (DetaFilterHandle->photonRefs()).size() > 0 || (DetaFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_DetaFilter_ += 1;
	

	edm::InputTag DphiFilterTag("hltEle27WPXXDphiFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> DphiFilterHandle;
	iEvent.getByLabel(DphiFilterTag, DphiFilterHandle);

	if(!DphiFilterHandle.isValid() ){
		return;
	}
	if( (DphiFilterHandle->photonRefs()).size() > 0 || (DphiFilterHandle->electronRefs()).size() > 0 ) numEvts_passing_DphiFilter_ += 1;
	

	edm::InputTag trackIsoFilterTag("hltEle27WPXXTrackIsoFilter", "", "TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> trackIsoFilterHandle;
	iEvent.getByLabel(trackIsoFilterTag, trackIsoFilterHandle);

	if(!trackIsoFilterHandle.isValid() ){
		//std::cout<<"no valid trackIsoFilterHandle in this event"<<std::endl;
		return;

	}

	std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > trackedRecoRefs;	//will be filled by calling trackIsoFilterHandle->getObjects()
	trackIsoFilterHandle->getObjects(trigger::TriggerCluster, trackedRecoRefs);
	if(trackedRecoRefs.empty() ) trackIsoFilterHandle->getObjects(trigger::TriggerPhoton, trackedRecoRefs);

	if(trackedRecoRefs.empty() ) return;

	numEvts_passing_TrackIsoFilter_ += 1;

	//now find the highest pT RecoEcalCandidate object in this event which passed the track iso filter
	double dR = 0;
	double maxPt = 0;
	unsigned int indexOfMaxPt = 0;
	numTrackedCandidates_ += trackedRecoRefs.size();
	for(unsigned int j=0; j<trackedRecoRefs.size() ; j++){
		dR = deltaR(genTrackedEta, genTrackedPhi, trackedRecoRefs[j]->eta(), trackedRecoRefs[j]->phi() );
		fill("trackedGENToHLTDeltaR", dR);
		if(trackedRecoRefs[j]->pt() > maxPt && dR < maxDrForMatch ){
			indexOfMaxPt = 0;
			maxPt = 0;
			indexOfMaxPt += j;
			maxPt += trackedRecoRefs[j]->pt();
		}//end maxPt filter

	}//end loop over trackedRecoRefs

	//now get the pT, eta, and phi of the highest pT RecoEcalCandidate object in this event which passed the track iso filter
	matched_tracked_pT_=trackedRecoRefs[indexOfMaxPt]->pt();
	matched_tracked_eta_=trackedRecoRefs[indexOfMaxPt]->eta();
	matched_tracked_phi_=trackedRecoRefs[indexOfMaxPt]->phi();

	*/
	
}//end GetTrackedTriggerObjects()


void GetMatchedTriggerObjects(
		const edm::Event& iEvent,
		const Float_t eta, const Float_t phi, const Float_t dRForMatch){

	/*edm::Handle<std::vector<reco::RecoEcalCandidate> > tracklessLegHltObjectsHandle;
std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > tracklessLegHltRefs;
std::vector<reco::RecoEcalCandidate> tracklessLegHltObjects;
	
edm::InputTag hltTracklessLegTag;

Int_t nTracklessHltEle;
Float_t etaTracklessHltEle[NELE];
Float_t ptTracklessHltEle[NELE];
Float_t phiTracklessHltEle[NELE];
*/

	//std::cout<<"entered GetMatchedTriggerObjects"<<std::endl;
	iEvent.getByLabel(hltTracklessLegTag, tracklessLegHltObjectsHandle);
	
	if(!tracklessLegHltObjectsHandle.isValid() || tracklessLegHltObjectsHandle->size() == 0 ) return;
	//std::cout<<"have a valid handle to the collection of trackless leg RecoEcalCandidate objects"<<std::endl;


	for(unsigned int h=0; h<tracklessLegHltObjectsHandle->size(); h++){
		tracklessLegHltRefs.push_back( getRef(tracklessLegHltObjectsHandle, h) );
	}
	//std::cout<<"added something to tracklessLegHltRefs"<<std::endl;


	for(unsigned int i=0; i<tracklessLegHltRefs.size(); i++){
		nTracklessHltEle += 1;
	}

	//std::cout<<"there are  "<< nTracklessHltEle <<"  trackless leg RecoEcalCandidate objects in this event"<<std::endl;

	for(Int_t j=0; j<nTracklessHltEle; j++){
		etaTracklessHltEle[j] = tracklessLegHltRefs[j]->eta();
		ptTracklessHltEle[j] = tracklessLegHltRefs[j]->pt();
		phiTracklessHltEle[j] = tracklessLegHltRefs[j]->phi();
	
	}

	/*
	//see how many evts pass each filter in the trackless leg
	edm::InputTag EtFilterTag("hltEG15WPYYtracklessEtFilterUnseeded","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> EtFilterHandle;
	iEvent.getByLabel(EtFilterTag, EtFilterHandle);

	if(!EtFilterHandle.isValid() ){
		return;
	}
	if( (EtFilterHandle->photonRefs()).size() + (EtFilterHandle->electronRefs()).size() > 1 ) numEvts_passing_trackless_EtFilter_ += 1;

	edm::InputTag ClusterShapeFilterTag("hltEle15WPYYtracklessClusterShapeFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> ClusterShapeFilterHandle;
	iEvent.getByLabel(ClusterShapeFilterTag, ClusterShapeFilterHandle);

	if(!ClusterShapeFilterHandle.isValid() ){
		return;
	}
	if( (ClusterShapeFilterHandle->photonRefs()).size() + (ClusterShapeFilterHandle->electronRefs()).size() > 1 ) numEvts_passing_trackless_ClusterShapeFilter_ += 1;


	edm::InputTag EcalIsoFilterTag("hltEle15WPYYtracklessEcalIsoFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> EcalIsoFilterHandle;
	iEvent.getByLabel(EcalIsoFilterTag, EcalIsoFilterHandle);

	if(!EcalIsoFilterHandle.isValid() ){
		return;
	}
	if( (EcalIsoFilterHandle->photonRefs()).size() + (EcalIsoFilterHandle->electronRefs()).size() > 1 ) numEvts_passing_trackless_EcalIsoFilter_ += 1;


	edm::InputTag HEFilterTag("hltEle15WPYYtracklessHEFilter","","TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> HEFilterHandle;
	iEvent.getByLabel(HEFilterTag, HEFilterHandle);

	if(!HEFilterHandle.isValid() ){
		return;
	}
	if( (HEFilterHandle->photonRefs()).size() + (HEFilterHandle->electronRefs()).size() > 1 ) numEvts_passing_trackless_HEFilter_ += 1;


	//I should not need anything from the collection of trigger::TriggerEventWithRefs objects.  I can just grab the RecoEcalCandidate
	//objects which pass the trackless HcalIso filter from a Handle tied to the trackless hcalIso filter!
	edm::InputTag hcalIsoFilterTag("hltEle15WPYYtracklessHcalIsoFilter", "", "TEST");
	edm::Handle<trigger::TriggerFilterObjectWithRefs> tracklessHcalIsoFilterHandle;
	iEvent.getByLabel(hcalIsoFilterTag, tracklessHcalIsoFilterHandle);

	if(!tracklessHcalIsoFilterHandle.isValid() ){
		//std::cout<<"no valid hcalIsoFilterHandle in this event"<<std::endl;
		return;

	}

	std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > recoRefs;	//will be filled by calling hcalIsoFilterHandle->getObjects()
	tracklessHcalIsoFilterHandle->getObjects(trigger::TriggerCluster, recoRefs);
	if(recoRefs.empty() ) tracklessHcalIsoFilterHandle->getObjects(trigger::TriggerPhoton, recoRefs);

	if(recoRefs.empty() ) return;

	if(recoRefs.size() > 1) numEvts_passing_trackless_HcalIsoFilter_ += 1;

	

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> > ecalCandToValMap;

	//collections for untracked electron candidates
	//these maps are available for RecoEcalCandidate objects after any filter, not just the filter
	//which cut on the variable stored in the map
	//for example, the map of HcalIso for trackless leg candidates is available to any RecoEcalCandidate object
	//which passes the trackless leg EtFilter 
	edm::InputTag hltNoTrackEcalClusterShapeTag("hltEgammaClusterShapeUnseeded","","TEST");
	edm::Handle<ecalCandToValMap> untrackedEcalClusterShapeHandle;
	iEvent.getByLabel(hltNoTrackEcalClusterShapeTag, untrackedEcalClusterShapeHandle);

	edm::InputTag hltNoTrackEcalClusterShapeSigmaIEtaIEtaTag("hltEgammaClusterShapeUnseeded","sigmaIEtaIEta5x5","TEST");
	edm::Handle<ecalCandToValMap> untrackedEcalClusterShapeSigmaIEtaIEtaHandle;
	iEvent.getByLabel(hltNoTrackEcalClusterShapeSigmaIEtaIEtaTag, untrackedEcalClusterShapeSigmaIEtaIEtaHandle);

	edm::InputTag hltNoTrackEcalIsoTag("hltEgammaEcalPFClusterIsoUnseeded","","TEST");
	edm::Handle<ecalCandToValMap> untrackedEcalIsoHandle;
	iEvent.getByLabel(hltNoTrackEcalIsoTag, untrackedEcalIsoHandle);

	edm::InputTag hltNoTrackHoverETag("hltEgammaHoverEUnseeded","","TEST");
	edm::Handle<ecalCandToValMap> untrackedHoverEHandle;
	iEvent.getByLabel(hltNoTrackHoverETag, untrackedHoverEHandle);

	edm::InputTag hltNoTrackHcalIsoTag("hltEgammaHcalPFClusterIsoUnseeded","","TEST");
	edm::Handle<ecalCandToValMap> untrackedHcalIsoHandle;
	iEvent.getByLabel(hltNoTrackHcalIsoTag, untrackedHcalIsoHandle);

 
	float hltPhi = 0;
	float maxPt = 0;
	unsigned int indexOfMaxPt = 0;
	int numPassingEtaCut = 0;
	double dR = 0;
	bool hasChanged = false;


	for(unsigned int i=0; i<recoRefs.size(); i++){
		if(std::fabs(recoRefs[i]->eta()) > 2.4 && std::fabs(recoRefs[i]->eta()) < 3.0){
			if(numEvts_passing_trackless_EtaFilter_ ==0) numEvts_passing_trackless_EtaFilter_ += 1;
			numPassingEtaCut += 1;
			hltPhi = recoRefs[i]->phi();
			dR = deltaR(eta, phi, recoRefs[i]->eta(), hltPhi);
			//save dR information for all objects which make it to this point 
			if(recoRefs[i]->pt() > maxPt && dR < dRForMatch ){
				//std::cout<<"called pt() on an object from recoRefs vector"<<std::endl;
				hasChanged = true;
				maxPt = 0;
				indexOfMaxPt = 0;
				maxPt += recoRefs[i]->pt();
				indexOfMaxPt += i;
			}//end filter on maxPt

		}//end eta filter

	}//end loop over reco ecal candidate object references
	
	numRecoEcalCands_ = numPassingEtaCut;

	if(numRecoEcalCands_ == 0) return;
	if(!hasChanged) return;

	//now that the highest pT, dR matched RecoEcalCandidate has been found, record the relative calo iso, (had/em)/energy, and sigmaIEIE
	//values associated with this RecoEcalCandidate
	unsigned int best = indexOfMaxPt;
	matched_pT_ = recoRefs[best]->pt();
	matched_eta_ = recoRefs[best]->eta();
   	matched_phi_ = recoRefs[best]->phi();
	
	edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> >::const_iterator untrackedSigmaIEIEMapIt = (*untrackedEcalClusterShapeSigmaIEtaIEtaHandle).find(recoRefs[best]);
	matched_ecalClusterShape_SigmaIEtaIEta_ = untrackedSigmaIEIEMapIt->val;
	
	edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> >::const_iterator untrackedEcalClusterShapeMapIt = (*untrackedEcalClusterShapeHandle).find(recoRefs[best]);
	matched_ecalClusterShape_ = untrackedEcalClusterShapeMapIt->val;
 	
	edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> >::const_iterator untrackedEcalIsoMapIt = (*untrackedEcalIsoHandle).find(recoRefs[best]);
	matched_ecalIso_ = (untrackedEcalIsoMapIt->val)/(matched_pT_);
  	
	edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> >::const_iterator untrackedHcalIsoMapIt = (*untrackedHcalIsoHandle).find(recoRefs[best]);
	matched_hcalIso_ = (untrackedHcalIsoMapIt->val)/(matched_pT_);

	edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> >::const_iterator untrackedHoverEMapIt = (*untrackedHoverEHandle).find(recoRefs[best]);
	matched_hOverE_ = (untrackedHoverEMapIt->val)/(matched_pT_*(TMath::CosH(matched_eta_)));

	*/

}//end GetMatchedTriggerObjects()


private:
virtual void beginJob() override;
virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
virtual void endJob() override;

/*
std::map<std::string,TH1D*> hists_;
std::map<std::string,TH2D*> histsTwo_;
std::map<std::string,TH3D*> histsThree_;
*/


//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

// ----------member data ---------------------------

edm::Handle<std::vector<reco::RecoEcalCandidate> > trackedLegHltObjectsHandle;
std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > trackedLegHltRefs;
//std::vector<reco::RecoEcalCandidate> trackedLegHltObjects;
	
edm::Handle<std::vector<reco::RecoEcalCandidate> > tracklessLegHltObjectsHandle;
std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > tracklessLegHltRefs;
//std::vector<reco::RecoEcalCandidate> tracklessLegHltObjects;
	
edm::Handle<edm::OwnVector<reco::Candidate> > trackedGenElectronHandle;
edm::Handle<edm::OwnVector<reco::Candidate> > tracklessGenElectronHandle;

std::string tName;

edm::InputTag hltTrackedLegTag;
edm::InputTag hltTracklessLegTag;
edm::InputTag trackedGenTag;
edm::InputTag tracklessGenTag;

TTree * tree;

Int_t nTrackedHltEle;
Float_t etaTrackedHltEle[NELE];
Float_t ptTrackedHltEle[NELE];
Float_t phiTrackedHltEle[NELE];

Int_t nTracklessHltEle;
Float_t etaTracklessHltEle[NELE];
Float_t ptTracklessHltEle[NELE];
Float_t phiTracklessHltEle[NELE];

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
recoAnalyzerZero::recoAnalyzerZero(const edm::ParameterSet& iConfig):
	tName(iConfig.getParameter<std::string>("treeName")),
	hltTrackedLegTag(iConfig.getParameter<edm::InputTag>("trackedElectronCollection")),
	hltTracklessLegTag(iConfig.getParameter<edm::InputTag>("tracklessElectronCollection")),
	trackedGenTag(iConfig.getParameter<edm::InputTag>("genTrackedElectronCollection")),
	tracklessGenTag(iConfig.getParameter<edm::InputTag>("genTracklessElectronCollection"))

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   
   tree=fs->make<TTree>(tName.c_str(),"RecoEcalCandidate object information before any trigger filters are applied");

   tree->Branch("nTrackedHltEle",&nTrackedHltEle,"nTrackedHltEle/I");
   tree->Branch("etaTrackedHltEle",etaTrackedHltEle,"etaTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("ptTrackedHltEle",ptTrackedHltEle,"ptTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("phiTrackedHltEle",phiTrackedHltEle,"phiTrackedHltEle[nTrackedHltEle]/F");

   tree->Branch("nTracklessHltEle",&nTracklessHltEle,"nTracklessHltEle/I");
   tree->Branch("etaTracklessHltEle",etaTracklessHltEle,"etaTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("ptTracklessHltEle",ptTracklessHltEle,"ptTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("phiTracklessHltEle",phiTracklessHltEle,"phiTracklessHltEle[nTracklessHltEle]/F");

   tree->Branch("evtNumber",&evtNumber,"evtNumber/l");
   tree->Branch("runNumber",&runNumber,"runNumber/I");

}


recoAnalyzerZero::~recoAnalyzerZero()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
recoAnalyzerZero::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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

	nTracklessHltEle = 0;
	nTrackedHltEle = 0;
	trackedLegHltRefs.clear();
	tracklessLegHltRefs.clear();

	for(Int_t r=0; r<NELE; r++){
		//set all entries in arrays to zero
		etaTrackedHltEle[r]=0;
		ptTrackedHltEle[r]=0;
		phiTrackedHltEle[r]=0;
		
		etaTracklessHltEle[r]=0;
		ptTracklessHltEle[r]=0;
		phiTracklessHltEle[r]=0;
	}

	GetTrackedTriggerObjects(iEvent, 0., 0., 20);
	GetMatchedTriggerObjects(iEvent, 0., 0., 20);

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
recoAnalyzerZero::beginJob()
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
recoAnalyzerZero::endJob() 
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
recoAnalyzerZero::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
recoAnalyzerZero::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
recoAnalyzerZero::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
recoAnalyzerZero::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
recoAnalyzerZero::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

/*
void recoAnalyzerZero::InitNewTree(void){

  //make one branch for each unique variable I want to track - ecal iso, lepton pT, invariant mass of dilepton system, etc

  std::cout << "[STATUS] InitNewTree" << std::endl;
  if(tree==NULL) return;
  tree->Branch("runNumber",     &runNumber,     "runNumber/I");
  tree->Branch("eventNumber",   &eventNumber, "eventNumber/l");
  tree->Branch("lumiBlock",     &lumiBlock,     "lumiBlock/I");
  tree->Branch("runTime",       &runTime,         "runTime/i");
  
  tree->Branch("mcGenWeight",   &mcGenWeight, "mcGenWeight/F");

  tree->Branch("nPU", nPU, "nPU[1]/I");
  tree->Branch("rho", &rho, "rho/F");
  tree->Branch("nPV", &nPV, "nPV/I");


  tree->Branch("chargeEle",   chargeEle,    "chargeEle[2]/I");	//[nEle]
  tree->Branch("etaSCEle",      etaSCEle,       "etaSCEle[2]/F");	//[nSCEle]
  tree->Branch("phiSCEle",      phiSCEle,       "phiSCEle[2]/F");	//[nSCEle]

  tree->Branch("PtEle",       PtEle,        "PtEle[2]/F");

  tree->Branch("seedXSCEle",           seedXSCEle,      "seedXSCEle[2]/F");
  tree->Branch("seedYSCEle",           seedYSCEle,      "seedYSCEle[2]/F");
  tree->Branch("seedEnergySCEle", seedEnergySCEle, "seedEnergySCEle[2]/F");

  tree->Branch("gainEle", gainEle, "gainEle[2]/b");

  tree->Branch("energyMCEle", energyMCEle, "energyMCEle[2]/F");
  tree->Branch("energySCEle", energySCEle, "energySCEle[2]/F");
  tree->Branch("rawEnergySCEle", rawEnergySCEle, "rawEnergySCEle[2]/F");
  tree->Branch("esEnergySCEle", esEnergySCEle, "esEnergySCEle[2]/F");


  tree->Branch("R9Ele", R9Ele, "R9Ele[2]/F");

  tree->Branch("e5x5SCEle", e5x5SCEle, "e5x5SCEle[2]/F");

  tree->Branch("invMass",    &invMass,      "invMass/F");   // invariant mass ele+SC
  tree->Branch("invMass_SC", &invMass_SC,   "invMass_SC/F"); // invariant mass SC+SC


  tree->Branch("invMass_MC", &invMass_MC, "invMass_MC/F");

  tree->Branch("etaMCEle",      etaMCEle,       "etaMCEle[2]/F");	//[nEle]
  tree->Branch("phiMCEle",      phiMCEle,       "phiMCEle[2]/F");	//[nEle]

  tree->Branch("nHitsSCEle", nHitsSCEle, "nHitsSCEle[2]/I");

  tree->Branch("sigmaIEtaIEtaSCEle", sigmaIEtaIEtaSCEle, "sigmaIEtaIEtaSCEle[2]/F");
  tree->Branch("sigmaIEtaIEtaSCEle", sigmaIEtaIEtaSCEle, "sigmaIEtaIEtaSCEle[2]/F");

  return;
}

//negative index means the corresponding electron does not exist
void recoAnalyzerZero::TreeSetSingleElectronVar(const pat::Electron& electron1, int index){

  if(index<0){
    PtEle[-index] 	  = 0;  
    chargeEle[-index] = 0;
    etaEle[-index]    = 0; 
    phiEle[-index]    = 0;
    return;
  }   

  PtEle[index]     = electron1.et();  
  chargeEle[index] = electron1.charge();
  etaEle[index]    = electron1.eta(); 
  phiEle[index]    = electron1.phi();
}

void recoAnalyzerZero::TreeSetSingleElectronVar(const reco::SuperCluster& electron1, int index){

  if(index<0){
    PtEle[-index] 	  = 0;
    chargeEle[-index] = 0;
    etaEle[-index]    = 0;
    phiEle[-index]    = 0;
    return;
  }

//checks

  PtEle[index]     = electron1.energy()/cosh(electron1.eta());
  chargeEle[index] = -100; // dont know the charge for SC
  etaEle[index]    = electron1.eta(); // eta = etaSC
  phiEle[index]    = electron1.phi();
}

void recoAnalyzerZero::TreeSetDiElectronVar(const pat::Electron& electron1, const reco::SuperCluster& electron2){
  
  TreeSetSingleElectronVar(electron1, 0);
  TreeSetSingleElectronVar(electron2, 1);

  double t1=TMath::Exp(-etaEle[0]);
  double t2=TMath::Exp(-etaEle[1]);
  double t1q = t1*t1;
  double t2q = t2*t2;

  double angle=1- ( (1-t1q)*(1-t2q)+4*t1*t2*cos(phiEle[0]-phiEle[1]))/( (1+t1q)*(1+t2q) );


  invMass = sqrt(2*electron1.energy()*electron2.energy() *angle);
  invMass_e5x5   = sqrt(2*electron1.e5x5()*(clustertools->e5x5(*electron2.seed())) * angle);

}
*/


//define this as a plug-in
DEFINE_FWK_MODULE(recoAnalyzerZero);
