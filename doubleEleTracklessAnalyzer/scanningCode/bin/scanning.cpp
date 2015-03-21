//#include "TStopwatch.h"
//#include "TString.h"
#include "TList.h"
#include "TTree.h"
#include "TChain.h"
#include "TFriendElement.h"
#include "../interface/Scan.h"
#include <cstdlib>
#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

#define DEBUG

using namespace std;

int main(int argc, char **argv){
	//TStopwatch myClock, globalClock;
	//globalClock.Start();

	//call InitCutVars() first, then InitInputTree(), then InitOutputTree() in scanning.cpp file

	string testFileName = "/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/scanningCode/doc/trial.txt";
	Scan testScan(testFileName);
	testScan.InitCutContainer();
#ifdef DEBUG
	cout<<"\t"<<endl;
	cout<<"there are "<< testScan.numCutVars() <<" CutVar objects in the cutContainer vector"<<endl;
	cout<<"\t"<<endl;
#endif
	
	//declare the primary input chain
	TChain * inputChain = new TChain("recoAnalyzerMatchedTracked/recoTreeBeforeTriggerFiltersMatchedTrackedSignal","");
	inputChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal_analyzer_trees_2.root");
	
	//declare a second input chain which will be added as a friend to the primary input chain
	TChain * inputFriendChain = new TChain("recoAnalyzerMatchedTrackless/recoTreeBeforeTriggerFiltersMatchedTracklessSignal","");
	inputFriendChain->Add("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal_analyzer_trees_2.root");
	
	string friendName = inputFriendChain->GetName();

#ifdef DEBUG
	cout<<"friend name ="<<"\t"<< friendName<<endl;
#endif

	string friendTreeName = friendName.substr(friendName.find("/")+1);
	inputChain->AddFriend(inputFriendChain,friendName.c_str());
	inputChain->GetListOfFriends()->Print();

	//inputChain->Scan((friendName+".nHltEle:nHltEle").c_str(),"","",10);
	// Int_t nHltEleFriend, nHltEle;
	// std::cout << inputChain->SetBranchAddress((friendName+".nHltEle").c_str(), &nHltEleFriend);
	// std::cout << "\t" << inputChain->SetBranchAddress((std::string(inputChain->GetName())+".nHltEle").c_str(), &nHltEle); 
	// std::cout << std::endl;
	// inputChain->GetEntry(10);
	// std::cout << nHltEle << "\t" << nHltEleFriend << std::endl;
	testScan.InitInputNtuple(inputChain);
	TTree * outTree = new TTree("testOutTree","");
	testScan.InitOutputNtuple(outTree);
	cout<<"\t"<<endl;
	cout<<"successfully called Init Input and Output Ntuple methods"<<endl;
	cout<<"\t"<<endl;

	testScan.runScan(testScan.numCutVars());
	cout<<"successfully called runScan() method"<<endl;

	testScan.SaveOutput("testScanTreeOutput.root");

	
	return 0;


}//end main()


