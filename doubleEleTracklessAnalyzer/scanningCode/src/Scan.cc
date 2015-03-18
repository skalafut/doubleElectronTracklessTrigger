#include "../interface/Scan.h"
#include "TFile.h"
//#include "TEntryListArray.h"
#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstddef>

#define NELE 400
#define ETABRANCHANAME "etaHltEle"

using namespace std;

void Scan::InitCutContainer(std::string configFileName_){
     ifstream confStrm(configFileName_);
	
     std::string branchName, ranges, region;
     while(confStrm.peek() != EOF && confStrm.good()){ /// \todo check if the file is valid
	  if(confStrm.peek() == 35){ // 35 = #
	       confStrm.ignore(1000,10); // ignore the rest of the line until \n
	       continue;
	  }
	  confStrm >> branchName >> ranges >> region; // read and put into strings
	  
	  _branchNames.insert(branchName);

	  CutVar cutObject(branchName,region);
	  cutObject.SetValuesFromString(ranges); // the parsing of the string is implemented in CutVar
#ifdef DEBUG
	  std::cout << cutObject << std::endl
#endif
	  _cutContainer.push_back(cutObject);
	  for(unsigned int i=0; i < NELE; i++){
	       _inputBranches[branchName][i]=0;
	       _outputBranches[branchName][i]=0;
	  }

     }//end while
}//end InitCutVars()



void Scan::InitInputNtuple(TChain *chain){
     // TList *friends = chain->GetListOfFriends();
     // TIter newfriend_itr(friends);

     for(floatBranchMap_t::iterator mapIt = _inputBranches.begin(); mapIt!=_inputBranches.end(); mapIt++){
	  chain->SetBranchAddress((mapIt->first).c_str(),&mapIt->second);
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
     // phi and eta
}

void Scan::InitOutputNtuple(TChain *tree){
     for(floatBranchMap_t::iterator mapIt = _inputBranches.begin(); mapIt!=_inputBranches.end(); mapIt++){
	  tree->Branch((mapIt->first).c_str(),&mapIt->second, (mapIt->first+"/F[NELE]").c_str());
     }//end loop over map elements

     // set additional branches

     //add two additional float branches to count the number of events analyzed, and
     //the number of evts which passed all cuts
     _outputTree->Branch("nEvents", &nEvents, "nEvents/l");
     _outputTree->Branch("nPassing", &nPassing, "nPassing/l");
}

void Scan::SaveOutput(std::string pathToOutputFile){
		
	  TFile * outTupleFile = new TFile(pathToOutputFile.c_str(),"update");
	  outTupleFile->cd();
	  _outputTree->Write();
	  outputTupleFile->Close();
	  return;
	
}

/*
  void setRange(std::string varName,float min,float max,float step){
  }//end setRange()
*/

/**
   Recursive method.
   @param[in] iCut number of remaining variables to loop over. if iCut==0 then end
 */
void Scan::runScan(unsigned int iCut){
     //scan over all of the variables in cutContainer, and for each variable loop over all possible
     //values of the threshold.  For each variable threshold value, loop over all input events
     //and count how many pass the current threshold values of all variables in cutContainer.


     //once iCut equals zero all of the cut thresholds have been set to new values
     //using these new threshold values I should loop over all events in the input tuple
     //and count how many pass the set of cuts.  This event count, the values of
     //every cut threshold, and the number of input evts analyzed should be written
     //to the output tuple by calling outputTree->Fill().  This tree should then be saved
     //to the output file by calling outputTree->Write().  Finally, I should return control
     //to the main program.
     if(iCut==0){
	  
	  //save these two vars to the output tree 
	  float numEvtsAnalyzed = 0;
	  float numEvtsPassingCuts = 0;
		
	  //loop over all entries in the two input tuples
	  numEvtsAnalyzed=_pInputChain->GetEntries(); // this is slow, do it once
	  for(Long64_t evt = 0; evt<_pInputChain->GetEntriesFast(); evt++){
	       _pInputChain->GetEntry(evt);
	       
	       bool passing=true;


	       std::map<std::string, std::set<int> > passingEleTree;
	       TList *friends = chain->GetListOfFriends();
	       TIter newfriend_itr(friends);

	       // loop over friends
	       for(TFriendElement *friendElement = (TFriendElement*) newfriend_itr.Next();
		   friendElement != NULL; friendElement = (TFriendElement*) newfriend_itr.Next()){
		    std::string treeName=friendElement->GetTreeName();
		    std::set<int> passingEle;
		    for(unsigned int iEle =0; iEle < _inputBranches[treeName+".nHltEle"]; iEle++){
			 passingEle.insert(iEle);
		    }
		    passingEleTree[treeName]=passingEle;
	       }
	       
	       // now you have the passingEleTree filled with all passible electrons (index) from both legs

	       for(std::vector<CutVar>::const_iterator cut_itr = _cutContainer.begin();
		   cut_itr != _cutContainer.end() && passing; cut_itr++){
		    std::string cutName= cut_itr->_cutName;

		    std::string treeName = ;//
		    std::string branchName =; //

		    std::set<int>& passingEle = passingEleTree[treeName];

		    for(std::set<int>::iterator iEle_itr=passingEle.begin(); iEle_itr!= passingEle.end(); ){

			 if(_inputBranches[treeName+ETABRANCHNAME][iEle] < 1.479 && cut_itr->region=="EE") continue;
			 if(_inputBranches[treeName+ETABRANCHNAME][iEle] > 1.479 && cut_itr->region=="EB") continue;
			 // here you have one electron matching the region

			 // now test if the electron is passing the selection
			 bool p=true;
			 if(currentCut.isUpperBound){ 
			      if(_inputBranches[cutName][iEle]>cut_itr->threshVal) p=false;
			 } else{
			      if(_inputBranches[cutName][iEle]<cut_itr->threshVal) p=false;
			 }

			 if(p) iEle_itr++; 
			 else passingEle.erase(iEle_itr);
		    }
	       }

	       // now loop over the passingEleTree to make Zee candidates
	       // this can lead to segmentation violation, there is no control on the number of trees
	       std::map<std::string, std::set<int> >::const_iterator map1_itr=passingEleTree.begin();
	       std::map<std::string, std::set<int> >::const_iterator map2_itr=map1_itr; map2_itr++;

	       passing = false;
	       for(std::set<int>::const_iterator iEle1_itr=map1_itr->begin();
		   iEle1_itr!=map1_itr->end();
		   iEle1_itr++){
		    for(std::set<int>::const_iterator iEle2_itr=map2_itr->begin();
			iEle2_itr!=map2_itr->end();
			iEle2_itr++){
			 // calculate invariant mass
			 float mass = 0;//
			 if(mass > 40 && mass < 140) passing = true;
		    }
	       }

	       if(passing) nPassing++;
	  }
	  _outputTree->Fill();
	  return;
     }//end if(iCut==0)

     // if iCut!=0 call this method varying the cut value
     CutVar& currentCut = _cutContainer[iCut-1];

     for(currentCut.threshVal = currentCut.minThresh; 
	 currentCut.threshVal<currentCut.maxThresh; 
	 currentCut+=currentCut.threshStep){
	  //NOTE
	  //in the current CutVar constructor the variable threshVal is always initialized to the minimum threshold value
	  //within this loop update the threshold value to a new value, and call runScan again to move on to the next
	  //cut variable stored in cutContainer.  The number of iterations which are executed within this for loop has
	  //nothing to do with the number of CutVar objects stored in cutContainer!
	  runScan(pathToOutputFile,iCut-1);
     }//end loop over all possible values of the cut threshold for a CutVar object in cutContainer

}//end runScan()

