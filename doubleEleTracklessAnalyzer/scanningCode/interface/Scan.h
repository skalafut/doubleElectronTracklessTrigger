#include "CutVar.h" 
#include <string>
#include <vector>
#include <map>
//#include "TTree.h"
//#include "TChain.h"


class Scan{
	public:
		//configTxtFile contains names of input tree branches which will be used in optimization (pt, sigmaIEIE, etc),
		//the ranges and step sizes of the threshold cut values, a single character which indicates whether or
		//not the threshold corresponds to an upper bound (like relative ecal iso) or lower bound (pt), and
		//a tag to indicate tracked barrel or endcap which will be used to define the output branch names
		Scan(const char * configTxtFileName);
		
		//void initialize(Int_t numVars,std::string outputFile,std::string treeOneName,std::string treeTwoName);
	
		//call InitCutVars() first, then InitInputTree(), then InitOutputTree() in scanning.cpp file
	
		//this fxn uses member var configFileName to create CutVar objects, and adds them
		//to cutContainer
		void InitCutVars();

		//fxn which returns the number of CutVar objects in the cutContainer vector 
		unsigned int numCutVars();
		
		void InitInputTree();
		void InitOutputTree(std::string outputFile,std::string outChainName);
		//void setRange(std::string varName,float min,float max,float step);
		
		//runScan() consists of three nested for loops.  The outer most loops over elements in cutContainer,
		//the middle loops over possible values of one cut variable (btwn min and max), and the inner most
		//loops over events from the two input TChains 
		void runScan();

	private:
		const char * configFileName;
		std::vector<CutVar> cutContainer;	//no emo :)
		
		//TChain * inputChainOne;
		//TChain * inputChainTwo;
		//TChain * outputChain;
		std::string outputFileName;
		std::map<std::string,float> inputBranchNamesAndVals;
		
		//outputBranch map will have at least 2 more elements than cutContainer
		//one for the number of evts which were analyzed, and another branch which 
		//saves the number of evts passing a set of tracked and trackless leg
		//cut values. The latter branch will have to be hard coded into this map.
		std::map<std::string,float> outputBranchNamesAndVals;


};//end class scan
