#include "../interface/AnalyzeScanResults.h"
//#include "../src/AnalyzeScanResults.cc"
#include "TStopwatch.h"
#include "TTree.h"
#include "TChain.h"
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main(int argc, char **argv){
	///create and start a stopwatch
	TStopwatch globalClock;
	globalClock.Start();

	string cfgFile = "/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/analyzeScanOutput/doc/config.txt";
	
	///create AnalyzeScanResults objects.  All objects have the same tree
	///structure, and thus use the same config file.
	Long64_t nEvtsSig=0, nEvtsHighPtBkgnd=0, nEvtsLowPtBkgnd=0;
	cout<<"input the number of evts which were analyzed to make the signal tuples which went into the scan algo"<<endl;
	cin >> nEvtsSig; 
	cout<<"input the number of evts which were analyzed to make the high pt bkgnd tuples which went into the scan algo"<<endl;
	cin >> nEvtsHighPtBkgnd; 
	cout<<"input the number of evts which were analyzed to make the low pt bkgnd tuples which went into the scan algo"<<endl;
	cin >> nEvtsLowPtBkgnd; 
	
	AnalyzeScanResults signalScanResults(cfgFile,nEvtsSig);
	AnalyzeScanResults highPtBkgndScanResults(cfgFile,nEvtsHighPtBkgnd);
	AnalyzeScanResults lowPtBkgndScanResults(cfgFile,nEvtsLowPtBkgnd);
	
	TChain * sigTuples = new TChain("scanned_tree");
	sigTuples->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/scanned_tuples/*.root");
	signalScanResults.InitInputNtuple(sigTuples);
	cout<< signalScanResults << endl;

	TChain * highPtBkgndTuples = new TChain("scanned_tree");
	highPtBkgndTuples->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_high_pt/scanned_tuples/*.root");
	highPtBkgndScanResults.InitInputNtuple(highPtBkgndTuples);
	cout<< highPtBkgndScanResults << endl;

	TChain * lowPtBkgndTuples = new TChain("scanned_tree");
	lowPtBkgndTuples->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/bkgnd_low_pt/scanned_tuples/*.root");
	lowPtBkgndScanResults.InitInputNtuple(lowPtBkgndTuples);
	cout<< lowPtBkgndScanResults << endl;


	///fill the vectors as inputs for findOptimalCuts()
	float lumi = (0.9)*(pow(10.,34));
	vector<float> rateInputsForHighPtBkgnd;
	rateInputsForHighPtBkgnd.push_back(lumi);
	rateInputsForHighPtBkgnd.push_back((185900000*0.06071)*pow(10.,-36));	///cross section of high pt bkgnd sample in cm squared
	vector<float> rateInputsForLowPtBkgnd;
	rateInputsForLowPtBkgnd.push_back(lumi);
	rateInputsForLowPtBkgnd.push_back((677300000*0.01029)*pow(10.,-36));	///cross section of low pt bkgnd sample in cm squared


	vector<map<string,float> > interestingSetsOfCuts = findOptimalCuts(3.0,signalScanResults,highPtBkgndScanResults,lowPtBkgndScanResults,rateInputsForHighPtBkgnd,rateInputsForLowPtBkgnd);
	for(unsigned int i=0; i<interestingSetsOfCuts.size(); i++){
		cout<<"\t"<<endl;
		cout<<"printing a set of cuts and the resulting trigger performance metrics"<<endl;
		cout<<"\t"<<endl;
		for(map<string,float>::const_iterator mapIt=interestingSetsOfCuts[i].begin(); mapIt!=interestingSetsOfCuts[i].end(); mapIt++){
			cout<< mapIt->first << " = " << mapIt->second <<endl;
		}///end loop over elements in the map (cut values, trigger rate, etc)
	}///end loop over maps in the vector interestingSetsOfCuts
	globalClock.Stop();
	globalClock.Print();

	return 0;

}//end main()

