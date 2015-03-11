#include "cutVar.h" 
#include "TString.h"
#include <vector>
#include "TTree.h"
#include "TChain.h"


class scan{
	public:
		void initialize(Int_t numVars,TString output,TString treeOneName,TString treeTwoName);
		void setRange(TString varName,Float_t min,Float_t max,Float_t step);
		void runScan();

	private:	
		std::vector<cutVar> cutContainer;	//no emo :)
		TChain * inputChainOne;
		TChain * inputChainTwo;
		TTree * outputTree;
		TString outputFileName;

}//end class scan
