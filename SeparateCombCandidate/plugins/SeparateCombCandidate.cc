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
	  bool isDuplicateRef(reco::CandidateBaseRef& refObject,std::unique_ptr<reco::RecoEcalCandidateRefVector>& ptrToRefColl){
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

	  void findAndSaveRef(edm::Handle<std::vector<reco::RecoEcalCandidate> >& inputParentHandle, edm::Handle<std::vector<reco::CompositeCandidate> >& inputMomHandle, std::unique_ptr<reco::RecoEcalCandidateRefVector>& ptrToOutputColl, std::string& dauRole){

		  for(std::vector<reco::CompositeCandidate>::const_iterator momIt = inputMomHandle->begin(); momIt != inputMomHandle->end(); momIt++){
			  //get a Ref to a daughter via momIt->daughter()->masterClone()
			  //then find the matching (pt, eta, phi) object in inputParentHandle, and
			  //save a reference to the object into the appropriate output collection via
			  //getRef(inputParentHandle, index number) 
#ifdef DEBUG
			  std::cout<<"looping over CompositeCandidate objects"<<std::endl;
#endif
			  if((momIt->daughter(dauRole.c_str()))->hasMasterClone() ){
#ifdef DEBUG
				  std::cout<<"found "<< dauRole <<" daughter with a master clone"<<std::endl;
#endif
				  reco::CandidateBaseRef dauRef = (momIt->daughter(dauRole.c_str()))->masterClone();
#ifdef DEBUG
				  std::cout<<"made a reference obj to a "<< dauRole << " daughter"<<std::endl;
#endif
				  for(unsigned int h=0; h<inputParentHandle->size(); h++){
					  if(dauRef->pt() == (getRef(inputParentHandle, h))->pt() ){
						  if(dauRef->eta() == (getRef(inputParentHandle, h))->eta() ){
							  if(dauRef->phi() == (getRef(inputParentHandle, h))->phi() ){
								  if(!isDuplicateRef(dauRef,ptrToOutputColl) ){
									  ptrToOutputColl->push_back( getRef(inputParentHandle, h) );
								  }//end duplicate check
							  }//end filter on phi

						  }//end filter on eta

					  }//end filter on pt

				  }//end loop over objects in inputParentHandle

			  }//end requirement that a master clone exists

		  }//end loop over objects in inputMomHandle


	  }//end findAndSaveRef()

	
   private:
      virtual void beginJob() override;
      virtual void produce(edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;
      
      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
 
      // ----------member data ---------------------------
	  edm::EDGetTokenT<std::vector<reco::CompositeCandidate> > momToken;
	  edm::EDGetTokenT<std::vector<reco::RecoEcalCandidate> > momParentOneToken;
	  edm::EDGetTokenT<std::vector<reco::RecoEcalCandidate> > momParentTwoToken;
	  
	  edm::Handle<std::vector<reco::CompositeCandidate> > momIn;
	  edm::Handle<std::vector<reco::RecoEcalCandidate> > momParentOneIn;	//for trackless leg RECs
	  edm::Handle<std::vector<reco::RecoEcalCandidate> > momParentTwoIn;	//for tracked leg RECs
	
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
	momToken( consumes<std::vector<reco::CompositeCandidate> >(iConfig.getParameter<edm::InputTag>("zedLabel"))),
	momParentOneToken( consumes<std::vector<reco::RecoEcalCandidate> >(iConfig.getParameter<edm::InputTag>("tracklessHltEle"))),
	momParentTwoToken( consumes<std::vector<reco::RecoEcalCandidate> >(iConfig.getParameter<edm::InputTag>("trackedHltEle"))),
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
   
   //momToken = consumes<std::vector<reco::CompositeCandidate> >(iConfig.getParameter<edm::InputTag>("zedLabel"));
   //momParentOneToken = consumes<std::vector<reco::RecoEcalCandidate> >(iConfig.getParameter<edm::InputTag>("tracklessHltEle"));
   //momParentTwoToken = consumes<std::vector<reco::RecoEcalCandidate> >(iConfig.getParameter<edm::InputTag>("trackedHltEle"));
   
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

#ifdef DEBUG
   std::cout<<"entered daughter producer code"<<std::endl;
#endif

   //read collection of reco::CompositeCandidate objects from iEvent
   iEvent.getByToken(momToken, momIn);
   iEvent.getByToken(momParentOneToken, momParentOneIn);
   iEvent.getByToken(momParentTwoToken, momParentTwoIn);

#ifdef DEBUG
   std::cout<<"made handles to input collections"<<std::endl;
#endif

   //create empty output collections, one for each daughter, and pointers to each collection
   //std::auto_ptr<reco::RecoEcalCandidateRefVector> daughterOneRefColl(new reco::RecoEcalCandidateRefVector );	//trackless collection
   //std::auto_ptr<reco::RecoEcalCandidateRefVector> daughterTwoRefColl(new reco::RecoEcalCandidateRefVector );	//tracked collection
   auto dauOneRefCands = std::make_unique<reco::RecoEcalCandidateRefVector>();
   auto dauTwoRefCands = std::make_unique<reco::RecoEcalCandidateRefVector>();

   std::string roleOne = "tracklessRecoEle";
   std::string roleTwo = "trackedRecoEle";
   findAndSaveRef(momParentOneIn, momIn, dauOneRefCands, roleOne); 
   findAndSaveRef(momParentTwoIn, momIn, dauTwoRefCands, roleTwo); 
  
#ifdef DEBUG
   std::cout<<"about to put daughter collections into root file"<<std::endl;
#endif
   //now put the two collections of Refs to daughter particles into the event
   //iEvent.put(daughterOneRefColl, daughterOneCollection);
   //iEvent.put(daughterTwoRefColl, daughterTwoCollection);
   iEvent.put(std::move(dauOneRefCands), daughterOneCollection);
   iEvent.put(std::move(dauTwoRefCands), daughterTwoCollection);



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
