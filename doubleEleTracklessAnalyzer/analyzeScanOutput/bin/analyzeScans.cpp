#include "../interface/AnalyzeScanResults.h"
#include "TStopwatch.h"
#include "TTree.h"
#include "TChain.h"
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv){
	///create and start a stopwatch
	TStopwatch globalClock;
	globalClock.Start();

	string cfgFile = "/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/analyzeScanOutput/doc/config.txt";
	
	///create AnalyzeScanResults objects.  All objects have the same tree
	///structure, and thus use the same config file.
	Long64_t nEvtsSig=0, nEvtsHighPtBkgnd=0;
	cout<<"input the number of evts which were analyzed to make the signal tuples which went into the scan algo"<<endl;
	cin >> nEvtsSig; 
	cout<<"input the number of evts which were analyzed to make the high pt bkgnd tuples which went into the scan algo"<<endl;
	cin >> nEvtsHighPtBkgnd; 
	
	AnalyzeScanResults signalScanResults(cfgFile,nEvtsSig);
	AnalyzeScanResults highPtBkgndScanResults(cfgFile,nEvtsHighPtBkgnd);
	
	TChain * sigTuples = new TChain("scanned_tree");
	sigTuples->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/scanned_tuples/*.root");
	signalScanResults.InitInputNtuple(sigTuples);
	cout<< signalScanResults << endl;

	TChain * highPtBkgndTuples = new TChain("scanned_tree");
	highPtBkgndTuples->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_high_pt/scanned_tuples/*.root");
	highPtBkgndScanResults.InitInputNtuple(highPtBkgndTuples);
	cout<< highPtBkgndScanResults << endl;

	globalClock.Stop();
	globalClock.Print();

	return 0;

}//end main()

