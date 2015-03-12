#include "CutVar.h" 
#include <string>
#include <vector>
#include <array>
#include <map>
#include "TTree.h"
#include "TChain.h"


class Scan{
	public:
		//configTxtFile contains names of input tree branches which will be used in optimization (pt, sigmaIEIE, etc),
		//the ranges and step sizes of the threshold cut values, a single character which indicates whether or
		//not the threshold corresponds to an upper bound (like relative ecal iso) or lower bound (pt), and
		//a tag to indicate tracked barrel or endcap which will be used to define the output branch names
		Scan(const char * configTxtFileName);
		
		//call InitCutVars() before InitInputTree() and InitOutputTree()
	
		//this fxn uses member var configFileName to create CutVar objects, and adds them
		//to cutContainer
		void InitCutVars();

		//this fxn returns the number of CutVar objects in the cutContainer vector 
		unsigned int numCutVars();

		//this fxn looks at all of the objects in cutContainer and, based on the name of each
		//object, identifies the number of unique branches to create within InitInputTuple()
		std::vector<std::string> identifyUniqueBranchNames();
		
		//this fxn initializes the N input TChain pointers, the entries in the inputBranchNamesAndVals
		//map (both the strings and floats), and calls SetBranchAddress using the map entries
		//the vector<string> objects will be filled with information from two txt files which are read
		//by scanning.cpp, and a call to identifyUniqueBranchNames() by a Scan class object 
		void InitInputTuple(std::vector<std::string> pathToInputTuples,std::vector<std::string> inputTupleNames,std::vector<std::string> branchNames);
		
		void InitOutputTuple(std::string outputFile,std::string outChainName);
		//void setRange(std::string varName,float min,float max,float step);
		
		//runScan() consists of three nested for loops.  The outer most loops over elements in cutContainer,
		//the middle loops over possible values of one cut variable (btwn min and max), and the inner most
		//loops over events from the two input TChains 
		void runScan();

	private:
		const char * configFileName;
		std::vector<CutVar> cutContainer;	//no emo :)
		
		std::vector<TChain*> pInputChains;
		//TChain * outputChain;
		std::string outputFileName;
		std::map<std::string,std::array<float>> inputBranchArrayNamesAndVals;	//branches which have arrays of floats
		std::map<std::string,float> inputBranchNamesAndVals;		//branches with one float per entry
		
		//outputBranch map will have at least 2 more elements than cutContainer
		//one for the number of evts which were analyzed, and another branch which 
		//saves the number of evts passing a set of tracked and trackless leg
		//cut values. The latter branch will have to be hard coded into this map.
		std::map<std::string,float> outputBranchNamesAndVals;


};//end class scan
