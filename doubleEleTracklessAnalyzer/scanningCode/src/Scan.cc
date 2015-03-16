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

Scan::Scan(const char * configTxtFileName){ configFileName = configTxtFileName;}

void Scan::InitCutVars(){
	FILE * pConfig = fopen(configFileName,"r");
	ifstream confStrm(configFileName,ifstream::in);
	
	if(pConfig != NULL){
		while(confStrm.peek() != EOF){
			string aLine;
			getline(confStrm,aLine);
			//skip the line if there is no bracket
			size_t openBracket = aLine.find_first_of("[");
			if(openBracket==string::npos) continue;
			size_t closeBracket = aLine.find_first_of("]");
			size_t firstComma = aLine.find_first_of(",");
			size_t secondComma = aLine.find_first_of(",",firstComma+1);
			size_t thirdComma = aLine.find_first_of(",",secondComma+1);

			//now parse the line of text in aLine
			string name = aLine.substr(0,openBracket);
			string minimum = aLine.substr(openBracket+1,firstComma-openBracket-1);
			string maximum = aLine.substr(firstComma+1,secondComma-firstComma-1);
			string stepLength = aLine.substr(secondComma+1,thirdComma-secondComma-1);
			string setAsUpperBound = aLine.substr(thirdComma+1,closeBracket-thirdComma-1);
			string region = aLine.substr(closeBracket+1)
			float minVal = strtof(minimum.c_str(),NULL);
			float maxVal = strtof(maximum.c_str(),NULL);
			float stepVal = strtof(stepLength.c_str(),NULL);

			//now make a cutVar object, set the name, four floats, and one bool var
			//associated with this object, and add the object to the scan class member 
			//var named cutContainer. This member var is a vector of cutVar objects.
			CutVar cutObject(name,region,minVal,minVal,maxVal,stepVal, (setAsUpperBound.compare("y")==0) );
			cutContainer.push_back(cutObject);

		}//end while
		fclose(pConfig);
	}//end if(pConfig != NULL)
}//end InitCutVars()

unsigned int Scan::numCutVars(){
	return cutContainer.size();
}//end numCutVars()

vector<string> identifyUniqueBranchNames(){
	vector<string> uniqueBranchNames;	//the vector which will be returned by this fxn
	for(vector<CutVar>::const_iterator cutIt=cutContainer.begin(); cutIt!=cutContainer.end(); cutIt++){
		string tempName = (*cutIt).getCutName();
		bool foundIdentical = false;
		if(uniqueBranchNames.size()==0) uniqueBranchNames.push_back(tempName);
		else{
			for(vector<string>::const_iterator namesIt=uniqueBranchNames.begin(); namesIt!=uniqueBranchNames.end(); namesIt++){
				if(tempName.compare(*namesIt)==0) foundIdentical=true;
				if(foundIdentical) break;
			}//end loop over uniqueBranchNames vector
			if(!foundIdentical) uniqueBranchNames.push_back(tempName);
		}//end else
	}//end loop over elements in cutContainer
	return uniqueBranchNames;
}//end identifyBranchNames()	

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
	float valOne=0., valTwo=0.;
	string valOneName="nEvtsAnalyzed", valTwoName="nEvtsPassing";
	outputBranchNamesAndVals[valOneName]=valOne;
	outputBranchNamesAndVals[valTwoName]=valTwo;
	outputTree->Branch(valOneName.c_str(),&(outputBranchNamesAndVals[valOneName]),(valOneName + "/f" ).c_str() );
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
		bool failedTrackedEB = false, failedTrackedEE = false, failedTracklessEE = false;
		
		//loop over all entries in the two input tuples
		for(long evt = 0; evt<pInputChains[0]->GetEntries(); evt++){
			pInputChains[0]->GetEntry(evt);
			pInputChains[1]->GetEntry(evt);
	
			//for each event in both trees, loop over all elements in cutContainer
			for(vector<CutVar>::const_iterator cutIt=cutContainer.begin(); cutIt!=cutContainer.end(); cutIt++){
				if(racklessPosition != string::npos){
					//the first element in pInputChains corresponds to a trackless tuple
					//the second element corresponds to a tracked tuple

					//now loop over each element in the array within the map entry
					//inputBranchArrayNamesAndVals[(*cutIt).getCutName()]
					//each branch in the input tuples contains an array of floats, not just a single float, hence
					//we must loop over all elements in each array
					for(array<float>::const_iterator eleOne=(*inputBranchArrayNamesAndVals[(*cutIt).getCutName()]).begin(); eleOne!=(*inputBranchArrayNamesAndVals[(*cutIt).getCutName()]).end(); eleOne++){
					
					}//end loop over elements of an array which is stored in a branch of an input tuple 

				}//end if(racklessPosition)
				
				else{
					//the first element in pInputChains corresponds to a tracked tuple
					//the second element corresponds to a trackless tuple

					//now loop over each entry in the array within the map entry
					//inputBranchArrayNamesAndVals[(*cutIt).getCutName()] 



				}//end else
			}//end loop over all cut variables
		
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
