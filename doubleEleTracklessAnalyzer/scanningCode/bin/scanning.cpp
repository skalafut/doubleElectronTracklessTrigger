//#include "TStopwatch.h"
//#include "TString.h"
//#include "TTree.h"
//#include "TChain.h"
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

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

	char fName[] = "/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/scanningCode/doc/outputFiles.txt";
	vector<string> outFileNames = getFileOutNames(fName);
	for(unsigned int i=0;i<outFileNames.size();i++){
		cout<<"path to output file number "<< i << " is "<< outFileNames[i] <<endl;
	}//end loop over vector of pathnames to output files
	return 0;

}//end main()


