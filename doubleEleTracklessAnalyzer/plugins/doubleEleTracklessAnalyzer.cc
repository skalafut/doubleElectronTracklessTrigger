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

void GetMatchedTriggerObjects(
		const edm::Event& iEvent,
		const std::vector<std::string>& trig_names, const double eta, const double phi, const double dRForMatch)
{
	/*
	 * Find all trigger objects that match a vector of trigger names and
	 * are within some minimum dR of a specified eta and phi.
	 * also see if there is a gen electron in the event with pT > 10 GeV that is heading into trackless EE
	 */
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
	//reset all of the private member vars which are saved to TTree to zero
	gen_l1_pT_=-1;	//pT of leading gen electron
	gen_l1_eta_=-7;	//eta of leading gen electron
	gen_l1_phi_=-7;	//phi of leading gen electron
	gen_l2_pT_=-1;	//pT of subleading gen electron
	gen_l2_eta_=-7;	//eta of subleading gen electron
	gen_l2_phi_=-7;	//phi of subleading gen electron
	gen_trackless_pT_=-1;	//pT of gen electron in trackless EE
	gen_trackless_eta_=-7;	//eta of gen electron in trackless EE
	gen_trackless_phi_=-7;	//phi of gen electron in trackless EE
	gen_tracked_pT_=-1;	//pT of gen electron in tracked ECAL
	gen_tracked_eta_=-7;	//eta of gen electron in tracked ECAL
	gen_tracked_phi_=-7;	//phi of gen electron in tracked ECAL
	genTriggeredEvent_ = -1;
   	genMLL_ = -1;
	//consistentGenAndHLTEvent_ = -1;
	//numGenLeptonsFromZ_ = 0;
	//trackedGenToRecoMatch_ = 0;	//equals 1 if the tracked gen electron is matched to a reco gsf electron

	matched_pT_=-1;
	matched_eta_=-7;
	matched_phi_=-7;
	matched_ecalIso_=999;
	matched_hcalIso_=999;
	matched_hOverE_=999;
	matched_ecalClusterShape_=999;
	matched_ecalClusterShape_SigmaIEtaIEta_=999;
	numUnmatchedCandidates_=0;

	//needed to compute dilepton mass at trigger level with HLT objects firing tracked and trackless legs of trigger
	matched_tracked_pT_=-1;
	matched_tracked_eta_=-7;
	matched_tracked_phi_=-7;

	hlt_mLL_ = -1;

	//reco_tracked_pT_=-1;
	//reco_tracked_eta_=-7;
	//reco_tracked_phi_=-7;
	//reco_untracked_pT_=-1;
	//reco_untracked_eta_=-7;
	//reco_untracked_phi_=-7;


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

//gen lepton variables going into TTree
//double numGenLeptonsFromZ_;		//number of generator e- or e+ which have Z boson mothers
double gen_l1_pT_;	//pT of leading gen electron
double gen_l1_eta_;	//eta of leading gen electron
double gen_l1_phi_;	//phi of leading gen electron
double gen_l2_pT_;	//pT of subleading gen electron
double gen_l2_eta_;	//eta of subleading gen electron
double gen_l2_phi_;	//phi of subleading gen electron
double gen_trackless_pT_;	//pT of gen electron in trackless EE
double gen_trackless_eta_;	//eta of gen electron in trackless EE
double gen_trackless_phi_;	//phi of gen electron in trackless EE
double gen_tracked_pT_;	//pT of gen electron in tracked ECAL
double gen_tracked_eta_;	//eta of gen electron in tracked ECAL 
double gen_tracked_phi_;	//phi of gen electron in tracked ECAL 
double genTriggeredEvent_;	// equals +1 for events which should have fired trackless and tracked legs of trigger based on GEN lvl info, equals -1 otherwise

//non-negative for events where there are two GEN electrons with a Z boson mother, one GEN electron is tracked with pT > 27, and other
//GEN electron is in trackless EE with pT > 15 
double genMLL_;

//double consistentGenAndHLTEvent_;	//equals +1 when GEN info is consistent with HLT firing, equals -1 otherwise
//int trackedGenToRecoMatch_;		//equals 1 when the tracked gen electron is matched to a reco gsf electron within deltaR = 0.2

//variables corresponding to matched HLT object in trackless EE which will go into TTree
double matched_pT_;
double matched_eta_;
double matched_phi_;
double matched_ecalIso_;
double matched_hcalIso_;
double matched_hOverE_;
double matched_ecalClusterShape_;
double matched_ecalClusterShape_SigmaIEtaIEta_;
double numUnmatchedCandidates_;

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
   
   //hists_["gsfElectronDeltaR"]=fs->make<TH1D>("gsfElectronDeltaR","#DeltaR gsfElectron to GEN tracked electron; #DeltaR;",100, 0., 0.6);
   //hists_["superclusterDeltaR"]=fs->make<TH1D>("superclusterDeltaR","#DeltaR supercluster to GEN trackless electron in Z peak evts; #DeltaR;",100, 0., 0.6);
   //hists_["superclusterHLTDeltaR"]=fs->make<TH1D>("superclusterHLTDeltaR","#DeltaR supercluster to no track HLT object; #DeltaR;",100,0.,0.6);
   //hists_["gsfHLTDeltaR"]=fs->make<TH1D>("gsfHLTDeltaR","#DeltaR gsf electron to tracked HLT object; #DeltaR;",100,0.,0.6);
   hists_["tracklessGENToHLTDeltaR"]=fs->make<TH1D>("tracklessGENToHLTDeltaR","#DeltaR gen trackless e- to ALL trackless HLT objects passing trigger; #DeltaR;",100,0.,0.4);
   hists_["trackedGENToHLTDeltaR"]=fs->make<TH1D>("trackedGENToHLTDeltaR","#DeltaR gen tracked e- to ALL tracked HLT objects passing trigger; #DeltaR;",100,0.,0.4);
  
   
   /*
   hists_["GenEta_leadingEle"]=fs->make<TH1D>("GenEta_leadingEle","#eta of leading generator electron; electron #eta;",300,-3.0,3.0);
   hists_["GenEta_subLeadingEle"]=fs->make<TH1D>("GenEta_subLeadingEle","#eta of sub-leading generator electron; electron #eta;",300,-3.0,3.0);

   hists_["GenPt_leadingEle"]=fs->make<TH1D>("GenPt_leadingEle","P_{T} of leading generator electron; electron p_{T} (GeV);",300,0.0,100.0);
   hists_["GenPt_subLeadingEle"]=fs->make<TH1D>("GenPt_subLeadingEle","P_{T} of sub-leading generator electron; electron p_{T} (GeV);",300,0.0,100.0);

   hists_["GenPt_untrackedEle"]=fs->make<TH1D>("GenPt_untrackedEle","P_{T} of untracked generator electron in events with one tracked electron and one untracked electron ; untracked electron p_{T} (GeV);",300,0.0,100.0);


   hists_["EventFraction"]=fs->make<TH1D>("EventFraction","Fraction of events with zero, one, and two untracked GEN electrons in EE; ; event fraction",3,0.0,3.0);

   hists_["HLTRecoEff"]=fs->make<TH1D>("HLTRecoEff","Efficiency of trackless leg of HLT path; ; efficiency",1,0.0,1.0);



   //THIS declaration is here for reference

   //histsThree_["PFClusterSum_HCALovrECAL_gen_eta_energy"]=fs->make<TH3D>("PFClusterSum_HCALovrECAL_gen_eta_energy","Reco E_HCAL/E_ECAL for Pi+ vs gen Pi+ energy and eta", 100, 0., 210., 15, 1.55, 3.0, 30, 0., 15.);

   */
   
   tree=fs->make<TTree>("doubleEleTrigger","Summary of trackless double electron trigger event info");
   //tree->Branch("numGenLeptonsFromZ_",&numGenLeptonsFromZ_,"numGenLeptonsFromZ_/D");
   tree->Branch("gen_l1_pT_",&gen_l1_pT_,"gen_l1_pT_/D");
   tree->Branch("gen_l2_pT_",&gen_l2_pT_,"gen_l2_pT_/D");
   tree->Branch("gen_l2_eta_",&gen_l2_eta_,"gen_l2_eta_/D");
   tree->Branch("gen_l1_eta_",&gen_l1_eta_,"gen_l1_eta_/D");
   tree->Branch("gen_l2_phi_",&gen_l2_phi_,"gen_l2_phi_/D");
   tree->Branch("gen_l1_phi_",&gen_l1_phi_,"gen_l1_phi_/D");
   tree->Branch("gen_trackless_eta_",&gen_trackless_eta_,"gen_trackless_eta_/D");
   tree->Branch("gen_trackless_pT_",&gen_trackless_pT_,"gen_trackless_pT_/D");
   tree->Branch("gen_trackless_phi_",&gen_trackless_phi_,"gen_trackless_phi_/D");
   tree->Branch("gen_tracked_eta_",&gen_tracked_eta_,"gen_tracked_eta_/D");
   tree->Branch("gen_tracked_pT_",&gen_tracked_pT_,"gen_tracked_pT_/D");
   tree->Branch("gen_tracked_phi_",&gen_tracked_phi_,"gen_tracked_phi_/D");
   tree->Branch("genTriggeredEvent_",&genTriggeredEvent_,"genTriggeredEvent_/D");
   tree->Branch("genMLL_",&genMLL_,"genMLL_/D");
   //tree->Branch("consistentGenAndHLTEvent_",&consistentGenAndHLTEvent_,"consistentGenAndHLTEvent_/D");
   //tree->Branch("trackedGenToRecoMatch_",&trackedGenToRecoMatch_,"trackedGenToRecoMatch_/I");


   tree->Branch("matched_pT_",&matched_pT_,"matched_pT_/D");
   tree->Branch("matched_eta_",&matched_eta_,"matched_eta_/D");
   tree->Branch("matched_phi_",&matched_phi_,"matched_phi_/D");
   tree->Branch("matched_ecalIso_",&matched_ecalIso_,"matched_ecalIso_/D");
   tree->Branch("matched_hcalIso_",&matched_hcalIso_,"matched_hcalIso_/D");
   tree->Branch("matched_ecalClusterShape_",&matched_ecalClusterShape_,"matched_ecalClusterShape_/D");
   tree->Branch("matched_ecalClusterShape_SigmaIEtaIEta_",&matched_ecalClusterShape_SigmaIEtaIEta_,"matched_ecalClusterShape_SigmaIEtaIEta_/D");
   tree->Branch("matched_hOverE_",&matched_hOverE_,"matched_hOverE_/D");
   tree->Branch("numUnmatchedCandidates_",&numUnmatchedCandidates_,"numUnmatchedCandidates_/D");

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

	//bool incrementedEffDenom = false;


	/**/
	std::vector<std::string> tracklessModNames;
	//tracklessModNames.push_back("hltL1sL1ZeroBias");
	//tracklessModNames.push_back("hltEGL1SingleEG20ORL1SingleEG22Filter");	//this module is called in the Ele27 sequence (this sequence looks for a tracked electron candidate)
	//tracklessModNames.push_back("hltL1sL1SingleEG20ORL1SingleEG22");	//this appears in the path for the double electron trigger, before the Ele27 and Ele15 sequences

	/*tracklessModNames.push_back("hltEgammaCandidatesWrapperUnseeded");
	tracklessModNames.push_back("hltEG15WPYYtracklessEtFilterUnseeded");
	tracklessModNames.push_back("hltEle15WPYYtracklessEcalIsoFilter");
	tracklessModNames.push_back("hltEle15WPYYtracklessHEFilter");
	*/
	tracklessModNames.push_back("hltEle15WPYYtracklessHcalIsoFilter");

	//uncomment these two lines when analyzing bkgnd files or unmatched signal files (to compute signal trigger rate)
	//GetMatchedTriggerObjects(iEvent, tracklessModNames, 0.0, 0.0, 20);
	//GetTrackedTriggerObjects(iEvent, 0.0, 0.0, 20);
	

	//uncomment this when analyzing matched signal files to determine Z->ee trigger efficiency
	/**/
	double maxDRForMatch = 0.1;

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
			//numGenLeptonsFromZ_ += 1.0;
			gPt = genIt->pt();
			addToPtSortedVector(genElectronPTs,gPt);	//the last element in genElectronPTs is the largest element in the vector
		}//end filter which saves kinematic info for GEN electrons and positrons which came from a Z decay 

	}//end loop over GenParticle

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

	if(matched_tracked_pT_ > 0. && matched_pT_ > 0.){
		//if this is true then compute the dilepton mass of the two HLT objects which fired the trigger
		double hlt_mLLSqd = 2*matched_tracked_pT_*matched_pT_*(TMath::CosH(matched_tracked_eta_ - matched_eta_) - TMath::Cos(matched_tracked_phi_ - matched_phi_) );
		if(hlt_mLLSqd > 0.) hlt_mLL_ = TMath::Sqrt(hlt_mLLSqd);

	}

	/**/
	

	//that's all folks!
	tree->Fill();


	/*

	   OLD no longer needed as of December 19 2014
	//first bin on the plot is bin # 1!!

	for(int i=1; i<=getXBins("EventFraction"); i++){
		if( getXBins("EventFraction") < 3) break;	//shouldn't need this, but just in case
		if(i==1 && !oneUntrackedElectron && !twoUntrackedElectrons ){
			set1DBinContents("EventFraction",i, get1DBinContents("EventFraction",i) + 1.0);
			break;
		}
		
		if(i==2 && oneUntrackedElectron){
			set1DBinContents("EventFraction",i, get1DBinContents("EventFraction",i) + 1.0);
			break;
		}
		
		if(i==3 && twoUntrackedElectrons){
			set1DBinContents("EventFraction",i, get1DBinContents("EventFraction",i) + 1.0);
			break;
		}

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
