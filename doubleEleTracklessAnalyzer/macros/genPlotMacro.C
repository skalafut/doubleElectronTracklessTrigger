#include <TFile.h>
#include <TTree.h>
#include <TROOT.h>
#include <TChain.h>
#include <TCanvas.h>
#include <TString.h>
#include <TStyle.h>
#include <TCut.h>
#include <TH1F.h>
#include <TLegend.h>
#include <TMath.h>
#include <TPad.h>
#include <TPaveStats.h>
#include <iostream>
#include <fstream>
//this include gives ROOT a temper tantrum 
//#include <array>
#include <vector>

///overlay two histos which were made from one TChain
///the histo with name histNameOne has looser cuts, and will be drawn first
///the histo named histNameTwo has tighter cuts, and will be drawn second
void overlayTwoHistos(TChain * chain,std::vector<TString> plotArgsVect,TString histNameOne,TString legEntryOne,TString histNameTwo,TString legEntryTwo,TString histTitle,TString xAxisTitle,TString canvName,std::vector<TCut> filtersVect,TString outputFile,Bool_t isPlottingEnergy){
	gStyle->SetOptStat("");
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	chain->Draw(plotArgsVect[0],filtersVect[0]);
	for(unsigned int i=1;i<plotArgsVect.size();i++){
		chain->Draw(plotArgsVect[i],filtersVect[i]);
	}

	TH1F * pHistOne = (TH1F*) gROOT->FindObject(histNameOne);
	TH1F * pHistTwo = (TH1F*) gROOT->FindObject(histNameTwo);
	pHistOne->SetTitle(histTitle);
	pHistOne->GetXaxis()->SetTitle(xAxisTitle);
	pHistOne->SetLineColor(1);
	pHistTwo->SetLineColor(2);
	pHistOne->SetFillColor(21);	///< sets color of area under drawn curve or hist line to grey
	pHistTwo->SetFillColor(30);
	
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHistOne->GetXaxis()->GetBinWidth(1));
	else sprintf(temp,"Events / %.2f ", pHistOne->GetXaxis()->GetBinWidth(1));
	pHistOne->GetYaxis()->SetTitle(temp);
	
	///add a legend to distinguish the two histos
	TLegend * leg = new TLegend(0.75,0.68,1,0.93);
	leg->AddEntry(pHistOne,legEntryOne);
	leg->AddEntry(pHistTwo,legEntryTwo);
	
	///pHistOne has looser cuts than pHistTwo.  Draw pHistOne first, then draw pHistTwo.
	pHistOne->Draw();
	pHistTwo->Draw("same");
	leg->Draw();
	canv->SaveAs(outputFile,"recreate");

}///end overlayTwoHistos()

//use this to make and save a histogram from a single TTree branch
//plotArgs is used in TTree::Draw, and could be something like "etaGenEle[0]>>leadingEta(100,-3.0,3.0)"
//histName is the name of the histogram object, and is contained in plotArgs
//histTitle and xAxisTitle will be used with pHist
//I should be able to determine the bin width and plot it on the y axis within this function, after pHist is initialized
void makeAndSaveSingleTreeHisto(TChain * chain,TString plotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	chain->Draw(plotArgs,filters);
	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
	pHist->SetTitle(histTitle);
	pHist->GetXaxis()->SetTitle(xAxisTitle);
	pHist->SetFillColor(21);
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	else sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");

}//end makeAndSaveSingleTreeHisto()

void makeAndSaveOverlayTreeHisto(TChain * chain,std::vector<TString> plotArgsVect,TString histName,TString histTitle,TString xAxisTitle,TString canvName,std::vector<TCut> filtersVect,TString outputFile,Bool_t isPlottingEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	chain->Draw(plotArgsVect[0],filtersVect[0]);
	for(unsigned int i=1;i<plotArgsVect.size();i++){
		chain->Draw(plotArgsVect[i],filtersVect[i]);
	}

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
	if(outputFile.Contains("trackless_gen_electron_etas")){
		///if the eta distributions of trackless electrons are being drawn, then move the stats box
		///to the center of the plot (near eta = 0)
		gPad->Update();
		TPaveStats *box = (TPaveStats*) pHist->FindObject("stats");
		box->SetX1NDC(0.4);
		box->SetX2NDC(0.65);
	}
	gPad->Update();
	canv->Update();
	canv->SaveAs(outputFile,"recreate");
	
}//end makeAndSaveOverlayTreeHisto()

void genPlotMacro(){

	TChain * genSignalChain = new TChain("genAnalyzerOne/genElectronsFromZ");
	genSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	//TCut objects 
	TCut trackedEta0 = "TMath::Abs(etaGenEle[0])<2.5";
	TCut trackedPt0 = "ptGenEle[0]>27";
	TCut trackedPtAndEta0 = trackedEta0 + trackedPt0;
	TCut trackedEta1 = "TMath::Abs(etaGenEle[1])<2.5";
	TCut trackedPt1 = "ptGenEle[1]>27";
	TCut trackedPtAndEta1 = trackedEta1 + trackedPt1;

	TCut tracklessEtaLow0 = "TMath::Abs(etaGenEle[0])>2.5";
	TCut tracklessEtaHigh0 = "TMath::Abs(etaGenEle[0])<3.0";
	TCut tracklessEtaLow1 = "TMath::Abs(etaGenEle[1])>2.5";
	TCut tracklessEtaHigh1 = "TMath::Abs(etaGenEle[1])<3.0";
	TCut tracklessPt0 = "ptGenEle[0]>15";
	TCut tracklessPt1 = "ptGenEle[1]>15";

	TCut tracklessPtAndEta0 = tracklessEtaLow0 + tracklessEtaHigh0 + tracklessPt0;
	TCut tracklessPtAndEta1 = tracklessEtaLow1 + tracklessEtaHigh1 + tracklessPt1;

	TCut dileptonMassLow = "invMassGen>60.";
	TCut dileptonMassHigh = "invMassGen<120.";
	TCut totalDileptonMass = dileptonMassLow + dileptonMassHigh;

	gStyle->SetOptStat(1111111);

	////plot leading pt, eta, phi
	//makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsBeforeAnyCuts","numGenEvtsBeforeAnyCuts","Evt numbers before any cuts","evt number","c35","","numGenEvts_before_any_cuts.png",false);
	//makeAndSaveSingleTreeHisto(genSignalChain,"ptGenEle[0]>>leadingpt(100,0.,140.0)","leadingpt","leading GEN electron P_{T}","pT (GeV)","c1","","leading_gen_electron_pt.png",true);
	//makeAndSaveSingleTreeHisto(genSignalChain,"etaGenEle[0]>>leadingeta(100,-4.0,4.0)","leadingeta","leading GEN electron #eta","#eta","c2","","leading_gen_electron_eta.png",false);
	//makeAndSaveSingleTreeHisto(genSignalChain,"phiGenEle[0]>>leadingphi(100,-4.0,4.0)","leadingphi","leading GEN electron #phi","#phi (rad)","c3","","leading_gen_electron_phi.png",false);

	////plot subleading pt, eta, phi
	//makeAndSaveSingleTreeHisto(genSignalChain,"ptGenEle[1]>>subleadingpt(100,0.,140.0)","subleadingpt","subleading GEN electron P_{T}","pT (GeV)","c4","","subleading_gen_electron_pt.png",true);
	//makeAndSaveSingleTreeHisto(genSignalChain,"etaGenEle[1]>>subleadingeta(100,-4.0,4.0)","subleadingeta","subleading GEN electron #eta","#eta","c5","","subleading_gen_electron_eta.png",false);
	//makeAndSaveSingleTreeHisto(genSignalChain,"phiGenEle[1]>>subleadingphi(100,-4.0,4.0)","subleadingphi","subleading GEN electron #phi","#phi (rad)","c6","","subleading_gen_electron_phi.png",false);



	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt, phi of all tracked GEN electrons with no other requirements
	std::vector<TString> plotArgsVector;
	//plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetas(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetas");
	std::vector<TCut> cutsVector;
	//cutsVector.push_back(trackedEta0);
	//cutsVector.push_back(trackedEta1);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetas","tracked GEN electron #eta","#eta","c7",cutsVector,"tracked_gen_electron_etas.png",false);

	//plotArgsVector.clear();
	//
	//plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronpts(100,0.,140.0)");
	//plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronpts");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronpts","tracked GEN electron pt","pT (GeV)","c8",cutsVector,"tracked_gen_electron_pts.png",false);

	//plotArgsVector.clear();

	//plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphis(100,-4.0,4.0)");
	//plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphis");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphis","tracked GEN electron #phi","#phi","c9",cutsVector,"tracked_gen_electron_phis.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();


	/*
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta of all electrons
	plotArgsVector.push_back("etaGenEle[0]>>+allElectronetas(60,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allElectronetas(60,-3.0,3.0)");
	cutsVector.push_back("");
	cutsVector.push_back("");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allElectronetas","#eta of all GEN electrons","#eta","c0",cutsVector,"all_electron_etas.png",false);
	plotArgsVector.clear();
	cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked and trackless GEN electrons in evts where both exist

	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExist(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExist");
	cutsVector.push_back(trackedEta0+tracklessEtaLow1+tracklessEtaHigh1);
	cutsVector.push_back(trackedEta1+tracklessEtaLow0+tracklessEtaHigh0);
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasBothElectronsExist","tracked GEN electron #eta in evts with one trackless GEN electron","#eta","c100",cutsVector,"tracked_gen_electron_etas_trackless_electron_exists.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsBothElectronsExist(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsBothElectronsExist");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsBothElectronsExist","tracked GEN electron pt in evts with one trackless GEN electron","pt (GeV)","c101",cutsVector,"tracked_gen_electron_pts_trackless_electron_exists.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisBothElectronsExist(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisBothElectronsExist");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisBothElectronsExist","tracked GEN electron #phi in evts with one trackless GEN electron","#phi","c102",cutsVector,"tracked_gen_electron_phis_trackless_electron_exists.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	cutsVector.push_back(trackedEta1+tracklessEtaLow0+tracklessEtaHigh0);
	cutsVector.push_back(trackedEta0+tracklessEtaLow1+tracklessEtaHigh1);
	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasBothElectronsExist(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasBothElectronsExist");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasBothElectronsExist","trackless GEN electron #eta in evts with one tracked GEN electron","#eta","c103",cutsVector,"trackless_gen_electron_etas_tracked_electron_exists.png",false);

	plotArgsVector.clear();

	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExist(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExist");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsBothElectronsExist","trackless GEN electron pt in evts with one tracked GEN electron","pt (GeV)","c104",cutsVector,"trackless_gen_electron_pts_tracked_electron_exists.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisBothElectronsExist(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisBothElectronsExist");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisBothElectronsExist","trackless GEN electron #phi in evts with one tracked GEN electron","#phi","c105",cutsVector,"trackless_gen_electron_phis_tracked_electron_exists.png",false);

	plotArgsVector.clear();
	cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked and trackless GEN electrons in evts where both exist and their dilepton mass
	////is btwn 60 and 120 GeV

	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExistWithDileptonMass(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExistWithDileptonMass");
	cutsVector.push_back(trackedEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	cutsVector.push_back(trackedEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasBothElectronsExistWithDileptonMass","tracked GEN electron #eta in evts with one trackless GEN electron and 60 < dilepton mass < 120 GeV","#eta","c106",cutsVector,"tracked_gen_electron_etas_trackless_electron_exists_good_dilepton_mass.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsBothElectronsExistWithDileptonMass(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsBothElectronsExistWithDileptonMass");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsBothElectronsExistWithDileptonMass","tracked GEN electron pt in evts with one trackless GEN electron and 60 < dilepton mass < 120 GeV","pt (GeV)","c107",cutsVector,"tracked_gen_electron_pts_trackless_electron_exists_good_dilepton_mass.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisBothElectronsExistWithDileptonMass(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisBothElectronsExistWithDileptonMass");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisBothElectronsExistWithDileptonMass","tracked GEN electron #phi in evts with one trackless GEN electron and 60 < dilepton mass < 120 GeV","#phi","c108",cutsVector,"tracked_gen_electron_phis_trackless_electron_exists_good_dilepton_mass.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	cutsVector.push_back(trackedEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	cutsVector.push_back(trackedEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasBothElectronsExistWithDileptonMass(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasBothElectronsExistWithDileptonMass");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasBothElectronsExistWithDileptonMass","trackless GEN electron #eta in evts with one tracked GEN electron and 60 < dilepton mass < 120 GeV","#eta","c109",cutsVector,"trackless_gen_electron_etas_tracked_electron_exists_good_dilepton_mass.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExistWithDileptonMass(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExistWithDileptonMass");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsBothElectronsExistWithDileptonMass","trackless GEN electron pt in evts with one tracked GEN electron and 60 < dilepton mass < 120 GeV","pt (GeV)","c110",cutsVector,"trackless_gen_electron_pts_tracked_electron_exists_good_dilepton_mass.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisBothElectronsExistWithDileptonMass(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisBothElectronsExistWithDileptonMass");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisBothElectronsExistWithDileptonMass","trackless GEN electron #phi in evts with one tracked GEN electron and 60 < dilepton mass < 120 GeV","#phi","c111",cutsVector,"trackless_gen_electron_phis_tracked_electron_exists_good_dilepton_mass.png",false);

	plotArgsVector.clear();
	cutsVector.clear();


	//void overlayTwoHistos(TChain * chain,std::vector<TString> plotArgsVect,TString histNameOne,TString legEntryOne,TString histNameTwo,TString legEntryTwo,TString histTitle,TString xAxisTitle,TString canvName,std::vector<TCut> filtersVect,TString outputFile,Bool_t isPlottingEnergy)
	
	///plot the eta of tracked GEN electrons before and after the tracked pt>27 cut is applied
	///in evts where one tracked and one trackless GEN electron exists, and their dilepton mass is btwn 60 and 120 GeV 
	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExistWithDileptonMass(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExistWithDileptonMass");
	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndTrackedPtCut(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndTrackedPtCut");
	cutsVector.push_back(trackedEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	cutsVector.push_back(trackedEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	overlayTwoHistos(genSignalChain,plotArgsVector,"allTrackedElectronetasBothElectronsExistWithDileptonMass","tracked #eta","allTrackedElectronetasBothElectronsExistWithDileptonMassAndTrackedPtCut","tracked #eta pt>27","Tracked GEN electron #eta","#eta","c300",cutsVector,"tracked_gen_etas_with_and_without_tracked_pt_cut_passes_dilepton_mass.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	*/
	
	///plot the pt of trackless GEN electrons before and after the tracked pt>27 cut is applied
	///in evts where one tracked and one trackless GEN electron exists, and their dilepton mass is btwn 60 and 120 GeV 
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExistWithDileptonMass(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExistWithDileptonMass");
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndTrackedPtCut(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndTrackedPtCut");
	
	cutsVector.push_back(trackedEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	cutsVector.push_back(trackedEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	overlayTwoHistos(genSignalChain,plotArgsVector,"allTracklessElectronptsBothElectronsExistWithDileptonMass","no cut","allTracklessElectronptsBothElectronsExistWithDileptonMassAndTrackedPtCut","tracked pT cut","Trackless GEN electron pT","pT (GeV)","c301",cutsVector,"trackless_gen_pts_with_and_without_tracked_pt_cut_passes_dilepton_mass.png",true);

	plotArgsVector.clear();
	cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked and trackless GEN electrons in evts where both exist, their dilepton mass
	////is btwn 60 and 120 GeV, and the tracked electron has pt>27

	/*
	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndTrackedPt(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndTrackedPt");
	cutsVector.push_back(trackedPtAndEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasBothElectronsExistWithDileptonMassAndTrackedPt","tracked GEN electron #eta with pt>27 in evts with one trackless GEN electron and 60 < dilepton mass < 120 GeV","#eta","c112",cutsVector,"tracked_gen_electron_etas_trackless_electron_exists_good_dilepton_mass_tracked_pt_gr_27.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsBothElectronsExistWithDileptonMassAndTrackedPt(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsBothElectronsExistWithDileptonMassAndTrackedPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsBothElectronsExistWithDileptonMassAndTrackedPt","tracked GEN electron pt with pt>27 in evts with one trackless GEN electron and 60 < dilepton mass < 120 GeV","pt (GeV)","c113",cutsVector,"tracked_gen_electron_pts_trackless_electron_exists_good_dilepton_mass_tracked_pt_gr_27.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisBothElectronsExistWithDileptonMassAndTrackedPt(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisBothElectronsExistWithDileptonMassAndTrackedPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisBothElectronsExistWithDileptonMassAndTrackedPt","tracked GEN electron #phi with pt>27 in evts with one trackless GEN electron and 60 < dilepton mass < 120 GeV","#phi","c114",cutsVector,"tracked_gen_electron_phis_trackless_electron_exists_good_dilepton_mass_tracked_pt_gr_27.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	*/

	/*
	cutsVector.push_back(trackedPtAndEta1+tracklessEtaLow0+tracklessEtaHigh0+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta0+tracklessEtaLow1+tracklessEtaHigh1+totalDileptonMass);
	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasBothElectronsExistWithDileptonMassAndTrackedPt(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasBothElectronsExistWithDileptonMassAndTrackedPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasBothElectronsExistWithDileptonMassAndTrackedPt","trackless GEN electron #eta in evts with one tracked GEN electron with pt>27 and 60 < dilepton mass < 120 GeV","#eta","c115",cutsVector,"trackless_gen_electron_etas_tracked_electron_exists_good_dilepton_mass_tracked_pt_gr_27.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndTrackedPt(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndTrackedPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsBothElectronsExistWithDileptonMassAndTrackedPt","trackless GEN electron pt in evts with one tracked GEN electron with pt>27 and 60 < dilepton mass < 120 GeV","pt (GeV)","c116",cutsVector,"trackless_gen_electron_pts_tracked_electron_exists_good_dilepton_mass_tracked_pt_gr_27.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisBothElectronsExistWithDileptonMassAndTrackedPt(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisBothElectronsExistWithDileptonMassAndTrackedPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisBothElectronsExistWithDileptonMassAndTrackedPt","trackless GEN electron #phi in evts with one tracked GEN electron with pt>27 and 60 < dilepton mass < 120 GeV","#phi","c117",cutsVector,"trackless_gen_electron_phis_tracked_electron_exists_good_dilepton_mass_tracked_pt_gr_27.png",false);

	plotArgsVector.clear();
	cutsVector.clear();



	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked and trackless GEN electrons in evts where both exist, their dilepton mass
	////is btwn 60 and 120 GeV, and the trackless electron has pt>15
	
	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndTracklessPt(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndTracklessPt");
	cutsVector.push_back(trackedEta0+tracklessPtAndEta1+totalDileptonMass);
	cutsVector.push_back(trackedEta1+tracklessPtAndEta0+totalDileptonMass);
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasBothElectronsExistWithDileptonMassAndTracklessPt","tracked GEN electron #eta in evts with one trackless GEN electron with pt>15 and 60 < dilepton mass < 120 GeV","#eta","c118",cutsVector,"tracked_gen_electron_etas_trackless_electron_exists_good_dilepton_mass_trackless_pt_gr_15.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsBothElectronsExistWithDileptonMassAndTracklessPt(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsBothElectronsExistWithDileptonMassAndTracklessPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsBothElectronsExistWithDileptonMassAndTracklessPt","tracked GEN electron pt in evts with one trackless GEN electron with pt>15 and 60 < dilepton mass < 120 GeV","pt (GeV)","c119",cutsVector,"tracked_gen_electron_pts_trackless_electron_exists_good_dilepton_mass_trackless_pt_gr_15.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisBothElectronsExistWithDileptonMassAndTracklessPt(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisBothElectronsExistWithDileptonMassAndTracklessPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisBothElectronsExistWithDileptonMassAndTracklessPt","tracked GEN electron #phi in evts with one trackless GEN electron with pt>15 and 60 < dilepton mass < 120 GeV","#phi","c120",cutsVector,"tracked_gen_electron_phis_trackless_electron_exists_good_dilepton_mass_trackless_pt_gr_15.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	cutsVector.push_back(trackedEta1+tracklessPtAndEta0+totalDileptonMass);
	cutsVector.push_back(trackedEta0+tracklessPtAndEta1+totalDileptonMass);
	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasBothElectronsExistWithDileptonMassAndTracklessPt(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasBothElectronsExistWithDileptonMassAndTracklessPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasBothElectronsExistWithDileptonMassAndTracklessPt","trackless GEN electron #eta with pt>15 in evts with one tracked GEN electron and 60 < dilepton mass < 120 GeV","#eta","c121",cutsVector,"trackless_gen_electron_etas_tracked_electron_exists_good_dilepton_mass_trackless_pt_gr_15.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndTracklessPt(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndTracklessPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsBothElectronsExistWithDileptonMassAndTracklessPt","trackless GEN electron pt with pt>15 in evts with one tracked GEN electron and 60 < dilepton mass < 120 GeV","pt (GeV)","c122",cutsVector,"trackless_gen_electron_pts_tracked_electron_exists_good_dilepton_mass_trackless_pt_gr_15.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisBothElectronsExistWithDileptonMassAndTracklessPt(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisBothElectronsExistWithDileptonMassAndTracklessPt");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisBothElectronsExistWithDileptonMassAndTracklessPt","trackless GEN electron #phi with pt>15 in evts with one tracked GEN electron and 60 < dilepton mass < 120 GeV","#phi","c123",cutsVector,"trackless_gen_electron_phis_tracked_electron_exists_good_dilepton_mass_trackless_pt_gr_15.png",false);

	plotArgsVector.clear();
	cutsVector.clear();



	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked and trackless GEN electrons in evts where both exist, their dilepton mass
	////is btwn 60 and 120 GeV, the tracked electron has pt>27, and the trackless electron has pt>15
	
	plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndPtCuts(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasBothElectronsExistWithDileptonMassAndPtCuts");
	cutsVector.push_back(trackedPtAndEta0+tracklessPtAndEta1+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta1+tracklessPtAndEta0+totalDileptonMass);
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasBothElectronsExistWithDileptonMassAndPtCuts","tracked GEN electron #eta in evts which pass all pt, eta, dilepton mass cuts","#eta","c124",cutsVector,"tracked_gen_electron_etas_with_all_dilepton_pt_eta_cuts.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsBothElectronsExistWithDileptonMassAndPtCuts(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsBothElectronsExistWithDileptonMassAndPtCuts");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsBothElectronsExistWithDileptonMassAndPtCuts","tracked GEN electron pt in evts which pass all pt, eta, dilepton mass cuts","pt (GeV)","c125",cutsVector,"tracked_gen_electron_pts_with_all_dilepton_pt_eta_cuts.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisBothElectronsExistWithDileptonMassAndPtCuts(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisBothElectronsExistWithDileptonMassAndPtCuts");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisBothElectronsExistWithDileptonMassAndPtCuts","tracked GEN electron #phi in evts which pass all pt, eta, dilepton mass cuts","#phi","c126",cutsVector,"tracked_gen_electron_phis_with_all_dilepton_pt_eta_cuts.png",false);

	plotArgsVector.clear();
	cutsVector.clear();

	cutsVector.push_back(trackedPtAndEta1+tracklessPtAndEta0+totalDileptonMass);
	cutsVector.push_back(trackedPtAndEta0+tracklessPtAndEta1+totalDileptonMass);
	plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasBothElectronsExistWithDileptonMassAndPtCuts(100,-3.0,3.0)");
	plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasBothElectronsExistWithDileptonMassAndPtCuts");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasBothElectronsExistWithDileptonMassAndPtCuts","trackless GEN electron #eta in evts which pass all pt, eta, dilepton mass cuts","#eta","c127",cutsVector,"trackless_gen_electron_etas_with_all_dilepton_pt_eta_cuts.png",false);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndPtCuts(100,0.,100.)");
	plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsBothElectronsExistWithDileptonMassAndPtCuts");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsBothElectronsExistWithDileptonMassAndPtCuts","trackless GEN electron pt in evts which pass all pt, eta, dilepton mass cuts","pt (GeV)","c128",cutsVector,"trackless_gen_electron_pts_with_all_dilepton_pt_eta_cuts.png",true);

	plotArgsVector.clear();
	
	plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisBothElectronsExistWithDileptonMassAndPtCuts(100,-4.0,4.0)");
	plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisBothElectronsExistWithDileptonMassAndPtCuts");
	makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisBothElectronsExistWithDileptonMassAndPtCuts","trackless GEN electron #phi in evts which pass all pt, eta, dilepton mass cuts","#phi","c129",cutsVector,"trackless_gen_electron_phis_with_all_dilepton_pt_eta_cuts.png",false);

	plotArgsVector.clear();
	cutsVector.clear();
	
	makeAndSaveSingleTreeHisto(genSignalChain,"invMassGen>>invMassPassingAllCuts","invMassPassingAllCuts","Dilepton mass in evts passing all GEN requirements","M_{ee} (GeV)","c130",(trackedPtAndEta0 || trackedPtAndEta1) && (tracklessPtAndEta0 || tracklessPtAndEta1) && totalDileptonMass,"invMassGen_passing_all_gen_requirements.png",true);

	*/

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked GEN electrons with one requirement: tracked pt>27

	//makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsPassingTracked","numGenEvtsPassingTracked","Evts with at least one GEN electron with |#eta| < 2.5 and pt>27","evt number","c30",trackedPtAndEta0 || trackedPtAndEta1,"numGenEvts_passing_gen_tracked_requirements.png",false);
	//
	//plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasminpt(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasminpt");
	//cutsVector.push_back(trackedEta0+trackedPt0);
	//cutsVector.push_back(trackedEta1+trackedPt1);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasminpt","#eta of tracked GEN electrons whose pt>27","#eta","c10",cutsVector,"tracked_gen_electron_etas_with_tracked_pt_above_27.png",false);

	//
	//plotArgsVector.clear();
	//

	//plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsminpt(100,0.,100.0)");
	//plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsminpt");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsminpt","P_{T} of tracked GEN electrons whose pt>27","pT (GeV)","c11",cutsVector,"tracked_gen_electron_pts_with_tracked_pt_above_27.png",true);

	//plotArgsVector.clear();


	//plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisminpt(100,-4.0,4.0)");
	//plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisminpt");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisminpt","#phi of tracked GEN electrons whose pt>27","#phi (rad)","c12",cutsVector,"tracked_gen_electron_phis_with_tracked_pt_above_27.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked GEN electrons with three requirements: tracked pt>27, dilepton mass between 60 and 120,
	////and a trackless electron is in the evt with pt>15
	//
	//makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsPassingAll","numGenEvtsPassingAll","Evts passing all GEN requirements","evt number","c32",(trackedPtAndEta0 || trackedPtAndEta1) && (tracklessPtAndEta0 || tracklessPtAndEta1) && totalDileptonMass,"numGenEvts_passing_all_gen_requirements.png",false);
	//

	//plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasminptAndTracklessElectron(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasminptAndTracklessElectron");
	//cutsVector.push_back(trackedEta0+trackedPt0+tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1+totalDileptonMass);
	//cutsVector.push_back(trackedEta1+trackedPt1+tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0+totalDileptonMass);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasminptAndTracklessElectron","#eta of tracked GEN electrons in evts passing all GEN Z->ee reqs","#eta","c13",cutsVector,"etas_of_tracked_gen_electron_in_evts_passing_all_GEN_reqs.png",false);

	//plotArgsVector.clear();

	//plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsminptAndTracklessElectron(100,0.,100.0)");
	//plotArgsVector.push_back("ptGenEle[1]>>+allTrackedElectronptsminptAndTracklessElectron");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronptsminptAndTracklessElectron","P_{T} of tracked GEN electrons in events passing all GEN Z->ee reqs","pt (GeV)","c14",cutsVector,"pts_of_tracked_gen_electrons_in_evts_passing_all_GEN_reqs.png",true);

	//plotArgsVector.clear();


	//plotArgsVector.push_back("phiGenEle[0]>>+allTrackedElectronphisminptAndTracklessElectron(100,-4.0,4.0)");
	//plotArgsVector.push_back("phiGenEle[1]>>+allTrackedElectronphisminptAndTracklessElectron");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphisminptAndTracklessElectron","#phi of tracked GEN electrons in events passing all GEN Z->ee reqs","#phi (rad)","c15",cutsVector,"phis_of_tracked_gen_electrons_in_evts_passing_all_GEN_reqs.png",false);

	//plotArgsVector.clear();
	//
	//plotArgsVector.push_back("(etaGenEle[0]-etaGenEle[1])>>+deltaEtaBtwnTrackedAndUntrackedElectrons(100,-3.,3.)");
	//plotArgsVector.push_back("(etaGenEle[1]-etaGenEle[0])>>+deltaEtaBtwnTrackedAndUntrackedElectrons");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"deltaEtaBtwnTrackedAndUntrackedElectrons","#Delta #eta btwn tracked and trackless GEN electrons in evts passing all GEN Z->ee requirements","#Delta #eta","c16",cutsVector,"deltaEta_gen_tracked_to_trackless_in_evts_passing_all_GEN_reqs.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all trackless electrons with no other requirements
	//
	//plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetas(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetas");
	//cutsVector.push_back(tracklessEtaLow0+tracklessEtaHigh0);
	//cutsVector.push_back(tracklessEtaLow1+tracklessEtaHigh1);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetas","trackless GEN electron #eta","#eta","c17",cutsVector,"trackless_gen_electron_etas.png",false);

	//plotArgsVector.clear();
	//
	//plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronpts(100,0.,100.0)");
	//plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronpts");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronpts","trackless GEN electron pt","pT (GeV)","c18",cutsVector,"trackless_gen_electron_pts.png",true);

	//plotArgsVector.clear();

	//plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphis(100,-4.0,4.0)");
	//plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphis");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphis","trackless GEN electron #phi","#phi (rad)","c19",cutsVector,"trackless_gen_electron_phis.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all trackless GEN electrons with one requirement: trackless pt>15 
	//
	//makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsPassingTrackless","numGenEvtsPassingTrackless","Evts with at least one GEN electron with 2.5 < | #eta | < 3.0 and pt>15","evt number","c33",tracklessPtAndEta0 || tracklessPtAndEta1,"numGenEvts_passing_trackless_gen_requirements.png",false);
	//

	//plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasminpt(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasminpt");
	//cutsVector.push_back(tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0);
	//cutsVector.push_back(tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasminpt","#eta of trackless GEN electrons whose pt>15","#eta","c20",cutsVector,"trackless_gen_electron_etas_with_trackless_pt_above_15.png",false);

	//plotArgsVector.clear();


	//plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsminpt(100,0.,100.0)");
	//plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsminpt");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsminpt","P_{T} of trackless GEN electrons whose pt>15","pT (GeV)","c21",cutsVector,"trackless_gen_electron_pts_with_trackless_pt_above_15.png",true);

	//plotArgsVector.clear();


	//plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisminpt(100,-4.0,4.0)");
	//plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisminpt");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisminpt","#phi of trackless GEN electrons whose pt>15","#phi (rad)","c22",cutsVector,"trackless_gen_electron_phis_with_trackless_pt_above_15.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();

}


