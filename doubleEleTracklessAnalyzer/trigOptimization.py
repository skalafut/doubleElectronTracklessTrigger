import ROOT
import array
import math

def findOptimalCutValuesAndRateAndEff(matchedSigFile, unmatchedSigFile, bkgndFile, desiredRate, effDenom, sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr):
	#this function takes three file objects, the desired total trigger rate, and Z->ee trigger efficiency denominator, and five 1D vectors as inputs
	#the five 1D arrays contain cut values for ET, sigma ietaieta, ecal iso/ET, (had/em)/energy, and hcal iso/ET
	#the ET array is sorted from low to high (last element in array is largest value)
	#the other four arrays are sorted from high to low (last element in array is smallest value)
	#this function calculates the total trigger rate and Z->ee trigger efficiency as a function of the cut variable values
	#and returns a 1D vector with the value of the five cut variables which maximizes the Z->ee trig efficiency, the total trigger rate, and the Z->ee trigger efficiency
	matchedSigTree = matchedSigFile.Get("demo/doubleEleTrigger")
	unmatchedSigTree = unmatchedSigFile.Get("demo/doubleEleTrigger")
	bkgndTree = bkgndFile.Get("demo/doubleEleTrigger")
	print 'declared the three TTree objects in findOptimalCutValuesAndRateAndEff'

	#expected peak luminosity in 2015, in units of 1/(sec * cm^2)
	value = 1.4
	power = 10**34 
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

	#make a 7D array which will be returned at the end
	#(ET, sigmaIEIE, ecalIso/ET, had/em/Energy, hcalIso/ET, calculated total trigger rate, Z->ee trig eff)
	cutsRatesAndEffs = []
	print 'length of sortedEtCutArr is ', len(sortedEtCutArr)
	
	#loop over all values of the five cut variables
	#sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr
	for a in xrange( int(len(sortedEtCutArr)) ):
		for b in xrange( int(len(sortedSigmaIEIECutArr)) ):
			for c in xrange( int(len(sortedEcalIsoCutArr)) ):
				for d in xrange( int(len(sortedHoverECutArr)) ):
					for f in xrange( int(len(sortedHcalIsoCutArr)) ):
						#three variables to count the number of bkgnd evts, unmatched sig evts, and matched sig evts pass all five filters
						numUnmatchedSigEvts = 0.
						numMatchedSigEvts = 0.
						numBkgndEvts = 0.
						print 'declared the three counter variables which will be used to calculate signal rate, bkgnd rate, and Z->ee trig eff'

						#loop over all signal evts which are matched to gen electrons coming from a Z decay
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
									if(matchedSigTree.matched_pT_ > sortedEtCutArr[a]):
										if(matchedSigTree.matched_ecalClusterShape_SigmaIEtaIEta_ < sortedSigmaIEIECutArr[b]):
											if( (matchedSigTree.matched_ecalIso_/matchedSigTree.matched_pT_) < sortedEcalIsoCutArr[c]):
												if( (matchedSigTree.matched_hOverE_/(matchedSigTree.matched_pT_*(math.cosh(matchedSigTree.matched_eta_)) )) < sortedHoverECutArr[d]):
													if( (matchedSigTree.matched_hcalIso_/matchedSigTree.matched_pT_) < sortedHcalIsoCutArr[f]):
														numMatchedSigEvts += 1.0

						#end loop over matchedSigTree entries to determine # of events with gen M_ee near Z peak which fired trigger
						#begin loop over unmatchedSigTree entries
						for j in xrange(unmatchedSigTree.GetEntries()):
							unmatchedSigTree.GetEntry(j)
							if(unmatchedSigTree.matched_pT_ > sortedEtCutArr[a]):
								if(unmatchedSigTree.matched_ecalClusterShape_SigmaIEtaIEta_ < sortedSigmaIEIECutArr[b]):
									if( (unmatchedSigTree.matched_ecalIso_/unmatchedSigTree.matched_pT_) < sortedEcalIsoCutArr[c]):
										if( (unmatchedSigTree.matched_hOverE_/(unmatchedSigTree.matched_pT_*(math.cosh(unmatchedSigTree.matched_eta_)) )) < sortedHoverECutArr[d]):
											if( (unmatchedSigTree.matched_hcalIso_/unmatchedSigTree.matched_pT_) < sortedHcalIsoCutArr[f]):
												numUnmatchedSigEvts += 1.0

						#end loop over unmatchedSigTree entries to determine # of signal events which fired trigger
						#begin loop over bkgndTree entries
						for k in xrange(bkgndTree.GetEntries()):
							bkgndTree.GetEntry(k)
							if(bkgndTree.matched_pT_ > sortedEtCutArr[a]):
								if(bkgndTree.matched_ecalClusterShape_SigmaIEtaIEta_ < sortedSigmaIEIECutArr[b]):
									if( (bkgndTree.matched_ecalIso_/bkgndTree.matched_pT_) < sortedEcalIsoCutArr[c]):
										if( (bkgndTree.matched_hOverE_/(bkgndTree.matched_pT_*(math.cosh(bkgndTree.matched_eta_)) )) < sortedHoverECutArr[d]):
											if( (bkgndTree.matched_hcalIso_/bkgndTree.matched_pT_) < sortedHcalIsoCutArr[f]):
												numBkgndEvts += 1.0

						#end loop over bkgndTree entries to determine # of bkgnd events which fired trigger
						
						#now calculate total trigger rate.  If the calculated rate is btwn 0.9 and 1.0 times the desired rate, then calculate the Z->ee efficiency, and save
						#the values of the five cut variables, the total rate, and the Z->ee trigger efficiency
						bkgndRate = (minBiasXSxn*peakLumi*numBkgndEvts)/bkgndTree.GetEntries()
						signalRate = (signalXSxn*peakLumi*numUnmatchedSigEvts)/unmatchedSigTree.GetEntries()
						totalRate = signalRate + bkgndRate
						print 'calculated total trigger rate'
						if(totalRate > (1.5)*desiredRate and f < (int(len(sortedHcalIsoCutArr))-2) ):
							f += 2
							print 'incremented f by 2 because calculated totalRate is too large'
							continue;
						if(totalRate >= (0.9)*desiredRate and totalRate <= desiredRate):
							zEff = (numMatchedSigEvts/effDenom)
							cutsRatesAndEffs.append([sortedEtCutArr[a], sortedSigmaIEIECutArr[b], sortedEcalIsoCutArr[c], sortedHoverECutArr[d], sortedHcalIsoCutArr[f], totalRate, zEff])

	#now that the 7D array named cutsRatesAndEffs is filled, I should find the values of the five cut variables which maximize the Z->ee trigger efficiency
	maxEff = 0.
	indexOfMaxEff = 0
	for i in xrange(int(len(cutsRatesAndEffs)) ):
		if(cutsRatesAndEffs[6][i] > maxEff):
			maxEff = 0.
			maxEff += cutsRatesAndEffs[6][i]
			indexOfMaxEff = 0
			indexOfMaxEff += i
	
	#end loop over cutsRatesAndEffs[6]
	#fill a 1D array with the five optimal cut values, the trigger rate, and the Z->ee trigger efficiency
	optimalValues = []
	for g in xrange(7):
		optimalValues.append(cutsRatesAndEffs[g][indexOfMaxEff])
	
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
f2 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/unmatched_signal_10kevts_very_loose_trackless_leg.root")
f3 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/bkgnd_10kevts_very_loose_trackless_leg.root")

#tree for signal evts which fire the trigger and are matched to gen electrons from Z decay
t1 = f1.Get("demo/doubleEleTrigger")

#tree for signal evts which fire the trigger but are not matched to gen electrons
#t2 = f2.Get("demo/doubleEleTrigger")

#tree for bkgnd evts which fire the trigger
#t3 = f3.Get("demo/doubleEleTrigger")


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
for z in xrange(1000):
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
			print 'found an event where the di-electron mass is between 81 and 101'
			if(t1.matched_pT_ > 0.):
				sigTuple.append([t1.matched_ecalClusterShape_SigmaIEtaIEta_, t1.matched_ecalIso_/t1.matched_pT_, t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ), t1.matched_ecalIso_/t1.matched_pT_])
				sigEcalIso.append(t1.matched_ecalIso_/t1.matched_pT_)
				sigHcalIso.append(t1.matched_hcalIso_/t1.matched_pT_)
				sigHoverE.append(t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ))
				sigSigmaIEIE.append(t1.matched_ecalClusterShape_SigmaIEtaIEta_)
				sigPt.append(t1.matched_pT_)
				sigEta.append(t1.matched_eta_)
				genTracklessPt.append(t1.gen_trackless_pT_)
				#calculate dilepton mass of the RECO gsf electron and EE supercluster which are matched to the two trigger objects
				if(t1.reco_tracked_pT_ > 0. and t1.reco_untracked_pT_ > 0.):
					recoDileptonSquared = 0.
					recoDileptonSquared += (2)*(t1.reco_tracked_pT_)*(t1.reco_untracked_pT_)*(math.cosh(t1.reco_tracked_eta_ - t1.reco_untracked_eta_) - math.cos(t1.reco_tracked_phi_ - t1.reco_untracked_phi_) )
					if( recoDileptonSquared > 0.):
						recoDileptonMass.append( math.sqrt(recoDileptonSquared) )

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

#print ' '
#
#for i in xrange(sigPtLen):
#	print 'sortedPt element # ', i, ' equals ', sortedPt[i]
#
#print ' '
#
#for i in xrange(sigPtLen):
#	print 'sortedSigmaIEIE element # ', i, ' equals ', sortedSigmaIEIE[i]
#
#print ' '
#
#for i in xrange(sigPtLen):
#	print 'sortedEcalIso element # ', i, ' equals ', sortedEcalIso[i]
#
#print ' '
#
#for i in xrange(sigPtLen):
#	print 'sortedHoverE element # ', i, ' equals ', sortedHoverE[i]
#
#print ' '
#
#for i in xrange(sigPtLen):
#	print 'sortedHcalIso element # ', i, ' equals ', sortedHcalIso[i]
#


targetRate = 0.4 
optimizedCutsRateAndEff = findOptimalCutValuesAndRateAndEff(f1, f2, f3, targetRate, efficiencyDenom, sortedPt, sortedSigmaIEIE, sortedEcalIso, sortedHoverE, sortedHcalIso)
for i in xrange(optimizedCutsRateAndEff):
	if(i < 5):
		print 'cut variable number ', i, ' equals ', optimizedCutsRateAndEff[i]
	if(i == 5):
		print ' '
		print 'desired trigger rate equals', targetRate
		print 'calculated trigger rate equals ', optimizedCutsRateAndEff[i]
	if(i == 6):
		print ' '
		print 'Z->ee trigger efficiency equals ', optimizedCutsRateAndEff[i]


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




