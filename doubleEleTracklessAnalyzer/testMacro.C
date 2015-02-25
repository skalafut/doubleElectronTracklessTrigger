#include <TFile.h>
#include <TTree.h>
#include <TROOT.h>
#include <TCanvas.h>
#include <TString.h>
#include <TCut.h>
#include <TH1F.h>
#include <TMath.h>
#include <TStyle.h>
#include <TEventList.h>
#include <TEntryList.h>
#include <TEntryListArray.h>
#include <iostream>
#include <fstream>
//this include gives ROOT a temper tantrum 
//#include <array>
#include <vector>


void makeAndSaveHistoUsingEntryList(TTree * tree,TString listFillArgs,TString listName,TString histPlotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy, Bool_t isPlottingInverseEnergy){
	//fill the TEntryList named listName, and apply the filters when the list is made
	tree->Draw(listFillArgs,filters,"entrylistarray");
	//tell the tree to only use entries in the object named listName when calling TTree::Draw() in the future
	tree->SetEntryList((TEntryListArray*) gROOT->FindObject(listName) );
	
	//run the code in makeAndSaveSingleTreeHisto() to make comprehendible plots with useful labels and title 
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	tree->Draw(histPlotArgs);
	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
	pHist->SetTitle(histTitle);
	pHist->GetXaxis()->SetTitle(xAxisTitle);
	if(histTitle.Contains("Iso") ){
		canv->SetLogy(1);
		pHist->SetMinimum(1);
	}
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingInverseEnergy && pHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f / GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if(isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f / GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.001){
		sprintf(temp,"Events / %.4f / GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f ", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	}
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");

}//end makeAndSaveHistoUsingEntryList()


//use this to make and save a histogram from a single TTree branch
//plotArgs is used in TTree::Draw, and could be something like "etaGenEle[0]>>leadingEta(100,-3.0,3.0)"
//histName is the name of the histogram object, and is contained in plotArgs
//histTitle and xAxisTitle will be used with pHist
//I should be able to determine the bin width and plot it on the y axis within this function, after pHist is initialized
void makeAndSaveSingleTreeHisto(TTree * tree,TString plotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy, Bool_t isPlottingInverseEnergy){
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	tree->Draw(plotArgs,filters);
	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
	pHist->SetTitle(histTitle);
	pHist->GetXaxis()->SetTitle(xAxisTitle);
	if(histTitle.Contains("Iso") ){
		canv->SetLogy(1);
		pHist->SetMinimum(1);
	}
	//every histo should have at least three bins.
	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
	char temp[130];
	if(isPlottingInverseEnergy && pHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f / GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if(isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f / GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.001){
		sprintf(temp,"Events / %.4f / GeV", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f ", pHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && pHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
	}
	pHist->GetYaxis()->SetTitle(temp);
	pHist->Draw();
	canv->SaveAs(outputFile,"recreate");

}//end makeAndSaveSingleTreeHisto()


//void makeAndSaveOverlayTreeHisto(TTree * tree,std::vector<TString> plotArgsVect,TString histName,TString histTitle,TString xAxisTitle,TString canvName,std::vector<TCut> filtersVect,TString outputFile,Bool_t isPlottingEnergy){
//	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
//	canv->cd();
//	tree->Draw(plotArgsVect[0],filtersVect[0]);
//	for(unsigned int i=1;i<plotArgsVect.size();i++){
//		tree->Draw(plotArgsVect[i],filtersVect[i]);
//	}
//
//	TH1F * pHist = (TH1F*) gROOT->FindObject(histName);
//	pHist->SetTitle(histTitle);
//	pHist->GetXaxis()->SetTitle(xAxisTitle);
//	//every histo should have at least three bins.
//	//if a histo is created with numBins = 1, then bin #1 is the bin which is plotted 
//	char temp[130];
//	if(isPlottingEnergy) sprintf(temp,"Events / %.2f GeV", pHist->GetXaxis()->GetBinWidth(1));
//	else sprintf(temp,"Events / %.2f ", pHist->GetXaxis()->GetBinWidth(1));
//	pHist->GetYaxis()->SetTitle(temp);
//	pHist->Draw();
//	canv->SaveAs(outputFile,"recreate");
//	
//}//end makeAndSaveOverlayTreeHisto()

void testMacro(){

	//TFile * f1 = new TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr25/signal_analyzer_trees_3.root");
	//TTree * hltTrackedObjectsTree = (TTree*) f1->Get("recoAnalyzerTracked/recoTreeBeforeTriggerFiltersTrackedSignal");		//tracked
	//TTree * hltTracklessObjectsTree = (TTree*) f1->Get("recoAnalyzerTrackless/recoTreeBeforeTriggerFiltersTracklessSignal");	//trackless
	//TTree * hltTrackedObjectsTree = (TTree*) f1->Get("recoAnalyzerMatchedTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignal");		//matched tracked
	//TTree * hltTracklessObjectsTree = (TTree*) f1->Get("recoAnalyzerMatchedTrackless/recoTreeBeforeTriggerFiltersMatchedTracklessSignal");		//matched trackless

	//TFile * f1 = new TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr25/high_pt_bkgnd_analyzer_trees_234.root");
	TFile * f1 = new TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr25/low_pt_bkgnd_analyzer_trees_10.root");
	TTree * hltTrackedObjectsTree = (TTree*) f1->Get("recoAnalyzerTracked/recoTreeBeforeTriggerFiltersTrackedBkgnd");
	//TTree * hltTracklessObjectsTree = (TTree*) f1->Get("recoAnalyzerTrackless/recoTreeBeforeTriggerFiltersTracklessBkgnd");

	/*
	//TCut objects 
	//TCut tracklessEtaLow = "TMath::Abs(etaTracklessHltEle)>2.5";
	//require that a tracked leg or trackless leg REC object exists
	TCut hasTrackedBarrelHlt = "nTrackedBarrelHltEle>0";
	TCut hasTrackedEndcapHlt = "nTrackedEndcapHltEle>0";
	TCut hasTrackedHlt = (hasTrackedBarrelHlt || hasTrackedEndcapHlt);
	TCut hasTracklessHlt = "nTracklessHltEle>0";
	*/

	//hlt eta cuts
	TCut trackedEBHltEta = "TMath::Abs(etaHltEle)<1.479";
	TCut trackedEEHltLowEta = "TMath::Abs(etaHltEle)>1.479";
	TCut trackedEEHltHighEta = "TMath::Abs(etaHltEle)<2.5";
	TCut trackedEEHltEta = trackedEEHltLowEta + trackedEEHltHighEta;
	TCut tracklessEEHltLowEta = "TMath::Abs(etaHltEle)>2.5";
	TCut tracklessEEHltHighEta = "TMath::Abs(etaHltEle)<3.0";
	TCut tracklessEEHltEta = tracklessEEHltLowEta + tracklessEEHltHighEta;

	//hlt Et cuts
	TCut trackedLegHltEt = "ptHltEle>27";
	TCut tracklessLegHltEt = "ptHltEle>15";

	//combined Et and eta cuts
	TCut trackedEBPtEta = trackedEBHltEta + trackedLegHltEt;
	TCut trackedEEPtEta = trackedEEHltEta + trackedLegHltEt;
	TCut tracklessEEPtEta = tracklessEEHltEta + tracklessLegHltEt;

	gStyle->SetOptStat(1111111);
	


	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects which would normally be run through the tracked leg
	//makeAndSaveHistoUsingEntryList(hltObjectsTree,"evtNumber>>numEvtsBothRecoMatchingThree","numEvtsBothRecoMatchingThree","Evt numbers where tracked and trackless reco objects are matched to GEN","evt nums","c55",hasTracklessHlt+hasTrackedHlt,"num_evts_both_reco_objs_matching_three.png",false, false);
	/*
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedptBarrelZeroList","trackedptBarrelZeroList","ptHltEle>>trackedptZeroBarrel(100,0.,100.)","trackedptZeroBarrel","P_{T} of tracked leg hlt objects in barrel before all filters","pt (GeV)","c1",trackedEBHltEta,"tracked_barrel_hlt_object_pt_ZeroBarrel.png",true, false);
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedetaBarrelZeroList","trackedetaBarrelZeroList","etaHltEle>>trackedetaZeroBarrel(100,-3.0,3.0)","trackedetaZeroBarrel","#eta of tracked leg hlt objects in barrel before all filters","#eta","c2",trackedEBHltEta,"tracked_barrel_hlt_object_eta_ZeroBarrel.png",false, false);

	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedphiBarrelZeroList","trackedphiBarrelZeroList","phiHltEle>>trackedphiZeroBarrel(100,-4.0,4.0)","trackedphiZeroBarrel","#phi of tracked leg hlt objects in barrel before all filters","#phi","c3",trackedEBHltEta,"tracked_barrel_hlt_object_phi_ZeroBarrel.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedclusterShapeBarrelZeroList","trackedclusterShapeBarrelZeroList","clusterShapeHltEle>>trackedclusterShapeZeroBarrel(100,0.,0.05)","trackedclusterShapeZeroBarrel","#sigma i#eta i#eta of tracked leg hlt objects in barrel before all filters","#sigma i#eta i#eta","c4",trackedEBHltEta,"tracked_barrel_hlt_object_clusterShape_ZeroBarrel.png",false, false);

	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedhadEmBarrelZeroList","trackedhadEmBarrelZeroList","hadEmHltEle>>trackedhadEmZeroBarrel(100,0.,0.3)","trackedhadEmZeroBarrel","Had/Em/energy of tracked leg hlt objects in barrel before all filters","Had/Em/Energy (1/GeV)","c5",trackedEBHltEta,"tracked_barrel_hlt_object_hadEm_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedecalIsoBarrelZeroList","trackedecalIsoBarrelZeroList","ecalIsoHltEle>>trackedecalIsoZeroBarrel(100,-0.2,1.8)","trackedecalIsoZeroBarrel","EcalIso/pt of tracked leg hlt objects in barrel before all filters","EcalIso/pt (1/GeV)","c6",trackedEBHltEta,"tracked_barrel_hlt_object_ecalIso_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedhcalIsoBarrelZeroList","trackedhcalIsoBarrelZeroList","hcalIsoHltEle>>trackedhcalIsoZeroBarrel(100,-0.2,1.1)","trackedhcalIsoZeroBarrel","HcalIso/pt of tracked leg hlt objects in barrel before all filters","HcalIso/pt","c7",trackedEBHltEta,"tracked_barrel_hlt_object_hcalIso_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedepBarrelZeroList","trackedepBarrelZeroList","epHltEle>>trackedepZeroBarrel(100,-0.015,0.3)","trackedepZeroBarrel","(1/E) - (1/P) of tracked leg hlt objects in barrel before all filters","(1/E)-(1/P) (1/GeV)","c8",trackedEBHltEta,"tracked_barrel_hlt_object_ep_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackeddEtaBarrelZeroList","trackeddEtaBarrelZeroList","dEtaHltEle>>trackeddEtaZeroBarrel(100,-0.01,0.03)","trackeddEtaZeroBarrel","#Delta #eta of tracked leg hlt objects in barrel before all filters","#Delta #eta","c9",trackedEBHltEta,"tracked_barrel_hlt_object_dEta_ZeroBarrel.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackeddPhiBarrelZeroList","trackeddPhiBarrelZeroList","dPhiHltEle>>trackeddPhiZeroBarrel(100,-0.03,0.2)","trackeddPhiZeroBarrel","#Delta #phi of tracked leg hlt objects in barrel before all filters","#Delta #phi","c10",trackedEBHltEta,"tracked_barrel_hlt_object_dPhi_ZeroBarrel.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedtrackIsoBarrelZeroList","trackedtrackIsoBarrelZeroList","trackIsoHltEle>>trackedtrackIsoZeroBarrel(100,-0.05,0.65)","trackedtrackIsoZeroBarrel","TrackIso/pt of tracked leg hlt objects in barrel before all filters","TrackIso/pt (1/GeV)","c11",trackedEBHltEta,"tracked_barrel_hlt_object_trackIso_ZeroBarrel.png",false, true);

	*/

	/**/
	//tracked objs in endcap before all filters
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedptEndcapZeroList","trackedptEndcapZeroList","ptHltEle>>trackedptZeroEndcap(100,0.,100.)","trackedptZeroEndcap","P_{T} of tracked leg hlt objects in endcap before all filters","pt (GeV)","c31",trackedEEHltEta,"tracked_endcap_hlt_object_pt_ZeroEndcap.png",true, false);
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedetaEndcapZeroList","trackedetaEndcapZeroList","etaHltEle>>trackedetaZeroEndcap(100,-3.0,3.0)","trackedetaZeroEndcap","#eta of tracked leg hlt objects in endcap before all filters","#eta","c32",trackedEEHltEta,"tracked_endcap_hlt_object_eta_ZeroEndcap.png",false, false);

	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedphiEndcapZeroList","trackedphiEndcapZeroList","phiHltEle>>trackedphiZeroEndcap(100,-4.0,4.0)","trackedphiZeroEndcap","#phi of tracked leg hlt objects in endcap before all filters","#phi","c33",trackedEEHltEta,"tracked_endcap_hlt_object_phi_ZeroEndcap.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedclusterShapeEndcapZeroList","trackedclusterShapeEndcapZeroList","clusterShapeHltEle>>trackedclusterShapeZeroEndcap(100,0.,0.06)","trackedclusterShapeZeroEndcap","#sigma i#eta i#eta of tracked leg hlt objects in endcap before all filters","#sigma i#eta i#eta","c34",trackedEEHltEta,"tracked_endcap_hlt_object_clusterShape_ZeroEndcap.png",false, false);

	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedhadEmEndcapZeroList","trackedhadEmEndcapZeroList","hadEmHltEle>>trackedhadEmZeroEndcap(100,0.,0.6)","trackedhadEmZeroEndcap","Had/Em/energy of tracked leg hlt objects in endcap before all filters","Had/Em/Energy (1/GeV)","c35",trackedEEHltEta,"tracked_endcap_hlt_object_hadEm_ZeroEndcap.png",false, true);

	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedecalIsoEndcapZeroList","trackedecalIsoEndcapZeroList","ecalIsoHltEle>>trackedecalIsoZeroEndcap(100,-0.2,1.8)","trackedecalIsoZeroEndcap","EcalIso/pt of tracked leg hlt objects in endcap before all filters","EcalIso/pt (1/GeV)","c36",trackedEEHltEta,"tracked_endcap_hlt_object_ecalIso_ZeroEndcap.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedhcalIsoEndcapZeroList","trackedhcalIsoEndcapZeroList","hcalIsoHltEle>>trackedhcalIsoZeroEndcap(100,-0.2,1.1)","trackedhcalIsoZeroEndcap","HcalIso/pt of tracked leg hlt objects in endcap before all filters","HcalIso/pt","c37",trackedEEHltEta,"tracked_endcap_hlt_object_hcalIso_ZeroEndcap.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedepEndcapZeroList","trackedepEndcapZeroList","epHltEle>>trackedepZeroEndcap(100,-0.015,0.3)","trackedepZeroEndcap","(1/E) - (1/P) of tracked leg hlt objects in endcap before all filters","(1/E)-(1/P) (1/GeV)","c38",trackedEEHltEta,"tracked_endcap_hlt_object_ep_ZeroEndcap.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackeddEtaEndcapZeroList","trackeddEtaEndcapZeroList","dEtaHltEle>>trackeddEtaZeroEndcap(100,-0.01,0.03)","trackeddEtaZeroEndcap","#Delta #eta of tracked leg hlt objects in endcap before all filters","#Delta #eta","c39",trackedEEHltEta,"tracked_endcap_hlt_object_dEta_ZeroEndcap.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackeddPhiEndcapZeroList","trackeddPhiEndcapZeroList","dPhiHltEle>>trackeddPhiZeroEndcap(100,-0.03,0.2)","trackeddPhiZeroEndcap","#Delta #phi of tracked leg hlt objects in endcap before all filters","#Delta #phi","c40",trackedEEHltEta,"tracked_endcap_hlt_object_dPhi_ZeroEndcap.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTrackedObjectsTree,">>trackedtrackIsoEndcapZeroList","trackedtrackIsoEndcapZeroList","trackIsoHltEle>>trackedtrackIsoZeroEndcap(100,-0.05,0.65)","trackedtrackIsoZeroEndcap","TrackIso/pt of tracked leg hlt objects in endcap before all filters","TrackIso/pt (1/GeV)","c41",trackedEEHltEta,"tracked_endcap_hlt_object_trackIso_ZeroEndcap.png",false, true);

	/**/

	/*
	//plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects which would be run through the trackless leg
	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklessptZeroList","tracklessptZeroList","ptHltEle>>tracklessptZero(100,0.,60.)","tracklessptZero","P_{T} of trackless leg hlt objects before all filters","pt (GeV)","c12",tracklessEEHltEta,"trackless_hlt_object_pt_Zero.png",true, false);
	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklessetaZeroList","tracklessetaZeroList","etaHltEle>>tracklessetaZero(100,-3.0,3.0)","tracklessetaZero","#eta of trackless leg hlt objects before all filters","#eta","c13",tracklessEEHltEta,"trackless_hlt_object_eta_Zero.png",false, false);
	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklessphiZeroList","tracklessphiZeroList","phiHltEle>>tracklessphiZero(100,-4.0,4.0)","tracklessphiZero","#phi of trackless leg hlt objects before all filters","#phi","c14",tracklessEEHltEta,"trackless_hlt_object_phi_Zero.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklessclusterShapeZeroList","tracklessclusterShapeZeroList","clusterShapeHltEle>>tracklessclusterShapeZero(100,0.,0.06)","tracklessclusterShapeZero","#sigma i#eta i#eta of trackless leg hlt objects before all filters","#sigma i#eta i#eta","c15",tracklessEEHltEta,"trackless_hlt_object_clusterShape_Zero.png",false, false);
	
	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklessecalIsoZeroList","tracklessecalIsoZeroList","ecalIsoHltEle>>tracklessecalIsoZero(100,-0.9,1.8)","tracklessecalIsoZero","EcalIso/pt of trackless leg hlt objects before all filters","EcalIso/pt (1/GeV)","c16",tracklessEEHltEta,"trackless_hlt_object_ecalIso_Zero.png",false, true);
	
	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklesshadEmZeroList","tracklesshadEmZeroList","hadEmHltEle>>tracklesshadEmZero(100,0.,2)","tracklesshadEmZero","Had/Em/energy of trackless leg hlt objects before all filters","Had/Em/energy","c17",tracklessEEHltEta,"trackless_hlt_object_hadEm_Zero.png",false, true);

	makeAndSaveHistoUsingEntryList(hltTracklessObjectsTree,">>tracklesshcalIsoZeroList","tracklesshcalIsoZeroList","hcalIsoHltEle>>tracklesshcalIsoZero(100,-1.0,5.0)","tracklesshcalIsoZero","HcalIso/pt of trackless leg hlt objects before all filters","HcalIso/pt (1/GeV)","c18",tracklessEEHltEta,"trackless_hlt_object_hcalIso_Zero.png",false, true);

	*/

	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects which would normally be run through the tracked leg 
	////and have pt>27.  No other requirements (on tracked or trackless RECs) are made.
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ptTrackedBarrelHltEle>>trackedptOneBarrel(100,0.,100.)","trackedptOneBarrel","P_{T} of tracked leg hlt objects in barrel with pt>27","pt (GeV)","c1","","tracked_barrel_hlt_object_pt_OneBarrel.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"etaTrackedBarrelHltEle>>trackedetaOneBarrel(100,-3.0,3.0)","trackedetaOneBarrel","#eta of tracked leg hlt objects in barrel with pt>27","#eta","c2","","tracked_barrel_hlt_object_eta_OneBarrel.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"phiTrackedBarrelHltEle>>trackedphiOneBarrel(100,-4.0,4.0)","trackedphiOneBarrel","#phi of tracked leg hlt objects in barrel with pt>27","#phi","c3","","tracked_barrel_hlt_object_phi_OneBarrel.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"clusterShapeTrackedBarrelHltEle>>trackedclusterShapeOneBarrel(100,0.,0.14)","trackedclusterShapeOneBarrel","#sigma i#eta i#eta of tracked leg hlt objects in barrel with pt>27","#sigma i#eta i#eta","c4","","tracked_barrel_hlt_object_clusterShape_OneBarrel.png",false, false);

	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hadEmTrackedBarrelHltEle>>trackedhadEmOneBarrel(100,0.,1.)","trackedhadEmOneBarrel","Had/Em/energy of tracked leg hlt objects in barrel with pt>27","Had/Em/Energy (1/GeV)","c5","","tracked_barrel_hlt_object_hadEm_OneBarrel.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ecalIsoTrackedBarrelHltEle>>trackedecalIsoOneBarrel(100,-0.2,1.7)","trackedecalIsoOneBarrel","EcalIso/pt of tracked leg hlt objects in barrel with pt>27","EcalIso/pt (1/GeV)","c6","","tracked_barrel_hlt_object_ecalIso_OneBarrel.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hcalIsoTrackedBarrelHltEle>>trackedhcalIsoOneBarrel(100,-0.2,1.1)","trackedhcalIsoOneBarrel","HcalIso/pt of tracked leg hlt objects in barrel with pt>27","HcalIso/pt","c7","","tracked_barrel_hlt_object_hcalIso_OneBarrel.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"epTrackedBarrelHltEle>>trackedepOneBarrel(100,-0.015,0.4)","trackedepOneBarrel","(1/E) - (1/P) of tracked leg hlt objects in barrel with pt>27","(1/E)-(1/P) (1/GeV)","c8","","tracked_barrel_hlt_object_ep_OneBarrel.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dEtaTrackedBarrelHltEle>>trackeddEtaOneBarrel(100,-0.01,0.05)","trackeddEtaOneBarrel","#Delta #eta of tracked leg hlt objects in barrel with pt>27","#Delta #eta","c9","","tracked_barrel_hlt_object_dEta_OneBarrel.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dPhiTrackedBarrelHltEle>>trackeddPhiOneBarrel(100,-0.03,0.3)","trackeddPhiOneBarrel","#Delta #phi of tracked leg hlt objects in barrel with pt>27","#Delta #phi","c10","","tracked_barrel_hlt_object_dPhi_OneBarrel.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"trackIsoTrackedBarrelHltEle>>trackedtrackIsoOneBarrel(100,-0.05,1.25)","trackedtrackIsoOneBarrel","TrackIso/pt of tracked leg hlt objects in barrel with pt>27","TrackIso/pt (1/GeV)","c11","","tracked_barrel_hlt_object_trackIso_OneBarrel.png",false, true);


	////tracked objs in endcap with pt>27
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ptTrackedEndcapHltEle>>trackedptOneEndcap(100,0.,100.)","trackedptOneEndcap","P_{T} of tracked leg hlt objects in endcap with pt>27","pt (GeV)","c31","","tracked_endcap_hlt_object_pt_OneEndcap.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"etaTrackedEndcapHltEle>>trackedetaOneEndcap(100,-3.0,3.0)","trackedetaOneEndcap","#eta of tracked leg hlt objects in endcap with pt>27","#eta","c32","","tracked_endcap_hlt_object_eta_OneEndcap.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"phiTrackedEndcapHltEle>>trackedphiOneEndcap(100,-4.0,4.0)","trackedphiOneEndcap","#phi of tracked leg hlt objects in endcap with pt>27","#phi","c33","","tracked_endcap_hlt_object_phi_OneEndcap.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"clusterShapeTrackedEndcapHltEle>>trackedclusterShapeOneEndcap(100,0.,0.4)","trackedclusterShapeOneEndcap","#sigma i#eta i#eta of tracked leg hlt objects in endcap with pt>27","#sigma i#eta i#eta","c34","","tracked_endcap_hlt_object_clusterShape_OneEndcap.png",false, false);

	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hadEmTrackedEndcapHltEle>>trackedhadEmOneEndcap(100,0.,0.8)","trackedhadEmOneEndcap","Had/Em/energy of tracked leg hlt objects in endcap with pt>27","Had/Em/Energy (1/GeV)","c35","","tracked_endcap_hlt_object_hadEm_OneEndcap.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ecalIsoTrackedEndcapHltEle>>trackedecalIsoOneEndcap(100,-0.15,1.1)","trackedecalIsoOneEndcap","EcalIso/pt of tracked leg hlt objects in endcap with pt>27","EcalIso/pt (1/GeV)","c36","","tracked_endcap_hlt_object_ecalIso_OneEndcap.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hcalIsoTrackedEndcapHltEle>>trackedhcalIsoOneEndcap(100,-0.15,1.1)","trackedhcalIsoOneEndcap","HcalIso/pt of tracked leg hlt objects in endcap with pt>27","HcalIso/pt","c37","","tracked_endcap_hlt_object_hcalIso_OneEndcap.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"epTrackedEndcapHltEle>>trackedepOneEndcap(100,-0.01,0.3)","trackedepOneEndcap","(1/E) - (1/P) of tracked leg hlt objects in endcap with pt>27","(1/E)-(1/P) (1/GeV)","c38","","tracked_endcap_hlt_object_ep_OneEndcap.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dEtaTrackedEndcapHltEle>>trackeddEtaOneEndcap(100,-0.015,0.1)","trackeddEtaOneEndcap","#Delta #eta of tracked leg hlt objects in endcap with pt>27","#Delta #eta","c39","","tracked_endcap_hlt_object_dEta_OneEndcap.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dPhiTrackedEndcapHltEle>>trackeddPhiOneEndcap(100,-0.02,0.3)","trackeddPhiOneEndcap","#Delta #phi of tracked leg hlt objects in endcap with pt>27","#Delta #phi","c40","","tracked_endcap_hlt_object_dPhi_OneEndcap.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"trackIsoTrackedEndcapHltEle>>trackedtrackIsoOneEndcap(100,-0.05,1.25)","trackedtrackIsoOneEndcap","TrackIso/pt of tracked leg hlt objects in endcap with pt>27","TrackIso/pt (1/GeV)","c41","","tracked_endcap_hlt_object_trackIso_OneEndcap.png",false, true);
	

	////plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects which would be run through the trackless leg
	////and have pt>15.  No other requirements (on tracked or trackless RECs) are applied.  
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"ptTracklessHltEle>>tracklessptOne(100,0.,100.)","tracklessptOne","P_{T} of trackless leg hlt objects before all filters with trackless pt>15","pt (GeV)","c12","","trackless_hlt_object_pt_One.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"etaTracklessHltEle>>tracklessetaOne(100,-3.0,3.0)","tracklessetaOne","#eta of trackless leg hlt objects before all filters with trackless pt>15","#eta","c13","","trackless_hlt_object_eta_One.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"phiTracklessHltEle>>tracklessphiOne(100,-4.0,4.0)","tracklessphiOne","#phi of trackless leg hlt objects before all filters with trackless pt>15","#phi","c14","","trackless_hlt_object_phi_One.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"clusterShapeTracklessHltEle>>tracklessclusterShapeOne(100,0.,0.06)","tracklessclusterShapeOne","#sigma i#eta i#eta of trackless leg hlt objects before all filters with trackless pt>15","#sigma i#eta i#eta","c15","","trackless_hlt_object_clusterShape_One.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"ecalIsoTracklessHltEle>>tracklessecalIsoOne(100,-0.2,0.6)","tracklessecalIsoOne","EcalIso/pt of trackless leg hlt objects before all filters with trackless pt>15","EcalIso/pt (1/GeV)","c16","","trackless_hlt_object_ecalIso_One.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"hadEmTracklessHltEle>>tracklesshadEmOne(100,0.,0.6)","tracklesshadEmOne","Had/Em/energy of trackless leg hlt objects before all filters with trackless pt>15","Had/Em/energy","c17","","trackless_hlt_object_hadEm_One.png",false, true);

	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"hcalIsoTracklessHltEle>>tracklesshcalIsoOne(100,-1.0,3.5)","tracklesshcalIsoOne","HcalIso/pt of trackless leg hlt objects before all filters with trackless pt>15","HcalIso/pt (1/GeV)","c18","","trackless_hlt_object_hcalIso_One.png",false, true);
	

	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects which are made in the tracked leg
	////and have pt>27, in events where there is at least one trackless REC object made in the trackless leg (no pt requirement)
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ptTrackedBarrelHltEle>>trackedptTwo(100,0.,100.)","trackedptTwo","P_{T} of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","pt (GeV)","c1",hasTracklessHlt,"tracked_hlt_object_pt_Two.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"etaTrackedBarrelHltEle>>trackedetaTwo(100,-3.0,3.0)","trackedetaTwo","#eta of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","#eta","c2",hasTracklessHlt,"tracked_hlt_object_eta_Two.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"phiTrackedBarrelHltEle>>trackedphiTwo(100,-4.0,4.0)","trackedphiTwo","#phi of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","#phi","c3",hasTracklessHlt,"tracked_hlt_object_phi_Two.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"clusterShapeTrackedBarrelHltEle>>trackedclusterShapeTwo(100,0.,0.06)","trackedclusterShapeTwo","#sigma i#eta i#eta of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","#sigma i#eta i#eta","c4",hasTracklessHlt,"tracked_hlt_object_clusterShape_Two.png",false, false);

	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hadEmTrackedBarrelHltEle>>trackedhadEmTwo(100,0.,0.6)","trackedhadEmTwo","Had/Em/energy of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","Had/Em/Energy (1/GeV)","c5",hasTracklessHlt,"tracked_hlt_object_hadEm_Two.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ecalIsoTrackedBarrelHltEle>>trackedecalIsoTwo(100,-0.2,0.6)","trackedecalIsoTwo","EcalIso/pt of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","EcalIso/pt (1/GeV)","c6",hasTracklessHlt,"tracked_hlt_object_ecalIso_Two.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hcalIsoTrackedBarrelHltEle>>trackedhcalIsoTwo(100,-0.2,0.6)","trackedhcalIsoTwo","HcalIso/pt of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","HcalIso/pt","c7",hasTracklessHlt,"tracked_hlt_object_hcalIso_Two.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"epTrackedBarrelHltEle>>trackedepTwo(100,0.,0.03)","trackedepTwo","(1/E) - (1/P) of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","(1/E)-(1/P) (1/GeV)","c8",hasTracklessHlt,"tracked_hlt_object_ep_Two.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dEtaTrackedBarrelHltEle>>trackeddEtaTwo(100,0.,0.1)","trackeddEtaTwo","#Delta #eta of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","#Delta #eta","c9",hasTracklessHlt,"tracked_hlt_object_dEta_Two.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dPhiTrackedBarrelHltEle>>trackeddPhiTwo(100,0.,0.1)","trackeddPhiTwo","#Delta #phi of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","#Delta #phi","c10",hasTracklessHlt,"tracked_hlt_object_dPhi_Two.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"trackIsoTrackedBarrelHltEle>>trackedtrackIsoTwo(100,-0.1,0.6)","trackedtrackIsoTwo","TrackIso/pt of tracked leg hlt objects with tracked pt>27 in evts with at least one trackless REC","TrackIso/pt (1/GeV)","c11",hasTracklessHlt,"tracked_hlt_object_trackIso_Two.png",false, true);


	////plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects which are made in the trackless leg
	////and have pt>15, in evts where there is at least one tracked REC obj which is made by the tracked leg 
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"ptTracklessHltEle>>tracklessptTwo(100,0.,100.)","tracklessptTwo","P_{T} of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","pt (GeV)","c12",hasTrackedHlt,"trackless_hlt_object_pt_Two.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"etaTracklessHltEle>>tracklessetaTwo(100,-3.0,3.0)","tracklessetaTwo","#eta of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","#eta","c13",hasTrackedHlt,"trackless_hlt_object_eta_Two.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"phiTracklessHltEle>>tracklessphiTwo(100,-4.0,4.0)","tracklessphiTwo","#phi of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","#phi","c14",hasTrackedHlt,"trackless_hlt_object_phi_Two.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"clusterShapeTracklessHltEle>>tracklessclusterShapeTwo(100,0.,0.06)","tracklessclusterShapeTwo","#sigma i#eta i#eta of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","#sigma i#eta i#eta","c15",hasTrackedHlt,"trackless_hlt_object_clusterShape_Two.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"ecalIsoTracklessHltEle>>tracklessecalIsoTwo(100,-0.2,0.6)","tracklessecalIsoTwo","EcalIso/pt of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","EcalIso/pt (1/GeV)","c16",hasTrackedHlt,"trackless_hlt_object_ecalIso_Two.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"hadEmTracklessHltEle>>tracklesshadEmTwo(100,0.,0.6)","tracklesshadEmTwo","Had/Em/energy of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","Had/Em/energy","c17",hasTrackedHlt,"trackless_hlt_object_hadEm_Two.png",false, true);

	//makeAndSaveSingleTreeHisto(hltObjectsTracklessPtTree,"hcalIsoTracklessHltEle>>tracklesshcalIsoTwo(100,-1.0,3.5)","tracklesshcalIsoTwo","HcalIso/pt of trackless leg hlt objects with trackless pt>15 in evts with at least one tracked REC","HcalIso/pt (1/GeV)","c18",hasTrackedHlt,"trackless_hlt_object_hcalIso_Two.png",false, true);


	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



	//make these two plots to show that a dR <= 0.1 for matching HLT REC to GEN electron objects is reasonable
	//the evts which go into these plots satisfy all GEN lvl Z->ee requirements, have at least one tracked leg REC with pt>27,
	//and at least one trackless leg REC with pt>15 
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"deltaRTrackedBarrelHltEle>>trackeddeltaRTwoAndHalf(100,0.,0.35)","trackeddeltaRTwoAndHalf","#DeltaR of tracked leg hlt objects to tracked GEN electrons in Z->ee evts","#DeltaR","c98","","tracked_hlt_object_deltaR_TwoAndHalf.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"deltaRTracklessHltEle>>tracklessdeltaRTwoAndHalf(100,0.,0.35)","tracklessdeltaRTwoAndHalf","#DeltaR of trackless leg hlt objects to trackless GEN electrons in Z->ee evts","#DeltaR","c99","","trackless_hlt_object_deltaR_TwoAndHalf.png",false, false);
		

	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



	//plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects which pass the very loose tracked leg
	//and have pt>27 and are within dR = 0.1 of a tracked GEN electron with pt>27
	//in events where there is at least one trackless REC object with pt>15 which is also matched within dR = 0.1 to a
	//trackless GEN electron with pt>15.  The GEN dilepton mass must be between 60 and 120 GeV. 
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"ptTrackedBarrelHltEle>>trackedptThree(100,0.,100.)","trackedptThree","P_{T} of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","pt (GeV)","c1","","tracked_hlt_object_pt_Three.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"etaTrackedBarrelHltEle>>trackedetaThree(100,-3.0,3.0)","trackedetaThree","#eta of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","#eta","c2","","tracked_hlt_object_eta_Three.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"phiTrackedBarrelHltEle>>trackedphiThree(100,-4.0,4.0)","trackedphiThree","#phi of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","#phi","c3","","tracked_hlt_object_phi_Three.png",false, false);
	
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"clusterShapeTrackedBarrelHltEle>>trackedclusterShapeThree(100,0.,0.06)","trackedclusterShapeThree","#sigma i#eta i#eta of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","#sigma i#eta i#eta","c4","","tracked_hlt_object_clusterShape_Three.png",false, false);

	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"hadEmTrackedBarrelHltEle>>trackedhadEmThree(100,0.,0.6)","trackedhadEmThree","Had/Em/energy of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","Had/Em/Energy (1/GeV)","c5","","tracked_hlt_object_hadEm_Three.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"ecalIsoTrackedBarrelHltEle>>trackedecalIsoThree(100,-0.2,0.6)","trackedecalIsoThree","EcalIso/pt of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","EcalIso/pt (1/GeV)","c6","","tracked_hlt_object_ecalIso_Three.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"hcalIsoTrackedBarrelHltEle>>trackedhcalIsoThree(100,-0.2,0.6)","trackedhcalIsoThree","HcalIso/pt of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","HcalIso/pt","c7","","tracked_hlt_object_hcalIso_Three.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"epTrackedBarrelHltEle>>trackedepThree(100,0.,0.03)","trackedepThree","(1/E) - (1/P) of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","(1/E)-(1/P) (1/GeV)","c8","","tracked_hlt_object_ep_Three.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"dEtaTrackedBarrelHltEle>>trackeddEtaThree(100,0.,0.1)","trackeddEtaThree","#Delta #eta of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","#Delta #eta","c9","","tracked_hlt_object_dEta_Three.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"dPhiTrackedBarrelHltEle>>trackeddPhiThree(100,0.,0.1)","trackeddPhiThree","#Delta #phi of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","#Delta #phi","c10","","tracked_hlt_object_dPhi_Three.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"trackIsoTrackedBarrelHltEle>>trackedtrackIsoThree(100,-0.1,0.6)","trackedtrackIsoThree","TrackIso/pt of tracked leg hlt objects with pt>27 matched to GEN tracked electrons","TrackIso/pt (1/GeV)","c11","","tracked_hlt_object_trackIso_Three.png",false, true);



	////plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects which pass the very loose trackless leg
	////and have pt>15 and are within dR = 0.1 of a trackless GEN electron with pt>15
	////in evts where there is at least one tracked REC obj with pt>27 which is matched within dR = 0.1 to a tracked
	////GEN electron with pt>27.  The GEN dilepton mass must be btwn 60 and 120 GeV. 
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"ptTracklessHltEle>>tracklessptThree(100,0.,100.)","tracklessptThree","P_{T} of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","pt (GeV)","c12","","trackless_hlt_object_pt_Three.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"etaTracklessHltEle>>tracklessetaThree(100,-3.0,3.0)","tracklessetaThree","#eta of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","#eta","c13","","trackless_hlt_object_eta_Three.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"phiTracklessHltEle>>tracklessphiThree(100,-4.0,4.0)","tracklessphiThree","#phi of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","#phi","c14","","trackless_hlt_object_phi_Three.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"clusterShapeTracklessHltEle>>tracklessclusterShapeThree(100,0.,0.06)","tracklessclusterShapeThree","#sigma i#eta i#eta of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","#sigma i#eta i#eta","c15","","trackless_hlt_object_clusterShape_Three.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"ecalIsoTracklessHltEle>>tracklessecalIsoThree(100,-0.2,0.6)","tracklessecalIsoThree","EcalIso/pt of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","EcalIso/pt (1/GeV)","c16","","trackless_hlt_object_ecalIso_Three.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"hadEmTracklessHltEle>>tracklesshadEmThree(100,0.,0.6)","tracklesshadEmThree","Had/Em/energy of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","Had/Em/energy","c17","","trackless_hlt_object_hadEm_Three.png",false, true);

	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"hcalIsoTracklessHltEle>>tracklesshcalIsoThree(100,-1.0,3.5)","tracklesshcalIsoThree","HcalIso/pt of trackless leg hlt objects with pt>15 matched to GEN trackless electrons","HcalIso/pt (1/GeV)","c18","","trackless_hlt_object_hcalIso_Three.png",false, true);
	


}//end testMacro()


