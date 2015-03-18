#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>
//this simple class represents a cut variable used in some selection
//this variable has a name, min value, max value, step size, and
//threshold value between the min and max 

class CutVar {
public:
     CutVar(std::string cutName_, std::string zone, float val, float min, float max, float step, bool setUpper):
	  _cutName(cutName_),
	  _detectorRegion(zone)
	  {
	       threshVal = val;
	       minThresh = min;
	       maxThresh = max;
	       threshStep = step;
	       isUpperBound = setUpper;
	  };
     /// standard constructor
     CutVar(std::string cutName_, std::string zone):
	  _cutName(cutName_),
	  _detectorRegion(zone){
     };

     inline void setThresholdValue(float value){ threshVal = value;};

     void SetValuesFromString(std::string ranges_){
	  char sign;
	  sscanf(ranges_.c_str(), "[%f,%f,%f,%c]", &minThresh, &maxThresh, &threshStep, &sign);
	  if(sign == '>') isUpperBound=false;
	  else if(sign == '<') isUpperBound=true;
	  else exit(1); /// \todo fix launching exception with error 
     }

     friend std::ostream& operator << (std::ostream& os, const CutVar a){
	  os <<  a._cutName  << "\t[" << std::setprecision(3) << a.minThresh << "," << a.maxThresh << "," << a.threshStep << ",";
	  char c = a.isUpperBound ? '<' : '>';
	  os << c << "]\t" << a._detectorRegion;
	  return os;
     }

public:
     //detectorRegion is used to distinguish tracked EB, tracked EE, and trackless EE
     std::string _cutName, _detectorRegion;
     float threshVal, minThresh, maxThresh, threshStep;
     bool isUpperBound;	//indicates if this cut will be used as an upper bound (someVal < threshVal)
};//end class cutVar

