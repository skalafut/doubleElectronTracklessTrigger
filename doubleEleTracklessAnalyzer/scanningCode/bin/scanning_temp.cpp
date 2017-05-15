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

//#define DEBUG

#define BKGND

//#define SIGNAL

using namespace std;

int main(int argc, char **argv){
	//call InitCutContainer() first read in a list of cut variables, and initialize objects which store their names and the range of cut values over which the scan runs
	//then call InitInputNtuple() to link cut variable objects to branches in the input TTree
	//then call InitOutputNtuple() to setup a tree in the output file whose branches list the cut variables and values over which the scan ran, and the number of events
	//read in and the number passing all cuts
	
	string configFileName;

#ifdef BKGND
	configFileName = "doc/trial_bkgnd.txt";
#endif

#ifdef SIGNAL
	configFileName = "doc/trial_signal.txt";
#endif
	
	Scan fullScan(configFileName);
	fullScan.InitCutContainer();
#ifdef DEBUG
	cout<<"\t"<<endl;
	cout<<"there are "<< fullScan.numCutVars() <<" CutVar objects in the cutContainer vector"<<endl;
	cout<<"\t"<<endl;
#endif
	
	TChain * inputChain;
	TChain * inputFriendChain;

#ifdef BKGND
	inputChain = new TChain("recoAnalyzerTrackedWithL1Filter/recoTreeBeforeTriggerFiltersTrackedBkgndWithL1Filter","");
	inputChain->Add("*.root");
	
	//declare a second input chain which will be added as a friend to the primary input chain
	inputFriendChain = new TChain("recoAnalyzerTracklessWithL1Filter/recoTreeBeforeTriggerFiltersTracklessBkgndWithL1Filter","");
	inputFriendChain->Add("*.root");
#endif

#ifdef SIGNAL
	//the input chain for SIGNAL mode has RECO objects matched to the two GEN electrons produced by the Z decay
	//thus the output from the output from the scanning procedure allows the signal efficiency to be calculated at different cut levels
	inputChain = new TChain("recoAnalyzerMatchedTrackedWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTrackedSignalWithL1Filter","");
	inputChain->Add("*.root");
	
	//declare a second input chain which will be added as a friend to the primary input chain
	inputFriendChain = new TChain("recoAnalyzerMatchedTracklessWithL1Filter/recoTreeBeforeTriggerFiltersMatchedTracklessSignalWithL1Filter","");
	inputFriendChain->Add("*.root");
#endif

	string friendName = inputFriendChain->GetName();

#ifdef DEBUG
	cout<<"friend name ="<<"\t"<< friendName<<endl;
#endif

	string friendTreeName = friendName.substr(friendName.find("/")+1);
	inputChain->AddFriend(inputFriendChain,friendName.c_str());
	inputChain->GetListOfFriends()->Print();

	fullScan.InitInputNtuple(inputChain);
	TTree * outTree = new TTree("scanned_tree","");
	fullScan.InitOutputNtuple(outTree);

	fullScan.runScan(fullScan.numCutVars());
	
	////template chain only needed if runScanUsingTupleInput() is used
	//TChain * templateChain = new TChain("scanned_tree","");
	//templateChain->Add("doc/trimmed_template_scanned_tree.root");
	//fullScan.runScanUsingTupleInput(templateChain);

#ifdef SIGNAL
	fullScan.SaveOutput("scanned_signal_tree.root");
#endif

#ifdef BKGND
	fullScan.SaveOutput("scanned_bkgnd_tree.root");
#endif
	
	
	return 0;

}//end main()


