void runCountingMacro(){
	gROOT->ProcessLine(".L countNpassingForAllCutSets.C+");
	countNpassingForAllCutSets();
}
