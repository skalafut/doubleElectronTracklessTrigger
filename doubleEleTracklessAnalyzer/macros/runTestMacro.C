void runTestMacro(){
	gROOT->ProcessLine(".L testMacro.C+");
	testMacro();
}
