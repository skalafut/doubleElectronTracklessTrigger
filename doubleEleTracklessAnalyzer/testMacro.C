#include <TFile.h>
#include <TTree.h>
#include <TChain.h>
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

//use this fxn to compare pt, eta, phi distributions of reco signal objects which have been matched
//to GEN signal objects. The GEN signal objects have passed all GEN selection requirements.
//the GEN and matched reco object kinematic info is stored in the same TTree
//make the pt, eta, and phi histogram overlays for tracked and trackless leg RECs whenever this fxn is called
void matchedRecoToGenOverlayHistos(TChain * trackedChain,TCut trackedCuts,TChain * tracklessChain,TCut tracklessCuts){
	trackedChain->Draw(">>matchedTrackedList",trackedCuts,"entrylistarray");
	trackedChain->SetEntryList((TEntryListArray*) gROOT->FindObject("matchedTrackedList"));
	
	tracklessChain->Draw(">>matchedTracklessList",tracklessCuts,"entrylistarray");
	tracklessChain->SetEntryList((TEntryListArray*) gROOT->FindObject("matchedTracklessList"));

	//tracked quantities
	TCanvas * c200 = new TCanvas("c200","c200",500,500);
	c200->cd();
	trackedChain->Draw("etaHltEle>>trackedHltEta(100,-3.5,3.5)");
	trackedChain->Draw("etaGenEle>>trackedGenEta(100,-3.5,3.5)");
	TH1F * trackedHltEtaHist = (TH1F*) gROOT->FindObject("trackedHltEta");
	TH1F * trackedGenEtaHist = (TH1F*) gROOT->FindObject("trackedGenEta");
	trackedHltEtaHist->SetTitle("matched reco (black) and gen (red) tracked electron #eta");
	trackedHltEtaHist->GetXaxis()->SetTitle("#eta");
	char tempTrackedEta[130];
	sprintf(tempTrackedEta,"Events / %.2f ", trackedHltEtaHist->GetXaxis()->GetBinWidth(1));
	trackedHltEtaHist->GetYaxis()->SetTitle(tempTrackedEta);
	trackedHltEtaHist->SetLineColor(1);	//black
	trackedGenEtaHist->SetLineColor(2);	//red
	trackedHltEtaHist->Draw();
	trackedGenEtaHist->Draw("same");
	c200->SaveAs("tracked_gen_and_matched_reco_eta.png","recreate");

	TCanvas * c201 = new TCanvas("c201","c201",500,500);
	c201->cd();
	trackedChain->Draw("ptHltEle>>trackedHltPt(100,0.,100.)");
	trackedChain->Draw("ptGenEle>>trackedGenPt(100,0.,100.)");
	TH1F * trackedHltPtHist = (TH1F*) gROOT->FindObject("trackedHltPt");
	TH1F * trackedGenPtHist = (TH1F*) gROOT->FindObject("trackedGenPt");
	trackedHltPtHist->SetTitle("matched reco (black) and gen (red) tracked electron P_{T}");
	trackedHltPtHist->GetXaxis()->SetTitle("pt (GeV)");
	trackedHltPtHist->SetMaximum((1.1)*(trackedGenPtHist->GetBinContent(trackedGenPtHist->GetMaximumBin() )) );
	char tempTrackedPt[130];
	sprintf(tempTrackedPt,"Events / %.2f GeV ", trackedHltPtHist->GetXaxis()->GetBinWidth(1));
	trackedHltPtHist->GetYaxis()->SetTitle(tempTrackedPt);
	trackedHltPtHist->SetLineColor(1);	//black
	trackedGenPtHist->SetLineColor(2);	//red
	trackedHltPtHist->Draw();
	trackedGenPtHist->Draw("same");
	c201->SaveAs("tracked_gen_and_matched_reco_pt.png","recreate");

	TCanvas * c202 = new TCanvas("c202","c202",500,500);
	c202->cd();
	trackedChain->Draw("phiHltEle>>trackedHltPhi(100,-3.5,3.5)");
	trackedChain->Draw("phiGenEle>>trackedGenPhi(100,-3.5,3.5)");
	TH1F * trackedHltPhiHist = (TH1F*) gROOT->FindObject("trackedHltPhi");
	TH1F * trackedGenPhiHist = (TH1F*) gROOT->FindObject("trackedGenPhi");
	trackedHltPhiHist->SetTitle("matched reco (black) and gen (red) tracked electron #phi");
	trackedHltPhiHist->GetXaxis()->SetTitle("#phi");
	char tempTrackedPhi[130];
	sprintf(tempTrackedPhi,"Events / %.2f ", trackedHltPhiHist->GetXaxis()->GetBinWidth(1));
	trackedHltPhiHist->GetYaxis()->SetTitle(tempTrackedPhi);
	trackedHltPhiHist->SetLineColor(1);	//black
	trackedGenPhiHist->SetLineColor(2);	//red
	trackedHltPhiHist->Draw();
	trackedGenPhiHist->Draw("same");
	c202->SaveAs("tracked_gen_and_matched_reco_phi.png","recreate");

	TCanvas * c203 = new TCanvas("c203","c203",500,500);
	c203->cd();
	trackedChain->Draw("diObjectMassHltEle>>trackedHltDiObjectMass(150,-2.,140.)");
	trackedChain->Draw("diObjectMassGenEle>>trackedGenDiObjectMass(150,-2.,140.)");
	TH1F * trackedHltDiObjectMassHist = (TH1F*) gROOT->FindObject("trackedHltDiObjectMass");
	TH1F * trackedGenDiObjectMassHist = (TH1F*) gROOT->FindObject("trackedGenDiObjectMass");
	trackedHltDiObjectMassHist->SetTitle("parent mass of matched reco (black) and gen (red) tracked electron");
	trackedHltDiObjectMassHist->GetXaxis()->SetTitle("diObjectMass (GeV)");
	trackedHltDiObjectMassHist->SetMaximum((1.1)*(trackedGenDiObjectMassHist->GetBinContent(trackedGenDiObjectMassHist->GetMaximumBin() )) );
	char tempTrackedDiObjectMass[130];
	sprintf(tempTrackedDiObjectMass,"Events / %.2f GeV ", trackedHltDiObjectMassHist->GetXaxis()->GetBinWidth(1));
	trackedHltDiObjectMassHist->GetYaxis()->SetTitle(tempTrackedDiObjectMass);
	trackedHltDiObjectMassHist->SetLineColor(1);	//black
	trackedGenDiObjectMassHist->SetLineColor(2);	//red
	trackedHltDiObjectMassHist->Draw();
	trackedGenDiObjectMassHist->Draw("same");
	c203->SaveAs("parent_inv_mass_tracked_gen_and_matched_reco.png","recreate");


	//trackless quantities
	TCanvas * c300 = new TCanvas("c300","c300",500,500);
	c300->cd();
	tracklessChain->Draw("etaHltEle>>tracklessHltEta(100,-3.5,3.5)");
	tracklessChain->Draw("etaGenEle>>tracklessGenEta(100,-3.5,3.5)");
	TH1F * tracklessHltEtaHist = (TH1F*) gROOT->FindObject("tracklessHltEta");
	TH1F * tracklessGenEtaHist = (TH1F*) gROOT->FindObject("tracklessGenEta");
	tracklessHltEtaHist->SetTitle("matched reco (black) and gen (red) trackless electron #eta");
	tracklessHltEtaHist->GetXaxis()->SetTitle("#eta");
	char tempTracklessEta[130];
	sprintf(tempTracklessEta,"Events / %.2f ", tracklessHltEtaHist->GetXaxis()->GetBinWidth(1));
	tracklessHltEtaHist->GetYaxis()->SetTitle(tempTracklessEta);
	tracklessHltEtaHist->SetLineColor(1);	//black
	tracklessGenEtaHist->SetLineColor(2);	//red
	tracklessHltEtaHist->Draw();
	tracklessGenEtaHist->Draw("same");
	c300->SaveAs("trackless_gen_and_matched_reco_eta.png","recreate");

	TCanvas * c301 = new TCanvas("c301","c301",500,500);
	c301->cd();
	tracklessChain->Draw("ptHltEle>>tracklessHltPt(100,0.,100.)");
	tracklessChain->Draw("ptGenEle>>tracklessGenPt(100,0.,100.)");
	TH1F * tracklessHltPtHist = (TH1F*) gROOT->FindObject("tracklessHltPt");
	TH1F * tracklessGenPtHist = (TH1F*) gROOT->FindObject("tracklessGenPt");
	tracklessHltPtHist->SetTitle("matched reco (black) and gen (red) trackless electron P_{T}");
	tracklessHltPtHist->GetXaxis()->SetTitle("pt (GeV)");
	tracklessHltPtHist->SetMaximum((1.1)*(tracklessGenPtHist->GetBinContent(tracklessGenPtHist->GetMaximumBin() )) );
	char tempTracklessPt[130];
	sprintf(tempTracklessPt,"Events / %.2f GeV ", tracklessHltPtHist->GetXaxis()->GetBinWidth(1));
	tracklessHltPtHist->GetYaxis()->SetTitle(tempTracklessPt);
	tracklessHltPtHist->SetLineColor(1);	//black
	tracklessGenPtHist->SetLineColor(2);	//red
	tracklessHltPtHist->Draw();
	tracklessGenPtHist->Draw("same");
	c301->SaveAs("trackless_gen_and_matched_reco_pt.png","recreate");


	TCanvas * c302 = new TCanvas("c302","c302",500,500);
	c302->cd();
	tracklessChain->Draw("phiHltEle>>tracklessHltPhi(100,-3.5,3.5)");
	tracklessChain->Draw("phiGenEle>>tracklessGenPhi(100,-3.5,3.5)");
	TH1F * tracklessHltPhiHist = (TH1F*) gROOT->FindObject("tracklessHltPhi");
	TH1F * tracklessGenPhiHist = (TH1F*) gROOT->FindObject("tracklessGenPhi");
	tracklessHltPhiHist->SetTitle("matched reco (black) and gen (red) trackless electron #phi");
	tracklessHltPhiHist->GetXaxis()->SetTitle("#phi");
	char tempTracklessPhi[130];
	sprintf(tempTracklessPhi,"Events / %.2f ", tracklessHltPhiHist->GetXaxis()->GetBinWidth(1));
	tracklessHltPhiHist->GetYaxis()->SetTitle(tempTracklessPhi);
	tracklessHltPhiHist->SetLineColor(1);	//black
	tracklessGenPhiHist->SetLineColor(2);	//red
	tracklessHltPhiHist->Draw();
	tracklessGenPhiHist->Draw("same");
	c302->SaveAs("trackless_gen_and_matched_reco_phi.png","recreate");
	
	TCanvas * c303 = new TCanvas("c303","c303",500,500);
	c303->cd();
	tracklessChain->Draw("diObjectMassHltEle>>tracklessHltDiObjectMass(150,-2.,140.)");
	tracklessChain->Draw("diObjectMassGenEle>>tracklessGenDiObjectMass(150,-2.,140.)");
	TH1F * tracklessHltDiObjectMassHist = (TH1F*) gROOT->FindObject("tracklessHltDiObjectMass");
	TH1F * tracklessGenDiObjectMassHist = (TH1F*) gROOT->FindObject("tracklessGenDiObjectMass");
	tracklessHltDiObjectMassHist->SetTitle("parent mass of matched reco (black) and gen (red) trackless electron");
	tracklessHltDiObjectMassHist->GetXaxis()->SetTitle("diObjectMass (GeV)");
	tracklessHltDiObjectMassHist->SetMaximum((1.1)*(tracklessGenDiObjectMassHist->GetBinContent(tracklessGenDiObjectMassHist->GetMaximumBin() )) );
	char tempTracklessDiObjectMass[130];
	sprintf(tempTracklessDiObjectMass,"Events / %.2f GeV ", tracklessHltDiObjectMassHist->GetXaxis()->GetBinWidth(1));
	tracklessHltDiObjectMassHist->GetYaxis()->SetTitle(tempTracklessDiObjectMass);
	tracklessHltDiObjectMassHist->SetLineColor(1);	//black
	tracklessGenDiObjectMassHist->SetLineColor(2);	//red
	tracklessHltDiObjectMassHist->Draw();
	tracklessGenDiObjectMassHist->Draw("same");
	c303->SaveAs("parent_inv_mass_of_trackless_gen_and_matched_reco_electrons.png","recreate");


}//end matchedRecoToGenOverlayHisto()

//use this fxn to compare distributions of pt,eta,phi,diobject mass from
//reco signal objects and gen signal objects 
//OR to compare other variable distributions where different cuts are applied
//to the two TChains
//this function is essentially two copies of makeAndSaveHistoUsingEntryList()
//two TChains, two listFillArgs, two list names, two histPlotArgs, two histNames, one histTitle,
//one xAxisTitle, one canvName, two TCut objects, one outputFile, and two Bool_t args are given
//to this fxn as inputs
void makeAndSaveOverlayHistoUsingEntryListsDiffCuts(TChain * sigChain,TChain * bkgndChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString sigHistPlotArg,TString bkgndHistPlotArg,TString sigHistName,TString bkgndHistName,TString histTitle,TString xAxisTitle,TString canvName,TCut sigFilters,TCut bkgndFilters,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t doScaling){
	sigChain->Draw(sigListFillArgs,sigFilters,"entrylistarray");
	sigChain->SetEntryList((TEntryListArray*) gROOT->FindObject(sigListName) );
	bkgndChain->Draw(bkgndListFillArgs,bkgndFilters,"entrylistarray");
	bkgndChain->SetEntryList((TEntryListArray*) gROOT->FindObject(bkgndListName) );

	TCanvas * canv = new TCanvas(canvName,canvName,700,700);
	canv->cd();
	sigChain->Draw(sigHistPlotArg);
	TH1F * sigHist = (TH1F*) gROOT->FindObject(sigHistName);
	bkgndChain->Draw(bkgndHistPlotArg);
	TH1F * bkgndHist = (TH1F*) gROOT->FindObject(bkgndHistName);

	//now normalize the two histos based on their integrals using Scale(1/(integral of original histo))
	if(doScaling){
		Double_t sigIntegral = sigHist->Integral();
		sigHist->Scale(1/sigIntegral);
		Double_t bkgndIntegral = bkgndHist->Integral();
		bkgndHist->Scale(1/bkgndIntegral);
	}
	sigHist->SetLineColor(1);	//black
	bkgndHist->SetLineColor(2);	//red

	//sigHist will be drawn first, bkgndHist overlaid on top.  If the largest bin in bkgndHist > the largest bin in sigHist,
	//then increase the y axis max on sigHist to accommodate the peak in bkgndHist
	if(sigHist->GetBinContent(sigHist->GetMaximumBin()) < bkgndHist->GetBinContent(bkgndHist->GetMaximumBin()) ){
		sigHist->SetMaximum((1.1)*( bkgndHist->GetBinContent(bkgndHist->GetMaximumBin()) ) );
	}
	TString titleAddendum;
	if(doScaling) titleAddendum = "  black=signal  red=bkgnd  areas normalized to 1";
	else titleAddendum = "";
	TString completeTitle = histTitle + titleAddendum;
	sigHist->SetTitle(completeTitle);
	//if isPlottingEnergy or isPlottingInverseEnergy is true, then append units to the x axis label
	TString enrg = " (GeV)";
	TString invEnrg = " (1/GeV)";
	TString completeXaxisTitle;
	if(isPlottingEnergy) completeXaxisTitle = xAxisTitle+enrg;
	if(isPlottingInverseEnergy) completeXaxisTitle = xAxisTitle+invEnrg;
	if(!isPlottingEnergy && !isPlottingInverseEnergy) completeXaxisTitle = xAxisTitle;
	sigHist->GetXaxis()->SetTitle(completeXaxisTitle);
	if(histTitle.Contains("Iso") ){
		canv->SetLogy(1);
		sigHist->SetMinimum(1);
	}
	char temp[130];
	if(isPlottingInverseEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f / GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if(isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f / GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.001){
		sprintf(temp,"Events / %.4f / GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	std::cout<<"sigHist has "<< sigHist->GetEntries() <<" entries"<<std::endl;
	std::cout<<"bkgndHist has "<< bkgndHist->GetEntries() <<" entries"<<std::endl;
	sigHist->GetYaxis()->SetTitle(temp);
	sigHist->Draw();
	bkgndHist->Draw("same");
	canv->SaveAs(outputFile,"recreate");
	
}//end makeAndSaveOverlayHistoUsingEntryListsDiffCuts()



//use this fxn to compare distributions of pt, ecal iso, H/E, etc from
//matched reco signal objects and reco bkgnd objects 
//this function is essentially two copies of makeAndSaveHistoUsingEntryList()
//two TChains, two listFillArgs, two list names, two histPlotArgs, two histNames, one histTitle,
//one xAxisTitle, one canvName, on TCut object, one outputFile, and two Bool_t args are given
//to this fxn as inputs
void makeAndSaveOverlayHistoUsingEntryLists(TChain * sigChain,TChain * bkgndChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString sigHistPlotArg,TString bkgndHistPlotArg,TString sigHistName,TString bkgndHistName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy){
	sigChain->Draw(sigListFillArgs,filters,"entrylistarray");
	sigChain->SetEntryList((TEntryListArray*) gROOT->FindObject(sigListName) );
	bkgndChain->Draw(bkgndListFillArgs,filters,"entrylistarray");
	bkgndChain->SetEntryList((TEntryListArray*) gROOT->FindObject(bkgndListName) );

	TCanvas * canv = new TCanvas(canvName,canvName,700,700);
	canv->cd();
	sigChain->Draw(sigHistPlotArg);
	TH1F * sigHist = (TH1F*) gROOT->FindObject(sigHistName);
	bkgndChain->Draw(bkgndHistPlotArg);
	TH1F * bkgndHist = (TH1F*) gROOT->FindObject(bkgndHistName);

	//now normalize the two histos based on their integrals using Scale(1/(integral of original histo))
	Double_t sigIntegral = sigHist->Integral();
	sigHist->Scale(1/sigIntegral);
	Double_t bkgndIntegral = bkgndHist->Integral();
	bkgndHist->Scale(1/bkgndIntegral);
	sigHist->SetLineColor(1);	//black
	bkgndHist->SetLineColor(2);	//red

	//sigHist will be drawn first, bkgndHist overlaid on top.  If the largest bin in bkgndHist > the largest bin in sigHist,
	//then increase the y axis max on sigHist to accommodate the peak in bkgndHist
	if(sigHist->GetBinContent(sigHist->GetMaximumBin()) < bkgndHist->GetBinContent(bkgndHist->GetMaximumBin()) ){
		sigHist->SetMaximum((1.1)*( bkgndHist->GetBinContent(bkgndHist->GetMaximumBin()) ) );
	}
	TString titleAddendum = "  black=signal  red=bkgnd  areas normalized to 1";
	TString completeTitle = histTitle + titleAddendum;
	sigHist->SetTitle(completeTitle);
	//if isPlottingEnergy or isPlottingInverseEnergy is true, then append units to the x axis label
	TString enrg = " (GeV)";
	TString invEnrg = " (1/GeV)";
	TString completeXaxisTitle;
	if(isPlottingEnergy) completeXaxisTitle = xAxisTitle+enrg;
	if(isPlottingInverseEnergy) completeXaxisTitle = xAxisTitle+invEnrg;
	if(!isPlottingEnergy && !isPlottingInverseEnergy) completeXaxisTitle = xAxisTitle;
	sigHist->GetXaxis()->SetTitle(completeXaxisTitle);
	if(histTitle.Contains("Iso") ){
		canv->SetLogy(1);
		sigHist->SetMinimum(1);
	}
	char temp[130];
	if(isPlottingInverseEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f / GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if(isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f / GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( isPlottingInverseEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.001){
		sprintf(temp,"Events / %.4f / GeV", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	sigHist->GetYaxis()->SetTitle(temp);
	sigHist->Draw();
	bkgndHist->Draw("same");
	canv->SaveAs(outputFile,"recreate");
	
}//end makeAndSaveOverlayHistoUsingEntryLists()


void makeAndSaveHistoUsingEntryList(TChain * chain,TString listFillArgs,TString listName,TString histPlotArgs,TString histName,TString histTitle,TString xAxisTitle,TString canvName,TCut filters,TString outputFile, Bool_t isPlottingEnergy, Bool_t isPlottingInverseEnergy){
	//fill the TEntryList named listName, and apply the filters when the list is made
	chain->Draw(listFillArgs,filters,"entrylistarray");
	//tell the chain to only use entries in the object named listName when calling TTree::Draw() in the future
	chain->SetEntryList((TEntryListArray*) gROOT->FindObject(listName) );
	
	//run the code in makeAndSaveSingleTreeHisto() to make comprehendible plots with useful labels and title 
	TCanvas * canv = new TCanvas(canvName,canvName,500,500);
	canv->cd();
	chain->Draw(histPlotArgs);
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

	//TChain * trackedBkgndChain = new TChain("recoAnalyzerTracked/recoTreeBeforeTriggerFiltersTrackedBkgnd","");
	//trackedBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_low_pt/low_pt_bkgnd_analyzer_trees_4*");
	//trackedBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_low_pt/low_pt_bkgnd_analyzer_trees_5*");
	//trackedBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_high_pt/high_pt_bkgnd_analyzer_trees_15*");
	//trackedBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_high_pt/high_pt_bkgnd_analyzer_trees_16*");
	
	//TChain * tracklessBkgndChain = new TChain("recoAnalyzerTrackless/recoTreeBeforeTriggerFiltersTracklessBkgnd","");
	//tracklessBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_low_pt/low_pt_bkgnd_analyzer_trees_4*");
	//tracklessBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_low_pt/low_pt_bkgnd_analyzer_trees_5*");
	//tracklessBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_high_pt/high_pt_bkgnd_analyzer_trees_15*");
	//tracklessBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/bkgnd_high_pt/high_pt_bkgnd_analyzer_trees_16*");



	//TChain * trackedSignalChain = new TChain("recoAnalyzerTracked/recoTreeBeforeTriggerFiltersTrackedSignal","");
	//trackedSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/signal/*");
	//
	TChain * tracklessSignalChain = new TChain("recoAnalyzerTrackless/recoTreeBeforeTriggerFiltersTracklessSignal","");
	tracklessSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/signal/*");
	
	//TChain * matchedTrackedSignalChain = new TChain("recoAnalyzerMatchedTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignal","");
	//matchedTrackedSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/signal/*");
	
	TChain * matchedTracklessSignalChain = new TChain("recoAnalyzerMatchedTrackless/recoTreeBeforeTriggerFiltersMatchedTracklessSignal","");
	matchedTracklessSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/signal/*");

	//TChain * genSignalChain = new TChain("genAnalyzerOne/genElectronsFromZ");
	//genSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_Febr27_withDiObjectMass/signal/*");

	//gen eta, pt, and dilepton mass cuts
	TCut trackedGenEta0 = "TMath::Abs(etaGenEle[0])<2.5";
	TCut trackedGenPt0 = "ptGenEle[0]>27";
	TCut trackedGenPtAndEta0 = trackedGenEta0 + trackedGenPt0;
	TCut trackedGenEta1 = "TMath::Abs(etaGenEle[1])<2.5";
	TCut trackedGenPt1 = "ptGenEle[1]>27";
	TCut trackedGenPtAndEta1 = trackedGenEta1 + trackedGenPt1;

	TCut tracklessGenEtaLow0 = "TMath::Abs(etaGenEle[0])>2.5";
	TCut tracklessGenEtaHigh0 = "TMath::Abs(etaGenEle[0])<3.0";
	TCut tracklessGenEtaLow1 = "TMath::Abs(etaGenEle[1])>2.5";
	TCut tracklessGenEtaHigh1 = "TMath::Abs(etaGenEle[1])<3.0";
	TCut tracklessGenPt0 = "ptGenEle[0]>15";
	TCut tracklessGenPt1 = "ptGenEle[1]>15";

	TCut tracklessGenPtAndEta0 = tracklessGenEtaLow0 + tracklessGenEtaHigh0 + tracklessGenPt0;
	TCut tracklessGenPtAndEta1 = tracklessGenEtaLow1 + tracklessGenEtaHigh1 + tracklessGenPt1;

	TCut dileptonGenMassLow = "invMassGen>60.";
	TCut dileptonGenMassHigh = "invMassGen<120.";
	TCut totalDileptonMass = dileptonGenMassLow + dileptonGenMassHigh;

	TCut allGenZeeCuts = totalDileptonMass && ( (trackedGenPtAndEta0 || trackedGenPtAndEta1) && (tracklessGenPtAndEta0 || tracklessGenPtAndEta1) );


	//hlt eta cuts
	TCut trackedEBHltEta = "TMath::Abs(etaHltEle)<1.479";
	TCut trackedEEHltLowEta = "TMath::Abs(etaHltEle)>1.479";
	TCut trackedEEHltHighEta = "TMath::Abs(etaHltEle)<2.5";
	TCut trackedEEHltEta = trackedEEHltLowEta + trackedEEHltHighEta;
	TCut tracklessEEHltLowEta = "TMath::Abs(etaHltEle)>2.5";
	TCut tracklessEEHltHighEta = "TMath::Abs(etaHltEle)<3.0";
	TCut tracklessEEHltEta = tracklessEEHltLowEta + tracklessEEHltHighEta;

	//hlt Et cuts
	TCut hltLowEt = "ptHltEle>10";
	TCut trackedLegHltEt = "ptHltEle>27";
	TCut tracklessLegHltEt = "ptHltEle>15";

	//combined hlt Et and eta cuts
	TCut trackedEBHltPtEta = trackedEBHltEta + trackedLegHltEt;
	TCut trackedEEHltPtEta = trackedEEHltEta + trackedLegHltEt;
	TCut tracklessEEHltPtEta = tracklessEEHltEta + tracklessLegHltEt;

	//hlt hcal and ecal iso cuts
	//use these cuts to study pt, eta, phi of reco objects with large negative values
	//of relative calorimeter isolation (less than -0.1 is unusual)
	TCut negativeHcalIso = "hcalIsoHltEle<-0.1";
	TCut negativeEcalIso = "ecalIsoHltEle<-0.1";
	TCut negativeCaloIso = (negativeHcalIso || negativeEcalIso);

	//gen and hlt dilepton mass cuts
	TCut genMllLow = "diObjectMassGenEle>60";
	TCut genMllHigh = "diObjectMassGenEle<120";
	TCut genMllRange = genMllLow+genMllHigh;
	TCut hltMllLow = "diObjectMassHltEle>60";
	TCut hltMllHigh = "diObjectMassHltEle<120";
	TCut hltMllRange = hltMllLow+hltMllHigh;
	TCut hltMllLowerBound = "diObjectMassHltEle>40";
	TCut hltMllAbsoluteLowerBound = "diObjectMassHltEle>1.";
	TCut hltMllTinyUpperBound = "diObjectMassHltEle<10";
	
	gStyle->SetOptStat(1111);

	//matchedRecoToGenOverlayHistos(matchedTrackedSignalChain,genMllRange+trackedEEHltHighEta, matchedTracklessSignalChain,genMllRange+tracklessEEHltEta);
	
	//use this to quickly change the ending of the title for all plots
	TString plotTitleModifier = " with reco parent mass>40 GeV ";


	//plots of matched signal distributions overlaid with bkgnd distributions.  Same TCuts applied to both.
	/*
	//tracked barrel distributions
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigptBarrelList","trackedSigptBarrelList",">>trackedBkgndptBarrelList","trackedBkgndptBarrelList","ptHltEle>>trackedSigptBarrel(100,0.,100.)","ptHltEle>>trackedBkgndptBarrel(100,0.,100.)","trackedSigptBarrel","trackedBkgndptBarrel","pt of tracked leg hlt objects in barrel"+plotTitleModifier,"pt","c1000",trackedEBHltEta+hltMllLowerBound,"pt_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",true,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigetaBarrelList","trackedSigetaBarrelList",">>trackedBkgndetaBarrelList","trackedBkgndetaBarrelList","etaHltEle>>trackedSigetaBarrel(100,-2.0,2.0)","etaHltEle>>trackedBkgndetaBarrel(100,-2.0,2.0)","trackedSigetaBarrel","trackedBkgndetaBarrel","eta of tracked leg hlt objects in barrel"+plotTitleModifier,"eta","c1001",trackedEBHltEta+hltMllLowerBound,"eta_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigphiBarrelList","trackedSigphiBarrelList",">>trackedBkgndphiBarrelList","trackedBkgndphiBarrelList","phiHltEle>>trackedSigphiBarrel(100,-3.5,3.5)","phiHltEle>>trackedBkgndphiBarrel(100,-3.5,3.5)","trackedSigphiBarrel","trackedBkgndphiBarrel","phi of tracked leg hlt objects in barrel"+plotTitleModifier,"phi","c1002",trackedEBHltEta+hltMllLowerBound,"phi_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigclusterShapeBarrelList","trackedSigclusterShapeBarrelList",">>trackedBkgndclusterShapeBarrelList","trackedBkgndclusterShapeBarrelList","clusterShapeHltEle>>trackedSigclusterShapeBarrel(100,0.,0.04)","clusterShapeHltEle>>trackedBkgndclusterShapeBarrel(100,0.,0.04)","trackedSigclusterShapeBarrel","trackedBkgndclusterShapeBarrel","#sigma_{i#etai#eta} of tracked leg hlt objects in barrel"+plotTitleModifier,"#sigma_{i#etai#eta}","c1003",trackedEBHltEta+hltMllLowerBound,"clusterShape_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighadEmBarrelList","trackedSighadEmBarrelList",">>trackedBkgndhadEmBarrelList","trackedBkgndhadEmBarrelList","hadEmHltEle>>trackedSighadEmBarrel(100,0.,0.3)","hadEmHltEle>>trackedBkgndhadEmBarrel(100,0.,0.3)","trackedSighadEmBarrel","trackedBkgndhadEmBarrel","relative had/Em of tracked leg hlt objects in barrel"+plotTitleModifier,"had/Em/Energy","c1004",trackedEBHltEta+hltMllLowerBound,"hadEm_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigecalIsoBarrelList","trackedSigecalIsoBarrelList",">>trackedBkgndecalIsoBarrelList","trackedBkgndecalIsoBarrelList","ecalIsoHltEle>>trackedSigecalIsoBarrel(100,-0.1,1.5)","ecalIsoHltEle>>trackedBkgndecalIsoBarrel(100,-0.1,1.5)","trackedSigecalIsoBarrel","trackedBkgndecalIsoBarrel","relative ecalIso of tracked leg hlt objects in barrel"+plotTitleModifier,"ecalIso/pt","c1005",trackedEBHltEta+hltMllLowerBound,"ecalIso_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighcalIsoBarrelList","trackedSighcalIsoBarrelList",">>trackedBkgndhcalIsoBarrelList","trackedBkgndhcalIsoBarrelList","hcalIsoHltEle>>trackedSighcalIsoBarrel(100,0.,1.)","hcalIsoHltEle>>trackedBkgndhcalIsoBarrel(100,0.,1.)","trackedSighcalIsoBarrel","trackedBkgndhcalIsoBarrel","relative hcalIso of tracked leg hlt objects in barrel"+plotTitleModifier,"hcalIso/pt","c1006",trackedEBHltEta+hltMllLowerBound,"hcalIso_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigepBarrelList","trackedSigepBarrelList",">>trackedBkgndepBarrelList","trackedBkgndepBarrelList","epHltEle>>trackedSigepBarrel(100,0.,0.27)","epHltEle>>trackedBkgndepBarrel(100,0.,0.27)","trackedSigepBarrel","trackedBkgndepBarrel","(1/E)-(1/P) of tracked leg hlt objects in barrel"+plotTitleModifier,"ep","c1010",trackedEBHltEta+hltMllLowerBound,"ep_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdEtaBarrelList","trackedSigdEtaBarrelList",">>trackedBkgnddEtaBarrelList","trackedBkgnddEtaBarrelList","dEtaHltEle>>trackedSigdEtaBarrel(100,0.,0.027)","dEtaHltEle>>trackedBkgnddEtaBarrel(100,0.,0.027)","trackedSigdEtaBarrel","trackedBkgnddEtaBarrel","#Delta #eta of tracked leg hlt objects in barrel"+plotTitleModifier,"#Delta #eta","c1007",trackedEBHltEta+hltMllLowerBound,"dEta_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdPhiBarrelList","trackedSigdPhiBarrelList",">>trackedBkgnddPhiBarrelList","trackedBkgnddPhiBarrelList","dPhiHltEle>>trackedSigdPhiBarrel(100,0.,0.17)","dPhiHltEle>>trackedBkgnddPhiBarrel(100,0.,0.17)","trackedSigdPhiBarrel","trackedBkgnddPhiBarrel","#Delta #phi of tracked leg hlt objects in barrel"+plotTitleModifier,"#Delta #phi","c1008",trackedEBHltEta+hltMllLowerBound,"dPhi_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigtrackIsoBarrelList","trackedSigtrackIsoBarrelList",">>trackedBkgndtrackIsoBarrelList","trackedBkgndtrackIsoBarrelList","trackIsoHltEle>>trackedSigtrackIsoBarrel(100,0.,0.5)","trackIsoHltEle>>trackedBkgndtrackIsoBarrel(100,0.,0.5)","trackedSigtrackIsoBarrel","trackedBkgndtrackIsoBarrel","relative trackIso of tracked leg hlt objects in barrel"+plotTitleModifier,"trackIso/pt","c1009",trackedEBHltEta+hltMllLowerBound,"trackIso_for_tracked_barrel_hlt_objs_signal_and_bkgnd.png",false,true);
	*/	

	/*
	//tracked endcap distributions
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigptEndcapList","trackedSigptEndcapList",">>trackedBkgndptEndcapList","trackedBkgndptEndcapList","ptHltEle>>trackedSigptEndcap(100,0.,100.)","ptHltEle>>trackedBkgndptEndcap(100,0.,100.)","trackedSigptEndcap","trackedBkgndptEndcap","pt of tracked leg hlt objects in endcap"+plotTitleModifier,"pt","c2000",trackedEEHltEta+hltMllLowerBound,"pt_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",true,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigetaEndcapList","trackedSigetaEndcapList",">>trackedBkgndetaEndcapList","trackedBkgndetaEndcapList","etaHltEle>>trackedSigetaEndcap(100,-2.5,2.5)","etaHltEle>>trackedBkgndetaEndcap(100,-2.5,2.5)","trackedSigetaEndcap","trackedBkgndetaEndcap","eta of tracked leg hlt objects in endcap"+plotTitleModifier,"eta","c2001",trackedEEHltEta+hltMllLowerBound,"eta_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigphiEndcapList","trackedSigphiEndcapList",">>trackedBkgndphiEndcapList","trackedBkgndphiEndcapList","phiHltEle>>trackedSigphiEndcap(100,-3.5,3.5)","phiHltEle>>trackedBkgndphiEndcap(100,-3.5,3.5)","trackedSigphiEndcap","trackedBkgndphiEndcap","phi of tracked leg hlt objects in endcap"+plotTitleModifier,"phi","c2002",trackedEEHltEta+hltMllLowerBound,"phi_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigclusterShapeEndcapList","trackedSigclusterShapeEndcapList",">>trackedBkgndclusterShapeEndcapList","trackedBkgndclusterShapeEndcapList","clusterShapeHltEle>>trackedSigclusterShapeEndcap(100,0.,0.08)","clusterShapeHltEle>>trackedBkgndclusterShapeEndcap(100,0.,0.08)","trackedSigclusterShapeEndcap","trackedBkgndclusterShapeEndcap","#sigma_{i#etai#eta} of tracked leg hlt objects in endcap"+plotTitleModifier,"#sigma_{i#etai#eta}","c2003",trackedEEHltEta+hltMllLowerBound,"clusterShape_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighadEmEndcapList","trackedSighadEmEndcapList",">>trackedBkgndhadEmEndcapList","trackedBkgndhadEmEndcapList","hadEmHltEle>>trackedSighadEmEndcap(100,0.,0.7)","hadEmHltEle>>trackedBkgndhadEmEndcap(100,0.,0.7)","trackedSighadEmEndcap","trackedBkgndhadEmEndcap","relative had/Em of tracked leg hlt objects in endcap"+plotTitleModifier,"had/Em/Energy","c2004",trackedEEHltEta+hltMllLowerBound,"hadEm_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigecalIsoEndcapList","trackedSigecalIsoEndcapList",">>trackedBkgndecalIsoEndcapList","trackedBkgndecalIsoEndcapList","ecalIsoHltEle>>trackedSigecalIsoEndcap(100,-0.2,3.)","ecalIsoHltEle>>trackedBkgndecalIsoEndcap(100,-0.2,3.)","trackedSigecalIsoEndcap","trackedBkgndecalIsoEndcap","relative ecalIso of tracked leg hlt objects in endcap"+plotTitleModifier,"ecalIso/pt","c2005",trackedEEHltEta+hltMllLowerBound,"ecalIso_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighcalIsoEndcapList","trackedSighcalIsoEndcapList",">>trackedBkgndhcalIsoEndcapList","trackedBkgndhcalIsoEndcapList","hcalIsoHltEle>>trackedSighcalIsoEndcap(100,-0.2,2.5)","hcalIsoHltEle>>trackedBkgndhcalIsoEndcap(100,-0.2,2.5)","trackedSighcalIsoEndcap","trackedBkgndhcalIsoEndcap","relative hcalIso of tracked leg hlt objects in endcap"+plotTitleModifier,"hcalIso/pt","c2006",trackedEEHltEta+hltMllLowerBound,"hcalIso_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigepEndcapList","trackedSigepEndcapList",">>trackedBkgndepEndcapList","trackedBkgndepEndcapList","epHltEle>>trackedSigepEndcap(100,0.,0.27)","epHltEle>>trackedBkgndepEndcap(100,0.,0.27)","trackedSigepEndcap","trackedBkgndepEndcap","(1/E)-(1/P) of tracked leg hlt objects in endcap"+plotTitleModifier,"ep","c2010",trackedEEHltEta+hltMllLowerBound,"ep_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdEtaEndcapList","trackedSigdEtaEndcapList",">>trackedBkgnddEtaEndcapList","trackedBkgnddEtaEndcapList","dEtaHltEle>>trackedSigdEtaEndcap(100,0.,0.027)","dEtaHltEle>>trackedBkgnddEtaEndcap(100,0.,0.027)","trackedSigdEtaEndcap","trackedBkgnddEtaEndcap","#Delta #eta of tracked leg hlt objects in endcap"+plotTitleModifier,"#Delta #eta","c2007",trackedEEHltEta+hltMllLowerBound,"dEta_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdPhiEndcapList","trackedSigdPhiEndcapList",">>trackedBkgnddPhiEndcapList","trackedBkgnddPhiEndcapList","dPhiHltEle>>trackedSigdPhiEndcap(100,0.,0.17)","dPhiHltEle>>trackedBkgnddPhiEndcap(100,0.,0.17)","trackedSigdPhiEndcap","trackedBkgnddPhiEndcap","#Delta #phi of tracked leg hlt objects in endcap"+plotTitleModifier,"#Delta #phi","c2008",trackedEEHltEta+hltMllLowerBound,"dPhi_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigtrackIsoEndcapList","trackedSigtrackIsoEndcapList",">>trackedBkgndtrackIsoEndcapList","trackedBkgndtrackIsoEndcapList","trackIsoHltEle>>trackedSigtrackIsoEndcap(100,0.,0.5)","trackIsoHltEle>>trackedBkgndtrackIsoEndcap(100,0.,0.5)","trackedSigtrackIsoEndcap","trackedBkgndtrackIsoEndcap","relative trackIso of tracked leg hlt objects in endcap"+plotTitleModifier,"trackIso/pt","c2009",trackedEEHltEta+hltMllLowerBound,"trackIso_for_tracked_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	*/

	/*
	//trackless endcap distributions
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigptEndcapList","tracklessSigptEndcapList",">>tracklessBkgndptEndcapList","tracklessBkgndptEndcapList","ptHltEle>>tracklessSigptEndcap(100,0.,100.)","ptHltEle>>tracklessBkgndptEndcap(100,0.,100.)","tracklessSigptEndcap","tracklessBkgndptEndcap","pt of trackless leg hlt objects in endcap"+plotTitleModifier,"pt","c3000",tracklessEEHltEta+hltMllLowerBound,"pt_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",true,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigetaEndcapList","tracklessSigetaEndcapList",">>tracklessBkgndetaEndcapList","tracklessBkgndetaEndcapList","etaHltEle>>tracklessSigetaEndcap(100,-3.1,3.1)","etaHltEle>>tracklessBkgndetaEndcap(100,-3.1,3.1)","tracklessSigetaEndcap","tracklessBkgndetaEndcap","eta of trackless leg hlt objects in endcap"+plotTitleModifier,"eta","c3001",tracklessEEHltEta+hltMllLowerBound,"eta_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigphiEndcapList","tracklessSigphiEndcapList",">>tracklessBkgndphiEndcapList","tracklessBkgndphiEndcapList","phiHltEle>>tracklessSigphiEndcap(100,-3.5,3.5)","phiHltEle>>tracklessBkgndphiEndcap(100,-3.5,3.5)","tracklessSigphiEndcap","tracklessBkgndphiEndcap","phi of trackless leg hlt objects in endcap"+plotTitleModifier,"phi","c3002",tracklessEEHltEta+hltMllLowerBound,"phi_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigclusterShapeEndcapList","tracklessSigclusterShapeEndcapList",">>tracklessBkgndclusterShapeEndcapList","tracklessBkgndclusterShapeEndcapList","clusterShapeHltEle>>tracklessSigclusterShapeEndcap(100,0.,0.08)","clusterShapeHltEle>>tracklessBkgndclusterShapeEndcap(100,0.,0.08)","tracklessSigclusterShapeEndcap","tracklessBkgndclusterShapeEndcap","#sigma_{i#etai#eta} of trackless leg hlt objects in endcap"+plotTitleModifier,"#sigma_{i#etai#eta}","c3003",tracklessEEHltEta+hltMllLowerBound,"clusterShape_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSighadEmEndcapList","tracklessSighadEmEndcapList",">>tracklessBkgndhadEmEndcapList","tracklessBkgndhadEmEndcapList","hadEmHltEle>>tracklessSighadEmEndcap(100,0.,2.)","hadEmHltEle>>tracklessBkgndhadEmEndcap(100,0.,2.)","tracklessSighadEmEndcap","tracklessBkgndhadEmEndcap","relative had/Em of trackless leg hlt objects in endcap"+plotTitleModifier,"had/Em/Energy","c3004",tracklessEEHltEta+hltMllLowerBound,"hadEm_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigecalIsoEndcapList","tracklessSigecalIsoEndcapList",">>tracklessBkgndecalIsoEndcapList","tracklessBkgndecalIsoEndcapList","ecalIsoHltEle>>tracklessSigecalIsoEndcap(100,-0.5,2.5)","ecalIsoHltEle>>tracklessBkgndecalIsoEndcap(100,-0.5,2.5)","tracklessSigecalIsoEndcap","tracklessBkgndecalIsoEndcap","relative ecalIso of trackless leg hlt objects in endcap"+plotTitleModifier,"ecalIso/pt","c3005",tracklessEEHltEta+hltMllLowerBound,"ecalIso_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSighcalIsoEndcapList","tracklessSighcalIsoEndcapList",">>tracklessBkgndhcalIsoEndcapList","tracklessBkgndhcalIsoEndcapList","hcalIsoHltEle>>tracklessSighcalIsoEndcap(100,-0.8,4.)","hcalIsoHltEle>>tracklessBkgndhcalIsoEndcap(100,-0.8,4.)","tracklessSighcalIsoEndcap","tracklessBkgndhcalIsoEndcap","relative hcalIso of trackless leg hlt objects in endcap"+plotTitleModifier,"hcalIso/pt","c3006",tracklessEEHltEta+hltMllLowerBound,"hcalIso_for_trackless_endcap_hlt_objs_signal_and_bkgnd.png",false,true);
	*/
	
	
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//BEGIN single plot fxn calls (no overlays of signal and bkgnd)
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	//diObject mass plots for matched signal and bkgnd (no splitting into barrel and endcap)
	//makeAndSaveHistoUsingEntryList(matchedTracklessSignalChain,">>tracklessdiObjectMassZeroList","tracklessdiObjectMassZeroList","diObjectMassHltEle>>tracklessdiObjectMassZero(100,0.,140.)","tracklessdiObjectMassZero","mass of parent signal particle whose daughters are matched to GEN electrons  mass>1 GeV","diObjectMass (GeV)","c150",tracklessEEHltEta+hltMllAbsoluteLowerBound,"parent_mass_of_matched_hlt_object_signal.png",true, false);
	//makeAndSaveHistoUsingEntryList(tracklessBkgndChain,">>tracklessdiObjectMassZeroListBkgnd","tracklessdiObjectMassZeroListBkgnd","diObjectMassHltEle>>tracklessdiObjectMassZeroBkgnd(100,0.,140.)","tracklessdiObjectMassZeroBkgnd","mass of parent bkgnd particle whose daughters were made by trigger  mass>1 GeV","diObjectMass (GeV)","c151",tracklessEEHltEta+hltMllAbsoluteLowerBound,"parent_mass_of_hlt_object_bkgnd.png",true, false);
	//makeAndSaveHistoUsingEntryList(matchedTracklessSignalChain,">>tracklessdiObjectMassZeroTinyList","tracklessdiObjectMassZeroTinyList","diObjectMassHltEle>>tracklessdiObjectMassZeroTiny(100,-2.,12.)","tracklessdiObjectMassZeroTiny","mass of parent signal particle whose daughters are matched to GEN electrons  mass<10 GeV","diObjectMass (GeV)","c152",tracklessEEHltEta+hltMllTinyUpperBound,"tiny_parent_mass_of_matched_hlt_object_signal.png",true, false);
	//makeAndSaveHistoUsingEntryList(tracklessBkgndChain,">>tracklessdiObjectMassZeroTinyListBkgnd","tracklessdiObjectMassZeroTinyListBkgnd","diObjectMassHltEle>>tracklessdiObjectMassZeroTinyBkgnd(100,-2.,12.)","tracklessdiObjectMassZeroTinyBkgnd","mass of parent bkgnd particle whose daughters were made by trigger  mass<10 GeV","diObjectMass (GeV)","c153",tracklessEEHltEta+hltMllTinyUpperBound,"tiny_parent_mass_of_hlt_object_bkgnd.png",true, false);
	
	////plot pt,eta,phi,and tracked leg cut variables of all RecoEcalCandidate objects which would normally be run through the tracked leg
	//makeAndSaveHistoUsingEntryList(hltObjectsTree,"evtNumber>>numEvtsBothRecoMatchingThree","numEvtsBothRecoMatchingThree","Evt numbers where tracked and trackless reco objects are matched to GEN","evt nums","c55",hasTracklessHlt+hasTrackedHlt,"num_evts_both_reco_objs_matching_three.png",false, false);
	//pt, eta, phi of GEN tracked electrons which pass all GEN Z->ee requirements
	/*
	makeAndSaveHistoUsingEntryList(matchedTrackedSignalChain,">>trackedptGenZeroList","trackedptGenZeroList","ptGenEle>>trackedptZeroGen(100,0.,100.)","trackedptZeroGen","P_{T} of tracked GEN electrons used for matching","pt (GeV)","c61","","tracked_gen_pt_for_matching.png",true, false);
	makeAndSaveHistoUsingEntryList(matchedTrackedSignalChain,">>trackedetaGenZeroList","trackedetaGenZeroList","etaGenEle>>trackedetaZeroGen(100,-3.0,3.0)","trackedetaZeroGen","#eta of tracked GEN electrons used for matching","#eta","c62","","tracked_gen_eta_for_matching.png",false, false);
	makeAndSaveHistoUsingEntryList(matchedTrackedSignalChain,">>trackedphiGenZeroList","trackedphiGenZeroList","phiGenEle>>trackedphiZeroGen(100,-4.0,4.0)","trackedphiZeroGen","#phi of tracked GEN electrons used for matching","#phi","c63","","tracked_gen_phi_for_matching.png",false, false);
	*/


	/*
	//barrel reco plots
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedptBarrelZeroList","trackedptBarrelZeroList","ptHltEle>>trackedptZeroBarrel(100,0.,100.)","trackedptZeroBarrel","P_{T} of tracked leg hlt objects in barrel"+plotTitleModifier,"pt (GeV)","c1",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_pt_ZeroBarrel.png",true, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedetaBarrelZeroList","trackedetaBarrelZeroList","etaHltEle>>trackedetaZeroBarrel(100,-3.0,3.0)","trackedetaZeroBarrel","#eta of tracked leg hlt objects in barrel"+plotTitleModifier,"#eta","c2",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_eta_ZeroBarrel.png",false, false);

	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedphiBarrelZeroList","trackedphiBarrelZeroList","phiHltEle>>trackedphiZeroBarrel(100,-4.0,4.0)","trackedphiZeroBarrel","#phi of tracked leg hlt objects in barrel"+plotTitleModifier,"#phi","c3",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_phi_ZeroBarrel.png",false, false);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedclusterShapeBarrelZeroList","trackedclusterShapeBarrelZeroList","clusterShapeHltEle>>trackedclusterShapeZeroBarrel(100,0.,0.14)","trackedclusterShapeZeroBarrel","#sigma i#eta i#eta of tracked leg hlt objects in barrel"+plotTitleModifier,"#sigma i#eta i#eta","c4",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_clusterShape_ZeroBarrel.png",false, false);

	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedhadEmBarrelZeroList","trackedhadEmBarrelZeroList","hadEmHltEle>>trackedhadEmZeroBarrel(100,0.,1.4)","trackedhadEmZeroBarrel","Had/Em/energy of tracked leg hlt objects in barrel"+plotTitleModifier,"Had/Em/Energy (1/GeV)","c5",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_hadEm_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedecalIsoBarrelZeroList","trackedecalIsoBarrelZeroList","ecalIsoHltEle>>trackedecalIsoZeroBarrel(100,-0.4,4.)","trackedecalIsoZeroBarrel","EcalIso/pt of tracked leg hlt objects in barrel"+plotTitleModifier,"EcalIso/pt (1/GeV)","c6",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_ecalIso_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedhcalIsoBarrelZeroList","trackedhcalIsoBarrelZeroList","hcalIsoHltEle>>trackedhcalIsoZeroBarrel(100,-0.4,3.5)","trackedhcalIsoZeroBarrel","HcalIso/pt of tracked leg hlt objects in barrel"+plotTitleModifier,"HcalIso/pt","c7",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_hcalIso_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedepBarrelZeroList","trackedepBarrelZeroList","epHltEle>>trackedepZeroBarrel(100,0.,0.5)","trackedepZeroBarrel","(1/E) - (1/P) of tracked leg hlt objects in barrel"+plotTitleModifier,"(1/E)-(1/P) (1/GeV)","c8",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_ep_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackeddEtaBarrelZeroList","trackeddEtaBarrelZeroList","dEtaHltEle>>trackeddEtaZeroBarrel(100,0.,0.07)","trackeddEtaZeroBarrel","#Delta #eta of tracked leg hlt objects in barrel"+plotTitleModifier,"#Delta #eta","c9",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_dEta_ZeroBarrel.png",false, false);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackeddPhiBarrelZeroList","trackeddPhiBarrelZeroList","dPhiHltEle>>trackeddPhiZeroBarrel(100,0.,0.4)","trackeddPhiZeroBarrel","#Delta #phi of tracked leg hlt objects in barrel"+plotTitleModifier,"#Delta #phi","c10",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_dPhi_ZeroBarrel.png",false, false);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedtrackIsoBarrelZeroList","trackedtrackIsoBarrelZeroList","trackIsoHltEle>>trackedtrackIsoZeroBarrel(100,0.,1.8)","trackedtrackIsoZeroBarrel","TrackIso/pt of tracked leg hlt objects in barrel"+plotTitleModifier,"TrackIso/pt (1/GeV)","c11",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_trackIso_ZeroBarrel.png",false, true);
	
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackeddiObjectMassBarrelZeroList","trackeddiObjectMassBarrelZeroList","diObjectMassHltEle>>trackeddiObjectMassZeroBarrel(100,30,140)","trackeddiObjectMassZeroBarrel","Parent particle mass of tracked leg hlt object in barrel","mass (GeV)","c100",diObjectMassRange+trackedEBHltEta,"tracked_barrel_hlt_object_diObjectMass_ZeroBarrel.png",true,false);


	*/

	/*
	//tracked objs in endcap before all filters
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedptEndcapZeroList","trackedptEndcapZeroList","ptHltEle>>trackedptZeroEndcap(100,0.,100.)","trackedptZeroEndcap","P_{T} of tracked leg hlt objects in endcap"+plotTitleModifier,"pt (GeV)","c31",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_pt_ZeroEndcap.png",true, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedetaEndcapZeroList","trackedetaEndcapZeroList","etaHltEle>>trackedetaZeroEndcap(100,-3.0,3.0)","trackedetaZeroEndcap","#eta of tracked leg hlt objects in endcap"+plotTitleModifier,"#eta","c32",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_eta_ZeroEndcap.png",false, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedphiEndcapZeroList","trackedphiEndcapZeroList","phiHltEle>>trackedphiZeroEndcap(100,-4.0,4.0)","trackedphiZeroEndcap","#phi of tracked leg hlt objects in endcap"+plotTitleModifier,"#phi","c33",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_phi_ZeroEndcap.png",false, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedclusterShapeEndcapZeroList","trackedclusterShapeEndcapZeroList","clusterShapeHltEle>>trackedclusterShapeZeroEndcap(100,0.,0.14)","trackedclusterShapeZeroEndcap","#sigma i#eta i#eta of tracked leg hlt objects in endcap"+plotTitleModifier,"#sigma i#eta i#eta","c34",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_clusterShape_ZeroEndcap.png",false, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedhadEmEndcapZeroList","trackedhadEmEndcapZeroList","hadEmHltEle>>trackedhadEmZeroEndcap(100,0.,1.4)","trackedhadEmZeroEndcap","Had/Em/energy of tracked leg hlt objects in endcap"+plotTitleModifier,"Had/Em/Energy (1/GeV)","c35",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_hadEm_ZeroEndcap.png",false, true);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedecalIsoEndcapZeroList","trackedecalIsoEndcapZeroList","ecalIsoHltEle>>trackedecalIsoZeroEndcap(100,-0.4,4.0)","trackedecalIsoZeroEndcap","EcalIso/pt of tracked leg hlt objects in endcap"+plotTitleModifier,"EcalIso/pt (1/GeV)","c36",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_ecalIso_ZeroEndcap.png",false, true);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedhcalIsoEndcapZeroList","trackedhcalIsoEndcapZeroList","hcalIsoHltEle>>trackedhcalIsoZeroEndcap(100,-0.4,3.5)","trackedhcalIsoZeroEndcap","HcalIso/pt of tracked leg hlt objects in endcap"+plotTitleModifier,"HcalIso/pt","c37",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_hcalIso_ZeroEndcap.png",false, true);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedepEndcapZeroList","trackedepEndcapZeroList","epHltEle>>trackedepZeroEndcap(100,0.,0.5)","trackedepZeroEndcap","(1/E) - (1/P) of tracked leg hlt objects in endcap"+plotTitleModifier,"(1/E)-(1/P) (1/GeV)","c38",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_ep_ZeroEndcap.png",false, true);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackeddEtaEndcapZeroList","trackeddEtaEndcapZeroList","dEtaHltEle>>trackeddEtaZeroEndcap(100,0.,0.07)","trackeddEtaZeroEndcap","#Delta #eta of tracked leg hlt objects in endcap"+plotTitleModifier,"#Delta #eta","c39",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_dEta_ZeroEndcap.png",false, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackeddPhiEndcapZeroList","trackeddPhiEndcapZeroList","dPhiHltEle>>trackeddPhiZeroEndcap(100,0.,0.4)","trackeddPhiZeroEndcap","#Delta #phi of tracked leg hlt objects in endcap"+plotTitleModifier,"#Delta #phi","c40",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_dPhi_ZeroEndcap.png",false, false);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackedtrackIsoEndcapZeroList","trackedtrackIsoEndcapZeroList","trackIsoHltEle>>trackedtrackIsoZeroEndcap(100,0.,1.8)","trackedtrackIsoZeroEndcap","TrackIso/pt of tracked leg hlt objects in endcap"+plotTitleModifier,"TrackIso/pt (1/GeV)","c41",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_trackIso_ZeroEndcap.png",false, true);
	makeAndSaveHistoUsingEntryList(trackedSignalChain,">>trackeddiObjectMassEndcapZeroList","trackeddiObjectMassEndcapZeroList","diObjectMassHltEle>>trackeddiObjectMassZeroEndcap(100,30,140)","trackeddiObjectMassZeroEndcap","Parent particle mass of tracked leg hlt objects in endcap","mass (GeV)","c101",diObjectMassRange+trackedEEHltEta,"tracked_endcap_hlt_object_diObjectMass_ZeroEndcap.png",true,false);

	*/
	
	/*
	//pt, eta, phi of GEN trackless electrons passing all GEN Z->ee requirements
	//makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessptGenZeroList","tracklessptGenZeroList","ptGenEle>>tracklessptZeroGen(100,0.,100.)","tracklessptZeroGen","P_{T} of trackless GEN electrons used for matching","pt (GeV)","c71","","trackless_gen_pt_for_matching.png",true, false);
	//makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessetaGenZeroList","tracklessetaGenZeroList","etaGenEle>>tracklessetaZeroGen(100,-3.0,3.0)","tracklessetaZeroGen","#eta of trackless GEN electrons used for matching","#eta","c72","","trackless_gen_eta_for_matching.png",false, false);
	//makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessphiGenZeroList","tracklessphiGenZeroList","phiGenEle>>tracklessphiZeroGen(100,-4.0,4.0)","tracklessphiZeroGen","#phi of trackless GEN electrons used for matching","#phi","c73","","trackless_gen_phi_for_matching.png",false, false);


	//plot eta,pt,phi, and trackless leg cut vars of all RecoEcalCandidate objects which would be run through the trackless leg
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessptZeroList","tracklessptZeroList","ptHltEle>>tracklessptZero(100,0.,60.)","tracklessptZero","P_{T} of trackless leg hlt objects"+plotTitleModifier,"pt (GeV)","c12",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_pt_Zero.png",true, false);
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessetaZeroList","tracklessetaZeroList","etaHltEle>>tracklessetaZero(100,-3.0,3.0)","tracklessetaZero","#eta of trackless leg hlt objects"+plotTitleModifier,"#eta","c13",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_eta_Zero.png",false, false);
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessphiZeroList","tracklessphiZeroList","phiHltEle>>tracklessphiZero(100,-4.0,4.0)","tracklessphiZero","#phi of trackless leg hlt objects"+plotTitleModifier,"#phi","c14",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_phi_Zero.png",false, false);
	
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessclusterShapeZeroList","tracklessclusterShapeZeroList","clusterShapeHltEle>>tracklessclusterShapeZero(100,0.,0.16)","tracklessclusterShapeZero","#sigma i#eta i#eta of trackless leg hlt objects"+plotTitleModifier,"#sigma i#eta i#eta","c15",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_clusterShape_Zero.png",false, false);
	
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessecalIsoZeroList","tracklessecalIsoZeroList","ecalIsoHltEle>>tracklessecalIsoZero(100,-0.9,4)","tracklessecalIsoZero","EcalIso/pt of trackless leg hlt objects"+plotTitleModifier,"EcalIso/pt (1/GeV)","c16",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_ecalIso_Zero.png",false, true);
	
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklesshadEmZeroList","tracklesshadEmZeroList","hadEmHltEle>>tracklesshadEmZero(100,0.,3)","tracklesshadEmZero","Had/Em/energy of trackless leg hlt objects"+plotTitleModifier,"Had/Em/energy","c17",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_hadEm_Zero.png",false, true);

	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklesshcalIsoZeroList","tracklesshcalIsoZeroList","hcalIsoHltEle>>tracklesshcalIsoZero(100,-1.0,7.0)","tracklesshcalIsoZero","HcalIso/pt of trackless leg hlt objects"+plotTitleModifier,"HcalIso/pt (1/GeV)","c18",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_hcalIso_Zero.png",false, true);
	
	makeAndSaveHistoUsingEntryList(tracklessSignalChain,">>tracklessdiObjectMassZeroList","tracklessdiObjectMassZeroList","diObjectMassHltEle>>tracklessdiObjectMassZero(100,30,140)","tracklessdiObjectMassZero","Parent particle mass of trackless leg hlt objects","mass (GeV)","c102",diObjectMassRange+tracklessEEHltEta,"trackless_hlt_object_diObjectMass_Zero.png",true,false);
	
	*/

	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	//something is messed up with the number of signal evts in which matching occurs
	//do the matching here starting with the bare signal and gen electron tuples
	//signal --> trackedSignalChain, tracklessSignalChain
	//gen --> matchedTrackedSignalChain, matchedTracklessSignalChain
	//many of the reco candidates which are being matched to GEN electrons have a parent diObject mass between 0. and 1.
	//this is messing up the plots when I require diObjectMassHltEle>1.
	//there are about 7600 events which pass all GEN Z->ee requirements.  There should be more than 4800 events where
	//two reasonable reco objects are matched to two GEN electrons in these 7600 evts!!

	//void makeAndSaveOverlayHistoUsingEntryListsDiffCuts(TChain * sigChain,TChain * bkgndChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString sigHistPlotArg,TString bkgndHistPlotArg,TString sigHistName,TString bkgndHistName,TString histTitle,TString xAxisTitle,TString canvName,TCut sigFilters,TCut bkgndFilters,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t doScaling)
	
	//use the matchedTracked or matchedTracklessSignalChain to access the pt, eta, phi, and diobject parent mass of the GEN electrons
	//which are used for matching
	makeAndSaveOverlayHistoUsingEntryListsDiffCuts(tracklessSignalChain,matchedTracklessSignalChain,">>tracklessdiObjectMassZeroSignalList","tracklessdiObjectMassZeroSignalList",">>tracklessdiObjectMassZeroGenList","tracklessdiObjectMassZeroGenList","diObjectMassHltEle>>tracklessdiObjectMassZeroSignal(150,-2.,140.)","diObjectMassGenEle>>tracklessdiObjectMassZeroGen(150,-2.,140.)","tracklessdiObjectMassZeroSignal","tracklessdiObjectMassZeroGen","Mass of parent particle for GEN and reco signal electrons","diObjectMass","c110",tracklessEEHltEta+hltMllAbsoluteLowerBound,"","parent_mass_gen_and_unmatched_reco_signal_eles.png",true,false,false);



}//end testMacro()


