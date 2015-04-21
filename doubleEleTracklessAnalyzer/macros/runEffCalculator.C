void runEffCalculator(){
	gROOT->ProcessLine(".L calculateEfficiencies.C+");
	calculateEfficiencies();
}
