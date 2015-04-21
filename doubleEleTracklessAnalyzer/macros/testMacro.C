#include <TFile.h>
#include <TLine.h>
#include <TPaveText.h>
#include <TLatex.h>
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
#include <algorithm>

//use this fxn to calculate total trigger rate and uncertainty
//given the number of signal and bkgnd evts which pass the trigger
std::vector<Float_t> calcTriggerRate(Float_t nSigEvts, TChain * sigChain, Float_t nLowPtBkgndEvts, TChain * lowPtBkgndChain, Float_t nHighPtBkgndEvts, TChain * highPtBkgndChain){
	Float_t peakLumi = (0.9)*(TMath::Power(10.,34));
	Float_t signalXSxn = (6960)*(TMath::Power(10.,-36));
	Float_t lowPtXSxn = (677300000*0.01029)*(TMath::Power(10.,-36));
	Float_t highPtXSxn = (185900000*0.06071)*(TMath::Power(10.,-36));

	Float_t sigRateErr=100, lowPtBkgndRateErr=100, highPtBkgndRateErr=100;
	Float_t sigRate = signalXSxn*peakLumi*nSigEvts/(sigChain->GetEntries());
	if(nSigEvts>0) sigRateErr = sigRate/(TMath::Sqrt(nSigEvts));
	Float_t lowPtBkgndRate = lowPtXSxn*peakLumi*nLowPtBkgndEvts/(lowPtBkgndChain->GetEntries());
	if(nLowPtBkgndEvts>0) lowPtBkgndRateErr = lowPtBkgndRate/(TMath::Sqrt(nLowPtBkgndEvts));
	Float_t highPtBkgndRate = highPtXSxn*peakLumi*nHighPtBkgndEvts/(highPtBkgndChain->GetEntries());
	if(nHighPtBkgndEvts>0) highPtBkgndRateErr = highPtBkgndRate/(TMath::Sqrt(nHighPtBkgndEvts));

	//trig rate uncertainty = trigger rate/sqrt(number of evts passing trigger)
	//sum signal and bkgnd rates in quadrature
	Float_t totRate = sigRate + lowPtBkgndRate + highPtBkgndRate;
	Float_t totRateErr = TMath::Sqrt( sigRateErr*sigRateErr + lowPtBkgndRateErr*lowPtBkgndRateErr + highPtBkgndRateErr*highPtBkgndRateErr );
	std::cout<<" "<<std::endl;
	std::cout<<"bkgnd rate = "<< lowPtBkgndRate+highPtBkgndRate << std::endl;
	std::cout<<"num bkgnd evts analyzed = "<< lowPtBkgndChain->GetEntries()+highPtBkgndChain->GetEntries() << std::cout;
	std::cout<<"sig rate = "<< sigRate << std::endl;
	std::cout<<"num sig evts analyzed = "<< sigChain->GetEntries() << std::endl;
	std::cout<<"total rate = "<< totRate << std::endl;
	std::cout<<"total rate error = "<< totRateErr << std::endl;
	std::cout<<" "<<std::endl;
	std::vector<Float_t> rateAndErr;
	rateAndErr.push_back(totRate);
	rateAndErr.push_back(totRateErr);
	return rateAndErr;
}

//use this fxn to find the number of evts from one particular physics process (signal: DY->ee, low pt bkgnd,
//high pt bkgnd) which pass both legs of the trigger with cuts applied to the tracked and trackless legs
//return the number of evts which passed both legs
Float_t numEvtsPassingBothLegs(TChain * tracklessChain,TChain * trackedChain,TString tracklessListFillArgs,TString tracklessListName,TString trackedListFillArgs,TString trackedListName,TCut tracklessFilters,TCut trackedFilters ){
	tracklessChain->Draw(tracklessListFillArgs,tracklessFilters,"entrylistarray");
	TEntryListArray * tracklessList = (TEntryListArray*) gROOT->Get(tracklessListName);
	tracklessChain->SetEntryList((TEntryListArray*) gROOT->FindObject(tracklessListName) );
	
	trackedChain->Draw(trackedListFillArgs,trackedFilters,"entrylistarray");
	TEntryListArray * trackedList = (TEntryListArray*) gROOT->Get(trackedListName);
	trackedChain->SetEntryList((TEntryListArray*) gROOT->FindObject(trackedListName) );

	Float_t numOverlappingEntries = 0;
	
	trackedChain->SetBranchStatus("*",0);
	trackedChain->SetBranchStatus("evtNumber",1);
	ULong64_t trackedEvtNum=-1;
	trackedChain->SetBranchAddress("evtNumber", &trackedEvtNum);
	Long64_t numFilteredtrackedEntries = trackedList->GetN();
	Long64_t trackedChainEntries = trackedChain->GetEntries();
	std::vector<ULong64_t> trackedEvtNumVec;

	tracklessChain->SetBranchStatus("*",0);
	tracklessChain->SetBranchStatus("evtNumber",1);
	ULong64_t tracklessEvtNum=-1;
	tracklessChain->SetBranchAddress("evtNumber", &tracklessEvtNum);
	Long64_t numFilteredtracklessEntries = tracklessList->GetN();
	Long64_t tracklessChainEntries = tracklessChain->GetEntries();
	std::vector<ULong64_t> tracklessEvtNumVec;

	std::cout<< trackedChainEntries << " evts in tracked chain"<<std::endl;
	std::cout<< numFilteredtrackedEntries << " evts in tracked chain pass filters"<<std::endl;
	std::cout<<"tracked leg efficiency = "<< numFilteredtrackedEntries/trackedChainEntries << std::endl;
	std::cout<< tracklessChainEntries << " evts in trackless chain"<<std::endl;
	std::cout<< numFilteredtracklessEntries << " evts in trackless chain pass filters"<<std::endl;
	std::cout<<"trackless leg efficiency = "<< numFilteredtracklessEntries/tracklessChainEntries << std::endl;

	Int_t treeNum=0;
	for(Long64_t oen = 0; oen < numFilteredtracklessEntries; oen++){
		if(oen==500) std::cout<<"finished 500 trackless evts"<<std::endl;
		Long64_t tracklessTreeEntry = tracklessList->GetEntryAndTree(oen,treeNum);
		Long64_t tracklessChainEntry = tracklessTreeEntry + tracklessChain->GetTreeOffset()[treeNum];
		tracklessChain->LoadTree(tracklessChainEntry);
		tracklessChain->GetEntry(tracklessTreeEntry);
		tracklessEvtNumVec.push_back(tracklessEvtNum);
	}//end loop over filtered trackless evts
	std::sort(tracklessEvtNumVec.begin(), tracklessEvtNumVec.end());	//sort tracklessEvt vector from low to high

	for(Long64_t oen = 0; oen < numFilteredtrackedEntries; oen++){
		if(oen==500) std::cout<<"finished 500 tracked evts"<<std::endl;
		Long64_t trackedTreeEntry = trackedList->GetEntryAndTree(oen,treeNum);
		Long64_t trackedChainEntry = trackedTreeEntry + trackedChain->GetTreeOffset()[treeNum];
		trackedChain->LoadTree(trackedChainEntry);
		trackedChain->GetEntry(trackedTreeEntry);
		trackedEvtNumVec.push_back(trackedEvtNum);
	}//end loop over filtered tracked evts
	std::sort(trackedEvtNumVec.begin(), trackedEvtNumVec.end());	//sort trackedEvt vector from low to high

	std::cout<<"finished sorting the two vectors of evt numbers"<<std::endl;

	if(tracklessEvtNumVec.size() < trackedEvtNumVec.size()){
		for(UInt_t i=0;i<tracklessEvtNumVec.size();i++){
			for(UInt_t j=0;j<trackedEvtNumVec.size();j++){
				if(trackedEvtNumVec[j] < tracklessEvtNumVec[i]) continue;
				if(trackedEvtNumVec[j] > tracklessEvtNumVec[i]) break;
				if(tracklessEvtNumVec[i]==trackedEvtNumVec[j]){
					numOverlappingEntries += 1;
					break;
				}
			}//end loop over filtered tracked evt numbers
		}//end loop over filtered trackless evt numbers
	}//fewer tracklessEvts than trackedEvts

	if(tracklessEvtNumVec.size() >= trackedEvtNumVec.size()){
		for(UInt_t i=0;i<trackedEvtNumVec.size();i++){
			for(UInt_t j=0;j<tracklessEvtNumVec.size();j++){
				if(tracklessEvtNumVec[j] < trackedEvtNumVec[i]) continue;
				if(tracklessEvtNumVec[j] > trackedEvtNumVec[i]) break;
				if(trackedEvtNumVec[i]==tracklessEvtNumVec[j]){
					numOverlappingEntries += 1;
					break;
				}
			}//end loop over filtered trackless evt numbers
		}//end loop over filtered tracked evt numbers
	}//fewer (or equal) trackedEvts than tracklessEvts
	
	std::cout<< numOverlappingEntries <<" evts passed both legs" << std::endl;
	return numOverlappingEntries;

}//end numEvtsPassingBothLegs()	

/**use this fxn to compare distributions from bkgnd and matched signal chains,
 * and show the ranges of cut values explored in the scan optimization, and
 * the ultimate value chosen for each variable.
 * eta filters need to be applied within this fxn, but no other filters are necessary
 */
void compareMatchedSigAndBkgnd(TChain * sigChain,TChain * bkgndVeryHighPtChain,TChain * bkgndHighPtChain,TChain * bkgndLowPtChain,TString sigFillArgs,TString sigListName,TString bkgndVHPtFillArgs,TString bkgndVHPtListName,TString bkgndHPtFillArgs,TString bkgndHPtListName,TString bkgndLPtFillArgs,TString bkgndLPtListName,TString sigHistPlotArg,TString bkgndVHPtHistPlotArg,TString bkgndHPtHistPlotArg,TString bkgndLPtHistPlotArg,TString sigHistName,TString bkgndVHPtHistName,TString bkgndHPtHistName,TString bkgndLPtHistName,Double_t highEffCutVal,Double_t lowEffCutVal,Double_t optimalCutVal,TString histTitle,TString xAxisTitle,TString canvName,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t isLowerBound,Bool_t doCrossSxnNormalization,TString etaRegion){
	if(!(etaRegion.Contains("trackless")) && !(etaRegion.Contains("trackedEE")) && !(etaRegion.Contains("EB")) ){
		std::cout<<"etaRegion is not formatted correctly!  Leaving fxn."<<std::endl;
		return;
	}
	TCut filters="";
	if(etaRegion.Contains("trackless")){
		filters="TMath::Abs(etaHltEle)>2.5 && TMath::Abs(etaHltEle)<3.0";
	}
	if(etaRegion.Contains("trackedEE")){
		filters="TMath::Abs(etaHltEle)<2.5 && TMath::Abs(etaHltEle)>1.479";
	}
	if(etaRegion.Contains("EB")){
		filters="TMath::Abs(etaHltEle)<1.479";
	}


	sigChain->Draw(sigFillArgs,filters,"entrylistarray");
	sigChain->SetEntryList((TEntryListArray*) gROOT->FindObject(sigListName));
	bkgndVeryHighPtChain->Draw(bkgndVHPtFillArgs,filters,"entrylistarray");
	bkgndVeryHighPtChain->SetEntryList((TEntryListArray*) gROOT->FindObject(bkgndVHPtListName));
	bkgndHighPtChain->Draw(bkgndHPtFillArgs,filters,"entrylistarray");
	bkgndHighPtChain->SetEntryList((TEntryListArray*) gROOT->FindObject(bkgndHPtListName));
	bkgndLowPtChain->Draw(bkgndLPtFillArgs,filters,"entrylistarray");
	bkgndLowPtChain->SetEntryList((TEntryListArray*) gROOT->FindObject(bkgndLPtListName));

	TCanvas * canv = new TCanvas(canvName,canvName,700,700);
	canv->cd();
	sigChain->Draw(sigHistPlotArg);
	TH1F * sigHist = (TH1F*) gROOT->FindObject(sigHistName);
	bkgndVeryHighPtChain->Draw(bkgndVHPtHistPlotArg);
	TH1F * bkgndVeryHighPtHist = (TH1F*) gROOT->FindObject(bkgndVHPtHistName);
	bkgndHighPtChain->Draw(bkgndHPtHistPlotArg);
	TH1F * bkgndHighPtHist = (TH1F*) gROOT->FindObject(bkgndHPtHistName);
	bkgndLowPtChain->Draw(bkgndLPtHistPlotArg);
	TH1F * bkgndLowPtHist = (TH1F*) gROOT->FindObject(bkgndLPtHistName);

	if(!doCrossSxnNormalization){
		bkgndHighPtHist->Add(bkgndLowPtHist);
		bkgndHighPtHist->Add(bkgndVeryHighPtHist);
		Double_t sigIntegral = sigHist->Integral();
		sigHist->Scale(1/sigIntegral);
		Double_t bkgndIntegral = bkgndHighPtHist->Integral();
		bkgndHighPtHist->Scale(1/bkgndIntegral);
	}//end if(!doCrossSxnNormalization)
	if(doCrossSxnNormalization){
		Double_t sigXSxn = (1500)*(TMath::Power(10.,-36));
		sigHist->Scale(sigXSxn/sigXSxn);
		Double_t bkgndLowPtXSxn = (677300000*0.01029)*(1e-36);
		Double_t bkgndHighPtXSxn = (185900000*0.06071)*(1e-36);
		Double_t bkgndVeryHighPtXSxn = (3.529*0.15443)*(1e-30);
		bkgndLowPtHist->Scale(bkgndLowPtXSxn/sigXSxn);
		bkgndHighPtHist->Scale(bkgndHighPtXSxn/sigXSxn);
		bkgndVeryHighPtHist->Scale(bkgndVeryHighPtXSxn/sigXSxn);
		bkgndHighPtHist->Add(bkgndLowPtHist);
		bkgndHighPtHist->Add(bkgndVeryHighPtHist);
	}//end if(doCrossSxnNormalization)
	std::cout<<"normalized histos"<<std::endl;
	sigHist->SetLineColor(1);	//black
	bkgndHighPtHist->SetLineColor(2);	//red

	///draw three TLine objects to represent the range of cut values scanned, and the optimal value chosen
	Double_t shift = 0.0001;
	TLine * highEffLine;
	TLine * lowEffLine;
	TLine * optimalCutLine;

	//sigHist will be drawn first, bkgndHighPtHist overlaid on top.  If the largest bin in bkgndHighPtHist > the largest bin in sigHist,
	//then increase the y axis max on sigHist to accommodate the peak in bkgndHighPtHist
	if(sigHist->GetBinContent(sigHist->GetMaximumBin()) < bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin())){
		std::cout<<"resetting sighist max, and setting length of cut lines"<<std::endl;
		sigHist->SetMaximum((1.1)*( bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()) ) );
		highEffLine = new TLine(highEffCutVal,0.001, highEffCutVal+shift, (1.0)*bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()));
		lowEffLine = new TLine(lowEffCutVal,0.001, lowEffCutVal+shift, (1.0)*bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()));
		optimalCutLine = new TLine(optimalCutVal,0.001, optimalCutVal+shift, (1.0)*bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()));
	}///end if(sigHist max < bkgndHist max)
	else{
		std::cout<<"sighist max is greater than bkgndHist max.  No need to rescale axes, just initialize TLine objects"<<std::endl;
		highEffLine = new TLine(highEffCutVal,0.001, highEffCutVal+shift, (1.0)*sigHist->GetBinContent(sigHist->GetMaximumBin()));
		lowEffLine = new TLine(lowEffCutVal,0.001, lowEffCutVal+shift, (1.0)*sigHist->GetBinContent(sigHist->GetMaximumBin()));
		optimalCutLine = new TLine(optimalCutVal,0.001, optimalCutVal+shift, (1.0)*sigHist->GetBinContent(sigHist->GetMaximumBin()));
	}
	
	std::cout<<"set length of cut lines"<<std::endl;

	highEffLine->SetLineColor(1);	///black
	lowEffLine->SetLineColor(1);
	optimalCutLine->SetLineColor(4);	///blue
	highEffLine->SetLineWidth(3);
	lowEffLine->SetLineWidth(3);
	optimalCutLine->SetLineWidth(3);
	std::cout<<"set color and width of cut lines"<<std::endl;
	
	TString titleAddendum = "  black=signal, red=bkgnd";
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
		//std::cout<<"setting y axis to log scale"<<std::endl;
		canv->SetLogy(1);
		//sigHist->SetMinimum(1);
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
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.001){
		sprintf(temp,"Events / %.4f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) <= 0.01){
		sprintf(temp,"Events / %.3f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	if( !isPlottingInverseEnergy && !isPlottingEnergy && sigHist->GetXaxis()->GetBinWidth(1) > 0.01){
		sprintf(temp,"Events / %.2f ", sigHist->GetXaxis()->GetBinWidth(1));
	}
	sigHist->GetYaxis()->SetTitle(temp);
	sigHist->Draw();
	bkgndHighPtHist->Draw("same");
	lowEffLine->Draw();
	highEffLine->Draw();
	optimalCutLine->Draw();
	canv->SaveAs(outputFile,"recreate");

}///end compareMatchedSigAndBkgnd()


//use this fxn to make a histogram of a kinematic or isolation variable for matched signal objects,
//and objects from bkgnd files.  The matched signal objects will be subject to a slightly different
//set of cuts than the objects from bkgnd events, but only because some deltaR filtering will be done
//to the signal objects acceptance and pt cuts are applied.  The acceptance and pt cuts applied to
//bkgnd objects will also be applied to matched signal objects.  Once the two histos are made this fxn
//will maximize:
// (integral of signal histo from lwr bound to cutVal) - (integral of bkgnd histo from lwr bound to cutVal)
//and return the value of the kinematic or isolation variable at which this minimization is achieved.
//This fxn finds the optimal cut value for one trigger filter variable without considering correlations btwn
//this trigger filter var and others.  Before returning the optimal cut value a histogram will be drawn
//showing the matched signal and bkgnd distributions after the cut is applied.  This histo will be saved to file.
//if doCrossSxnNormalization is false, then normalize the signal histo area and summed bkgnd histo area
//(lowpt + highpt) to 1
std::vector<Double_t> findOptimalCutMaxSigMinBkgnd(TChain * sigChain,TChain * bkgndHighPtChain,TChain * bkgndLowPtChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString lowPtBkgndListFillArgs,TString lowPtBkgndListName,TString sigHistPlotArg,TString bkgndHighPtHistPlotArg,TString bkgndLowPtHistPlotArg,TString sigHistName,TString bkgndHighPtHistName,TString bkgndLowPtHistName,Double_t histCritVal,TString histTitle,TString xAxisTitle,TString canvName,TCut sigFilters,TCut bkgndFilters,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t isLowerBound,Bool_t doCrossSxnNormalization,Double_t oldCutVal){
	sigChain->Draw(sigListFillArgs,sigFilters,"entrylistarray");
	sigChain->SetEntryList((TEntryListArray*) gROOT->FindObject(sigListName) );
	
	bkgndHighPtChain->Draw(bkgndListFillArgs,bkgndFilters,"entrylistarray");
	bkgndHighPtChain->SetEntryList((TEntryListArray*) gROOT->FindObject(bkgndListName) );

	bkgndLowPtChain->Draw(lowPtBkgndListFillArgs,bkgndFilters,"entrylistarray");
	bkgndLowPtChain->SetEntryList((TEntryListArray*) gROOT->FindObject(lowPtBkgndListName) );

	TCanvas * canv = new TCanvas(canvName,canvName,700,700);
	canv->cd();
	sigChain->Draw(sigHistPlotArg);
	TH1F * sigHist = (TH1F*) gROOT->FindObject(sigHistName);
	bkgndHighPtChain->Draw(bkgndHighPtHistPlotArg);
	TH1F * bkgndHighPtHist = (TH1F*) gROOT->FindObject(bkgndHighPtHistName);
	bkgndLowPtChain->Draw(bkgndLowPtHistPlotArg);
	TH1F * bkgndLowPtHist = (TH1F*) gROOT->FindObject(bkgndLowPtHistName);

	//std::cout<<"grabbed histos"<<std::endl;
	//the last element in cutVals is the value of the variable being plotted which maximizes
	//the integral difference shown immediately above
	std::vector<Double_t> bkgndSuppressionFrxn;
	std::vector<Double_t> sigEfficiencyFrxn;
	std::vector<Double_t> cutVals;
	std::vector<Int_t> maxBinVals;
	Double_t largestIntegralDiff=-1;	//placeholder variable, updated many times in subsequent loop
	for(Int_t i=2;i<sigHist->GetNbinsX();i++){
		//start at i=1 to avoid underflow bin
		if(!isLowerBound){
			//std::cout<<"isLowerBound is false"<<std::endl;
			Double_t integralDiff = ((sigHist->Integral(1,i)/sigHist->Integral()) - (bkgndHighPtHist->Integral(1,i)/bkgndHighPtHist->Integral()) - (bkgndLowPtHist->Integral(1,i)/bkgndLowPtHist->Integral()) );
			//std::cout<<"integralDiff = "<< integralDiff <<std::endl;
			if(integralDiff > largestIntegralDiff){
				//negative cut values should not be considered
				largestIntegralDiff = 0;
				largestIntegralDiff += integralDiff;
				maxBinVals.push_back(i);
				cutVals.push_back(sigHist->GetXaxis()->GetBinCenter(i));
				bkgndSuppressionFrxn.push_back( (bkgndHighPtHist->Integral(1,i)+bkgndLowPtHist->Integral(1,i))/(bkgndHighPtHist->Integral()+bkgndLowPtHist->Integral()) );
				sigEfficiencyFrxn.push_back( (sigHist->Integral(1,i)/sigHist->Integral()) );
			}
		}//end if(!isLowerBound)

		if(isLowerBound){
			Int_t lastBin = (sigHist->GetNbinsX()-1);
			Double_t integralDiff = ((sigHist->Integral(i,lastBin)/sigHist->Integral()) - (bkgndHighPtHist->Integral(i,lastBin)/bkgndHighPtHist->Integral()) - (bkgndLowPtHist->Integral(i,lastBin)/bkgndLowPtHist->Integral()) );
			if(sigHist->GetXaxis()->GetBinCenter(i) > 0. && integralDiff > largestIntegralDiff){
				//negative cut values should not be considered
				largestIntegralDiff = 0;
				largestIntegralDiff += integralDiff;
				maxBinVals.push_back(i);
				cutVals.push_back(sigHist->GetXaxis()->GetBinCenter(i));
				bkgndSuppressionFrxn.push_back( (bkgndHighPtHist->Integral(i,lastBin)+bkgndLowPtHist->Integral(i,lastBin))/(bkgndHighPtHist->Integral()+bkgndLowPtHist->Integral()) );
				sigEfficiencyFrxn.push_back( (sigHist->Integral(i,lastBin)/sigHist->Integral()) );
			}
		}//end if(isLowerBound)

	}//end loop over bins of signal and bkgnd histos (both have the same number of bins, min val, and max val)
	//std::cout<<"obtained optimal cut val"<<std::endl;
	if(cutVals.size() == 0 && !isLowerBound){
		//std::cout<<"didn't find any optimal cut value"<<std::endl;
		cutVals.push_back(0.07);
		//THIS BKGNDSUPPRESSION IS BAD FIX THIS
		bkgndSuppressionFrxn.push_back( 1/( (bkgndHighPtHist->Integral(1,bkgndHighPtHist->FindFirstBinAbove(0.07,1))/bkgndHighPtHist->Integral()) + (bkgndLowPtHist->Integral(1,bkgndLowPtHist->FindFirstBinAbove(0.07,1) )/bkgndLowPtHist->Integral()) )  );
		sigEfficiencyFrxn.push_back( (sigHist->Integral(1, sigHist->FindFirstBinAbove(0.07,1) )/sigHist->Integral()) );
	}
	if( cutVals[ (cutVals.size()-1) ] < 0. && histTitle.Contains("hcalIso") && histTitle.Contains("barrel") ){
		cutVals.push_back(0.1);
		Int_t maxBin = 0;
		for(Int_t r=0;r<100;r++){
			Double_t width = sigHist->GetBinWidth(1);
			Double_t lowVal = sigHist->GetBinLowEdge(1);
			if(r*width+lowVal >= 0.1){
				maxBin = r;
				break;
			}
		}//end loop
		bkgndSuppressionFrxn.push_back( ( (bkgndHighPtHist->Integral(1,maxBin)+bkgndLowPtHist->Integral(1,maxBin))/(bkgndHighPtHist->Integral()+bkgndLowPtHist->Integral()) )  );
		sigEfficiencyFrxn.push_back( (sigHist->Integral(1,maxBin)/sigHist->Integral()) );

	}
	//if(!isLowerBound) sigHist->SetAxisRange( histCritVal , cutVals[ (cutVals.size()-1) ] ,"X");
	//if(!isLowerBound) bkgndHist->SetAxisRange( histCritVal , cutVals[ (cutVals.size()-1) ] ,"X");
	//if(isLowerBound) sigHist->SetAxisRange( cutVals[ (cutVals.size()-1) ] , histCritVal,"X");
	//if(isLowerBound) bkgndHist->SetAxisRange( cutVals[ (cutVals.size()-1) ] , histCritVal,"X");


	//doCrossSxnNormalization
	//now normalize the two histos based on their integrals using Scale(1/(integral of original histo))
	//or by their cross sections
	if(!doCrossSxnNormalization){
		bkgndHighPtHist->Add(bkgndLowPtHist);
		Double_t sigIntegral = sigHist->Integral();
		sigHist->Scale(1/sigIntegral);
		Double_t bkgndIntegral = bkgndHighPtHist->Integral();
		bkgndHighPtHist->Scale(1/bkgndIntegral);
	}//end if(!doCrossSxnNormalization)
	if(doCrossSxnNormalization){
		Double_t sigXSxn = (6960)*(TMath::Power(10.,-36));
		sigHist->Scale(sigXSxn/sigXSxn);
		Double_t bkgndLowPtXSxn = (677300000*0.01029)*(TMath::Power(10.,-36));
		Double_t bkgndHighPtXSxn = (185900000*0.06071)*(TMath::Power(10.,-36));
		bkgndLowPtHist->Scale(bkgndLowPtXSxn/sigXSxn);
		bkgndHighPtHist->Scale(bkgndHighPtXSxn/sigXSxn);
		bkgndHighPtHist->Add(bkgndLowPtHist);
	}//end if(doCrossSxnNormalization)
	//std::cout<<"normalized histos"<<std::endl;
	sigHist->SetLineColor(1);	//black
	bkgndHighPtHist->SetLineColor(2);	//red

	//eventually draw two TLine objects to show the new optimized cut value, and the old cut value
	//which was used in 2012
	Double_t shift = 0.0005;
	//TLine * oldCutLine;
	//TLine * optimizedCutLine;

	//std::cout<<"optimized cut val = "<< cutVals[ (cutVals.size()-1) ] <<std::endl;
	//sigHist will be drawn first, bkgndHighPtHist overlaid on top.  If the largest bin in bkgndHighPtHist > the largest bin in sigHist,
	//then increase the y axis max on sigHist to accommodate the peak in bkgndHighPtHist
	Bool_t isTrackIso = histTitle.Contains("trackIso");
	if(sigHist->GetBinContent(sigHist->GetMaximumBin()) < bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()) && !isTrackIso){
		//std::cout<<"resetting sighist max, and setting length of cut lines"<<std::endl;
		sigHist->SetMaximum((1.1)*( bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()) ) );
		//oldCutLine = new TLine(oldCutVal,0.001, oldCutVal+shift, (1.07)*bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()));
		//optimizedCutLine = new TLine(cutVals[ (cutVals.size()-1) ],0.001, cutVals[ (cutVals.size()-1) ]+shift, (1.07)*bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()));
	}
	if(!isTrackIso && sigHist->GetBinContent(sigHist->GetMaximumBin()) < bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()) ){
		//std::cout<<"setting length of cut lines"<<std::endl;
		//oldCutLine = new TLine(oldCutVal,0.001, oldCutVal+shift, (1.07)*sigHist->GetBinContent(sigHist->GetMaximumBin()) );
		//optimizedCutLine = new TLine(cutVals[ (cutVals.size()-1) ],0.001, cutVals[ (cutVals.size()-1) ]+shift, (1.07)*sigHist->GetBinContent(sigHist->GetMaximumBin()));
	}
	/*
	if(sigHist->GetBinContent(sigHist->GetMaximumBin()) < bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()) && isTrackIso){
		std::cout<<"setting length of track iso cut lines AAA"<<std::endl;
		//sigHist->SetMaximum((1.1)*( bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()) ) );
		oldCutLine = new TLine(oldCutVal,0.001, oldCutVal+shift, );
		optimizedCutLine = new TLine(cutVals[ (cutVals.size()-1) ],0.001, cutVals[ (cutVals.size()-1) ]+shift, (1.07)*bkgndHighPtHist->GetBinContent(bkgndHighPtHist->GetMaximumBin()));
	}*/
	if(isTrackIso){
		//std::cout<<"setting length of track iso cut lines"<<std::endl;
		//oldCutLine = new TLine(oldCutVal,0.001, oldCutVal+shift, 0.5);
		//optimizedCutLine = new TLine(cutVals[ (cutVals.size()-1) ],0.001, cutVals[ (cutVals.size()-1) ]+shift, 0.5);
	}

	//std::cout<<"set length of cut lines"<<std::endl;

	//oldCutLine->SetLineColor(2);	//red
	//optimizedCutLine->SetLineColor(1);	//black
	//std::cout<<"set color of cut lines"<<std::endl;
	TString titleAddendum = "  black=signal, new optimized cut  red=bkgnd, 2012 cut";
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
		//std::cout<<"setting y axis to log scale"<<std::endl;
		canv->SetLogy(1);
		//sigHist->SetMinimum(1);
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
	//std::cout<<"sigHist has "<< sigHist->GetEntries() <<" entries"<<std::endl;
	//std::cout<<"bkgndHighPtHist has "<< bkgndHighPtHist->GetEntries() <<" entries"<<std::endl;
	sigHist->GetYaxis()->SetTitle(temp);
	char sigEff[130];
	char bkgndRej[130];
	char finalCutVal[130];
	sprintf(finalCutVal,"cut value = %.3f", cutVals[ (cutVals.size()-1) ]);
	sprintf(sigEff,"signal efficiency = %.3f", sigEfficiencyFrxn[sigEfficiencyFrxn.size()-1]);
	sprintf(bkgndRej,"bkgnd survival = %.3f", bkgndSuppressionFrxn[bkgndSuppressionFrxn.size()-1]);
	std::cout<<"filled char arrays"<<std::endl;
	TLatex * cutBox;
	TLatex * sigEffBox;
	TLatex * bkgndBox;
	if(!isLowerBound && histTitle.Contains("Iso") && cutVals[ (cutVals.size()-1) ] > 0.){
		cutBox = new TLatex((0.4)*cutVals[ (cutVals.size()-1) ] ,(0.01),finalCutVal);
		sigEffBox = new TLatex((0.4)*cutVals[ (cutVals.size()-1) ] ,(0.007),sigEff);
		bkgndBox = new TLatex((0.4)*cutVals[ (cutVals.size()-1) ] ,(0.004),bkgndRej);
	}
	if(!isLowerBound && histTitle.Contains("Iso") && cutVals[ (cutVals.size()-1) ] < 0.){
		cutBox = new TLatex((0.)*cutVals[ (cutVals.size()-1) ] ,(0.01),finalCutVal);
		sigEffBox = new TLatex((0.)*cutVals[ (cutVals.size()-1) ] ,(0.007),sigEff);
		bkgndBox = new TLatex((0.)*cutVals[ (cutVals.size()-1) ] ,(0.004),bkgndRej);
	}


	if(!isLowerBound && !(histTitle.Contains("Iso")) ){
		cutBox = new TLatex((0.5)*cutVals[ (cutVals.size()-1) ] ,(0.45)*(sigHist->GetMaximum()+sigHist->GetMinimum()),finalCutVal);
		sigEffBox = new TLatex((0.5)*cutVals[ (cutVals.size()-1) ] ,(0.37)*(sigHist->GetMaximum()+sigHist->GetMinimum()),sigEff);
		bkgndBox = new TLatex((0.5)*cutVals[ (cutVals.size()-1) ] ,(0.3)*(sigHist->GetMaximum()+sigHist->GetMinimum()),bkgndRej);
	}
	if(isLowerBound){
		cutBox = new TLatex((0.5)*histCritVal,(0.45)*(sigHist->GetMaximum()+sigHist->GetMinimum()),finalCutVal);
		sigEffBox = new TLatex((0.5)*histCritVal,(0.37)*(sigHist->GetMaximum()+sigHist->GetMinimum()),sigEff);
		bkgndBox = new TLatex((0.5)*histCritVal,(0.3)*(sigHist->GetMaximum()+sigHist->GetMinimum()),bkgndRej);
	}
	cutBox->SetTextSize(0.029);
	sigEffBox->SetTextSize(0.029);
	bkgndBox->SetTextSize(0.029);
	sigHist->Draw();
	bkgndHighPtHist->Draw("same");
	cutBox->Draw();
	sigEffBox->Draw();
	bkgndBox->Draw();
	//oldCutLine->Draw();
	//optimizedCutLine->Draw();
	canv->SaveAs(outputFile,"recreate");
	std::vector<Double_t> usefulCutInfo;
	usefulCutInfo.push_back( cutVals[ (cutVals.size()-1) ] );
	usefulCutInfo.push_back( sigEfficiencyFrxn[sigEfficiencyFrxn.size()-1] );
	usefulCutInfo.push_back( bkgndSuppressionFrxn[bkgndSuppressionFrxn.size()-1] );
	return usefulCutInfo;
	
}//end findOptimalCutMaxSigMinBkgnd()

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
Float_t makeAndSaveOverlayHistoUsingEntryListsDiffCuts(TChain * sigChain,TChain * bkgndChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString sigHistPlotArg,TString bkgndHistPlotArg,TString sigHistName,TString bkgndHistName,TString histTitle,TString xAxisTitle,TString canvName,TCut sigFilters,TCut bkgndFilters,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t doScaling,Bool_t doLogX){
	sigChain->Draw(sigListFillArgs,sigFilters,"entrylistarray");
	TEntryListArray * sigList = (TEntryListArray*) gROOT->Get(sigListName);
	sigChain->SetEntryList((TEntryListArray*) gROOT->FindObject(sigListName) );
	
	bkgndChain->Draw(bkgndListFillArgs,bkgndFilters,"entrylistarray");
	TEntryListArray * bkgndList = (TEntryListArray*) gROOT->Get(bkgndListName);
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
	if(doLogX){
		canv->SetLogx(1);
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
	std::cout<<" "<<std::endl;
	sigHist->GetYaxis()->SetTitle(temp);
	sigHist->Draw();
	bkgndHist->Draw("same");
	canv->SaveAs(outputFile,"recreate");
	Float_t numOverlappingEntries = 0;
	if(sigHistName.Contains("evtNumber")){
		//determine how many evts are present in both filtered chains (i.e. how many evts pass both legs)
		//here bkgnd and sig correspond to tracked and trackless legs for the same physics process (like DY->ee)
		bkgndChain->SetBranchStatus("*",0);
		bkgndChain->SetBranchStatus("evtNumber",1);
		ULong64_t bkgndEvtNum=-1;
		bkgndChain->SetBranchAddress("evtNumber", &bkgndEvtNum);
		Long64_t numFilteredbkgndEntries = bkgndList->GetN();
		Long64_t bkgndChainEntries = bkgndChain->GetEntries();
		std::vector<ULong64_t> bkgndEvtNumVec;
	
		sigChain->SetBranchStatus("*",0);
		sigChain->SetBranchStatus("evtNumber",1);
		ULong64_t sigEvtNum=-1;
		sigChain->SetBranchAddress("evtNumber", &sigEvtNum);
		Long64_t numFilteredsigEntries = sigList->GetN();
		Long64_t sigChainEntries = sigChain->GetEntries();
		std::vector<ULong64_t> sigEvtNumVec;
	
		std::cout<< bkgndChainEntries << " evts in bkgnd chain"<<std::endl;
		std::cout<< numFilteredbkgndEntries << " evts in bkgnd chain pass filters"<<std::endl;
		std::cout<< sigChainEntries << " evts in sig chain"<<std::endl;
		std::cout<< numFilteredsigEntries << " evts in sig chain pass filters"<<std::endl;

		Int_t treeNum=0;
		for(Long64_t oen = 0; oen < numFilteredsigEntries; oen++){
			if(oen==500) std::cout<<"finished exploring 500 evts"<<std::endl;
			Long64_t sigTreeEntry = sigList->GetEntryAndTree(oen,treeNum);
			Long64_t sigChainEntry = sigTreeEntry + sigChain->GetTreeOffset()[treeNum];
			sigChain->LoadTree(sigChainEntry);
			sigChain->GetEntry(sigTreeEntry);
			sigEvtNumVec.push_back(sigEvtNum);
		}//end loop over filtered sig evts
		std::sort(sigEvtNumVec.begin(), sigEvtNumVec.end());	//sort sigEvt vector from low to high

		for(Long64_t oen = 0; oen < numFilteredbkgndEntries; oen++){
			if(oen==500) std::cout<<"finished exploring 500 evts"<<std::endl;
			Long64_t bkgndTreeEntry = bkgndList->GetEntryAndTree(oen,treeNum);
			Long64_t bkgndChainEntry = bkgndTreeEntry + bkgndChain->GetTreeOffset()[treeNum];
			bkgndChain->LoadTree(bkgndChainEntry);
			bkgndChain->GetEntry(bkgndTreeEntry);
			bkgndEvtNumVec.push_back(bkgndEvtNum);
		}//end loop over filtered bkgnd evts
		std::sort(bkgndEvtNumVec.begin(), bkgndEvtNumVec.end());	//sort bkgndEvt vector from low to high

		std::cout<<"finished sorting the two vectors of evt numbers"<<std::endl;

		if(sigEvtNumVec.size() < bkgndEvtNumVec.size()){
			for(UInt_t i=0;i<sigEvtNumVec.size();i++){
				for(UInt_t j=0;j<bkgndEvtNumVec.size();j++){
					if(bkgndEvtNumVec[j] < sigEvtNumVec[i]) continue;
					if(bkgndEvtNumVec[j] > sigEvtNumVec[i]) break;
					if(sigEvtNumVec[i]==bkgndEvtNumVec[j]){
						numOverlappingEntries += 1;
						//std::cout<<"found an event which passes both legs"<<std::endl;
						break;
					}

				}//end loop over filtered bkgnd evt numbers
			}//end loop over filtered sig evt numbers
		}//fewer sigEvts than bkgndEvts
		
		if(sigEvtNumVec.size() >= bkgndEvtNumVec.size()){
			for(UInt_t i=0;i<bkgndEvtNumVec.size();i++){
				for(UInt_t j=0;j<sigEvtNumVec.size();j++){
					if(sigEvtNumVec[j] < bkgndEvtNumVec[i]) continue;
					if(sigEvtNumVec[j] > bkgndEvtNumVec[i]) break;
					if(bkgndEvtNumVec[i]==sigEvtNumVec[j]){
						numOverlappingEntries += 1;
						//std::cout<<"found an event which passes both legs"<<std::endl;
						break;
					}
				}//end loop over filtered bkgnd evt numbers
			}//end loop over filtered sig evt numbers
		}//fewer (or equal) bkgndEvts than sigEvts

	}//end if(sigHistName contains evtNumber)

	std::cout<< numOverlappingEntries <<" evts passed both legs" << std::endl;
	//std::cout<<"num bins with more than 1 entry = "<< numLargeBins << std::endl;
	return numOverlappingEntries;
	
}//end makeAndSaveOverlayHistoUsingEntryListsDiffCuts()



//use this fxn to compare distributions of pt, ecal iso, H/E, etc from
//matched reco signal objects and reco bkgnd objects 
//this function is essentially two copies of makeAndSaveHistoUsingEntryList()
//two TChains, two listFillArgs, two list names, two histPlotArgs, two histNames, one histTitle,
//one xAxisTitle, one canvName, on TCut object, one outputFile, and two Bool_t args are given
//to this fxn as inputs
void makeAndSaveOverlayHistoUsingEntryLists(TChain * sigChain,TChain * bkgndChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString sigHistPlotArg,TString bkgndHistPlotArg,TString sigHistName,TString bkgndHistName,TString histTitle,TString xAxisTitle,TString canvName,TCut sigFilt,TCut bkgndFilt,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy){
	sigChain->Draw(sigListFillArgs,sigFilt,"entrylistarray");
	sigChain->SetEntryList((TEntryListArray*) gROOT->FindObject(sigListName) );
	bkgndChain->Draw(bkgndListFillArgs,bkgndFilt,"entrylistarray");
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
	TString titleAddendum = "  black=matched signal  red=bkgnd  areas normalized to 1";
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

	//use these TString objects for plotting and filtering
	TString BkgndTrackedTreeName = "recoTreeBeforeTriggerFiltersTrackedBkgnd.";
	TString BkgndTracklessTreeName = "recoTreeBeforeTriggerFiltersTracklessBkgnd.";
	TString SignalTrackedTreeName = "recoTreeBeforeTriggerFiltersTrackedSignal.";
	TString SignalTracklessTreeName = "recoTreeBeforeTriggerFiltersTracklessSignal.";


	TChain * trackedLowPtBkgndChain = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	trackedLowPtBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_20to30_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedHighPtBkgndChain = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	trackedHighPtBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_30to80_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * trackedVeryHighPtBkgndChain = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	trackedVeryHighPtBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_80to170_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");



	TChain * tracklessLowPtBkgndChain = new TChain("recoAnalyzerTracklessWithL1Filter/recoTreeBeforeTriggerFiltersTracklessBkgndWithL1Filter","");
	tracklessLowPtBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_20to30_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * tracklessHighPtBkgndChain = new TChain("recoAnalyzerTracklessWithL1Filter/recoTreeBeforeTriggerFiltersTracklessBkgndWithL1Filter","");
	tracklessHighPtBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_30to80_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * tracklessVeryHighPtBkgndChain = new TChain("recoAnalyzerTracklessWithL1Filter/recoTreeBeforeTriggerFiltersTracklessBkgndWithL1Filter","");
	tracklessVeryHighPtBkgndChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_80to170_pt/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * trackedSignalChain = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedSignalWithL1Filter","");
	trackedSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * tracklessSignalChain = new TChain("recoAnalyzerTracklessWithL1Filter/recoTreeBeforeTriggerFiltersTracklessSignalWithL1Filter","");
	tracklessSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	TChain * matchedTrackedSignalChain = new TChain("recoAnalyzerMatchedTrackedWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTrackedSignalWithL1Filter","");
	matchedTrackedSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");
	
	TChain * matchedTracklessSignalChain = new TChain("recoAnalyzerMatchedTracklessWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTracklessSignalWithL1Filter","");
	matchedTracklessSignalChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/from7_4_0_patch1/*_25ns_DoubleEG_22_10.root");


	//void compareMatchedSigAndBkgnd(TChain * sigChain,TChain * bkgndVeryHighPtChain,TChain * bkgndHighPtChain,TChain * bkgndLowPtChain,TString sigFillArgs,TString sigListName,TString bkgndVHPtFillArgs,TString bkgndVHPtListName,TString bkgndHPtFillArgs,TString bkgndHPtListName,TString bkgndLPtFillArgs,TString bkgndLPtListName,TString sigHistPlotArg,TString bkgndVHPtHistPlotArg,TString bkgndHPtHistPlotArg,TString bkgndLPtHistPlotArg,TString sigHistName,TString bkgndVHPtHistName,TString bkgndHPtHistName,TString bkgndLPtHistName,Double_t highEffCutVal,Double_t lowEffCutVal,Double_t optimalCutVal,TString histTitle,TString xAxisTitle,TString canvName,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t isLowerBound,Bool_t doCrossSxnNormalization,TString etaRegion)

	compareMatchedSigAndBkgnd(matchedTrackedSignalChain,trackedVeryHighPtBkgndChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>clusterShapeTrackedBarrelSignalList","clusterShapeTrackedBarrelSignalList",">>clusterShapeTrackedBarrelVHPtBkgndList","clusterShapeTrackedBarrelVHPtBkgndList",">>clusterShapeTrackedBarrelHPtBkgndList","clusterShapeTrackedBarrelHPtBkgndList",">>clusterShapeTrackedBarrelLPtBkgndList","clusterShapeTrackedBarrelLPtBkgndList","clusterShapeHltEle>>clusterShapeTrackedBarrelSignalHisto(100,0.,0.04)","clusterShapeHltEle>>clusterShapeTrackedBarrelVHPtBkgndHisto(100,0.,0.04)","clusterShapeHltEle>>clusterShapeTrackedBarrelHPtBkgndHisto(100,0.,0.04)","clusterShapeHltEle>>clusterShapeTrackedBarrelLPtBkgndHisto(100,0.,0.04)","clusterShapeTrackedBarrelSignalHisto","clusterShapeTrackedBarrelVHPtBkgndHisto","clusterShapeTrackedBarrelHPtBkgndHisto","clusterShapeTrackedBarrelLPtBkgndHisto",0.017,0.011,0.014,"#sigma_{i#etai#eta} in EB for signal and bkgnds","#sigma_{i#etai#eta}","c1","cluster_shape_EB_matched_signal_and_bkgnds_showing_scan_range.png",false,false,false,false,"EB");

	compareMatchedSigAndBkgnd(matchedTrackedSignalChain,trackedVeryHighPtBkgndChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>hadEmTrackedBarrelSignalList","hadEmTrackedBarrelSignalList",">>hadEmTrackedBarrelVHPtBkgndList","hadEmTrackedBarrelVHPtBkgndList",">>hadEmTrackedBarrelHPtBkgndList","hadEmTrackedBarrelHPtBkgndList",">>hadEmTrackedBarrelLPtBkgndList","hadEmTrackedBarrelLPtBkgndList","hadEmHltEle>>hadEmTrackedBarrelSignalHisto(100,0.,0.4)","hadEmHltEle>>hadEmTrackedBarrelVHPtBkgndHisto(100,0.,0.4)","hadEmHltEle>>hadEmTrackedBarrelHPtBkgndHisto(100,0.,0.4)","hadEmHltEle>>hadEmTrackedBarrelLPtBkgndHisto(100,0.,0.4)","hadEmTrackedBarrelSignalHisto","hadEmTrackedBarrelVHPtBkgndHisto","hadEmTrackedBarrelHPtBkgndHisto","hadEmTrackedBarrelLPtBkgndHisto",0.2,0.08,0.14,"relative H/E in EB for signal and bkgnds","relative H/E","c2","rel_HoverE_EB_matched_signal_and_bkgnds_showing_scan_range.png",false,true,false,false,"EB");

	compareMatchedSigAndBkgnd(matchedTrackedSignalChain,trackedVeryHighPtBkgndChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>ecalIsoTrackedBarrelSignalList","ecalIsoTrackedBarrelSignalList",">>ecalIsoTrackedBarrelVHPtBkgndList","ecalIsoTrackedBarrelVHPtBkgndList",">>ecalIsoTrackedBarrelHPtBkgndList","ecalIsoTrackedBarrelHPtBkgndList",">>ecalIsoTrackedBarrelLPtBkgndList","ecalIsoTrackedBarrelLPtBkgndList","ecalIsoHltEle>>ecalIsoTrackedBarrelSignalHisto(100,0.,0.6)","ecalIsoHltEle>>ecalIsoTrackedBarrelVHPtBkgndHisto(100,0.,0.6)","ecalIsoHltEle>>ecalIsoTrackedBarrelHPtBkgndHisto(100,0.,0.6)","ecalIsoHltEle>>ecalIsoTrackedBarrelLPtBkgndHisto(100,0.,0.6)","ecalIsoTrackedBarrelSignalHisto","ecalIsoTrackedBarrelVHPtBkgndHisto","ecalIsoTrackedBarrelHPtBkgndHisto","ecalIsoTrackedBarrelLPtBkgndHisto",0.39,0.19,0.29,"relative ecalIso in EB for signal and bkgnds","relative ecalIso","c3","rel_ecalIso_EB_matched_signal_and_bkgnds_showing_scan_range.png",false,true,false,false,"EB");

	compareMatchedSigAndBkgnd(matchedTrackedSignalChain,trackedVeryHighPtBkgndChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>hcalIsoTrackedBarrelSignalList","hcalIsoTrackedBarrelSignalList",">>hcalIsoTrackedBarrelVHPtBkgndList","hcalIsoTrackedBarrelVHPtBkgndList",">>hcalIsoTrackedBarrelHPtBkgndList","hcalIsoTrackedBarrelHPtBkgndList",">>hcalIsoTrackedBarrelLPtBkgndList","hcalIsoTrackedBarrelLPtBkgndList","hcalIsoHltEle>>hcalIsoTrackedBarrelSignalHisto(100,0.,0.5)","hcalIsoHltEle>>hcalIsoTrackedBarrelVHPtBkgndHisto(100,0.,0.5)","hcalIsoHltEle>>hcalIsoTrackedBarrelHPtBkgndHisto(100,0.,0.5)","hcalIsoHltEle>>hcalIsoTrackedBarrelLPtBkgndHisto(100,0.,0.5)","hcalIsoTrackedBarrelSignalHisto","hcalIsoTrackedBarrelVHPtBkgndHisto","hcalIsoTrackedBarrelHPtBkgndHisto","hcalIsoTrackedBarrelLPtBkgndHisto",0.3,0.15,0.25,"relative hcalIso in EB for signal and bkgnds","relative hcalIso","c4","rel_hcalIso_EB_matched_signal_and_bkgnds_showing_scan_range.png",false,true,false,false,"EB");





	//hlt eta cuts
	TCut trackedEBHltEta = "TMath::Abs(etaHltEle)<1.479";
	TCut trackedEEHltLowEta = "TMath::Abs(etaHltEle)>1.479";
	TCut trackedEEHltHighEta = "TMath::Abs(etaHltEle)<2.5";
	TCut trackedEEHltEta = trackedEEHltLowEta + trackedEEHltHighEta;
	TCut tracklessEEHltLowEta = "TMath::Abs(etaHltEle)>2.5";
	TCut tracklessEEHltHighEta = "TMath::Abs(etaHltEle)<3.0";
	TCut tracklessEEHltEta = tracklessEEHltLowEta + tracklessEEHltHighEta;

	//hlt dR cuts
	TCut hltDr = "deltaRHltEle<0.1";

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
	TCut hltMllLowerBound = "diObjectMassHltEle>10";
	TCut hltMllAbsoluteLowerBound = "diObjectMassHltEle>2.";
	TCut hltMllTinyUpperBound = "diObjectMassHltEle<10";

	//tracked and trackless leg cuts from old trigger used in 2012
	//original tracked leg
	TCut originalTrackedPt = "ptHltEle>27.";
	TCut originalTrackedEESigmaIEIE = "clusterShapeHltEle<0.031";
	TCut originalTrackedEEHE = "hadEmHltEle<0.075";
	TCut originalTrackedEEEcalIso = "ecalIsoHltEle<0.11";
	TCut originalTrackedEEHcalIso = "hcalIsoHltEle<0.11";
	
	TCut originalTrackedEEEp = "epHltEle<0.009";
	TCut originalTrackedEEDeta = "dEtaHltEle<0.01";
	TCut originalTrackedEEDphi = "dPhiHltEle<0.03";
	TCut originalTrackedEETrackIso = "trackIsoHltEle<0.125";
	TCut originalTrackedEBSigmaIEIE = "clusterShapeHltEle<0.011";
	TCut originalTrackedEBHE = "hadEmHltEle<0.1";
	TCut originalTrackedEBEcalIso = "ecalIsoHltEle<0.16";
	TCut originalTrackedEBHcalIso = "hcalIsoHltEle<0.11";
	TCut originalTrackedEBEp = "epHltEle<0.012";
	TCut originalTrackedEBDeta = "dEtaHltEle<0.005";
	TCut originalTrackedEBDphi = "dPhiHltEle<0.03";
	TCut originalTrackedEBTrackIso = "trackIsoHltEle<0.125";

	//original trackless leg
	TCut originalTracklessPt = "ptHltEle>15.";
	TCut originalTracklessEESigmaIEIE = "clusterShapeHltEle<0.031";
	TCut originalTracklessEEHE = "hadEmHltEle<0.075";
	TCut originalTracklessEEEcalIso = "ecalIsoHltEle<0.2";
	TCut originalTracklessEEHcalIso = "hcalIsoHltEle<0.2";


	//optimized tracked leg 
	TCut optimizedTrackedPt = "ptHltEle>31.";
	TCut optimizedTrackedEESigmaIEIE = "clusterShapeHltEle<0.027";
	TCut optimizedTrackedEEHE = "hadEmHltEle<0.063";
	TCut optimizedTrackedEEEcalIso = "ecalIsoHltEle<0.084";
	TCut optimizedTrackedEEHcalIso = "hcalIsoHltEle<0.14";
	
	TCut optimizedTrackedEEEp = "epHltEle<0.0019";
	TCut optimizedTrackedEEDeta = "dEtaHltEle<0.0011";
	TCut optimizedTrackedEEDphi = "dPhiHltEle<0.0075";
	TCut optimizedTrackedEETrackIso = "trackIsoHltEle<0.07";
	
	TCut optimizedTrackedEBSigmaIEIE = "clusterShapeHltEle<0.009";
	TCut optimizedTrackedEBHE = "hadEmHltEle<0.038";
	TCut optimizedTrackedEBEcalIso = "ecalIsoHltEle<0.11";
	TCut optimizedTrackedEBHcalIso = "hcalIsoHltEle<0.1";
	TCut optimizedTrackedEBEp = "epHltEle<0.0039";
	TCut optimizedTrackedEBDeta = "dEtaHltEle<0.0017";
	TCut optimizedTrackedEBDphi = "dPhiHltEle<0.0015";
	TCut optimizedTrackedEBTrackIso = "trackIsoHltEle<0.044";


	//optimized trackless leg 
	TCut optimizedTracklessPt = "ptHltEle>25.";
	TCut optimizedTracklessEESigmaIEIE = "clusterShapeHltEle<0.027";
	TCut optimizedTracklessEEHE = "hadEmHltEle<0.13";
	TCut optimizedTracklessEEEcalIso = "ecalIsoHltEle<0.084";
	TCut optimizedTracklessEEHcalIso = "hcalIsoHltEle<0.37";


	////tracked and trackless leg cuts for playing around
	TCut trialTrackedEBPt = "ptHltEle>=27.";

	TCut trialTrackedEBSigmaIEIE = "clusterShapeHltEle<=0.017";
	TCut trialTrackedEBHE = "hadEmHltEle<=0.2";
	TCut trialTrackedEBEcalIso = "ecalIsoHltEle<=0.39";
	TCut trialTrackedEBHcalIso = "hcalIsoHltEle<=0.3";
	TCut trialTrackedEBEp = "epHltEle<=0.012";
	TCut trialTrackedEBDeta = "dEtaHltEle<=0.005";
	TCut trialTrackedEBDphi = "dPhiHltEle<=0.03";
	TCut trialTrackedEBTrackIso = "trackIsoHltEle<=0.125";

	TCut trialTrackedEEPt = "ptHltEle>=27.";
	TCut trialTrackedEESigmaIEIE = "clusterShapeHltEle<=0.036";
	TCut trialTrackedEEHE = "hadEmHltEle<=0.2";
	TCut trialTrackedEEEcalIso = "ecalIsoHltEle<=0.26";
	TCut trialTrackedEEHcalIso = "hcalIsoHltEle<=0.34";
	TCut trialTrackedEEEp = "epHltEle<=0.009";
	TCut trialTrackedEEDeta = "dEtaHltEle<=0.01";
	TCut trialTrackedEEDphi = "dPhiHltEle<=0.03";
	TCut trialTrackedEETrackIso = "trackIsoHltEle<=0.125";

	TCut trialTracklessPt = "ptHltEle>=16.";
	TCut trialTracklessEESigmaIEIE = "clusterShapeHltEle<=0.043";
	TCut trialTracklessEEHE = "hadEmHltEle<=0.26";
	TCut trialTracklessEEEcalIso = "ecalIsoHltEle<=0.25";
	TCut trialTracklessEEHcalIso = "hcalIsoHltEle<=0.77";




	TCut originalTrackedBarrelLeg = originalTrackedPt+originalTrackedEBSigmaIEIE+originalTrackedEBHE+originalTrackedEBEcalIso+originalTrackedEBHcalIso+trackedEBHltEta+originalTrackedEBEp+originalTrackedEBDeta+originalTrackedEBDphi+originalTrackedEBTrackIso;
	TCut originalTrackedEndcapLeg = originalTrackedPt+originalTrackedEESigmaIEIE+originalTrackedEEHE+originalTrackedEEEcalIso+originalTrackedEEHcalIso+trackedEEHltEta+originalTrackedEEEp+originalTrackedEEDeta+originalTrackedEEDphi+originalTrackedEETrackIso;
	TCut originalTracklessEndcapLeg = originalTracklessPt+originalTracklessEESigmaIEIE+originalTracklessEEHE+originalTracklessEEEcalIso+originalTracklessEEHcalIso+tracklessEEHltEta;

	TCut optimizedTrackedBarrelLeg = optimizedTrackedPt+optimizedTrackedEBSigmaIEIE+optimizedTrackedEBHE+optimizedTrackedEBEcalIso+optimizedTrackedEBHcalIso+trackedEBHltEta+optimizedTrackedEBEp+optimizedTrackedEBDeta+optimizedTrackedEBDphi+optimizedTrackedEBTrackIso;
	TCut optimizedTrackedEndcapLeg = optimizedTrackedPt+optimizedTrackedEESigmaIEIE+optimizedTrackedEEHE+optimizedTrackedEEEcalIso+optimizedTrackedEEHcalIso+trackedEEHltEta+optimizedTrackedEEEp+optimizedTrackedEEDeta+optimizedTrackedEEDphi+optimizedTrackedEETrackIso;
	TCut optimizedTracklessEndcapLeg = optimizedTracklessPt+optimizedTracklessEESigmaIEIE+optimizedTracklessEEHE+optimizedTracklessEEEcalIso+optimizedTracklessEEHcalIso+tracklessEEHltEta;

	TCut trialTrackedBarrelLeg = trialTrackedEBPt+trialTrackedEBSigmaIEIE+trialTrackedEBHE+trialTrackedEBEcalIso+trialTrackedEBHcalIso+trackedEBHltEta+trialTrackedEBEp+trialTrackedEBDeta+trialTrackedEBDphi+trialTrackedEBTrackIso;
	TCut trialTrackedEndcapLeg = trialTrackedEEPt+trialTrackedEESigmaIEIE+trialTrackedEEHE+trialTrackedEEEcalIso+trialTrackedEEHcalIso+trackedEEHltEta+trialTrackedEEEp+trialTrackedEEDeta+trialTrackedEEDphi+trialTrackedEETrackIso;
	TCut trialTracklessEndcapLeg = trialTracklessPt+trialTracklessEESigmaIEIE+trialTracklessEEHE+trialTracklessEEEcalIso+trialTracklessEEHcalIso+tracklessEEHltEta;



	/*
	//these are the filtered trees which contain evts passing all tracked and trackless leg selections
	trackedLowPtBkgndChain->Draw(">>LowPtoriginalTrackedLegList",(originalTrackedBarrelLeg || originalTrackedEndcapLeg),"entrylistarray");
	trackedLowPtBkgndChain->SetEntryList((TEntryListArray*) gROOT->FindObject("LowPtoriginalTrackedLegList") );
	trackedHighPtBkgndChain->Draw(">>HighPtoriginalTrackedLegList",(originalTrackedBarrelLeg || originalTrackedEndcapLeg),"entrylistarray");
	trackedHighPtBkgndChain->SetEntryList((TEntryListArray*) gROOT->FindObject("HighPtoriginalTrackedLegList") );
	trackedSignalChain->Draw(">>trackedLegSignalList",(originalTrackedBarrelLeg || originalTrackedEndcapLeg),"entrylistarray");
	trackedSignalChain->SetEntryList((TEntryListArray*) gROOT->FindObject("trackedLegSignalList") );
	
	tracklessLowPtBkgndChain->Draw(">>LowPtoriginalTracklessLegList",originalTracklessEndcapLeg,"entrylistarray");
	tracklessLowPtBkgndChain->SetEntryList((TEntryListArray*) gROOT->FindObject("LowPtoriginalTracklessLegList") );

	tracklessHighPtBkgndChain->Draw(">>HighPttrialTracklessLegList",trialTracklessEndcapLeg,"entrylistarray");
	TEntryListArray * highPtTracklessLegList = (TEntryListArray*) gROOT->Get("HighPttrialTracklessLegList");
	tracklessHighPtBkgndChain->SetEntryList((TEntryListArray*) gROOT->FindObject("HighPttrialTracklessLegList") );
	
	tracklessSignalChain->Draw(">>tracklessLegSignalList",originalTracklessEndcapLeg,"entrylistarray");
	tracklessSignalChain->SetEntryList((TEntryListArray*) gROOT->FindObject("tracklessLegSignalList") );
	

	std::cout<< trackedHighPtBkgndChain->GetEntryList()->GetN() <<" high pt bkgnd evts pass the tracked leg"<<std::endl;
	std::cout<< tracklessHighPtBkgndChain->GetEntryList()->GetN() <<" high pt bkgnd evts pass the trackless leg"<<std::endl;
	std::cout<<" "<<std::endl;
	
	std::cout<< trackedLowPtBkgndChain->GetEntryList()->GetN() <<" low pt bkgnd evts pass the tracked leg"<<std::endl;
	std::cout<< tracklessLowPtBkgndChain->GetEntryList()->GetN() <<" low pt bkgnd evts pass the trackless leg"<<std::endl;
	std::cout<<" "<<std::endl;

	std::cout<< trackedSignalChain->GetEntryList()->GetN() <<" signal evts pass the tracked leg"<<std::endl;
	std::cout<< tracklessSignalChain->GetEntryList()->GetN() <<" signal evts pass the trackless leg"<<std::endl;
	std::cout<<" "<<std::endl;
	*/


	Float_t sigEvtsPassing=0, bkgndLowPtEvtsPassing=0, bkgndHighPtEvtsPassing=0, bkgndVeryHighPtEvtsPassing=0;


	//Float_t numEvtsPassingBothLegs(TChain * tracklessChain,TChain * trackedChain,TString tracklessListFillArgs,TString tracklessListName,TString trackedListFillArgs,TString trackedListName,TCut tracklessFilters,TCut trackedFilters )
	
	//numEvtsPassingBothLegs(matchedTracklessSignalChain,matchedTrackedSignalChain,">>tracklessevtNumberZeroMatchedSignalList","tracklessevtNumberZeroMatchedSignalList",">>trackedevtNumberZeroMatchedSignalList","trackedevtNumberZeroMatchedSignalList",hltDr,hltDr);

	//numEvtsPassingBothLegs(matchedTracklessSignalChain,matchedTrackedSignalChain,">>tracklessevtNumberOneMatchedSignalList","tracklessevtNumberOneMatchedSignalList",">>trackedevtNumberOneMatchedSignalList","trackedevtNumberOneMatchedSignalList",hltDr+trialTracklessEndcapLeg,hltDr+(trialTrackedBarrelLeg || trialTrackedEndcapLeg) );


	//sigEvtsPassing = numEvtsPassingBothLegs(tracklessSignalChain,trackedSignalChain,">>tracklessevtNumberZeroSignalList","tracklessevtNumberZeroSignalList",">>trackedevtNumberZeroSignalList","trackedevtNumberZeroSignalList",trialTracklessEndcapLeg,(trialTrackedBarrelLeg || trialTrackedEndcapLeg) );


	/*
	bkgndLowPtEvtsPassing = numEvtsPassingBothLegs(tracklessLowPtBkgndChain,trackedLowPtBkgndChain,">>tracklessevtNumberZeroLowPtBkgndList","tracklessevtNumberZeroLowPtBkgndList",">>trackedevtNumberZeroLowPtBkgndList","trackedevtNumberZeroLowPtBkgndList",trialTracklessEndcapLeg,(trialTrackedBarrelLeg || trialTrackedEndcapLeg) );

	bkgndHighPtEvtsPassing = numEvtsPassingBothLegs(tracklessHighPtBkgndChain,trackedHighPtBkgndChain,">>tracklessevtNumberZeroHighPtBkgndList","tracklessevtNumberZeroHighPtBkgndList",">>trackedevtNumberZeroHighPtBkgndList","trackedevtNumberZeroHighPtBkgndList",trialTracklessEndcapLeg,(trialTrackedBarrelLeg || trialTrackedEndcapLeg) );

	bkgndVeryHighPtEvtsPassing = numEvtsPassingBothLegs(tracklessVeryHighPtBkgndChain,trackedVeryHighPtBkgndChain,">>tracklessevtNumberZeroVeryHighPtBkgndList","tracklessevtNumberZeroVeryHighPtBkgndList",">>trackedevtNumberZeroVeryHighPtBkgndList","trackedevtNumberZeroVeryHighPtBkgndList",trialTracklessEndcapLeg,(trialTrackedBarrelLeg || trialTrackedEndcapLeg) );

	std::cout<<"\t"<<std::endl;
	std::cout<< bkgndHighPtEvtsPassing <<"\t HighPt bkgnd evts passed cuts"<<std::endl;
	std::cout<< bkgndVeryHighPtEvtsPassing <<"\t VeryHighPt bkgnd evts passed cuts"<<std::endl;
	std::cout<< bkgndLowPtEvtsPassing <<"\t LowPt bkgnd evts passed cuts"<<std::endl;
	std::cout<<"\t"<<std::endl;
	*/

	//std::vector<Float_t> calcTriggerRate(Float_t nSigEvts, TChain * sigChain, Float_t nLowPtBkgndEvts, TChain * lowPtBkgndChain, Float_t nHighPtBkgndEvts, TChain * highPtBkgndChain)

	//calcTriggerRate(sigEvtsPassing,trackedSignalChain,bkgndLowPtEvtsPassing,trackedLowPtBkgndChain,bkgndHighPtEvtsPassing,trackedHighPtBkgndChain);


	gStyle->SetOptStat(1111);

	//matchedRecoToGenOverlayHistos(matchedTrackedSignalChain,genMllRange+trackedEEHltHighEta, matchedTracklessSignalChain,genMllRange+tracklessEEHltEta);
	
	//use this to quickly change the ending of the title for all plots
	TString plotTitleModifier = " pt>10 GeV ";

	//matchedTracklessSignalChain->Draw(">>testList",genMllRange+tracklessEEHltEta+hltDr+hltLowEt+hltMllAbsoluteLowerBound,"entrylistarray");
	//matchedTracklessSignalChain->SetEntryList((TEntryListArray*) gROOT->FindObject("testList") );
	//TCanvas * c999 = new TCanvas("c999","c999",500,500);
	//c999->cd();
	//matchedTracklessSignalChain->Draw("evtNumber>>evtNumberHisto");

	//TCanvas * c1010 = new TCanvas("c1010","c1010",500,500);
	//c1010->cd();
	//matchedTracklessSignalChain->Draw("diObjectMassHltEle>>diObjectMassHltEleHisto");

	//matchedTracklessSignalChain->SetEntryList(0);
	//TCanvas * c1011 = new TCanvas("c1011","c1011",500,500);
	//c1011->cd();
	//matchedTracklessSignalChain->Draw("evtNumber>>evtNumberHistoOne");





	//plots of matched signal distributions overlaid with bkgnd distributions.  Same TCuts applied to both.
	/*
	//tracked barrel distributions
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigptBarrelList","trackedSigptBarrelList",">>trackedBkgndptBarrelList","trackedBkgndptBarrelList","ptHltEle>>trackedSigptBarrel(100,0.,100.)","ptHltEle>>trackedBkgndptBarrel(100,0.,100.)","trackedSigptBarrel","trackedBkgndptBarrel","pt of tracked leg hlt objects in barrel"+plotTitleModifier,"pt","c1000",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"pt_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",true,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigetaBarrelList","trackedSigetaBarrelList",">>trackedBkgndetaBarrelList","trackedBkgndetaBarrelList","etaHltEle>>trackedSigetaBarrel(100,-2.0,2.0)","etaHltEle>>trackedBkgndetaBarrel(100,-2.0,2.0)","trackedSigetaBarrel","trackedBkgndetaBarrel","eta of tracked leg hlt objects in barrel"+plotTitleModifier,"eta","c1001",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"eta_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigphiBarrelList","trackedSigphiBarrelList",">>trackedBkgndphiBarrelList","trackedBkgndphiBarrelList","phiHltEle>>trackedSigphiBarrel(100,-3.5,3.5)","phiHltEle>>trackedBkgndphiBarrel(100,-3.5,3.5)","trackedSigphiBarrel","trackedBkgndphiBarrel","phi of tracked leg hlt objects in barrel"+plotTitleModifier,"phi","c1002",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"phi_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigclusterShapeBarrelList","trackedSigclusterShapeBarrelList",">>trackedBkgndclusterShapeBarrelList","trackedBkgndclusterShapeBarrelList","clusterShapeHltEle>>trackedSigclusterShapeBarrel(100,0.,0.04)","clusterShapeHltEle>>trackedBkgndclusterShapeBarrel(100,0.,0.04)","trackedSigclusterShapeBarrel","trackedBkgndclusterShapeBarrel","#sigma_{i#etai#eta} of tracked leg hlt objects in barrel"+plotTitleModifier,"#sigma_{i#etai#eta}","c1003",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"clusterShape_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighadEmBarrelList","trackedSighadEmBarrelList",">>trackedBkgndhadEmBarrelList","trackedBkgndhadEmBarrelList","hadEmHltEle>>trackedSighadEmBarrel(100,0.,0.3)","hadEmHltEle>>trackedBkgndhadEmBarrel(100,0.,0.3)","trackedSighadEmBarrel","trackedBkgndhadEmBarrel","relative had/Em of tracked leg hlt objects in barrel"+plotTitleModifier,"had/Em/Energy","c1004",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"hadEm_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigecalIsoBarrelList","trackedSigecalIsoBarrelList",">>trackedBkgndecalIsoBarrelList","trackedBkgndecalIsoBarrelList","ecalIsoHltEle>>trackedSigecalIsoBarrel(100,-0.1,1.5)","ecalIsoHltEle>>trackedBkgndecalIsoBarrel(100,-0.1,1.5)","trackedSigecalIsoBarrel","trackedBkgndecalIsoBarrel","relative ecalIso of tracked leg hlt objects in barrel"+plotTitleModifier,"ecalIso/pt","c1005",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"ecalIso_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighcalIsoBarrelList","trackedSighcalIsoBarrelList",">>trackedBkgndhcalIsoBarrelList","trackedBkgndhcalIsoBarrelList","hcalIsoHltEle>>trackedSighcalIsoBarrel(100,0.,1.)","hcalIsoHltEle>>trackedBkgndhcalIsoBarrel(100,0.,1.)","trackedSighcalIsoBarrel","trackedBkgndhcalIsoBarrel","relative hcalIso of tracked leg hlt objects in barrel"+plotTitleModifier,"hcalIso/pt","c1006",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"hcalIso_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigepBarrelList","trackedSigepBarrelList",">>trackedBkgndepBarrelList","trackedBkgndepBarrelList","epHltEle>>trackedSigepBarrel(100,0.,0.27)","epHltEle>>trackedBkgndepBarrel(100,0.,0.27)","trackedSigepBarrel","trackedBkgndepBarrel","(1/E)-(1/P) of tracked leg hlt objects in barrel"+plotTitleModifier,"ep","c1010",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"ep_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdEtaBarrelList","trackedSigdEtaBarrelList",">>trackedBkgnddEtaBarrelList","trackedBkgnddEtaBarrelList","dEtaHltEle>>trackedSigdEtaBarrel(100,0.,0.027)","dEtaHltEle>>trackedBkgnddEtaBarrel(100,0.,0.027)","trackedSigdEtaBarrel","trackedBkgnddEtaBarrel","#Delta #eta of tracked leg hlt objects in barrel"+plotTitleModifier,"#Delta #eta","c1007",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"dEta_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdPhiBarrelList","trackedSigdPhiBarrelList",">>trackedBkgnddPhiBarrelList","trackedBkgnddPhiBarrelList","dPhiHltEle>>trackedSigdPhiBarrel(100,0.,0.17)","dPhiHltEle>>trackedBkgnddPhiBarrel(100,0.,0.17)","trackedSigdPhiBarrel","trackedBkgnddPhiBarrel","#Delta #phi of tracked leg hlt objects in barrel"+plotTitleModifier,"#Delta #phi","c1008",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"dPhi_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigtrackIsoBarrelList","trackedSigtrackIsoBarrelList",">>trackedBkgndtrackIsoBarrelList","trackedBkgndtrackIsoBarrelList","trackIsoHltEle>>trackedSigtrackIsoBarrel(100,0.,0.5)","trackIsoHltEle>>trackedBkgndtrackIsoBarrel(100,0.,0.5)","trackedSigtrackIsoBarrel","trackedBkgndtrackIsoBarrel","relative trackIso of tracked leg hlt objects in barrel"+plotTitleModifier,"trackIso/pt","c1009",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"trackIso_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdiObjectMassBarrelList","trackedSigdiObjectMassBarrelList",">>trackedBkgnddiObjectMassBarrelList","trackedBkgnddiObjectMassBarrelList","diObjectMassHltEle>>trackedSigdiObjectMassBarrel(150,-2.,140.)","diObjectMassHltEle>>trackedBkgnddiObjectMassBarrel(150,-2.,140.)","trackedSigdiObjectMassBarrel","trackedBkgnddiObjectMassBarrel","diObjectMass of tracked leg hlt objects in barrel"+plotTitleModifier,"diObjectMass","c1011",trackedEBHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEBHltEta+hltMllLowerBound,"diObjectMass_for_tracked_barrel_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",true,false);
	
	*/	

	/*
	//tracked endcap distributions
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigptEndcapList","trackedSigptEndcapList",">>trackedBkgndptEndcapList","trackedBkgndptEndcapList","ptHltEle>>trackedSigptEndcap(100,0.,100.)","ptHltEle>>trackedBkgndptEndcap(100,0.,100.)","trackedSigptEndcap","trackedBkgndptEndcap","pt of tracked leg hlt objects in endcap"+plotTitleModifier,"pt","c2000",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"pt_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",true,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigetaEndcapList","trackedSigetaEndcapList",">>trackedBkgndetaEndcapList","trackedBkgndetaEndcapList","etaHltEle>>trackedSigetaEndcap(100,-2.5,2.5)","etaHltEle>>trackedBkgndetaEndcap(100,-2.5,2.5)","trackedSigetaEndcap","trackedBkgndetaEndcap","eta of tracked leg hlt objects in endcap"+plotTitleModifier,"eta","c2001",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"eta_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigphiEndcapList","trackedSigphiEndcapList",">>trackedBkgndphiEndcapList","trackedBkgndphiEndcapList","phiHltEle>>trackedSigphiEndcap(100,-3.5,3.5)","phiHltEle>>trackedBkgndphiEndcap(100,-3.5,3.5)","trackedSigphiEndcap","trackedBkgndphiEndcap","phi of tracked leg hlt objects in endcap"+plotTitleModifier,"phi","c2002",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"phi_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigclusterShapeEndcapList","trackedSigclusterShapeEndcapList",">>trackedBkgndclusterShapeEndcapList","trackedBkgndclusterShapeEndcapList","clusterShapeHltEle>>trackedSigclusterShapeEndcap(100,0.,0.08)","clusterShapeHltEle>>trackedBkgndclusterShapeEndcap(100,0.,0.08)","trackedSigclusterShapeEndcap","trackedBkgndclusterShapeEndcap","#sigma_{i#etai#eta} of tracked leg hlt objects in endcap"+plotTitleModifier,"#sigma_{i#etai#eta}","c2003",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"clusterShape_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighadEmEndcapList","trackedSighadEmEndcapList",">>trackedBkgndhadEmEndcapList","trackedBkgndhadEmEndcapList","hadEmHltEle>>trackedSighadEmEndcap(100,0.,0.7)","hadEmHltEle>>trackedBkgndhadEmEndcap(100,0.,0.7)","trackedSighadEmEndcap","trackedBkgndhadEmEndcap","relative had/Em of tracked leg hlt objects in endcap"+plotTitleModifier,"had/Em/Energy","c2004",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"hadEm_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigecalIsoEndcapList","trackedSigecalIsoEndcapList",">>trackedBkgndecalIsoEndcapList","trackedBkgndecalIsoEndcapList","ecalIsoHltEle>>trackedSigecalIsoEndcap(100,-0.2,3.)","ecalIsoHltEle>>trackedBkgndecalIsoEndcap(100,-0.2,3.)","trackedSigecalIsoEndcap","trackedBkgndecalIsoEndcap","relative ecalIso of tracked leg hlt objects in endcap"+plotTitleModifier,"ecalIso/pt","c2005",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"ecalIso_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSighcalIsoEndcapList","trackedSighcalIsoEndcapList",">>trackedBkgndhcalIsoEndcapList","trackedBkgndhcalIsoEndcapList","hcalIsoHltEle>>trackedSighcalIsoEndcap(100,-0.2,2.5)","hcalIsoHltEle>>trackedBkgndhcalIsoEndcap(100,-0.2,2.5)","trackedSighcalIsoEndcap","trackedBkgndhcalIsoEndcap","relative hcalIso of tracked leg hlt objects in endcap"+plotTitleModifier,"hcalIso/pt","c2006",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"hcalIso_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigepEndcapList","trackedSigepEndcapList",">>trackedBkgndepEndcapList","trackedBkgndepEndcapList","epHltEle>>trackedSigepEndcap(100,0.,0.27)","epHltEle>>trackedBkgndepEndcap(100,0.,0.27)","trackedSigepEndcap","trackedBkgndepEndcap","(1/E)-(1/P) of tracked leg hlt objects in endcap"+plotTitleModifier,"ep","c2010",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"ep_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdEtaEndcapList","trackedSigdEtaEndcapList",">>trackedBkgnddEtaEndcapList","trackedBkgnddEtaEndcapList","dEtaHltEle>>trackedSigdEtaEndcap(100,0.,0.027)","dEtaHltEle>>trackedBkgnddEtaEndcap(100,0.,0.027)","trackedSigdEtaEndcap","trackedBkgnddEtaEndcap","#Delta #eta of tracked leg hlt objects in endcap"+plotTitleModifier,"#Delta #eta","c2007",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"dEta_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdPhiEndcapList","trackedSigdPhiEndcapList",">>trackedBkgnddPhiEndcapList","trackedBkgnddPhiEndcapList","dPhiHltEle>>trackedSigdPhiEndcap(100,0.,0.17)","dPhiHltEle>>trackedBkgnddPhiEndcap(100,0.,0.17)","trackedSigdPhiEndcap","trackedBkgnddPhiEndcap","#Delta #phi of tracked leg hlt objects in endcap"+plotTitleModifier,"#Delta #phi","c2008",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"dPhi_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigtrackIsoEndcapList","trackedSigtrackIsoEndcapList",">>trackedBkgndtrackIsoEndcapList","trackedBkgndtrackIsoEndcapList","trackIsoHltEle>>trackedSigtrackIsoEndcap(100,0.,0.5)","trackIsoHltEle>>trackedBkgndtrackIsoEndcap(100,0.,0.5)","trackedSigtrackIsoEndcap","trackedBkgndtrackIsoEndcap","relative trackIso of tracked leg hlt objects in endcap"+plotTitleModifier,"trackIso/pt","c2009",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"trackIso_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTrackedSignalChain,trackedBkgndChain,">>trackedSigdiObjectMassEndcapList","trackedSigdiObjectMassEndcapList",">>trackedBkgnddiObjectMassEndcapList","trackedBkgnddiObjectMassEndcapList","diObjectMassHltEle>>trackedSigdiObjectMassEndcap(150,-2.,140.)","diObjectMassHltEle>>trackedBkgnddiObjectMassEndcap(150,-2.,140.)","trackedSigdiObjectMassEndcap","trackedBkgnddiObjectMassEndcap","diObjectMass of tracked leg hlt objects in endcap"+plotTitleModifier,"diObjectMass","c2011",trackedEEHltEta+hltMllLowerBound+hltDr+genMllRange,trackedEEHltEta+hltMllLowerBound,"diObjectMass_for_tracked_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",true,false);
	
	*/

	/*
	//trackless endcap distributions
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigptEndcapList","tracklessSigptEndcapList",">>tracklessBkgndptEndcapList","tracklessBkgndptEndcapList","ptHltEle[0]>>tracklessSigptEndcap(100,0.,100.)","ptHltEle>>tracklessBkgndptEndcap(100,0.,100.)","tracklessSigptEndcap","tracklessBkgndptEndcap","pt of trackless leg hlt objects in endcap"+plotTitleModifier,"pt","c3000",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"pt_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",true,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigetaEndcapList","tracklessSigetaEndcapList",">>tracklessBkgndetaEndcapList","tracklessBkgndetaEndcapList","etaHltEle[0]>>tracklessSigetaEndcap(100,-3.1,3.1)","etaHltEle>>tracklessBkgndetaEndcap(100,-3.1,3.1)","tracklessSigetaEndcap","tracklessBkgndetaEndcap","eta of trackless leg hlt objects in endcap"+plotTitleModifier,"eta","c3001",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"eta_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigphiEndcapList","tracklessSigphiEndcapList",">>tracklessBkgndphiEndcapList","tracklessBkgndphiEndcapList","phiHltEle[0]>>tracklessSigphiEndcap(100,-3.5,3.5)","phiHltEle>>tracklessBkgndphiEndcap(100,-3.5,3.5)","tracklessSigphiEndcap","tracklessBkgndphiEndcap","phi of trackless leg hlt objects in endcap"+plotTitleModifier,"phi","c3002",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"phi_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigclusterShapeEndcapList","tracklessSigclusterShapeEndcapList",">>tracklessBkgndclusterShapeEndcapList","tracklessBkgndclusterShapeEndcapList","clusterShapeHltEle[0]>>tracklessSigclusterShapeEndcap(100,0.,0.08)","clusterShapeHltEle>>tracklessBkgndclusterShapeEndcap(100,0.,0.08)","tracklessSigclusterShapeEndcap","tracklessBkgndclusterShapeEndcap","#sigma_{i#etai#eta} of trackless leg hlt objects in endcap"+plotTitleModifier,"#sigma_{i#etai#eta}","c3003",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"clusterShape_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,false);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSighadEmEndcapList","tracklessSighadEmEndcapList",">>tracklessBkgndhadEmEndcapList","tracklessBkgndhadEmEndcapList","hadEmHltEle[0]>>tracklessSighadEmEndcap(100,0.,2.)","hadEmHltEle>>tracklessBkgndhadEmEndcap(100,0.,2.)","tracklessSighadEmEndcap","tracklessBkgndhadEmEndcap","relative had/Em of trackless leg hlt objects in endcap"+plotTitleModifier,"had/Em/Energy","c3004",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"hadEm_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigecalIsoEndcapList","tracklessSigecalIsoEndcapList",">>tracklessBkgndecalIsoEndcapList","tracklessBkgndecalIsoEndcapList","ecalIsoHltEle[0]>>tracklessSigecalIsoEndcap(100,-0.5,2.5)","ecalIsoHltEle>>tracklessBkgndecalIsoEndcap(100,-0.5,2.5)","tracklessSigecalIsoEndcap","tracklessBkgndecalIsoEndcap","relative ecalIso of trackless leg hlt objects in endcap"+plotTitleModifier,"ecalIso/pt","c3005",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"ecalIso_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSighcalIsoEndcapList","tracklessSighcalIsoEndcapList",">>tracklessBkgndhcalIsoEndcapList","tracklessBkgndhcalIsoEndcapList","hcalIsoHltEle[0]>>tracklessSighcalIsoEndcap(100,-0.8,4.)","hcalIsoHltEle>>tracklessBkgndhcalIsoEndcap(100,-0.8,4.)","tracklessSighcalIsoEndcap","tracklessBkgndhcalIsoEndcap","relative hcalIso of trackless leg hlt objects in endcap"+plotTitleModifier,"hcalIso/pt","c3006",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"hcalIso_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",false,true);
	makeAndSaveOverlayHistoUsingEntryLists(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigdiObjectMassEndcapList","tracklessSigdiObjectMassEndcapList",">>tracklessBkgnddiObjectMassEndcapList","tracklessBkgnddiObjectMassEndcapList","diObjectMassHltEle[0]>>tracklessSigdiObjectMassEndcap(150,-2.,140.)","diObjectMassHltEle>>tracklessBkgnddiObjectMassEndcap(150,-2.,140.)","tracklessSigdiObjectMassEndcap","tracklessBkgnddiObjectMassEndcap","diObjectMass of trackless leg hlt objects in endcap"+plotTitleModifier,"diObjectMass","c3007",tracklessEEHltEta+hltMllLowerBound+hltDr+genMllRange,tracklessEEHltEta+hltMllLowerBound,"diObjectMass_for_trackless_endcap_hlt_objs_signal_and_bkgnd_parent_mass_above_10.png",true,false);
	
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
	//makeAndSaveOverlayHistoUsingEntryListsDiffCuts(tracklessSignalChain,matchedTracklessSignalChain,">>tracklessdiObjectMassZeroSignalList","tracklessdiObjectMassZeroSignalList",">>tracklessdiObjectMassZeroGenList","tracklessdiObjectMassZeroGenList","diObjectMassHltEle>>tracklessdiObjectMassZeroSignal(150,-2.,140.)","diObjectMassGenEle>>tracklessdiObjectMassZeroGen(150,-2.,140.)","tracklessdiObjectMassZeroSignal","tracklessdiObjectMassZeroGen","Mass of parent particle for GEN and reco signal electrons","diObjectMass","c110",tracklessEEHltEta+hltMllAbsoluteLowerBound,"","parent_mass_gen_and_unmatched_reco_signal_eles.png",true,false,false);


	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	//find optimal cut values for tracked (barrel and endcap) and trackless leg cut variables 
	
	std::vector<TString> cutVarNames;
	//cutVarNames.push_back("dilepton mass cut = ");
	//cutVarNames.push_back("hcalIso cut for tracked endcap = ");
	//cutVarNames.push_back("ecalIso cut for tracked endcap = ");
	//cutVarNames.push_back("sigmaIEIE cut for tracked endcap = ");
	//cutVarNames.push_back("hadEm cut for tracked endcap = ");
	//cutVarNames.push_back("pt cut for tracked endcap = ");
	//cutVarNames.push_back("(1/E)-(1/P) cut for tracked endcap = ");
	//cutVarNames.push_back("deltaEta cut for tracked endcap = ");
	//cutVarNames.push_back("deltaPhi cut for tracked endcap = ");
	//cutVarNames.push_back("trackIso cut for tracked endcap = ");

	cutVarNames.push_back("hcalIso cut for tracked endcap = ");
	cutVarNames.push_back("ecalIso cut for tracked endcap = ");
	cutVarNames.push_back("sigmaIEIE cut for tracked endcap = ");
	cutVarNames.push_back("hadEm cut for tracked endcap = ");
	cutVarNames.push_back("pt cut for tracked endcap = ");
	cutVarNames.push_back("(1/E)-(1/P) cut for tracked endcap = ");
	cutVarNames.push_back("deltaEta cut for tracked endcap = ");
	cutVarNames.push_back("deltaPhi cut for tracked endcap = ");
	cutVarNames.push_back("trackIso cut for tracked endcap = ");

	//cutVarNames.push_back("hcalIso cut for trackless endcap = ");
	//cutVarNames.push_back("hadEm cut for trackless endcap = ");
	//cutVarNames.push_back("ecalIso cut for trackless endcap = ");
	//cutVarNames.push_back("sigmaIEIE cut for trackless endcap = ");
	//cutVarNames.push_back("pt cut for trackless endcap = ");
	


	std::vector<std::vector<Double_t>> cutInfo;
	//cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTracklessSignalChain,tracklessBkgndChain,">>tracklessSigdiObjectMassList","tracklessSigdiObjectMassList",">>tracklessBkgnddiObjectMassList","tracklessBkgnddiObjectMassList","diObjectMassHltEle>>tracklessSigdiObjectMass(150,0.,140.)","diObjectMassHltEle>>tracklessBkgnddiObjectMass(150,0.,140.)","tracklessSigdiObjectMass","tracklessBkgnddiObjectMass",140.,"optimal diObjectMass cut value"+plotTitleModifier,"diObjectMass","c4000",tracklessEEHltEta+hltMllAbsoluteLowerBound+genMllRange+hltDr+hltLowEt,tracklessEEHltEta+hltMllAbsoluteLowerBound+hltLowEt,"optimal_diObjectMass_cut_val_trackless.png",true,false,true));

	//std::vector<Double_t> findOptimalCutMaxSigMinBkgnd(TChain * sigChain,TChain * bkgndHighPtChain,TChain * bkgndLowPtChain,TString sigListFillArgs,TString sigListName,TString bkgndListFillArgs,TString bkgndListName,TString lowPtBkgndListFillArgs,TString lowPtBkgndListName,TString sigHistPlotArg,TString bkgndHighPtHistPlotArg,TString bkgndLowPtHistPlotArg,TString sigHistName,TString bkgndHighPtHistName,TString bkgndLowPtHistName,Double_t histCritVal,TString histTitle,TString xAxisTitle,TString canvName,TCut sigFilters,TCut bkgndFilters,TString outputFile,Bool_t isPlottingEnergy,Bool_t isPlottingInverseEnergy,Bool_t isLowerBound,Bool_t doCrossSxnNormalization, Double_t oldCutVal){

	//tracked endcap
	/*
	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSighcalIsoEndcapList","trackedSighcalIsoEndcapList",">>trackedBkgndhcalIsoEndcapList","trackedBkgndhcalIsoEndcapList",">>trackedLowPtBkgndhcalIsoEndcapList","trackedLowPtBkgndhcalIsoEndcapList","hcalIsoHltEle>>trackedSighcalIsoEndcap(100,-0.2,2.5)","hcalIsoHltEle>>trackedHighPtBkgndhcalIsoEndcap(100,-0.2,2.5)","hcalIsoHltEle>>trackedLowPtBkgndhcalIsoEndcap(100,-0.2,2.5)","trackedSighcalIsoEndcap","trackedHighPtBkgndhcalIsoEndcap","trackedLowPtBkgndhcalIsoEndcap",-0.2,"optimal hcalIso cut value for tracked leg endcap"+plotTitleModifier,"hcalIso/pt","c4001",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_hcalIso_cut_val_tracked_endcap.png",false,true,false,false,0.11));

	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigecalIsoEndcapList","trackedSigecalIsoEndcapList",">>trackedBkgndecalIsoEndcapList","trackedBkgndecalIsoEndcapList",">>trackedLowPtBkgndecalIsoEndcapList","trackedLowPtBkgndecalIsoEndcapList","ecalIsoHltEle>>trackedSigecalIsoEndcap(100,-0.2,2.5)","ecalIsoHltEle>>trackedHighPtBkgndecalIsoEndcap(100,-0.2,2.5)","ecalIsoHltEle>>trackedLowPtBkgndecalIsoEndcap(100,-0.2,2.5)","trackedSigecalIsoEndcap","trackedHighPtBkgndecalIsoEndcap","trackedLowPtBkgndecalIsoEndcap",-0.2,"optimal ecalIso cut value for tracked leg endcap"+plotTitleModifier,"ecalIso/pt","c4002",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_ecalIso_cut_val_tracked_endcap.png",false,true,false,false,0.11));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigclusterShapeEndcapList","trackedSigclusterShapeEndcapList",">>trackedBkgndclusterShapeEndcapList","trackedBkgndclusterShapeEndcapList",">>trackedLowPtBkgndclusterShapeEndcapList","trackedLowPtBkgndclusterShapeEndcapList","clusterShapeHltEle>>trackedSigclusterShapeEndcap(100,0.,0.09)","clusterShapeHltEle>>trackedHighPtBkgndclusterShapeEndcap(100,0.,0.09)","clusterShapeHltEle>>trackedLowPtBkgndclusterShapeEndcap(100,0.,0.09)","trackedSigclusterShapeEndcap","trackedHighPtBkgndclusterShapeEndcap","trackedLowPtBkgndclusterShapeEndcap",0.,"optimal #sigma_{i#eta i#eta} cut value for tracked leg endcap"+plotTitleModifier,"#sigma_{i#eta i#eta}","c4003",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_clusterShape_cut_val_tracked_endcap.png",false,false,false,false,0.031));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSighadEmEndcapList","trackedSighadEmEndcapList",">>trackedBkgndhadEmEndcapList","trackedBkgndhadEmEndcapList",">>trackedLowPtBkgndhadEmEndcapList","trackedLowPtBkgndhadEmEndcapList","hadEmHltEle>>trackedSighadEmEndcap(100,0.,2.5)","hadEmHltEle>>trackedHighPtBkgndhadEmEndcap(100,0.,2.5)","hadEmHltEle>>trackedLowPtBkgndhadEmEndcap(100,0.,2.5)","trackedSighadEmEndcap","trackedHighPtBkgndhadEmEndcap","trackedLowPtBkgndhadEmEndcap",0.,"optimal had/Em/energy cut value for tracked leg endcap"+plotTitleModifier,"had/Em/energy","c4004",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_hadEm_cut_val_tracked_endcap.png",false,true,false,false,0.075));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigptEndcapList","trackedSigptEndcapList",">>trackedBkgndptEndcapList","trackedBkgndptEndcapList",">>trackedLowPtBkgndptEndcapList","trackedLowPtBkgndptEndcapList","ptHltEle>>trackedSigptEndcap(100,0.,90.)","ptHltEle>>trackedHighPtBkgndptEndcap(100,0.,90.)","ptHltEle>>trackedLowPtBkgndptEndcap(100,0.,90.)","trackedSigptEndcap","trackedHighPtBkgndptEndcap","trackedLowPtBkgndptEndcap",90.,"optimal pt cut value for tracked leg endcap"+plotTitleModifier,"pt","c4005",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_pt_cut_val_tracked_endcap.png",true,false,true,false,27.));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigepEndcapList","trackedSigepEndcapList",">>trackedBkgndepEndcapList","trackedBkgndepEndcapList",">>trackedLowPtBkgndepEndcapList","trackedLowPtBkgndepEndcapList","epHltEle>>trackedSigepEndcap(100,0.,0.02)","epHltEle>>trackedHighPtBkgndepEndcap(100,0.,0.02)","epHltEle>>trackedLowPtBkgndepEndcap(100,0.,0.02)","trackedSigepEndcap","trackedHighPtBkgndepEndcap","trackedLowPtBkgndepEndcap",0.,"optimal (1/E)-(1/P) cut value for tracked leg endcap"+plotTitleModifier,"(1/E)-(1/P)","c4006",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_ep_cut_val_tracked_endcap.png",false,true,false,false,0.009));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigdEtaEndcapList","trackedSigdEtaEndcapList",">>trackedBkgnddEtaEndcapList","trackedBkgnddEtaEndcapList",">>trackedLowPtBkgnddEtaEndcapList","trackedLowPtBkgnddEtaEndcapList","dEtaHltEle>>trackedSigdEtaEndcap(100,0.,0.02)","dEtaHltEle>>trackedHighPtBkgnddEtaEndcap(100,0.,0.02)","dEtaHltEle>>trackedLowPtBkgnddEtaEndcap(100,0.,0.02)","trackedSigdEtaEndcap","trackedHighPtBkgnddEtaEndcap","trackedLowPtBkgnddEtaEndcap",0.,"optimal #Delta #eta cut value for tracked leg endcap"+plotTitleModifier,"#Delta #eta","c4007",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_dEta_cut_val_tracked_endcap.png",false,false,false,false,0.01));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigdPhiEndcapList","trackedSigdPhiEndcapList",">>trackedBkgnddPhiEndcapList","trackedBkgnddPhiEndcapList",">>trackedLowPtBkgnddPhiEndcapList","trackedLowPtBkgnddPhiEndcapList","dPhiHltEle>>trackedSigdPhiEndcap(100,0.,0.1)","dPhiHltEle>>trackedHighPtBkgnddPhiEndcap(100,0.,0.1)","dPhiHltEle>>trackedLowPtBkgnddPhiEndcap(100,0.,0.1)","trackedSigdPhiEndcap","trackedHighPtBkgnddPhiEndcap","trackedLowPtBkgnddPhiEndcap",0.,"optimal #Delta #phi cut value for tracked leg endcap"+plotTitleModifier,"#Delta #phi","c4008",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_dPhi_cut_val_tracked_endcap.png",false,false,false,false,0.03));

	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigtrackIsoEndcapList","trackedSigtrackIsoEndcapList",">>trackedBkgndtrackIsoEndcapList","trackedBkgndtrackIsoEndcapList",">>trackedLowPtBkgndtrackIsoEndcapList","trackedLowPtBkgndtrackIsoEndcapList","trackIsoHltEle>>trackedSigtrackIsoEndcap(100,0.,0.3)","trackIsoHltEle>>trackedHighPtBkgndtrackIsoEndcap(100,0.,0.3)","trackIsoHltEle>>trackedLowPtBkgndtrackIsoEndcap(100,0.,0.3)","trackedSigtrackIsoEndcap","trackedHighPtBkgndtrackIsoEndcap","trackedLowPtBkgndtrackIsoEndcap",0.,"optimal trackIso/pt cut value for tracked leg endcap"+plotTitleModifier,"trackIso/pt","c4009",trackedEEHltEta+hltLowEt+genMllRange+hltDr,trackedEEHltEta+hltLowEt,"optimal_trackIso_cut_val_tracked_endcap.png",false,true,false,false,0.125));
	*/

	//tracked barrel
	/*
	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSighcalIsoBarrelList","trackedSighcalIsoBarrelList",">>trackedBkgndhcalIsoBarrelList","trackedBkgndhcalIsoBarrelList",">>trackedLowPtBkgndhcalIsoBarrelList","trackedLowPtBkgndhcalIsoBarrelList","hcalIsoHltEle>>trackedSighcalIsoBarrel(100,-0.2,2.5)","hcalIsoHltEle>>trackedHighPtBkgndhcalIsoBarrel(100,-0.2,2.5)","hcalIsoHltEle>>trackedLowPtBkgndhcalIsoBarrel(100,-0.2,2.5)","trackedSighcalIsoBarrel","trackedHighPtBkgndhcalIsoBarrel","trackedLowPtBkgndhcalIsoBarrel",-0.2,"optimal hcalIso cut value for tracked leg barrel"+plotTitleModifier,"hcalIso/pt","c6001",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_hcalIso_cut_val_tracked_barrel.png",false,true,false,false,0.11));

	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigecalIsoBarrelList","trackedSigecalIsoBarrelList",">>trackedBkgndecalIsoBarrelList","trackedBkgndecalIsoBarrelList",">>trackedLowPtBkgndecalIsoBarrelList","trackedLowPtBkgndecalIsoBarrelList","ecalIsoHltEle>>trackedSigecalIsoBarrel(100,-0.2,2.5)","ecalIsoHltEle>>trackedHighPtBkgndecalIsoBarrel(100,-0.2,2.5)","ecalIsoHltEle>>trackedLowPtBkgndecalIsoBarrel(100,-0.2,2.5)","trackedSigecalIsoBarrel","trackedHighPtBkgndecalIsoBarrel","trackedLowPtBkgndecalIsoBarrel",-0.2,"optimal ecalIso cut value for tracked leg barrel"+plotTitleModifier,"ecalIso/pt","c6002",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_ecalIso_cut_val_tracked_barrel.png",false,true,false,false,0.16));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigclusterShapeBarrelList","trackedSigclusterShapeBarrelList",">>trackedBkgndclusterShapeBarrelList","trackedBkgndclusterShapeBarrelList",">>trackedLowPtBkgndclusterShapeBarrelList","trackedLowPtBkgndclusterShapeBarrelList","clusterShapeHltEle>>trackedSigclusterShapeBarrel(100,0.,0.09)","clusterShapeHltEle>>trackedHighPtBkgndclusterShapeBarrel(100,0.,0.09)","clusterShapeHltEle>>trackedLowPtBkgndclusterShapeBarrel(100,0.,0.09)","trackedSigclusterShapeBarrel","trackedHighPtBkgndclusterShapeBarrel","trackedLowPtBkgndclusterShapeBarrel",0.,"optimal #sigma_{i#eta i#eta} cut value for tracked leg barrel"+plotTitleModifier,"#sigma_{i#eta i#eta}","c6003",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_clusterShape_cut_val_tracked_barrel.png",false,false,false,false,0.011));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSighadEmBarrelList","trackedSighadEmBarrelList",">>trackedBkgndhadEmBarrelList","trackedBkgndhadEmBarrelList",">>trackedLowPtBkgndhadEmBarrelList","trackedLowPtBkgndhadEmBarrelList","hadEmHltEle>>trackedSighadEmBarrel(100,0.,2.5)","hadEmHltEle>>trackedHighPtBkgndhadEmBarrel(100,0.,2.5)","hadEmHltEle>>trackedLowPtBkgndhadEmBarrel(100,0.,2.5)","trackedSighadEmBarrel","trackedHighPtBkgndhadEmBarrel","trackedLowPtBkgndhadEmBarrel",0.,"optimal had/Em/energy cut value for tracked leg barrel"+plotTitleModifier,"had/Em/energy","c6004",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_hadEm_cut_val_tracked_barrel.png",false,true,false,false,0.1));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigptBarrelList","trackedSigptBarrelList",">>trackedBkgndptBarrelList","trackedBkgndptBarrelList",">>trackedLowPtBkgndptBarrelList","trackedLowPtBkgndptBarrelList","ptHltEle>>trackedSigptBarrel(100,0.,90.)","ptHltEle>>trackedHighPtBkgndptBarrel(100,0.,90.)","ptHltEle>>trackedLowPtBkgndptBarrel(100,0.,90.)","trackedSigptBarrel","trackedHighPtBkgndptBarrel","trackedLowPtBkgndptBarrel",90.,"optimal pt cut value for tracked leg barrel"+plotTitleModifier,"pt","c6005",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_pt_cut_val_tracked_barrel.png",true,false,true,false,27.));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigepBarrelList","trackedSigepBarrelList",">>trackedBkgndepBarrelList","trackedBkgndepBarrelList",">>trackedLowPtBkgndepBarrelList","trackedLowPtBkgndepBarrelList","epHltEle>>trackedSigepBarrel(100,0.,0.02)","epHltEle>>trackedHighPtBkgndepBarrel(100,0.,0.02)","epHltEle>>trackedLowPtBkgndepBarrel(100,0.,0.02)","trackedSigepBarrel","trackedHighPtBkgndepBarrel","trackedLowPtBkgndepBarrel",0.,"optimal (1/E)-(1/P) cut value for tracked leg barrel"+plotTitleModifier,"(1/E)-(1/P)","c6006",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_ep_cut_val_tracked_barrel.png",false,true,false,false,0.012));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigdEtaBarrelList","trackedSigdEtaBarrelList",">>trackedBkgnddEtaBarrelList","trackedBkgnddEtaBarrelList",">>trackedLowPtBkgnddEtaBarrelList","trackedLowPtBkgnddEtaBarrelList","dEtaHltEle>>trackedSigdEtaBarrel(100,0.,0.02)","dEtaHltEle>>trackedHighPtBkgnddEtaBarrel(100,0.,0.02)","dEtaHltEle>>trackedLowPtBkgnddEtaBarrel(100,0.,0.02)","trackedSigdEtaBarrel","trackedHighPtBkgnddEtaBarrel","trackedLowPtBkgnddEtaBarrel",0.,"optimal #Delta #eta cut value for tracked leg barrel"+plotTitleModifier,"#Delta #eta","c6007",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_dEta_cut_val_tracked_barrel.png",false,false,false,false,0.005));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigdPhiBarrelList","trackedSigdPhiBarrelList",">>trackedBkgnddPhiBarrelList","trackedBkgnddPhiBarrelList",">>trackedLowPtBkgnddPhiBarrelList","trackedLowPtBkgnddPhiBarrelList","dPhiHltEle>>trackedSigdPhiBarrel(100,0.,0.1)","dPhiHltEle>>trackedHighPtBkgnddPhiBarrel(100,0.,0.1)","dPhiHltEle>>trackedLowPtBkgnddPhiBarrel(100,0.,0.1)","trackedSigdPhiBarrel","trackedHighPtBkgnddPhiBarrel","trackedLowPtBkgnddPhiBarrel",0.,"optimal #Delta #phi cut value for tracked leg barrel"+plotTitleModifier,"#Delta #phi","c6008",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_dPhi_cut_val_tracked_barrel.png",false,false,false,false,0.03));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTrackedSignalChain,trackedHighPtBkgndChain,trackedLowPtBkgndChain,">>trackedSigtrackIsoBarrelList","trackedSigtrackIsoBarrelList",">>trackedBkgndtrackIsoBarrelList","trackedBkgndtrackIsoBarrelList",">>trackedLowPtBkgndtrackIsoBarrelList","trackedLowPtBkgndtrackIsoBarrelList","trackIsoHltEle>>trackedSigtrackIsoBarrel(100,0.,0.3)","trackIsoHltEle>>trackedHighPtBkgndtrackIsoBarrel(100,0.,0.3)","trackIsoHltEle>>trackedLowPtBkgndtrackIsoBarrel(100,0.,0.3)","trackedSigtrackIsoBarrel","trackedHighPtBkgndtrackIsoBarrel","trackedLowPtBkgndtrackIsoBarrel",0.,"optimal trackIso/pt cut value for tracked leg barrel"+plotTitleModifier,"trackIso/pt","c6009",trackedEBHltEta+hltLowEt+genMllRange+hltDr,trackedEBHltEta+hltLowEt,"optimal_trackIso_cut_val_tracked_barrel.png",false,true,false,false,0.125));
	*/

	//trackless endcap
	/*
	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTracklessSignalChain,tracklessHighPtBkgndChain,tracklessLowPtBkgndChain,">>tracklessSighcalIsoEndcapList","tracklessSighcalIsoEndcapList",">>tracklessBkgndhcalIsoEndcapList","tracklessBkgndhcalIsoEndcapList",">>tracklessLowPtBkgndhcalIsoEndcapList","tracklessLowPtBkgndhcalIsoEndcapList","hcalIsoHltEle>>tracklessSighcalIsoEndcap(100,-0.2,3.5)","hcalIsoHltEle>>tracklessHighPtBkgndhcalIsoEndcap(100,-0.2,3.5)","hcalIsoHltEle>>tracklessLowPtBkgndhcalIsoEndcap(100,-0.2,3.5)","tracklessSighcalIsoEndcap","tracklessHighPtBkgndhcalIsoEndcap","tracklessLowPtBkgndhcalIsoEndcap",-0.2,"optimal hcalIso/pt cut value for trackless leg endcap"+plotTitleModifier,"hcalIso/pt","c5001",tracklessEEHltEta+hltLowEt+genMllRange+hltDr,tracklessEEHltEta+hltLowEt,"optimal_hcalIso_cut_val_trackless_endcap.png",false,true,false,false,0.2));

	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTracklessSignalChain,tracklessHighPtBkgndChain,tracklessLowPtBkgndChain,">>tracklessSighadEmEndcapList","tracklessSighadEmEndcapList",">>tracklessBkgndhadEmEndcapList","tracklessBkgndhadEmEndcapList",">>tracklessLowPtBkgndhadEmEndcapList","tracklessLowPtBkgndhadEmEndcapList","hadEmHltEle>>tracklessSighadEmEndcap(100,0.,1.5)","hadEmHltEle>>tracklessHighPtBkgndhadEmEndcap(100,0.,1.5)","hadEmHltEle>>tracklessLowPtBkgndhadEmEndcap(100,0.,1.5)","tracklessSighadEmEndcap","tracklessHighPtBkgndhadEmEndcap","tracklessLowPtBkgndhadEmEndcap",0.,"optimal had/Em/energy cut value for trackless leg endcap"+plotTitleModifier,"had/Em/energy","c5002",tracklessEEHltEta+hltLowEt+genMllRange+hltDr,tracklessEEHltEta+hltLowEt,"optimal_hadEm_cut_val_trackless_endcap.png",false,true,false,false,0.075));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTracklessSignalChain,tracklessHighPtBkgndChain,tracklessLowPtBkgndChain,">>tracklessSigecalIsoEndcapList","tracklessSigecalIsoEndcapList",">>tracklessBkgndecalIsoEndcapList","tracklessBkgndecalIsoEndcapList",">>tracklessLowPtBkgndecalIsoEndcapList","tracklessLowPtBkgndecalIsoEndcapList","ecalIsoHltEle>>tracklessSigecalIsoEndcap(100,-0.2,2.5)","ecalIsoHltEle>>tracklessHighPtBkgndecalIsoEndcap(100,-0.2,2.5)","ecalIsoHltEle>>tracklessLowPtBkgndecalIsoEndcap(100,-0.2,2.5)","tracklessSigecalIsoEndcap","tracklessHighPtBkgndecalIsoEndcap","tracklessLowPtBkgndecalIsoEndcap",-0.2,"optimal ecalIso/pt cut value for trackless leg endcap"+plotTitleModifier,"ecalIso/pt","c5003",tracklessEEHltEta+hltLowEt+genMllRange+hltDr,tracklessEEHltEta+hltLowEt,"optimal_ecalIso_cut_val_trackless_endcap.png",false,true,false,false,0.2));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTracklessSignalChain,tracklessHighPtBkgndChain,tracklessLowPtBkgndChain,">>tracklessSigclusterShapeEndcapList","tracklessSigclusterShapeEndcapList",">>tracklessBkgndclusterShapeEndcapList","tracklessBkgndclusterShapeEndcapList",">>tracklessLowPtBkgndclusterShapeEndcapList","tracklessLowPtBkgndclusterShapeEndcapList","clusterShapeHltEle>>tracklessSigclusterShapeEndcap(100,0.,0.1)","clusterShapeHltEle>>tracklessHighPtBkgndclusterShapeEndcap(100,0.,0.1)","clusterShapeHltEle>>tracklessLowPtBkgndclusterShapeEndcap(100,0.,0.1)","tracklessSigclusterShapeEndcap","tracklessHighPtBkgndclusterShapeEndcap","tracklessLowPtBkgndclusterShapeEndcap",0.,"optimal #sigma_{i#eta i#eta} cut value for trackless leg endcap"+plotTitleModifier,"#sigma_{i#eta i#eta}","c5004",tracklessEEHltEta+hltLowEt+genMllRange+hltDr,tracklessEEHltEta+hltLowEt,"optimal_clusterShape_cut_val_trackless_endcap.png",false,false,false,false,0.031));


	cutInfo.push_back(findOptimalCutMaxSigMinBkgnd(matchedTracklessSignalChain,tracklessHighPtBkgndChain,tracklessLowPtBkgndChain,">>tracklessSigptEndcapList","tracklessSigptEndcapList",">>tracklessBkgndptEndcapList","tracklessBkgndptEndcapList",">>tracklessLowPtBkgndptEndcapList","tracklessLowPtBkgndptEndcapList","ptHltEle>>tracklessSigptEndcap(100,0.,80.)","ptHltEle>>tracklessHighPtBkgndptEndcap(100,0.,80.)","ptHltEle>>tracklessLowPtBkgndptEndcap(100,0.,80.)","tracklessSigptEndcap","tracklessHighPtBkgndptEndcap","tracklessLowPtBkgndptEndcap",80.,"optimal pt cut value for trackless leg endcap"+plotTitleModifier,"pt","c5005",tracklessEEHltEta+hltLowEt+genMllRange+hltDr,tracklessEEHltEta+hltLowEt,"optimal_pt_cut_val_trackless_endcap.png",true,false,true,false,15.));



	for(unsigned int j=0; j<cutInfo.size(); j++){
		for(unsigned int h=0; h<cutInfo[j].size(); h++){
			if(h==0) std::cout<< cutVarNames[j] << cutInfo[j][h] <<std::endl;
			if(h==1) std::cout<<"signal efficiency = " << cutInfo[j][h] <<std::endl;
			if(h==2) std::cout<<"bkgnd survival = " << cutInfo[j][h] <<std::endl;
		}
	}//end loop which prints all cut values which were determined using the simple algorithm (no correlations taken into account)

	*/

}//end testMacro()


