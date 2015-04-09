#include <TFile.h>
#include <TTree.h>
#include <TChain.h>
#include <TObjArray.h>
#include "TCollection.h"
#include <TCut.h>
#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#define DEBUG

using namespace std;

/**use this function to identify a few sets of cut values which yield good Z->ee trigger efficiency
 * and total rate
 * the same string keys are used in all of the maps which are passed as inputs to this fxn
 * the total rate returned by this function will only represent the rate due to bkgnd evts
 * I should use testMacro.C to calculate the total rate, including signal evts
 */ 
vector<map<string,Float_t> > findOptimalCutSets(Float_t desiredRate, string signalKey, map<string,vector<ULong64_t> >& numPassingMap, 
		map<string,vector<ULong64_t> >& maxNumPassingMap, TChain * templateChain, map<string,vector<Float_t> >& bkgndXsxnsAndLumi){
	///calculate the rate for every entry in numPassingMap with a bkgnd key
	vector<Float_t> rateVector;
	vector<Float_t> efficiencyVector;
	
	///fill rateVector with lots of elements, all equal to zero
	///the number of entries in templateChain is equal to the number of elements in all of the vector<ULong64_t> objects in numPassingMap
	for(Long64_t entries=0; entries<templateChain->GetEntries(); entries++){
		rateVector.push_back(0);
		efficiencyVector.push_back(0);
	}///end loop to initialize values in rateVector
	
	///now calculate the rate
	for(map<string,vector<ULong64_t> >::const_iterator numPassIt=numPassingMap.begin(); numPassIt!=numPassingMap.end(); numPassIt++){
		if((numPassIt->first).compare(signalKey) == 0) continue;	///<skip the map entry associated with the signal
		Float_t lumi = bkgndXsxnsAndLumi[numPassIt->first][0];
		Float_t xSxn = bkgndXsxnsAndLumi[numPassIt->first][1];
		Float_t nEvtsInSample = bkgndXsxnsAndLumi[numPassIt->first][2];

#ifdef DEBUG
		cout<<"lumi = "<< lumi << "\t"<<"xSxn = "<<xSxn <<"\t"<<"total num evts = "<< nEvtsInSample <<endl;
		cout<<"the number of different cut sets = \t"<< (numPassIt->second).size() << endl;
		cout<<"\t"<<endl;
#endif

		for(ULong64_t ind=0; ind<(numPassIt->second).size(); ind++){
			///multiply the number of passing evts by the lumi and X sxn, and divide by the total number of evts in the sample
			///store this number in rateVector
			rateVector[ind] += (Float_t) ((numPassIt->second)[ind])*lumi*xSxn/(nEvtsInSample);
		}///end loop over elements in numPassingMap vector tied to a specific bkgnd source
	}///end loop over different bkgnds

	///now the total rate, counting all bkgnd sources, is known for every unique set of cut values
	///now calculate the Z->ee trigger efficiency for each unique set of cut vals, and store these efficiencies in a vector
	for(ULong64_t index=0; index<(numPassingMap[signalKey]->second).size(); index++){
		Float_t nPass = (Float_t) (numPassingMap[signalKey]->second)[index];
		Float_t nPossible = (Float_t) (maxNumPassingMap[signalKey]->second)[index];
#ifdef DEBUG
		if(index<8) cout<<"num sig evts passing = \t"<<nPass<<endl;
		if(index<8) cout<<"max num sig evts passing = \t"<<nPossible<<endl;
		if(index<8) cout<<"\t"<<endl;
#endif
		
		if(nPossible>0) efficiencyVector[index] += nPass/nPossible;
	}///end loop which calculates the Z->ee trigger efficiency for each unique set of cuts

	///now we know the total rate and Z->ee trigger efficiency for all sets of cut values
	///find the 5 sets of cuts which maximize Z->ee trigger efficiency and yield a trigger rate <= desiredRate
	

}///end findOptimalCutSets()

/**use this function to fill two vectors with _nPassing and _nEvents values
 * if the first entry of _nEvents is different from the second, then reset the first element in the vector
 * of _nEvents to match the second element in the same vector
 * numPassing will be filled with values of _nPassing
 * maxNumPassing will be filled with values of _nEvents 
 */
void iterateOverFilesAndEntries(TChain * chain, vector<ULong64_t>& numPassing, vector<ULong64_t>& maxNumPassing){
	TObjArray * fileElems = chain->GetListOfFiles();
	TIter fileItr(fileElems);
	ULong64_t numEvtsPassing=0, maxNumEvtsPassing=0;
	for(TFile * aFile = (TFile*) fileItr.Next(); aFile!=NULL; aFile=(TFile*) fileItr.Next()){
		TChain * tempChain = new TChain("scanned_tree","");
		tempChain->Add(aFile->GetTitle());
		if(numPassing.size()==0){
			for(Long64_t entr=0; entr<tempChain->GetEntries(); entr++){
				numPassing.push_back(0);
				maxNumPassing.push_back(0);
			}///end loop which fills two vectors of Long64_t with lots of elements, all equal to zero
		}///end check that the vector of Long64_t has more than zero elements 
		tempChain->SetBranchAddress("_nPassing",&numEvtsPassing);
		tempChain->SetBranchAddress("_nEvents",&maxNumEvtsPassing);

		///now loop over every entry in the file, and add _nPassing to the appropriate vector declared above
		for(Long64_t evt=0; evt<tempChain->GetEntries(); evt++){
			tempChain->GetEntry(evt);
			numPassing[evt]+=numEvtsPassing;
			maxNumPassing[evt]+=maxNumEvtsPassing;
		}///end loop over different sets of cut values in tempChain
		
		///the first entry of _nEvents in every bkgnd scan file is enormous, and not consistent with the other entries
		///this if() statement fixes this problem for each bkgnd scan file
		if(maxNumPassing.size()>1 && maxNumPassing[0] != maxNumPassing[1]){
			///the first entry of _nEvents is messed up, reset it to the correct value
			maxNumPassing[0] = maxNumPassing[1];
		}///end if(first element in maxNumPassing is different from all other elements)

#ifdef DEBUG
		cout<<"looked at \t"<<tempChain->GetEntries()<<"\t entries in a chain"<<endl;
		cout<<"there are \t"<<numPassing.size()<<"\t elements in numPassing vector"<<endl;
		for(unsigned int i=0; i<10;i++){
			cout<< numPassing[i] <<"\t evts out of \t" << maxNumPassing[i] <<"\t evts passed a set of cuts"<< endl;
		}///end loop over 10 elements in input vector<ULong64_t> objects
#endif


	}///end loop over files in input chain

}///end iterateOverFilesAndEntries()

/**this macro, another marvelous creation inspired by discussions with Shervin, takes
 * the tuples created by the scan jobs and counts the number of events which passed each set of cuts.
 * Every tuple created by a scan job has the same number of entries.  Each entry in one of these
 * tuples corresponds to a unique set of cut values.  In addition, the order of these cut values is
 * identical in every tuple.  Thus, to count the number of events which pass every unique set of cuts,
 * I simply need to loop over all scan output tuple files, and for each tuple save _nPassing in a
 * vector whose index corresponds to the evt number.
 *
 * loop over all tuple files, then for each tuple file loop over all entries in the tuple.
 */
void countNpassingForAllCutSets(){
	vector<ULong64_t> nSignalPassing;	///number of matched signal evts which pass different sets of cuts
	vector<ULong64_t> nSignalMaxPassing;	///max number of matched signal evts which could have passed a set of cuts 
	vector<ULong64_t> nHighPtBkgndPassing;	///number of high pt bkgnd evts which pass different sets of cuts
	vector<ULong64_t> nHighPtBkgndMaxPassing;	///max number of high pt bkgnd evts which could have passed a set of cuts 
	vector<ULong64_t> nLowPtBkgndPassing;	///number of low pt bkgnd evts which pass different sets of cuts
	vector<ULong64_t> nLowPtBkgndMaxPassing;	///max number of low pt bkgnd evts which could have passed a set of cuts 
	
	///make three TChains, each with access to the entire directory of signal OR high pt bkgnd OR low pt bkgnd tuples
	///use the TChain method GetFile, and finally call GetName() to get the name of the file
	///use this file name to make a TFile object, and loop over the entries in this file
	string signalPath = "/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/scanned_tuples/scanned_signal_tree_*";
	string highPtPath = "/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_high_pt/scanned_tuples/scanned_high_pt_bkgnd_tree_*";
	string lowPtPath = "/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_high_pt/scanned_tuples/scanned_low_pt_bkgnd_tree_*";
	if(signalPath.empty() || highPtPath.empty() || lowPtPath.empty()){
		cout<<"where are the scanned tuples?"<<endl;
		return;
	}
	TChain * sigChain = new TChain("scanned_tree","");
	sigChain->Add(signalPath.c_str());
	TChain * highPtChain = new TChain("scanned_tree","");
	highPtChain->Add(highPtPath.c_str());
	TChain * lowPtChain = new TChain("scanned_tree","");
	lowPtChain->Add(lowPtPath.c_str());

	iterateOverFilesAndEntries(sigChain,nSignalPassing,nSignalMaxPassing);
	iterateOverFilesAndEntries(highPtChain,nHighPtBkgndPassing,nHighPtBkgndMaxPassing);
	iterateOverFilesAndEntries(lowPtChain,nLowPtBkgndPassing,nLowPtBkgndMaxPassing);

	///now vectors of _nPassing and _nEvents are filled, so the trigger rate and Z->ee trigger
	///efficiencies can be calculated
	
	//map<string,Float_t> findOptimalCutSets(Float_t desiredRate, string signalKey, map<string,vector<ULong64_t> >& numPassingMap, 
	//	map<string,vector<ULong64_t> >& maxNumPassingMap, TChain * templateChain, map<string,vector<Float_t> >& bkgndXsxnsAndLumi)


	///declare quantities needed for findOptimalCutSets()
	Float_t targetRate = 2.5;
	map<string,vector<ULong64_t> > nPassingMap, nEventsMap;
	string sigKey = "signal", lowPtKey = "lowPtBkgnd", highPtKey = "highPtBkgnd";
	nPassingMap[sigKey]=nSignalPassing;
	nPassingMap[lowPtKey]=nLowPtBkgndPassing;
	nPassingMap[highPtKey]=nHighPtBkgndPassing;
	nEventsMap[sigKey]=nSignalMaxPassing;
	nEventsMap[lowPtKey]=nLowPtBkgndMaxPassing;
	nEventsMap[highPtKey]=nHighPtBkgndMaxPassing;
	TChain * chainForCuts = new TChain("scanned_tree","");
	chainForCuts->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/scanned_tuples/scanned_signal_tree_4.root");
	map<string,vector<Float_t> > lumiAndXsxns;
	vector<Float_t> forHighPt, forLowPt;	///<first element = lumi, second element = cross section, third element = total number evts analyzed
	Float_t highPtBkgndEvts = 740502, lowPtBkgndEvts = 608199;
	forHighPt.push_back((0.9)*pow(10.,34));
	forHighPt.push_back((185900000*0.06071)*pow(10.,-36));
	forHighPt.push_back(highPtBkgndEvts);
	forLowPt.push_back((0.9)*pow(10.,34));
	forLowPt.push_back((677300000*0.01029)*pow(10.,-36));
	forLowPt.push_back(lowPtBkgndEvts);
	lumiAndXsxns[lowPtKey]=forLowPt;
	lumiAndXsxns[highPtKey]=forHighPt;

	vector<map<string,Float_t> > interestingCutSets = findOptimalCutSets(targetRate, sigKey, nPassingMap, nEventsMap, chainForCuts, lumiAndXsxns);


}///end countNpassingForAllCutSets()

