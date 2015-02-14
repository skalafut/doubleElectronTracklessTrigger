// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/recoAnalyzerBothMatch
// Class:      recoAnalyzerBothMatch
// 
/**\class recoAnalyzerBothMatch recoAnalyzerBothMatch.cc doubleElectronTracklessTrigger/recoAnalyzerBothMatch/plugins/recoAnalyzerBothMatch.cc

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

class recoAnalyzerBothMatch : public edm::EDAnalyzer {
   public:
      explicit recoAnalyzerBothMatch(const edm::ParameterSet&);
      ~recoAnalyzerBothMatch();

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
		nTrackedHltEle += 1;
	}

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;
	
	//declare const_iterators to maps outside for loop
	forMapIt::const_iterator trackedSigmaIEIEIt, trackedHadEmIt, trackedHcalIsoIt, trackedEcalIsoIt, trackedTrackIsoIt, trackedDphiIt, trackedDetaIt, trackedEpIt;
	for(Int_t j=0; j< nTrackedHltEle; j++){
		etaTrackedHltEle[j] = trackedLegHltRefs[j]->eta();
		ptTrackedHltEle[j] = trackedLegHltRefs[j]->pt();
		phiTrackedHltEle[j] = trackedLegHltRefs[j]->phi();

		//initialize const_iterators to maps inside for loop using find(edm::Ref)
		trackedSigmaIEIEIt = (*trackedSigmaIEIEHandle).find(trackedLegHltRefs[j]);
		clusterShapeTrackedHltEle[j] = trackedSigmaIEIEIt->val;
		trackedHadEmIt = (*trackedHadEmHandle).find(trackedLegHltRefs[j]);
		hadEmTrackedHltEle[j] = (trackedHadEmIt->val)/(ptTrackedHltEle[j]*(TMath::CosH(etaTrackedHltEle[j]) ));
		trackedHcalIsoIt = (*trackedHcalIsoHandle).find(trackedLegHltRefs[j]);
		hcalIsoTrackedHltEle[j] = (trackedHcalIsoIt->val)/ptTrackedHltEle[j];
		trackedEcalIsoIt = (*trackedEcalIsoHandle).find(trackedLegHltRefs[j]);
		ecalIsoTrackedHltEle[j] = (trackedEcalIsoIt->val)/ptTrackedHltEle[j];

		trackedTrackIsoIt = (*trackedTrackIsoHandle).find(trackedLegHltRefs[j]);
		trackIsoTrackedHltEle[j] = (trackedTrackIsoIt->val)/ptTrackedHltEle[j];
		trackedDphiIt = (*trackedDphiHandle).find(trackedLegHltRefs[j]);
		dPhiTrackedHltEle[j] = trackedDphiIt->val;
		trackedDetaIt = (*trackedDetaHandle).find(trackedLegHltRefs[j]);
		dEtaTrackedHltEle[j] = trackedDetaIt->val;
		trackedEpIt = (*trackedEpHandle).find(trackedLegHltRefs[j]);
		epTrackedHltEle[j] = trackedEpIt->val;

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
		if(std::fabs( (getRef(tracklessLegHltObjectsHandle, h))->eta() ) > 2.5 && std::fabs( (getRef(tracklessLegHltObjectsHandle, h))->eta() ) < 3.0){
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

double trackedDrMatchReqr;
double tracklessDrMatchReqr;


TTree * tree;

Int_t nTrackedHltEle;
Float_t etaTrackedHltEle[NELE];
Float_t ptTrackedHltEle[NELE];
Float_t phiTrackedHltEle[NELE];
Float_t clusterShapeTrackedHltEle[NELE];
Float_t hadEmTrackedHltEle[NELE];
Float_t ecalIsoTrackedHltEle[NELE];
Float_t hcalIsoTrackedHltEle[NELE];
Float_t epTrackedHltEle[NELE];
Float_t dEtaTrackedHltEle[NELE];
Float_t dPhiTrackedHltEle[NELE];
Float_t trackIsoTrackedHltEle[NELE];


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
recoAnalyzerBothMatch::recoAnalyzerBothMatch(const edm::ParameterSet& iConfig):
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
	tracklessGenTag(iConfig.getParameter<edm::InputTag>("genTracklessElectronCollection")),
	trackedDrMatchReqr(iConfig.getParameter<double>("trackedDr")),
	tracklessDrMatchReqr(iConfig.getParameter<double>("tracklessDr"))

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;

  
   tree=fs->make<TTree>(tName.c_str(),"RecoEcalCandidate object information before any trigger filters are applied");
  
   //tracked leg branches
   tree->Branch("nTrackedHltEle",&nTrackedHltEle,"nTrackedHltEle/I");
   tree->Branch("etaTrackedHltEle",etaTrackedHltEle,"etaTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("ptTrackedHltEle",ptTrackedHltEle,"ptTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("phiTrackedHltEle",phiTrackedHltEle,"phiTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("clusterShapeTrackedHltEle",clusterShapeTrackedHltEle,"clusterShapeTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("hadEmTrackedHltEle",hadEmTrackedHltEle,"hadEmTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("ecalIsoTrackedHltEle",ecalIsoTrackedHltEle,"ecalIsoTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("hcalIsoTrackedHltEle",hcalIsoTrackedHltEle,"hcalIsoTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("epTrackedHltEle",epTrackedHltEle,"epTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("dEtaTrackedHltEle",dEtaTrackedHltEle,"dEtaTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("dPhiTrackedHltEle",dPhiTrackedHltEle,"dPhiTrackedHltEle[nTrackedHltEle]/F");
   tree->Branch("trackIsoTrackedHltEle",trackIsoTrackedHltEle,"trackIsoTrackedHltEle[nTrackedHltEle]/F");

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


recoAnalyzerBothMatch::~recoAnalyzerBothMatch()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
recoAnalyzerBothMatch::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
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
		clusterShapeTrackedHltEle[r]=0;
		hadEmTrackedHltEle[r]=0;
		ecalIsoTrackedHltEle[r]=0;
		hcalIsoTrackedHltEle[r]=0;
		epTrackedHltEle[r]=0;
		dEtaTrackedHltEle[r]=0;
		dPhiTrackedHltEle[r]=0;
		trackIsoTrackedHltEle[r]=0;

		etaTracklessHltEle[r]=0;
		ptTracklessHltEle[r]=0;
		phiTracklessHltEle[r]=0;
		clusterShapeTracklessHltEle[r]=0;
		hadEmTracklessHltEle[r]=0;
		ecalIsoTracklessHltEle[r]=0;
		hcalIsoTracklessHltEle[r]=0;
	}

	iEvent.getByLabel(trackedGenTag,trackedGenElectronHandle);
	iEvent.getByLabel(tracklessGenTag,tracklessGenElectronHandle);

	edm::OwnVector<reco::Candidate>::const_iterator trackedGenIt = trackedGenElectronHandle->begin(), tracklessGenIt = tracklessGenElectronHandle->begin();

	//gets the tracked leg trigger objects matched to tracked GEN electrons
	GetTrackedTriggerObjects(iEvent, trackedGenIt->eta(), trackedGenIt->phi(), trackedDrMatchReqr);

	//gets the trackless leg trigger objects matched to trackless GEN electrons
	GetMatchedTriggerObjects(iEvent, tracklessGenIt->eta(), tracklessGenIt->phi(), tracklessDrMatchReqr);

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
recoAnalyzerBothMatch::beginJob()
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
recoAnalyzerBothMatch::endJob() 
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
recoAnalyzerBothMatch::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
recoAnalyzerBothMatch::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
recoAnalyzerBothMatch::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
recoAnalyzerBothMatch::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
recoAnalyzerBothMatch::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

/*
void recoAnalyzerBothMatch::InitNewTree(void){

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
void recoAnalyzerBothMatch::TreeSetSingleElectronVar(const pat::Electron& electron1, int index){

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

void recoAnalyzerBothMatch::TreeSetSingleElectronVar(const reco::SuperCluster& electron1, int index){

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

void recoAnalyzerBothMatch::TreeSetDiElectronVar(const pat::Electron& electron1, const reco::SuperCluster& electron2){
  
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
DEFINE_FWK_MODULE(recoAnalyzerBothMatch);
