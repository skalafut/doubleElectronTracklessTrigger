#include <TFile.h>
#include <TTree.h>
#include <TChain.h>
#include <string>
#include <iostream>

using namespace std;

///this macro is used to fix a TTree which will be used as a template TChain for scan jobs, but needs
///to be pruned of a few ultra-tight sets of cut values
void fixScanTreeWithTightCut(){
	string pathToInputChain = "/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/scanned_tuples/scanned_signal_tree_4.root";
	//string pathToInputChain = "";
	if(pathToInputChain.empty()){
		cout<<"where is the file containing the input chain?"<<endl;
		return;
	}
	TChain * chainWithTightCut = new TChain("scanned_tree","");
	chainWithTightCut->Add(pathToInputChain.c_str());
	
	string pathToOutputFile = "/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_mostRecent/signal/scanned_tuples/test_fixTightCut_tree_4.root";
	//string pathToOutputFile = "";
	if(pathToOutputFile.empty()){
		cout<<"where should the output chain be stored?"<<endl;
		return;
	}
	TFile * outputFile = new TFile(pathToOutputFile.c_str(),"recreate");

	///put the list of cuts which should be applied in the string var named selection
	string selection = "_nPassing/_nEvents>0.5 && hadEmHltEleutEE>=0.1490";
	TChain * chainWithoutTightCut = (TChain*) chainWithTightCut->CopyTree(selection.c_str());
	chainWithoutTightCut->Scan("*",selection.c_str(),"",10);	///< check that the selection cuts were applied correctly
	outputFile->cd();
	chainWithoutTightCut->Write();
	outputFile->Close();

}///end fixScanTreeWithTightCut()
