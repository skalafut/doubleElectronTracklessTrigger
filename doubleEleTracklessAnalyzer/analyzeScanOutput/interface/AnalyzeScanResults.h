#include <string>
#include <vector>
#include <array>
#include <map>
#include <set>
#include <TTree.h>
#include <TChain.h>
#include "TObjArray.h"
#include "TFile.h"
#include <cstdlib>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <cstddef>
#include <cmath>


#define DEBUG
#define INPUTNELE 1

using namespace std;

//use AnalyzeScanResults objects to find the best set of cut values given a set of constraints 
class AnalyzeScanResults{
	public:
		AnalyzeScanResults(std::string txtConfigFileName, Long64_t totalNumEvts):
			_configFile(txtConfigFileName),
			_totalNumberEvts(totalNumEvts){};

		/**this method links an input TChain to the private member variable _inputChain, and
		 * links the branches in the input TChain to the Float_t arrays in _inputArrayBranches
		 * and the Long64_t values in _numEvtsPassing and _maxPossibleNumEvtsPassing.
		 * _inputArrayBranches, _numEvtsPassing, and _maxPossibleNumEvtsPassing are all private
		 * member variables (as indicated by the leading underscore in each variable name).
		 */
   		void InitInputNtuple(TChain *chain);

		/**use this fxn (function) to double check the contents of the configuration txt file
		 * after initializing the input tuple
		 */
		friend std::ostream& operator << (std::ostream& os, const AnalyzeScanResults g){
			TObjArray* branchList = g._inputChain->GetListOfBranches();
			for(Int_t elem=0; elem<branchList->GetEntries(); elem++){
				os<< "declared input branch named \t"<< branchList->At(elem)->GetName() << std::endl;
			}//end loop over branches in _inputChain

			return os;
		}//end friend output operator

		/**use this method within findOptimalCuts()
		 *
		 */
		/*
		friend void updateCutSetsAndEvtsPassing(std::map<long,std::map<std::string,float> >& mapHoldingMaps,long mapIndx,std::string& evtKey, std::map<std::string,AnalyzeScanResults>::const_iterator& asrMapIt);
		*/

		friend void updateCutSetsAndEvtsPassing(std::map<long,std::map<std::string,Float_t> >& mapHoldingMaps,long mapIndx,string& evtKey, const AnalyzeScanResults& asrRef){
#ifdef DEBUG
			cout<<"in updateCutSetsAndEvtsPassing"<<endl;
#endif
			map<string,Float_t> cutValsAndEvtsPassing;
			if(mapHoldingMaps.empty()){
#ifdef DEBUG
				cout<<"no map between long key and map<string,float> object"<<endl;
#endif
				for(floatBranchMap_t::const_iterator brMapIt=asrRef._inputArrayBranches.begin();
						brMapIt!=asrRef._inputArrayBranches.end(); brMapIt++){
#ifdef DEBUG
					cout<<"cut variable named"<<"\t"<<brMapIt->first <<"\t equals \t"<< (brMapIt->second)[0]<<endl;
#endif
					cutValsAndEvtsPassing[(brMapIt->first)]=(brMapIt->second)[0];	///<BE CAREFUL there is only one element in each Float_t array
				}///end loop over array branches  NOTE each branch has only one element
#ifdef DEBUG
				cout<<"num evts passing equals \t"<< asrRef._numEvtsPassing <<endl;
#endif
				cutValsAndEvtsPassing[evtKey]=asrRef._numEvtsPassing;
				mapHoldingMaps[mapIndx]=cutValsAndEvtsPassing;
#ifdef DEBUG
				cout<<"added a map<string,float> object and long key value to a map of maps"<<endl;
#endif
			}///end if(mapHoldingMaps is empty)

			else{
				///check if this set of cut values already exists in tempBkgndMap
				///if it does, increment the number of evts passing stored in the map by the current value of _numEvtsPassing
				///otherwise, make a new entry in the vector with the new set of cut values and the number of evts passing this set of cuts
				bool foundUniqueCutSet = true;
				long evtNumWithSameCutSet;

#ifdef DEBUG
				cout<<"map of maps has at least one element"<<endl;
#endif

				///fill cutValsAndEvtsPassing, then look to see if the cut values in the map have already been put into mapHoldingMaps
				for(floatBranchMap_t::const_iterator brMapIt=asrRef._inputArrayBranches.begin();
						brMapIt!=asrRef._inputArrayBranches.end(); brMapIt++){
					cutValsAndEvtsPassing[(brMapIt->first)]=(brMapIt->second)[0];	///<BE CAREFUL there is only one element in each Float_t array
				}///end loop over array branches  NOTE each branch has only one element
				cutValsAndEvtsPassing[evtKey]=asrRef._numEvtsPassing;

				///check if the cut values in cutValsAndEvtsPassing already exist in mapHoldingMaps
				for(map<long,map<string,Float_t> >::const_iterator tempMapIt=mapHoldingMaps.begin(); tempMapIt!=mapHoldingMaps.end(); tempMapIt++){
					bool brokeOutOfInner = false;
					for(map<string,Float_t>::const_iterator innerTmpIt=(tempMapIt->second).begin();
							innerTmpIt!=(tempMapIt->second).end(); innerTmpIt++){
						///innerTmpIt is a map<string,float> iterator, so I can call ->first and ->second on innerTmpIt 
						if(innerTmpIt->second != (cutValsAndEvtsPassing.find(innerTmpIt->first))->second){
							brokeOutOfInner = true;
							break;
						}///end check for duplicate set of cut values 
					}///end loop over the entries in a map stored within mapHoldingMaps
					///if brokeOutOfInner is false, then the set of cut values in cutValsAndEvtsPassing is not unique
					if(!brokeOutOfInner){
						foundUniqueCutSet = false;
						evtNumWithSameCutSet = tempMapIt->first;
						break;
					}
				}///end loop over entries in mapHoldingMaps (a map of maps)
				if(foundUniqueCutSet){
					mapHoldingMaps[mapIndx] = cutValsAndEvtsPassing;
				}
				else{
					///if the set of cut vals is not unique, find the map in mapHoldingMaps with the duplicate set of cut vals
					///and increment the number of bkgnd evts passing
					float oldNumEvts = (mapHoldingMaps[evtNumWithSameCutSet].find(evtKey))->second;
					float newNumEvts = oldNumEvts + cutValsAndEvtsPassing[evtKey];
#ifdef DEBUG
					cout<<"found a duplicate set of cut vals"<<endl;
					cout<<"the old number of evts passing this set of cuts was"<<endl;
					cout<< oldNumEvts <<endl;
#endif
					mapHoldingMaps[evtNumWithSameCutSet].at(evtKey) = newNumEvts;
#ifdef DEBUG
					cout<<"the new number of evts passing this set of cuts is"<<endl;
					cout<< (mapHoldingMaps[evtNumWithSameCutSet].find(evtKey))->second <<endl;
#endif				
				}///the set of cut vals in cutValsAndEvtsPassing is not unique

			}///end filter mapHoldingMaps is not empty
#ifdef DEBUG
			cout<<"leaving updateCutSetsAndEvtsPassing method"<<endl;
#endif

		};///end updateCutSetsAndEvtsPassing


		/*
		friend void updateCutSetsAndEvtsPassing(std::map<long,std::map<std::string,float> >& mapHoldingMaps,long mapIndx,string& evtKey, map<string,AnalyzeScanResults>::const_iterator& asrMapIt){
#ifdef DEBUG
			cout<<"in updateCutSetsAndEvtsPassing"<<endl;
#endif
			map<string,float> cutValsAndEvtsPassing;
			if(mapHoldingMaps.empty()){
#ifdef DEBUG
				cout<<"no map between long key and map<string,float> object"<<endl;
#endif
				for(floatBranchMap_t::const_iterator brMapIt=(asrMapIt->second)._inputArrayBranches.begin();
						brMapIt!=(asrMapIt->second)._inputArrayBranches.end(); brMapIt++){
					cutValsAndEvtsPassing[(brMapIt->first)]=(brMapIt->second)[0];	///<BE CAREFUL there is only one element in each Float_t array
				}///end loop over array branches  NOTE each branch has only one element
				cutValsAndEvtsPassing[evtKey]=(asrMapIt->second)._numEvtsPassing;
				mapHoldingMaps[mapIndx]=cutValsAndEvtsPassing;
#ifdef DEBUG
				cout<<"added a map<string,float> object and long key value to a map of maps"<<endl;
#endif
			}///end if(mapHoldingMaps is empty)

			else{
				///check if this set of cut values already exists in tempBkgndMap
				///if it does, increment the number of evts passing stored in the map by the current value of _numEvtsPassing
				///otherwise, make a new entry in the vector with the new set of cut values and the number of evts passing this set of cuts
				bool foundUniqueCutSet = true;
				long evtNumWithSameCutSet;

#ifdef DEBUG
				cout<<"map of maps has at least one element"<<endl;
#endif

				///fill cutValsAndEvtsPassing, then look to see if the cut values in the map have already been put into mapHoldingMaps
				for(floatBranchMap_t::const_iterator brMapIt=(asrMapIt->second)._inputArrayBranches.begin();
						brMapIt!=(asrMapIt->second)._inputArrayBranches.end(); brMapIt++){
					cutValsAndEvtsPassing[(brMapIt->first)]=(brMapIt->second)[0];	///<BE CAREFUL there is only one element in each Float_t array
				}///end loop over array branches  NOTE each branch has only one element
				cutValsAndEvtsPassing[evtKey]=(asrMapIt->second)._numEvtsPassing;

				///check if the cut values in cutValsAndEvtsPassing already exist in mapHoldingMaps
				for(map<long,map<string,float> >::const_iterator tempMapIt=mapHoldingMaps.begin(); tempMapIt!=mapHoldingMaps.end(); tempMapIt++){
					bool brokeOutOfInner = false;
					for(map<string,float>::const_iterator innerTmpIt=(tempMapIt->second).begin();
							innerTmpIt!=(tempMapIt->second).end(); innerTmpIt++){
						///innerTmpIt is a map<string,float> iterator, so I can call ->first and ->second on innerTmpIt 
						if(innerTmpIt->second != (cutValsAndEvtsPassing.find(innerTmpIt->first))->second){
							brokeOutOfInner = true;
							break;
						}///end check for duplicate set of cut values 
					}///end loop over the entries in a map stored within mapHoldingMaps
					///if brokeOutOfInner is false, then the set of cut values in cutValsAndEvtsPassing is not unique
					if(!brokeOutOfInner){
						foundUniqueCutSet = false;
						evtNumWithSameCutSet = tempMapIt->first;
						break;
					}
				}///end loop over entries in mapHoldingMaps (a map of maps)
				if(foundUniqueCutSet){
					mapHoldingMaps[mapIndx] = cutValsAndEvtsPassing;
				}
				else{
					///if the set of cut vals is not unique, find the map in mapHoldingMaps with the duplicate set of cut vals
					///and increment the number of bkgnd evts passing
					float oldNumEvts = (mapHoldingMaps[evtNumWithSameCutSet].find(evtKey))->second;
					float newNumEvts = oldNumEvts + cutValsAndEvtsPassing[evtKey];
#ifdef DEBUG
					cout<<"found a duplicate set of cut vals"<<endl;
					cout<<"the old number of evts passing this set of cuts was"<<endl;
					cout<< oldNumEvts <<endl;
#endif
					mapHoldingMaps[evtNumWithSameCutSet].at(evtKey) = newNumEvts;
#ifdef DEBUG
					cout<<"the new number of evts passing this set of cuts is"<<endl;
					cout<< (mapHoldingMaps[evtNumWithSameCutSet].find(evtKey))->second <<endl;
#endif				
				}///the set of cut vals in cutValsAndEvtsPassing is not unique

			}///end filter mapHoldingMaps is not empty
#ifdef DEBUG
			cout<<"leaving updateCutSetsAndEvtsPassing method"<<endl;
#endif

		};///end updateCutSetsAndEvtsPassing
		*/


		/**this fxn (function) finds the sets of cut values which yield a trigger rate near the input desiredRate
		 * and maximize the Z->ee trigger efficiency.  The input parameters are a desired rate in Hz, 
		 * AnalyzeScanResults class objects tied to signal and bkgnd tuples, and a map with the expected lumi
		 * and cross section values for each type of bkgnd.
		 * Inside this fxn, the trigger rate is calculated only based on the number of bkgnd evts which pass
		 * a set of cut values.  Thus, a higher trigger rate will have a lower uncertainty.
		 * The Z->ee trigger efficiency is calculated by taking the ratio of _numEvtsPassing and
		 * _maxPossibleNumEvtsPassing, so that the reco efficiency does not diminish the Z->ee trigger efficiency.
		 * This fxn returns a vector of maps.  Each map stores the values which constitute one set of cuts, the
		 * trigger rate and uncertainty (bkgnd only), and the Z->ee trigger efficiency.  A vector of maps is returned
		 * to allow the user to identify the best set of cut values.
		 * 
		 * It would be nice to make a more generic function which could be used in other projects (like WR cut optimization),
		 * but I can't quickly think of a way to make a more generic function. 
		 */
		/*
		friend std::vector<std::map<std::string,float> > findOptimalCuts(float desiredRate, const AnalyzeScanResults& signal, std::map<std::string,AnalyzeScanResults> bkgnds, std::map<std::string,std::vector<float> > xSxnsAndLumi);
		*/

		friend vector<map<string,float> > findOptimalCuts(float desiredRate, const AnalyzeScanResults& signal, const AnalyzeScanResults& bkgndOne, const AnalyzeScanResults& bkgndTwo, vector<float> xSxnAndLumiOne, vector<float> xSxnAndLumiTwo){

#ifdef DEBUG
			cout<<"in findOptimalCuts method"<<endl;
#endif

			vector<map<string,float> > mapToReturn;	///< return this map at the end of this fxn
			vector<map<long,map<string,Float_t> > > listOfInterestingCutSets;	///one element in this vector for each element in input 'bkgnds' map
			string evtsPassingKey = "evtsPassing";
			///loop over entries in each bkgnd TChain and find sets of cut values which yield a trigger rate near the desired rate
			map<long,map<string,Float_t> > tempBkgndOneMap;	///use this to hold interesting sets of cut values, and the number of evts passing
			map<long,map<string,Float_t> > tempBkgndTwoMap;	///use this to hold interesting sets of cut values, and the number of evts passing
			for(long evt=0; evt<bkgndOne._inputChain->GetEntriesFast(); evt++){
				bkgndOne._inputChain->GetEntry();
				if(bkgndOne._numEvtsPassing > 0){
					updateCutSetsAndEvtsPassing(tempBkgndOneMap,evt,evtsPassingKey,bkgndOne);
				}

			}///end loop over entries in bkgndOne chain
			listOfInterestingCutSets.push_back(tempBkgndOneMap);
#ifdef DEBUG
			cout<<"added a map of maps to listOfInterestingCutSets vector"<<endl;
#endif

			for(long evt=0; evt<bkgndTwo._inputChain->GetEntriesFast(); evt++){
				bkgndTwo._inputChain->GetEntry();
				if(bkgndTwo._numEvtsPassing > 0){
					updateCutSetsAndEvtsPassing(tempBkgndTwoMap,evt,evtsPassingKey,bkgndTwo);
				}

			}///end loop over entries in bkgndTwo chain
			listOfInterestingCutSets.push_back(tempBkgndTwoMap);


#ifdef DEBUG
			cout<<"leaving findOptimalCuts method"<<endl;
#endif

			return mapToReturn;
		};//end findOptimalCuts()


		/*
		friend vector<map<string,float> > findOptimalCuts(float desiredRate, const AnalyzeScanResults& signal, map<string, AnalyzeScanResults>& bkgnds, map<string,vector<float> > xSxnsAndLumi){

#ifdef DEBUG
			cout<<"in findOptimalCuts method"<<endl;
#endif

			vector<map<string,float> > mapToReturn;	///< return this map at the end of this fxn
			vector<map<long,map<string,float> > > listOfInterestingCutSets;	///one element in this vector for each element in input 'bkgnds' map
			string evtsPassingKey = "evtsPassing";
			int bkgndType = -1;	///<used to distinguish entries in tempBkgndMap which come from different AnalyzeScanResults objects in input map named bkgnds
			///loop over entries in each bkgnd TChain and find sets of cut values which yield a trigger rate near the desired rate
			for(map<string,AnalyzeScanResults>::const_iterator mapIt=bkgnds.begin(); mapIt!=bkgnds.end(); mapIt++){
				bkgndType++;
				map<long,map<string,float> > tempBkgndMap;	///use this to hold interesting sets of cut values, and the number of evts passing
				for(long evt=0; evt<(mapIt->second)._inputChain->GetEntriesFast(); evt++){
					(mapIt->second)._inputChain->GetEntry(evt);
					if((mapIt->second)._numEvtsPassing > 0){
						updateCutSetsAndEvtsPassing(tempBkgndMap,evt,evtsPassingKey,mapIt);
					}///end filter to skip TChain entries where no bkgnd evts pass
				}///end loop over entries in one bkgnd TChain 
			}///end loop over different bkgnd samples (high pt QCD, low pt QCD, etc) stored in bkgnds map

#ifdef DEBUG
			cout<<"leaving findOptimalCuts method"<<endl;
#endif

			return mapToReturn;
		};//end findOptimalCuts()
		*/

	private:
		std::string _configFile;	///< path to configuration file with names of input branches
		
		///_totalNumberEvts is not saved in the input tuple, it will need to be filled during runtime
		long _totalNumberEvts;	///< number of evts from original dataset which were used to make tuples which fed into Scan algo
		
		///_numEvtsPassing and _maxPossibleNumEvtsPassing are stored as branches (under different branch names) in the input tuples
		Long64_t _numEvtsPassing;	///the number of evts passing a set of cuts
		
		/**this variable is the number of evts which pass all pre-scan filters (python module filters on 
		 * reco eta, reco dilepton mass, etc) and actually see the entire space of possible cut value sets
		*/
		Long64_t _maxPossibleNumEvtsPassing;	
		
		TChain* _inputChain;	///pointer to an input tuple 
		
		typedef std::map<std::string, Float_t[INPUTNELE]> floatBranchMap_t;	///most input branches hold single element Float_t arrays
		floatBranchMap_t _inputArrayBranches;



};//end AnalyzeScanResults class


