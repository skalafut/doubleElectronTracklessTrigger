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
#include <array>
#include <set>
#include <cassert>

#define NELE 400
#define OUTPUTNELE 1
#define ETABRANCHNAME "etaHltEle"
#define PHIBRANCHNAME "phiHltEle"
#define PTBRANCHNAME "ptHltEle"
#define NUMELEBRANCHNAME "nHltEle"
//#define DEBUG
//#define DEBUG2

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
		string outputBranchName = branchName.substr(branchName.find(".")+1)+region;

		CutVar cutObject(branchName,region,outputBranchName);
		cutObject.SetValuesFromString(ranges); // the parsing of the string is implemented in CutVar

#ifdef DEBUG
		//use this to check the range of values assigned to each cut variable, and its status as an upper or lower bound
		cout << cutObject << endl;
#endif
		_cutContainer.push_back(cutObject);
		for(unsigned int i=0; i < NELE; i++){
			_inputBranches[branchName][i]=0;
		}
		for(unsigned int i=0; i < OUTPUTNELE; i++){
			_outputBranches[outputBranchName][i]=0;
		}


	}//end while
	return;
}//end InitCutContainer()



void Scan::InitInputNtuple(TChain *chain){
#ifdef DEBUG
	cout<<"in InitInputNtuple() fxn"<<endl;
#endif
	_pInputChain = chain;
	string chainName = chain->GetName();

	for(unsigned int h=0;h<NELE;h++){
		//add phi,eta, and nHltEle tree.branch names from _pInputChain to _inputBranches and _inputBranchesInt maps 
		_inputBranches[chainName+"."+PHIBRANCHNAME][h]=-1;
		_inputBranches[chainName+"."+ETABRANCHNAME][h]=100;
		_inputBranchesInt[chainName+"."+NUMELEBRANCHNAME][h]=-1;
	}//end loop which initializes array values in additional input branches

	TList *friends = chain->GetListOfFriends();
	TIter newfriend_itr(friends);
	for(TFriendElement *friendElement = (TFriendElement*) newfriend_itr.Next();
			friendElement != NULL; friendElement = (TFriendElement*) newfriend_itr.Next()){
		std::string treeName=friendElement->GetTreeName();
		//add phi,eta, and nHltEle tree.branch names from friends of _pInputChain
		//to _inputBranches and _inputBranchesInt maps 
	
		for(unsigned int h=0;h<NELE;h++){
			_inputBranches[treeName+"."+PHIBRANCHNAME][h]=-1;
			_inputBranches[treeName+"."+ETABRANCHNAME][h]=100;
			_inputBranchesInt[treeName+"."+NUMELEBRANCHNAME][h]=-1;
		}//end loop which initializes array values to additional input branches tied to friend chains

	}//end loop over TFriendElements

	for(intBranchMap_t::iterator mapIt = _inputBranchesInt.begin(); mapIt!=_inputBranchesInt.end(); mapIt++){
		string brName = mapIt->first;
		if(brName.find(chainName)!=string::npos) brName = brName.substr(brName.find(".")+1);
#ifdef DEBUG
		if(brName.compare(mapIt->first)!=0) cout<<"brName has been shortened to"<<"\t"<<brName<<endl;
#endif
		//now brName will access the correct branch (of the main tree, or one of its friends), and the
		//variable assigned to this branch comes from _inputBranchesInt 
		int iRead=_pInputChain->SetBranchAddress(brName.c_str(),&(mapIt->second));
#ifdef DEBUG
		if(iRead!=0) cout<<"branch named"<<"\t"<<brName<<"\t"<<"is no good"<<"\t"<<"exit status ="<<"\t"<< iRead <<endl;
#endif
	}

#ifdef DEBUG
	cout<<"initialized Int_t array branches to main input chain and its friends"<<endl;
#endif

	for(floatBranchMap_t::iterator mapIt = _inputBranches.begin(); mapIt!=_inputBranches.end(); mapIt++){
		string brName = mapIt->first;
		if(brName.find(chainName)!=string::npos) brName = brName.substr((brName).find(".")+1);
#ifdef DEBUG
		if(brName.compare(mapIt->first)!=0) cout<<"brName has been shortened to"<<"\t"<<brName<<endl;
#endif
		_pInputChain->SetBranchAddress(brName.c_str(),&(mapIt->second));
	}//end loop over map elements

#ifdef DEBUG
	cout<<"initialized Float_t array branches to main input chain and its friends"<<endl;
	cout<<"\t"<<endl;
#endif
	return;
}

void Scan::InitOutputNtuple(TTree *tree){
#ifdef DEBUG
	cout<<"\t"<<endl;
	cout<<"in InitOutputNtuple() method"<<endl;
#endif
	_outputTree = tree;

	//use _detectorRegion
	for(altFloatBranchMap_t::iterator mapIt = _outputBranches.begin(); mapIt!=_outputBranches.end(); mapIt++){
		_outputTree->Branch((mapIt->first).c_str(),&(mapIt->second), (mapIt->first+"["+to_string(OUTPUTNELE)+"]/F").c_str());
	}//end loop over _outputBranches map elements

	// set additional branches
	//add two additional float branches to count the number of events analyzed, and
	//the number of evts which passed all cuts
	_outputTree->Branch("_nEvents", &_nEvents, "_nEvents/l");
	_outputTree->Branch("_nPassing", &_nPassing, "_nPassing/l");
#ifdef DEBUG	
	cout<<"initialized all branches to output tree"<<endl;
	cout<<"\t"<<endl;
#endif
	return;
}

void Scan::SaveOutput(string pathToOutputFile){
#ifdef DEBUG
	cout<<"\t"<<endl;
	cout<<"in SaveOutput() method"<<endl;
#endif
	TFile * outTupleFile = new TFile(pathToOutputFile.c_str(),"recreate");
	outTupleFile->cd();
	_outputTree->Scan("","","",10);
	_outputTree->Write();
	outTupleFile->Close();
#ifdef DEBUG
	cout<<"wrote output tree to file"<<endl;
	cout<<"\t"<<endl;
#endif
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
#ifdef DEBUG
		cout<<"\t"<<endl;
		cout<<"in iCut==0 portion of runScan() method"<<endl;
		cout<<"\t"<<endl;
		cout<<"about to call GetEntries() on main input chain"<<endl;
#endif

		_nPassing=0;
		_nEvents=0;
		//loop over all entries
		//replace 50 with _pInputChain->GetEntriesFast()
		for(Long64_t evt = 0; evt<_pInputChain->GetEntriesFast(); evt++){
#ifdef DEBUG
			if(evt>=0) cout<<"about to call GetEntry() on main input chain"<<endl;
			if(evt>=0) cout<<"on Tree entry number"<<"\t"<<evt<<endl;
#endif

			_pInputChain->GetEntry(evt);
	
#ifdef DEBUG
			if(evt>=0) cout<<"called GetEntry() on main input chain"<<endl;
#endif
	
			bool passing=true;

			map<string, set<int> > passingEleTree;
			TList *friends = _pInputChain->GetListOfFriends();
			TIter newfriend_itr(friends);
#ifdef DEBUG
			if(evt>=0) cout<<"called GetListOfFriends() on main input chain"<<endl;
#endif

			string mainChainName = _pInputChain->GetName();
			//count number of reco objects made in this evt in the primary input chain
			set<int> mainPassingEle;
			for(unsigned int q=0; q <_inputBranchesInt[mainChainName+".nHltEle"][0]; q++){
				mainPassingEle.insert(q);
			}
			passingEleTree[mainChainName] = mainPassingEle;
#ifdef DEBUG
			if(evt>=0) cout<<"mainChainName="<<"\t"<<mainChainName<<endl;
			if(evt>=0) cout<<"num reco eles in main chain="<<"\t"<<_inputBranchesInt[mainChainName+".nHltEle"][0]<<endl;
#endif

			// loop over friends and count the total number of reco objects made in TTree entry number evt
			for(TFriendElement *friendElement = (TFriendElement*) newfriend_itr.Next();
					friendElement != NULL; friendElement = (TFriendElement*) newfriend_itr.Next()){
				string treeName=friendElement->GetTreeName();
#ifdef DEBUG
				if(evt>=0) cout<<"friendElement treeName = "<< treeName <<endl;
				if(evt>=0) cout<<"num reco eles in friend="<<"\t"<< _inputBranchesInt[treeName+".nHltEle"][0]<<endl;
#endif

				set<int> passingEle;
				for(unsigned int iEle =0; iEle < _inputBranchesInt[treeName+".nHltEle"][0]; iEle++){
					passingEle.insert(iEle);
				}
				passingEleTree[treeName]=passingEle;
			}
			bool recoOk=true;
			for(map<string,set<int> >::const_iterator mapIt=passingEleTree.begin(); mapIt!=passingEleTree.end(); mapIt++){
				if(mapIt->second.size()==0){
#ifdef DEBUG2
					cout<<mapIt->first<<"\t"<<mapIt->second.size()<<endl;
#endif
					recoOk=false;
				}	
			}
			if(recoOk) _nEvents++;
#ifdef DEBUG2
			cout<<"-----------------------------------------------------"<<endl;
#endif	
			// now you have the map passingEleTree filled with all possible electrons (indexes) from both legs

			for(vector<CutVar>::const_iterator cut_itr = _cutContainer.begin();
					cut_itr != _cutContainer.end(); cut_itr++){

#ifdef DEBUG
			  	if(evt>=0) cout<<"\t"<<endl;
				if(evt>=0) cout<<"about to apply cut"<<"\t"<<*cut_itr<<endl;
#endif
				string cutName= cut_itr->_cutName;	//here _cutName = treeName.branchName
				size_t dotPos = cutName.find(".");

				string treeName = cutName.substr(0,dotPos);	//treeName listed before dot in cutName
				string branchName = cutName.substr(dotPos+1); 	//branchName listed after dot in cutName
#ifdef DEBUG
				if(evt>=0) cout<<"treeName="<<"\t"<<treeName<<endl;
				if(evt>=0) cout<<"branchName="<<"\t"<<branchName<<endl;
#endif

				set<int>& passingEle = passingEleTree[treeName];

#ifdef DEBUG
				if(evt>=0) cout<<"size of passingEleTree with key \t"<< treeName <<"\t=\t"<< passingEle.size() <<endl;
				if(evt>=0) cout<<"about to start looping over a set of ints store in passingEleTree"<<endl;
				if(evt>=0) cout<<"passingEleTree[treeName] has this many elements:"<<"\t"<<passingEleTree[treeName].size()<<endl;
#endif
	
				for(set<int>::iterator iEle_itr=passingEle.begin(); iEle_itr!= passingEle.end() && !passingEle.empty(); ){
					// there is no CutVar tied to the eta branch (we are not optimizing the eta range of the selection)
					// so the treeName + eta branch name must be used to access eta values in _inputBranches

#ifdef DEBUG
					if(evt>=0) cout<<"\t"<<endl;
					if(evt>=0) cout<<"in loop over passingEle elements"<<endl;
#endif
					string fullEtaBrName = treeName;
					fullEtaBrName.append(".");
					fullEtaBrName.append(ETABRANCHNAME);
#ifdef DEBUG
					if(evt>=0) cout<<"reco eta =\t"<< _inputBranches[fullEtaBrName][*iEle_itr] <<endl;
#endif

					//leave this loop over passingEle elements once the eta value in _inputBranches[fullEtaBrName][*iEle_itr]
					//is greater than 5.0 or less than -5.0
					//this will happen because the array of Float_t values at _inputBranches[fullEtaBrName] has 400 entries
					//or whatever NELE is set to
					assert(fabs(_inputBranches[fullEtaBrName][*iEle_itr]) < 5.0);

					if(fabs(_inputBranches[fullEtaBrName][*iEle_itr]) < 2.5 && (cut_itr->_detectorRegion).compare("utEE")==0){
						iEle_itr++;
						continue;
					}//end trackless eta filter
					if( (fabs(_inputBranches[fullEtaBrName][*iEle_itr]) < 1.479 || fabs(_inputBranches[fullEtaBrName][*iEle_itr]) >= 2.5) && (cut_itr->_detectorRegion).compare("tEE")==0 ){
						iEle_itr++;
						continue;
					}//end tracked EE eta filter
					if(fabs(_inputBranches[fullEtaBrName][*iEle_itr]) > 1.479 && (cut_itr->_detectorRegion).compare("EB")==0){
						iEle_itr++;
						continue;
					}//end tracked EB eta filter
					// here you have one electron matching the _detectorRegion

#ifdef DEBUG
					if(evt>=0) cout<<"have an electron which passes eta requirement"<<endl;
					if(evt>=0) cout<<"about to apply this cut:"<<endl;
					if(evt>=0) cout<<*cut_itr<<endl;
					if(evt>=0) cout<<"\t"<<endl;
#endif

					// now test if the electron passes the cut 
					bool p=true;
					if(cut_itr->_isUpperBound){ 
						if(_inputBranches[cutName][*iEle_itr]>cut_itr->_threshVal) p=false;
					} else{
						if(_inputBranches[cutName][*iEle_itr]<cut_itr->_threshVal) p=false;
					}

#ifdef DEBUG
					if((evt>=0) && p) cout<<"reco electron passed cut"<<endl;
					if((evt>=0) && !p) cout<<"reco electron failed cut"<<endl;
#endif

					if(p) iEle_itr++; 
					else{
						passingEle.erase(iEle_itr);	//remove this element if it fails the cut
					}
				}//end loop over integers in passingEle set
				//now reassign the set passingEle to the map element passingEleTree[treeName]
				//passingEleTree[treeName] = ;
#ifdef DEBUG
				if(evt>=0){
					cout<<"left loop over integers in passingEle set"<<endl;
					cout<<"after applying a cut"<<endl;
					cout<<"passingEleTree[treeName] has this many elements:"<<"\t"<<passingEleTree[treeName].size()<<endl;
				   	cout<<"\t"<<endl;
				}
#endif
			}//end loop over CutVar objects in _cutContainer

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
#ifdef DEBUG
					if(evt>=0) cout<<"mass="<<"\t"<<mass<<endl;
#endif

					//if(mass > 40 && mass < 140)
					passing = true;
					if(passing) break;
				}//end loop over iEle2_itr
				if(passing) break;
			}//end loop over iEle1_itr

			if(passing) _nPassing++;
		}//end loop over entries in TChain

		for(vector<CutVar>::const_iterator cut_itr = _cutContainer.begin();
		    cut_itr != _cutContainer.end(); cut_itr++){
		  cout << cut_itr->printNameVal() << endl;
		}
		_outputTree->Fill();
		//cout<<"filled _outputTree, leaving runScan() method"<<endl;
		return;
	}//end if(iCut==0)

#ifdef DEBUG
	std::cout << _cutContainer.size() << "\t" <<"elements in _cutContainer"<<"\t"<< iCut << std::endl;
#endif
	// if iCut!=0 call this method varying the cut value
	CutVar& currentCut = _cutContainer[iCut-1];

	for(currentCut._threshVal = currentCut._minThresh; 
			currentCut._threshVal<currentCut._maxThresh; 
			currentCut._threshVal+=currentCut._threshStep){
		// all CutVar member vars (like _threshVal and _threshStep) are public
		// in this loop _threshVal is initialized to _minThresh, then incremented by _threshStep
		// until _maxThresh is reached 
		// The number of iterations which are executed within this for loop has
		// nothing to do with the number of CutVar objects stored in _cutContainer!
		//
		// now set the value of the variable in _outputBranches[_shortCutName]
		// and use some recursive magic!
		_outputBranches[currentCut._shortCutName][0] = currentCut._threshVal;
		runScan(iCut-1);
	}//end loop over all possible values of the cut threshold for a CutVar object in _cutContainer

}//end runScan()

