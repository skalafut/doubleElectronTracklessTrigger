import ROOT
import array
import math

def findOptimalCutValuesAndRateAndEff(matchedSigFile, unmatchedSigFile, bkgndFile, desiredRate, effDenom, sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr, totalBkgndEvts, numBkgndEvtsPassingTrigger, tupleForBkgndEvtsPassingTrig, totalUnmatchedSigEvts, numUnmatchedSigEvtsPassingTrig, tupleForUnmatchedSigEvts):
	#this function takes three file objects, the desired total trigger rate, and Z->ee trigger efficiency denominator, and five 1D vectors as inputs
	#to speed up processing, this function also takes a 5D array capturing the characteristics of all bkgnd evts which fire the trigger, the number of entries in
	#this 5D array, and the total number of bkgnd events which were analyzed and resulted in a small # of evts firing the trigger
	#the five 1D arrays contain cut values for ET, sigma ietaieta, ecal iso/ET, (had/em)/energy, and hcal iso/ET
	#the ET array is sorted from low to high (last element in array is largest value)
	#the other four arrays are sorted from high to low (last element in array is smallest value)
	#numEventsToAnalyze equals the number of events to run over in each tree - 1000, 2000, etc
	#this function calculates the total trigger rate and Z->ee trigger efficiency as a function of the cut variable values
	#and returns a 1D vector with the value of the five cut variables which maximizes the Z->ee trig efficiency, the total trigger rate, and the Z->ee trigger efficiency
	matchedSigTree = matchedSigFile.Get("demo/doubleEleTrigger")
	#unmatchedSigTree = unmatchedSigFile.Get("demo/doubleEleTrigger")
	#bkgndTree = bkgndFile.Get("demo/doubleEleTrigger")
	#print 'declared the three TTree objects in findOptimalCutValuesAndRateAndEff'

	#expected peak luminosity in 2015, in units of 1/(sec * cm^2)
	value = 0.9
	power = math.pow(10,34) 
	peakLumi = value*power 

	#cross section for dy->ee and minbias at 13 TeV in cm^2 (units need to match luminosity units!) 
	signalInPB = 6960
	picoBarnToSquareCm = math.pow(10,-36)
	#dy->ee cross section in units of cm^2
	signalXSxn = signalInPB*picoBarnToSquareCm
	
	#minbias cross section at 13 TeV is approximately 70 millibarns
	minBiasInMB = 70
	milliBarnToPicoBarn = math.pow(10,9)
	#minbias cross section in units of cm^2
	minBiasXSxn = minBiasInMB*milliBarnToPicoBarn*picoBarnToSquareCm

	#make an 11D array which will be returned at the end
	#(ET, sigmaIEIE, ecalIso/ET, had/em/Energy, hcalIso/ET, calculated total trigger rate, Z->ee trig eff, bkgnd rate, num bkgnd evts passing trig, signal rate, num unmatched signal evts passing trig)
	cutsRatesAndEffs = []
	addedElementToCutsRatesEffs = 0

	#vars used in optimization algorithm
	minHltPT = 15.
	totalRate = -0.01
	leftHcalIso = False
	leaveEcalIso = False
	leaveSigmaIEIE = False 
	increaseHcalIsoIterator = False
	magnifyHcalIsoIterator = False

	#loop over all values of the five cut variables
	#sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr
	#for a in xrange( int(len(sortedEtCutArr)) ):
	for b in xrange( int(len(sortedSigmaIEIECutArr)) ):
		for c in xrange( int(len(sortedEcalIsoCutArr)) ):
			for d in xrange( int(len(sortedHoverECutArr)) ):
				hcalIsoIt = 0
				for f in xrange( int(len(sortedHcalIsoCutArr)) ):
					#three variables to count the number of bkgnd evts, unmatched sig evts, and matched sig evts pass all five filters
					numUnmatchedSigEvts = 0.
					numMatchedSigEvts = 0.
					numBkgndEvts = 0.
					#print 'declared the three counter variables which will be used to calculate signal rate, bkgnd rate, and Z->ee trig eff'
					if(magnifyHcalIsoIterator):
						magnifyHcalIsoIterator = False
						increaseHcalIsoIterator = False
						#print 'f equals ', f
						#print 'old hcalIsoIt equals ', hcalIsoIt
						hcalIsoIt += 100
						#print 'new hcalIsoIt equals ', hcalIsoIt
					if(increaseHcalIsoIterator):
						increaseHcalIsoIterator = False
						#print 'f equals ', f
						#print 'old hcalIsoIt equals ', hcalIsoIt
						hcalIsoIt += 20 
						#print 'new hcalIsoIt equals ', hcalIsoIt
	
					if(hcalIsoIt >= (int(len(sortedHcalIsoCutArr))-1) ):
						break
	
					#loop over all signal evts where an HLT object is matched to a gen electron in trackless EE coming from a Z decay
					for i in xrange(matchedSigTree.GetEntries()):
						matchedSigTree.GetEntry(i)
						if(matchedSigTree.genTriggeredEvent_ > 0.):
							#calculate gen di-electron mass, and only analyze evts from matchedSigTree for M_ee btwn 81 and 101 GeV
							genDileptonSquared = 0.
							genDileptonSquared += (2)*(matchedSigTree.gen_tracked_pT_)*(matchedSigTree.gen_trackless_pT_)*(math.cosh(matchedSigTree.gen_tracked_eta_ - matchedSigTree.gen_trackless_eta_) - math.cos(matchedSigTree.gen_tracked_phi_ - matchedSigTree.gen_trackless_phi_) )
							genDileptonMass = 0.
							if(genDileptonSquared > 0.):
								genDileptonMass += math.sqrt(genDileptonSquared)
	
							if(genDileptonMass > 81. and genDileptonMass < 101.):
								if(matchedSigTree.matched_pT_ > minHltPT):
									if(matchedSigTree.matched_ecalClusterShape_SigmaIEtaIEta_ < sortedSigmaIEIECutArr[b]):
										if( (matchedSigTree.matched_ecalIso_/matchedSigTree.matched_pT_) < sortedEcalIsoCutArr[c]):
											if( (matchedSigTree.matched_hOverE_/(matchedSigTree.matched_pT_*(math.cosh(matchedSigTree.matched_eta_)) )) < sortedHoverECutArr[d]):
												if( (matchedSigTree.matched_hcalIso_/matchedSigTree.matched_pT_) < sortedHcalIsoCutArr[hcalIsoIt]):
													numMatchedSigEvts += 1.0
	
					#end loop over matchedSigTree entries to determine # of events with gen M_ee near Z peak which fired trigger
					#begin loop over unmatchedSigTree entries
					for j in xrange(numUnmatchedSigEvtsPassingTrig):
						if(tupleForUnmatchedSigEvts[j][0] > minHltPT):
							if(tupleForUnmatchedSigEvts[j][1] < sortedSigmaIEIECutArr[b]):
								if(tupleForUnmatchedSigEvts[j][2] < sortedEcalIsoCutArr[c]):
									if(tupleForUnmatchedSigEvts[j][3] < sortedHoverECutArr[d]):
										if(tupleForUnmatchedSigEvts[j][4] < sortedHcalIsoCutArr[hcalIsoIt]):
											numUnmatchedSigEvts += 1.0
	
					#end loop over unmatchedSigTree entries to determine # of signal events which fired trigger
					#begin loop over bkgndTree entries
					for k in xrange(numBkgndEvtsPassingTrigger):
						if(tupleForBkgndEvtsPassingTrig[k][0] > minHltPT):
							if(tupleForBkgndEvtsPassingTrig[k][1] < sortedSigmaIEIECutArr[b]):
								if(tupleForBkgndEvtsPassingTrig[k][2] < sortedEcalIsoCutArr[c]):
									if(tupleForBkgndEvtsPassingTrig[k][3] < sortedHoverECutArr[d]):
										if(tupleForBkgndEvtsPassingTrig[k][4] < sortedHcalIsoCutArr[hcalIsoIt]):
											numBkgndEvts += 1.0
					
					#end loop over bkgndTree entries to determine # of bkgnd events which fired trigger
					#now calculate total trigger rate.  If the calculated rate is btwn 0.8 and 1.0 times the desired rate, then calculate the Z->ee efficiency, and save
					#the values of the five cut variables, the total rate, and the Z->ee trigger efficiency
					if(numBkgndEvts < 10):
						break
					bkgndRate = (minBiasXSxn*peakLumi*numBkgndEvts)/totalBkgndEvts
					#print 'bkgnd trigger rate equals ', bkgndRate
					#print 'num bkgnd evts passing trig = ', numBkgndEvts
					#print 'total num bkgnd evts analyzed = ', totalBkgndEvts
					signalRate = (signalXSxn*peakLumi*numUnmatchedSigEvts)/totalUnmatchedSigEvts
					#print 'signal trigger rate equals ', signalRate
					#print 'num unmatched sig evts passing trig = ', numUnmatchedSigEvts
					#print 'total num unmatched sig evts analyzed = ', totalUnmatchedSigEvts
					totalRate = 0.
					totalRate += signalRate + bkgndRate
					#print 'total trigger rate = ', totalRate
					#print 'desired rate = ', desiredRate
					if(totalRate > (5.0)*desiredRate):
						#print 'total rate > 5 times desiredRate'
						increaseHcalIsoIterator = True
						if(totalRate > (20.0)*desiredRate):
							#print 'total rate > 20 times desiredRate'
							magnifyHcalIsoIterator = True
					if(totalRate < (0.79)*desiredRate):
						#print 'total rate < 89% of desired rate'
						leftHcalIso = True
						break
					if(totalRate >= (0.8)*desiredRate and totalRate <= desiredRate and numBkgndEvts >= 10 and numUnmatchedSigEvts >= 10):
						zEff = (numMatchedSigEvts/effDenom)
						cutsRatesAndEffs.append([minHltPT, sortedSigmaIEIECutArr[b], sortedEcalIsoCutArr[c], sortedHoverECutArr[d], sortedHcalIsoCutArr[f], totalRate, zEff, bkgndRate, numBkgndEvts, signalRate, numUnmatchedSigEvts])
						addedElementToCutsRatesEffs += 1
					hcalIsoIt += 1
				
				#end loop over sortedHcalIsoCutArr values
				if(leftHcalIso and d==0):
					#print 'd equals zero and leftHcalIso is True'
					leaveEcalIso = True
					break
			#end loop over sortedHoverECutArr values
			if(leaveEcalIso):
				if(c==0):
					#break out of loop over sortedSigmaIEIECutArr if c==0 and leaveEcalIso==True
					leaveSigmaIEIE = True
				break
		#end loop over sortedEcalIsoCutArr values
		if(leaveSigmaIEIE):
			break
	#end loop over sortedSigmaIEIECutArr values

	#now that the 11D array named cutsRatesAndEffs is filled, I should find the values of the five cut variables which maximize the Z->ee trigger efficiency
	maxEff = 0.
	indexOfMaxEff = 0
	for i in xrange(addedElementToCutsRatesEffs):
		if(cutsRatesAndEffs[i][6] > maxEff):
			maxEff = 0.
			maxEff += cutsRatesAndEffs[i][6]
			indexOfMaxEff = 0
			indexOfMaxEff += i
	
	#end loop over cutsRatesAndEffs
	#fill a 1D array with the five optimal cut values, the trigger rate, the Z->ee trigger efficiency, the bkgnd rate, the num of bkgnd evts passing trig, the signal rate, and the num of signal evts passing trig
	optimalValues = []
	for g in xrange(11):
		optimalValues.append(cutsRatesAndEffs[indexOfMaxEff][g])
	
	return optimalValues



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


#make a TGraphErrors plot showing the Z->ee trigger efficiency on the y axis as a function of the total trigger rate on the x axis
#the Z->ee trigger eff uncertainty can be neglected, but the uncertainty on the total trigger rate should be computed as
#  sqrt[ (bkgndRate/sqrt(numPassingBkgndEvts))^2 + (signalRate/sqrt(numPassingSignalEvts))^2 ]
def effVsRateGraph(zEffArr, zEffErrArr, trigRateArr, trigRateErrArr, graphTitle, outFilePath):
	numPoints = int( len(zEffArr) )
	cv=ROOT.TCanvas("zEff","zEff",800,800)
	cv.cd()
	xArr=array.array('f', [])
	xErrArr=array.array('f', [])
	yArr=array.array('f', [])
	yErrArr=array.array('f', [])
	for b in xrange(numPoints):
		xArr.append(trigRateArr[b])
		xErrArr.append(trigRateErrArr[b])
		yArr.append(zEffArr[b])
		yErrArr.append(zEffErrArr[b])
	
	grErr=ROOT.TGraphErrors(len(xArr), xArr, yArr, xErrArr, yErrArr)
	grErr.SetTitle(graphTitle)
	grErr.SetLineColor(4)
	grErr.Draw("AB")
	cv.Update()
	cv.Modified()
	cv.SaveAs(outFilePath,"recreate")
	grPainter = ROOT.TGraphPainter()
	grPainter.PaintGraphSimple(grErr,"AB")
	return cv


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



f1 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_ALLevts_very_loose_trackless_leg.root")
f2 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/unmatched_signal_ALLevts_very_loose_trackless_leg.root")
#f3 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/bkgnd_10kevts_very_loose_trackless_leg.root")
f3 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/about_20M_bkgnd_evts_very_loose_trackless_leg.root")

#tree for signal evts which fire the trigger and are matched to gen electrons from Z decay
t1 = f1.Get("demo/doubleEleTrigger")

#tree for signal evts which fire the trigger but are not matched to gen electrons
t2 = f2.Get("demo/doubleEleTrigger")

#tree for bkgnd evts which fire the trigger
t3 = f3.Get("demo/doubleEleTrigger")


#array vars
sigTuple = []
sigEcalIso = []
sigHcalIso = []
sigHoverE = []
sigSigmaIEIE = []
sigPt = []
sigEta = []
genTracklessPt = []
genTrackedPt = []
recoTrackedPt = []
recoTrackedEta = []
recoUntrackedPt = []
recoUntrackedEta = []
recoDileptonMass = []

#pT, sigmaIEIE, ecal iso/pT, had/em / energy, hcal iso/pT for bkgnd evts which fire the very loose trigger
bkgndTuple = []
numBkgndEvtsFired = 0
#bkgndPt = []
#bkgndSigmaIEIE = []
#bkgndEcalIso = []
#bkgndHoverE = []
#bkgndHcalIso = []

for w in xrange(t3.GetEntries()):
	t3.GetEntry(w)
	if(t3.matched_pT_ > 0.):
		#print 'found a minBias evt which fired loose double electron trigger'
		bkgndTuple.append([t3.matched_pT_, t3.matched_ecalClusterShape_SigmaIEtaIEta_, t3.matched_ecalIso_/t3.matched_pT_, t3.matched_hOverE_/(t3.matched_pT_*(math.cosh(t3.matched_eta_)) ), t3.matched_hcalIso_/t3.matched_pT_])
		numBkgndEvtsFired += 1
		#bkgndPt.append(t3.matched_pT_)
		#bkgndSigmaIEIE.append(t3.matched_ecalClusterShape_SigmaIEtaIEta_)
		#bkgndEcalIso.append(t3.matched_ecalIso_/t3.matched_pT_)
		#bkgndHoverE.append(t3.matched_hOverE_/(t3.matched_pT_*(math.cosh(t3.matched_eta_)) ))
		#bkgndHcalIso.append(t3.matched_hcalIso_/t3.matched_pT_)

#pT, sigmaIEIE, ecal iso/pT, had/em / energy, hcal iso/pT for sig evts not matched to gen electrons which fire the very loose trigger
unmatchedSigTuple = []
numUnmatchedSigEvtsFired = 0

for q in xrange(t2.GetEntries()):
	t2.GetEntry(q)
	if(t2.matched_pT_ > 0.):
		#print 'found a minBias evt which fired loose double electron trigger'
		unmatchedSigTuple.append([t2.matched_pT_, t2.matched_ecalClusterShape_SigmaIEtaIEta_, t2.matched_ecalIso_/t2.matched_pT_, t2.matched_hOverE_/(t2.matched_pT_*(math.cosh(t2.matched_eta_)) ), t2.matched_hcalIso_/t2.matched_pT_])
		numUnmatchedSigEvtsFired += 1

#print 'the number of signal evts which fired the trigger = ', numUnmatchedSigEvtsFired
#print 'the total number of signal evts which were passed through the trigger = ', t2.GetEntries()


#single number vars
efficiencyDenom = 0	#denominator of efficiency, equal to # of events with one untracked EE gen e- (pT > 15), one tracked gen e- (pT > 27), and the dilepton mass of these two gen electrons is between 81 and 101 GeV 

analyzeThisManyEvents = t1.GetEntries() #the number of TTree entries to inspect
#eventually swap 2000 for t1.GetEntries()
for z in xrange(analyzeThisManyEvents):
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
			genTrackedPt.append(t1.gen_tracked_pT_)
			genTracklessPt.append(t1.gen_trackless_pT_)
			#print 'found an event where the di-electron mass is between 81 and 101'
			if(t1.matched_pT_ > 0.):
				sigTuple.append([t1.matched_ecalClusterShape_SigmaIEtaIEta_, t1.matched_ecalIso_/t1.matched_pT_, t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ), t1.matched_ecalIso_/t1.matched_pT_])
				sigEcalIso.append(t1.matched_ecalIso_/t1.matched_pT_)
				sigHcalIso.append(t1.matched_hcalIso_/t1.matched_pT_)
				sigHoverE.append(t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ))
				sigSigmaIEIE.append(t1.matched_ecalClusterShape_SigmaIEtaIEta_)
				sigPt.append(t1.matched_pT_)
				sigEta.append(t1.matched_eta_)
				#calculate dilepton mass of the RECO gsf electron and EE supercluster which are matched to the two trigger objects
				if(t1.reco_tracked_pT_ > 0. and t1.reco_untracked_pT_ > 0.):
					recoDileptonSquared = 0.
					recoDileptonSquared += (2)*(t1.reco_tracked_pT_)*(t1.reco_untracked_pT_)*(math.cosh(t1.reco_tracked_eta_ - t1.reco_untracked_eta_) - math.cos(t1.reco_tracked_phi_ - t1.reco_untracked_phi_) )
					if( recoDileptonSquared > 0.):
						recoDileptonMass.append( math.sqrt(recoDileptonSquared) )
						recoTrackedPt.append(t1.reco_tracked_pT_)
						recoTrackedEta.append(t1.reco_tracked_eta_)
						recoUntrackedPt.append(t1.reco_untracked_pT_)
						recoUntrackedEta.append(t1.reco_untracked_eta_)

#sigTupleLen defined here is equal to the # of events which passed the trackless leg of the trigger
sigTupleLen = float(len(sigTuple))
sigPtLen = int(len(sigPt))
#print 'sigPtLen equals ', sigPtLen
recoDileptonLen = int(len(recoDileptonMass))
maxEff = float(len(sigPt))*(100)/efficiencyDenom

#make sorted arrays of sigPt, sigSigmaIEIE, sigEcalIso, sigHoverE, and sigHcalIso
#all arrays except sigPt will be sorted from high to low (last element is smallest value)
sortedPt = sorted(sigPt)
sortedSigmaIEIE = sorted(sigSigmaIEIE, reverse=True)
sortedEcalIso = sorted(sigEcalIso, reverse=True)
sortedHoverE = sorted(sigHoverE, reverse=True)
sortedHcalIso = sorted(sigHcalIso, reverse=True)

#returned array contains these elements in this exact order:
#pT, sigmaIEIE, ecal iso/pT, (had/em)/energy, hcal iso/pT, total rate, Z->ee efficiency, bkgnd rate, bkgnd evts passing trig, signal rate, signal evts passing trig
#the last six elements should be used to plot Z->ee efficiency as a function of total rate + uncertainty

optimalCuts = []	#a 5D array which stores the values of the 5 cut variables used in the trackless leg of the trigger
zEff = []
zEffErr = []
totalTrigRate = []
totalTrigRateErr = []

highRate = 1700.
incrementRate = 100.
numDiffRates = 13 
for q in xrange(numDiffRates):
	targetRate = (highRate - q*incrementRate)
	optimizedCutsRateAndEff = findOptimalCutValuesAndRateAndEff(f1, f2, f3, targetRate, efficiencyDenom, sortedPt, sortedSigmaIEIE, sortedEcalIso, sortedHoverE, sortedHcalIso, t3.GetEntries(), numBkgndEvtsFired, bkgndTuple, t2.GetEntries(), numUnmatchedSigEvtsFired, unmatchedSigTuple)
	print 'q = ', q
	optimalCuts.append([optimizedCutsRateAndEff[0], optimizedCutsRateAndEff[1], optimizedCutsRateAndEff[2], optimizedCutsRateAndEff[3], optimizedCutsRateAndEff[4] ])
	totalTrigRate.append(optimizedCutsRateAndEff[5])
	bkgndRateErr = optimizedCutsRateAndEff[7]/math.sqrt(optimizedCutsRateAndEff[8])
	signalRateErr = optimizedCutsRateAndEff[9]/math.sqrt(optimizedCutsRateAndEff[10])
	totalTrigRateErr.append(math.sqrt( math.pow(bkgndRateErr,2) + math.pow(signalRateErr,2) ) )
	zEff.append(optimizedCutsRateAndEff[6])
	zEffErr.append(0.0)

for r in xrange(numDiffRates):
	print ' '
	print 'Z->ee trig eff = ', zEff[r]
	print 'total trig rate = ', totalTrigRate[r]
	print 'total trig rate err = ', totalTrigRateErr[r]
	print 'min ET = ', optimalCuts[r][0]
	print 'max sigmaIEIE = ', optimalCuts[r][1]
	print 'max ecal iso/ET = ', optimalCuts[r][2]
	print 'max had/em / Energy = ', optimalCuts[r][3]
	print 'max hcal iso/ET = ', optimalCuts[r][4]
	print ' '

effVsRateGraph(zEff, zEffErr, totalTrigRate, totalTrigRateErr, "Z->ee trigger efficiency vs total trigger rate","../triggerPlots/efficiencies/optimizedZtoEE_eff_vs_trigRate_allEvts.png" )

#print 'after analyzing 10000 events, efficiency denom equals ', efficiencyDenom
#print 'out of 10000 possible events, the trigger fired in this many events ', sigPtLen
#print 'max trigger efficiency equals: ', maxEff

#sigEff_EcalIso = []
#sigEff_HcalIso = []
#sigEff_HoverE = []
#sigEff_SigmaIEIE = []
#sigEff_Pt = []
#sigEff_Eta = []
#
##for loop to fill sigEff_* arrays 
##sigPt, sigEcalIso, sigEff_* should all have the same length
#for q in xrange(sigPtLen):
#	sigEff_EcalIso.append( calcEff(True, sigEcalIso, sigEcalIso[q], efficiencyDenom ) )
#	sigEff_HcalIso.append( calcEff(True, sigHcalIso, sigHcalIso[q], efficiencyDenom ) )
#	sigEff_HoverE.append( calcEff(True, sigHoverE, sigHoverE[q], efficiencyDenom ) )
#	sigEff_SigmaIEIE.append( calcEff(True, sigSigmaIEIE, sigSigmaIEIE[q], efficiencyDenom ) )
#	sigEff_Pt.append( calcEff(False, sigPt, sigPt[q], efficiencyDenom ) )
#	sigEff_Eta.append( calcEff(False, sigEta, sigEta[q], efficiencyDenom ) )
#
##testPt = sorted(sigPt)
##testEff = sorted(sigEff_Pt, reverse = False)
##for q in xrange(sigPtLen):
##	for w in xrange(sigPtLen):
##		if(testPt[w] == sigPt[q]):
##			print 'sigPt element # ', q, ' equals ', sigPt[q]
##			print 'sigEff_Pt element # ', q, ' equals ', sigEff_Pt[q]
##			print 'testEff element # ', w, ' equals ', testEff[w]
##			print ' '


#efficiencyGraph(sigEcalIso,sigEff_EcalIso,"canvEcalIso","Z->ee trig efficiency vs HLT EcalIso/HLT PT",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_EcalIsoGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigHcalIso,sigEff_HcalIso,"canvHcalIso","Z->ee trig efficiency vs HcalIso/HLT PT",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_HcalIsoGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigHoverE,sigEff_HoverE,"canvHoverE","Z->ee trig efficiency vs HoverE/HLT E",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_HoverEGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigSigmaIEIE,sigEff_SigmaIEIE,"canvSigmaIEIE","Efficiency vs HLT #sigma_{i#etai#eta}",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_SigmaIEIEGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigPt,sigEff_Pt,"canvPt","Z->ee trig efficiency vs HLT PT",True, True,"../triggerPlots/efficiencies/ZtoEE_trigEff_PtGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigEta,sigEff_Eta,"canvEta","Efficiency vs HLT Eta",True, True,"../triggerPlots/efficiencies/ZtoEE_trigEff_EtaGraph_low_thresholds_allEvts.png")

#makeAndSaveHisto(sigEcalIso, "EcalIsoHistoCanv","EcalIso/HLT PT of HLT object matched to gen trackless electron",100,-0.3,0.5, "../triggerPlots/hltObjectPlots/signal_EcalIsoHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigSigmaIEIE, "SigmaIEIEHistoCanv","#sigma_{i#etai#eta} of HLT object matched to gen trackless electron",100,0.,0.2, "../triggerPlots/hltObjectPlots/signal_SigmaIEIEHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigHcalIso, "HcalIsoHistoCanv","HcalIso/HLT PT of HLT object matched to gen trackless electron",100,-0.3,0.5, "../triggerPlots/hltObjectPlots/signal_HcalIsoHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigHoverE, "HoverEHistoCanv","HoverE/HLT E of HLT object matched to gen trackless electron",100,0.,1, "../triggerPlots/hltObjectPlots/signal_HoverEHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigPt, "PtHistoCanv","P_{T} of HLT object matched to gen trackless electron",100,0.,250., "../triggerPlots/hltObjectPlots/signal_HLT_matched_PtHisto_low_thresholds_allEvts.png")


#makeAndSaveHisto(genTracklessPt, "genTracklessPtHistoCanv","P_{T} of trackless gen electron from Z->ee decay",100,0.,150., "../triggerPlots/genParticlePlots/signal_gen_trackless_PtHisto_low_thresholds_allEvts.png")
#
#makeAndSaveHisto(genTrackedPt, "genTrackedPtHistoCanv","P_{T} of tracked gen electron from Z->ee decay",100,0.,150., "../triggerPlots/genParticlePlots/signal_gen_tracked_PtHisto_low_thresholds_allEvts.png")
#
#
#makeAndSaveHisto(recoDileptonMass, "recoMLLCanv","M_{ee} of reco Gsf Electron and trackless EE supercluster matched to two HLT objects which fired trigger",100, 40., 150., "../triggerPlots/recoPlots/recoDileptonMass_allEvts.png")
#
#makeAndSaveHisto(recoTrackedPt, "recoTrackedPtCanv","P_{T} of reco Gsf Electron matched to an HLT object which fired trigger",100, 0., 150., "../triggerPlots/recoPlots/recoTrackedPt_allEvts.png")
#
#makeAndSaveHisto(recoTrackedEta, "recoTrackedEtaCanv","#eta of reco Gsf Electron matched to an HLT object which fired trigger",100, -3.5, 3.5, "../triggerPlots/recoPlots/recoTrackedEta_allEvts.png")
#
#makeAndSaveHisto(recoUntrackedPt, "recoUntrackedPtCanv","P_{T} of reco supercluster in trackless EE matched to an HLT object which fired trigger",100, 0., 150., "../triggerPlots/recoPlots/recoUntrackedPt_allEvts.png")
#
#makeAndSaveHisto(recoUntrackedEta, "recoUntrackedEtaCanv","#eta of reco supercluster in trackless EE matched to an HLT object which fired trigger",100, -3.5, 3.5, "../triggerPlots/recoPlots/recoUntrackedEta_allEvts.png")


#makeAndSaveHisto(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath)
#makeAndSaveGraph(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath)




