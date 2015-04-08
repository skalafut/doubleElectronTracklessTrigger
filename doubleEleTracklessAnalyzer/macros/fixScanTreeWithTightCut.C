#include <TFile.h>
#include <TTree.h>
#include <TChain.h>
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <cstddef>

using namespace std;

///this macro is used to fix a TTree which will be used as a template TChain for scan jobs, but needs
///to be pruned of a few ultra-tight sets of cut values
void fixScanTreeWithTightCut(){
	string pathToInputChain = "";
	if(pathToInputChain.empty()){
		cout<<"where is the file containing the input chain?"<<endl;
		return;
	}
	TChain * chainWithTightCut = new TChain("scanned_tree","");
	chainWithTightCut->Add(pathToInputChain.c_str());
	
	string pathToOutputFile = "";
	if(pathToOutputFile.empty()){
		cout<<"where should the output chain be stored?"<<endl;
		return;
	}
	TFile * outputFile = new TFile(pathToOutputFile.c_str(),"recreate");

	string selection = "_nPassing/_nEvents>0.5 && hadEmHltEleutEE>=0.15";
	TChain * chainWithoutTightCut = chainWithTightCut->CopyTree(selection.c_str());
	outputFile->cd();
	chainWithoutTightCut->Write();
	outputFile->Close();

}///end fixScanTreeWithTightCut()
