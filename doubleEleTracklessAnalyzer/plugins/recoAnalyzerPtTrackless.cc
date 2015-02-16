// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/recoAnalyzerPtTrackless
// Class:      recoAnalyzerPtTrackless
// 
/**\class recoAnalyzerPtTrackless recoAnalyzerPtTrackless.cc doubleElectronTracklessTrigger/recoAnalyzerPtTrackless/plugins/recoAnalyzerPtTrackless.cc

 Description: [one line class summary]

 used to filter out events with at least one trackless RecoEcalCandidate with pt>15
 no requirements on tracked REC
 
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

class recoAnalyzerPtTrackless : public edm::EDAnalyzer {
   public:
      explicit recoAnalyzerPtTrackless(const edm::ParameterSet&);
      ~recoAnalyzerPtTrackless();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
     

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
	
	if(!trackedLegHltObjectsHandle.isValid() || trackedLegHltObjectsHandle->size() == 0 ) return;

	if(!trackedSigmaIEIEHandle.isValid() || !trackedHadEmHandle.isValid() || !trackedHcalIsoHandle.isValid() || !trackedEcalIsoHandle.isValid() || !trackedTrackIsoHandle.isValid() || !trackedDphiHandle.isValid() || !trackedDetaHandle.isValid() || !trackedEpHandle.isValid()) return;

	for(unsigned int h=0; h<trackedLegHltObjectsHandle->size(); h++){
		if( std::fabs( (getRef(trackedLegHltObjectsHandle, h))->eta()) < 2.5){
			trackedLegHltRefs.push_back( getRef(trackedLegHltObjectsHandle, h) );
		}
	}

	if(trackedLegHltRefs.size() == 0) return; //there is a chance there may not be any REC which passes the |eta|<2.5 requirement in one evt

	for(unsigned int i=0; i<trackedLegHltRefs.size(); i++){
		if(std::fabs(trackedLegHltRefs[i]->eta()) < 1.4791) nTrackedBarrelHltEle += 1;
		if(std::fabs(trackedLegHltRefs[i]->eta()) > 1.4791) nTrackedEndcapHltEle += 1;
	}

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;
	
	Int_t totalTrackedEles = nTrackedBarrelHltEle + nTrackedEndcapHltEle;
	
	//declare const_iterators to maps outside for loop
	forMapIt::const_iterator trackedSigmaIEIEIt, trackedHadEmIt, trackedHcalIsoIt, trackedEcalIsoIt, trackedTrackIsoIt, trackedDphiIt, trackedDetaIt, trackedEpIt;
	for(Int_t j=0; j< totalTrackedEles; j++){
		if(std::fabs(trackedLegHltRefs[j]->eta()) < 1.4791){
			etaTrackedBarrelHltEle[j] = trackedLegHltRefs[j]->eta();
			ptTrackedBarrelHltEle[j] = trackedLegHltRefs[j]->pt();
			phiTrackedBarrelHltEle[j] = trackedLegHltRefs[j]->phi();

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			trackedSigmaIEIEIt = (*trackedSigmaIEIEHandle).find(trackedLegHltRefs[j]);
			clusterShapeTrackedBarrelHltEle[j] = trackedSigmaIEIEIt->val;
			trackedHadEmIt = (*trackedHadEmHandle).find(trackedLegHltRefs[j]);
			hadEmTrackedBarrelHltEle[j] = (trackedHadEmIt->val)/(ptTrackedBarrelHltEle[j]*(TMath::CosH(etaTrackedBarrelHltEle[j]) ));
			trackedHcalIsoIt = (*trackedHcalIsoHandle).find(trackedLegHltRefs[j]);
			hcalIsoTrackedBarrelHltEle[j] = (trackedHcalIsoIt->val)/ptTrackedBarrelHltEle[j];
			trackedEcalIsoIt = (*trackedEcalIsoHandle).find(trackedLegHltRefs[j]);
			ecalIsoTrackedBarrelHltEle[j] = (trackedEcalIsoIt->val)/ptTrackedBarrelHltEle[j];

			trackedTrackIsoIt = (*trackedTrackIsoHandle).find(trackedLegHltRefs[j]);
			trackIsoTrackedBarrelHltEle[j] = (trackedTrackIsoIt->val)/ptTrackedBarrelHltEle[j];
			trackedDphiIt = (*trackedDphiHandle).find(trackedLegHltRefs[j]);
			dPhiTrackedBarrelHltEle[j] = trackedDphiIt->val;
			trackedDetaIt = (*trackedDetaHandle).find(trackedLegHltRefs[j]);
			dEtaTrackedBarrelHltEle[j] = trackedDetaIt->val;
			trackedEpIt = (*trackedEpHandle).find(trackedLegHltRefs[j]);
			epTrackedBarrelHltEle[j] = trackedEpIt->val;
		}//end barrel eta filter
		
		if(std::fabs(trackedLegHltRefs[j]->eta()) > 1.4791){
			etaTrackedEndcapHltEle[j] = trackedLegHltRefs[j]->eta();
			ptTrackedEndcapHltEle[j] = trackedLegHltRefs[j]->pt();
			phiTrackedEndcapHltEle[j] = trackedLegHltRefs[j]->phi();

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			trackedSigmaIEIEIt = (*trackedSigmaIEIEHandle).find(trackedLegHltRefs[j]);
			clusterShapeTrackedEndcapHltEle[j] = trackedSigmaIEIEIt->val;
			trackedHadEmIt = (*trackedHadEmHandle).find(trackedLegHltRefs[j]);
			hadEmTrackedEndcapHltEle[j] = (trackedHadEmIt->val)/(ptTrackedEndcapHltEle[j]*(TMath::CosH(etaTrackedEndcapHltEle[j]) ));
			trackedHcalIsoIt = (*trackedHcalIsoHandle).find(trackedLegHltRefs[j]);
			hcalIsoTrackedEndcapHltEle[j] = (trackedHcalIsoIt->val)/ptTrackedEndcapHltEle[j];
			trackedEcalIsoIt = (*trackedEcalIsoHandle).find(trackedLegHltRefs[j]);
			ecalIsoTrackedEndcapHltEle[j] = (trackedEcalIsoIt->val)/ptTrackedEndcapHltEle[j];

			trackedTrackIsoIt = (*trackedTrackIsoHandle).find(trackedLegHltRefs[j]);
			trackIsoTrackedEndcapHltEle[j] = (trackedTrackIsoIt->val)/ptTrackedEndcapHltEle[j];
			trackedDphiIt = (*trackedDphiHandle).find(trackedLegHltRefs[j]);
			dPhiTrackedEndcapHltEle[j] = trackedDphiIt->val;
			trackedDetaIt = (*trackedDetaHandle).find(trackedLegHltRefs[j]);
			dEtaTrackedEndcapHltEle[j] = trackedDetaIt->val;
			trackedEpIt = (*trackedEpHandle).find(trackedLegHltRefs[j]);
			epTrackedEndcapHltEle[j] = trackedEpIt->val;
		}//end endcap eta requirement

	}

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


	//fill handle to RecoEcalCandidate object collection made by the trackless leg
	iEvent.getByLabel(hltTracklessLegTag, tracklessLegHltObjectsHandle);
	if(!tracklessLegHltObjectsHandle.isValid() || tracklessLegHltObjectsHandle->size() == 0 ) return;

	if(!tracklessEcalIsoHandle.isValid() || !tracklessHcalIsoHandle.isValid() || !tracklessHadEmHandle.isValid() || !tracklessClusterShapeHandle.isValid() ) return;

	for(unsigned int h=0; h<tracklessLegHltObjectsHandle->size(); h++){
		if(std::fabs( (getRef(tracklessLegHltObjectsHandle, h))->eta() ) > 2.5 && std::fabs( (getRef(tracklessLegHltObjectsHandle, h))->eta() ) < 3.0 && (getRef(tracklessLegHltObjectsHandle, h))->pt() > 15){
			tracklessLegHltRefs.push_back( getRef(tracklessLegHltObjectsHandle, h) );
		}
	}

	if(tracklessLegHltRefs.size() == 0) return;

	for(unsigned int i=0; i<tracklessLegHltRefs.size(); i++){
		nTracklessHltEle += 1;
	}

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;
	
	//declare const_iterators to maps outside for loop
	forMapIt::const_iterator tracklessClusterShapeIt, tracklessHadEmIt, tracklessHcalIsoIt, tracklessEcalIsoIt;
	for(Int_t j=0; j<nTracklessHltEle; j++){
		etaTracklessHltEle[j] = tracklessLegHltRefs[j]->eta();
		ptTracklessHltEle[j] = tracklessLegHltRefs[j]->pt();
		phiTracklessHltEle[j] = tracklessLegHltRefs[j]->phi();

		//initialize map iterators inside for loop with find(edm::Ref)
		tracklessClusterShapeIt = (*tracklessClusterShapeHandle).find(tracklessLegHltRefs[j]);
		clusterShapeTracklessHltEle[j] = tracklessClusterShapeIt->val;
		tracklessHadEmIt = (*tracklessHadEmHandle).find(tracklessLegHltRefs[j]);
		hadEmTracklessHltEle[j] = (tracklessHadEmIt->val)/(ptTracklessHltEle[j]*(TMath::CosH(etaTracklessHltEle[j])) );
		tracklessHcalIsoIt = (*tracklessHcalIsoHandle).find(tracklessLegHltRefs[j]);
		hcalIsoTracklessHltEle[j] = (tracklessHcalIsoIt->val)/ptTracklessHltEle[j];
		tracklessEcalIsoIt = (*tracklessEcalIsoHandle).find(tracklessLegHltRefs[j]);
		ecalIsoTracklessHltEle[j] = (tracklessEcalIsoIt->val)/ptTracklessHltEle[j];

	}

}//end GetMatchedTriggerObjects()


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

//handles and inputTags to AssociationMaps for RecoEcalCandidate objects made in the tracked leg
edm::Handle<ecalCandToValMap> trackedSigmaIEIEHandle;
edm::InputTag trackedSigmaIEIETag;

edm::Handle<ecalCandToValMap> trackedHadEmHandle;
edm::InputTag trackedHadEmTag;

edm::Handle<ecalCandToValMap> trackedEcalIsoHandle;
edm::InputTag trackedEcalIsoTag;

edm::Handle<ecalCandToValMap> trackedHcalIsoHandle;
edm::InputTag trackedHcalIsoTag;

edm::Handle<ecalCandToValMap> trackedEpHandle;
edm::InputTag trackedEpTag;

edm::Handle<ecalCandToValMap> trackedDetaHandle;
edm::InputTag trackedDetaTag;

edm::Handle<ecalCandToValMap> trackedDphiHandle;
edm::InputTag trackedDphiTag;

edm::Handle<ecalCandToValMap> trackedTrackIsoHandle;
edm::InputTag trackedTrackIsoTag;


//handles and inputTags to AssociationMaps for RecoEcalCandidate objects made in the trackless leg
edm::Handle<ecalCandToValMap> tracklessClusterShapeHandle;
edm::InputTag tracklessClusterShapeTag;

edm::Handle<ecalCandToValMap> tracklessHadEmHandle;
edm::InputTag tracklessHadEmTag;

edm::Handle<ecalCandToValMap> tracklessEcalIsoHandle;
edm::InputTag tracklessEcalIsoTag;

edm::Handle<ecalCandToValMap> tracklessHcalIsoHandle;
edm::InputTag tracklessHcalIsoTag;



//RecoEcalCandidate and reco::Candidate handles, relevant InputTags, and tree variables
edm::Handle<std::vector<reco::RecoEcalCandidate> > trackedLegHltObjectsHandle;
std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > trackedLegHltRefs;
	
edm::Handle<std::vector<reco::RecoEcalCandidate> > tracklessLegHltObjectsHandle;
std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > tracklessLegHltRefs;

edm::Handle<edm::OwnVector<reco::Candidate> > trackedGenElectronHandle;
edm::Handle<edm::OwnVector<reco::Candidate> > tracklessGenElectronHandle;

std::string tName;

edm::InputTag hltTrackedLegTag;
edm::InputTag hltTracklessLegTag;
edm::InputTag trackedGenTag;
edm::InputTag tracklessGenTag;

TTree * tree;

Int_t nTrackedBarrelHltEle;
Float_t etaTrackedBarrelHltEle[NELE];
Float_t ptTrackedBarrelHltEle[NELE];
Float_t phiTrackedBarrelHltEle[NELE];
Float_t clusterShapeTrackedBarrelHltEle[NELE];
Float_t hadEmTrackedBarrelHltEle[NELE];
Float_t ecalIsoTrackedBarrelHltEle[NELE];
Float_t hcalIsoTrackedBarrelHltEle[NELE];
Float_t epTrackedBarrelHltEle[NELE];
Float_t dEtaTrackedBarrelHltEle[NELE];
Float_t dPhiTrackedBarrelHltEle[NELE];
Float_t trackIsoTrackedBarrelHltEle[NELE];

Int_t nTrackedEndcapHltEle;
Float_t etaTrackedEndcapHltEle[NELE];
Float_t ptTrackedEndcapHltEle[NELE];
Float_t phiTrackedEndcapHltEle[NELE];
Float_t clusterShapeTrackedEndcapHltEle[NELE];
Float_t hadEmTrackedEndcapHltEle[NELE];
Float_t ecalIsoTrackedEndcapHltEle[NELE];
Float_t hcalIsoTrackedEndcapHltEle[NELE];
Float_t epTrackedEndcapHltEle[NELE];
Float_t dEtaTrackedEndcapHltEle[NELE];
Float_t dPhiTrackedEndcapHltEle[NELE];
Float_t trackIsoTrackedEndcapHltEle[NELE];


Int_t nTracklessHltEle;
Float_t etaTracklessHltEle[NELE];
Float_t ptTracklessHltEle[NELE];
Float_t phiTracklessHltEle[NELE];
Float_t clusterShapeTracklessHltEle[NELE];
Float_t ecalIsoTracklessHltEle[NELE];
Float_t hadEmTracklessHltEle[NELE];
Float_t hcalIsoTracklessHltEle[NELE];

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
recoAnalyzerPtTrackless::recoAnalyzerPtTrackless(const edm::ParameterSet& iConfig):
	trackedSigmaIEIETag(iConfig.getParameter<edm::InputTag>("trackedSigmaIEIE")),
	trackedHadEmTag(iConfig.getParameter<edm::InputTag>("trackedHadEm")),
	trackedEcalIsoTag(iConfig.getParameter<edm::InputTag>("trackedEcalIso")),
	trackedHcalIsoTag(iConfig.getParameter<edm::InputTag>("trackedHcalIso")),
	trackedEpTag(iConfig.getParameter<edm::InputTag>("trackedEp")),
	trackedDetaTag(iConfig.getParameter<edm::InputTag>("trackedDeta")),
	trackedDphiTag(iConfig.getParameter<edm::InputTag>("trackedDphi")),
	trackedTrackIsoTag(iConfig.getParameter<edm::InputTag>("trackedTrackIso")),
	tracklessClusterShapeTag(iConfig.getParameter<edm::InputTag>("tracklessClusterShape")),
	tracklessHadEmTag(iConfig.getParameter<edm::InputTag>("tracklessHadEm")),
	tracklessEcalIsoTag(iConfig.getParameter<edm::InputTag>("tracklessEcalIso")),
	tracklessHcalIsoTag(iConfig.getParameter<edm::InputTag>("tracklessHcalIso")),
	tName(iConfig.getParameter<std::string>("treeName")),
	hltTrackedLegTag(iConfig.getParameter<edm::InputTag>("trackedElectronCollection")),
	hltTracklessLegTag(iConfig.getParameter<edm::InputTag>("tracklessElectronCollection")),
	trackedGenTag(iConfig.getParameter<edm::InputTag>("genTrackedElectronCollection")),
	tracklessGenTag(iConfig.getParameter<edm::InputTag>("genTracklessElectronCollection"))

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   
   tree=fs->make<TTree>(tName.c_str(),"RecoEcalCandidate object information before any trigger filters are applied");
  
   //tracked leg branches
   tree->Branch("nTrackedBarrelHltEle",&nTrackedBarrelHltEle,"nTrackedBarrelHltEle/I");
   tree->Branch("etaTrackedBarrelHltEle",etaTrackedBarrelHltEle,"etaTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("ptTrackedBarrelHltEle",ptTrackedBarrelHltEle,"ptTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("phiTrackedBarrelHltEle",phiTrackedBarrelHltEle,"phiTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("clusterShapeTrackedBarrelHltEle",clusterShapeTrackedBarrelHltEle,"clusterShapeTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("hadEmTrackedBarrelHltEle",hadEmTrackedBarrelHltEle,"hadEmTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("ecalIsoTrackedBarrelHltEle",ecalIsoTrackedBarrelHltEle,"ecalIsoTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("hcalIsoTrackedBarrelHltEle",hcalIsoTrackedBarrelHltEle,"hcalIsoTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("epTrackedBarrelHltEle",epTrackedBarrelHltEle,"epTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("dEtaTrackedBarrelHltEle",dEtaTrackedBarrelHltEle,"dEtaTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("dPhiTrackedBarrelHltEle",dPhiTrackedBarrelHltEle,"dPhiTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");
   tree->Branch("trackIsoTrackedBarrelHltEle",trackIsoTrackedBarrelHltEle,"trackIsoTrackedBarrelHltEle[nTrackedBarrelHltEle]/F");

   tree->Branch("nTrackedEndcapHltEle",&nTrackedEndcapHltEle,"nTrackedEndcapHltEle/I");
   tree->Branch("etaTrackedEndcapHltEle",etaTrackedEndcapHltEle,"etaTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("ptTrackedEndcapHltEle",ptTrackedEndcapHltEle,"ptTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("phiTrackedEndcapHltEle",phiTrackedEndcapHltEle,"phiTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("clusterShapeTrackedEndcapHltEle",clusterShapeTrackedEndcapHltEle,"clusterShapeTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("hadEmTrackedEndcapHltEle",hadEmTrackedEndcapHltEle,"hadEmTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("ecalIsoTrackedEndcapHltEle",ecalIsoTrackedEndcapHltEle,"ecalIsoTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("hcalIsoTrackedEndcapHltEle",hcalIsoTrackedEndcapHltEle,"hcalIsoTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("epTrackedEndcapHltEle",epTrackedEndcapHltEle,"epTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("dEtaTrackedEndcapHltEle",dEtaTrackedEndcapHltEle,"dEtaTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("dPhiTrackedEndcapHltEle",dPhiTrackedEndcapHltEle,"dPhiTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");
   tree->Branch("trackIsoTrackedEndcapHltEle",trackIsoTrackedEndcapHltEle,"trackIsoTrackedEndcapHltEle[nTrackedEndcapHltEle]/F");


   //trackless leg branches
   tree->Branch("nTracklessHltEle",&nTracklessHltEle,"nTracklessHltEle/I");
   tree->Branch("etaTracklessHltEle",etaTracklessHltEle,"etaTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("ptTracklessHltEle",ptTracklessHltEle,"ptTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("phiTracklessHltEle",phiTracklessHltEle,"phiTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("clusterShapeTracklessHltEle",clusterShapeTracklessHltEle,"clusterShapeTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("ecalIsoTracklessHltEle",ecalIsoTracklessHltEle,"ecalIsoTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("hadEmTracklessHltEle",hadEmTracklessHltEle,"hadEmTracklessHltEle[nTracklessHltEle]/F");
   tree->Branch("hcalIsoTracklessHltEle",hcalIsoTracklessHltEle,"hcalIsoTracklessHltEle[nTracklessHltEle]/F");

   //general branches not specifically related to one leg or the other
   tree->Branch("evtNumber",&evtNumber,"evtNumber/l");
   tree->Branch("runNumber",&runNumber,"runNumber/I");

}


recoAnalyzerPtTrackless::~recoAnalyzerPtTrackless()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
recoAnalyzerPtTrackless::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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
	nTrackedBarrelHltEle = 0;
	nTrackedEndcapHltEle = 0;
	
	trackedLegHltRefs.clear();
	tracklessLegHltRefs.clear();

	for(Int_t r=0; r<NELE; r++){
		//set all entries in arrays to zero
		etaTrackedBarrelHltEle[r]=0;
		ptTrackedBarrelHltEle[r]=0;
		phiTrackedBarrelHltEle[r]=0;
		clusterShapeTrackedBarrelHltEle[r]=0;
		hadEmTrackedBarrelHltEle[r]=0;
		ecalIsoTrackedBarrelHltEle[r]=0;
		hcalIsoTrackedBarrelHltEle[r]=0;
		epTrackedBarrelHltEle[r]=0;
		dEtaTrackedBarrelHltEle[r]=0;
		dPhiTrackedBarrelHltEle[r]=0;
		trackIsoTrackedBarrelHltEle[r]=0;

		etaTrackedEndcapHltEle[r]=0;
		ptTrackedEndcapHltEle[r]=0;
		phiTrackedEndcapHltEle[r]=0;
		clusterShapeTrackedEndcapHltEle[r]=0;
		hadEmTrackedEndcapHltEle[r]=0;
		ecalIsoTrackedEndcapHltEle[r]=0;
		hcalIsoTrackedEndcapHltEle[r]=0;
		epTrackedEndcapHltEle[r]=0;
		dEtaTrackedEndcapHltEle[r]=0;
		dPhiTrackedEndcapHltEle[r]=0;
		trackIsoTrackedEndcapHltEle[r]=0;


		etaTracklessHltEle[r]=0;
		ptTracklessHltEle[r]=0;
		phiTracklessHltEle[r]=0;
		clusterShapeTracklessHltEle[r]=0;
		hadEmTracklessHltEle[r]=0;
		ecalIsoTracklessHltEle[r]=0;
		hcalIsoTracklessHltEle[r]=0;
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
recoAnalyzerPtTrackless::beginJob()
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
recoAnalyzerPtTrackless::endJob() 
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
recoAnalyzerPtTrackless::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
recoAnalyzerPtTrackless::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
recoAnalyzerPtTrackless::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
recoAnalyzerPtTrackless::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
recoAnalyzerPtTrackless::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

/*
void recoAnalyzerPtTrackless::InitNewTree(void){

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
void recoAnalyzerPtTrackless::TreeSetSingleElectronVar(const pat::Electron& electron1, int index){

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

void recoAnalyzerPtTrackless::TreeSetSingleElectronVar(const reco::SuperCluster& electron1, int index){

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

void recoAnalyzerPtTrackless::TreeSetDiElectronVar(const pat::Electron& electron1, const reco::SuperCluster& electron2){
  
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
DEFINE_FWK_MODULE(recoAnalyzerPtTrackless);
