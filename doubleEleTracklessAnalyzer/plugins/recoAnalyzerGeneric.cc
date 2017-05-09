// -*- C++ -*-
//
// Package:    doubleElectronTracklessTrigger/recoAnalyzerGeneric
// Class:      recoAnalyzerGeneric
// 
/**\class recoAnalyzerGeneric recoAnalyzerGeneric.cc doubleElectronTracklessTrigger/recoAnalyzerGeneric/plugins/recoAnalyzerGeneric.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Sean Kalafut
//         Created:  Thu, 06 Nov 2014 23:16:33 GMT
//
//


// system include files
#include <memory>
#include <map>
#include <utility>
#include <cstring>
#include <string>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <cmath>
#include <vector>
#include <array>



// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/Candidate/interface/CompositeCandidate.h"

#include "DataFormats/Common/interface/getRef.h"

#include "DataFormats/RecoCandidate/interface/RecoEcalCandidate.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateFwd.h"
#include "DataFormats/RecoCandidate/interface/RecoEcalCandidateIsolation.h"
#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"


#include "DataFormats/EgammaReco/interface/SuperCluster.h"
//#include "DataFormats/EgammaReco/interface/SuperClusterFwd.h"
#include "DataFormats/EgammaReco/interface/ClusterShape.h"
#include "DataFormats/EgammaReco/interface/ClusterShapeFwd.h"
#include "DataFormats/EgammaReco/interface/BasicCluster.h"
#include "DataFormats/EgammaReco/interface/BasicClusterFwd.h"
#include "DataFormats/EgammaCandidates/interface/Electron.h"
//#include "DataFormats/EgammaCandidates/interface/ElectronFwd.h"
#include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
//#include "DataFormats/EgammaCandidates/interface/GsfElectronFwd.h"
//#include "DataFormats/HLTReco/interface/TriggerEvent.h" // trigger::TriggerEvent
#include "DataFormats/HLTReco/interface/TriggerObject.h" 
#include "DataFormats/HLTReco/interface/TriggerEventWithRefs.h" 
#include "DataFormats/HLTReco/interface/TriggerFilterObjectWithRefs.h" 
#include "DataFormats/HLTReco/interface/TriggerRefsCollections.h" 
#include "DataFormats/HLTReco/interface/TriggerTypeDefs.h" 



#include "SimDataFormats/GeneratorProducts/interface/HepMCProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidateFwd.h"

#include "DataFormats/ParticleFlowReco/interface/PFCluster.h"
#include "DataFormats/ParticleFlowReco/interface/PFClusterFwd.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecHitFraction.h"
#include "DataFormats/ParticleFlowReco/interface/PFLayer.h"

#include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
#include "DataFormats/ParticleFlowReco/interface/PFRecHitFwd.h"

#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/CaloRecHit/interface/CaloRecHit.h"
#include "DataFormats/CaloRecHit/interface/CaloCluster.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TMath.h"
#include "TH1.h"
#include "TH2.h"
#include "TH3.h"
#include "TAttFill.h"
#include "TAttMarker.h"
#include <TString.h>
#include <TCanvas.h>
#include <TLegend.h>
#include <TStyle.h>
#include <TROOT.h>
#include "TTree.h"

#define NELE 400 


//
// class declaration
//

class recoAnalyzerGeneric : public edm::EDAnalyzer {
   public:
      explicit recoAnalyzerGeneric(const edm::ParameterSet&);
      ~recoAnalyzerGeneric();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
     

void getTriggerObjectsInfo(const edm::Event& iEvent){

	iEvent.getByToken(hltZedMomObjectsTag, hltZedMomObjectsHandle);
	if(!hltZedMomObjectsHandle.isValid() ) return;

	if(analyzingTracked && maxDeltaR < 0){
		iEvent.getByToken(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByToken(HadEmTag,HadEmHandle);
		iEvent.getByToken(HcalIsoTag,HcalIsoHandle);
		iEvent.getByToken(EcalIsoTag,EcalIsoHandle);
		iEvent.getByToken(TrackIsoTag,TrackIsoHandle);
		iEvent.getByToken(DphiTag,DphiHandle);
		iEvent.getByToken(DetaTag,DetaHandle);
		iEvent.getByToken(EpTag,EpHandle);

		iEvent.getByToken(hltObjectsTag, hltObjectsHandle);

		//std::cout<<"setup handles to tracked leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid()) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() || !TrackIsoHandle.isValid() || !DphiHandle.isValid() || !DetaHandle.isValid() || !EpHandle.isValid()) return;

		//std::cout<<"all tracked leg handles are valid"<<std::endl;

		for(unsigned int h=0; h<hltObjectsHandle->size(); h++){
			nHltEle += 1;
		}

		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt, TrackIsoIt, DphiIt, DetaIt, EpIt;
		unsigned int j=0;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			etaHltEle[j] = (*refIt)->eta();
			//std::cout<<"eta = "<< (*refIt)->eta() << std::endl;
			ptHltEle[j] = (*refIt)->pt();
			phiHltEle[j] = (*refIt)->phi();

			//now that I have the eta, pt, and phi of a tracked leg RecoEcalCandidate, I should look for the OBJECTSSS 
			//in hltZedMomObjectsHandle which have a tracked leg daughter particle with matching eta, pt, and phi.
			//of all of the mothers that are found I should save the mass of the highest mass mother in diObjectMassHltEle[j]
			Float_t maxMass = -1;
			for(std::vector<reco::CompositeCandidate>::const_iterator momIt=hltZedMomObjectsHandle->begin(); momIt != hltZedMomObjectsHandle->end();momIt++){
				if((momIt->daughter("trackedRecoEle"))->hasMasterClone() ){
					reco::CandidateBaseRef dauRef = (momIt->daughter("trackedRecoEle"))->masterClone();
					if(dauRef->pt()==ptHltEle[j] && dauRef->eta()==etaHltEle[j] && dauRef->phi()==phiHltEle[j]){
						if(momIt->mass() > maxMass) maxMass = momIt->mass();
					}//end requirement that pt, eta, and phi are identical 

				}//end filter to select tracked leg RecoEcalCandidate obj daughters

			}//end loop over mother reco Z boson objects
			diObjectMassHltEle[j] = maxMass;


			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
			clusterShapeHltEle[j] = SigmaIEIEIt->val;
			HadEmIt = (*HadEmHandle).find(*refIt);
			hadEmHltEle[j] = (HadEmIt->val)/(ptHltEle[j]*(TMath::CosH(etaHltEle[j]) ));
			HcalIsoIt = (*HcalIsoHandle).find(*refIt);
			hcalIsoHltEle[j] = (HcalIsoIt->val)/ptHltEle[j];
			EcalIsoIt = (*EcalIsoHandle).find(*refIt);
			ecalIsoHltEle[j] = (EcalIsoIt->val)/ptHltEle[j];

			TrackIsoIt = (*TrackIsoHandle).find(*refIt);
			trackIsoHltEle[j] = (TrackIsoIt->val)/ptHltEle[j];
			DphiIt = (*DphiHandle).find(*refIt);
			dPhiHltEle[j] = DphiIt->val;
			DetaIt = (*DetaHandle).find(*refIt);
			dEtaHltEle[j] = DetaIt->val;
			EpIt = (*EpHandle).find(*refIt);
			epHltEle[j] = EpIt->val;
			j += 1;
		}//end loop over all entries in hltObjectsHandle

	}//end filter on tracked leg objects 
	
	if(!analyzingTracked && maxDeltaR < 0){
		iEvent.getByToken(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByToken(HadEmTag,HadEmHandle);
		iEvent.getByToken(HcalIsoTag,HcalIsoHandle);
		iEvent.getByToken(EcalIsoTag,EcalIsoHandle);
	
		iEvent.getByToken(hltObjectsTag, hltObjectsHandle);
		
		//std::cout<<"setup handles to trackless leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid()) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() ) return;
	
		//std::cout<<"all trackless leg handles are valid"<<std::endl;

		for(unsigned int h=0; h<hltObjectsHandle->size(); h++){
			nHltEle += 1;
		}

		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt;
		unsigned int j=0;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			etaHltEle[j] = (*refIt)->eta();
			//std::cout<<"eta = "<< (*refIt)->eta() << std::endl;
			ptHltEle[j] = (*refIt)->pt();
			phiHltEle[j] = (*refIt)->phi();

			//now that I have the eta, pt, and phi of a trackless leg RecoEcalCandidate, I should look for the OBJECTSS
			//in hltZedMomObjectsHandle which have a trackless leg daughter particle with matching eta, pt, and phi.
			//out of all of these mothers, I should store the mass of the highest mass mother in diObjectMassHltEle
			Float_t maxMass = -1;
			for(std::vector<reco::CompositeCandidate>::const_iterator momIt=hltZedMomObjectsHandle->begin(); momIt != hltZedMomObjectsHandle->end();momIt++){
				if((momIt->daughter("tracklessRecoEle"))->hasMasterClone() ){
					reco::CandidateBaseRef dauRef = (momIt->daughter("tracklessRecoEle"))->masterClone();
					if(dauRef->pt()==ptHltEle[j] && dauRef->eta()==etaHltEle[j] && dauRef->phi()==phiHltEle[j]){
						if(momIt->mass() > maxMass) maxMass = momIt->mass();
					}//end requirement that pt, eta, and phi are identical 

				}//end filter to select trackless leg RecoEcalCandidate obj daughters

			}//end loop over mother reco Z boson objects
			diObjectMassHltEle[j] = maxMass;
	

			//initialize const_iterators to maps inside for loop using find(edm::Ref)
			SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
			clusterShapeHltEle[j] = SigmaIEIEIt->val;
			HadEmIt = (*HadEmHandle).find(*refIt);
			hadEmHltEle[j] = (HadEmIt->val)/(ptHltEle[j]*(TMath::CosH(etaHltEle[j]) ));
			HcalIsoIt = (*HcalIsoHandle).find(*refIt);
			hcalIsoHltEle[j] = (HcalIsoIt->val)/ptHltEle[j];
			EcalIsoIt = (*EcalIsoHandle).find(*refIt);
			ecalIsoHltEle[j] = (EcalIsoIt->val)/ptHltEle[j];
			j += 1;
		}//end loop over all entries in hltObjectsHandle

	}//end filter on trackless leg objects 

	if(analyzingTracked && maxDeltaR > 0){
		iEvent.getByToken(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByToken(HadEmTag,HadEmHandle);
		iEvent.getByToken(HcalIsoTag,HcalIsoHandle);
		iEvent.getByToken(EcalIsoTag,EcalIsoHandle);
		iEvent.getByToken(TrackIsoTag,TrackIsoHandle);
		iEvent.getByToken(DphiTag,DphiHandle);
		iEvent.getByToken(DetaTag,DetaHandle);
		iEvent.getByToken(EpTag,EpHandle);

		iEvent.getByToken(hltObjectsTag, hltObjectsHandle);
		iEvent.getByToken(genObjectsTag, genObjectsHandle);
		iEvent.getByToken(genZedMomObjectsTag,genZedMomObjectsHandle);

		//std::cout<<"setup handles to tracked leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid() || !genObjectsHandle.isValid() || genObjectsHandle->size()==0 || !genZedMomObjectsHandle.isValid() || genZedMomObjectsHandle->size()==0) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() || !TrackIsoHandle.isValid() || !DphiHandle.isValid() || !DetaHandle.isValid() || !EpHandle.isValid()) return;

		//std::cout<<"all tracked leg handles are valid"<<std::endl;

		edm::OwnVector<reco::Candidate>::const_iterator genIt = genObjectsHandle->begin();
		etaGenEle = genIt->eta();
		ptGenEle = genIt->pt();
		phiGenEle = genIt->phi();
		
		//there will never be more than 1 object in genZedMomObjectsHandle for any signal event
		//see the module process.combEle in hlt_tracklessDoubleElectron_signal.py for more details
		std::vector<reco::CompositeCandidate>::const_iterator genMomIt=genZedMomObjectsHandle->begin();
		diObjectMassGenEle = genMomIt->mass();
		
		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt, TrackIsoIt, DphiIt, DetaIt, EpIt;
		unsigned int j=0;
		double minDR = maxDeltaR;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			Float_t hltEta = (*refIt)->eta();
			Float_t hltPhi = (*refIt)->phi();
	
			deltaRAllHltEle[j] = deltaR(hltEta, hltPhi, etaGenEle, phiGenEle);
			nAllHltEle++;
			j++;
		
			if(deltaR(hltEta, hltPhi, etaGenEle, phiGenEle) < minDR){
				//overwrite the old kinematic and isolation info when a new REC object is found which is closer to the GEN electron
				//thus there will only be one entry in each array per event
				minDR = deltaR(hltEta, hltPhi, etaGenEle, phiGenEle);
				etaHltEle[0] = (*refIt)->eta();
				ptHltEle[0] = (*refIt)->pt();
				phiHltEle[0] = (*refIt)->phi();
				deltaRHltEle[0] = deltaR(etaHltEle[0], phiHltEle[0], etaGenEle, phiGenEle);

				//now that I have the eta, pt, and phi of a tracked leg RecoEcalCandidate, I should look for the OBJECTSS 
				//in hltZedMomObjectsHandle which have a tracked leg daughter particle with matching eta, pt, and phi.
				//Out of all of these mothers, I should store the mass of the highest mass mother object in diObjectMassHltEle
				Float_t maxMass = -1;
				for(std::vector<reco::CompositeCandidate>::const_iterator momIt=hltZedMomObjectsHandle->begin(); momIt != hltZedMomObjectsHandle->end();momIt++){
					if((momIt->daughter("trackedRecoEle"))->hasMasterClone() ){
						reco::CandidateBaseRef dauRef = (momIt->daughter("trackedRecoEle"))->masterClone();
						if(dauRef->pt()==ptHltEle[0] && dauRef->eta()==etaHltEle[0] && dauRef->phi()==phiHltEle[0]){
							if(momIt->mass() > maxMass) maxMass = momIt->mass();
						}//end requirement that pt, eta, and phi are identical 

					}//end filter to select tracked leg RecoEcalCandidate obj daughters

				}//end loop over mother reco Z boson objects
				diObjectMassHltEle[0] = maxMass;


				//initialize const_iterators to maps inside for loop using find(edm::Ref)
				SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
				clusterShapeHltEle[0] = SigmaIEIEIt->val;
				HadEmIt = (*HadEmHandle).find(*refIt);
				hadEmHltEle[0] = (HadEmIt->val)/(ptHltEle[0]*(TMath::CosH(etaHltEle[0]) ));
				HcalIsoIt = (*HcalIsoHandle).find(*refIt);
				hcalIsoHltEle[0] = (HcalIsoIt->val)/ptHltEle[0];
				EcalIsoIt = (*EcalIsoHandle).find(*refIt);
				ecalIsoHltEle[0] = (EcalIsoIt->val)/ptHltEle[0];

				TrackIsoIt = (*TrackIsoHandle).find(*refIt);
				trackIsoHltEle[0] = (TrackIsoIt->val)/ptHltEle[0];
				DphiIt = (*DphiHandle).find(*refIt);
				dPhiHltEle[0] = DphiIt->val;
				DetaIt = (*DetaHandle).find(*refIt);
				dEtaHltEle[0] = DetaIt->val;
				EpIt = (*EpHandle).find(*refIt);
				epHltEle[0] = EpIt->val;
				nHltEle = 1;

			}//end deltaR filter
		
		}//end loop over all entries in hltObjectsHandle

	}//end filter on tracked leg objects which should be matched to one GEN tracked electron 
	
	if(!analyzingTracked && maxDeltaR > 0){
		iEvent.getByToken(SigmaIEIETag,SigmaIEIEHandle);
		iEvent.getByToken(HadEmTag,HadEmHandle);
		iEvent.getByToken(HcalIsoTag,HcalIsoHandle);
		iEvent.getByToken(EcalIsoTag,EcalIsoHandle);
	
		iEvent.getByToken(hltObjectsTag, hltObjectsHandle);
		iEvent.getByToken(genObjectsTag, genObjectsHandle);
		iEvent.getByToken(genZedMomObjectsTag,genZedMomObjectsHandle);

		//std::cout<<"setup handles to trackless leg objects and variables"<<std::endl;
		
		if(!hltObjectsHandle.isValid() || !genObjectsHandle.isValid() || genObjectsHandle->size()==0 || !genZedMomObjectsHandle.isValid() || genZedMomObjectsHandle->size()==0) return;

		if(!SigmaIEIEHandle.isValid() || !HadEmHandle.isValid() || !HcalIsoHandle.isValid() || !EcalIsoHandle.isValid() ) return;
	
		//std::cout<<"all trackless leg handles are valid"<<std::endl;

		edm::OwnVector<reco::Candidate>::const_iterator genIt = genObjectsHandle->begin();
		etaGenEle = genIt->eta();
		ptGenEle = genIt->pt();
		phiGenEle = genIt->phi();
		
		//there will never be more than 1 object in genZedMomObjectsHandle for any signal event
		//see the module process.combEle in hlt_tracklessDoubleElectron_signal.py for more details
		std::vector<reco::CompositeCandidate>::const_iterator genMomIt=genZedMomObjectsHandle->begin();
		diObjectMassGenEle = genMomIt->mass();
	
		typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>, float> > forMapIt;

		//declare const_iterators to maps outside for loop
		forMapIt::const_iterator SigmaIEIEIt, HadEmIt, HcalIsoIt, EcalIsoIt;
		unsigned int j=0;
		double minDR = maxDeltaR;
		for(reco::RecoEcalCandidateRefVector::const_iterator refIt=hltObjectsHandle->begin(); refIt != hltObjectsHandle->end(); refIt++){
			Float_t hltEta = (*refIt)->eta();
			Float_t hltPhi = (*refIt)->phi();

			deltaRAllHltEle[j] = deltaR(hltEta, hltPhi, etaGenEle, phiGenEle);
			nAllHltEle++;
			j++;


			if(deltaR(hltEta, hltPhi, etaGenEle, phiGenEle) < minDR){
				minDR = deltaR(hltEta, hltPhi, etaGenEle, phiGenEle);
				etaHltEle[0] = (*refIt)->eta();
				ptHltEle[0] = (*refIt)->pt();
				phiHltEle[0] = (*refIt)->phi();
				deltaRHltEle[0] = deltaR(etaHltEle[0], phiHltEle[0], etaGenEle, phiGenEle);

				//now that I have the eta, pt, and phi of a trackless leg RecoEcalCandidate, I should look for the OBJECTSSS 
				//in hltZedMomObjectsHandle which have a trackless leg daughter particle with matching eta, pt, and phi.
				//Out of all of these mothers, I should store the mass of the heaviest mother Z object in diObjectMassHltEle
				Float_t maxMass = -1;
				for(std::vector<reco::CompositeCandidate>::const_iterator momIt=hltZedMomObjectsHandle->begin(); momIt != hltZedMomObjectsHandle->end();momIt++){
					if((momIt->daughter("tracklessRecoEle"))->hasMasterClone() ){
						reco::CandidateBaseRef dauRef = (momIt->daughter("tracklessRecoEle"))->masterClone();
						if(dauRef->pt()==ptHltEle[0] && dauRef->eta()==etaHltEle[0] && dauRef->phi()==phiHltEle[0]){
							if(momIt->mass() > maxMass) maxMass = momIt->mass();
						}//end requirement that pt, eta, and phi are identical 

					}//end filter to select trackless leg RecoEcalCandidate obj daughters

				}//end loop over mother reco Z boson objects
				diObjectMassHltEle[0] = maxMass;

				//initialize const_iterators to maps inside for loop using find(edm::Ref)
				SigmaIEIEIt = (*SigmaIEIEHandle).find(*refIt);
				clusterShapeHltEle[0] = SigmaIEIEIt->val;
				HadEmIt = (*HadEmHandle).find(*refIt);
				hadEmHltEle[0] = (HadEmIt->val)/(ptHltEle[0]*(TMath::CosH(etaHltEle[0]) ));
				HcalIsoIt = (*HcalIsoHandle).find(*refIt);
				hcalIsoHltEle[0] = (HcalIsoIt->val)/ptHltEle[0];
				EcalIsoIt = (*EcalIsoHandle).find(*refIt);
				ecalIsoHltEle[0] = (EcalIsoIt->val)/ptHltEle[0];
				nHltEle = 1;
			}//end deltaR filter

		}//end loop over all entries in hltObjectsHandle

	}//end filter on trackless leg objects which should be matched to one trackless GEN electron 

}//end getTriggerObjectsInfo()


private:
virtual void beginJob() override;
virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
virtual void endJob() override;


//virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
//virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
//virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

// ----------member data ---------------------------

typedef edm::AssociationMap<edm::OneToValue<std::vector<reco::RecoEcalCandidate>,float,unsigned int> > ecalCandToValMap;

//handles and inputTags to AssociationMaps for RecoEcalCandidate objects 
edm::Handle<ecalCandToValMap> SigmaIEIEHandle;
edm::EDGetToken SigmaIEIETag;

edm::Handle<ecalCandToValMap> HadEmHandle;
edm::EDGetToken HadEmTag;

edm::Handle<ecalCandToValMap> EcalIsoHandle;
edm::EDGetToken EcalIsoTag;

edm::Handle<ecalCandToValMap> HcalIsoHandle;
edm::EDGetToken HcalIsoTag;

edm::Handle<ecalCandToValMap> EpHandle;
edm::EDGetToken EpTag;

edm::Handle<ecalCandToValMap> DetaHandle;
edm::EDGetToken DetaTag;

edm::Handle<ecalCandToValMap> DphiHandle;
edm::EDGetToken DphiTag;

edm::Handle<ecalCandToValMap> TrackIsoHandle;
edm::EDGetToken TrackIsoTag;


//RecoEcalCandidate and reco::Candidate handles, relevant EDGetTokens, and tree variables
//edm::Handle<std::vector<reco::RecoEcalCandidate> > hltObjectsHandle;
edm::Handle<reco::RecoEcalCandidateRefVector> hltObjectsHandle;
//original std::vector<edm::Ref<reco::RecoEcalCandidateCollection> > hltRefs;
//equivalent to original const edm::RefVector<std::vector<reco::RecoEcalCandidate>> hltRefs;

edm::Handle<std::vector<reco::CompositeCandidate>> hltZedMomObjectsHandle;

edm::Handle<edm::OwnVector<reco::Candidate> > genObjectsHandle;
edm::Handle<std::vector<reco::CompositeCandidate>> genZedMomObjectsHandle;

std::string tName;

edm::EDGetToken hltObjectsTag;

bool analyzingTracked;
edm::EDGetToken genObjectsTag;
double maxDeltaR;
edm::EDGetToken hltZedMomObjectsTag;
edm::EDGetToken genZedMomObjectsTag;

TTree * tree;

Int_t nHltEle;
Int_t nAllHltEle;	///< for matched evts
Float_t etaHltEle[NELE];
Float_t ptHltEle[NELE];
Float_t phiHltEle[NELE];
Float_t clusterShapeHltEle[NELE];
Float_t hadEmHltEle[NELE];
Float_t ecalIsoHltEle[NELE];
Float_t hcalIsoHltEle[NELE];
Float_t epHltEle[NELE];
Float_t dEtaHltEle[NELE];
Float_t dPhiHltEle[NELE];
Float_t trackIsoHltEle[NELE];

//used to keep track of the mass of the CompositeCandidate objects
//made by the module named combRecoEle 
Float_t diObjectMassHltEle[NELE];

//contains the deltaR value between one REC and a GEN electron in a signal evt
Float_t deltaRHltEle[NELE];

///contains the dR value btwn all RECs and a GEN electron in a signal evt
Float_t deltaRAllHltEle[NELE];


//GEN electron eta, pt, phi
//there will only be one GEN electron relevant to each entry in the tree
Float_t etaGenEle;
Float_t ptGenEle;
Float_t phiGenEle;

//invariant mass of the parent GEN particle whose daughter GEN electron
//is matched to a RecoEcalCandidate produced by the trigger
Float_t diObjectMassGenEle;

Int_t runNumber;
Long64_t evtNumber;
Double_t rescaledEvtNumber;



};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
//the order of private member vars which are initialized using iConfig.getParameter<>() is important!
recoAnalyzerGeneric::recoAnalyzerGeneric(const edm::ParameterSet& iConfig):
	SigmaIEIETag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("SigmaIEIE")) ),
	HadEmTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("HadEm")) ),
	EcalIsoTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("EcalIso")) ),
	HcalIsoTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("HcalIso")) ),
	EpTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("Ep")) ),
	DetaTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("Deta")) ),
	DphiTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("Dphi")) ),
	TrackIsoTag( consumes<ecalCandToValMap>(iConfig.getParameter<edm::InputTag>("TrackIso")) ),
	tName(iConfig.getParameter<std::string>("treeName")),
	hltObjectsTag( consumes<reco::RecoEcalCandidateRefVector>(iConfig.getParameter<edm::InputTag>("recoElectronCollection")) ),
	analyzingTracked(iConfig.getParameter<bool>("doAnalysisOfTracked")),
	genObjectsTag( consumes<edm::OwnVector<reco::Candidate> >(iConfig.getParameter<edm::InputTag>("genCollection")) ),
	maxDeltaR(iConfig.getParameter<double>("dRMatch")),
	hltZedMomObjectsTag( consumes<std::vector<reco::CompositeCandidate> >(iConfig.getParameter<edm::InputTag>("recoZedCollection")) ),
	genZedMomObjectsTag( consumes<std::vector<reco::CompositeCandidate> >(iConfig.getParameter<edm::InputTag>("genZedCollection")) )

{
   //now do what ever initialization is needed
   edm::Service<TFileService> fs;
   //hltZedMomObjectsTag
   tree=fs->make<TTree>(tName.c_str(),"RecoEcalCandidate object information before any trigger filters are applied");
  
   //RecoEcalCandidate object branches
   tree->Branch("nHltEle",&nHltEle,"nHltEle/I");
   tree->Branch("nAllHltEle",&nAllHltEle,"nAllHltEle/I");
   tree->Branch("etaHltEle",etaHltEle,"etaHltEle[nHltEle]/F");
   tree->Branch("ptHltEle",ptHltEle,"ptHltEle[nHltEle]/F");
   tree->Branch("phiHltEle",phiHltEle,"phiHltEle[nHltEle]/F");
   tree->Branch("clusterShapeHltEle",clusterShapeHltEle,"clusterShapeHltEle[nHltEle]/F");
   tree->Branch("hadEmHltEle",hadEmHltEle,"hadEmHltEle[nHltEle]/F");
   tree->Branch("ecalIsoHltEle",ecalIsoHltEle,"ecalIsoHltEle[nHltEle]/F");
   tree->Branch("hcalIsoHltEle",hcalIsoHltEle,"hcalIsoHltEle[nHltEle]/F");
   tree->Branch("epHltEle",epHltEle,"epHltEle[nHltEle]/F");
   tree->Branch("dEtaHltEle",dEtaHltEle,"dEtaHltEle[nHltEle]/F");
   tree->Branch("dPhiHltEle",dPhiHltEle,"dPhiHltEle[nHltEle]/F");
   tree->Branch("trackIsoHltEle",trackIsoHltEle,"trackIsoHltEle[nHltEle]/F");
   tree->Branch("diObjectMassHltEle",diObjectMassHltEle,"diObjectMassHltEle[nHltEle]/F");
   tree->Branch("deltaRHltEle",deltaRHltEle,"deltaRHltEle[nHltEle]/F");
   tree->Branch("deltaRAllHltEle",deltaRAllHltEle,"deltaRAllHltEle[nAllHltEle]/F");
 

   //GEN electron branches
   tree->Branch("etaGenEle",&etaGenEle,"etaGenEle/F");
   tree->Branch("ptGenEle",&ptGenEle,"ptGenEle/F");
   tree->Branch("phiGenEle",&phiGenEle,"phiGenEle/F");
   tree->Branch("diObjectMassGenEle",&diObjectMassGenEle,"diObjectMassGenEle/F");


   //branches unrelated to REC objects
   tree->Branch("evtNumber",&evtNumber,"evtNumber/l");
   tree->Branch("runNumber",&runNumber,"runNumber/I");
   tree->Branch("rescaledEvtNumber",&rescaledEvtNumber,"rescaledEvtNumber/D");

}


recoAnalyzerGeneric::~recoAnalyzerGeneric()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
recoAnalyzerGeneric::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
	using namespace edm;

	/*
	 * reference code for computing di-object mass, using the two RecoEcalCandidate objects which fired the trigger
	if(matched_tracked_pT_ > 1. && matched_pT_ > 1.){
		//if this is true then compute the dilepton mass of the two HLT objects which fired the trigger
		double hlt_mLLSqd = 2*matched_tracked_pT_*matched_pT_*(TMath::CosH(matched_tracked_eta_ - matched_eta_) - TMath::Cos(matched_tracked_phi_ - matched_phi_) );
		if(hlt_mLLSqd > 0.) hlt_mLL_ = TMath::Sqrt(hlt_mLLSqd);

	}
	*/

	evtNumber = iEvent.id().event();
	runNumber = iEvent.id().run();
	rescaledEvtNumber = TMath::Log(iEvent.id().event());


	nHltEle = 0;
	nAllHltEle = 0;
	
	for(Int_t r=0; r<NELE; r++){
		//set all entries in arrays to zero
		etaHltEle[r]=1000;
		ptHltEle[r]=1000;
		phiHltEle[r]=1000;
		clusterShapeHltEle[r]=1000;
		hadEmHltEle[r]=1000;
		ecalIsoHltEle[r]=1000;
		hcalIsoHltEle[r]=1000;
		epHltEle[r]=1000;
		dEtaHltEle[r]=1000;
		dPhiHltEle[r]=1000;
		trackIsoHltEle[r]=1000;
		diObjectMassHltEle[r]=-1;
		deltaRHltEle[r]=1000;
		deltaRAllHltEle[r]=1000;
		
		etaGenEle=1000;
		ptGenEle=1000;
		phiGenEle=1000;
		diObjectMassGenEle=-1;
	}

	getTriggerObjectsInfo(iEvent);

	//that's all folks!
	tree->Fill();


#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);
#endif
}


// ------------ method called once each job just before starting event loop  ------------
void 
recoAnalyzerGeneric::beginJob()
{
/*
  tree_file = new TFile(foutName.c_str(), "recreate");
  if(tree_file->IsZombie()){
    throw cms::Exception("OutputError") <<  "Output tree not created (Zombie): " << foutName;
    return;
  }
  tree_file->cd();
  
  //now do what ever initialization is needed
  tree = new TTree("selected","selected");
  tree->SetDirectory(tree_file);

  //InitNewTree();
*/

}

// ------------ method called once each job just after ending the event loop  ------------
void 
recoAnalyzerGeneric::endJob() 
{
	//loop over bins of "EventFraction", divide each bin content by totalNumEvents, then reset the bin content to the old content divided by totalNumEvents

	/*
	for(int i=1; i<=getXBins("EventFraction"); i++){
		if( getXBins("EventFraction") < 3) break;	//shouldn't need this, but just in case
	
		std::cout<<"bin # "<< i <<" content equals "<< get1DBinContents("EventFraction",i) <<std::endl;
		set1DBinContents("EventFraction",i, (get1DBinContents("EventFraction",i)/getTotalNumEvents() ) );
		std::cout<<"bin # "<< i <<" content equals "<< get1DBinContents("EventFraction",i) <<std::endl;
	
	}

   std::cout<< "the trackless leg of trigger fired on "<< getNumTriggeredEvents() << " events out of "<< getEfficiencyDenominator() << " total events which should have fired trackless leg of trigger" <<std::endl;
   set1DBinContents("HLTRecoEff",1, getNumTriggeredEvents()/getEfficiencyDenominator());

   */


	/*
  //save the tree into the file
  tree_file->cd();
  tree->Write();
  tree_file->Close();
*/

}

// ------------ method called when starting to processes a run  ------------
/*
void 
recoAnalyzerGeneric::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
recoAnalyzerGeneric::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
recoAnalyzerGeneric::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
recoAnalyzerGeneric::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
recoAnalyzerGeneric::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}


//define this as a plug-in
DEFINE_FWK_MODULE(recoAnalyzerGeneric);
