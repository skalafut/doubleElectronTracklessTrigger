// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer
// Class:      doubleEleTracklessAnalyzer
// 
/**\class doubleEleTracklessAnalyzer doubleEleTracklessAnalyzer.cc doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/plugins/doubleEleTracklessAnalyzer.cc

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


//
// class declaration
//

class doubleEleTracklessAnalyzer : public edm::EDAnalyzer {
   public:
      explicit doubleEleTracklessAnalyzer(const edm::ParameterSet&);
      ~doubleEleTracklessAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
      

	  void incrementTotalNumEvents(){
		  totalNumEvents = totalNumEvents + 1.0;
	  }
	  double getTotalNumEvents(){
		  return totalNumEvents;
	  }

	  void incrementNumTriggeredEvents(){
		  numTriggeredEvents = numTriggeredEvents + 1.0;
	  }
	  double getNumTriggeredEvents(){
		  return numTriggeredEvents;
	  }

	  void incrementEfficiencyDenominator(){
		  efficiencyDenominator = efficiencyDenominator + 1.0;
	  }
	  double getEfficiencyDenominator(){
		  return efficiencyDenominator;
	  }


   //private:
	  //TFile *tree_file;
	  //std::string foutName;
      //void InitNewTree(void);

   //public:
      bool booked(const std::string histName) const { return hists_.find(histName.c_str())!=hists_.end(); };
      bool bookedTwo(const std::string histName) const { return histsTwo_.find(histName.c_str())!=histsTwo_.end(); };
      bool bookedThree(const std::string histName) const { return histsThree_.find(histName.c_str())!=histsThree_.end(); };

      /// fill histogram if it had been booked before
      void fill(const std::string histName, double value) const { if(booked(histName.c_str())) hists_.find(histName.c_str())->second->Fill(value); };
      void fillTwo(const std::string histName, double valX, double valY) const{  if(bookedTwo(histName.c_str())) histsTwo_.find(histName.c_str())->second->Fill(valX, valY); };
      void fillThree(const std::string histName, double valX, double valY, double valZ) const{  if(bookedThree(histName.c_str())) histsThree_.find(histName.c_str())->second->Fill(valX, valY, valZ); };


      //this takes three 2D histograms, divides two of them, and places the contents of the two divided histogram into the histo (histNameReturned) that called Divide
      void divideTwo(const std::string histNameNumerator, const std::string histNameDenominator, const std::string histNameReturned) const{
	      if(bookedTwo(histNameNumerator.c_str()) && bookedTwo(histNameDenominator.c_str()) && bookedTwo(histNameReturned.c_str()) ){
		      //if all three 2D histos have been declared, then call divide on histNameReturned and pass histNameNumerator, histNameDenominator into Divide as arguments
		      histsTwo_.find(histNameReturned.c_str())->second->Divide( histsTwo_.find(histNameNumerator.c_str())->second, histsTwo_.find(histNameDenominator.c_str())->second );

	      }

      }

      //this gets the number of X axis bins from a 1D, 2D, or 3D histo
      int getXBins(const std::string histName) const {
	      if(bookedTwo(histName.c_str()) ){
		      int binsX = histsTwo_.find(histName.c_str() )->second->GetNbinsX();
		      return binsX;
	      }

	      if(booked(histName.c_str()) ){
		      int binsX = hists_.find(histName.c_str() )->second->GetNbinsX();
		      return binsX;
	      }

	      if(bookedThree(histName.c_str()) ){
		      int binsX = histsThree_.find(histName.c_str() )->second->GetNbinsX();
		      return binsX;
	      }


	      int failsafe = 0;
	      return failsafe;
      }//end getXBins(histName) 

      //this gets the number of Y axis bins from a 2D or 3D histo
      int getYBins(const std::string histName) const {
	      if(bookedTwo(histName.c_str()) ){
		      int binsY = histsTwo_.find(histName.c_str() )->second->GetNbinsY();
		      return binsY;
	      }

	      if(bookedThree(histName.c_str()) ){
		      int binsY = histsThree_.find(histName.c_str() )->second->GetNbinsY();
		      return binsY;
	      }


	      int failsafe = 0;
	      return failsafe;
      }//end getYBins(histName)

      //this returns the contents of bin (x,y) in a 2D histo
      double get2DBinContents(const std::string histName, int xBin, int yBin) const {
	      if(bookedTwo(histName.c_str()) ){
		      double binContents = histsTwo_.find(histName.c_str() )->second->GetBinContent(xBin, yBin);
		      return binContents;
	      }

	      double failsafe = 0.;
	      return failsafe;

      }//end get2DBinContents()

      //this returns the contents of bin xBin in a 1D histo
      double get1DBinContents(const std::string histName, int xBin) const {
	      if(booked(histName.c_str()) ){
		      double binContents = hists_.find(histName.c_str() )->second->GetBinContent(xBin);
		      return binContents;
	      }

	      double failsafe = 0.;
	      return failsafe;

      }//end get1DBinContents()

      //this returns the upper value (right most) corresponding to the right edge of a bin in a 1D histo
      double get1DUpperBinEdge(const std::string histName, int xBin) const {
	      if(booked(histName.c_str()) ){
		      double lowerBinEdge = hists_.find(histName.c_str() )->second->GetBinLowEdge(xBin);
		      double binWidth = hists_.find(histName.c_str() )->second->GetBinWidth(xBin);
		      double upperBinEdge = lowerBinEdge + binWidth;
		      return upperBinEdge;
	      }

	      double failsafe = 0.;
	      return failsafe;

      }//end get1DUpperBinEdge()

      //this sets the contents of bin xBin in a 1D histo
      void set1DBinContents(const std::string histName, int xBin, double content) const {
	      if(booked(histName.c_str()) ){
		      hists_.find(histName.c_str() )->second->SetBinContent(xBin, content);
	      }

      }//end set1DBinContents()


      void set2DBinContents(const std::string histName, int xBin, int yBin, double content) const {
	      if(bookedTwo(histName.c_str()) ){
		      histsTwo_.find(histName.c_str() )->second->SetBinContent(xBin, yBin, content);
	      }

      }//end set2DBinContents()

      double get3DBinContents(const std::string histName, int xBin, int yBin, int zBin) const {
	      if(bookedThree(histName.c_str()) ){
		      double binContents = histsThree_.find(histName.c_str() )->second->GetBinContent(xBin, yBin, zBin);
		      return binContents;
	      }

	      double failsafe = 0.;
	      return failsafe;

      }//end get3DBinContents()

      void set3DBinContents(const std::string histName, int xBin, int yBin, int zBin, double content) const {
	      if(bookedThree(histName.c_str()) ){
		      histsThree_.find(histName.c_str() )->second->SetBinContent(xBin, yBin, zBin, content);
	      }

      }//end set3DBinContents()


void makeAndSaveSingleHisto(TString title, TString filePostfix, TString canvName, TString legEntry, const std::string histName, bool doLogYAxis){
	TString longPathName = "/eos/uscms/store/user/skalafut/HGCal/1D_";

	TH1D * histogram = hists_.find(histName.c_str())->second;
	TString saveFileType = ".gif";
	TString canvasName = canvName;

	TCanvas * c111=new TCanvas(canvasName,canvasName,800,800);
	c111->cd();
	if(doLogYAxis==true){
		c111->SetLogy(1);
		histogram->SetMinimum(1);
	}
	if(doLogYAxis==false){
		histogram->SetMinimum(0);
	}


	histogram->SetLineColor(1);
	histogram->SetLineWidth(1);
	histogram->SetTitle(title);

	TLegend * leg111 = new TLegend(.8,.27,1,.4);
	leg111->AddEntry(histogram,legEntry);

	histogram->Draw("hist");
	leg111->Draw();

	c111->SaveAs(longPathName+filePostfix+saveFileType, "recreate");

}//end makeAndSaveSingleHisto(...)

void makeAndSaveSingle2DHisto(TString title, TString filePostfix, TString canvName, TString legEntry, const std::string histName, bool doLogYAxis){
	TString longPathName = "/eos/uscms/store/user/skalafut/HGCal/2D_";

	TH2D * histogram = histsTwo_.find(histName.c_str())->second;
	TString saveFileType = ".gif";
	TString canvasName = canvName;

	TCanvas * c111=new TCanvas(canvasName,canvasName,800,800);
	c111->cd();
	if(doLogYAxis==true){
		c111->SetLogy(1);
		histogram->SetMinimum(1);
	}
	if(doLogYAxis==false){
		histogram->SetMinimum(0);
	}


	histogram->SetLineColor(1);
	histogram->SetLineWidth(1);
	histogram->SetTitle(title);

	TLegend * leg111 = new TLegend(.8,.27,1,.4);
	leg111->AddEntry(histogram,legEntry);

	histogram->Draw("hist");
	leg111->Draw();

	c111->SaveAs(longPathName+filePostfix+saveFileType, "recreate");

}//end makeAndSaveSingle2DHisto(...)



void makeAndSaveSingle3DHisto(TString title, TString filePostfix, TString canvName, TString legEntry, const std::string histName, bool doLogZAxis){
	TString longPathName = "/eos/uscms/store/user/skalafut/HGCal/3D_";

	TH3D * histogram = histsThree_.find(histName.c_str())->second;
	TString saveFileType = ".gif";
	TString canvasName = canvName;

	TCanvas * c111=new TCanvas(canvasName,canvasName,800,800);
	c111->cd();
	if(doLogZAxis==true){
		c111->SetLogz(1);
		histogram->SetMinimum(1);
	}
	if(doLogZAxis==false){
		histogram->SetMinimum(0);
	}


	histogram->SetLineColor(1);
	histogram->SetLineWidth(1);
	histogram->SetTitle(title);
	histogram->GetXaxis()->SetTitleOffset(1.6);
	histogram->GetYaxis()->SetTitleOffset(1.75);
	histogram->GetZaxis()->SetTitleOffset(1.5);


	TLegend * leg111 = new TLegend(.8,.27,1,.4);
	leg111->AddEntry(histogram,legEntry);

	histogram->Draw("hist");
	leg111->Draw();

	c111->SaveAs(longPathName+filePostfix+saveFileType, "recreate");

}//end makeAndSaveSingle3DHisto(...)


/*
void GetTrackedTriggerObjects(const edm::Event& iEvent, const double genTrackedEta, const double genTrackedPhi, const double maxDrForMatch){
	//get the pT, eta, and phi of the HLT object which fires the tracked leg and has the closest match to the GEN tracked electron

	// Load Trigger Event with references to objects 
	edm::InputTag hltTrigInfoTag("hltTriggerSummaryRAW","","TEST");
	edm::Handle<trigger::TriggerEventWithRefs> trig_event;

	iEvent.getByLabel(hltTrigInfoTag, trig_event);
	if (!trig_event.isValid() ){
		std::cout << "No valid hltTriggerSummaryRAW." << std::endl;
		return;
	}

	std::vector<std::string> trig_names;
	trig_names.push_back("hltEle27WPXXTrackIsoFilter");
	unsigned int bestMatchIndex = -1;
	int bestMatchPhotonId = 0;
	double highPt = 0;

	for (auto& trig_name : trig_names) {
		//loop over the different filter modules that appear in the HLT path.  The names of these modules are specified in the input vector<std::string> called trig_names.
		//std::cout<<"looking at trigger module named "<< trig_name <<std::endl; 
		edm::InputTag filter_tag(trig_name, "", "TEST");

		trigger::size_type filter_index = trig_event->filterIndex(filter_tag);
		
		if(filter_index < trig_event->size()) { //Check that at least one object in the event passed the filter corresponding to filter_index 
			//std::cout<<"at least one object in the event passed filter number "<< filter_index << std::endl;
			//std::cout<<"the name of this filter module is "<< trig_name << std::endl;

			for(int i=0; i<=100; i++){
				//loop over all possible photon ids (integer values)
				//each object that passes a filter is assigned an id #
				//most photon ids are equal to 81 or 82 

				//trigger::VRphoton is a typedef to a vector of edm::Refs which points to reco::RecoEcalCandidate objects
				trigger::VRphoton tracklessEleRefs;

				//this fills the vector of RecoEcalCandidate references named tracklessEleRefs with pointers to real RecoEcalCandidate objects
				trig_event->getObjects(filter_index, i, tracklessEleRefs);
				//std::cout<<"when photonId equals "<< i <<" there are "<< tracklessEleRefs.size() <<" different references to RecoEcalCandidate objects"<<std::endl; 

				//now loop over all objects which passed 
				for(unsigned int j=0; j<tracklessEleRefs.size() ; j++){

					if(filter_index == 16){//corresponds to track iso filter
						if( std::fabs(tracklessEleRefs[j]->eta()) < 2.5 ){
							double dR = deltaR(genTrackedEta, genTrackedPhi, tracklessEleRefs[j]->eta(), tracklessEleRefs[j]->phi() );
							double pt = (tracklessEleRefs[j]->energy()/TMath::CosH(tracklessEleRefs[j]->eta() ) );
							fill("trackedGENToHLTDeltaR", dR);
							if(dR < maxDrForMatch && pt > highPt){
								bestMatchIndex = 0;
								bestMatchIndex += j;
								bestMatchPhotonId = 0;
								bestMatchPhotonId += i;
								highPt = 0;
								highPt += pt;
							}

						}//end requirement that REC fall within tracker coverage 

					}//end filter_index == 16 

				}//end loop over all elements in tracklessEleRefs vector

			}//end loop over photon id values

			//now use the bestMatchPhotonId, bestMatchIndex, and highPt vars to identify the tracked trigger object
			//whose pT, eta, and phi should be saved.  This trigger object must be within maxDrForMatch of the eta and
			//phi values which were input to this function
			trigger::VRphoton trackedEleRef;
			trig_event->getObjects(filter_index, bestMatchPhotonId, trackedEleRef);
			for(unsigned int q=0; q<trackedEleRef.size(); q++){
				if(q==bestMatchIndex && filter_index == 16){
					matched_tracked_pT_ = (trackedEleRef[q]->energy()/TMath::CosH(trackedEleRef[q]->eta() ) );
					matched_tracked_eta_ = trackedEleRef[q]->eta();
					matched_tracked_phi_ = trackedEleRef[q]->phi();
					break;
				}
			}//end loop over objects in trackedEleRef vector

		}//end if(filter_index...)

	}//end loop over trigger module names

}//end GetTrackedTriggerObjects() 
*/

void GetTrackedTriggerObjects(const edm::Event& iEvent, const double genTrackedEta, const double genTrackedPhi, const double maxDrForMatch){

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

   hists_["trackedLeg_postFILT_Pt"]=fs->make<TH1D>("trackedLeg_postFILT_Pt","P_{T} of candidates passing tracked leg FILT;P_{T} (GeV);"100,0.,250.);
   hists_["trackedLeg_postFILT_Eta"]=fs->make<TH1D>("trackedLeg_postFILT_Eta","#eta of candidates passing tracked leg FILT;#eta;"200,-4.0,4.0);
   hists_["trackedLeg_postFILT_SigmaIEIE"]=fs->make<TH1D>("trackedLeg_postFILT_SigmaIEIE","#sigma_{i#eta i#eta} of candidates passing tracked leg FILT;#sigma_{i#eta i#eta};"200,0.,0.1);
   hists_["trackedLeg_postFILT_HE"]=fs->make<TH1D>("trackedLeg_postFILT_HE","relative H/E of candidates passing tracked leg FILT;Had/Em/Energy;"200,-0.1,0.6);
   hists_["trackedLeg_postFILT_EcalIso"]=fs->make<TH1D>("trackedLeg_postFILT_EcalIso","relative Ecal iso of candidates passing tracked leg FILT;EcalIso/pT;"200,-0.1,0.6);
   hists_["trackedLeg_postFILT_HcalIso"]=fs->make<TH1D>("trackedLeg_postFILT_HcalIso","relative Hcal iso of candidates passing tracked leg FILT;HcalIso/pT;"200,-0.1,0.6);
   hists_["trackedLeg_postFILT_EP"]=fs->make<TH1D>("trackedLeg_postFILT_EP","(1/E)-(1/P) of candidates passing tracked leg FILT;(1/E)-(1/P);"200,-0.05,0.2);


	}//end if(recoTrackedRefs.size() > 0 )

	*/

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

}//end GetTrackedTriggerObjects()


/*
void hasGenMatchedTrackedElectron(const edm::Event& iEvent, const double genEta, const double genPhi){
	//checks that the gen tracked electron is matched to a reco Gsf Electron
	
	//load GsfElectron object collection
	edm::InputTag gsfEleTag("hltEgammaGsfElectrons","","TEST");
	edm::Handle<std::vector<reco::Electron> > gsfElectrons;
	iEvent.getByLabel(gsfEleTag, gsfElectrons);
	if(!gsfElectrons.isValid() ){
		std::cout<<"no valid gsfElectron collection"<<std::endl;
		return;
	}
   
	for(std::vector<reco::Electron>::const_iterator gsfIt=gsfElectrons->begin(); gsfIt != gsfElectrons->end(); gsfIt++){
		//loop over all gsf electrons in event
		//gsf electrons will only be saved in the event record if the tracked leg of the trigger is fired
		fill("gsfElectronDeltaR", deltaR(gsfIt->eta(), gsfIt->phi(), genEta, genPhi) );
		if(deltaR(gsfIt->eta(), gsfIt->phi(), genEta, genPhi) <= 0.2){
			trackedGenToRecoMatch_ = 1;
		}
		
	}//end loop over gsf electrons

	return;

}//end hasGenMatchedTrackedElectron()

*/

/*
void GetMatchedTriggerObjects(
		const edm::Event& iEvent,
		const std::vector<std::string>& trig_names, const double eta, const double phi, const double dRForMatch)
{
	// If our vector is empty or the first item is blank
	if (trig_names.size() == 0 || trig_names[0].size() == 0) {
		return;
	}

	//begin work with trigger objects

	// Load Trigger Event with references to objects 
	edm::InputTag hltTrigInfoTag("hltTriggerSummaryRAW","","TEST");
	edm::Handle<trigger::TriggerEventWithRefs> trig_event;

	iEvent.getByLabel(hltTrigInfoTag, trig_event);
	if (!trig_event.isValid() ){
		std::cout << "No valid hltTriggerSummaryRAW." << std::endl;
		return;
	}

	typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> > ecalCandToValMap;

	//collections for untracked electron candidates
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

	std::vector<edm::Handle<ecalCandToValMap> > untrackedHandles;
	untrackedHandles.push_back(untrackedEcalClusterShapeHandle);
	untrackedHandles.push_back(untrackedEcalClusterShapeSigmaIEtaIEtaHandle);
	untrackedHandles.push_back(untrackedEcalIsoHandle);
	untrackedHandles.push_back(untrackedHoverEHandle);
	untrackedHandles.push_back(untrackedHcalIsoHandle);

	unsigned int bestMatchIndex=-1;
	int bestMatchPhotonId=0;
	double highPt=0;

	for (auto& trig_name : trig_names) {
		//loop over the different filter modules that appear in the HLT path.  The names of these modules are specified in the input vector<std::string> called trig_names.
		//std::cout<<"looking at trigger module named "<< trig_name <<std::endl; 
		edm::InputTag filter_tag(trig_name, "", "TEST");

		trigger::size_type filter_index = trig_event->filterIndex(filter_tag);
		
		if(filter_index < trig_event->size()) { //Check that at least one object in the event passed the filter corresponding to filter_index 
			//std::cout<<"at least one object in the event passed filter number "<< filter_index << std::endl;
			//std::cout<<"the name of this filter module is "<< trig_name << std::endl;
	
			for(int i=0; i<=100; i++){
				//loop over all possible photon ids (integer values)
				//each object that passes a filter is assigned an id # 
				//most ids are either 81 or 92, even if there are more than 2 objects which pass the filter

				//trigger::VRphoton is a typedef to a vector of edm::Refs which points to reco::RecoEcalCandidate objects
				trigger::VRphoton tracklessEleRefs;

				//this fills the vector of RecoEcalCandidate references named tracklessEleRefs with pointers to real RecoEcalCandidate objects
				trig_event->getObjects(filter_index, i, tracklessEleRefs);
				//std::cout<<"when photonId equals "<< i <<" there are "<< tracklessEleRefs.size() <<" different references to RecoEcalCandidate objects"<<std::endl; 

				//now loop over all objects which passed  
				for(unsigned int j=0; j<tracklessEleRefs.size() ; j++){
					//for the trackless electron candidate: ecal iso cut <--> filter_index = 5, H/E cut <--> filter_index = 6, 
					//hcal iso cut <--> filter_index = 7
					
					if(filter_index == 7){
						//filter_index = 7 corresponds to HCAL iso
						if( std::fabs(tracklessEleRefs[j]->eta()) >= 2.5 && std::fabs(tracklessEleRefs[j]->eta()) < 3.0 ){
							numUnmatchedCandidates_ += 1.0;
							double dR = deltaR(eta, phi, tracklessEleRefs[j]->eta(), tracklessEleRefs[j]->phi() );
							double pt = (tracklessEleRefs[j]->energy()/TMath::CosH(tracklessEleRefs[j]->eta() ) );
							fill("tracklessGENToHLTDeltaR", dR);
   						   	if(dR < dRForMatch && pt > highPt){
								//now the best match HLT object has been found
								bestMatchPhotonId = 0;
								bestMatchPhotonId += i;
								bestMatchIndex = 0;
								bestMatchIndex += j;
								highPt = 0;
								highPt += pt;
							}

						}//end requirement that REC be in trackless EE

					}//end filter_index == 7

				}//end loop over all elements in tracklessEleRefs vector

			}//end loop over photon id values

			//now use bestMatchIndex and bestMatchPhotonId to save the pT, eta, phi, and trigger cut vars of the HLT object which fired the trackless leg
			//look for the highest pT HLT object within some dR of a specified point (the GEN electron in Z->ee evts, or an arbitrary point for general signal and bkgnd evts)
			trigger::VRphoton tracklessEleRef;
			trig_event->getObjects(filter_index, bestMatchPhotonId, tracklessEleRef);

			for(unsigned int r=0; r<tracklessEleRef.size(); r++){
				if(filter_index == 7 && r == bestMatchIndex){
					//get and save the pT, eta, phi, and other trigger cut variables associated with the HLT object which fired the trackless leg
   					std::vector<float> untrackedEleParams;
					untrackedEleParams.push_back( tracklessEleRef[r]->energy()/( TMath::CosH(tracklessEleRef[r]->eta() ) ) );
					untrackedEleParams.push_back( tracklessEleRef[r]->eta() );
					std::vector<ecalCandToValMap> valMaps;
					for(unsigned int q=0; q<untrackedHandles.size() ;q++){
						if(untrackedHandles[q].isValid() ){
							valMaps.push_back( *(untrackedHandles[q].product() ) );	//gets a map from the handle, puts map in the last element of a vector
							untrackedEleParams.push_back( ( valMaps[valMaps.size()-1].find(tracklessEleRef[r]) )->val ); //gets value of variable (ecal iso, H/E, etc) from map, and stores it in a vector
						}

					}//end loop over edm::Handle objects to collections tied to untracked electron candidates

					matched_pT_=untrackedEleParams[0];
					matched_eta_=untrackedEleParams[1];
					matched_phi_=tracklessEleRef[r]->phi();
					matched_ecalClusterShape_=untrackedEleParams[2];
					matched_ecalClusterShape_SigmaIEtaIEta_=untrackedEleParams[3];
					matched_ecalIso_=untrackedEleParams[4];
					matched_hOverE_=untrackedEleParams[5];
					matched_hcalIso_=untrackedEleParams[6];

					incrementNumTriggeredEvents();
					std::cout<<"numTriggeredEvents equals "<< getNumTriggeredEvents() <<std::endl;
					break;
				}//end requirement that r == bestMatchIndex and filter_index == 7 (hcal iso cut)
			
			}//end loop over tracklessEleRef elements

		}//end if(filter_index...)

	}//end loop over trigger module names

}//end GetMatchedTriggerObjects() 
*/

void GetMatchedTriggerObjects(
		const edm::Event& iEvent,
		const double eta, const double phi, const double dRForMatch){

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
			fill("tracklessGENToHLTDeltaR", dR);
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


}//end GetMatchedTriggerObjects()


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

}	

void resetCounters(){
	//reset all of the private member vars which are saved to the TTree 

	//there are never more than 2 gen electrons/positrons in the event
	//cut zero = no cuts
	gen_l1_pT_cutZero_= -1;
	gen_l1_eta_cutZero_ = -7;
	gen_l2_pT_cutZero_= -1;
	gen_l2_eta_cutZero_ = -7;

	//cut one = two gen electrons from Z boson mother, both with pT > 15 
	gen_l1_pT_cutOne_= -1;
	gen_l1_eta_cutOne_ = -7;
	gen_l2_pT_cutOne_= -1;
	gen_l2_eta_cutOne_ = -7;

	//cut two = cut one + one tracked gen electron with pT > 27  
	gen_l1_pT_cutTwo_= -1;
	gen_l1_eta_cutTwo_ = -7;
	gen_l2_pT_cutTwo_= -1;
	gen_l2_eta_cutTwo_ = -7;


	//cut three = cut two + one untracked gen electron (whose pT must be > 15 due to prior cuts)
	gen_l1_pT_cutThree_= -1;
	gen_l1_eta_cutThree_ = -7;
	gen_l2_pT_cutThree_= -1;
	gen_l2_eta_cutThree_ = -7;


	numEvents_cutLvlZero_=0;	//the total number of events which were analyzed, no cuts on anything
	numEvents_cutLvlOne_=0;	//the total number of events where two gen electrons are found with a Z boson mother and pt>15
    numEvents_cutLvlTwo_=0;	//total # of evts with two gen electrons coming from a Z boson, and one tracked lepton with pt>27 
    numEvents_cutLvlThree_=0;  //total # evts passing gen mother, pT, and eta cuts (tracked pt > 27, trackless pt > 15)
	numEvents_cutLvlFour_=0;	//total # evts passing gen mother, pT, eta cuts, and GEN dilepton mass btwn 60 and 120 GeV


	//vars to explore which filters are tightest in tracked leg
	//these variables will help explain why there is a large drop btwn numEvents_cutLvlFour_ and
	//the number of evts which fire the trigger AND pass cutLvlFour
	numEvts_passing_L1Seed_=0;		//looks for L1_SingleEG20 seed
	numEvts_passing_L1Filter_=0;	//after L1Seed requirement, not sure what this filter does
	numEvts_passing_EtFilter_=0;	//requires one tracked electron with ET > 27, after L1Filter
   	numEvts_passing_ClusterShapeFilter_=0;	//cuts on sigmaIEIE, after EtFilter
   	numEvts_passing_HEFilter_=0;	//cuts on (had/em)/energy, after ClusterShapeFilter
  	numEvts_passing_EcalIsoFilter_=0;	//cuts on ecalIso/pT, after HEFilter
	numEvts_passing_HcalIsoFilter_=0;	//cuts on hcalIso/pT, after EcalIsoFilter 
	numEvts_passing_PixelMatchFilter_=0;	//after HcalIsoFilter, cuts on pixel detector vars
   	numEvts_passing_E_P_Filter_=0;		//cuts on (1/E)-(1/P), after PixelMatchFilter
	numEvts_passing_DetaFilter_=0;		//cuts on dEta btwn candidate and track, after (1/E)-(1/P) filter
	numEvts_passing_DphiFilter_=0;		//cuts on dPhi, after dEta filter.  This is the 2nd to last filter in the tracked leg
	numEvts_passing_TrackIsoFilter_=0;	//last filter in tracked leg, runs after dPhi filter

	//vars to explore which filters are tightest in trackless leg
	numEvts_passing_trackless_EtFilter_=0;
	numEvts_passing_trackless_ClusterShapeFilter_=0;
	numEvts_passing_trackless_EcalIsoFilter_=0;
	numEvts_passing_trackless_HEFilter_=0;
	numEvts_passing_trackless_HcalIsoFilter_=0;
	numEvts_passing_trackless_EtaFilter_=0;


	//these pT, eta, and phi values are equivalent to the kinematic values for events
	//which have numEvents_cutLvlFour_ = 1
	gen_trackless_pT_=-1;	//pT of gen electron in trackless EE
	gen_trackless_eta_=-7;	//eta of gen electron in trackless EE
	gen_trackless_phi_=-7;	//phi of gen electron in trackless EE
	gen_tracked_pT_=-1;	//pT of gen electron in tracked ECAL
	gen_tracked_eta_=-7;	//eta of gen electron in tracked ECAL
	gen_tracked_phi_=-7;	//phi of gen electron in tracked ECAL
	genTriggeredEvent_ = -1;

	matched_pT_=-1;
	matched_eta_=-7;
	matched_phi_=-7;
	matched_ecalIso_=999;
	matched_hcalIso_=999;
	matched_hOverE_=999;
	matched_ecalClusterShape_=999;
	matched_ecalClusterShape_SigmaIEtaIEta_=999;
	numRecoEcalCands_=0;	//# of trackless trigger leg RecoEcalCandidate objects which pass the hcal iso filter and have 2.4 < |eta| < 3.0 
	numUnmatchedCandidates_=0;

	//needed to compute dilepton mass at trigger level with HLT objects firing tracked and trackless legs of trigger
	numTrackedCandidates_ = 0;
	matched_tracked_pT_=-1;
	matched_tracked_eta_=-7;
	matched_tracked_phi_=-7;

	hlt_mLL_ = -1;

}



private:
virtual void beginJob() override;
virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
virtual void endJob() override;

std::map<std::string,TH1D*> hists_;
std::map<std::string,TH2D*> histsTwo_;
std::map<std::string,TH3D*> histsThree_;


//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

// ----------member data ---------------------------

//here I need to initialize all of the variables which I want to save into the TTree, in addition to a pointer to the TTree

double totalNumEvents;	//total number of events which are analyzed, no requirement on either GEN electron

//these two variables will not be saved to the TTree
double numTriggeredEvents=0;
double efficiencyDenominator=0;	//total number of events where there is one GEN electron with pT > 15 GeV in the trackless region, and one tracked electron

TTree * tree;
//cut zero = no cuts
double gen_l1_pT_cutZero_;
double gen_l1_eta_cutZero_;
double gen_l2_pT_cutZero_;
double gen_l2_eta_cutZero_;

//cut one = two gen electrons from Z boson mother, both with pT > 15 
double gen_l1_pT_cutOne_;
double gen_l1_eta_cutOne_;
double gen_l2_pT_cutOne_;
double gen_l2_eta_cutOne_;

//cut two = cut one + one tracked gen electron with pT > 27  
double gen_l1_pT_cutTwo_;
double gen_l1_eta_cutTwo_;
double gen_l2_pT_cutTwo_;
double gen_l2_eta_cutTwo_;

//cut three = cut two + one untracked gen electron
double gen_l1_pT_cutThree_;
double gen_l1_eta_cutThree_;
double gen_l2_pT_cutThree_;
double gen_l2_eta_cutThree_;


//vars used to study # of evts passing different levels of cuts
//nomenclature example: cutLvlThree includes all of the cuts made in cutLvlTwo 
int numEvents_cutLvlZero_;	//the total number of events which were analyzed, no cuts on anything
int numEvents_cutLvlOne_;	//the total number of events where two gen electrons are found with a Z boson mother and pt > 15
int numEvents_cutLvlTwo_;	//total # of evts with two gen electrons coming from a Z boson, and one tracked lepton with pt>27
int numEvents_cutLvlThree_;  //total # evts passing gen mother, pT, and eta cuts (tracked pt > 27, trackless pt > 15)
int numEvents_cutLvlFour_;	//total # evts passing gen mother, pT, eta cuts, and GEN dilepton mass btwn 60 and 120 GeV


//vars to explore which filters are tightest in tracked leg
//these variables will help explain why there is a large drop btwn numEvents_cutLvlFour_ and
//the number of evts which fire the trigger AND pass cutLvlFour 
int numEvts_passing_L1Seed_;		//looks for L1_SingleEG20 seed
int numEvts_passing_L1Filter_;	//after L1Seed requirement, not sure what this filter does
int numEvts_passing_EtFilter_;	//requires one tracked electron with ET > 27, after L1Filter
int numEvts_passing_ClusterShapeFilter_;	//cuts on sigmaIEIE, after EtFilter
int numEvts_passing_HEFilter_;	//cuts on (had/em)/energy, after ClusterShapeFilter
int numEvts_passing_EcalIsoFilter_;	//cuts on ecalIso/pT, after HEFilter
int numEvts_passing_HcalIsoFilter_;	//cuts on hcalIso/pT, after EcalIsoFilter 
int numEvts_passing_PixelMatchFilter_;	//after HcalIsoFilter, cuts on pixel detector vars
int numEvts_passing_E_P_Filter_;		//cuts on (1/E)-(1/P), after PixelMatchFilter
int numEvts_passing_DetaFilter_;		//cuts on dEta btwn candidate and track, after (1/E)-(1/P) filter
int numEvts_passing_DphiFilter_;		//cuts on dPhi, after dEta filter.  This is the 2nd to last filter in the tracked leg
int numEvts_passing_TrackIsoFilter_;	//last filter in tracked leg, runs after dPhi filter

//vars to explore which filters are tightest in trackless leg
int numEvts_passing_trackless_EtFilter_;
int numEvts_passing_trackless_ClusterShapeFilter_;
int numEvts_passing_trackless_EcalIsoFilter_;
int numEvts_passing_trackless_HEFilter_;
int numEvts_passing_trackless_HcalIsoFilter_;
int numEvts_passing_trackless_EtaFilter_;



//gen lepton variables going into TTree
double gen_trackless_pT_;	//pT of gen electron in trackless EE
double gen_trackless_eta_;	//eta of gen electron in trackless EE
double gen_trackless_phi_;	//phi of gen electron in trackless EE
double gen_tracked_pT_;	//pT of gen electron in tracked ECAL
double gen_tracked_eta_;	//eta of gen electron in tracked ECAL 
double gen_tracked_phi_;	//phi of gen electron in tracked ECAL 
double genTriggeredEvent_;	// equals +1 for events which should have fired trackless and tracked legs of trigger based on GEN lvl info, equals -1 otherwise

//variables corresponding to matched HLT object in trackless EE which will go into TTree
double matched_pT_;
double matched_eta_;
double matched_phi_;
double matched_ecalIso_;	//ecalIso/pT
double matched_hcalIso_;	//hcalIso/pT
double matched_hOverE_;		// (had/em)/energy 
double matched_ecalClusterShape_;
double matched_ecalClusterShape_SigmaIEtaIEta_;
int numRecoEcalCands_;
double numUnmatchedCandidates_;

//number of reco ecal objects which passed the tracked leg of the trigger in the event
int numTrackedCandidates_;

//pT, eta, phi of HLT object which fired tracked leg of trigger
double matched_tracked_pT_;
double matched_tracked_eta_;
double matched_tracked_phi_;

//dilepton mass of the tracked HLT object firing the tracked leg, and the trackless HLT object firing the trackless leg
double hlt_mLL_;

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
doubleEleTracklessAnalyzer::doubleEleTracklessAnalyzer(const edm::ParameterSet& iConfig)
	//foutName(iConfig.getUntrackedParameter<std::string>("foutName"))
/*  vtxCollectionTAG(iConfig.getParameter<edm::InputTag>("vertexCollection")),
  BeamSpotTAG(iConfig.getParameter<edm::InputTag>("BeamSpotCollection")),
  electronsTAG(iConfig.getParameter<edm::InputTag>("electronCollection")),
  recHitCollectionEBTAG(iConfig.getParameter<edm::InputTag>("recHitCollectionEB")),
  recHitCollectionEETAG(iConfig.getParameter<edm::InputTag>("recHitCollectionEE")),
  EESuperClustersTAG(iConfig.getParameter<edm::InputTag>("EESuperClusterCollection")),
  rhoTAG(iConfig.getParameter<edm::InputTag>("rhoFastJet")),
  triggerResultsTAG(iConfig.getParameter<edm::InputTag>("triggerResultsCollection")),*/

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   
   hists_["tracklessGENToHLTDeltaR"]=fs->make<TH1D>("tracklessGENToHLTDeltaR","#DeltaR gen trackless e- to ALL trackless HLT objects passing trigger; #DeltaR;",100,0.,0.4);
   hists_["trackedGENToHLTDeltaR"]=fs->make<TH1D>("trackedGENToHLTDeltaR","#DeltaR gen tracked e- to ALL tracked HLT objects passing trigger; #DeltaR;",100,0.,0.4);


   /*
   hists_["trackedLeg_postFILT_Pt"]=fs->make<TH1D>("trackedLeg_postFILT_Pt","P_{T} of candidates passing tracked leg FILT;P_{T} (GeV);"100,0.,250.);
   hists_["trackedLeg_postFILT_Eta"]=fs->make<TH1D>("trackedLeg_postFILT_Eta","#eta of candidates passing tracked leg FILT;#eta;"200,-4.0,4.0);
   hists_["trackedLeg_postFILT_SigmaIEIE"]=fs->make<TH1D>("trackedLeg_postFILT_SigmaIEIE","#sigma_{i#eta i#eta} of candidates passing tracked leg FILT;#sigma_{i#eta i#eta};"200,0.,0.1);
   hists_["trackedLeg_postFILT_HE"]=fs->make<TH1D>("trackedLeg_postFILT_HE","relative H/E of candidates passing tracked leg FILT;Had/Em/Energy;"200,-0.1,0.6);
   hists_["trackedLeg_postFILT_EcalIso"]=fs->make<TH1D>("trackedLeg_postFILT_EcalIso","relative Ecal iso of candidates passing tracked leg FILT;EcalIso/pT;"200,-0.1,0.6);
   hists_["trackedLeg_postFILT_HcalIso"]=fs->make<TH1D>("trackedLeg_postFILT_HcalIso","relative Hcal iso of candidates passing tracked leg FILT;HcalIso/pT;"200,-0.1,0.6);
   hists_["trackedLeg_postFILT_EP"]=fs->make<TH1D>("trackedLeg_postFILT_EP","(1/E)-(1/P) of candidates passing tracked leg FILT;(1/E)-(1/P);"200,-0.05,0.2);

   */




   /*
   //THIS declaration is here for reference
   //histsThree_["PFClusterSum_HCALovrECAL_gen_eta_energy"]=fs->make<TH3D>("PFClusterSum_HCALovrECAL_gen_eta_energy","Reco E_HCAL/E_ECAL for Pi+ vs gen Pi+ energy and eta", 100, 0., 210., 15, 1.55, 3.0, 30, 0., 15.);
   */
   
   tree=fs->make<TTree>("doubleEleTrigger","Summary of trackless double electron trigger event info");

   tree->Branch("gen_l1_pT_cutZero_",&gen_l1_pT_cutZero_,"gen_l1_pT_cutZero_/D");
   tree->Branch("gen_l1_eta_cutZero_",&gen_l1_eta_cutZero_,"gen_l1_eta_cutZero_/D");
   tree->Branch("gen_l2_pT_cutZero_",&gen_l2_pT_cutZero_,"gen_l2_pT_cutZero_/D");
   tree->Branch("gen_l2_eta_cutZero_",&gen_l2_eta_cutZero_,"gen_l2_eta_cutZero_/D");
 
   tree->Branch("gen_l1_pT_cutOne_",&gen_l1_pT_cutOne_,"gen_l1_pT_cutOne_/D");
   tree->Branch("gen_l1_eta_cutOne_",&gen_l1_eta_cutOne_,"gen_l1_eta_cutOne_/D");
   tree->Branch("gen_l2_pT_cutOne_",&gen_l2_pT_cutOne_,"gen_l2_pT_cutOne_/D");
   tree->Branch("gen_l2_eta_cutOne_",&gen_l2_eta_cutOne_,"gen_l2_eta_cutOne_/D");
 
   tree->Branch("gen_l1_pT_cutTwo_",&gen_l1_pT_cutTwo_,"gen_l1_pT_cutTwo_/D");
   tree->Branch("gen_l1_eta_cutTwo_",&gen_l1_eta_cutTwo_,"gen_l1_eta_cutTwo_/D");
   tree->Branch("gen_l2_pT_cutTwo_",&gen_l2_pT_cutTwo_,"gen_l2_pT_cutTwo_/D");
   tree->Branch("gen_l2_eta_cutTwo_",&gen_l2_eta_cutTwo_,"gen_l2_eta_cutTwo_/D");
 
   tree->Branch("gen_l1_pT_cutThree_",&gen_l1_pT_cutThree_,"gen_l1_pT_cutThree_/D");
   tree->Branch("gen_l1_eta_cutThree_",&gen_l1_eta_cutThree_,"gen_l1_eta_cutThree_/D");
   tree->Branch("gen_l2_pT_cutThree_",&gen_l2_pT_cutThree_,"gen_l2_pT_cutThree_/D");
   tree->Branch("gen_l2_eta_cutThree_",&gen_l2_eta_cutThree_,"gen_l2_eta_cutThree_/D");


   tree->Branch("numEvents_cutLvlZero_",&numEvents_cutLvlZero_,"numEvents_cutLvlZero_/I");
   tree->Branch("numEvents_cutLvlOne_",&numEvents_cutLvlOne_,"numEvents_cutLvlOne_/I");
   tree->Branch("numEvents_cutLvlTwo_",&numEvents_cutLvlTwo_,"numEvents_cutLvlTwo_/I");
   tree->Branch("numEvents_cutLvlThree_",&numEvents_cutLvlThree_,"numEvents_cutLvlThree_/I");
   tree->Branch("numEvents_cutLvlFour_",&numEvents_cutLvlFour_,"numEvents_cutLvlFour_/I");


   tree->Branch("numEvts_passing_L1Seed_",&numEvts_passing_L1Seed_,"numEvts_passing_L1Seed_/I");
   tree->Branch("numEvts_passing_L1Filter_",&numEvts_passing_L1Filter_,"numEvts_passing_L1Filter_/I");
   tree->Branch("numEvts_passing_EtFilter_",&numEvts_passing_EtFilter_,"numEvts_passing_EtFilter_/I");
   tree->Branch("numEvts_passing_ClusterShapeFilter_",&numEvts_passing_ClusterShapeFilter_,"numEvts_passing_ClusterShapeFilter_/I");
   tree->Branch("numEvts_passing_HEFilter_",&numEvts_passing_HEFilter_,"numEvts_passing_HEFilter_/I");
   tree->Branch("numEvts_passing_EcalIsoFilter_",&numEvts_passing_EcalIsoFilter_,"numEvts_passing_EcalIsoFilter_/I");
   tree->Branch("numEvts_passing_HcalIsoFilter_",&numEvts_passing_HcalIsoFilter_,"numEvts_passing_HcalIsoFilter_/I");
   tree->Branch("numEvts_passing_PixelMatchFilter_",&numEvts_passing_PixelMatchFilter_,"numEvts_passing_PixelMatchFilter_/I");
   tree->Branch("numEvts_passing_E_P_Filter_",&numEvts_passing_E_P_Filter_,"numEvts_passing_E_P_Filter_/I");
   tree->Branch("numEvts_passing_DetaFilter_",&numEvts_passing_DetaFilter_,"numEvts_passing_DetaFilter_/I");
   tree->Branch("numEvts_passing_DphiFilter_",&numEvts_passing_DphiFilter_,"numEvts_passing_DphiFilter_/I");
   tree->Branch("numEvts_passing_TrackIsoFilter_",&numEvts_passing_TrackIsoFilter_,"numEvts_passing_TrackIsoFilter_/I");


   tree->Branch("numEvts_passing_trackless_EtFilter_",&numEvts_passing_trackless_EtFilter_,"numEvts_passing_trackless_EtFilter_/I");
   tree->Branch("numEvts_passing_trackless_ClusterShapeFilter_",&numEvts_passing_trackless_ClusterShapeFilter_,"numEvts_passing_trackless_ClusterShapeFilter_/I");
   tree->Branch("numEvts_passing_trackless_EcalIsoFilter_",&numEvts_passing_trackless_EcalIsoFilter_,"numEvts_passing_trackless_EcalIsoFilter_/I");
   tree->Branch("numEvts_passing_trackless_HEFilter_",&numEvts_passing_trackless_HEFilter_,"numEvts_passing_trackless_HEFilter_/I");
   tree->Branch("numEvts_passing_trackless_HcalIsoFilter_",&numEvts_passing_trackless_HcalIsoFilter_,"numEvts_passing_trackless_HcalIsoFilter_/I");
   tree->Branch("numEvts_passing_trackless_EtaFilter_",&numEvts_passing_trackless_EtaFilter_,"numEvts_passing_trackless_EtaFilter_/I");
 

   tree->Branch("gen_trackless_eta_",&gen_trackless_eta_,"gen_trackless_eta_/D");
   tree->Branch("gen_trackless_pT_",&gen_trackless_pT_,"gen_trackless_pT_/D");
   tree->Branch("gen_trackless_phi_",&gen_trackless_phi_,"gen_trackless_phi_/D");
   tree->Branch("gen_tracked_eta_",&gen_tracked_eta_,"gen_tracked_eta_/D");
   tree->Branch("gen_tracked_pT_",&gen_tracked_pT_,"gen_tracked_pT_/D");
   tree->Branch("gen_tracked_phi_",&gen_tracked_phi_,"gen_tracked_phi_/D");
   tree->Branch("genTriggeredEvent_",&genTriggeredEvent_,"genTriggeredEvent_/D");


   tree->Branch("matched_pT_",&matched_pT_,"matched_pT_/D");
   tree->Branch("matched_eta_",&matched_eta_,"matched_eta_/D");
   tree->Branch("matched_phi_",&matched_phi_,"matched_phi_/D");
   tree->Branch("matched_ecalIso_",&matched_ecalIso_,"matched_ecalIso_/D");
   tree->Branch("matched_hcalIso_",&matched_hcalIso_,"matched_hcalIso_/D");
   tree->Branch("matched_ecalClusterShape_",&matched_ecalClusterShape_,"matched_ecalClusterShape_/D");
   tree->Branch("matched_ecalClusterShape_SigmaIEtaIEta_",&matched_ecalClusterShape_SigmaIEtaIEta_,"matched_ecalClusterShape_SigmaIEtaIEta_/D");
   tree->Branch("matched_hOverE_",&matched_hOverE_,"matched_hOverE_/D");
   tree->Branch("numRecoEcalCands_",&numRecoEcalCands_,"numRecoEcalCands_/I");

   tree->Branch("numTrackedCandidates_",&numTrackedCandidates_,"numTrackedCandidates_/I");
 
   tree->Branch("matched_tracked_pT_",&matched_tracked_pT_,"matched_tracked_pT_/D");
   tree->Branch("matched_tracked_eta_",&matched_tracked_eta_,"matched_tracked_eta_/D");
   tree->Branch("matched_tracked_phi_",&matched_tracked_phi_,"matched_tracked_phi_/D");

   tree->Branch("hlt_mLL_",&hlt_mLL_,"hlt_mLL_/D");


}


doubleEleTracklessAnalyzer::~doubleEleTracklessAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
doubleEleTracklessAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;

	resetCounters();
	incrementTotalNumEvents();

   	numEvents_cutLvlZero_ += 1;


	//uncomment these two lines when analyzing bkgnd files or unmatched signal files (to compute signal trigger rate)
	//GetMatchedTriggerObjects(iEvent, 0.0, 0.0, 20);
	//GetTrackedTriggerObjects(iEvent, 0.0, 0.0, 20);
	

	//uncomment this when analyzing matched signal files to determine Z->ee trigger efficiency

	InputTag genParticleTag("genParticles","","HLT");
	Handle<std::vector<reco::GenParticle> > genPart;
	iEvent.getByLabel(genParticleTag, genPart);

	std::vector<double> genPts;

	for(std::vector<reco::GenParticle>::const_iterator genIt = genPart->begin(); genIt != genPart->end(); genIt++){
		double genPt = genIt->pt();
		addToPtSortedVector(genPts, genPt);
	}//end loop over GenParticle collection

	for(std::vector<reco::GenParticle>::const_iterator genIt = genPart->begin(); genIt != genPart->end(); genIt++){
		if(genIt->pt() == genPts[genPts.size()-2] ){
			gen_l2_pT_cutZero_ = genIt->pt();
		   	gen_l2_eta_cutZero_ = genIt->eta();
		}
		if(genIt->pt() == genPts[genPts.size()-1] ){
			gen_l1_pT_cutZero_ = genIt->pt();
		   	gen_l1_eta_cutZero_ = genIt->eta();
		}

	}//end loop over GenParticle collection to find leading and subleading GEN leptons


	InputTag zBosonMomTag("genEle","","TEST");
	Handle<edm::OwnVector<reco::Candidate,edm::ClonePolicy<reco::Candidate> > > leptonsFromZHandle;
   	iEvent.getByLabel(zBosonMomTag, leptonsFromZHandle);

	if(!leptonsFromZHandle.isValid() ){
		//std::cout<<"did not find any GEN electron or positron with pt > 15 and Z boson mother"<<std::endl;
		tree->Fill();
		return;
	}

	if(leptonsFromZHandle->size() > 1){
		numEvents_cutLvlOne_ += 1;
		std::vector<double> genPtsCutOne;
		for(edm::OwnVector<reco::Candidate>::const_iterator leptonFromZedIt = leptonsFromZHandle->begin(); leptonFromZedIt != leptonsFromZHandle->end(); leptonFromZedIt++){
			double lepPt = leptonFromZedIt->pt();
			addToPtSortedVector(genPtsCutOne, lepPt);
		}//end loop over collection of GEN electrons/positrons with pt > 15 and Z boson mother

		for(edm::OwnVector<reco::Candidate>::const_iterator leptonFromZedIt = leptonsFromZHandle->begin(); leptonFromZedIt != leptonsFromZHandle->end(); leptonFromZedIt++){
			if(leptonFromZedIt->pt() == genPtsCutOne[genPtsCutOne.size()-2] ){
				gen_l2_pT_cutOne_ = leptonFromZedIt->pt();
				gen_l2_eta_cutOne_ = leptonFromZedIt->eta();
			}

			if(leptonFromZedIt->pt() == genPtsCutOne[genPtsCutOne.size()-1] ){
				gen_l1_pT_cutOne_ = leptonFromZedIt->pt();
				gen_l1_eta_cutOne_ = leptonFromZedIt->eta();
			}

		}//end loop over collection of GEN electrons/positrons with pt > 15 and Z boson mother

	}


	InputTag trackedLeptTag("genEleTrack","","TEST");
	Handle<edm::OwnVector<reco::Candidate,edm::ClonePolicy<reco::Candidate> > > trackedLeptHandle;
	iEvent.getByLabel(trackedLeptTag, trackedLeptHandle);

	if(!trackedLeptHandle.isValid() ){
		//std::cout<<"in evt with at least one GEN lepton with pt > 15 and Z mother"<<std::endl;
		//std::cout<<"did not find any GEN electron or positron with pt > 27 in the tracked region, and with Z mother"<<std::endl;
		tree->Fill();
		return;
	}

	if(trackedLeptHandle->size() > 0 && leptonsFromZHandle->size() > 1){
		numEvents_cutLvlTwo_ += 1;

		//there will never be more than 2 gen electrons in an event
		//if trackedLeptHandle->size() == 2, then both gen_l1 and gen_l2 will come from trackedLeptHandle
		std::vector<double> genPtsCutTwo;
		if(trackedLeptHandle->size() == 2){
			for(edm::OwnVector<reco::Candidate>::const_iterator trackedLeptIt = trackedLeptHandle->begin(); trackedLeptIt != trackedLeptHandle->end(); trackedLeptIt++){
				double lepPt = trackedLeptIt->pt();
				addToPtSortedVector(genPtsCutTwo, lepPt);
			}//end loop over collection of tracked GEN electrons/positrons 

			for(edm::OwnVector<reco::Candidate>::const_iterator trackedLeptIt = trackedLeptHandle->begin(); trackedLeptIt != trackedLeptHandle->end(); trackedLeptIt++){
				if(trackedLeptIt->pt() == genPtsCutTwo[genPtsCutTwo.size()-1] ){
					gen_l1_pT_cutTwo_ = trackedLeptIt->pt();
					gen_l1_eta_cutTwo_ = trackedLeptIt->eta();
				}

				if(trackedLeptIt->pt() == genPtsCutTwo[genPtsCutTwo.size()-2] ){
					gen_l2_pT_cutTwo_ = trackedLeptIt->pt();
					gen_l2_eta_cutTwo_ = trackedLeptIt->eta();
				}


			}//end loop over collection of tracked GEN electrons/positrons

		}//end if(trackedLeptHandle->size() == 2)

		//if trackedLeptHandle->size() == 1, then I should loop over leptonsFromZHandle and find
		//the tracked lepton with pT > 27, and the untracked lepton with pT > 15
		if(trackedLeptHandle->size() == 1){
			for(edm::OwnVector<reco::Candidate>::const_iterator leptIt = leptonsFromZHandle->begin(); leptIt != leptonsFromZHandle->end(); leptIt++){
				double lepPt = leptIt->pt();
				addToPtSortedVector(genPtsCutTwo, lepPt);
			}//end loop over leptonsFromZHandle

			for(edm::OwnVector<reco::Candidate>::const_iterator leptIt = leptonsFromZHandle->begin(); leptIt != leptonsFromZHandle->end(); leptIt++){
				if(leptIt->pt() == genPtsCutTwo[genPtsCutTwo.size()-1] ){
					gen_l1_pT_cutTwo_ = leptIt->pt();
					gen_l1_eta_cutTwo_ = leptIt->eta();
				}

				if(leptIt->pt() == genPtsCutTwo[genPtsCutTwo.size()-2] ){
					gen_l2_pT_cutTwo_ = leptIt->pt();
					gen_l2_eta_cutTwo_ = leptIt->eta();
				}

			}//end loop over leptonsFromZHandle

		}//end if(trackedLeptHandle->size() == 1)

	}//end if(trackedLeptHandle->size() > 0)

	InputTag untrackedLeptTag("genUntrack","","TEST");
	Handle<edm::OwnVector<reco::Candidate,edm::ClonePolicy<reco::Candidate> > > untrackedLeptHandle;
	iEvent.getByLabel(untrackedLeptTag, untrackedLeptHandle);

	if(!untrackedLeptHandle.isValid() ){
		//std::cout<<"in evts with 2 GEN leptons with pt > 15, both with Z boson mother, and at least one GEN lepton in the tracked region with pt > 27"<<std::endl;
		//std::cout<<"did not find any GEN electron or positron with pt > 15, in the trackless EE region, and with Z mother"<<std::endl;
		tree->Fill();
		return;
	}

	if(untrackedLeptHandle->size() > 0 && trackedLeptHandle->size() > 0){
		numEvents_cutLvlThree_ += 1;
		std::vector<double> genPtsCutThree;
		for(edm::OwnVector<reco::Candidate>::const_iterator leptIt = leptonsFromZHandle->begin(); leptIt != leptonsFromZHandle->end(); leptIt++){
			double lepPt = leptIt->pt();
			addToPtSortedVector(genPtsCutThree, lepPt);
		}//end loop over leptonsFromZHandle

		for(edm::OwnVector<reco::Candidate>::const_iterator leptIt = leptonsFromZHandle->begin(); leptIt != leptonsFromZHandle->end(); leptIt++){
			if(leptIt->pt() == genPtsCutThree[genPtsCutThree.size()-1] ){
				gen_l1_pT_cutThree_ = leptIt->pt();
				gen_l1_eta_cutThree_ = leptIt->eta();
			}

			if(leptIt->pt() == genPtsCutThree[genPtsCutThree.size()-2] ){
				gen_l2_pT_cutThree_ = leptIt->pt();
				gen_l2_eta_cutThree_ = leptIt->eta();
			}

		}//end loop over leptonsFromZHandle

	}

	InputTag genZedTag("combEle","","TEST");
	Handle<std::vector<reco::CompositeCandidate> > genZedHandle;
	iEvent.getByLabel(genZedTag, genZedHandle);

	if(!genZedHandle.isValid() ){
		//std::cout<<"in evts with two GEN leptons, one tracked, one untracked, both with Z boson mothers, and passed pt cuts"<<std::endl;
		//std::cout<<"did not find an object, created by combining the two GEN leptons, with 60<mass<120"<<std::endl;
		tree->Fill();
		return;
	}


	if(genZedHandle->size() > 0){
		numEvents_cutLvlFour_ += 1;
		genTriggeredEvent_ = 1;

		double maxPtUntracked = 0;

		for(edm::OwnVector<reco::Candidate>::const_iterator untracked=untrackedLeptHandle->begin(); untracked != untrackedLeptHandle->end(); untracked++){
			if(untracked->pt() > maxPtUntracked){
				maxPtUntracked = 0;
				maxPtUntracked = untracked->pt();
				gen_trackless_pT_ = untracked->pt();
				gen_trackless_eta_ = untracked->eta();
				gen_trackless_phi_ = untracked->phi();

			}

		}//end loop over untracked gen electrons and positrons

		double maxPtTracked = 0;

		for(edm::OwnVector<reco::Candidate>::const_iterator tracked=trackedLeptHandle->begin(); tracked != trackedLeptHandle->end(); tracked++){
			if(tracked->pt() > maxPtTracked){
				maxPtTracked = 0;
				maxPtTracked = tracked->pt();
				gen_tracked_pT_ = tracked->pt();
				gen_tracked_eta_ = tracked->eta();
				gen_tracked_phi_ = tracked->phi();
			}

		}//end loop over tracked gen electrons and positrons
		
		GetTrackedTriggerObjects(iEvent, gen_tracked_eta_, gen_tracked_phi_, .5);
		
		if(matched_tracked_pT_ > 1.) GetMatchedTriggerObjects(iEvent, gen_trackless_eta_, gen_trackless_phi_, .5);
	}



	if(matched_tracked_pT_ > 1. && matched_pT_ > 1.){
		//if this is true then compute the dilepton mass of the two HLT objects which fired the trigger
		double hlt_mLLSqd = 2*matched_tracked_pT_*matched_pT_*(TMath::CosH(matched_tracked_eta_ - matched_eta_) - TMath::Cos(matched_tracked_phi_ - matched_phi_) );
		if(hlt_mLLSqd > 0.) hlt_mLL_ = TMath::Sqrt(hlt_mLLSqd);

	}


	//that's all folks!
	tree->Fill();


	/*
	numEvents_cutLvlZero_ += 1;

	InputTag genParticleTag("genParticles","","SIM");
	Handle<std::vector<reco::GenParticle> > genPart;
	iEvent.getByLabel(genParticleTag, genPart);

	//std::cout<<"declared and initialized handle object to reco::GenParticle collection"<<std::endl;

	double gPt=0;

	//the last two elements in these vectors represent the leading (last element) and subleading (2nd to last element) GEN electrons
	std::vector<double> genElectronPTs;
	std::vector<double> genElectronEtas;
	std::vector<double> genElectronPhis;
	bool foundElectron = false;
	bool foundPositron = false;

	for(std::vector<reco::GenParticle>::const_iterator genIt=genPart->begin(); genIt != genPart->end(); genIt++){

		//it seems each of the gen electrons and positrons only have 1 mother
		if( std::fabs(genIt->pdgId()) == 11 && std::fabs(genIt->mother(0)->pdgId() ) == 23 ){
			//numGenLeptonsFromZ_ += 1.0;
			if(genIt->pdgId() == 11) foundElectron = true;
			if(genIt->pdgId() == -11) foundPositron = true;
			gPt = genIt->pt();
			addToPtSortedVector(genElectronPTs,gPt);	//the last element in genElectronPTs is the largest element in the vector
		}//end filter which saves kinematic info for GEN electrons and positrons which came from a Z decay 

	}//end loop over GenParticle

	if(foundElectron && foundPositron) numEvents_cutLvlOne_ += 1;

	unsigned int length = genElectronPTs.size();

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



	//see if the event contains the two necessary GEN electrons/positrons from a Z decay to fire the trigger
	bool has; 
	
	for(unsigned int i=0; i<length ; i++){
		//see if the event contains two gen electrons which came from a Z boson. One with pT > 15.0, other with pT > 27.0
		if(genElectronPTs[i] > 15.0 && std::fabs(genElectronEtas[i]) >= 2.5 && std::fabs(genElectronEtas[i]) < 3.0){
			haveTracklessEleCandPartOne = true;
			tracklessEleIndexPartOne += i;
			break;
		}
	}
	for(unsigned int i=0; i<length ; i++){
		//see if the event contains a tracked gen electron which came from a Z boson with pT > 27.0
		if(genElectronPTs[i] > 27.0 && std::fabs(genElectronEtas[i]) < 2.5 && haveTracklessEleCand ){
			//hasGenMatchedTrackedElectron(iEvent, genElectronEtas[i], genElectronPhis[i]);
			incrementEfficiencyDenominator();
			gen_tracked_pT_ = genElectronPTs[i];	//save the pT, eta, and phi of the tracked gen electron to calculate M_ee
			gen_tracked_eta_ = genElectronEtas[i];
			gen_tracked_phi_ = genElectronPhis[i];
			gen_trackless_pT_ = genElectronPTs[tracklessEleIndex];	//save the pT, eta, and phi of the trackless gen electron to calculate M_ee
			gen_trackless_eta_ = genElectronEtas[tracklessEleIndex];
			gen_trackless_phi_ = genElectronPhis[tracklessEleIndex];
			double mLLSqd = 2*gen_tracked_pT_*gen_trackless_pT_*(TMath::CosH(gen_tracked_eta_ - gen_trackless_eta_) - TMath::Cos(gen_tracked_phi_ - gen_trackless_phi_ )  );
			if(mLLSqd > 0.) genMLL_ = TMath::Sqrt(mLLSqd);
			genTriggeredEvent_ = 1.0;
			GetTrackedTriggerObjects(iEvent, gen_tracked_eta_, gen_tracked_phi_, maxDRForMatch);
			break;
		}
	}


	//in any event of DY->ee MC there are never more than 2 GEN electrons/positrons which come from a Z decay
	if(genTriggeredEvent_ ==1){
		//if genTriggeredEvent_ = 1 then there is one GEN electron with pT > 15.0 in the trackless EE region ( 2.5 <= abs(eta) < 3.0 ) 
		//and one GEN electron with pT > 27.0 in the tracker ( abs(eta) < 2.5)
		GetMatchedTriggerObjects(iEvent, tracklessModNames, gen_trackless_eta_, gen_trackless_phi_, maxDRForMatch);
		std::cout<<"# of events that should have fired trigger, based on GEN info, is "<< getEfficiencyDenominator() << std::endl;

	}

	
	//save the pT and eta of the two gen electrons, even if their pT and/or eta values are not sufficient to fire the trigger
	if(length >= 2){
		gen_l2_eta_ = genElectronEtas[length-2];
		gen_l2_phi_ = genElectronPhis[length-2];
		gen_l2_pT_ = genElectronPTs[length-2];

		gen_l1_phi_ = genElectronPhis[length-1];
		gen_l1_eta_ = genElectronEtas[length-1];
		gen_l1_pT_ = genElectronPTs[length-1];
	}

	*/
	


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
doubleEleTracklessAnalyzer::beginJob()
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
doubleEleTracklessAnalyzer::endJob() 
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
doubleEleTracklessAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
doubleEleTracklessAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
doubleEleTracklessAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
doubleEleTracklessAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
doubleEleTracklessAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

/*
void doubleEleTracklessAnalyzer::InitNewTree(void){

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
void doubleEleTracklessAnalyzer::TreeSetSingleElectronVar(const pat::Electron& electron1, int index){

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

void doubleEleTracklessAnalyzer::TreeSetSingleElectronVar(const reco::SuperCluster& electron1, int index){

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

void doubleEleTracklessAnalyzer::TreeSetDiElectronVar(const pat::Electron& electron1, const reco::SuperCluster& electron2){
  
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
DEFINE_FWK_MODULE(doubleEleTracklessAnalyzer);
