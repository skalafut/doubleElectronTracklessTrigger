#include <TFile.h>
#include <TBranch.h>
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
#include <map>

#define OUTPUTNELE 1
//#define DEBUG

using namespace std;


/**use this function to fill two vectors with _nPassing and _nEvents values, and save the cumulative
 * _nPassing and _nEvents values to a new tree
 * if the first entry of _nEvents is different from the second, then reset the first element in the vector
 * of _nEvents to match the second element in the same vector
 * numPassing will be filled with values of _nPassing
 * maxNumPassing will be filled with values of _nEvents
 * this fxn is called once for every unique signal and bkgnd source, so there is no need to pass 
 * map<string,vector<Float_t> > objects as inputs to this fxn
 */
void iterateOverFilesAndEntries(TChain * chain, vector<ULong64_t>& numPassing, vector<ULong64_t>& maxNumPassing, string treeIDTag, string outputFileName, Float_t genEff, Float_t recoEff, Float_t lumiTimesXsxn){
	string newTreeName = "master_scanned_tree_"+treeIDTag;
	TFile * outputFile = new TFile(outputFileName.c_str(),"recreate");
	outputFile->cd();
	TTree * outputTree = new TTree(newTreeName.c_str(),"");  ///< this tree will have the same structure as tempChain, but with two additional branches
	TObjArray * fileElems = chain->GetListOfFiles();
	TIter fileItr(fileElems);
	ULong64_t numEvtsPassing=0, maxNumEvtsPassing=0;
	vector<map<string,Float_t[OUTPUTNELE]> > cutBranchesMapVector;		///< branches in tempChain which are tied to cut variables
	map<string,Float_t[OUTPUTNELE]> cutBranchesMap;

	Long_t index=-1;	///< use this to fill cutBranchesMapVector once, only for the first file in the list of files
   	Long64_t maxEntries=0;
	for(TFile * aFile = (TFile*) fileItr.Next(); aFile!=NULL; aFile=(TFile*) fileItr.Next()){
		index++;
		TChain * tempChain = new TChain("scanned_tree","");
		tempChain->Add(aFile->GetTitle());
		maxEntries = tempChain->GetEntries();
		
		///all of the code within numPassing.size()==0 will only be executed once per call of iterateOverFilesAndEntries()
		///the vector numPassing will only be zero when no file has been read in 
		if(numPassing.size()==0){
			TObjArray * branches = tempChain->GetListOfBranches();
			TIter brItr(branches);
			for(TBranch * aBranch=(TBranch*) brItr.Next(); aBranch!=NULL; aBranch=(TBranch*) brItr.Next()){
				string brName = aBranch->GetName();
#ifdef DEBUG
				cout<<"branch name = \t"<< brName <<endl;
#endif
				if(brName.compare("_nPassing")==0 || brName.compare("_nEvents")==0) continue;	///skip the branches which do not have Float_t arrays
				for(unsigned int i=0; i<OUTPUTNELE; i++){
					cutBranchesMap[brName][i]=0;
				}///end loop which initializes values in Float_t array in tempMap
			}///end loop over branches in tempChain to initialize keys and values in cutBranchesMap


			for(Long64_t entr=0; entr<maxEntries; entr++){
				numPassing.push_back(0);
				maxNumPassing.push_back(0);
			}///end loop which fills two vectors of Long64_t with lots of elements, all equal to zero

		}///end check that the vector of Long64_t has more than zero elements
		
		tempChain->SetBranchAddress("_nPassing",&numEvtsPassing);
		tempChain->SetBranchAddress("_nEvents",&maxNumEvtsPassing);
		for(map<string,Float_t[OUTPUTNELE]>::iterator mapIt=cutBranchesMap.begin(); mapIt!=cutBranchesMap.end(); mapIt++){
			///link the Float_t arrays in cutBranchesMap to branches in tempChain
			tempChain->SetBranchAddress((mapIt->first).c_str(), &(mapIt->second));
		}///end loop to link elements in cutBranchesMap to branches in tempChain

		///now loop over every entry in the file, and add _nPassing to the appropriate vector declared above
		for(Long64_t evt=0; evt<maxEntries; evt++){
			tempChain->GetEntry(evt);
			numPassing[evt]+=numEvtsPassing;
			maxNumPassing[evt]+=maxNumEvtsPassing;
			if(index==0) cutBranchesMapVector.push_back(cutBranchesMap);
		}///end loop over different sets of cut values in tempChain
		
		///the first entry of _nEvents in every bkgnd scan file, and some signal scan files, is enormous, 
		///and not consistent with the other entries
		///this if() statement fixes this problem for each bkgnd scan file
		if(maxNumPassing.size()>1 && maxNumPassing[0] != maxNumPassing[1]){
			///the first entry of _nEvents is messed up, reset it to the correct value
			maxNumPassing[0] = maxNumPassing[1];
		}///end if(first element in maxNumPassing is different from all other elements)

		///the first entry of _nPassing in some signal scan files is enormous, and not consistent with
		///subsequent entries of _nPassing in the same file or with _nEvents in the same entry.
		///This if statement remedies this problem.
		if(numPassing.size()>1 && numPassing[0] > maxNumPassing[0]){
			///this is not the correct value, but it will suffice for now
			///the first entry in the tree has looser cuts than the second entry, so
			///at worst the first entry in _nPassing (numPassing[0]) will be equal to the second entry
			///in _nPassing (numPassing[1])
			numPassing[0] = numPassing[1];
		}

#ifdef DEBUG
		cout<<"looked at \t"<<maxEntries<<"\t entries in a chain"<<endl;
		cout<<"there are \t"<<numPassing.size()<<"\t elements in numPassing vector"<<endl;
		for(unsigned int i=0; i<10;i++){
			cout<< numPassing[i] <<"\t evts out of \t" << maxNumPassing[i] <<"\t evts passed a set of cuts"<< endl;
		}///end loop over 10 elements in input vector<ULong64_t> objects
#endif

	}///end loop over files in input chain

	///now declare two ULong64_t vars, many Float_t[OUTPUTNELE] vars, one Float_t var, and link these vars to branches in outputTree
	ULong64_t totalNumPassing=0, totalMaxNumPassing=0;
	Float_t rate=0;		///< write this into a new branch in the output tree
   	map<string,Float_t[OUTPUTNELE]> floatArrayBranchesMap;
	for(map<string,Float_t[OUTPUTNELE]>::iterator mapIt=cutBranchesMap.begin(); mapIt!=cutBranchesMap.end(); mapIt++){
		for(unsigned int i=0; i<OUTPUTNELE; i++){
			floatArrayBranchesMap[mapIt->first][i]=0;
		}
	}///end loop over elements in cutBranchesMap declared above
	for(map<string,Float_t[OUTPUTNELE]>::iterator mapIt=floatArrayBranchesMap.begin();
			mapIt!=floatArrayBranchesMap.end(); mapIt++){
		outputTree->Branch((mapIt->first).c_str(),&(mapIt->second),((mapIt->first)+"["+to_string(OUTPUTNELE)+"]/F").c_str() );
	}///end loop to make new Float_t array branches in outputTree
	outputTree->Branch("_nPassing",&totalNumPassing,"_nPassing/l");
	outputTree->Branch("_nEvents",&totalMaxNumPassing,"_nEvents/l");
	outputTree->Branch("rate",&rate,"rate/F");

	///fill the branches with values from numPassing, maxNumPassing, and cutBranchesMapVector
	ULong64_t maxIndex = (ULong64_t) numPassing.size();
	for(ULong64_t indx=0; indx<maxIndex; indx++){
		totalNumPassing = numPassing[indx];
		totalMaxNumPassing = maxNumPassing[indx];
		Float_t trigEff = (Float_t) (numPassing[indx])/maxNumPassing[indx];
		rate = trigEff*genEff*recoEff*lumiTimesXsxn;
		for(map<string,Float_t[OUTPUTNELE]>::iterator mapIt=cutBranchesMap.begin();
				mapIt!=cutBranchesMap.end(); mapIt++){
			for(unsigned int h=0; h<OUTPUTNELE; h++){
				//floatArrayBranchesMap[mapIt->first][h] = ((*cutBranchesMapVector[indx])->second).at(h);
				floatArrayBranchesMap[mapIt->first][h] = (cutBranchesMapVector[indx].at(mapIt->first))[h];
			
			}///end loop over number of elements in Float_t arrays
		}///end loop over elements in cutBranchesMap

		///that's all folks!
		outputTree->Fill();
	}///loop over elements in numPassing, maxNumPassing, and cutBranchesMapVector and fill outputTree
	

	///save outputTree to outputFileName
	//outputFile->cd();
	cout<<"outputTree name is \t"<< outputTree->GetName() <<endl;
	outputTree->Scan("*","","",10);
	outputTree->Write();
	outputFile->Close();

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
	vector<ULong64_t> nVeryHighPtBkgndPassing;	///number of very high pt bkgnd evts which pass different sets of cuts
	vector<ULong64_t> nVeryHighPtBkgndMaxPassing;	///max number of very high pt bkgnd evts which could have passed a set of cuts 
	
	///make three TChains, each with access to the entire directory of signal OR high pt bkgnd OR low pt bkgnd tuples
	///use the TChain method GetFile, and finally call GetName() to get the name of the file
	///use this file name to make a TFile object, and loop over the entries in this file
	string signalPath = "scanned_signal_tree_*.root";
	//string highPtPath = "/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_high_pt/*_DoubleEG_22_10.root";
	string localDir = "../scanningCode/scanResultTrees/";
	//string lowPtPath = "scanned_bkgnd_tree_pt50to80*.root";
	//string lowPtPath = "scanned_WJets_tree_*.root";
	string lowPtPath = "scanned_TT_tree_*.root";
	
	//string veryHighPtPath = "scanned_bkgnd_tree_pt80to120.root";
	//if(signalPath.empty() || highPtPath.empty() || lowPtPath.empty() || veryHighPtPath.empty()){
	//	cout<<"where are the scanned tuples?"<<endl;
	//	return;
	//}
	//TChain * sigChain = new TChain("scanned_tree","");
	//sigChain->Add((localDir+signalPath).c_str());
	//TChain * highPtChain = new TChain("scanned_tree","");
	//highPtChain->Add(highPtPath.c_str());
	TChain * lowPtChain = new TChain("scanned_tree","");
	lowPtChain->Add((localDir+lowPtPath).c_str());
	//TChain * veryHighPtChain = new TChain("scanned_tree","");
	//veryHighPtChain->Add(veryHighPtPath.c_str());


	//string lowPtTreeId="wjetsBkgnd";
	string lowPtTreeId="ttbarBkgnd";

	string sigTreeId="signal", highPtTreeId="highPtBkgnd";
	string veryHighPtTreeId = "veryHighPtBkgnd";
	string sigOutPath = "all_scanned_signal.root";
	//string highPtOutPath = "/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_high_pt/DoubleEG_22_10_master_high_pt_bkgnd_tuple.root";
	//string lowPtOutPath = "all_scanned_bkgnd_pt50to80.root";
	//string lowPtOutPath = "all_scanned_WJets.root";
	string lowPtOutPath = "all_scanned_TT.root";
	
	//string veryHighPtOutPath = "/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_very_high_pt/DoubleEG_22_10_master_very_high_pt_bkgnd_tuple.root";

	//Float_t pt50to80SkimEff = 0.0000709;	//for QCD pt20to30 bkgnd
	//Float_t pt50to80SkimEff = .0004215;	//for WJets bkgnd
	Float_t pt50to80SkimEff = .00584;	//for TTBar bkgnd
	
	Float_t pt30to80BkgndL1Eff = 0.043, pt30to80BkgndRecoEff = 0.107;
	Float_t pt80to170BkgndL1Eff = 0.123, pt80to170BkgndRecoEff = 0.147;
	Float_t sigRecoEff = 0.51, sigGenEff = 0.077, sigL1Eff = 0.83, sigTrackedMatchEff = 0.96, sigTracklessMatchEff = 0.84;
	
	Float_t lumi = 2.0e34;
	//Float_t rateFactor50to80 = lumi*((2890800)*(1e-36));
	//Float_t rateFactor50to80 = lumi*((52700)*(1e-36));	///< xSxn times lumi for WJets bkgnd
	Float_t rateFactor50to80 = lumi*((730)*(1e-36));	///< xSxn times lumi for TTBar bkgnd
	
	//Float_t rateFactor30to80 = lumi*((1.859*0.06071)*(1e-28));
	//Float_t rateFactor80to170 = lumi*((3.529*0.15443)*(1e-30));
	Float_t rateFactorSignal = lumi*(2.0)*(1e-33);

	//iterateOverFilesAndEntries(sigChain,nSignalPassing,nSignalMaxPassing, sigTreeId, localDir+sigOutPath, sigGenEff, sigRecoEff*sigL1Eff*sigTrackedMatchEff*sigTracklessMatchEff, rateFactorSignal);
	//iterateOverFilesAndEntries(highPtChain,nHighPtBkgndPassing,nHighPtBkgndMaxPassing, highPtTreeId, highPtOutPath,1, pt30to80BkgndL1Eff*pt30to80BkgndRecoEff, rateFactor30to80);
	//iterateOverFilesAndEntries(veryHighPtChain,nVeryHighPtBkgndPassing,nVeryHighPtBkgndMaxPassing, veryHighPtTreeId, veryHighPtOutPath,1, pt80to170BkgndL1Eff*pt80to170BkgndRecoEff, rateFactor80to170);
	iterateOverFilesAndEntries(lowPtChain,nLowPtBkgndPassing,nLowPtBkgndMaxPassing, lowPtTreeId, localDir+lowPtOutPath,1, pt50to80SkimEff, rateFactor50to80);
	


}///end countNpassingForAllCutSets()

