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


def efficiencyGraph(someXArray, someYArray, canvName, graphTitle, isSignal, doReverseSort, outFilePath):
	numPoints = int( len(someXArray) )
	sortXArray = []
	sortYArray = []
	#sorting the input vectors shouldn't affect the graph
	if(not doReverseSort):
		sortXArray = sorted(someXArray)
		sortYArray = sorted(someYArray)
	#if doReverseSort is True, then the X array should be sorted from low to high (element 1 < element 2)
	#but the Y array should be sorted from high to low (element 1 > element 2 > element 3 ...)
	if(doReverseSort):
		sortXArray = sorted(someXArray)
		sortYArray = sorted(someYArray, reverse=True)
	
	cv = ROOT.TCanvas(canvName, canvName,800,800)
	cv.cd()
	xVect = array.array('f', [])
	yVect = array.array('f', [])
	for a in xrange(numPoints):
		xVect.append( sortXArray[a] )
		yVect.append( sortYArray[a] )
	
	gr = ROOT.TGraph(len(xVect), xVect, yVect)
	gr.SetTitle(graphTitle)
	if(isSignal):
		gr.SetLineColor(4)
	if(not isSignal):
		gr.SetLineColor(2)
	gr.Draw("AB")
	cv.Update()
	cv.Modified()
	cv.SaveAs(outFilePath,"recreate")
	grPainter = ROOT.TGraphPainter()
	grPainter.PaintGraphSimple(gr,"AB")
	return cv



def makeAndSaveGraph(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath):
	#make a histo first, then pass the histogram object to the TGraph constructor TGraph(const TH1* h)
	#draw the graph, and finally save the canvas on which it was drawn
	histo = ROOT.TH1F(histTitle, histTitle, numBins, xmin, xmax)
	histo.SetLineColor(2) #1 is black, 2 is red, 3 is blue
	histo.SetLineWidth(2)
	otherCanv = ROOT.TCanvas(canvName,canvName,800,800)
	otherCanv.cd()
	for w in xrange( int(len(someArray) ) ):
		#print 'element number ', w, ' of input array contains ', someArray[w]
		histo.Fill(someArray[w])

	#FINALLY!! This does what I want.
	graph = ROOT.TGraph(histo)
	graph.Draw("AC")
	otherCanv.Update()
	otherCanv.Modified()
	
	otherCanv.SaveAs(outFilePath,"recreate")
	graphPainter = ROOT.TGraphPainter()
	graphPainter.PaintGraphSimple(graph,"AC")
	return otherCanv


#def efficiency(var, cut, lt=True):
#   global sigTupleLen
#   num = 0
#   for val in var:
#      if (val < cut and lt):
#         num += 1.
#         
#   print float(num), sigTupleLen
#   ratio = float(num)/sigTupleLen
#   return ratio


def calcEff(isUpperLimit, inputArray, critValFromInputArray, effDenom):
	#decide how to act based on isUpperLimit
	#isUpperLimit = True for H/E, ecal iso, hcal iso, and sigma_ietaieta
	#sortedInputArray = sorted(inputArray)	#sortedInputArray[i] < sortedInputArray[i+1]
	inputArrayLen = int( len(inputArray) )
	sortedArray = sorted(inputArray)
	critIndex = 0	#the index at which sortedInputArray[critIndex] is slightly greater than or slightly less than critValFromInputArray
	if(isUpperLimit):
		for g in xrange(inputArrayLen):
			if(critValFromInputArray < sortedArray[g]):
				critIndex = g-1
				break
			if(g == (inputArrayLen -1) ):
				critIndex = g

	if(not isUpperLimit):
		for g in xrange(inputArrayLen):
			if(critValFromInputArray < sortedArray[g]):
				critIndex = (inputArrayLen - g)
				break
			if(g == (inputArrayLen -1) ):
				critIndex = 0
	
	#critIndex = the numerator of efficiency
	#now that I have critIndex, I should return the efficiency (between zero and one)
	efficiency = (critIndex/effDenom)
	return efficiency



f1 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_10kevts_very_loose_trackless_leg.root")
#f2 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/bkgnd_10kevts_very_loose_trackless_leg.root")


t1 = f1.Get("demo/doubleEleTrigger")

#branch variables
#   tree->Branch("numGenLeptonsFromZ_",&numGenLeptonsFromZ_,"numGenLeptonsFromZ_/D");
#   tree->Branch("gen_l1_pT_",&gen_l1_pT_,"gen_l1_pT_/D");
#   tree->Branch("gen_l2_pT_",&gen_l2_pT_,"gen_l2_pT_/D");
#   tree->Branch("gen_l2_eta_",&gen_l2_eta_,"gen_l2_eta_/D");
#   tree->Branch("gen_l1_eta_",&gen_l1_eta_,"gen_l1_eta_/D");
#   tree->Branch("gen_l2_phi_",&gen_l2_phi_,"gen_l2_phi_/D");
#   tree->Branch("gen_l1_phi_",&gen_l1_phi_,"gen_l1_phi_/D");
#   tree->Branch("gen_trackless_eta_",&gen_trackless_eta_,"gen_trackless_eta_/D");
#   tree->Branch("gen_trackless_pT_",&gen_trackless_pT_,"gen_trackless_pT_/D");
#   tree->Branch("gen_trackless_phi_",&gen_trackless_phi_,"gen_trackless_phi_/D");
#   tree->Branch("gen_tracked_eta_",&gen_tracked_eta_,"gen_tracked_eta_/D");
#   tree->Branch("gen_tracked_pT_",&gen_tracked_pT_,"gen_tracked_pT_/D");
#   tree->Branch("gen_tracked_phi_",&gen_tracked_phi_,"gen_tracked_phi_/D");
#   tree->Branch("genTriggeredEvent_",&genTriggeredEvent_,"genTriggeredEvent_/D");
#   tree->Branch("consistentGenAndHLTEvent_",&consistentGenAndHLTEvent_,"consistentGenAndHLTEvent_/D");
#
#
#   tree->Branch("matched_pT_",&matched_pT_,"matched_pT_/D");
#   tree->Branch("matched_eta_",&matched_eta_,"matched_eta_/D");
#   tree->Branch("matched_ecalIso_",&matched_ecalIso_,"matched_ecalIso_/D");
#   tree->Branch("matched_hcalIso_",&matched_hcalIso_,"matched_hcalIso_/D");
#   tree->Branch("matched_ecalClusterShape_",&matched_ecalClusterShape_,"matched_ecalClusterShape_/D");
#   tree->Branch("matched_ecalClusterShape_SigmaIEtaIEta_",&matched_ecalClusterShape_SigmaIEtaIEta_,"matched_ecalClusterShape_SigmaIEtaIEta_/D");
#   tree->Branch("matched_hOverE_",&matched_hOverE_,"matched_hOverE_/D");
#   tree->Branch("numUnmatchedCandidates_",&numUnmatchedCandidates_,"numUnmatchedCandidates_/D");
#
#   tree->Branch("reco_tracked_pT_",&reco_tracked_pT_,"reco_tracked_pT_/D");
#   tree->Branch("reco_tracked_eta_",&reco_tracked_eta_,"reco_tracked_eta_/D");
#   tree->Branch("reco_tracked_phi_",&reco_tracked_phi_,"reco_tracked_phi_/D");
#   tree->Branch("reco_untracked_pT_",&reco_untracked_pT_,"reco_untracked_pT_/D");
#   tree->Branch("reco_untracked_eta_",&reco_untracked_eta_,"reco_untracked_eta_/D");
#   tree->Branch("reco_untracked_phi_",&reco_untracked_phi_,"reco_untracked_phi_/D");


#array vars
sigTuple = []
sigEcalIso = []
sigHcalIso = []
sigHoverE = []
sigSigmaIEIE = []
sigPt = []
sigEta = []
genTracklessPt = []
recoDileptonMass = []

#single number vars
efficiencyDenom = 0	#denominator of efficiency, equal to # of events with one untracked EE gen e- (pT > 15), one tracked gen e- (pT > 27), and the dilepton mass of these two gen electrons exceeds 50 GeV

#eventually swap 1000 for t1.GetEntries()
for z in xrange(t1.GetEntries()):
	#loop over all events that were analyzed to make signal.root
	t1.GetEntry(z)
	#calculate two dilepton mass values for the signal event (dy->ee)
	#one value uses GEN electron kinematics, while the other value uses RECO gsf electron and supercluster kinematics
	if(t1.genTriggeredEvent_ > 0.):
		#calculate dilepton mass of the two GEN electrons
		genDileptonSquared = 0.
		genDileptonSquared += (2)*(t1.gen_tracked_pT_)*(t1.gen_trackless_pT_)*(math.cosh(t1.gen_tracked_eta_ - t1.gen_trackless_eta_) - math.cos(t1.gen_tracked_phi_ - t1.gen_trackless_phi_) )
		genDileptonMass = 0.
		if( genDileptonSquared > 0.):
			genDileptonMass += math.sqrt(genDileptonSquared)
		
		#count events in the efficiency denominator only if the gen lvl dilepton mass exceeds 50 GeV
		if(genDileptonMass > 81. and genDileptonMass < 101.):
			efficiencyDenom += 1.


	if(t1.matched_pT_ > 0. and t1.reco_tracked_pT_ > 0. and t1.reco_untracked_pT_ > 0.):
		sigTuple.append([t1.matched_ecalClusterShape_SigmaIEtaIEta_, t1.matched_ecalIso_/t1.matched_pT_, t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ), t1.matched_ecalIso_/t1.matched_pT_])
		sigEcalIso.append(t1.matched_ecalIso_/t1.matched_pT_)
		sigHcalIso.append(t1.matched_hcalIso_/t1.matched_pT_)
		sigHoverE.append(t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ))
		sigSigmaIEIE.append(t1.matched_ecalClusterShape_SigmaIEtaIEta_)
		sigPt.append(t1.matched_pT_)
		sigEta.append(t1.matched_eta_)
		genTracklessPt.append(t1.gen_trackless_pT_)
		#calculate dilepton mass of the RECO gsf electron and EE supercluster which are matched to the two trigger objects
		recoDileptonSquared = 0.
		recoDileptonSquared += (2)*(t1.reco_tracked_pT_)*(t1.reco_untracked_pT_)*(math.cosh(t1.reco_tracked_eta_ - t1.reco_untracked_eta_) - math.cos(t1.reco_tracked_phi_ - t1.reco_untracked_phi_) )
		if( recoDileptonSquared > 0.):
			recoDileptonMass.append( math.sqrt(recoDileptonSquared) )


#sigTupleLen defined here is equal to the # of events which passed the trackless leg of the trigger
sigTupleLen = float(len(sigTuple))
sigPtLen = int(len(sigPt))
recoDileptonLen = int(len(recoDileptonMass))
maxEff = float(len(sigPt))*(100)/efficiencyDenom

print 'after analyzing 1000 events, efficiency denom equals ', efficiencyDenom
print 'out of 1000 possible events, the trigger fired in this many events ', sigPtLen
print 'max trigger efficiency equals: ', maxEff

sigEff_EcalIso = []
sigEff_HcalIso = []
sigEff_HoverE = []
sigEff_SigmaIEIE = []
sigEff_Pt = []
sigEff_Eta = []

#for loop to fill sigEff_* arrays 
#sigPt, sigEcalIso, sigEff_* should all have the same length
for q in xrange(sigPtLen):
	sigEff_EcalIso.append( calcEff(True, sigEcalIso, sigEcalIso[q], efficiencyDenom ) )
	sigEff_HcalIso.append( calcEff(True, sigHcalIso, sigHcalIso[q], efficiencyDenom ) )
	sigEff_HoverE.append( calcEff(True, sigHoverE, sigHoverE[q], efficiencyDenom ) )
	sigEff_SigmaIEIE.append( calcEff(True, sigSigmaIEIE, sigSigmaIEIE[q], efficiencyDenom ) )
	sigEff_Pt.append( calcEff(False, sigPt, sigPt[q], efficiencyDenom ) )
	sigEff_Eta.append( calcEff(False, sigEta, sigEta[q], efficiencyDenom ) )

#testPt = sorted(sigPt)
#testEff = sorted(sigEff_Pt, reverse = False)
#for q in xrange(sigPtLen):
#	for w in xrange(sigPtLen):
#		if(testPt[w] == sigPt[q]):
#			print 'sigPt element # ', q, ' equals ', sigPt[q]
#			print 'sigEff_Pt element # ', q, ' equals ', sigEff_Pt[q]
#			print 'testEff element # ', w, ' equals ', testEff[w]
#			print ' '


#efficiencyGraph(sigEcalIso,sigEff_EcalIso,"canvEcalIso","Efficiency vs HLT EcalIso/HLT pT",True, False,"../triggerPlots/efficiencies/trigEff_EcalIsoGraph_low_thresholds_Dec_20_1kevts.png")
#efficiencyGraph(sigHcalIso,sigEff_HcalIso,"canvHcalIso","Efficiency vs HcalIso/HLT pT",True, False,"../triggerPlots/efficiencies/trigEff_HcalIsoGraph_low_thresholds_Dec_20_1kevts.png")
#efficiencyGraph(sigHoverE,sigEff_HoverE,"canvHoverE","Efficiency vs HoverE/HLT E",True, False,"../triggerPlots/efficiencies/trigEff_HoverEGraph_low_thresholds_Dec_20_1kevts.png")
#efficiencyGraph(sigSigmaIEIE,sigEff_SigmaIEIE,"canvSigmaIEIE","Efficiency vs HLT #sigma_{i#etai#eta}",True, False,"../triggerPlots/efficiencies/trigEff_SigmaIEIEGraph_low_thresholds_Dec_20_1kevts.png")
#efficiencyGraph(sigPt,sigEff_Pt,"canvPt","Efficiency vs HLT Pt",True, True,"../triggerPlots/efficiencies/trigEff_PtGraph_low_thresholds_Dec_20_1kevts.png")
#efficiencyGraph(sigEta,sigEff_Eta,"canvEta","Efficiency vs HLT Eta",True, True,"../triggerPlots/efficiencies/trigEff_EtaGraph_low_thresholds_Dec_20_1kevts.png")

#makeAndSaveHisto(sigEcalIso, "EcalIsoHistoCanv","EcalIso/HLT pT of HLT object matched to gen trackless electron",100,-0.3,0.5, "../triggerPlots/hltObjectPlots/signal_EcalIsoHisto_low_thresholds_Dec_20_1kevts.png")
#makeAndSaveHisto(sigSigmaIEIE, "SigmaIEIEHistoCanv","#sigma_{i#etai#eta} of HLT object matched to gen trackless electron",100,0.,0.2, "../triggerPlots/hltObjectPlots/signal_SigmaIEIEHisto_low_thresholds_Dec_20_1kevts.png")
#makeAndSaveHisto(sigHcalIso, "HcalIsoHistoCanv","HcalIso/HLT pT of HLT object matched to gen trackless electron",100,-0.3,0.5, "../triggerPlots/hltObjectPlots/signal_HcalIsoHisto_low_thresholds_Dec_20_1kevts.png")
#makeAndSaveHisto(sigHoverE, "HoverEHistoCanv","HoverE/HLT E of HLT object matched to gen trackless electron",100,0.,1, "../triggerPlots/hltObjectPlots/signal_HoverEHisto_low_thresholds_Dec_20_1kevts.png")
#makeAndSaveHisto(sigPt, "PtHistoCanv","Pt of HLT object matched to gen trackless electron",100,0.,250., "../triggerPlots/hltObjectPlots/signal_HLT_matched_PtHisto_low_thresholds_Dec_20_1kevts.png")


#makeAndSaveHisto(genTracklessPt, "genTracklessPtHistoCanv","Pt of trackless gen electron which was matched to an HLT object",100,0.,150., "../triggerPlots/genParticlePlots/signal_gen_trackless_PtHisto_low_thresholds_Dec_20_1kevts.png")




#makeAndSaveHisto(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath)
#makeAndSaveGraph(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath)




