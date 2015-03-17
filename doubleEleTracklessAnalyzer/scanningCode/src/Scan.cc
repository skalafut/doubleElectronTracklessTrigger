#include "../interface/Scan.h"
#include "TFile.h"
//#include "TEntryListArray.h"
#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstddef>

#define NELE 400

using namespace std;

void Scan::InitCutContainer(std::string configFileName_){
     ifstream confStrm(configFileName_);
	
     std::string branchName, ranges, region;
     while(confStrm.peek() != EOF){ /// \todo check if the file is valid
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


void Scan::InitInputNtuple(TChain *tree){
     for(floatBranchMap_t::iterator mapIt = _inputBranches.begin(); mapIt!=_inputBranches.end(); mapIt++){
	  tree->SetBranchAddress((mapIt->first).c_str(),&mapIt->second);
     }//end loop over map elements
}

void Scan::InitOutputNtuple(TChain *tree){
     for(floatBranchMap_t::iterator mapIt = _outputBranches.begin(); mapIt!=_outputBranches.end(); mapIt++){
	  tree->SetBranchAddress((mapIt->first).c_str(),&mapIt->second);
     }//end loop over map elements
}


#ifdef shervin
//use the vector<string> returned by identifyUniqueBranchNames() as the input parameter branchNames to InitInputTuple()
void Scan::InitInputTuple(vector<string> pathToInputTuples,vector<string> inputTupleNames,vector<string> branchNames){
     if(pathToInputTuples.size() != inputTupleNames.size()){
	  cout<<"can't initialize input tuples because there are more unique tuple names than paths to tuple files"<<endl;
	  cout<<"check that the number of unique input tuple names equals the number of paths to input tuple files"<<endl;
	  return;
     }
	
     vector<string>::const_iterator pathIt = pathToInputTuples.begin();
     for(vector<string>::const_iterator tupleIt=inputTupleNames.begin(); tupleIt!=inputTupleNames.end(); tupleIt++){
	  pInputChains.push_back(new TChain((*tupleIt).c_str() ,""));
	  (pInputChains.back())->Add((*pathIt).c_str() );
	  pathIt++;	//not completely confident that this pathIt approach will work 
     }//make a new TChain pointer for every unique tree name

     //now setup maps between float arrays and branch (cut) variable names
     for(unsigned int h=0;h<pInputChains.size(); h++){
	  map<string,Float_t[NELE]> inputMap;
	  unsigned int index = 0;
	  for(vector<string>::const_iterator brIt=branchNames.begin(); brIt!=branchNames.end(); brIt++){
	       //add an entry to inputBranchArrayNamesAndVals for each entry in the vector
	       //returned by identifyUniqueBranchNames()
	       //(*brIt) is the name of a branch in an input file which will be used in the optimization, like
	       //ecalIsoHltEle
	       Float_t arr[NELE];
	       for(unsigned int i=0;i<NELE;i++){ arr[i]=0.;}	//initialize all elements to zero
	       inputMap[(*brIt)]=arr;
	       index++;
	       if(index == branchNames.size()){
		    //add entries to inputBranchArrayNames and inputBranchNames maps, and update pInputChains with map entries, to read in
		    //fixed size Float_t arrays containing eta, phi, and deltaR values
		    Float_t arrayOne[NELE],arrayTwo[NELE],arrayThree[NELE];
		    for(unsigned int j=0;j<NELE;j++){
			 arrayOne[j]=0.;
			 arrayTwo[j]=0.;
			 arrayThree[j]=0.;
		    }//end array initialization
		    string arrayOneName="etaHltEle",arrayTwoName="phiHltEle",arrayThreeName="deltaRHltEle";
		    inputMap[arrayOneName]=arrayOne;
		    inputMap[arrayTwoName]=arrayTwo;
		    inputMap[arrayThreeName]=arrayThree;

		    //now that all of the maps are setup, add inputMap to the vector of map objects
		    inputBranchArrayNamesAndVals.push_back(inputMap);
	       }//end if(index == number of unique branch names)
	  }//end loop over unique branch names pulled from objects in cutContainer

	  for(map<string,Float_t[NELE]>::iterator mapIt=inputBranchArrayNamesAndVals[h].begin(); mapIt!=inputBranchArrayNamesAndVals[h].end(); mapIt++){
	       pInputChains[h]->SetBranchAddress((mapIt->first).c_str(),mapIt->second);
	  }//end loop over map elements

     }//end loop over pointers to input TChain objects

}//end InitInputTuple()

void Scan::InitOutputTuple(string outTupleName){
     outputTree = new TTree(outputTupleName.c_str(),"");
     for(vector<CutVar>::const_iterator cutIt=cutContainer.begin(); cutIt!=cutContainer.end(); cutIt++){
	  string aCutVarName= (*cutIt).getCutName() + (*cutIt).getRegion();
	  string nameAndType = aCutVarName + "/f";
	  float val=0.;
	  outputBranchNamesAndVals[aCutVarName]=val;
	  outputTree->Branch(aCutVarName.c_str(),&(outputBranchNamesAndVals[aCutVarName]),nameAndType.c_str());
     }//end loop over cutContainer elements (objects of CutVar class)

     //add two additional float branches to count the number of events analyzed, and
     //the number of evts which passed all cuts
     long valOne=0.;
     float valTwo=0.;
     string valOneName="nEvtsAnalyzed", valTwoName="nEvtsPassing";
     outputBranchNamesAndVals[valOneName]=valOne;
     outputBranchNamesAndVals[valTwoName]=valTwo;
     outputTree->Branch(valOneName.c_str(),&(outputBranchNamesAndVals[valOneName]),(valOneName + "/l" ).c_str() );
     outputTree->Branch(valTwoName.c_str(),&(outputBranchNamesAndVals[valTwoName]),(valTwoName + "/f" ).c_str() );

}//end InitOutputTuple()

/*
  void setRange(std::string varName,float min,float max,float step){
  }//end setRange()
*/

void Scan::runScan(string pathToOutputFile, unsigned int iCut){
     //scan over all of the variables in cutContainer, and for each variable loop over all possible
     //values of the threshold.  For each variable threshold value, loop over all input events
     //and count how many pass the current threshold values of all variables in cutContainer.

     if(iCut==0){
	  //once iCut equals zero all of the cut thresholds have been set to new values
	  //using these new threshold values I should loop over all events in the input tuple
	  //and count how many pass the set of cuts.  This event count, the values of
	  //every cut threshold, and the number of input evts analyzed should be written
	  //to the output tuple by calling outputTree->Fill().  This tree should then be saved
	  //to the output file by calling outputTree->Write().  Finally, I should return control
	  //to the main program.

	  //CutVar::isThresholdUpperBound()
	  if(pInputChains.size() < 2){
	       cout<<"setup runScan method in Scan.cc to work with only one input tuple"<<endl;
	       return;
	  }


	  //use this string to distinguish tracked tree from trackless tree, and signal trees from bkgnd trees
	  string firstTupleName = pInputChains[0]->GetName();
	  size_t racklessPosition = firstTupleName.find("rackless");
	  size_t bkgndPosition = firstTupleName.find("kgnd");
	  bool failedTrackedLeg = false, failedTracklessLeg = false;
		
	  //save these two vars to the output tree 
	  float numEvtsAnalyzed = 0;
	  float numEvtsPassingCuts = 0;
		
	  //loop over all entries in the two input tuples
	  for(long evt = 0; evt<pInputChains[0]->GetEntries(); evt++){
	       pInputChains[0]->GetEntry(evt);
	       pInputChains[1]->GetEntry(evt);
	       numEvtsAnalyzed += 1;

	       //these four vars will only be used when scanning over matched signal evts
	       unsigned int bestIndexFirstChain = -1;
	       Float_t bestDrFirstChain=0.15;
	       unsigned int bestIndexSecondChain = -1;
	       Float_t bestDrSecondChain=0.15;

	       //these two vectors will only be used when scanning over bkgnd evts
	       //the trackless and tracked eta filters are applied before these vectors are filled
	       vector<unsigned int> indexesFirstChain;
	       vector<unsigned int> indexesSecondChain;

	       if(racklessPosition != string::npos){
		    //the first element in pInputChains corresponds to a trackless tuple
		    //the second element corresponds to a tracked tuple

		    //now loop over each element in the array within the vector<map> entry
		    //inputBranchArrayNamesAndVals[0][(*cutIt).getCutName()]
		    //each branch in the input tuples contains an array of floats, not just a single float, hence
		    //we must loop over all elements in each array
		    for(unsigned int ele=0; ele<(inputBranchArrayNamesAndVals[0].find(cutContainer[0].getCutName()))->second.size(); ele++){
			 Float_t eta = inputBranchArrayNamesAndVals[0].find("etaHltEle")->second.at(ele);
			 Float_t dR = inputBranchArrayNamesAndVals[0].find("deltaRHltEle")->second.at(ele);
			 if(fabs(eta) <= 3.0 && fabs(eta) >= 2.5){
			      if(bkgndPosition == string::npos){
				   //this chain corresponds to matched signal. look at the candidate with the smallest
				   //dR value less than 0.15
				   if(dR < bestDrFirstChain){
					bestIndexFirstChain = ele;
					bestDrFirstChain = dR;
				   }
			      }//end signal filter
			      else{
				   //use this for bkgnd evts where dR matching is not required
				   indexesFirstChain.push_back(ele);
			      }//end else
			 }//end trackless eta filter
		    }//end loop over elements of an array which is stored in a branch of an input tuple

		    for(unsigned int ele=0; ele<(inputBranchArrayNamesAndVals[1].find(cutContainer[0].getCutName()))->second.size(); ele++){
			 Float_t eta = inputBranchArrayNamesAndVals[1].find("etaHltEle")->second.at(ele);
			 Float_t dR = inputBranchArrayNamesAndVals[1].find("deltaRHltEle")->second.at(ele);
			 if(fabs(eta) < 2.5){
			      if(bkgndPosition == string::npos){
				   //this chain corresponds to matched signal. look at the candidate with the smallest
				   //dR value less than 0.15
				   if(dR < bestDrSecondChain){
					bestIndexSecondChain = ele;
					bestDrSecondChain = dR;
				   }
			      }//end signal filter
			      else{
				   //use this for bkgnd evts (dR matching is not applied) 
				   indexesSecondChain.push_back(ele);
			      }//end else
			 }//end tracked eta filter
		    }//end loop over elements of an array which is stored in a branch of an input tuple

		    //now we know of any matched signal or bkgnd reco objects in the evt which passed the tracker
		    //and trackless EE eta requirements (and dR matching for signal)
		    if(bkgndPosition == string::npos && (bestIndexFirstChain==-1 || bestIndexSecondChain==-1)) continue;	//go to next evt
		    if(bkgndPosition != string::npos && (indexesFirstChain.size()==0 || indexesSecondChain.size()==0) ) continue;

		    for(vector<CutVar>::const_iterator cutIt=cutContainer.begin(); cutIt!=cutContainer.end(); cutIt++){
			 if(bkgndPosition == string::npos){
			      if((*cutIt).getRegion().compare("_utEE")==0 ){
				   if((*cutIt).isThresholdUpperBound()){
					if(inputBranchArrayNamesAndVals[0].find((*cutIt).getCutName())->second.at(bestIndexFirstChain) > (*cutIt).getCurrentThreshold() ){
					     failedTracklessLeg = true;
					     break;	//leave loop over cutContainer elements
					}//end if matched signal entry fails an upper bound cut

				   }//end check to see if cutVar is an upper bound or lower bound

				   else{
					//cutIt points to a lower bound
					if(inputBranchArrayNamesAndVals[0].find((*cutIt).getCutName())->second.at(bestIndexFirstChain) < (*cutIt).getCurrentThreshold() ){
					     failedTracklessLeg = true;
					     break;	//leave loop over cutContainer elements
					}//end if matched signal entry fails an upper bound cut
				   }//end check to see if cutVar is a lower bound 
			      }//end if(CutVar corresponds to a trackless leg threshold)
						
			      else{
				   //CutVar corresponds to a tracked leg threshold
				   if( (*cutIt).getRegion().compare("_tEB")==0 && inputBranchArrayNamesAndVals[1].find("etaHltEle")->second.at(bestIndexSecondChain) < 1.479){
					//cutIt points to a tracked EB cut
				   }//end if(cutIt points to a tracked EB cut and matched tracked signal entry is in tracked EB)
				   else{
					//cutIt points to a tracked EE cut
				   }//end else (cutIt points to a tracked EE cut)
						
			      }//end else (when cut corresponds to a tracked leg threshold) 
					
			 }//check if the two input chains correspond to matched signal tuples

		    }//end loop over CutVar objects in cutContainer
			
	       }//end if(racklessPosition)
			
	       if(failedTrackedLeg) continue;

	       else{
		    //the first element in pInputChains corresponds to a tracked tuple
		    //the second element corresponds to a trackless tuple

		    //now loop over each entry in the array within the map entry
		    //inputBranchArrayNamesAndVals[(*cutIt).getCutName()] 



	       }//end else

	  }//end loop over all evts in input tuples (same number of entries in all input tuples)


		
	  TFile * outTupleFile = new TFile(pathToOutputFile.c_str(),"update");
	  outTupleFile->cd();
	  outputTree->Write();
	  outputTupleFile->Close();
	  return;
	
     }//end if(iCut==0)

     float current = cutContainer[iCut-1].getCurrentThreshold();
     float min = cutContainer[iCut-1].getMinThreshold();
     float max = cutContainer[iCut-1].getMaxThreshold();
     for(float multiplier=0; (current>=min && current<=max); multiplier += 1){
	  //NOTE
	  //in the current CutVar constructor the variable threshVal is always initialized to the minimum threshold value
	  //within this loop update the threshold value to a new value, and call runScan again to move on to the next
	  //cut variable stored in cutContainer.  The number of iterations which are executed within this for loop has
	  //nothing to do with the number of CutVar objects stored in cutContainer!
	  float updatedThreshVal = cutContainer[iCut-1].getCurrentThreshold() + (cutContainer[iCut-1].getThresholdStep())*multiplier;
	  cutContainer[iCut-1].setThresholdValue(updatedThreshVal);
	  runScan(pathToOutputFile,iCut-1);
     }//end loop over all possible values of the cut threshold for a CutVar object in cutContainer

}//end runScan()

#endif
