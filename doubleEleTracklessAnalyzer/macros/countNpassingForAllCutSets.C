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

/**use this function to fill two vectors with _nPassing and _nEvents values, and write those vectors
 * elements and corresponding sets of cut values into a new TTree
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

	//void iterateOverFilesAndEntries(TChain * chain, vector<ULong64_t>& numPassing, vector<ULong64_t>& maxNumPassing)
	iterateOverFilesAndEntries(highPtChain,nHighPtBkgndPassing,nHighPtBkgndMaxPassing);
	
	/*
	///loop over the list of bkgnd and signal files
	///calling fileItr->GetTitle() returns the absolute path name of the file
	///See the TChain constructor for more details
	TObjArray * fileElems = highPtChain->GetListOfFiles();
	TIter fileItr(fileElems);
	ULong64_t numEvtsPassing=0, maxNumEvtsPassing=0;		///these will be saved in the vectors declared above
	for(TFile * aFile = (TFile*) fileItr.Next(); aFile != NULL; aFile = (TFile*) fileItr.Next()){
		///tempChain will only contain one file
		TChain * tempChain = new TChain("scanned_tree","");
#ifdef DEBUG
		cout <<"file name is \t"<< aFile->GetTitle() << endl;
#endif
		tempChain->Add(aFile->GetTitle());
#ifdef DEBUG
		cout<<"there are \t"<< tempChain->GetEntries() <<"\t evts in the chain"<<endl;
#endif
		if(nHighPtBkgndPassing.size()==0){
			for(Long64_t entr=0; entr<tempChain->GetEntries(); entr++){
				nHighPtBkgndPassing.push_back(0);
				nHighPtBkgndMaxPassing.push_back(0);
			}///end loop which fills two vectors of Long64_t with lots of elements, all equal to zero
		}///end check that the vector of Long64_t has more than zero elements 
		tempChain->SetBranchAddress("_nPassing",&numEvtsPassing);
		tempChain->SetBranchAddress("_nEvents",&maxNumEvtsPassing);

		///now loop over every entry in the file, and add _nPassing to the appropriate vector declared above
		for(Long64_t evt=0; evt<tempChain->GetEntries(); evt++){
			tempChain->GetEntry(evt);
			nHighPtBkgndPassing[evt]+=numEvtsPassing;
			nHighPtBkgndMaxPassing[evt]+=maxNumEvtsPassing;
		}///end loop over different sets of cut values in tempChain

	}///end loop over files in TChain
	*/



}///end countNpassingForAllCutSets()

