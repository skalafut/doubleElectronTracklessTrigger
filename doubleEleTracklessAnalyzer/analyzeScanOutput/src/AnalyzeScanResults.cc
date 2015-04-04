#include "../interface/AnalyzeScanResults.h"
#include "TTree.h"
#include "TChain.h"
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

