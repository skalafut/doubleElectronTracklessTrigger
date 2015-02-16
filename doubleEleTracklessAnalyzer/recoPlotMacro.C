#include <TFile.h>
#include <TTree.h>
#include <TROOT.h>
#include <TCanvas.h>
#include <TString.h>
#include <TCut.h>
#include <TH1F.h>
#include <TMath.h>
#include <TStyle.h>
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

//use this method to loop over all evts in a tree, identify the  
//void filterMakeAndSaveTreeHisto(){
//
//}

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

void recoPlotMacro(){

	TFile * f1 = new TFile("/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/experiment.root");

	//tree made from tracked leg RecoEcalCandidate (REC) objects with |eta| < 2.5, and trackless leg
	//RECs with 2.5 < |eta| < 3.0 
	TTree * hltObjectsTree = (TTree*) f1->Get("recoAnalyzerZero/recoTreeBeforeTriggerFilters");
	
	//tree made from tracked leg RECs with |eta| < 2.5 and pt>27, and trackless leg RECs with
	//2.5 < |eta| < 3.0
	//require nTracklessHltEle > 0 to filter out evts which do not have a trackless leg REC 
	//TTree * hltObjectsTrackedPtTree = (TTree*) f1->Get("recoAnalyzerOne/recoTreeBeforeTriggerFiltersTrackedPtRequirement");
	
	//tree made from tracked leg RECs with |eta| < 2.5, and trackless leg RECs with
	//2.5 < |eta| < 3.0 and pt>15
	//TTree * hltObjectsTracklessPtTree = (TTree*) f1->Get("recoAnalyzerTwo/recoTreeBeforeTriggerFiltersTracklessPtRequirement");
	
	//tree made from tracked leg RECs with |eta| < 2.5 and pt>27, and trackless leg RECs with
	//2.5 < |eta| < 3.0 and pt>15. The tracked leg REC is matched to a GEN tracked electron with pt>27, and the
	//trackless leg REC is matched to a trackless GEN electron with pt>15.  The invariant mass of the
	//GEN lvl electrons is btwn 60 and 120 GeV.
	//deltaR information is stored in this tree
	//TTree * hltObjectsMatchedTree = (TTree*) f1->Get("recoAnalyzerThree/recoTreeBeforeTriggerFiltersBothMatch");



	//TCut objects 
	//TCut tracklessEtaLow = "TMath::Abs(etaTracklessHltEle)>2.5";
	//require that a tracked leg or trackless leg REC object exists
	TCut hasTrackedBarrelHlt = "nTrackedBarrelHltEle>0";
	TCut hasTrackedEndcapHlt = "nTrackedEndcapHltEle>0";
	TCut hasTrackedHlt = hasTrackedBarrelHlt+hasTrackedEndcapHlt;
	TCut hasTracklessHlt = "nTracklessHltEle>0";

	gStyle->SetOptStat(1111111);

	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects made at the start of the tracked leg
	//tracked objs in barrel
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTrackedBarrelHltEle>>trackedptZeroBarrel(100,0.,100.)","trackedptZeroBarrel","P_{T} of tracked leg hlt objects in barrel before all filters","pt (GeV)","c1","","tracked_barrel_hlt_object_pt_ZeroBarrel.png",true, false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTrackedBarrelHltEle>>trackedetaZeroBarrel(100,-3.0,3.0)","trackedetaZeroBarrel","#eta of tracked leg hlt objects in barrel before all filters","#eta","c2","","tracked_barrel_hlt_object_eta_ZeroBarrel.png",false, false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTrackedBarrelHltEle>>trackedphiZeroBarrel(100,-4.0,4.0)","trackedphiZeroBarrel","#phi of tracked leg hlt objects in barrel before all filters","#phi","c3","","tracked_barrel_hlt_object_phi_ZeroBarrel.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"clusterShapeTrackedBarrelHltEle>>trackedclusterShapeZeroBarrel(100,0.,0.03)","trackedclusterShapeZeroBarrel","#sigma i#eta i#eta of tracked leg hlt objects in barrel before all filters","#sigma i#eta i#eta","c4","","tracked_barrel_hlt_object_clusterShape_ZeroBarrel.png",false, false);

	makeAndSaveSingleTreeHisto(hltObjectsTree,"hadEmTrackedBarrelHltEle>>trackedhadEmZeroBarrel(100,0.,0.6)","trackedhadEmZeroBarrel","Had/Em/energy of tracked leg hlt objects in barrel before all filters","Had/Em/Energy (1/GeV)","c5","","tracked_barrel_hlt_object_hadEm_ZeroBarrel.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ecalIsoTrackedBarrelHltEle>>trackedecalIsoZeroBarrel(100,-0.2,0.6)","trackedecalIsoZeroBarrel","EcalIso/pt of tracked leg hlt objects in barrel before all filters","EcalIso/pt (1/GeV)","c6","","tracked_barrel_hlt_object_ecalIso_ZeroBarrel.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"hcalIsoTrackedBarrelHltEle>>trackedhcalIsoZeroBarrel(100,-0.2,0.6)","trackedhcalIsoZeroBarrel","HcalIso/pt of tracked leg hlt objects in barrel before all filters","HcalIso/pt","c7","","tracked_barrel_hlt_object_hcalIso_ZeroBarrel.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"epTrackedBarrelHltEle>>trackedepZeroBarrel(100,0.,0.03)","trackedepZeroBarrel","(1/E) - (1/P) of tracked leg hlt objects in barrel before all filters","(1/E)-(1/P) (1/GeV)","c8","","tracked_barrel_hlt_object_ep_ZeroBarrel.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"dEtaTrackedBarrelHltEle>>trackeddEtaZeroBarrel(100,0.,0.1)","trackeddEtaZeroBarrel","#Delta #eta of tracked leg hlt objects in barrel before all filters","#Delta #eta","c9","","tracked_barrel_hlt_object_dEta_ZeroBarrel.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"dPhiTrackedBarrelHltEle>>trackeddPhiZeroBarrel(100,0.,0.1)","trackeddPhiZeroBarrel","#Delta #phi of tracked leg hlt objects in barrel before all filters","#Delta #phi","c10","","tracked_barrel_hlt_object_dPhi_ZeroBarrel.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"trackIsoTrackedBarrelHltEle>>trackedtrackIsoZeroBarrel(100,-0.1,0.6)","trackedtrackIsoZeroBarrel","TrackIso/pt of tracked leg hlt objects in barrel before all filters","TrackIso/pt (1/GeV)","c11","","tracked_barrel_hlt_object_trackIso_ZeroBarrel.png",false, true);


	//tracked objs in endcap
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTrackedEndcapHltEle>>trackedptZeroEndcap(100,0.,100.)","trackedptZeroEndcap","P_{T} of tracked leg hlt objects in endcap before all filters","pt (GeV)","c31","","tracked_endcap_hlt_object_pt_ZeroEndcap.png",true, false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTrackedEndcapHltEle>>trackedetaZeroEndcap(100,-3.0,3.0)","trackedetaZeroEndcap","#eta of tracked leg hlt objects in endcap before all filters","#eta","c32","","tracked_endcap_hlt_object_eta_ZeroEndcap.png",false, false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTrackedEndcapHltEle>>trackedphiZeroEndcap(100,-4.0,4.0)","trackedphiZeroEndcap","#phi of tracked leg hlt objects in endcap before all filters","#phi","c33","","tracked_endcap_hlt_object_phi_ZeroEndcap.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"clusterShapeTrackedEndcapHltEle>>trackedclusterShapeZeroEndcap(100,0.,0.04)","trackedclusterShapeZeroEndcap","#sigma i#eta i#eta of tracked leg hlt objects in endcap before all filters","#sigma i#eta i#eta","c34","","tracked_endcap_hlt_object_clusterShape_ZeroEndcap.png",false, false);

	makeAndSaveSingleTreeHisto(hltObjectsTree,"hadEmTrackedEndcapHltEle>>trackedhadEmZeroEndcap(100,0.,0.6)","trackedhadEmZeroEndcap","Had/Em/energy of tracked leg hlt objects in endcap before all filters","Had/Em/Energy (1/GeV)","c35","","tracked_endcap_hlt_object_hadEm_ZeroEndcap.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ecalIsoTrackedEndcapHltEle>>trackedecalIsoZeroEndcap(100,-0.2,0.6)","trackedecalIsoZeroEndcap","EcalIso/pt of tracked leg hlt objects in endcap before all filters","EcalIso/pt (1/GeV)","c36","","tracked_endcap_hlt_object_ecalIso_ZeroEndcap.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"hcalIsoTrackedEndcapHltEle>>trackedhcalIsoZeroEndcap(100,-0.2,0.6)","trackedhcalIsoZeroEndcap","HcalIso/pt of tracked leg hlt objects in endcap before all filters","HcalIso/pt","c37","","tracked_endcap_hlt_object_hcalIso_ZeroEndcap.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"epTrackedEndcapHltEle>>trackedepZeroEndcap(100,0.,0.03)","trackedepZeroEndcap","(1/E) - (1/P) of tracked leg hlt objects in endcap before all filters","(1/E)-(1/P) (1/GeV)","c38","","tracked_endcap_hlt_object_ep_ZeroEndcap.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"dEtaTrackedEndcapHltEle>>trackeddEtaZeroEndcap(100,0.,0.1)","trackeddEtaZeroEndcap","#Delta #eta of tracked leg hlt objects in endcap before all filters","#Delta #eta","c39","","tracked_endcap_hlt_object_dEta_ZeroEndcap.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"dPhiTrackedEndcapHltEle>>trackeddPhiZeroEndcap(100,0.,0.1)","trackeddPhiZeroEndcap","#Delta #phi of tracked leg hlt objects in endcap before all filters","#Delta #phi","c40","","tracked_endcap_hlt_object_dPhi_ZeroEndcap.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"trackIsoTrackedEndcapHltEle>>trackedtrackIsoZeroEndcap(100,-0.1,0.6)","trackedtrackIsoZeroEndcap","TrackIso/pt of tracked leg hlt objects in endcap before all filters","TrackIso/pt (1/GeV)","c41","","tracked_endcap_hlt_object_trackIso_ZeroEndcap.png",false, true);
	
	
	//plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects made at the start of the trackless leg
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ptTracklessHltEle>>tracklessptZero(100,0.,100.)","tracklessptZero","P_{T} of trackless leg hlt objects before all filters","pt (GeV)","c12","","trackless_hlt_object_pt_Zero.png",true, false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"etaTracklessHltEle>>tracklessetaZero(100,-3.0,3.0)","tracklessetaZero","#eta of trackless leg hlt objects before all filters","#eta","c13","","trackless_hlt_object_eta_Zero.png",false, false);
	makeAndSaveSingleTreeHisto(hltObjectsTree,"phiTracklessHltEle>>tracklessphiZero(100,-4.0,4.0)","tracklessphiZero","#phi of trackless leg hlt objects before all filters","#phi","c14","","trackless_hlt_object_phi_Zero.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"clusterShapeTracklessHltEle>>tracklessclusterShapeZero(100,0.,0.06)","tracklessclusterShapeZero","#sigma i#eta i#eta of trackless leg hlt objects before all filters","#sigma i#eta i#eta","c15","","trackless_hlt_object_clusterShape_Zero.png",false, false);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"ecalIsoTracklessHltEle>>tracklessecalIsoZero(100,-0.2,0.6)","tracklessecalIsoZero","EcalIso/pt of trackless leg hlt objects before all filters","EcalIso/pt (1/GeV)","c16","","trackless_hlt_object_ecalIso_Zero.png",false, true);
	
	makeAndSaveSingleTreeHisto(hltObjectsTree,"hadEmTracklessHltEle>>tracklesshadEmZero(100,0.,0.6)","tracklesshadEmZero","Had/Em/energy of trackless leg hlt objects before all filters","Had/Em/energy","c17","","trackless_hlt_object_hadEm_Zero.png",false, true);

	makeAndSaveSingleTreeHisto(hltObjectsTree,"hcalIsoTracklessHltEle>>tracklesshcalIsoZero(100,-1.0,5.0)","tracklesshcalIsoZero","HcalIso/pt of trackless leg hlt objects before all filters","HcalIso/pt (1/GeV)","c18","","trackless_hlt_object_hcalIso_Zero.png",false, true);



	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects made at the start of the tracked leg
	////which have pt>27
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ptTrackedBarrelHltEle>>trackedptOne(100,0.,100.)","trackedptOne","P_{T} of tracked leg hlt objects before all filters with tracked pt>27","pt (GeV)","c1","","tracked_hlt_object_pt_One.png",true, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"etaTrackedBarrelHltEle>>trackedetaOne(100,-3.0,3.0)","trackedetaOne","#eta of tracked leg hlt objects before all filters with tracked pt>27","#eta","c2","","tracked_hlt_object_eta_One.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"phiTrackedBarrelHltEle>>trackedphiOne(100,-4.0,4.0)","trackedphiOne","#phi of tracked leg hlt objects before all filters with tracked pt>27","#phi","c3","","tracked_hlt_object_phi_One.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"clusterShapeTrackedBarrelHltEle>>trackedclusterShapeOne(100,0.,0.06)","trackedclusterShapeOne","#sigma i#eta i#eta of tracked leg hlt objects before all filters with tracked pt>27","#sigma i#eta i#eta","c4","","tracked_hlt_object_clusterShape_One.png",false, false);

	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hadEmTrackedBarrelHltEle>>trackedhadEmOne(100,0.,0.6)","trackedhadEmOne","Had/Em/energy of tracked leg hlt objects before all filters with tracked pt>27","Had/Em/Energy (1/GeV)","c5","","tracked_hlt_object_hadEm_One.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"ecalIsoTrackedBarrelHltEle>>trackedecalIsoOne(100,-0.2,0.6)","trackedecalIsoOne","EcalIso/pt of tracked leg hlt objects before all filters with tracked pt>27","EcalIso/pt (1/GeV)","c6","","tracked_hlt_object_ecalIso_One.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"hcalIsoTrackedBarrelHltEle>>trackedhcalIsoOne(100,-0.2,0.6)","trackedhcalIsoOne","HcalIso/pt of tracked leg hlt objects before all filters with tracked pt>27","HcalIso/pt","c7","","tracked_hlt_object_hcalIso_One.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"epTrackedBarrelHltEle>>trackedepOne(100,0.,0.03)","trackedepOne","(1/E) - (1/P) of tracked leg hlt objects before all filters with tracked pt>27","(1/E)-(1/P) (1/GeV)","c8","","tracked_hlt_object_ep_One.png",false, true);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dEtaTrackedBarrelHltEle>>trackeddEtaOne(100,0.,0.1)","trackeddEtaOne","#Delta #eta of tracked leg hlt objects before all filters with tracked pt>27","#Delta #eta","c9","","tracked_hlt_object_dEta_One.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"dPhiTrackedBarrelHltEle>>trackeddPhiOne(100,0.,0.1)","trackeddPhiOne","#Delta #phi of tracked leg hlt objects before all filters with tracked pt>27","#Delta #phi","c10","","tracked_hlt_object_dPhi_One.png",false, false);
	//
	//makeAndSaveSingleTreeHisto(hltObjectsTrackedPtTree,"trackIsoTrackedBarrelHltEle>>trackedtrackIsoOne(100,-0.1,0.6)","trackedtrackIsoOne","TrackIso/pt of tracked leg hlt objects before all filters with tracked pt>27","TrackIso/pt (1/GeV)","c11","","tracked_hlt_object_trackIso_One.png",false, true);


	////plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects made at the start of the trackless leg
	////which have pt>15
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
	


	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects made at the start of the tracked leg
	////which have pt>27, in events where there is at least one trackless REC object (no pt requirement)
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


	////plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects made at the start of the trackless leg
	////which have pt>15, in evts where there is at least one tracked REC obj (no pt requirement)
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



	//make these two plots to show that a dR <= 0.1 for matching HLT REC to GEN electron objects is reasonable
	//the evts which go into these plots satisfy all GEN lvl Z->ee requirements, have at least one tracked leg REC with pt>27,
	//and at least one trackless leg REC with pt>15 
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"deltaRTrackedBarrelHltEle>>trackeddeltaRTwoAndHalf(100,0.,0.35)","trackeddeltaRTwoAndHalf","#DeltaR of tracked leg hlt objects to tracked GEN electrons in Z->ee evts","#DeltaR","c98","","tracked_hlt_object_deltaR_TwoAndHalf.png",false, false);
	//makeAndSaveSingleTreeHisto(hltObjectsMatchedTree,"deltaRTracklessHltEle>>tracklessdeltaRTwoAndHalf(100,0.,0.35)","tracklessdeltaRTwoAndHalf","#DeltaR of trackless leg hlt objects to trackless GEN electrons in Z->ee evts","#DeltaR","c99","","trackless_hlt_object_deltaR_TwoAndHalf.png",false, false);
		


	//plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects made at the start of the tracked leg
	//which have pt>27 and are within dR = 0.1 of a tracked GEN electron with pt>27
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



	////plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects made at the start of the trackless leg
	////which have pt>15 and are within dR = 0.1 of a trackless GEN electron with pt>15
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
	


}//end recoPlotMacro()


