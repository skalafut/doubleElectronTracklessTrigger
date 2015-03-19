//#include "TStopwatch.h"
//#include "TString.h"
//#include "TTree.h"
//#include "TChain.h"
#include "../interface/Scan.h"
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

//use this fxn for testing operations to read text in from a file
void testReadFxns(const char * fName){
	FILE * pF = fopen(fName,"r");
	ifstream testStrm(fName,ifstream::in);
	if(pF != NULL){
		while(testStrm.peek() != EOF){
			string aLine;
			getline(testStrm,aLine);
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
			float minVal = strtof(minimum.c_str(),NULL);
			float maxVal = strtof(maximum.c_str(),NULL);
			float stepVal = strtof(stepLength.c_str(),NULL);
			cout<<"name = "<< name << endl;
			cout<<"minimum = "<< minimum << endl;
			cout<<"minimum = "<< minVal << " using stof fxn"<< endl;
			cout<<"maximum = "<< maximum << endl;
			cout<<"maximum = "<< maxVal << " using stof fxn"<< endl;
			cout<<"stepLength = "<< stepLength << endl;
			cout<<"stepLength = "<< stepVal << " using stof fxn"<< endl;
			cout<<"setAsUpperBound = "<< setAsUpperBound << endl;
			cout<<" "<<endl;

	
		}//end while
	}//end null check

}//end testReadFxns()

//this fxn reads a txt file which specifies the absolute paths to the
//output files (each containing one TTree).  Eventually each output 
//file path name will be assigned to the member variable outputFileName
//in scan class objects. 
vector<string> getFileOutNames(const char * fileName){
	//open the text file, and wrap an ifstream object around it
	FILE * pFile = fopen(fileName,"r");
	ifstream file(fileName,ifstream::in);

	//initialize the vector of strings that will be returned by this fxn
	vector<string> outPaths;

	if(pFile != NULL){
		//use fstream::peek() to leave the while loop
		while(file.peek() != EOF){
			string oneLine;
			getline(file,oneLine);
			cout<< oneLine << endl;
			outPaths.push_back(oneLine);
		}//end while
		fclose(pFile);
	}
	
	return outPaths;

}//end getFileOutNames()

int main(int argc, char **argv){
	//TStopwatch myClock, globalClock;
	//globalClock.Start();

	/*
	char fiName[] = "/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/scanningCode/doc/outputFiles.txt";
	vector<string> outFileNames = getFileOutNames(fiName);
	for(unsigned int i=0;i<outFileNames.size();i++){
		cout<<"path to output file number "<< i << " is "<< outFileNames[i] <<endl;
	}//end loop over vector of pathnames to output files
	*/
	
	//call InitCutVars() first, then InitInputTree(), then InitOutputTree() in scanning.cpp file
	

	char testFileName[] = "/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/scanningCode/doc/thresholdValues.txt";
	//testReadFxns(testFileName);
	Scan testScan(testFileName);
	testScan.InitCutContainer();
	cout<<"there are "<< testScan.numCutVars() <<" CutVar objects in the cutContainer vector"<<endl;
	TChain * inputChain = new TChain("recoAnalyzerMatchedTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignal","");
	inputChain->Add("file.root"); // hard code here the files, you can use wildcards!
	TChain * inputFriendChain = new TChain("recoAnalyzerMatchedTrackless/recoTreeBeforeTriggerFiltersMatchedTracklessSignal","");
	inputFriendChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/*");
	inputChain->AddFriend("recoAnalyzerMatchedTrackless/recoTreeBeforeTriggerFiltersMatchedTracklessSignal");
	testScan.InitInputNtuple(inputChain);
	TTree * outTree = new TTree("testOutTree","");
	testScan.InitOutputNtuple(outTree);
	cout<<"successfully called Init Input and Output Ntuple methods"<<endl;
	
	return 0;


}//end main()


