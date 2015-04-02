#include <string>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <TTree.h>
#include <TChain.h>
#include "TObjArray.h"

#define INPUTNELE 1

//use AnalyzeScanResults objects to find the best set of cut values given a set of constraints 
class AnalyzeScanResults{
	public:
		AnalyzeScanResults(std::string txtConfigFileName, Long64_t totalNumEvts):
			_configFile(txtConfigFileName),
			_totalNumberEvts(totalNumEvts){};

   		void InitInputNtuple(TChain *chain); /// \todo add branches specific for input

		/**use this fxn to double check the contents of the configuration txt file
		 * after initializing the input tuple
		 */
		friend std::ostream& operator << (std::ostream& os, const AnalyzeScanResults g){
			TObjArray* branchList = g._inputChain->GetListOfBranches();
			for(Int_t elem=0; elem<branchList->GetEntries(); elem++){
				os<< "declared input branch named \t"<< branchList->At(elem)->GetName();
			}//end loop over branches in _inputChain

			return os;
		}//end friend operator	
 

	private:
		std::string _configFile;	///< path to configuration file with names of input branches
		
		///_totalNumberEvts is not saved in the input tuple, it will need to be filled during runtime
		Long64_t _totalNumberEvts;	///< number of evts from original dataset which were used to make tuples which fed into Scan algo
		
		///_numEvtsPassing and _maxPossibleNumEvtsPassing are stored as branches (under different branch names) in the input tuples
		Long64_t _numEvtsPassing;	///the number of evts passing a set of cuts
		
		/**this variable is the number of evts which pass all pre-scan filters (python module filters on 
		 * reco eta, reco dilepton mass, etc) and actually see the entire space of possible cut value sets
		*/
		Long64_t _maxPossibleNumEvtsPassing;	
		
		TChain* _inputChain;	///pointer to input chain of tuples which were created by scan jobs
		
		typedef std::map<std::string, Float_t[INPUTNELE]> floatBranchMap_t;	///most input branches hold single element Float_t arrays
		floatBranchMap_t _inputArrayBranches;




};//end AnalyzeScanResults class

