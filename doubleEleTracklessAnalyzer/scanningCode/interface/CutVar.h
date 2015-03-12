#include <string>

//this simple class represents a cut variable used in some selection
//this variable has a name, min value, max value, step size, and
//threshold value between the min and max 

class CutVar{
	public:
		CutVar(std::string str,float val,float min,float max,float step,bool setUpper){
			cutName = str;
			threshVal = val;
			minThresh = min;
			maxThresh = max;
			threshStep = step;
			isUpperBound = setUpper;
		};

	private:
		std::string cutName;
		float threshVal, minThresh, maxThresh, threshStep;
		bool isUpperBound;	//indicates if this cut will be used as an upper bound (someVal < threshVal)
};//end class cutVar

