import ROOT
import array
import math

def makeAndSaveHisto(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath):
	h = ROOT.TH1F(histTitle, histTitle, numBins, xmin, xmax)
	canv = ROOT.TCanvas(canvName,canvName,500,500)
	canv.cd()
	for w in xrange( int(len(someArray) ) ):
		#print 'element number ', w, ' of input array contains ', someArray[w]
		h.Fill(someArray[w])

	h.SetLineColor(2) #1 is black, 2 is red, 3 is lime green, 4 is blue 
	h.SetLineWidth(2)
	h.DrawCopy()	#DrawCopy() must be used here!
	canv.SaveAs(outFilePath,"recreate")

f1 = ROOT.TFile("/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_2_0/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/experiment.root")

t1 = f1.Get("demo/doubleEleTrigger")

PT = []
ETA = []
sigmaIEIE = []
relEcalIso = []
relHadOverEm = []
relHcalIso = []
mLL = []
trackedPT = []
trackedETA = []

#lists for gen quantities/cut efficiencies
leading_gen_pt_cutZero = []
leading_gen_eta_cutZero = []
subleading_gen_pt_cutZero = []
subleading_gen_eta_cutZero = []
leading_gen_pt_cutOne = []
leading_gen_eta_cutOne = []
subleading_gen_pt_cutOne = []
subleading_gen_eta_cutOne = []





for z in xrange(t1.GetEntries() ):
	t1.GetEntry(z)
	if(t1.matched_pT_ > 0.):
		PT.append(t1.matched_pT_)
		ETA.append(t1.matched_eta_)
		sigmaIEIE.append(t1.matched_ecalClusterShape_SigmaIEtaIEta_)
		relEcalIso.append(t1.matched_ecalIso_)
		relHadOverEm.append(t1.matched_hOverE_)
		relHcalIso.append(t1.matched_hcalIso_)
		trackedPT.append(t1.matched_tracked_pT_)
		trackedETA.append(t1.matched_tracked_eta_)
		if(t1.hlt_mLL_ > 0.):
			mLL.append(t1.hlt_mLL_)

numEvts = int(len(PT))
print numEvts, ' fired the trigger'

makeAndSaveHisto(PT, "PTCanv", "PT", 100, 0., 100., "PT.png")
makeAndSaveHisto(ETA, "ETACanv", "ETA", 100, -3.0, 3.0, "ETA.png")
makeAndSaveHisto(sigmaIEIE, "sigmaIEIECanv", "sigmaIEIE", 100, 0., 0.15, "sigmaIEIE.png")
makeAndSaveHisto(relEcalIso, "relEcalIsoCanv", "relEcalIso", 100, 0., 0.9, "relEcalIso.png")
makeAndSaveHisto(relHadOverEm, "relHadOverEmCanv", "relHadOverEm", 100, 0., 1.3, "relHadOverEm.png")
makeAndSaveHisto(relHcalIso, "relHcalIsoCanv", "relHcalIso", 100, 0., 1.3, "relHcalIso.png")
makeAndSaveHisto(mLL, "mLLCanv", "mLL", 100, 0., 200., "mLL.png")
makeAndSaveHisto(trackedPT, "trackedPTCanv", "trackedPT", 100, 0., 100., "trackedPT.png")
makeAndSaveHisto(trackedETA, "trackedETACanv", "trackedETA", 100, -3.0, 3.0, "trackedETA.png")








