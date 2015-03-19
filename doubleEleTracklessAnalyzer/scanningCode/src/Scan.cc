#include "../interface/Scan.h"
#include "TTree.h"
#include "TChain.h"
#include "TFriendElement.h"
#include "TList.h"
#include "TCollection.h"
#include "TFile.h"
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstddef>
#include <cmath>
#include <map>
#include <set>

//#define DEBUG true
#define NELE 400
#define ETABRANCHNAME "etaHltEle"
#define PHIBRANCHNAME "phiHltEle"
#define PTBRANCHNAME "ptHltEle"
#define DRBRANCHNAME "deltaRHltEle"
#define NUMELEBRANCHNAME "nHltEle"

using namespace std;

void Scan::InitCutContainer(){
	ifstream confStrm(_configFileName);

	while(confStrm.peek() != EOF && confStrm.good()){ /// \todo check if the file is valid
		if(confStrm.peek() == 35){ // 35 = #
			confStrm.ignore(1000,'\n'); // ignore the rest of the line until \n
			continue;
		}
		string branchName, ranges, region;

		///this works much better than getLine()
		confStrm >> branchName >> ranges >> region; // read and put into strings
		if(branchName.empty()) break;

		//cout<<"about to add a branchName to the set of strings named _branchName"<<endl;
		_branchNames.insert(branchName);

		//cout<<"about to make a CutVar object"<<endl;
		CutVar cutObject(branchName,region);
		cutObject.SetValuesFromString(ranges); // the parsing of the string is implemented in CutVar
/*
#ifdef DEBUG
		//use this to check the range of values assigned to each cut variable, and its status as an upper or lower bound
		cout << cutObject << endl;
#endif
*/
		_cutContainer.push_back(cutObject);
		for(unsigned int i=0; i < NELE; i++){
			_inputBranches[branchName][i]=0;
			_outputBranches[branchName][i]=0;
		}

	}//end while
	return;
}//end InitCutContainer()



void Scan::InitInputNtuple(TChain *chain){
	// TList *friends = chain->GetListOfFriends();
	// TIter newfriend_itr(friends);
	_pInputChain = chain;
	string chainName = chain->GetName();

	//add elements to _inputBranches for phi, eta, and deltaR
	for(unsigned int h=0;h<NELE;h++){
		_inputBranches[chainName+"."+PHIBRANCHNAME][h]=0;
		_inputBranches[chainName+"."+ETABRANCHNAME][h]=0;
	}//end loop which initializes array values in additional input branches

	for(floatBranchMap_t::iterator mapIt = _inputBranches.begin(); mapIt!=_inputBranches.end(); mapIt++){
		_pInputChain->SetBranchAddress((mapIt->first).c_str(),&mapIt->second);
		// useful code related to TFriendElement manipulation
		// assuming the same branch name in all the friend trees, you can loop over the friends
		// loop over friends
		// for(TFriendElement *friendElement = (TFriendElement*) newfriend_itr.Next();
		//     friendElement != NULL; friendElement = (TFriendElement*) newfriend_itr.Next()){
		//      TString treeName=friendElement->GetTreeName();
		//      TTree *tree=friendElement->GetTree();
		//tree->SetBranchAddress((mapIt->first).c_str(),&mapIt->second);
		//}
	}//end loop over map elements

	// additional branches
	// nHltEle 
	_pInputChain->SetBranchAddress((chainName + "."+NUMELEBRANCHNAME).c_str(),&_numEles);
	return;
}

void Scan::InitOutputNtuple(TTree *tree){
	_outputTree = tree;
	for(floatBranchMap_t::iterator mapIt = _outputBranches.begin(); mapIt!=_outputBranches.end(); mapIt++){
		_outputTree->Branch((mapIt->first).c_str(),&mapIt->second, (mapIt->first+"/F[NELE]").c_str());
	}//end loop over map elements

	// set additional branches
	//add two additional float branches to count the number of events analyzed, and
	//the number of evts which passed all cuts
	_outputTree->Branch("_nEvents", &_nEvents, "_nEvents/l");
	_outputTree->Branch("_nPassing", &_nPassing, "_nPassing/l");
	return;
}

void Scan::SaveOutput(string pathToOutputFile){
	  TFile * outTupleFile = new TFile(pathToOutputFile.c_str(),"update");
	  outTupleFile->cd();
	  _outputTree->Write();
	  outTupleFile->Close();
	  return;
}

/**
   Recursive method.
   @param[in] iCut number of remaining variables to loop over. if iCut==0 then end
 */
void Scan::runScan(unsigned int iCut){
     //scan over all of the variables in _cutContainer, and for each variable loop over all possible
     //values of the threshold.  For each variable threshold value, loop over all input events
     //and count how many pass the current threshold values of all variables in _cutContainer.


     //once iCut equals zero all of the cut thresholds have been set to new values
     //using these new threshold values I should loop over all events in the input tuple
     //and count how many pass the set of cuts.  This event count, the values of
     //every cut threshold, and the number of input evts analyzed should be written
     //to the output tuple by calling outputTree->Fill().  This tree should then be saved
     //to the output file by calling outputTree->Write().  Finally, I should return control
     //to the main program.
     if(iCut==0){
	  
	  //loop over all entries in the two input tuples
	  _nEvents=_pInputChain->GetEntries(); // this is slow, do it once
	  for(Long64_t evt = 0; evt<_pInputChain->GetEntriesFast(); evt++){
	       _pInputChain->GetEntry(evt);
	       
	       bool passing=true;

	       map<string, set<int> > passingEleTree;
	       TList *friends = _pInputChain->GetListOfFriends();
	       TIter newfriend_itr(friends);

	       // loop over friends
	       for(TFriendElement *friendElement = (TFriendElement*) newfriend_itr.Next();
		   friendElement != NULL; friendElement = (TFriendElement*) newfriend_itr.Next()){
		    string treeName=friendElement->GetTreeName();
			set<int> passingEle;
		    for(unsigned int iEle =0; iEle < _numEles; iEle++){
			 passingEle.insert(iEle);
		    }
		    passingEleTree[treeName]=passingEle;
	       }
	       
	       // now you have the map passingEleTree filled with all passible electrons (indexes) from both legs

	       for(vector<CutVar>::const_iterator cut_itr = _cutContainer.begin();
		   cut_itr != _cutContainer.end() && passing; cut_itr++){
		    string cutName= cut_itr->_cutName;	//here _cutName = treeName.branchName
			size_t dotPos = cutName.find(".");

		    string treeName = cutName.substr(0,dotPos-1);	//treeName listed before dot in cutName
		    string branchName = cutName.substr(dotPos+1); 	//branchName listed after dot in cutName

		    set<int>& passingEle = passingEleTree[treeName];

		    for(set<int>::iterator iEle_itr=passingEle.begin(); iEle_itr!= passingEle.end(); ){
			 
			 // there is no CutVar tied to the eta branch (we are not optimizing the eta range of the selection)
			 // so the treeName + eta branch name must be used to access eta values in _inputBranches
			 if(_inputBranches[treeName+ETABRANCHNAME][*iEle_itr] < 1.479 && cut_itr->_detectorRegion=="EE") continue;
			 if(_inputBranches[treeName+ETABRANCHNAME][*iEle_itr] > 1.479 && cut_itr->_detectorRegion=="EB") continue;
			 // here you have one electron matching the _detectorRegion

			 // now test if the electron is passing the selection
			 bool p=true;
			 //this if used to contain currentCut._isUpperBound
			 if(cut_itr->_isUpperBound){ 
			      if(_inputBranches[cutName][*iEle_itr]>cut_itr->_threshVal) p=false;
			 } else{
			      if(_inputBranches[cutName][*iEle_itr]<cut_itr->_threshVal) p=false;
			 }

			 if(p) iEle_itr++; 
			 else passingEle.erase(iEle_itr);	//remove this element if it fails the cut. erase() increments iEle_itr by one
		    }
	       }

	       // now loop over the passingEleTree to make Zee candidates
	       // this can lead to segmentation violation, there is no control on the number of trees
	       // now there are two unique keys in passingEleTree (two tree names)
		   // each key is tied to a set (an ordered vector which can be searched)
		   // map1_itr is linked to the first unique key (here tracked leg or trackless leg) in passingEleTree
		   // map2_itr is linked to the second unique key (the leg which is not represented by the first key) in passingEleTree
		   map<string, set<int> >::const_iterator map1_itr=passingEleTree.begin();
	       map<string, set<int> >::const_iterator map2_itr=map1_itr; map2_itr++;

	       passing = false;
		   float mass=0, firstPt=0, firstEta=0, firstPhi=0, secondPt=0, secondEta=0, secondPhi=0, mSqd=-1;
	       for(set<int>::const_iterator iEle1_itr=map1_itr->second.begin();
		   iEle1_itr!=map1_itr->second.end();
		   iEle1_itr++){
		    for(set<int>::const_iterator iEle2_itr=map2_itr->second.begin();
			iEle2_itr!=map2_itr->second.end();
			iEle2_itr++){
			 // calculate invariant mass
			 // use iEle1_itr and iEle2_itr to access pt, eta, and phi in _inputBranches
			 firstPt = _inputBranches[(map1_itr->first)+"."+PTBRANCHNAME][*iEle1_itr];
			 firstEta = _inputBranches[(map1_itr->first)+"."+ETABRANCHNAME][*iEle1_itr];
			 firstPhi = _inputBranches[(map1_itr->first)+"."+PHIBRANCHNAME][*iEle1_itr];
			 secondPt = _inputBranches[(map2_itr->first)+"."+PTBRANCHNAME][*iEle2_itr];
			 secondEta = _inputBranches[(map2_itr->first)+"."+ETABRANCHNAME][*iEle2_itr];
			 secondPhi = _inputBranches[(map2_itr->first)+"."+PHIBRANCHNAME][*iEle2_itr];
			 mSqd = 2*firstPt*secondPt*(cosh(firstEta-secondEta) - cos(firstPhi-secondPhi));
			 if(mSqd > 0) mass = sqrt(mSqd);
			 if(mass > 40 && mass < 140) passing = true;
			 if(passing) break;
		    }//end loop over iEle2_itr
			if(passing) break;
	       }//end loop over iEle1_itr

	       if(passing) _nPassing++;
	  }
	  _outputTree->Fill();
	  return;
     }//end if(iCut==0)

     // if iCut!=0 call this method varying the cut value
     CutVar& currentCut = _cutContainer[iCut-1];

	 for(currentCut._threshVal = currentCut._minThresh; 
		 currentCut._threshVal<currentCut._maxThresh; 
		 currentCut._threshVal+=currentCut._threshStep){
		 // the CutVar member vars _threshVal, _minThresh, _maxThresh, and _threshStep are all public
		 // in this loop _threshVal is initialized to _minThresh, then incremented by _threshStep
		 // until _maxThresh is reached 
		 // The number of iterations which are executed within this for loop has
		 // nothing to do with the number of CutVar objects stored in _cutContainer!
		 // now use some recursive magic!
		 runScan(iCut-1);
	 }//end loop over all possible values of the cut threshold for a CutVar object in _cutContainer

}//end runScan()

