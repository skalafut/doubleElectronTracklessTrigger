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

f1 = ROOT.TFile("/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/speedTrial_no_early_filter.root")
#f1 = ROOT.TFile("/afs/cern.ch/user/s/skalafut/DoubleElectronHLT_2014/CMSSW_7_3_1_patch2/src/doubleElectronTracklessTrigger/doubleEleTracklessAnalyzer/speedTrial_filter_on_untracked_after_making_genEle.root")

bothGenLeptonsTree = f1.Get("genAnalyzerOne/genElectronsFromZ")
TrackedLeptonsTree = f1.Get("genAnalyzerTwo/genTrackedElectrons")		#evts with at least one tracked electron with pt>27
TracklessLeptonsTree = f1.Get("genAnalyzerThree/genTracklessElectrons")		#evts with at least one trackless electron with pt>15
genTriggeredEvtsTree = f1.Get("genAnalyzerFour/genTriggeredZee")	#evts passing all GEN Z->ee requirements, including dilepton mass

allTracklessPt = []
allTracklessEta = []

for g in xrange(TracklessLeptonsTree.GetEntries() ):
	TracklessLeptonsTree.GetEntry(g)
	numTrackless = int(len(TracklessLeptonsTree.ptGenEle))
	for n in xrange(numTrackless):
		allTracklessPt.append(TracklessLeptonsTree.ptGenEle[n])
		allTracklessEta.append(TracklessLeptonsTree.etaGenEle[n])

makeAndSaveHisto(allTracklessPt,"allTracklessPtCanv","allTracklessPt",50, 0., 120.,"allTracklessPt.png")
makeAndSaveHisto(allTracklessEta,"allTracklessEtaCanv","allTracklessEta",100, -3.0, 3.0,"allTracklessEta.png")


allTrackedPt = []
allTrackedEta = []

for g in xrange(TrackedLeptonsTree.GetEntries() ):
	TrackedLeptonsTree.GetEntry(g)
	numTracked = int(len(TrackedLeptonsTree.ptGenEle))
	for n in xrange(numTracked):
		allTrackedPt.append(TrackedLeptonsTree.ptGenEle[n])
		allTrackedEta.append(TrackedLeptonsTree.etaGenEle[n])

makeAndSaveHisto(allTrackedPt,"allTrackedPtCanv","allTrackedPt",50, 0., 120.,"allTrackedPt.png")
makeAndSaveHisto(allTrackedEta,"allTrackedEtaCanv","allTrackedEta",100, -3.0, 3.0,"allTrackedEta.png")


tupleFilteredTrackedPt = []
tupleFilteredTrackedEta = []
tupleFilteredTracklessPt = []
tupleFilteredTracklessEta = []
tupleFilteredDileptonMass = []

genTriggeredTrackedPt = []
genTriggeredTrackedEta = []
genTriggeredTracklessPt = []
genTriggeredTracklessEta = []
genTriggeredDileptonMass = []

for b in xrange(genTriggeredEvtsTree.GetEntries() ):
	TrackedIndex = -1
	TracklessIndex = -1
	genTriggeredEvtsTree.GetEntry(b)
	if(math.fabs(genTriggeredEvtsTree.etaGenEle[0]) < 2.5):
		TrackedIndex = 0
		TracklessIndex = 1
	if(math.fabs(genTriggeredEvtsTree.etaGenEle[1]) < 2.5):
		TrackedIndex = 1
		TracklessIndex = 0
	genTriggeredTrackedPt.append(genTriggeredEvtsTree.ptGenEle[TrackedIndex])
	genTriggeredTrackedEta.append(genTriggeredEvtsTree.etaGenEle[TrackedIndex])
	genTriggeredTracklessPt.append(genTriggeredEvtsTree.ptGenEle[TracklessIndex])
	genTriggeredTracklessEta.append(genTriggeredEvtsTree.etaGenEle[TracklessIndex])
	genTriggeredDileptonMass.append(genTriggeredEvtsTree.invMassGen)

makeAndSaveHisto(genTriggeredTrackedPt,"genTriggeredTrackedPtCanv","genTriggeredTrackedPt",50, 0., 120.,"genTriggeredTrackedPt.png")
makeAndSaveHisto(genTriggeredTrackedEta,"genTriggeredTrackedEtaCanv","genTriggeredTrackedEta",100, -3.0, 3.0,"genTriggeredTrackedEta.png")
makeAndSaveHisto(genTriggeredTracklessPt,"genTriggeredTracklessPtCanv","genTriggeredTracklessPt",50, 0., 120.,"genTriggeredTracklessPt.png")
makeAndSaveHisto(genTriggeredTracklessEta,"genTriggeredTracklessEtaCanv","genTriggeredTracklessEta",100, -3.0, 3.0,"genTriggeredTracklessEta.png")
makeAndSaveHisto(genTriggeredDileptonMass,"genTriggeredDileptonMassCanv","genTriggeredDileptonMass",100, 0., 120.,"genTriggeredDileptonMass.png")


for z in xrange(bothGenLeptonsTree.GetEntries() ):
	bothGenLeptonsTree.GetEntry(z)
	indexOfTracklessLepton = -1
	indexOfTrackedLepton = -1
	if(bothGenLeptonsTree.ptGenEle[0] > 15 and bothGenLeptonsTree.ptGenEle[1] > 15):
		#look for tracked lepton with pt>27
		if(math.fabs(bothGenLeptonsTree.etaGenEle[0]) < 2.5):
			indexOfTrackedLepton = 0
		if(math.fabs(bothGenLeptonsTree.etaGenEle[1]) < 2.5):
			indexOfTrackedLepton = 1
		if(math.fabs(bothGenLeptonsTree.etaGenEle[0]) > 2.5 and math.fabs(bothGenLeptonsTree.etaGenEle[0]) < 3.0):
			indexOfTracklessLepton = 0
		if(math.fabs(bothGenLeptonsTree.etaGenEle[1]) > 2.5 and math.fabs(bothGenLeptonsTree.etaGenEle[1]) < 3.0):
			indexOfTracklessLepton = 1
		if(indexOfTracklessLepton >= 0 and indexOfTrackedLepton >= 0):
			if(bothGenLeptonsTree.ptGenEle[indexOfTrackedLepton] > 27):
				#an event which passes all GEN Z->ee requirements has been found
				tupleFilteredTrackedPt.append(bothGenLeptonsTree.ptGenEle[indexOfTrackedLepton])
				tupleFilteredTrackedEta.append(bothGenLeptonsTree.etaGenEle[indexOfTrackedLepton])
				tupleFilteredTracklessPt.append(bothGenLeptonsTree.ptGenEle[indexOfTracklessLepton])
				tupleFilteredTracklessEta.append(bothGenLeptonsTree.etaGenEle[indexOfTracklessLepton])
				tupleFilteredDileptonMass.append(bothGenLeptonsTree.invMassGen)

makeAndSaveHisto(tupleFilteredTrackedPt,"tupleFilteredTrackedPtCanv","tupleFilteredTrackedPt",50, 0., 120.,"tupleFilteredTrackedPt.png")
makeAndSaveHisto(tupleFilteredTrackedEta,"tupleFilteredTrackedEtaCanv","tupleFilteredTrackedEta",100, -3.0, 3.0,"tupleFilteredTrackedEta.png")
makeAndSaveHisto(tupleFilteredTracklessPt,"tupleFilteredTracklessPtCanv","tupleFilteredTracklessPt",50, 0., 120.,"tupleFilteredTracklessPt.png")
makeAndSaveHisto(tupleFilteredTracklessEta,"tupleFilteredTracklessEtaCanv","tupleFilteredTracklessEta",100, -3.0, 3.0,"tupleFilteredTracklessEta.png")
makeAndSaveHisto(tupleFilteredDileptonMass,"tupleFilteredDileptonMassCanv","tupleFilteredDileptonMass",100, 0., 120.,"tupleFilteredDileptonMass.png")



#template
#makeAndSaveHisto(listName, "listNameCanv","Title",numBins, minVal, maxVal, "listName.png")
#example
#makeAndSaveHisto(PT, "PTCanv", "PT", 100, 0., 100., "PT.png")





