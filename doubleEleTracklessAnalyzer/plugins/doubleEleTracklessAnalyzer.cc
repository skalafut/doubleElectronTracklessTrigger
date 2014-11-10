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
#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EgammaReco/interface/ClusterShape.h"
#include "DataFormats/EgammaReco/interface/ClusterShapeFwd.h"
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
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





//
// class declaration
//

class doubleEleTracklessAnalyzer : public edm::EDAnalyzer {
   public:
      explicit doubleEleTracklessAnalyzer(const edm::ParameterSet&);
      ~doubleEleTracklessAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
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




      /*
	 void makeAndSaveSingleHistoAndFit(TString title, TString filePostfix, TString canvName, TString legEntry, const std::string histName, const std::string fitName, bool doLogYAxis){
	 TString longPathName = "/eos/uscms/store/user/skalafut/HGCal/chargedPionGun_PFCands/analyzed/plots/analyzed_chgdPionGun_PFCandidate_";

	 TH1F * histogram = hists_.find(histName.c_str())->second;
	 TF1 * fitCurve = fits_.find(fitName.c_str())->second;
	 TString saveFileType = ".jpg";
	 TString canvasName = canvName;
//std::cout<<"line 143"<<std::endl;

gStyle->SetOptFit(111);

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
fitCurve->Draw("SAME");
leg111->Draw();

c111->SaveAs(longPathName+filePostfix+saveFileType, "recreate");

}//end makeAndSaveSingleHistoAndFit(...)

*/


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

    //typedef std::pair<const trigger::TriggerObject*, double> trig_dr_pair;
    //typedef std::vector<trig_dr_pair> trig_dr_vec;
  
    //calculates delta R between two specified (eta, phi) points, and returns the value of delta R
    double deltaR(const double ETA, const double PHI, const double eta, const double phi){
	double deltaEta = ETA-eta;
	double deltaPhi = PHI-phi;
	double dR = TMath::Sqrt( TMath::Power(deltaEta,2) + TMath::Power(deltaPhi,2) );
	return dR;

    }

void GetMatchedTriggerObjects(
		const edm::Event& iEvent,
		const std::vector<std::string>& trig_names,
		const double ETA, const double PHI, const double DR_CUT
		) {
	/*
	 * Find all trigger objects that match a vector of trigger names and
	 * are within some minimum dR of a specified eta and phi. Return them
	 * as a vector of pairs of the object, and the dr.
	 */
	// If our vector is empty or the first item is blank
	if (trig_names.size() == 0 || trig_names[0].size() == 0) {
		return;
	}

	// Load Trigger Objects
	edm::InputTag hltTrigInfoTag("hltTriggerSummaryRAW","","TEST");
	edm::Handle<trigger::TriggerEventWithRefs> trig_event;

	iEvent.getByLabel(hltTrigInfoTag, trig_event);
	if (!trig_event.isValid() ){
		std::cout << "No valid hltTriggerSummaryRAW." << std::endl;
		return;
	}

	//trig_dr_vec* out_v = new trig_dr_vec();
	// Loop over triggers, filter the objects from these triggers, and then try to match
	for (auto& trig_name : trig_names) {
		// Loop over triggers, filter the objects from these triggers, and then try to match
		//std::cout<<"looping over trig module names"<<std::endl;
		edm::InputTag filter_tag(trig_name, "", "TEST");

		// the method filterIndex() is defined for TriggerEvent and TriggerEventWithRefs objects!
		trigger::size_type filter_index = trig_event->filterIndex(filter_tag);
		//std::cout<<"declared and initialized a filter_index"<<std::endl;
		//std::cout<< filter_index <<std::endl;
		
		if(filter_index < trig_event->size()) { // Check that the filter is in triggerEvent
			std::cout<<"filter number "<< filter_index<< " is in the trigger event"<<std::endl;

			for(int i=0; i<=100; i++){
				//loop over all possible photon ids
				//most ids are 81 and 91

				//std::vector<edm::Ref<std::vector<reco::RecoEcalCandidate> > > tracklessEleRefs;
			
				
				//trigger::VRphoton tracklessEleRefs = (new trigger::TriggerRefsCollections())->photonRefs();
				trigger::VRphoton tracklessEleRefs;

				//this getObjects() call fills tracklessEleRefs with references to reco::RecoEcalCandidate objects
				trig_event->getObjects(filter_index, i, tracklessEleRefs);
				//std::cout<< tracklessEleRefs.size() <<std::endl;

				//now loop over all elements in tracklessEleRefs
				for(unsigned int j=0; j<tracklessEleRefs.size() ; j++){

					//const reco::RecoEcalCandidate * temp = tracklessEleRefs[j].get();
					double energy = tracklessEleRefs[j]->energy();
					std::cout<<"trackless electron has energy equal to "<< energy <<std::endl;

/*
					double energy = (temp->RecoCandidate::superCluster() )->rawEnergy();
					std::cout<< "trackless electron SC has energy equal to "<< energy <<std::endl;
					double eta = ( temp->RecoCandidate::superCluster() )->CaloCluster::eta();
					std::cout<<"trackless electron SC has eta equal to "<< eta <<std::endl;
*/

					//std::cout<<"supercluster energy is "<< theSC->rawEnergy() <<std::endl;
					//std::cout<<"supercluster eta is "<< theSC->eta() <<std::endl;	//eta() defined in CaloCluster class, SC inherits from this class


				}//end loop over all elements in tracklessEleRefs vector

			}//end loop over photon id values


/*
			const trigger::Keys& trig_keys = trig_event->filterKeys(filter_index);

			const trigger::TriggerObjectCollection& trig_obj_collection(trig_event->getObjects());
			// Get the objects from the trigger keys
			for (auto& i_key : trig_keys) {
				const trigger::TriggerObject* trig_obj = &trig_obj_collection[i_key];
				const double DR = deltaR(ETA, PHI, trig_obj->eta(), trig_obj->phi());
				std::cout<<"DR equals "<< DR << std::endl;
				// Do Delta R matching, and assign a new object if we have a
				// better match
				if (DR < DR_CUT) {
					out_v->push_back(std::make_pair(trig_obj, DR));
					std::cout<<"added an element to out_v vector in GetMatchedTriggerObjects"<<std::endl;
				}
			}
*/


		}
	}
	//return out_v;
}


/*
    const trigger::TriggerObject* GetBestMatchedTriggerObject(
            const edm::Event& iEvent,
            const std::vector<std::string>& trig_names,
            const double ETA, const double PHI
            ) {
        // Given the ETA and PHI of a particle, and a list of trigger paths,
        //  returns the trigger object from those paths that is closest to the
         // given coordinates. 
        //RESET MIN_DR to a reasonable value later
	const double MIN_DR = 2;
        const trig_dr_vec* trig_vec = GetMatchedTriggerObjects(iEvent, trig_names, ETA, PHI, MIN_DR);

        double best_dr = 1.;
        const trigger::TriggerObject* trig_obj = NULL;
        for (auto& i_obj : *trig_vec) {
            if (i_obj.second < best_dr) {
                best_dr = i_obj.second;
                trig_obj = i_obj.first;
            }
        }
        return trig_obj;
    }


    bool TriggerMatch(
            const edm::Event& iEvent,
            const std::vector<std::string>& trig_names,
            const double ETA, const double PHI, const double DR_CUT
            ) {
        // Get the vector and see if there are objects
        const trig_dr_vec* zev = GetMatchedTriggerObjects(iEvent, trig_names, ETA, PHI, DR_CUT);
        if (zev != NULL && zev->size() >= 1) {
            return true;
        } else {
            return false;
        }
    }
*/

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

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;

   //PFRecHit based plots
   /*
   hists_["EnergyFrxnVsLambda"]=fs->make<TH1D>("EnergyFrxnVsLambda","temp Energy fraction vs hadronic interaction length; hadronic int length #lambda; Energy fraction",400,0.,10.9);
   hists_["FinalEnergyFrxnVsLambda"]=fs->make<TH1D>("FinalEnergyFrxnVsLambda","Energy fraction vs hadronic interaction length; hadronic int length #lambda; Energy fraction",400,0.,10.9);

   hists_["EE_PFRecHit_energy"]=fs->make<TH1D>("EE_PFRecHit_energy","Energy of rechits in HGCEE in GeV",100,0.,0.001);  
   hists_["HEF_PFRecHit_energy"]=fs->make<TH1D>("HEF_PFRecHit_energy","Energy of rechits in HGCHEF in GeV",100,0.,0.001);  
   hists_["HEB_PFRecHit_energy"]=fs->make<TH1D>("HEB_PFRecHit_energy","Energy of rechits in HGCHEB in GeV",100,0.,0.01);  

   */


   //these four plots DO NOT pull PFRecHit objects from PFCluster objects, they are simply showing all of the PFRecHit objects as a fxn of Z distance for all events
   /*
   hists_["EE_PFRecHit_z"]=fs->make<TH1D>("EE_PFRecHit_z","Z position of rechits in HGCEE in centimeters",150,300.,360.);  //this histo is made to show the Z distance between each Si layer in HGCEE
   hists_["HEF_PFRecHit_z"]=fs->make<TH1D>("HEF_PFRecHit_z","Z position of rechits in HGCHEF in centimeters",100,350.,460.);  //this histo is made to show the Z distance between each Si layer in HGCHEF
   hists_["HEB_PFRecHit_z"]=fs->make<TH1D>("HEB_PFRecHit_z","Z position of rechits in HGCHEB in centimeters",100,400.,600.);  //this histo is made to show the Z distance between each scintillator layer in HGCHEB
   */

   //hists_["All_PFRecHit_z"]=fs->make<TH1D>("All_PFRecHit_z","Z position of all HGC PFRecHits ; distance from IP (cm);",500,310.,560.);  //this histo is made to show the Z distance between each sensitive layer of HGC (Si or scintillator) 



   /*
   histsThree_["PFClusterSum_HCALovrECAL_gen_eta_energy"]=fs->make<TH3D>("PFClusterSum_HCALovrECAL_gen_eta_energy","Reco E_HCAL/E_ECAL for Pi+ vs gen Pi+ energy and eta", 100, 0., 210., 15, 1.55, 3.0, 30, 0., 15.);

   histsThree_["EEPFCluster_deltaR_energy"]=fs->make<TH3D>("EEPFCluster_deltaR_energy","#Delta#eta and #Delta#phi between EE PFClusters and generator pi+ as a function of PFCluster energy", 632, -3.16, 3.16, 40, -1.5, 1.5, 200, 0., 100.);
 
   histsThree_["HEFPFCluster_deltaR_energy"]=fs->make<TH3D>("HEFPFCluster_deltaR_energy","#Delta#eta and #Delta#phi between HEF PFClusters and generator pi+ as a function of PFCluster energy", 632, -3.16, 3.16, 40, -1.5, 1.5, 200, 0., 100.);

   histsThree_["HEBPFCluster_deltaR_energy"]=fs->make<TH3D>("HEBPFCluster_deltaR_energy","#Delta#eta and #Delta#phi between HEB PFClusters and generator pi+ as a function of PFCluster energy", 632, -3.16, 3.16, 40, -1.5, 1.5, 100, 0., 50.);
 
   histsThree_["MaxEEPFCluster_deltaR_energy"]=fs->make<TH3D>("MaxEEPFCluster_deltaR_energy","#Delta#eta and #Delta#phi between highest energy EE PFClusters and generator pi+ as a function of PFCluster energy", 632, -3.16, 3.16, 40, -1.5, 1.5, 200, 0., 300.);
 
   histsThree_["MaxHEFPFCluster_deltaR_energy"]=fs->make<TH3D>("MaxHEFPFCluster_deltaR_energy","#Delta#eta and #Delta#phi between highest energy HEF PFClusters and generator pi+ as a function of PFCluster energy", 632, -3.16, 3.16, 40, -1.5, 1.5, 200, 0., 300.);

   histsThree_["MaxHEBPFCluster_deltaR_energy"]=fs->make<TH3D>("MaxHEBPFCluster_deltaR_energy","#Delta#eta and #Delta#phi between highest energy HEB PFClusters and generator pi+ as a function of PFCluster energy", 632, -3.16, 3.16, 40, -1.5, 1.5, 100, 0., 300.);

  */ 



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
   
   //////////////////////////////////////////////////////////////////////////
   //get the energy of the generator lvl pi+
   //plot E_gen
   //at the end of the run store the mean of the E_gen histogram 
   /////////////////////////////////////////////////////////////////////////

/*
   edm::Handle<std::vector<reco::GenParticle> > genPart;
   iEvent.getByLabel("genParticles",genPart);
 
   float gEn =0;	//energy of a generator chgd pion
   float gEta = 0;
   float gPhi = 0;	//eta and phi of generator chgd pion
   int numGenParticles = 0;	//keeps track of the total number of gen lvl particles in the event

   for(std::vector<reco::GenParticle>::const_iterator genIt=genPart->begin(); genIt != genPart->end(); genIt++){
	   numGenParticles++;
	   if(genIt->pdgId() == 211){
		  //if the genIt pdgId is +211 then the particle is a pi+
		  gEta = genIt->eta();
		  gPhi = genIt->phi();
		  gEn = (genIt->pt())*(TMath::CosH(genIt->eta()));
	   }

   }//end loop over GenParticle
*/
   std::vector<std::string> tracklessModNames;
   //tracklessModNames.push_back("hltEgammaCandidatesWrapperUnseeded");
   tracklessModNames.push_back("hltEG15WPYYtracklessEtFilterUnseeded");
   tracklessModNames.push_back("hltEle15WPYYtracklessEcalIsoFilter");
   tracklessModNames.push_back("hltEle15WPYYtracklessHEFilter");
   tracklessModNames.push_back("hltEle15WPYYtracklessHcalIsoFilter");
   std::cout<<"added four filter module names to a vector of strings"<<std::endl;

   GetMatchedTriggerObjects(iEvent, tracklessModNames, 2.5, 2.0, 5);
   

   //std::cout<< "pT of " << bestMatch->pt() << "  eta of "<< bestMatch->eta() <<std::endl;
/*   
   if( bestMatch->pt() >= 15 && TMath::Abs(bestMatch->eta()) >= 2.4 && TMath::Abs(bestMatch->eta()) <= 3.0 ){
	std::cout<<"found an electron candidate that passes Ecal iso, H/E, Hcal iso, and pT and eta requirements"<<std::endl;
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
}

// ------------ method called once each job just after ending the event loop  ------------
void 
doubleEleTracklessAnalyzer::endJob() 
{

	/*
	for(unsigned int j=0; j<finalEnergyFrxns.size();j++){
		//std::cout<<"finalEnergyFrxnBinNums element # "<<j<<" equals "<< finalEnergyFrxnBinNums[j] <<std::endl;
		//std::cout<<"finalEnergyFrxns element # "<<j<<" equals "<< finalEnergyFrxns[j] <<std::endl;
		set1DBinContents("FinalEnergyFrxnVsLambda", finalEnergyFrxnBinNums[j], finalEnergyFrxns[j]);
	}

	for(int e=0; e<getXBins("All_PFRecHit_z") ; e++){
		if(get1DBinContents("All_PFRecHit_z",e) > 0.0 ){
			std::cout<< get1DUpperBinEdge("All_PFRecHit_z",e) << std::endl;
		}

	}
	*/


	//makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between PFCandidate objects and gen pi+ objects as fxn of PFCandidate energy; #Delta #phi (rad); #Delta #eta; PFCand energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_PFCand_and_gen_chgd_pion_vs_PFCand_energy","24","","PFCandidate_deltaR_energy", false);


	/*
	makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between EE PFClusters and generator pi+ as fxn of PFCluster energy;#Delta #phi (rad); #Delta #eta; PFCluster energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_EEPFClust_and_gen_chgd_pion_vs_EEPFClust_energy","31","","EEPFCluster_deltaR_energy", false);
   
	makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between HEF PFClusters and generator pi+ as fxn of PFCluster energy;#Delta #phi (rad); #Delta #eta; PFCluster energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_HEFPFClust_and_gen_chgd_pion_vs_HEFPFClust_energy","32","","HEFPFCluster_deltaR_energy", false);

	makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between HEB PFClusters and generator pi+ as fxn of PFCluster energy;#Delta #phi (rad); #Delta #eta; PFCluster energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_HEBPFClust_and_gen_chgd_pion_vs_HEBPFClust_energy","33","","HEBPFCluster_deltaR_energy", false);
 
	makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between highest energy EE PFClusters and generator pi+ as fxn of PFCluster energy;#Delta #phi (rad); #Delta #eta; PFCluster energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_max_energy_EEPFClust_and_gen_chgd_pion_vs_EEPFClust_energy","34","","MaxEEPFCluster_deltaR_energy", false);
   
	makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between highest energy HEF PFClusters and generator pi+ as fxn of PFCluster energy;#Delta #phi (rad); #Delta #eta; PFCluster energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_max_energy_HEFPFClust_and_gen_chgd_pion_vs_HEFPFClust_energy","35","","MaxHEFPFCluster_deltaR_energy", false);

	makeAndSaveSingle3DHisto("#Delta #eta and #Delta #phi between highest energy HEB PFClusters and generator pi+ as fxn of PFCluster energy;#Delta #phi (rad); #Delta #eta; PFCluster energy (GeV)","chgdPi_pT50_NoPU_deltaR_btwn_max_energy_HEBPFClust_and_gen_chgd_pion_vs_HEBPFClust_energy","36","","MaxHEBPFCluster_deltaR_energy", false);
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

//define this as a plug-in
DEFINE_FWK_MODULE(doubleEleTracklessAnalyzer);
