#include "../interface/Scan.h"
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
			CutVar cutObject(name,region,0,minVal,maxVal,stepVal, (setAsUpperBound.compare("y")==0) );
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
	for(vector<CutVar>::const_iterator cutIt=cutContainer->begin(); cutIt!=cutContainer->end(); cutIt++){
		string tempName = (*cutIt).getCutName();
		bool foundIdentical = false;
		if(uniqueBranchNames.size()==0) uniqueBranchNames.push_back(tempName);
		else{
			for(vector<string>::const_iterator namesIt=uniqueBranchNames->begin(); namesIt!=uniqueBranchNames->end(); namesIt++){
				if(tempName.compare(*namesIt)==0) foundIdentical=true;
				if(foundIdentical) break;
			}//end loop over uniqueBranchNames vector
			if(!foundIdentical) uniqueBranchNames.push_back(tempName);
		}//end else
	}//end loop over elements in cutContainer
	return uniqueBranchNames;
}//end identifyBranchNames()	

void Scan::InitInputTuple(vector<string> pathToInputTuples,vector<string> inputTupleNames,vector<string> branchNames){
	if(pathToInputTuples.size() != inputTupleNames.size()){
		cout<<"can't initialize input tuples because there are more unique tuple names than paths to tuple files"<<endl;
		cout<<"check that the number of unique input tuple names equals the number of paths to input tuple files"<<endl;
		return;
	}
	
	vector<string>::const_iterator pathIt = pathToInputTuples->begin();
	for(vector<string>::const_iterator tupleIt=inputTupleNames->begin(); tupleIt!=inputTupleNames->end(); tupleIt++){
		pInputChains.push_back(new TChain((*tupleIt).c_str() ,""));
		(pInputChains.back())->Add((*pathIt).c_str() );
		pathIt++;	//not completely confident that this pathIt approach will work 
	}//make a new TChain pointer for every unique tree name

	for(vector<string>::const_iterator brIt=branchNames->begin(); cutIt!=branchNames->end(); cutIt++){
		//add an entry to inputBranchArrayNamesAndVals for each entry in the vector
		//returned by identifyUniqueBranchNames()
		//(*brIt) is the name of a branch in an input file which will be used in the optimization, like
		//ecalIsoHltEle 
		array<float,NELE> inputArray;
		for(unsigned int i=0;i<inputArray.size();i++){ inputArray[i]=0.;}	//initialize all elements to zero
		inputBranchArrayNamesAndVals[(*brIt)]= inputArray;		//should there be an asterisk or ampersand?
		pInputChains->SetBranchAddress((*brIt).c_str(),inputBranchArrayNamesAndVals[(*brIt)]);	//need an asterisk or ampersand in front of map name?
	}//end loop over unique branch names identified pulled from objects in cutContainer

	//add entries to inputBranchArrayNames and inputBranchNames maps, and update pInputChains with map entries, to read in
	//float arrays containing eta, phi, and deltaR values, and float values (one per evt)
	//for the pt, eta, phi of each gen electron, and the float value
	//representing their dilepton mass (at gen level).  These values exist in the bkgnd files
	//as well as the signal files
	array<float,NELE> arrayOne,arrayTwo,arrayThree;
	for(unsigned int j=0;j<arrayOne.size();j++){
		arrayOne[j]=0.;
		arrayTwo[j]=0.;
		arrayThree[j]=0.;
	}//end array initialization
	string arrayOneName="etaHltEle",arrayTwoName="phiHltEle",arrayThreeName="deltaRHltEle";
	inputBranchArrayNamesAndVals[arrayOneName]= arrayOne;
	inputBranchArrayNamesAndVals[arrayTwoName]= arrayTwo;
	inputBranchArrayNamesAndVals[arrayThreeName]= arrayThree;
	pInputChains->SetBranchAddress(arrayOneName.c_str(),arrayOne);
	pInputChains->SetBranchAddress(arrayTwoName.c_str(),arrayTwo);
	pInputChains->SetBranchAddress(arrayThreeName.c_str(),arrayThree);

	float one=0,two=0,three=0,four=0;
	string oneName="etaGenEle",twoName="ptGenEle",threeName="phiGenEle",fourName="diObjectMassGenEle"; 
	inputBranchNamesAndVals[oneName]=one;
	inputBranchNamesAndVals[twoName]=two;
	inputBranchNamesAndVals[threeName]=three;
	inputBranchNamesAndVals[fourName]=four;
	pInputChains->SetBranchAddress(oneName.c_str(),&one);
	pInputChains->SetBranchAddress(twoName.c_str(),&two);
	pInputChains->SetBranchAddress(threeName.c_str(),&three);
	pInputChains->SetBranchAddress(fourName.c_str(),&four);

}//end InitInputTuple()

void Scan::InitOutputTuple(string outputFile,string outChainName){

}//end InitOutputTuple()

/*
void setRange(std::string varName,float min,float max,float step){

}//end setRange()
*/

void Scan::runScan(){

}//end runScan()
