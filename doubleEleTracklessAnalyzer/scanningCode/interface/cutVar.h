#include "TString.h"

//this simple class represents a cut variable used in some selection
//this variable has a name, min value, max value, step size, and
//threshold value between the min and max 

class cutVar{
	TString cutName;
	Float_t threshVal, minThresh, maxThresh, threshStep;
}//end class cutVar

