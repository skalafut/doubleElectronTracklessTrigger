//#include "../interface/CutVar.h"
#include "../interface/Scan.h"
//#include "TEntryListArray.h"
#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstddef>

using namespace std;

Scan::Scan(const char * configTxtFileName){
	configFileName = configTxtFileName;
}

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
			float minVal = strtof(minimum.c_str(),NULL);
			float maxVal = strtof(maximum.c_str(),NULL);
			float stepVal = strtof(stepLength.c_str(),NULL);

			//now make a cutVar object, set the name, four floats, and one bool var
			//associated with this object, and add the object to the scan class member 
			//var named cutContainer. This member var is a vector of cutVar objects.
			CutVar cutObject(name,0,minVal,maxVal,stepVal, (setAsUpperBound.compare("y")==0) );
			/*
			cutObject.cutName = name;
			cutObject.threshVal = 0;
			cutObject.minThresh = minVal;
			cutObject.maxThresh = maxVal;
			cutObject.threshStep = stepVal;
			if(setAsUpperBound.compare("y") == 0) cutObject.isUpperBound = true;
			if(setAsUpperBound.compare("y") != 0) cutObject.isUpperBound = false;
			*/
			cutContainer.push_back(cutObject);

		}//end while
		fclose(pConfig);
	}//end if(pConfig != NULL)
}//end InitCutVars()

unsigned int Scan::numCutVars(){
	return cutContainer.size();
}//end numCutVars()

void InitInputTree(){

}//end InitInputTree()

void InitOutputTree(std::string outputFile,std::string outChainName){

}//end InitOutputTree()

/*
void setRange(std::string varName,float min,float max,float step){

}//end setRange()
*/

void runScan(){

}//end runScan()
