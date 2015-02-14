#include <TFile.h>
#include <TTree.h>
#include <TROOT.h>
#include <TCanvas.h>
#include <TString.h>
#include <TCut.h>
#include <TH1F.h>
#include <TMath.h>
#include <iostream>
#include <fstream>
//this include gives ROOT a temper tantrum 
//#include <array>
#include <vector>

//use this to make and save a histogram from a single TTree branch
//plotArgs is used in TTree::Draw, and could be something like "etaGenEle[0]>>leadingEta(100,-3.0,3.0)"
//histName is the name of the histogram object, and is contained in plotArgs
//histTitle and xAxisTitle will be used with pHist
//I should be able to determine the bin width and plot it on the y axis within this function, after pHist is initialized
void makeAndSaveSingleTreeHisto(TTree * tree,TString plotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	tree->Draw(plotArgs,filters);
	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
	pHist->SetTitle(histTitle);
	pHist->GetXaxis()->SetTitle(xAxisTitle);
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	else sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");

}//end makeAndSaveSingleTreeHisto()

void makeAndSaveOverlayTreeHisto(TTree * tree,std::vector<TString> plotArgsVect,TString histName,TString histTitle,TString xAxisTitle,TString canvName,std::vector<TCut> filtersVect,TString outputFile,Bool_t isPlottingEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	tree->Draw(plotArgsVect[0],filtersVect[0]);
	for(unsigned int i=1;i<plotArgsVect.size();i++){
		tree->Draw(plotArgsVect[i],filtersVect[i]);
	}

	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
	pHist->SetTitle(histTitle);
	pHist->GetXaxis()->SetTitle(xAxisTitle);
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	else sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");
	
}//end makeAndSaveOverlayTreeHisto()

void recoPlotMacro(){

	TFile * f1 = new TFile("/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/experiment.root");

	TTree * hltObjectsTree = (TTree*) f1->Get("recoAnalyzerZero/recoTreeBeforeTriggerFilters");

	//TCut objects 
	TCut trackedEta = "TMath::Abs(etaTrackedHltEle)<2.5";
	TCut trackedPt = "ptTrackedHltEle>27";

	TCut tracklessEtaLow = "TMath::Abs(etaTracklessHltEle)>2.5";
	TCut tracklessEtaHigh = "TMath::Abs(etaTracklessHltEle)<3.0";
	TCut tracklessPt = "ptTracklessHltEle>15";


	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the tracked leg
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTrackedHltEle>>trackedpt(100,0.,140.)","trackedpt","P_{T} of tracked leg hlt objects before all filters","pt (GeV)","c1","","tracked_hlt_object_pt.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTrackedHltEle>>trackedeta(100,-4.0,4.0)","trackedeta","#eta of tracked leg hlt objects before all filters","#eta","c2","","tracked_hlt_object_eta.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTrackedHltEle>>trackedphi(100,-4.0,4.0)","trackedphi","#phi of tracked leg hlt objects before all filters","#phi","c3","","tracked_hlt_object_phi.png",false);
	

	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the tracked leg with |eta|<2.5
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTrackedHltEle>>trackedptWithinTracker(100,0.,140.)","trackedptWithinTracker","P_{T} of tracked leg hlt objects before all filters within tracker acceptance","pt (GeV)","c4",trackedEta,"tracked_hlt_object_pt_within_tracker.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTrackedHltEle>>trackedetaWithinTracker(100,-3.0,3.0)","trackedetaWithinTracker","#eta of tracked leg hlt objects before all filters within tracker acceptance","#eta","c5",trackedEta,"tracked_hlt_object_eta_within_tracker.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTrackedHltEle>>trackedphiWithinTracker(100,-4.0,4.0)","trackedphiWithinTracker","#phi of tracked leg hlt objects before all filters within tracker acceptance","#phi","c6",trackedEta,"tracked_hlt_object_phi_within_tracker.png",false);
	

	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the tracked leg with |eta|<2.5 and pt>27
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTrackedHltEle>>trackedptWithinTrackerMinPt(100,0.,140.)","trackedptWithinTrackerMinPt","P_{T} of tracked leg hlt objects before all filters within tracker acceptance Pt>27","pt (GeV)","c7",trackedEta+trackedPt,"tracked_hlt_object_pt_within_tracker_min_pt_27.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTrackedHltEle>>trackedetaWithinTrackerMinPt(100,-3.0,3.0)","trackedetaWithinTrackerMinPt","#eta of tracked leg hlt objects before all filters within tracker acceptance Pt>27","#eta","c8",trackedEta+trackedPt,"tracked_hlt_object_eta_within_tracker_min_pt_27.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTrackedHltEle>>trackedphiWithinTrackerMinPt(100,-4.0,4.0)","trackedphiWithinTrackerMinPt","#phi of tracked leg hlt objects before all filters within tracker acceptance Pt>27","#phi","c9",trackedEta+trackedPt,"tracked_hlt_object_phi_within_tracker_min_pt_27.png",false);
	


	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the trackless leg
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTracklessHltEle>>tracklesspt(100,0.,140.)","tracklesspt","P_{T} of trackless leg hlt objects before all filters","pt (GeV)","c10","","trackless_hlt_object_pt.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTracklessHltEle>>tracklesseta(100,-4.0,4.0)","tracklesseta","#eta of trackless leg hlt objects before all filters","#eta","c11","","trackless_hlt_object_eta.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTracklessHltEle>>tracklessphi(100,-4.0,4.0)","tracklessphi","#phi of trackless leg hlt objects before all filters","#phi","c12","","trackless_hlt_object_phi.png",false);
	

	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the trackless leg with 2.5<|eta|<3.0
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTracklessHltEle>>tracklessptOutsideTracker(100,0.,140.)","tracklessptOutsideTracker","P_{T} of trackless leg hlt objects before all filters outside tracker acceptance","pt (GeV)","c13",tracklessEtaLow+tracklessEtaHigh,"trackless_hlt_object_pt_outside_tracker.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTracklessHltEle>>tracklessetaOutsideTracker(100,-3.0,3.0)","tracklessetaOutsideTracker","#eta of trackless leg hlt objects before all filters outside tracker acceptance","#eta","c14",tracklessEtaLow+tracklessEtaHigh,"trackless_hlt_object_eta_outside_tracker.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTracklessHltEle>>tracklessphiOutsideTracker(100,-4.0,4.0)","tracklessphiOutsideTracker","#phi of trackless leg hlt objects before all filters outside tracker acceptance","#phi","c15",tracklessEtaLow+tracklessEtaHigh,"trackless_hlt_object_phi_outside_tracker.png",false);
	

	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the trackless leg with 2.5<|eta|<3.0 and pt>15
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTracklessHltEle>>tracklessptOutsideTrackerMinPt(100,0.,140.)","tracklessptOutsideTrackerMinPt","P_{T} of trackless leg hlt objects before all filters outside tracker acceptance Pt>15","pt (GeV)","c16",tracklessEtaLow+tracklessEtaHigh+tracklessPt,"trackless_hlt_object_pt_outside_tracker_min_pt_15.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTracklessHltEle>>tracklessetaOutsideTrackerMinPt(100,-3.0,3.0)","tracklessetaOutsideTrackerMinPt","#eta of trackless leg hlt objects before all filters outside tracker acceptance Pt>15","#eta","c17",tracklessEtaLow+tracklessEtaHigh+tracklessPt,"trackless_hlt_object_eta_outside_tracker_min_pt_15.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTracklessHltEle>>tracklessphiOutsideTrackerMinPt(100,-4.0,4.0)","tracklessphiOutsideTrackerMinPt","#phi of trackless leg hlt objects before all filters outside tracker acceptance Pt>15","#phi","c18",tracklessEtaLow+tracklessEtaHigh+tracklessPt,"trackless_hlt_object_phi_outside_tracker_min_pt_15.png",false);


	//plot pt,eta,phi of all RecoEcalCandidate objects made at the start of the tracked leg which have |eta|<2.5, pt>27, and appear
	//in evts where there is a trackless RecoEcalCandidate object with pt>15
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTrackedHltEle>>trackedptWithinTrackerMinPtWithTrackless(100,0.,140.)","trackedptWithinTrackerMinPtWithTrackless","P_{T} of tracked leg hlt objects before all filters within tracker acceptance Pt>27 and evt has trackless hlt obj","pt (GeV)","c19",trackedEta+trackedPt+tracklessEtaLow+tracklessEtaHigh+tracklessPt,"tracked_hlt_object_pt_within_tracker_min_pt_27_and_evt_has_trackless_hlt_obj.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTrackedHltEle>>trackedetaWithinTrackerMinPtWithTrackless(100,-3.0,3.0)","trackedetaWithinTrackerMinPtWithTrackless","#eta of tracked leg hlt objects before all filters within tracker acceptance Pt>27 and evt has trackless hlt obj","#eta","c20",trackedEta+trackedPt+tracklessEtaLow+tracklessEtaHigh+tracklessPt,"tracked_hlt_object_eta_within_tracker_min_pt_27_and_evt_has_trackless_hlt_obj.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTrackedHltEle>>trackedphiWithinTrackerMinPtWithTrackless(100,-4.0,4.0)","trackedphiWithinTrackerMinPtWithTrackless","#phi of tracked leg hlt objects before all filters within tracker acceptance Pt>27 and evt has trackless hlt obj","#phi","c21",trackedEta+trackedPt+tracklessEtaLow+tracklessEtaHigh+tracklessPt,"tracked_hlt_object_phi_within_tracker_min_pt_27_and_evt_has_trackless_hlt_obj.png",false);
	



	/*
	//plot leading pt, eta, phi
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptGenEle[0]>>leadingpt(100,0.,140.0)","leadingpt","leading GEN electron P_{T}","pT (GeV)","c1","","leading_gen_electron_pt.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaGenEle[0]>>leadingeta(100,-4.0,4.0)","leadingeta","leading GEN electron #eta","#eta","c2","","leading_gen_electron_eta.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiGenEle[0]>>leadingphi(100,-4.0,4.0)","leadingphi","leading GEN electron #phi","#phi (rad)","c3","","leading_gen_electron_phi.png",false);

	//plot subleading pt, eta, phi
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptGenEle[1]>>subleadingpt(100,0.,140.0)","subleadingpt","subleading GEN electron P_{T}","pT (GeV)","c4","","subleading_gen_electron_pt.png",true);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaGenEle[1]>>subleadingeta(100,-4.0,4.0)","subleadingeta","subleading GEN electron #eta","#eta","c5","","subleading_gen_electron_eta.png",false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiGenEle[1]>>subleadingphi(100,-4.0,4.0)","subleadingphi","subleading GEN electron #phi","#phi (rad)","c6","","subleading_gen_electron_phi.png",false);


	//plot eta,pt, phi of all tracked GEN electrons with no other requirements

	std::vector<TString> plotArgsVector;
	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetas(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetas");
	std::vector<TCut> cutsVector;
	cutsVector.push_back(trackedEta0);
	cutsVector.push_back(trackedEta1);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronetas","tracked GEN electron #eta","#eta","c7",cutsVector,"tracked_gen_electron_etas.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronpts(100,0.,140.0)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronpts");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronpts","tracked GEN electron pt","pT (GeV)","c8",cutsVector,"tracked_gen_electron_pts.png",false);

	plotArgsVector.clear();

	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphis(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphis");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronphis","tracked GEN electron #phi","#phi (rad)","c9",cutsVector,"tracked_gen_electron_phis.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	//plot eta,pt,phi of all tracked GEN electrons with one requirement: tracked pt>27

	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasminpt(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasminpt");
	cutsVector.push_back(trackedEta0+trackedPt0);
	cutsVector.push_back(trackedEta1+trackedPt1);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronetasminpt","#eta of tracked GEN electrons whose pt>27","#eta","c10",cutsVector,"tracked_gen_electron_etas_with_tracked_pt_above_27.png",false);

	plotArgsVector.clear();


	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsminpt(100,0.,140.0)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsminpt");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronptsminpt","P_{T} of tracked GEN electrons whose pt>27","pT (GeV)","c11",cutsVector,"tracked_gen_electron_pts_with_tracked_pt_above_27.png",true);

	plotArgsVector.clear();


	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisminpt(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisminpt");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronphisminpt","#phi of tracked GEN electrons whose pt>27","#phi (rad)","c12",cutsVector,"tracked_gen_electron_phis_with_tracked_pt_above_27.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	//plot eta,pt,phi of all tracked GEN electrons with two requirements: tracked pt>27, and a trackless electron is in the evt with pt>15

	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasminptAndTracklessElectron(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasminptAndTracklessElectron");
	cutsVector.push_back(trackedEta0+trackedPt0+tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1);
	cutsVector.push_back(trackedEta1+trackedPt1+tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronetasminptAndTracklessElectron","#eta of tracked GEN electrons whose pt>27 in events with trackless GEN ele with pt>15","#eta","c13",cutsVector,"tracked_gen_electron_etas_with_tracked_pt_above_27_and_trackless_ele.png",false);

	plotArgsVector.clear();

	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsminptAndTracklessElectron(100,0.,140.0)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsminptAndTracklessElectron");
	cutsVector.push_back(trackedEta0+trackedPt0+tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1);
	cutsVector.push_back(trackedEta1+trackedPt1+tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronptsminptAndTracklessElectron","P_{T} of tracked GEN electrons whose pt>27 in events with trackless GEN ele with pt>15","#pt","c14",cutsVector,"tracked_gen_electron_pts_with_tracked_pt_above_27_and_trackless_ele.png",false);

	plotArgsVector.clear();


	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisminptAndTracklessElectron(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisminptAndTracklessElectron");
	cutsVector.push_back(trackedEta0+trackedPt0+tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1);
	cutsVector.push_back(trackedEta1+trackedPt1+tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTrackedElectronphisminptAndTracklessElectron","#phi of tracked GEN electrons whose pt>27 in events with trackless GEN ele with pt>15","#phi (rad)","c15",cutsVector,"tracked_gen_electron_phis_with_tracked_pt_above_27_and_trackless_ele.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	//plot eta,pt,phi of all trackless electrons with no other requirements
	
	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetas(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetas");
	cutsVector.push_back(tracklessEtaLow0+tracklessEtaHigh0);
	cutsVector.push_back(tracklessEtaLow1+tracklessEtaHigh1);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTracklessElectronetas","trackless GEN electron #eta","#eta","c7",cutsVector,"trackless_gen_electron_etas.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronpts(100,0.,140.0)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronpts");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTracklessElectronpts","trackless GEN electron pt","pT (GeV)","c8",cutsVector,"trackless_gen_electron_pts.png",false);

	plotArgsVector.clear();

	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphis(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphis");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTracklessElectronphis","trackless GEN electron #phi","#phi (rad)","c9",cutsVector,"trackless_gen_electron_phis.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	//plot eta,pt,phi of all trackless GEN electrons with one requirement: trackless pt>15 

	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasminpt(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasminpt");
	cutsVector.push_back(tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0);
	cutsVector.push_back(tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1);
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTracklessElectronetasminpt","#eta of trackless GEN electrons whose pt>15","#eta","c10",cutsVector,"trackless_gen_electron_etas_with_trackless_pt_above_15.png",false);

	plotArgsVector.clear();


	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsminpt(100,0.,140.0)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsminpt");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTracklessElectronptsminpt","P_{T} of trackless GEN electrons whose pt>15","pT (GeV)","c11",cutsVector,"trackless_gen_electron_pts_with_trackless_pt_above_15.png",true);

	plotArgsVector.clear();


	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisminpt(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisminpt");
	makeAndSaveOverlayTreeHisto(hltObjectsTree,plotArgsVector,"allTracklessElectronphisminpt","#phi of trackless GEN electrons whose pt>15","#phi (rad)","c12",cutsVector,"trackless_gen_electron_phis_with_trackless_pt_above_15.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	*/

}//end recoPlotMacro()


