void runTreeFixMacro(){
	gROOT->ProcessLine(".L fixScanTreeWithTightCut.C+");
	fixScanTreeWithTightCut();
}
