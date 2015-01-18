// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/doubleEleAODAnalyzer
// Class:      doubleEleAODAnalyzer
// 
/**\class doubleEleAODAnalyzer doubleEleAODAnalyzer.cc doubleElectronTracklessTrigger/doubleEleAODAnalyzer/plugins/doubleEleAODAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Sean Kalafut
//         Created:  Sun, 11 Jan 2015 23:00:30 GMT
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

#include "DataFormats/EgammaReco/interface/SuperCluster.h"
//#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EgammaReco/interface/ClusterShape.h"
#include "DataFormats/EgammaReco/interface/ClusterShapeFwd.h"
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaCandidates/interface/Electron.h"
//#include "DataFormats/EgammaCandidates/interface/ElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"

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


//
// class declaration
//

class doubleEleAODAnalyzer : public edm::EDAnalyzer {
   public:
      explicit doubleEleAODAnalyzer(const edm::ParameterSet&);
      ~doubleEleAODAnalyzer();

	  static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

	  bool booked(const std::string histName) const { return hists_.find(histName.c_str())!=hists_.end(); };
      bool bookedTwo(const std::string histName) const { return histsTwo_.find(histName.c_str())!=histsTwo_.end(); };
      bool bookedThree(const std::string histName) const { return histsThree_.find(histName.c_str())!=histsThree_.end(); };

      /// fill histogram if it had been booked before
      void fill(const std::string histName, double value) const { if(booked(histName.c_str())) hists_.find(histName.c_str())->second->Fill(value); };
      void fillTwo(const std::string histName, double valX, double valY) const{  if(bookedTwo(histName.c_str())) histsTwo_.find(histName.c_str())->second->Fill(valX, valY); };
      void fillThree(const std::string histName, double valX, double valY, double valZ) const{  if(bookedThree(histName.c_str())) histsThree_.find(histName.c_str())->second->Fill(valX, valY, valZ); };



	  unsigned int addToPtSortedVector(std::vector<double>& genElePts,double& genPT){
		  //add the double value named genPT to the vector genElePts such that the first element in genElePts is the smallest element in the vector, and
		  //the last element in genElePts is the largest element in the vector
		  //return the element # where genPT is placed
		  unsigned int vectorSize = genElePts.size();

		  if(genElePts.size() < 1){
			  //if genElePts is empty when it is passed to this function
			  genElePts.push_back(genPT);
			  return 0;
		  }

		  //if vectorSize >= 1, then loop over all elements of the genElePts vector, insert genPT such that genElePts remains pT sorted, and
		  //return the index where genPT was added.  This index will be used by the vectors which store gen electron eta and phi.
		  unsigned int i=0;
		  for(std::vector<double>::iterator iT = genElePts.begin(); iT != genElePts.end() ; iT++){
			  if(genPT< *iT){
				  genElePts.insert(iT, genPT);
				  return i;
			  }

			  //if genPT is > any element currently in genElePts
			  if(i == (vectorSize -1) ){
				  genElePts.push_back(genPT);
				  return (i+1);
			  }

			  i++;	//if genPT is not less than the current element pointed to by the iterator iT, then increase i by one and keep looking for the appropriate place to insert genPT

		  }//end for loop

		  return 0;

	  }//end addToPtSortedVector()	


	  void resetCounters(){
		  //reset all of the private member vars which are saved to TTree to zero
		  gen_trackless_pT_=-1;	//pT of gen electron in trackless EE
		  gen_trackless_eta_=-7;	//eta of gen electron in trackless EE
		  gen_trackless_phi_=-7;	//phi of gen electron in trackless EE
		  gen_tracked_pT_=-1;	//pT of gen electron in tracked ECAL
		  gen_tracked_eta_=-7;	//eta of gen electron in tracked ECAL
		  gen_tracked_phi_=-7;	//phi of gen electron in tracked ECAL
		  genTriggeredEvent_ = -1;
		  
		  //dilepton mass of the two GEN electrons.
		  //non-negative only if both electrons have Z boson mother, the tracked ele has pT > 27, and the untracked ele has pT > 15
		  genMLL_ = -1;
		  
		  reco_tracked_pT_=-1;
		  reco_tracked_eta_=-7;
		  reco_tracked_phi_=-7;
		  reco_untracked_pT_=-1;
		  reco_untracked_eta_=-7;
		  reco_untracked_phi_=-7;
		  reco_mLL_ = -1;

	  }


   private:
      virtual void beginJob() override;
	  virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
	  virtual void endJob() override;

	  std::map<std::string,TH1D*> hists_;
	  std::map<std::string,TH2D*> histsTwo_;
	  std::map<std::string,TH3D*> histsThree_;

	  TTree * tree;

	  //gen lepton vars going into TTree
	  double gen_trackless_pT_;	//pT of gen electron in trackless EE
	  double gen_trackless_eta_;	//eta of gen electron in trackless EE
	  double gen_trackless_phi_;	//phi of gen electron in trackless EE
	  double gen_tracked_pT_;	//pT of gen electron in tracked ECAL
	  double gen_tracked_eta_;	//eta of gen electron in tracked ECAL 
	  double gen_tracked_phi_;	//phi of gen electron in tracked ECAL 
	  double genTriggeredEvent_;	// equals +1 for events which should have fired trackless and tracked legs of trigger based on GEN lvl info, equals -1 otherwise

	  //dilepton mass of the two GEN electrons.
	  //non-negative only if both electrons have Z boson mother, the tracked ele has pT > 27, and the untracked ele has pT > 15
	  double genMLL_;

	  //variables corresponding to RECO GsfElectron (tracked) and PFSuperCluster (untracked) objects which
	  //are matched to GEN electron objects which meet the GEN lvl trigger requirements (mother is Z, tracked pT > 27, untracked pT > 15)
	  //and the two GEN electrons have an invariant mass btwn 60 and 120 GeV 
	  double reco_tracked_pT_;
	  double reco_tracked_eta_;
	  double reco_tracked_phi_;
	  double reco_untracked_pT_;
	  double reco_untracked_eta_;
	  double reco_untracked_phi_;

	  //dilepton mass of the RECO Gsf electron and EE supercluster
	  //non-negative only if genTriggeredEvent_ > 0, and genMLL_ btwn 60 and 120 GeV
	  double reco_mLL_;



      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
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
doubleEleAODAnalyzer::doubleEleAODAnalyzer(const edm::ParameterSet& iConfig)

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   
   hists_["gsfElectronDeltaR"]=fs->make<TH1D>("gsfElectronDeltaR","#DeltaR gsfElectron to GEN tracked electron with pT > 27; #DeltaR;",100, 0., 0.3);
   hists_["superclusterDeltaR"]=fs->make<TH1D>("superclusterDeltaR","#DeltaR supercluster to GEN trackless electron with pT > 15; #DeltaR;",100, 0., 0.6);
   
   tree=fs->make<TTree>("doubleEleTrigger","Summary of trackless double electron trigger event info");
   tree->Branch("gen_trackless_eta_",&gen_trackless_eta_,"gen_trackless_eta_/D");
   tree->Branch("gen_trackless_pT_",&gen_trackless_pT_,"gen_trackless_pT_/D");
   tree->Branch("gen_trackless_phi_",&gen_trackless_phi_,"gen_trackless_phi_/D");
   tree->Branch("gen_tracked_eta_",&gen_tracked_eta_,"gen_tracked_eta_/D");
   tree->Branch("gen_tracked_pT_",&gen_tracked_pT_,"gen_tracked_pT_/D");
   tree->Branch("gen_tracked_phi_",&gen_tracked_phi_,"gen_tracked_phi_/D");
   tree->Branch("genTriggeredEvent_",&genTriggeredEvent_,"genTriggeredEvent_/D");
   tree->Branch("genMLL_",&genMLL_,"genMLL_/D");

   tree->Branch("reco_tracked_pT_",&reco_tracked_pT_,"reco_tracked_pT_/D");
   tree->Branch("reco_tracked_eta_",&reco_tracked_eta_,"reco_tracked_eta_/D");
   tree->Branch("reco_tracked_phi_",&reco_tracked_phi_,"reco_tracked_phi_/D");
   tree->Branch("reco_untracked_pT_",&reco_untracked_pT_,"reco_untracked_pT_/D");
   tree->Branch("reco_untracked_eta_",&reco_untracked_eta_,"reco_untracked_eta_/D");
   tree->Branch("reco_untracked_phi_",&reco_untracked_phi_,"reco_untracked_phi_/D");
   tree->Branch("reco_mLL_",&reco_mLL_,"reco_mLL_/D");


}


doubleEleAODAnalyzer::~doubleEleAODAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
doubleEleAODAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;

   resetCounters();

   InputTag genParticleTag("genParticles","","SIM");
   Handle<std::vector<reco::GenParticle> > genPart;
   iEvent.getByLabel(genParticleTag, genPart);

   //std::cout<<"declared and initialized handle object to reco::GenParticle collection"<<std::endl;

   double gPt=0;

   //the last two elements in these vectors represent the leading (last element) and subleading (2nd to last element) GEN electrons
   std::vector<double> genElectronPTs;
   std::vector<double> genElectronEtas;
   std::vector<double> genElectronPhis;

   for(std::vector<reco::GenParticle>::const_iterator genIt=genPart->begin(); genIt != genPart->end(); genIt++){

	   //it seems each of the gen electrons and positrons only have 1 mother
	   if( std::fabs(genIt->pdgId()) == 11 && std::fabs(genIt->mother(0)->pdgId() ) == 23 ){
		   gPt = genIt->pt();
		   addToPtSortedVector(genElectronPTs,gPt);	//the last element in genElectronPTs is the largest element in the vector
	   }//end filter which saves kinematic info for GEN electrons and positrons which came from a Z decay 

   }//end loop over GenParticle

   unsigned int length = genElectronPTs.size();
   if(length < 2){
	   tree->Fill();
	   return;
   }

   //fill genElectronEtas and Phis vectors with correct content
   //element #i in genElectronPTs, genElectronEtas, and genElectronPhis correspond to one particular gen electron or positron from a Z decay
   unsigned int index = 0;
   for(std::vector<reco::GenParticle>::const_iterator genIt=genPart->begin(); genIt != genPart->end(); genIt++){
	   if(index == length) break;
	   if( std::fabs(genIt->pdgId()) == 11 && std::fabs(genIt->mother(0)->pdgId() ) == 23 && genIt->pt() == genElectronPTs[index]){
		   genElectronEtas.push_back(genIt->eta());
		   genElectronPhis.push_back(genIt->phi());
		   index += 1;
	   }
   }//end loop over GenParticle

   //now I have the pT, eta, and phi of the two leading GEN electrons which came from a Z boson (no dilepton mass requirement enforced)

   //see if the event contains the two necessary GEN electrons/positrons from a Z decay to fire the trigger 
   bool haveTracklessEleCand = false;
   unsigned int tracklessEleIndex = 0;
   for(unsigned int i=0; i<length ; i++){
	   //see if the event contains a trackless EE gen electron which came from a Z boson with pT > 15.0
	   if(genElectronPTs[i] > 15.0 && std::fabs(genElectronEtas[i]) >= 2.5 && std::fabs(genElectronEtas[i]) < 3.0){
		   haveTracklessEleCand = true;
		   tracklessEleIndex += i;
		   break;
	   }
   }
   for(unsigned int i=0; i<length ; i++){
	   //see if the event contains a tracked gen electron which came from a Z boson with pT > 27.0
	   if(genElectronPTs[i] > 27.0 && std::fabs(genElectronEtas[i]) < 2.5 && haveTracklessEleCand ){
		   gen_tracked_pT_ = genElectronPTs[i];	//save the pT, eta, and phi of the tracked gen electron to calculate M_ee
		   gen_tracked_eta_ = genElectronEtas[i];
		   gen_tracked_phi_ = genElectronPhis[i];
		   gen_trackless_pT_ = genElectronPTs[tracklessEleIndex];
		   gen_trackless_eta_ = genElectronEtas[tracklessEleIndex];
		   gen_trackless_phi_ = genElectronPhis[tracklessEleIndex];
		   genTriggeredEvent_ = 1.0;
		   double mLLSqd = 2*gen_tracked_pT_*gen_trackless_pT_*(TMath::CosH(gen_tracked_eta_ - gen_trackless_eta_) - TMath::Cos(gen_tracked_phi_ - gen_trackless_phi_)  );
		   if(mLLSqd > 0) genMLL_ = TMath::Sqrt(mLLSqd);
		   break;
	   }
   }

   if(genTriggeredEvent_ ==1 && genMLL_ > 60. && genMLL_ < 120.){
	   //save the pT, eta, and phi of the GsfElectron and Supercluster object which are matched
	   //to the two gen electrons (in events where the two GEN electrons have an appropriate dilepton mass)

	   //load GsfElectron and EE Supercluster collections
	   InputTag gsfEleTag("gsfElectrons","","RECO");
	   Handle<std::vector<reco::GsfElectron> > gsfEle;
	   iEvent.getByLabel(gsfEleTag, gsfEle);

	   InputTag eeSCTag("particleFlowSuperClusterECAL","particleFlowSuperClusterECALEndcapWithPreshower","RECO");
	   Handle<std::vector<reco::SuperCluster> > eeSC;
	   iEvent.getByLabel(eeSCTag, eeSC);

	   //loop over all GsfElectrons and EE Superclusters, calculate dR btwn these objects and their GEN correspondents, and
	   //save the pT, eta, and phi of the highest pT matching GsfElectron and EE Supercluster to the TTree
	   if(gsfEle.isValid() && eeSC.isValid() ){
		   //vectors to identify the highest pT SC and gsfElectron matched to the GEN electrons
		   std::vector<double> scPt;
		   std::vector<double> gsfPt;

		   //deltaR requirements for matching gsf electrons and EE superclusters to GEN electrons
		   double maxGsfDR = 0.05;
		   double maxSCDR = 0.1;

		   for(std::vector<reco::GsfElectron>::const_iterator gsfIt=gsfEle->begin(); gsfIt != gsfEle->end(); gsfIt++){
			   double dR = deltaR(gsfIt->eta(), gsfIt->phi(), gen_tracked_eta_, gen_tracked_phi_);
			   fill("gsfElectronDeltaR", dR);
			   double elePt = gsfIt->pt();
			   if(dR <= maxGsfDR) addToPtSortedVector(gsfPt, elePt);
		   }//end first loop over gsf electrons

		   //use this loop to save the eta, pT, and phi of the highest pT gsf electron which is matched
		   //to a GEN tracked electron 
		   for(std::vector<reco::GsfElectron>::const_iterator gsfIt=gsfEle->begin(); gsfIt != gsfEle->end(); gsfIt++){
			   if(gsfPt.size() < 1) break;
			   if(gsfIt->pt() == gsfPt[gsfPt.size()-1]){
				   //found the highest pT gsf electron which is matched to a GEN tracked electron
				   reco_tracked_pT_ = gsfIt->pt();
				   reco_tracked_eta_ = gsfIt->eta();
				   reco_tracked_phi_ = gsfIt->phi();
				   break;
			   }
		   }//end second loop over gsf electrons to save matching gsf electron pT, eta, and phi

		   for(std::vector<reco::SuperCluster>::const_iterator eeSCIt=eeSC->begin(); eeSCIt != eeSC->end(); eeSCIt++){
			   if(std::fabs(eeSCIt->eta() ) >= 2.5 && std::fabs(eeSCIt->eta() ) < 3.0){
				   double dR = deltaR(eeSCIt->eta(), eeSCIt->phi(), gen_trackless_eta_, gen_trackless_phi_);
				   fill("superclusterDeltaR", dR);
				   double untrkElePt = (eeSCIt->energy()/TMath::CosH(eeSCIt->eta()) );
				   if(dR <= maxSCDR) addToPtSortedVector(scPt, untrkElePt);
			   }

		   }//end first loop over EE superclusters

		   //use this loop to save the eta, pT, and phi of the highest pT EE supercluster which
		   //is matched to a GEN trackless EE electron
		   for(std::vector<reco::SuperCluster>::const_iterator eeSCIt=eeSC->begin(); eeSCIt != eeSC->end(); eeSCIt++){
			   if(scPt.size() < 1) break;
			   if(std::fabs(eeSCIt->eta() ) >= 2.5 && std::fabs(eeSCIt->eta() ) < 3.0){
				   double clstPt = (eeSCIt->energy()/TMath::CosH(eeSCIt->eta()) );
				   if(clstPt == scPt[scPt.size()-1]){
					   //found the highest pT EE supercluster which is matched to a GEN trackless EE electron
					   reco_untracked_pT_ = clstPt;
					   reco_untracked_eta_ = eeSCIt->eta();
					   reco_untracked_phi_ = eeSCIt->phi();
					   break;
				   }
			   }

		   }//end second loop over EE superclusters to save pT, eta, and phi of matched EE supercluster

		   //calculate and save the reco dilepton mass if a matching Gsf electron and EE supercluster were found
		   if(reco_tracked_pT_ > 0 && reco_untracked_pT_ > 0){
			   double reco_mLLSqd = 2*reco_tracked_pT_*reco_untracked_pT_*(TMath::CosH(reco_tracked_eta_ - reco_untracked_eta_) - TMath::Cos(reco_tracked_phi_ - reco_untracked_phi_)  );
			   if(reco_mLLSqd > 0) reco_mLL_ = TMath::Sqrt(reco_mLLSqd);
		   }//end requirement that matching Gsf electron and EE supercluster objects were found

	   }//end requirement that the gsfelectron and EE supercluster collections exist in the event

   }//end if(genTriggeredEvent_ == 1 && 60 < genMLL_ < 120) 


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
doubleEleAODAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
doubleEleAODAnalyzer::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
doubleEleAODAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
doubleEleAODAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
doubleEleAODAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
doubleEleAODAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
doubleEleAODAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(doubleEleAODAnalyzer);
