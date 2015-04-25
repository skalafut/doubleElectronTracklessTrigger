#include <TTree.h>
#include <TChain.h>
#include <TFile.h>
#include <TROOT.h>
#include <TCanvas.h>
#include <TString.h>
#include <TStyle.h>
#include <TCut.h>
#include <TH1F.h>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include "TMath.h"

using namespace std;

/**use this to make and save a histogram from a single TTree branch
 * plotArgs is used in TTree::Draw, and could be something like "etaGenEle[0]>>leadingEta(100,-3.0,3.0)"
 * histName is the name of the histogram object, and is contained in plotArgs
 * histTitle and xAxisTitle will be used with pHist
 */
void makeAndSaveSingleTreeHisto(TChain * chain,TString plotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	chain->Draw(plotArgs,filters);
	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
	pHist->SetTitle(histTitle);
	pHist->GetXaxis()->SetTitle(xAxisTitle);
	pHist->SetFillColor(21);	///< sets color of area under drawn curve or hist line to grey
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	else sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");

}//end makeAndSaveSingleTreeHisto()


/**use this fxn to calculate the matching efficiency and uncertainty for signal
 * conditional on reco cuts being passed
 * the input chain can only contain evts which pass the signal gen, L1, and reco cuts
 */
void calcMatchingEffAndUnc(TChain * chain, Float_t & efficiency, Float_t & uncertainty){
	Float_t effDenom = (Float_t) chain->GetEntries();
	TTree * filteredTree = (TTree*) chain->CopyTree("nHltEle>0");
	Float_t effNumer = (Float_t) filteredTree->GetEntries();	///< returns the number of evts passing selection applied in line above
	efficiency = effNumer/effDenom;
	uncertainty = (1/effDenom)*TMath::Sqrt(effNumer*(1 - (effNumer/effDenom) ));

}///end calcMatchingEff()


/**use this fxn to calculate an efficiency and uncertainty on the efficiency given
 * a number of evts N available, and a subset of evts k which pass the cuts
 */
void calcEffAndUnc(Float_t Nevts, Float_t kevts, Float_t & eff, Float_t & uncert){
	//cout<<"max num evts = \t"<< Nevts <<"\t passing evts = \t"<< kevts <<endl;
	eff = kevts/Nevts;
	uncert = (1/Nevts)*TMath::Sqrt(kevts*(1 - (kevts/Nevts) ));
}///end calcEffAndUnc()

/**use this macro to calculate the efficiencies of different selection requirements which are
 * applied to the tuples which are used in scans over sets of trigger cut variables
 *
 * for bkgnd, the efficiencies that I can calculate are:
 * L1 efficiency (fraction of evts which fire L1 trigger)
 * 
 * reco efficiency conditional on L1 (for evts which fire L1 trigger, the fraction of evts
 * which have at least one tracked reco object, one trackless reco object, and the combination
 * of at least one tracked+trackless object has an invariant mass btwn 50 and 130 GeV)
 *
 *
 * for signal, the efficiencies I can calculate are:
 * gen efficiency (frxn of evts with one tracked gen electron with Z mother and pt>27, one
 * trackless gen electron with Z mother and pt>15, and gen dilepton mass btwn 60 and 120 GeV)
 * 
 * L1 efficiency conditional on gen (for evts passing gen cuts, the frxn of evts which fire
 * the L1 trigger)
 * 
 * reco efficiency conditional on L1 (for evts which fire L1 trigger, the frxn of evts with
 * at least one tracked reco object and one trackless reco object whose combined invariant mass
 * is btwn 50 and 130 GeV)
 *
 * matching efficiency conditional on reco (for evts with at least two reco objects with appropriate
 * diobject mass, the frxn of evts where two reco objects are matched to the two gen electrons within
 * dR=0.1)
 *
 */
void calculateEfficiencies(){

	//swap btwn DoubleEG_22_10, DoubleEG_15_10, SingleEG25, and SingleEG40
	//can also use files in from7_4_0_pre9/*_25ns_SingleEG25.root
	///declare TChains needed to compute efficiencies
	TChain * trackedLowPtBkgndChainWithL1Filter = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	trackedLowPtBkgndChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_20to30_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedHighPtBkgndChainWithL1Filter = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	trackedHighPtBkgndChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_30to80_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedVeryHighPtBkgndChainWithL1Filter = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	trackedVeryHighPtBkgndChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_80to170_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");

	TChain * trackedLowPtBkgndChainNoCutsWithL1Filter = new TChain("recoAnalyzerTrackedNoCutsWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndNoCutsWithL1Filter","");
	trackedLowPtBkgndChainNoCutsWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_20to30_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedHighPtBkgndChainNoCutsWithL1Filter = new TChain("recoAnalyzerTrackedNoCutsWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndNoCutsWithL1Filter","");
	trackedHighPtBkgndChainNoCutsWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_30to80_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedVeryHighPtBkgndChainNoCutsWithL1Filter = new TChain("recoAnalyzerTrackedNoCutsWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndNoCutsWithL1Filter","");
	trackedVeryHighPtBkgndChainNoCutsWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_80to170_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");

	TChain * trackedLowPtBkgndChainNoCuts = new TChain("recoAnalyzerTrackedNoCuts/recoTreeBeforeTriggerFiltersTrackedBkgndNoCuts","");
	trackedLowPtBkgndChainNoCuts->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_20to30_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedHighPtBkgndChainNoCuts = new TChain("recoAnalyzerTrackedNoCuts/recoTreeBeforeTriggerFiltersTrackedBkgndNoCuts","");
	trackedHighPtBkgndChainNoCuts->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_30to80_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedVeryHighPtBkgndChainNoCuts = new TChain("recoAnalyzerTrackedNoCuts/recoTreeBeforeTriggerFiltersTrackedBkgndNoCuts","");
	trackedVeryHighPtBkgndChainNoCuts->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_80to170_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");





	TChain * trackedSignalChainWithL1Filter = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedSignalWithL1Filter","");
	trackedSignalChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");

	TChain * tracklessSignalChainWithL1Filter = new TChain("recoAnalyzerTracklessWithL1Filter/recoTreeBeforeTriggerFiltersTracklessSignalWithL1Filter","");
	tracklessSignalChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");





	TChain * matchedTrackedSignalChainWithL1Filter = new TChain("recoAnalyzerMatchedTrackedWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTrackedSignalWithL1Filter","");
	matchedTrackedSignalChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");

	TChain * matchedTrackedSignalChain = new TChain("recoAnalyzerMatchedTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignal","");
	matchedTrackedSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * matchedTracklessSignalChainWithL1Filter = new TChain("recoAnalyzerMatchedTracklessWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTracklessSignalWithL1Filter","");
	matchedTracklessSignalChainWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * matchedTrackedSignalChainNoCutsWithL1Filter = new TChain("recoAnalyzerMatchedTrackedNoCutsWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTrackedSignalNoCutsWithL1Filter","");
	matchedTrackedSignalChainNoCutsWithL1Filter->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * matchedTrackedSignalChainNoCuts = new TChain("recoAnalyzerMatchedTrackedNoCuts/recoTreeBeforeTriggerFiltersMatchedTrackedSignalNoCuts","");
	matchedTrackedSignalChainNoCuts->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");

	TChain * matchedTrackedSignalChainNoCutsHasTracklessAndTracked = new TChain("recoAnalyzerMatchedTrackedNoCutsHasTracklessAndTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignalNoCutsHasTracklessAndTracked","");
	matchedTrackedSignalChainNoCutsHasTracklessAndTracked->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * matchedTrackedSignalChainNoCutsRequireTracked = new TChain("recoAnalyzerMatchedTrackedNoCutsRequireTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignalNoCutsRequireTracked","");
	matchedTrackedSignalChainNoCutsRequireTracked->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * matchedTrackedSignalChainNoCutsRequireTrackless = new TChain("recoAnalyzerMatchedTrackedNoCutsRequireTrackless/recoTreeBeforeTriggerFiltersMatchedTrackedSignalNoCutsRequireTrackless","");
	matchedTrackedSignalChainNoCutsRequireTrackless->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * trackedSignalChainNoCuts = new TChain("recoAnalyzerTrackedNoCuts/recoTreeBeforeTriggerFiltersTrackedSignalNoCuts","");
	trackedSignalChainNoCuts->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");




	Float_t signalGenEff=0, signalL1Eff=0, signalRecoEff=0, signalTrackedMatchingEff=0, signalTracklessMatchingEff=0;
	Float_t signalGenEffUnc=10, signalL1EffUnc=10, signalRecoEffUnc=10, signalTrackedMatchingEffUnc=10, signalTracklessMatchingEffUnc=10;
	Float_t signalRecoTrackedEff=0, signalRecoTracklessEff=0, signalRecoMassCutEff=0;
	Float_t signalRecoTrackedEffUnc=10, signalRecoTracklessEffUnc=10, signalRecoMassCutEffUnc=10;


	///calculate the fraction of evts which have two GEN electrons with Z mother, one of which is in the tracked eta region, the other is
	///in the trackless EE region, and their dilepton mass is btwn 60 and 120 GeV
	calcEffAndUnc((Float_t) (trackedSignalChainNoCuts->GetEntries()), (Float_t) (matchedTrackedSignalChainNoCuts->GetEntries()), signalGenEff, signalGenEffUnc);

	///calculate the fraction of evts which already passed the GEN cuts and have at least one RecoEcalCandidate within tracker eta coverage 
	calcEffAndUnc((Float_t) (matchedTrackedSignalChainNoCuts->GetEntriesFast()), (Float_t) (matchedTrackedSignalChainNoCutsRequireTracked->GetEntries()),signalRecoTrackedEff,signalRecoTrackedEffUnc);

	///calculate the fraction of evts which already passed the GEN cuts and have at least one RecoEcalCandidate within trackless eta region 
	calcEffAndUnc((Float_t) (matchedTrackedSignalChainNoCuts->GetEntriesFast()), (Float_t) (matchedTrackedSignalChainNoCutsRequireTrackless->GetEntries()),signalRecoTracklessEff,signalRecoTracklessEffUnc);

	///calculate the fraction of evts which already passed GEN cuts and have at least one RecoEcalCandidate in the tracked and trackless
	///eta region, and the dilepton mass of at least one tracked+trackless RecoEcalCandidate pair is btwn 50 and 130 GeV
	calcEffAndUnc((Float_t) (matchedTrackedSignalChainNoCutsHasTracklessAndTracked->GetEntries()), (Float_t) (matchedTrackedSignalChain->GetEntries()),signalRecoMassCutEff,signalRecoMassCutEffUnc);

	///calculate the fraction of evts which already passed GEN cuts and now pass all three RecoEcalCandidate cuts (two eta requirements,
	///one dilepton mass requirement)
	calcEffAndUnc((Float_t) (matchedTrackedSignalChainNoCuts->GetEntriesFast()), (Float_t) (matchedTrackedSignalChain->GetEntries()),signalRecoEff,signalRecoEffUnc);

	///calculate the fraction of evts which already passed all GEN and RecoEcalCandidate cuts, and now fire the L1 trigger
	calcEffAndUnc((Float_t) (matchedTrackedSignalChain->GetEntriesFast()), (Float_t) (matchedTrackedSignalChainWithL1Filter->GetEntries()),signalL1Eff,signalL1EffUnc);
	

	///calculate the fraction of evts which already passed all GEN and RecoEcalCandidate cuts, and fired the L1 trigger, and
	///now satisfy the gen matching requirements
	calcMatchingEffAndUnc(matchedTrackedSignalChainWithL1Filter, signalTrackedMatchingEff, signalTrackedMatchingEffUnc);
	calcMatchingEffAndUnc(matchedTracklessSignalChainWithL1Filter, signalTracklessMatchingEff, signalTracklessMatchingEffUnc);


	/*
	Float_t LowPtBkgndL1Eff=0, HighPtBkgndL1Eff=0, VeryHighPtBkgndL1Eff=0;
	Float_t LowPtBkgndL1EffUnc=10, HighPtBkgndL1EffUnc=10, VeryHighPtBkgndL1EffUnc=10;
	Float_t LowPtBkgndRecoEff=0, HighPtBkgndRecoEff=0, VeryHighPtBkgndRecoEff=0;
	Float_t LowPtBkgndRecoEffUnc=10, HighPtBkgndRecoEffUnc=10, VeryHighPtBkgndRecoEffUnc=10;


	calcEffAndUnc((Float_t) (trackedLowPtBkgndChainNoCuts->GetEntries()),(Float_t) (trackedLowPtBkgndChainNoCutsWithL1Filter->GetEntries()),LowPtBkgndL1Eff,LowPtBkgndL1EffUnc);
	calcEffAndUnc((Float_t) (trackedHighPtBkgndChainNoCuts->GetEntries()),(Float_t) (trackedHighPtBkgndChainNoCutsWithL1Filter->GetEntries()),HighPtBkgndL1Eff,HighPtBkgndL1EffUnc);
	calcEffAndUnc((Float_t) (trackedVeryHighPtBkgndChainNoCuts->GetEntries()),(Float_t) (trackedVeryHighPtBkgndChainNoCutsWithL1Filter->GetEntries()),VeryHighPtBkgndL1Eff,VeryHighPtBkgndL1EffUnc);

	calcEffAndUnc((Float_t) (trackedLowPtBkgndChainNoCutsWithL1Filter->GetEntriesFast()),(Float_t) (trackedLowPtBkgndChainWithL1Filter->GetEntries()),LowPtBkgndRecoEff,LowPtBkgndRecoEffUnc);
	calcEffAndUnc((Float_t) (trackedHighPtBkgndChainNoCutsWithL1Filter->GetEntriesFast()),(Float_t) (trackedHighPtBkgndChainWithL1Filter->GetEntries()),HighPtBkgndRecoEff,HighPtBkgndRecoEffUnc);
	calcEffAndUnc((Float_t) (trackedVeryHighPtBkgndChainNoCutsWithL1Filter->GetEntriesFast()),(Float_t) (trackedVeryHighPtBkgndChainWithL1Filter->GetEntries()),VeryHighPtBkgndRecoEff,VeryHighPtBkgndRecoEffUnc);


	cout<<"LowPt bkgnd L1 efficiency = \t"<< LowPtBkgndL1Eff <<"\t uncertainty = \t" << LowPtBkgndL1EffUnc <<endl;
	cout<<"LowPt bkgnd Reco efficiency conditional on L1 = \t"<< LowPtBkgndRecoEff <<"\t uncertainty = \t"<< LowPtBkgndRecoEffUnc <<endl;
	
	cout<<"HighPt bkgnd L1 efficiency = \t"<< HighPtBkgndL1Eff <<"\t uncertainty = \t" << HighPtBkgndL1EffUnc <<endl;
	cout<<"HighPt bkgnd Reco efficiency conditional on L1 = \t"<< HighPtBkgndRecoEff <<"\t uncertainty = \t"<< HighPtBkgndRecoEffUnc <<endl;
	
	cout<<"VeryHighPt bkgnd L1 efficiency = \t"<< VeryHighPtBkgndL1Eff <<"\t uncertainty = \t" << VeryHighPtBkgndL1EffUnc <<endl;
	cout<<"VeryHighPt bkgnd Reco efficiency conditional on L1 = \t"<< VeryHighPtBkgndRecoEff <<"\t uncertainty = \t"<< VeryHighPtBkgndRecoEffUnc <<endl;
	*/

	cout<<"signal Gen efficiency = \t"<< signalGenEff << "\t uncertainty = \t"<< signalGenEffUnc << endl;
	cout<<"signal RecoTracked efficiency conditional on gen = \t"<< signalRecoTrackedEff << "\t uncertainty = \t"<< signalRecoTrackedEffUnc << endl;
	cout<<"signal RecoTrackless efficiency conditional on gen = \t"<< signalRecoTracklessEff << "\t uncertainty = \t"<< signalRecoTracklessEffUnc << endl;
	cout<<"signal RecoMassCut efficiency conditional on tracked and trackless = \t"<< signalRecoMassCutEff << "\t uncertainty = \t"<< signalRecoMassCutEffUnc << endl;
	cout<<"signal Reco efficiency conditional on gen = \t"<< signalRecoEff << "\t uncertainty = \t"<< signalRecoEffUnc << endl;
	cout<<"signal L1 efficiency conditional on reco = \t"<< signalL1Eff << "\t uncertainty = \t"<< signalL1EffUnc << endl;
	cout<<"signal matching eff for Tracked objs conditional on L1 = \t"<< signalTrackedMatchingEff << "\t uncertainty = \t" << signalTrackedMatchingEffUnc << endl;
	cout<<"signal matching eff for Trackless objs conditional on L1 = \t"<< signalTracklessMatchingEff << "\t uncertainty = \t" << signalTracklessMatchingEffUnc << endl;

	//void makeAndSaveSingleTreeHisto(TChain * chain,TString plotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy)
	//makeAndSaveSingleTreeHisto(matchedTrackedSignalChainWithL1Filter,"deltaRAllHltEle>>matchedTrackedDeltaR(100,0.,0.2)","matchedTrackedDeltaR","#DeltaR between tracked reco and GEN electrons","#DeltaR","c1","","tracked_reco_electron_dR_for_evts_passing_all_GEN_L1_and_reco_cuts.png",false);
	//makeAndSaveSingleTreeHisto(matchedTracklessSignalChainWithL1Filter,"deltaRAllHltEle>>matchedTracklessDeltaR(100,0.,6.4)","matchedTracklessDeltaR","#DeltaR between trackless reco and GEN electrons","#DeltaR","c2","","trackless_reco_electron_dR_for_evts_passing_all_GEN_L1_and_reco_cuts.png",false);
	
	

}///end calculateEfficiencies()

