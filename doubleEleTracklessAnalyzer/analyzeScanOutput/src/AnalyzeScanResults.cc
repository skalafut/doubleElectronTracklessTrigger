#include "../interface/AnalyzeScanResults.h"
#include "TTree.h"
#include "TChain.h"
//#include "TFriendElement.h"
#include "TObjArray.h"
#include "TFile.h"
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstddef>
#include <cmath>
#include <map>
#include <array>
#include <set>
#include <cassert>

#define INPUTNELE 1
#define DEBUG

using namespace std;

void AnalyzeScanResults::InitInputNtuple(TChain *chain){
	_inputChain = chain;
	_numEvtsPassing = 0;
	_maxPossibleNumEvtsPassing=0;	
	
	map<string,string> singleValuedBranches;	///< used for branches which are read in from _configFile and contain single numerical values (no arrays) 
	ifstream configStrm(_configFile);
	while(configStrm.peek() != EOF && configStrm.good() ){
		if(configStrm.peek() == 35){// char number 35 is the number sign #, which I use in _configFile to indicate a comment
			configStrm.ignore(1000,'\n');
			continue;
		}
		string branchName, varType, rank;
		configStrm >> branchName >> varType >> rank;

		///now branchName is filled with the name of a branch, varType is filled and indicates the type of variable stored in the branch
		///varType = AF indicates a Float_t array is stored in the branch
		///varType = L indicates a Long64_t value is stored in the branch
		///and rank is filled with the names of private member vars which will be linked with single valued branches
		///rank = _maxPossibleNumEvtsPassing indicates this branch holds the largest value amongst the single valued (non-array) branches in any event
		///rank = _numEvtsPassing indicates this branch holds the second largest value amongst the single valued (non-array) branches in any event

		if(branchName.empty()) break;	///< _configFile ends with an empty line. leave this loop once this empty line is reached
		
		///if varType is AF, then assign the string in branchName to the _inputArrayBranches map
		if(varType.compare("AF") == 0){
			for(unsigned int i=0; i<INPUTNELE; i++){
				_inputArrayBranches[branchName][i] = 0;
			}///end for loop to initialize array entries linked to _inputArrayBranches[someString]
		}//end filter to select branchNames which are linked to Float_t arrays

		///if varType is L, then put the branchName and rank into the map named singleValuedBranches declared above
		if(varType.compare("L")==0){
			///save the branchName and rank (_maxPossibleNumEvtsPassing, _numEvtsPassing, etc) in the map named singleValuedBranches
			singleValuedBranches[branchName]=rank;
		}//end filter to select branchNames which are linked to Long64_t values

	}///end loop over lines of txt in _configFile
	
	/// \todo link _numEvtsPassing to _nPassing branch, and _maxPossibleNumEvtsPassing to _nEvents branch 
	for(floatBranchMap_t::iterator mapIt = _inputArrayBranches.begin(); mapIt!=_inputArrayBranches.end(); mapIt++){
		///this links the Float_t arrays in _inputArrayBranches to the Float_t array branches in _inputChain
		int iRead = _inputChain->SetBranchAddress((mapIt->first).c_str(),&(mapIt->second));
#ifdef DEBUG
		if(iRead!=0) cout<<"branch named"<<"\t"<<mapIt->first<<"\t"<<"is no good"<<"\t"<<"exit status ="<<"\t"<< iRead <<endl;
#endif
	}///end loop over elements in _inputArrayBranches map

	for(map<string,string>::iterator mapIt=singleValuedBranches.begin(); mapIt!=singleValuedBranches.end(); mapIt++){
		///this links the Long64_t values in an AnalyzeScanResults class object to the Long64_t branches in _inputChain
		int iRead = _inputChain->SetBranchAddress((mapIt->first).c_str(),&(mapIt->second));
#ifdef DEBUG
		if(iRead!=0) cout<<"branch named"<<"\t"<<mapIt->first<<"\t"<<"is no good"<<"\t"<<"exit status ="<<"\t"<< iRead <<endl;
#endif
	}///end loop over elements in singleValuedBranches map

}///end InitInputNtuple()

/*
static void updateCutSetsAndEvtsPassing(std::map<long,std::map<std::string,float> >& mapHoldingMaps,long mapIndx,string& evtKey, map<string,AnalyzeScanResults>::const_iterator& asrMapIt){
#ifdef DEBUG
	cout<<"in updateCutSetsAndEvtsPassing"<<endl;
#endif
	map<string,float> cutValsAndEvtsPassing;
	if(mapHoldingMaps.empty()){
#ifdef DEBUG
		cout<<"no map between long key and map<string,float> object"<<endl;
#endif
		for(AnalyzeScanResults::floatBranchMap_t::const_iterator brMapIt=(asrMapIt->second)._inputArrayBranches.begin();
				brMapIt!=(asrMapIt->second)._inputArrayBranches.end(); brMapIt++){
			cutValsAndEvtsPassing[(brMapIt->first)]=(brMapIt->second)[0];	///<BE CAREFUL there is only one element in each Float_t array
		}///end loop over array branches  NOTE each branch has only one element
		cutValsAndEvtsPassing[evtKey]=(asrMapIt->second)._numEvtsPassing;
		mapHoldingMaps[mapIndx]=cutValsAndEvtsPassing;
#ifdef DEBUG
		cout<<"added a map<string,float> object and long key value to a map of maps"<<endl;
#endif
	}///end if(mapHoldingMaps is empty)

	else{
		///check if this set of cut values already exists in tempBkgndMap
		///if it does, increment the number of evts passing stored in the map by the current value of _numEvtsPassing
		///otherwise, make a new entry in the vector with the new set of cut values and the number of evts passing this set of cuts
		bool foundUniqueCutSet = true;
		long evtNumWithSameCutSet;

#ifdef DEBUG
		cout<<"map of maps has at least one element"<<endl;
#endif

		///fill cutValsAndEvtsPassing, then look to see if the cut values in the map have already been put into mapHoldingMaps
		for(AnalyzeScanResults::floatBranchMap_t::const_iterator brMapIt=(asrMapIt->second)._inputArrayBranches.begin();
				brMapIt!=(asrMapIt->second)._inputArrayBranches.end(); brMapIt++){
			cutValsAndEvtsPassing[(brMapIt->first)]=(brMapIt->second)[0];	///<BE CAREFUL there is only one element in each Float_t array
		}///end loop over array branches  NOTE each branch has only one element
		cutValsAndEvtsPassing[evtKey]=(asrMapIt->second)._numEvtsPassing;

		///check if the cut values in cutValsAndEvtsPassing already exist in mapHoldingMaps
		for(map<long,map<string,float> >::const_iterator tempMapIt=mapHoldingMaps.begin(); tempMapIt!=mapHoldingMaps.end(); tempMapIt++){
			bool brokeOutOfInner = false;
			for(map<string,float>::const_iterator innerTmpIt=(tempMapIt->second).begin();
					innerTmpIt!=(tempMapIt->second).end(); innerTmpIt++){
				///innerTmpIt is a map<string,float> iterator, so I can call ->first and ->second on innerTmpIt 
				if(innerTmpIt->second != (cutValsAndEvtsPassing.find(innerTmpIt->first))->second){
					brokeOutOfInner = true;
					break;
				}///end check for duplicate set of cut values 
			}///end loop over the entries in a map stored within mapHoldingMaps
			///if brokeOutOfInner is false, then the set of cut values in cutValsAndEvtsPassing is not unique
			if(!brokeOutOfInner){
				foundUniqueCutSet = false;
				evtNumWithSameCutSet = tempMapIt->first;
				break;
			}
		}///end loop over entries in mapHoldingMaps (a map of maps)
		if(foundUniqueCutSet){
			mapHoldingMaps[mapIndx] = cutValsAndEvtsPassing;
		}
		else{
			///if the set of cut vals is not unique, find the map in mapHoldingMaps with the duplicate set of cut vals
			///and increment the number of bkgnd evts passing
			float oldNumEvts = (mapHoldingMaps[evtNumWithSameCutSet].find(evtKey))->second;
			float newNumEvts = oldNumEvts + cutValsAndEvtsPassing[evtKey];
#ifdef DEBUG
			cout<<"found a duplicate set of cut vals"<<endl;
			cout<<"the old number of evts passing this set of cuts was"<<endl;
			cout<< oldNumEvts <<endl;
#endif
			mapHoldingMaps[evtNumWithSameCutSet].at(evtKey) = newNumEvts;
#ifdef DEBUG
			cout<<"the new number of evts passing this set of cuts is"<<endl;
			cout<< (mapHoldingMaps[evtNumWithSameCutSet].find(evtKey))->second <<endl;
#endif				
		}///the set of cut vals in cutValsAndEvtsPassing is not unique

	}///end filter mapHoldingMaps is not empty
#ifdef DEBUG
	cout<<"leaving updateCutSetsAndEvtsPassing method"<<endl;
#endif

}///end updateCutSetsAndEvtsPassing
*/

/*
static vector<map<string,float> > findOptimalCuts(float desiredRate, const AnalyzeScanResults& signal, map<string,AnalyzeScanResults> bkgnds, map<string,vector<float> > xSxnsAndLumi){

#ifdef DEBUG
	cout<<"in findOptimalCuts method"<<endl;
#endif

	vector<map<string,float> > mapToReturn;	///< return this map at the end of this fxn
	vector<map<long,map<string,float> > > listOfInterestingCutSets;	///one element in this vector for each element in input 'bkgnds' map
	string evtsPassingKey = "evtsPassing";
	int bkgndType = -1;	///<used to distinguish entries in tempBkgndMap which come from different AnalyzeScanResults objects in input map named bkgnds
	///loop over entries in each bkgnd TChain and find sets of cut values which yield a trigger rate near the desired rate
	for(map<string,AnalyzeScanResults>::const_iterator mapIt=bkgnds.begin(); mapIt!=bkgnds.end(); mapIt++){
		bkgndType++;
		map<long,map<string,float> > tempBkgndMap;	///use this to hold interesting sets of cut values, and the number of evts passing
		for(long evt=0; evt<(mapIt->second)._inputChain->GetEntriesFast(); evt++){
			(mapIt->second)._inputChain->GetEntry(evt);
			if((mapIt->second)._numEvtsPassing > 0){
				updateCutSetsAndEvtsPassing(tempBkgndMap,evt,evtsPassingKey,mapIt);
			}///end filter to skip TChain entries where no bkgnd evts pass
		}///end loop over entries in one bkgnd TChain 
	}///end loop over different bkgnd samples (high pt QCD, low pt QCD, etc) stored in bkgnds map

#ifdef DEBUG
	cout<<"leaving findOptimalCuts method"<<endl;
#endif

	return mapToReturn;
}//end findOptimalCuts()
*/

