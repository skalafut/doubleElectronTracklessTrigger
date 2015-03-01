#include <TFile.h>
#include <TTree.h>
#include <TROOT.h>
#include <TChain.h>
#include <TCanvas.h>
#include <TString.h>
#include <TStyle.h>
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
void makeAndSaveSingleTreeHisto(TChain * chain,TString plotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	chain->Draw(plotArgs,filters);
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
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	else sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");
	
}//end makeAndSaveOverlayTreeHisto()

void genPlotMacro(){

	//TFile * f1 = new TFile("/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/genAnalyzerTree.root");
	//TTree * bothGenLeptonsTree = (TTree*) f1->Get("genAnalyzerOne/genElectronsFromZ");

	TChain * genSignalChain = new TChain("genAnalyzerOne/genElectronsFromZ");
	genSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/signal/*");


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
	makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsBeforeAnyCuts","numGenEvtsBeforeAnyCuts","Evt numbers before any cuts","evt number","c35","","numGenEvts_before_any_cuts.png",false);
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
	//std::vector<TString> plotArgsVector;
	//plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetas(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetas");
	//std::vector<TCut> cutsVector;
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
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronphis","tracked GEN electron #phi","#phi (rad)","c9",cutsVector,"tracked_gen_electron_phis.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();


	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////plot eta,pt,phi of all tracked GEN electrons with one requirement: tracked pt>27

	makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsPassingTracked","numGenEvtsPassingTracked","Evts with at least one GEN electron with |#eta| < 2.5 and pt>27","evt number","c30",trackedPtAndEta0 || trackedPtAndEta1,"numGenEvts_passing_gen_tracked_requirements.png",false);
	//
	//plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasminpt(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasminpt");
	//cutsVector.push_back(trackedEta0+trackedPt0);
	//cutsVector.push_back(trackedEta1+trackedPt1);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasminpt","#eta of tracked GEN electrons whose pt>27","#eta","c10",cutsVector,"tracked_gen_electron_etas_with_tracked_pt_above_27.png",false);

	//
	//plotArgsVector.clear();
	//

	//plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsminpt(100,0.,140.0)");
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
	makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsPassingAll","numGenEvtsPassingAll","Evts passing all GEN requirements","evt number","c32",(trackedPtAndEta0 || trackedPtAndEta1) && (tracklessPtAndEta0 || tracklessPtAndEta1) && totalDileptonMass,"numGenEvts_passing_all_gen_requirements.png",false);
	//

	//plotArgsVector.push_back("etaGenEle[0]>>+allTrackedElectronetasminptAndTracklessElectron(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTrackedElectronetasminptAndTracklessElectron");
	//cutsVector.push_back(trackedEta0+trackedPt0+tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1+totalDileptonMass);
	//cutsVector.push_back(trackedEta1+trackedPt1+tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0+totalDileptonMass);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTrackedElectronetasminptAndTracklessElectron","#eta of tracked GEN electrons in evts passing all GEN Z->ee reqs","#eta","c13",cutsVector,"etas_of_tracked_gen_electron_in_evts_passing_all_GEN_reqs.png",false);

	//plotArgsVector.clear();

	//plotArgsVector.push_back("ptGenEle[0]>>+allTrackedElectronptsminptAndTracklessElectron(100,0.,140.0)");
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
	//plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronpts(100,0.,140.0)");
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
	makeAndSaveSingleTreeHisto(genSignalChain,"evtNumber>>numGenEvtsPassingTrackless","numGenEvtsPassingTrackless","Evts with at least one GEN electron with 2.5 < | #eta | < 3.0 and pt>15","evt number","c33",tracklessPtAndEta0 || tracklessPtAndEta1,"numGenEvts_passing_trackless_gen_requirements.png",false);
	//

	//plotArgsVector.push_back("etaGenEle[0]>>+allTracklessElectronetasminpt(100,-3.0,3.0)");
	//plotArgsVector.push_back("etaGenEle[1]>>+allTracklessElectronetasminpt");
	//cutsVector.push_back(tracklessEtaLow0+tracklessEtaHigh0+tracklessPt0);
	//cutsVector.push_back(tracklessEtaLow1+tracklessEtaHigh1+tracklessPt1);
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronetasminpt","#eta of trackless GEN electrons whose pt>15","#eta","c20",cutsVector,"trackless_gen_electron_etas_with_trackless_pt_above_15.png",false);

	//plotArgsVector.clear();


	//plotArgsVector.push_back("ptGenEle[0]>>+allTracklessElectronptsminpt(100,0.,140.0)");
	//plotArgsVector.push_back("ptGenEle[1]>>+allTracklessElectronptsminpt");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronptsminpt","P_{T} of trackless GEN electrons whose pt>15","pT (GeV)","c21",cutsVector,"trackless_gen_electron_pts_with_trackless_pt_above_15.png",true);

	//plotArgsVector.clear();


	//plotArgsVector.push_back("phiGenEle[0]>>+allTracklessElectronphisminpt(100,-4.0,4.0)");
	//plotArgsVector.push_back("phiGenEle[1]>>+allTracklessElectronphisminpt");
	//makeAndSaveOverlayTreeHisto(genSignalChain,plotArgsVector,"allTracklessElectronphisminpt","#phi of trackless GEN electrons whose pt>15","#phi (rad)","c22",cutsVector,"trackless_gen_electron_phis_with_trackless_pt_above_15.png",false);

	//plotArgsVector.clear();
	//cutsVector.clear();

}


