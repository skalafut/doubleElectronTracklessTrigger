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
#include <vector>
#include <cstring>
#include <string>

TCut buildCutObject(TString tupleVarName, Bool_t doLessThan, Float_t cutVal){
	TString cutString = tupleVarName;
	if(doLessThan){
		TString filter = "<";
		cutString.Append(filter);
		TString threshold = "";
		threshold += cutVal;
		cutString.Append(threshold);
		std::cout<< cutString <<std::endl;
	}//end if(doLessThan)

	else{
		TString filter = ">";
		cutString.Append(filter);
		TString threshold = "";
		threshold += cutVal;
		cutString.Append(threshold);
		std::cout<< cutString <<std::endl;
	}
	TCut theCut(cutString);
	return theCut;

}//end buildCutObject()

/*
findOptimalCutsRateAndEff(Float_t desiredRate, Float_t effDenom, Float_t minEtCut, Float_t maxEtCut,  Float_t minSigmaIEIECut, Float_t maxSigmaIEIECut, Float_t minEcalIsoCut, Float_t maxEcalIsoCut, Float_t minHoverECut, Float_t maxHoverECut, Float_t minHcalIsoCut, Float_t maxHcalIsoCut, TChain * lowPtBkgndTuple,Float_t totalBkgndEvtsLowPt, TChain * highPtBkgndTuple, Float_t totalBkgndEvtsHighPt, TChain * matchedSigTuple, TChain * sigTuple, Float_t totalSigEvts,TCut bkgndFilters, TCut sigFilters){
	//use minEtCut, maxEtCut, minSigmaIEIECut, maxSigmaIEIECut, etc to make and fill sorted vectors
	//of float values (sorted low to high or high to low).  These vectors hold cut values of pt,
	//sigmaIEIE, relative ecalIso, etc used to filter evts.  The pt vector is sorted from low to high,
	//and the other four vectors are sorted from high to low.
	//the vectors should be named sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr
	//and sortedHcalIsoCutArr
	std::vector<Float_t> sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr;
	Float_t EtStep = ((maxEtCut - minEtCut)/100);
	Float_t SigmaIEIEStep = ((maxSigmaIEIECut - minSigmaIEIECut)/100);
	Float_t EcalIsoStep = ((maxEcalIsoCut - minEcalIsoCut)/100);
	Float_t HoverEStep = ((maxHoverECut - minHoverECut)/100);
	Float_t HcalIsoStep = ((maxHcalIsoCut - minHcalIsoCut)/100);
	for(Int_t j=0;j<100;j++){
		sortedEtCutArr.push_back(minEtCut + j*EtStep);
		sortedSigmaIEIECutArr.push_back(minSigmaIEIECut + j*SigmaIEIEStep);
		sortedEcalIsoCutArr.push_back(minEcalIsoCut + j*EcalIsoStep);
		sortedHoverECutArr.push_back(minHoverECut + j*HoverEStep);
		sortedHcalIsoCutArr.push_back(minHcalIsoCut + j*HcalIsoStep);
	}//end loop which fills cut arrays


	
	//calculate peak luminosity and cross sxns of signal and bkgnd (all needed for rate)
	Float_t peakLumi = (0.9)*(TMath::Power(10.,34));
	Float_t signalXSxn = (6960)*(TMath::Power(10.,-36));
	Float_t lowPtXSxn = (677300000*0.01029)*(TMath::Power(10.,-36));
	Float_t highPtXSxn = (185900000*0.06071)*(TMath::Power(10.,-36));
	
	//make a vector whose elements are vectors of Float_t vals
	std::vector<std::vector<Float_t>> cutsRatesAndEffs;
	Int_t addedElementToCutsRatesEffs = 0;
	Float_t totalRate = -0.01;

	//make two 2D vectors which contain the # of low pt and high pt QCD bkgnd evts passing the trigger (first element)
	//and the corresponding bkgnd trigger rate (second element)
	//sorted from high to low
	std::vector<std::vector<Float_t>> lowPtBkgndEvtsAndRate;
	for(Float_t s=0;s<lowPtBkgndTuple->GetEntries();s++){
		Float_t rate = ((lowPtXSxn)*(peakLumi)*(lowPtBkgndTuple->GetEntries()-s)/totalBkgndEvtsLowPt);
		std::vector<Float_t> evtsRate;
		evtsRate.push_back(lowPtBkgndTuple->GetEntries()-s);
		evtsRate.push_back(rate);
		lowPtBkgndEvtsAndRate.push_back(evtsRate);
	}
	std::vector<Float_t> quickLowPt;
	quickLowPt.push_back(0.);
	quickLowPt.push_back(0.);
	lowPtBkgndEvtsAndRate.push_back(quickLowPt);


	std::vector<std::vector<Float_t>> highPtBkgndEvtsAndRate;
	for(Float_t s=0;s<highPtBkgndTuple->GetEntries();s++){
		Float_t rate = ((highPtXSxn)*(peakLumi)*(highPtBkgndTuple->GetEntries()-s)/totalBkgndEvtsLowPt);
		std::vector<Float_t> evtsRate;
		evtsRate.push_back(highPtBkgndTuple->GetEntries()-s);
		evtsRate.push_back(rate);
		highPtBkgndEvtsAndRate.push_back(evtsRate);
	}
	std::vector<Float_t> quickHighPt;
	quickHighPt.push_back(0.);
	quickHighPt.push_back(0.);
	highPtBkgndEvtsAndRate.push_back(quickHighPt);

	//there will be several sets of (pt,sigmaIEIE,ecalIso,hadEm,hcalIso) cuts which will yield
	//a reasonable number of bkgnd evts passing the trigger (and thus a reasonable total trigger rate)
	//save each set of five cut values into a 5D vector, and loop over these sets of cut vals
	//in the second system of nested for loops
	std::vector<std::vector<Float_t>> allSetsOfInitialVals;
	Bool_t foundASet = false;
	Int_t numEntriesInAllSets = 0;

	//call chain->SetEntryList(0) to remove all of selection criteria
	Int_t maxRange = 10;
	Long64_t multiplier = (matchedSigTuple->GetEntries()/maxRange);
	for(Float_t z=0;z<sortedEtCutArr.size();z++){
		if(multiplier*z >= sortedEtCutArr.size()) break;

	}//end loop over pt cut vals

	//boolean vars used to speed up optimization
	Bool_t leftHcalIso = false;
	Bool_t leaveEcalIso = false;
	Bool_t leaveSigmaIEIE = false;
	Bool_t increasHcalIsoIterator = false;
	Bool_t magnifyHcalIsoIterator = false;

}//end findOptimalCutsRateAndEff()
*/

void triggerOptimization(){
	buildCutObject("test",true,0.150000);
	buildCutObject("trial",false,2.10000);

}//end triggerOptimization()



