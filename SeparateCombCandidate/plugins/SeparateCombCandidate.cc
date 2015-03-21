// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/SeparateCombCandidate
// Class:      SeparateCombCandidate
// 
/**\class SeparateCombCandidate SeparateCombCandidate.cc doubleElectronTracklessTrigger/SeparateCombCandidate/plugins/SeparateCombCandidate.cc

 Description: [one line class summary]

 this module takes a collection of reco::CompositeCandidate objects and parses each object into its
 two daughters.  Two vectors of edm::Ref objects pointing to reco::RecoEcalCandidate objects are produced
 and saved to the input .root file.  These two collections can then be used to access kinematic and isolation
 information from the daughters.

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Sean Kalafut
//         Created:  Thu, 19 Feb 2015 15:29:04 GMT
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
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Common/interface/getRef.h"

#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateFwd.h"
//#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateIsolation.h"
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

//#define DEBUG

//
// class declaration
//

class SeparateCombCandidate : public edm::EDProducer {
   public:
      explicit SeparateCombCandidate(const edm::ParameterSet&);
      ~SeparateCombCandidate();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
	  
	  //check if a Ref with pt, eta, and phi already exists in a collection of Ref objects
	  //return false if the Ref object does not exist in the collection
	  //return true if the Ref object does exist in the collection of Ref objects
	  bool isDuplicateRef(reco::CandidateBaseRef& refObject,std::auto_ptr<reco::RecoEcalCandidateRefVector>& ptrToRefColl){
#ifdef DEBUG
		  std::cout<<"in isDuplicateRef()"<<std::endl;
		  std::cout<<"about to check if RefVector size = 0"<<std::endl;
#endif
		  if(ptrToRefColl->size()==0) return false;
		  for(unsigned int i=0; i<ptrToRefColl->size(); i++){
#ifdef DEBUG
			  std::cout<<"about to check if refObject is a duplicate"<<std::endl;
			  std::cout<<"RefVector size="<<"\t"<< ptrToRefColl->size() <<std::endl;
#endif
			  if(refObject->pt()==(ptrToRefColl->at(i))->pt() || refObject->eta()==(ptrToRefColl->at(i))->eta() || refObject->phi()==(ptrToRefColl->at(i))->phi() ) return true;
		  }//end loop over all elements in RecoEcalCandidateRefVector
		  return false;
	  }//end isDuplicateRef() 

	
   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
 
      // ----------member data ---------------------------
	  edm::EDGetTokenT<std::vector<reco::CompositeCandidate>> momToken;
	  edm::EDGetTokenT<std::vector<reco::RecoEcalCandidate>> momParentOneToken;
      edm::EDGetTokenT<std::vector<reco::RecoEcalCandidate>> momParentTwoToken;
	
   	  std::string daughterOneCollection;
	  std::string daughterTwoCollection;
 
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
SeparateCombCandidate::SeparateCombCandidate(const edm::ParameterSet& iConfig):
	daughterOneCollection(iConfig.getParameter<std::string>("tracklessEleCollectionName")),
	daughterTwoCollection(iConfig.getParameter<std::string>("trackedEleCollectionName"))
{
   //register your products
/* Examples
   produces<ExampleData2>();

   //if do put with a label
   produces<ExampleData2>("label");
 
   //if you want to put into the Run
   produces<ExampleData2,InRun>();
*/
   
   momToken = consumes<std::vector<reco::CompositeCandidate>>(iConfig.getParameter<edm::InputTag>("zedLabel"));
   momParentOneToken = consumes<std::vector<reco::RecoEcalCandidate>>(iConfig.getParameter<edm::InputTag>("tracklessHltEle"));
   momParentTwoToken = consumes<std::vector<reco::RecoEcalCandidate>>(iConfig.getParameter<edm::InputTag>("trackedHltEle"));
   //daughterOneCollection = iConfig.getParameter<std::string>("tracklessEleCollectionName");
   //daughterTwoCollection = iConfig.getParameter<std::string>("trackedEleCollectionName");
   
   //register the two collections of products - std::vector<edm::Refs to RecoEcalCandidate objects> (daughters of Z)
   produces<reco::RecoEcalCandidateRefVector>(daughterOneCollection);
   produces<reco::RecoEcalCandidateRefVector>(daughterTwoCollection);


}


SeparateCombCandidate::~SeparateCombCandidate()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called to produce the data  ------------
void
SeparateCombCandidate::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   //std::cout<<"entered daughter producer code"<<std::endl;

   //read collection of reco::CompositeCandidate objects from iEvent
   Handle<std::vector<reco::CompositeCandidate> > momIn;
   iEvent.getByToken(momToken, momIn);

   Handle<std::vector<reco::RecoEcalCandidate> > momParentOneIn;	//for trackless leg RECs
   iEvent.getByToken(momParentOneToken, momParentOneIn);

   Handle<std::vector<reco::RecoEcalCandidate> > momParentTwoIn;	//for tracked leg RECs
   iEvent.getByToken(momParentTwoToken, momParentTwoIn);

   //std::cout<<"made handles to input collections"<<std::endl;

   //create empty output collections, one for each daughter, and pointers to each collection
   std::auto_ptr<reco::RecoEcalCandidateRefVector> daughterOneRefColl(new reco::RecoEcalCandidateRefVector );	//trackless collection
   std::auto_ptr<reco::RecoEcalCandidateRefVector> daughterTwoRefColl(new reco::RecoEcalCandidateRefVector );	//tracked collection

   
   for(std::vector<reco::CompositeCandidate>::const_iterator momIt = momIn->begin(); momIt != momIn->end(); momIt++){
	   //get a Ref to a daughter via momIt->daughter()->masterClone()
	   //then find the matching (pt, eta, phi) object in momParent(One or Two)In handles, and
	   //save a reference to the object into the appropriate output collection via
	   //getRef(momParent(One or Two)In, index number) 
	   //std::cout<<"looping over CompositeCandidate objects"<<std::endl;
	   if((momIt->daughter("tracklessRecoEle"))->hasMasterClone() ){
		   //std::cout<<"found tracklessRecoEle daughter with a master clone"<<std::endl;
		   reco::CandidateBaseRef dauOneRef = (momIt->daughter("tracklessRecoEle"))->masterClone();
		   //std::cout<<"made a reference obj to a trackless daughter"<<std::endl;
		   for(unsigned int h=0; h<momParentOneIn->size(); h++){
			   if(dauOneRef->pt() == (getRef(momParentOneIn, h))->pt() ){
				   if(dauOneRef->eta() == (getRef(momParentOneIn, h))->eta() ){
					   if(dauOneRef->phi() == (getRef(momParentOneIn, h))->phi() ){
						   if(!isDuplicateRef(dauOneRef,daughterOneRefColl) ){
							   daughterOneRefColl->push_back( getRef(momParentOneIn, h) );
						   }//end duplicate check
					   }//end filter on phi

				   }//end filter on eta

			   }//end filter on pt

		   }//end loop over objects in momParentOneIn

	   }//end requirement that a master clone exists

	   if((momIt->daughter("trackedRecoEle"))->hasMasterClone() ){
		   //std::cout<<"found trackedRecoEle daughter with a master clone"<<std::endl;
		   reco::CandidateBaseRef dauTwoRef = (momIt->daughter("trackedRecoEle"))->masterClone();
		   for(unsigned int m=0; m<momParentTwoIn->size(); m++){
			   if(dauTwoRef->pt() == (getRef(momParentTwoIn, m))->pt() ){
				   if(dauTwoRef->eta() == (getRef(momParentTwoIn, m))->eta() ){
					   if(dauTwoRef->phi() == (getRef(momParentTwoIn, m))->phi() ){
						   if(!isDuplicateRef(dauTwoRef,daughterTwoRefColl) ){
							   daughterTwoRefColl->push_back( getRef(momParentTwoIn, m) );
						   }//end duplicate check
					   }//end filter on phi

				   }//end filter on eta

			   }//end filter on pt

		   }//end loop over objects in momParentTwoIn

	   }//end requirement that a master clone exists
	
   }//end loop over all CompositeCandidate objects in the event


   //std::cout<<"about to put daughter collections into root file"<<std::endl;
   //now put the two collections of Refs to daughter particles into the event
   iEvent.put(daughterOneRefColl, daughterOneCollection);
   iEvent.put(daughterTwoRefColl, daughterTwoCollection);



/* This is an event example
   //Read 'ExampleData' from the Event
   //use getByToken()
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);

   //Use the ExampleData to create an ExampleData2 which 
   // is put into the Event
   std::unique_ptr<ExampleData2> pOut(new ExampleData2(*pIn));	makes a copy of the collection which pIn points to
   or
   std::unique_ptr<ExampleData2> pOut(new ExampleData2() );
   combRecoEle->daughter(0);
   pOut->push_back(ExampleData2 object);
   iEvent.put(std::move(pOut));
*/

/* this is an EventSetup example
   //Read SetupData from the SetupRecord in the EventSetup
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
*/
 
}

// ------------ method called once each job just before starting event loop  ------------
void 
SeparateCombCandidate::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
SeparateCombCandidate::endJob() {
}

// ------------ method called when starting to processes a run  ------------
/*
void
SeparateCombCandidate::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
void
SeparateCombCandidate::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
void
SeparateCombCandidate::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
SeparateCombCandidate::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SeparateCombCandidate::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SeparateCombCandidate);
