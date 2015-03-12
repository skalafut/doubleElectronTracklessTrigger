#include <string>

//this simple class represents a cut variable used in some selection
//this variable has a name, min value, max value, step size, and
//threshold value between the min and max 

class CutVar{
	public:
		CutVar(std::string str,std::string zone,float val,float min,float max,float step,bool setUpper){
			cutName = str;
			detectorRegion = zone;
			threshVal = val;
			minThresh = min;
			maxThresh = max;
			threshStep = step;
			isUpperBound = setUpper;
		};

		float getMinThreshold(){ return minThresh;};
		float getMaxThreshold(){ return maxThresh;};
		float getThresholdStep(){ return threshStep;};
		float getCurrentThreshold(){ return threshVal;};
		bool isThresholdUpperBound(){ return isUpperBound;};
		std::string getCutName(){ return cutName;};
		std::string getRegion(){ return detectorRegion;};

		void setThresholdValue(float value){ threshVal = value;};

	private:
		//detectorRegion is used to distinguish tracked EB, tracked EE, and trackless EE
		std::string cutName, detectorRegion;
		float threshVal, minThresh, maxThresh, threshStep;
		bool isUpperBound;	//indicates if this cut will be used as an upper bound (someVal < threshVal)
};//end class cutVar

