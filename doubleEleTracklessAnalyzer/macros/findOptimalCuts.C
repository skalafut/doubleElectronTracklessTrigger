#include <TFile.h>
#include <TCanvas.h>
#include <TString.h>
#include <TBranch.h>
#include <TTree.h>
#include <TChain.h>
#include <TObjArray.h>
#include "TCollection.h"
#include <TCut.h>
#include <cmath>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <map>

#define DEBUG

using namespace std;

/**find the sets of cuts which maximize Z->ee trigger efficiency (_nPassing/_nEvents) at
 * different values of the total bkgnd rate
 */
void findOptimalCuts(){
	///declare the tree and file names which are needed to determine the bkgnd rate and Z->ee efficiency
	TString treeNameSignal="master_scanned_tree_signal";
	TString fileNameSignal="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/signal/singleEG25_master_signal_tuple.root";

	TString treeName30to80Bkg="master_scanned_tree_highPtBkgnd";
	TString fileName30to80Bkg="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_high_pt/singleEG25_master_high_pt_bkgnd_tuple.root";

	TString treeName20to30Bkg="master_scanned_tree_lowPtBkgnd";
	TString fileName20to30Bkg="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_low_pt/singleEG25_master_low_pt_bkgnd_tuple.root";

	TString treeName80to170Bkg="master_scanned_tree_veryHighPtBkgnd";
	TString fileName80to170Bkg="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_very_high_pt/singleEG25_master_very_high_pt_bkgnd_tuple.root";

	///declare the TChain objects
	TChain sigbkg(treeNameSignal,"");
	sigbkg.Add(fileNameSignal);
	
	TChain bkg30to80(treeName30to80Bkg,"");
	bkg30to80.Add(fileName30to80Bkg);
	sigbkg.AddFriend(&bkg30to80, "bkg30to80");

	TChain bkg20to30(treeName20to30Bkg,"");
	bkg20to30.Add(fileName20to30Bkg);
	sigbkg.AddFriend(&bkg20to30, "bkg20to30");

	TChain bkg80to170(treeName80to170Bkg,"");
	bkg80to170.Add(fileName80to170Bkg);
	sigbkg.AddFriend(&bkg80to170, "bkg80to170");

	if(sigbkg.GetEntries()!=bkg30to80.GetEntries() || sigbkg.GetEntries()!=bkg20to30.GetEntries() || sigbkg.GetEntries()!=bkg80to170.GetEntries() ){
		std::cerr << "============================== ERROR!!!" << std::endl;
	}

	map<Float_t,ULong64_t> rateToEfficiencyMap;	///< links values of the bkgnd rate to max Z->ee efficiency values
	for(Long64_t init=0; init<sib)
	ULong64_t _nPassingSig = 0, _nEventsSig = 0;
	Float_t rate20to30Bkgnd = 0, rate30to80Bkgnd = 0, rate80to170Bkgnd = 0;
	sigbkg.SetBranchAddress("_nPassing",&_nPassingSig);
	sigbkg.SetBranchAddress("_nEvents",&_nEventsSig);
	sigbkg.SetBranchAddress("bkg20to30.rate",&rate20to30Bkgnd);
	sigbkg.SetBranchAddress("bkg30to80.rate",&rate30to80Bkgnd);
	sigbkg.SetBranchAddress("bkg80to170.rate",&rate80to170Bkgnd);
	for(Long64_t evt=0; evt<sigbkg.GetEntriesFast(); evt++){
		sigbkg.GetEntry(evt);

	}///end loop over entries in sigbkg chain 



}///end findOptimalCuts()
