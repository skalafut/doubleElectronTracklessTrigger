import ROOT
import array
import math

def findOptimalCutValuesAndRateAndEff(desiredRate, effDenom, sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr, totalBkgndEvts, numBkgndEvtsPassingTrigger, tupleForBkgndEvtsPassingTrig, totalUnmatchedSigEvts, numUnmatchedSigEvtsPassingTrig, tupleForUnmatchedSigEvts, maxMatchedSigEvts, tupleForMatchedSigEvts):
	#this function takes three file objects, the desired total trigger rate, and Z->ee trigger efficiency denominator, and five 1D vectors as inputs
	#to speed up processing, this function also takes a 5D array capturing the characteristics of all bkgnd evts which fire the trigger, the number of entries in
	#this 5D array, and the total number of bkgnd events which were analyzed and resulted in a small # of evts firing the trigger
	#the five 1D arrays contain cut values for ET, sigma ietaieta, ecal iso/ET, (had/em)/energy, and hcal iso/ET
	#the ET array is sorted from low to high (last element in array is largest value)
	#the other four arrays are sorted from high to low (last element in array is smallest value)
	#numEventsToAnalyze equals the number of events to run over in each tree - 1000, 2000, etc
	#this function calculates the total trigger rate and Z->ee trigger efficiency as a function of the cut variable values
	#and returns a 1D vector with the value of the five cut variables which maximizes the Z->ee trig efficiency, the total trigger rate, and the Z->ee trigger efficiency

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
	minHltPT = 20.
	totalRate = -0.01
	leftHcalIso = False
	leaveEcalIso = False
	leaveSigmaIEIE = False 
	increaseHcalIsoIterator = False
	magnifyHcalIsoIterator = False

	#make a 2D array which contains the # of bkgnd evts passing the trigger, and the corresponding bkgnd trigger rate
	#the first entry in this array will be larger than the second entry in this array
	bkgndEvtsPassingAndRate = []
	for s in xrange(numBkgndEvtsPassingTrigger):
		#print 'num bkgnd evts passing = ', (numBkgndEvtsPassingTrigger-s)
		rate = (minBiasXSxn*peakLumi*(numBkgndEvtsPassingTrigger-s))/totalBkgndEvts
		#print 'rate = ', rate
		bkgndEvtsPassingAndRate.append([(numBkgndEvtsPassingTrigger-s),rate])
	
	bkgndEvtsPassingAndRate.append([0,0.0])
	#now loop over bkgndEvtsPassingAndRate and identify the largest # of bkgnd evts which yields a bkgnd trigger rate <= 2.0 times the desired total rate
	limitBkgndEvts = 0.
	for q in xrange(int(len(bkgndEvtsPassingAndRate) ) ):
		if( bkgndEvtsPassingAndRate[q][1] <= (2)*desiredRate ):
			limitBkgndEvts += bkgndEvtsPassingAndRate[q][0]
			break

	#totalUnmatchedSigEvts, numUnmatchedSigEvtsPassingTrig, tupleForUnmatchedSigEvts
	#repeat the same process done above for DY->ee evts which fire the loose trigger
	#only when limitBkgndEvts = 0
	#dyEvtsPassingAndRate[row=0][0] = 0, increases as row increases
	dyEvtsPassingAndRate = []
	for v in xrange(numUnmatchedSigEvtsPassingTrig):
		if(limitBkgndEvts > 0.5):
			break
		sRate = (signalXSxn*peakLumi*v)/totalUnmatchedSigEvts
		dyEvtsPassingAndRate.append([v,sRate])

	#now loop over dyEvtsPassingAndRate and identify the fewest # of DY->ee evts which yields a signal trigger rate >= 0.5 times the desired total rate
	limitSigEvts = 0.
	for h in xrange(numUnmatchedSigEvtsPassingTrig):
		if(limitBkgndEvts > 0.5):
			break
		if(dyEvtsPassingAndRate[h][1] >= (0.5)*desiredRate):
			limitSigEvts += dyEvtsPassingAndRate[h][0]
			break

	#now quickly loop over the sorted lists of sigmaIEIE, EcalIso, HoverE, and HcalIso to find starting values of these four vars which only allow
	#limitBkgndEvts to pass the cuts.  Save these starting values and use them in the higher accuracy but slower nested for loop system

	#there will be several sets of initial values which will work
	#save each set into a 4D list, and add a 5th nested for loop on top of the other four to the slow but accurate for loop system
	#to iterate over this 4D list
	allSetsOfInitialVals = []
	foundASet = False
	numEntriesInAllSets = 0

	for r in xrange(5):
		if(limitBkgndEvts < 0.5):
			#use a different system of coarse step, nested for loops to determine initial threshold values
			#if the target number of bkgnd evts is zero
			print 'skipped correct system of coarse step, nested for loops'
			break
		for t in xrange(5):
			for w in xrange(5):
				for g in xrange(5):
					numBkgEvts = 0.  #reset numBkgEvts to zero before looping over all bkgnd evts which pass the trigger!
					#begin for loop over bkgnd evts which passed loose trigger
					for k in xrange(numBkgndEvtsPassingTrigger):
						if(tupleForBkgndEvtsPassingTrig[k][0] > minHltPT):
							if(tupleForBkgndEvtsPassingTrig[k][1] < sortedSigmaIEIECutArr[(80*r)]):
								if(tupleForBkgndEvtsPassingTrig[k][2] < sortedEcalIsoCutArr[(80*t)]):
									if(tupleForBkgndEvtsPassingTrig[k][3] < sortedHoverECutArr[(80*w)]):
										if(tupleForBkgndEvtsPassingTrig[k][4] < sortedHcalIsoCutArr[(80*g)]):
											numBkgEvts += 1.0
					#end for loop over bkgnd evts which passed loose trigger
		
					if((limitBkgndEvts - numBkgEvts) >= 0 and (limitBkgndEvts - numBkgEvts) <= 1 and k == (numBkgndEvtsPassingTrigger-1) and sortedSigmaIEIECutArr[(80*r)] > 0. and sortedEcalIsoCutArr[(80*t)] > 0. and sortedHoverECutArr[(80*w)] > 0. and sortedHcalIsoCutArr[(80*g)] > 0.):
						#print 'found trigger cut values which yield a reasonable bkgnd rate'
						#print 'limitBkgndEvts = ', limitBkgndEvts
						#print 'numBkgEvts = ', numBkgEvts
						#print ' '
						#print 'hcalIso iterator g = ', g
						#print 'hOverE iterator w = ', w
						#print 'ecalIso iterator t = ', t
						#print 'sigmaIEIE iterator r = ', r
						#print ' '
						#print 'very loose sigmaIEIE = ', sortedSigmaIEIECutArr[0]
						#print 'new initial sigmaIEIE = ', sortedSigmaIEIECutArr[(80*r)]
						#print ' '
						#print 'very loose ecalIso = ', sortedEcalIsoCutArr[0]
						#print 'new initial ecalIso = ', sortedEcalIsoCutArr[(80*t)]
						#print ' '
						#print 'very loose hOverE = ', sortedHoverECutArr[0]
						#print 'new initial hOverE = ', sortedHoverECutArr[(80*w)]
						#print ' '
						#print 'very loose hcalIso = ', sortedHcalIsoCutArr[0]
						#print 'new initial hcalIso = ', sortedHcalIsoCutArr[(80*g)]

						if(foundASet == False):
							#foundASet will be false for as long as there is no entry into allSetsOfInitialVals
							allSetsOfInitialVals.append([minHltPT, sortedSigmaIEIECutArr[(80*r)], sortedEcalIsoCutArr[(80*t)], sortedHoverECutArr[(80*w)], sortedHcalIsoCutArr[(80*g)] ] )
							numEntriesInAllSets += 1
							#print 'increased numEntriesInAllSets by one'
						#end if(!foundASet)

						if(foundASet == True):
							#on the second or later addition to allSetsOfInitialVals I should check that the set of cut values being added to the list
							#has at least one value which is greater than the last set of values enterred into the list
							if(sortedSigmaIEIECutArr[(80*r)] > allSetsOfInitialVals[numEntriesInAllSets-1][0] or sortedEcalIsoCutArr[(80*t)] > allSetsOfInitialVals[numEntriesInAllSets-1][1] or sortedHoverECutArr[(80*w)] > allSetsOfInitialVals[numEntriesInAllSets-1][2] or sortedHcalIsoCutArr[(80*g)] > allSetsOfInitialVals[numEntriesInAllSets-1][3]):
								allSetsOfInitialVals.append( [minHltPT, sortedSigmaIEIECutArr[(80*r)], sortedEcalIsoCutArr[(80*t)], sortedHoverECutArr[(80*w)], sortedHcalIsoCutArr[(80*g)] ] )
								numEntriesInAllSets += 1
								#print 'increased numEntriesInAllSets by one'
					
						foundASet = True 
				#end loop over g (hcalIso)
			#end loop over w (hOverE)
		#end loop over t (ecalIso)
	#end loop over r (sigmaIEIE)

	maxRange = 14 
	multiplier = 21 
	for r in xrange(maxRange):
		if(limitBkgndEvts > 0.5):
			#dont use this system of coarse step, nested for loops to determine initial threshold values
			#if the target number of bkgnd evts is one or greater 
			break
		if(r==0):
			print 'in correct system of nested for loops'
		if(multiplier*r > (int(len(sortedSigmaIEIECutArr))-1) ):
			break
		for t in xrange(maxRange):
			if(multiplier*t > (int(len(sortedEcalIsoCutArr))-1) ):
				break
			for w in xrange(maxRange):
				if(multiplier*w > (int(len(sortedHoverECutArr))-1) ):
					break
				for g in xrange(maxRange):
					if(multiplier*g > (int(len(sortedHcalIsoCutArr))-1) ):
						break
					numBkgEvts = 0.  #reset numBkgEvts to zero before looping over all bkgnd evts which pass the trigger!
					numGoodEvts = 0.
					numGoldenEvts = 0.
					#begin for loop over bkgnd evts which passed loose trigger
					for k in xrange(numBkgndEvtsPassingTrigger):
						if(tupleForBkgndEvtsPassingTrig[k][0] > minHltPT):
							if(tupleForBkgndEvtsPassingTrig[k][1] < sortedSigmaIEIECutArr[(multiplier*r)]):
								if(tupleForBkgndEvtsPassingTrig[k][2] < sortedEcalIsoCutArr[(multiplier*t)]):
									if(tupleForBkgndEvtsPassingTrig[k][3] < sortedHoverECutArr[(multiplier*w)]):
										if(tupleForBkgndEvtsPassingTrig[k][4] < sortedHcalIsoCutArr[(multiplier*g)]):
											numBkgEvts += 1.0
					#end for loop over bkgnd evts which passed loose trigger
		
					#begin loop over DY->ee evts which passed loose trigger
					for s in xrange(numUnmatchedSigEvtsPassingTrig):
						if(tupleForUnmatchedSigEvts[s][0] > minHltPT):
							if(tupleForUnmatchedSigEvts[s][1] < sortedSigmaIEIECutArr[(multiplier*r)]):
								if(tupleForUnmatchedSigEvts[s][2] < sortedEcalIsoCutArr[(multiplier*t)]):
									if(tupleForUnmatchedSigEvts[s][3] < sortedHoverECutArr[(multiplier*w)]):
										if(tupleForUnmatchedSigEvts[s][4] < sortedHcalIsoCutArr[(multiplier*g)]):
											numGoodEvts += 1.0
					#end for loop over DY->ee evts which passed loose trigger
					
					#begin for loop over Z->ee candidate evts
					for i in xrange(maxMatchedSigEvts):
						if(tupleForMatchedSigEvts[i][0] > minHltPT):
							if(tupleForMatchedSigEvts[i][1] < sortedSigmaIEIECutArr[multiplier*r]):
								if(tupleForMatchedSigEvts[i][2] < sortedEcalIsoCutArr[multiplier*t]):
									if(tupleForMatchedSigEvts[i][3] < sortedHoverECutArr[multiplier*w]):
										if(tupleForMatchedSigEvts[i][4] < sortedHcalIsoCutArr[multiplier*g]):
											numGoldenEvts += 1.0
	
					#require that a reasonable number of DY->ee evts pass the cuts 
					if(numBkgEvts < 1 and (numGoodEvts - limitSigEvts) >= 0 and s == (numUnmatchedSigEvtsPassingTrig-1) and sortedSigmaIEIECutArr[(multiplier*r)] > 0. and sortedEcalIsoCutArr[(multiplier*t)] > 0. and sortedHoverECutArr[(multiplier*w)] > 0. and sortedHcalIsoCutArr[(multiplier*g)] > 0.):

						#if numBkgEvts = 0, then the total rate = the signal rate
						totRate = (signalXSxn*peakLumi*numGoodEvts)/totalUnmatchedSigEvts
						zedEff = (numGoldenEvts/effDenom)
						
						if(foundASet == False):
							#foundASet will be false for as long as there is no entry into allSetsOfInitialVals
							allSetsOfInitialVals.append([minHltPT, sortedSigmaIEIECutArr[(multiplier*r)], sortedEcalIsoCutArr[(multiplier*t)], sortedHoverECutArr[(multiplier*w)], sortedHcalIsoCutArr[(multiplier*g)], totRate, zedEff, 0., numBkgEvts, totRate, numGoodEvts, multiplier*r, multiplier*t, multiplier*w, multiplier*g] )
							numEntriesInAllSets += 1
							print ' '
							print 'signal trigger rate = ', totRate 
							print 'very loose sigmaIEIE = ', sortedSigmaIEIECutArr[0]
							print 'new initial sigmaIEIE = ', sortedSigmaIEIECutArr[(multiplier*r)]
							print ' '
							print 'very loose ecalIso = ', sortedEcalIsoCutArr[0]
							print 'new initial ecalIso = ', sortedEcalIsoCutArr[(multiplier*t)]
							print ' '
							print 'very loose hOverE = ', sortedHoverECutArr[0]
							print 'new initial hOverE = ', sortedHoverECutArr[(multiplier*w)]
							print ' '
							print 'very loose hcalIso = ', sortedHcalIsoCutArr[0]
							print 'new initial hcalIso = ', sortedHcalIsoCutArr[(multiplier*g)]
							#print 'increased numEntriesInAllSets by one'
						#end if(!foundASet)

						if(foundASet == True):
							#on the second or later addition to allSetsOfInitialVals I should check that the set of cut values being added to the list
							#has at least one value which is greater than the last set of values enterred into the list
							if(sortedSigmaIEIECutArr[(multiplier*r)] > allSetsOfInitialVals[numEntriesInAllSets-1][1] or sortedEcalIsoCutArr[(multiplier*t)] > allSetsOfInitialVals[numEntriesInAllSets-1][2] or sortedHoverECutArr[(multiplier*w)] > allSetsOfInitialVals[numEntriesInAllSets-1][3] or sortedHcalIsoCutArr[(multiplier*g)] > allSetsOfInitialVals[numEntriesInAllSets-1][4]):

								allSetsOfInitialVals.append([minHltPT, sortedSigmaIEIECutArr[(multiplier*r)], sortedEcalIsoCutArr[(multiplier*t)], sortedHoverECutArr[(multiplier*w)], sortedHcalIsoCutArr[(multiplier*g)], totRate, zedEff, 0., numBkgEvts, totRate, numGoodEvts, multiplier*r, multiplier*t, multiplier*w, multiplier*g] )

								print ' '
								print 'signal trigger rate = ', totRate 
								print 'very loose sigmaIEIE = ', sortedSigmaIEIECutArr[0]
								print 'new initial sigmaIEIE = ', sortedSigmaIEIECutArr[(multiplier*r)]
								print ' '
								print 'very loose ecalIso = ', sortedEcalIsoCutArr[0]
								print 'new initial ecalIso = ', sortedEcalIsoCutArr[(multiplier*t)]
								print ' '
								print 'very loose hOverE = ', sortedHoverECutArr[0]
								print 'new initial hOverE = ', sortedHoverECutArr[(multiplier*w)]
								print ' '
								print 'very loose hcalIso = ', sortedHcalIsoCutArr[0]
								print 'new initial hcalIso = ', sortedHcalIsoCutArr[(multiplier*g)]
								
								numEntriesInAllSets += 1
								#print 'increased numEntriesInAllSets by one'
					
						foundASet = True 
				#end loop over g (hcalIso)
			#end loop over w (hOverE)
		#end loop over t (ecalIso)
	#end loop over r (sigmaIEIE)

	print 'numEntriesInAllSets = ', numEntriesInAllSets

	if(foundASet == False):
		#if no reasonable cut values have been found at this point, then set the start* values to the first values in each sorted list
		print 'no reasonable cut values found by using coarse step system of nested for loops shown above'
		allSetsOfInitialVals.append([sortedSigmaIEIECutArr[0], sortedEcalIsoCutArr[0], sortedHoverECutArr[0], sortedHcalIsoCutArr[0] ] )


	minRateFraction = 0.4
	maxRateFraction = 2.0
	stepSize = 12 
	#loop over all values of the five cut variables
	#sortedEtCutArr, sortedSigmaIEIECutArr, sortedEcalIsoCutArr, sortedHoverECutArr, sortedHcalIsoCutArr
	#for a in xrange( int(len(sortedEtCutArr)) ):
	for n in xrange(numEntriesInAllSets):
		#loop over all entries (about 30) in the list named allSetsOfInitialVals
		if(numEntriesInAllSets==1):
			print 'there is only one entry in allSetsOfInitialVals. Skip to the last system of nested for loops.'
			break
		print 'looking at set number ', n+1, 'out of a possible ', numEntriesInAllSets, ' sets'
		print 'found ', addedElementToCutsRatesEffs ,' interesting sets of cut threshold values'
		sigmaIEIEIt = 0
		for b in xrange( int(len(sortedSigmaIEIECutArr)) ):
			if(sigmaIEIEIt > ( int(len(sortedSigmaIEIECutArr))-1 ) ):
				break
			if(sortedSigmaIEIECutArr[sigmaIEIEIt] > allSetsOfInitialVals[n][1] or sortedSigmaIEIECutArr[sigmaIEIEIt] < 0.):
				sigmaIEIEIt += 4 
				continue
			ecalIsoIt = 0
			for c in xrange( int(len(sortedEcalIsoCutArr)) ):
				if(ecalIsoIt > ( int(len(sortedEcalIsoCutArr))-1 ) ):
					break
				if(sortedEcalIsoCutArr[ecalIsoIt] > allSetsOfInitialVals[n][2] or sortedEcalIsoCutArr[ecalIsoIt] < 0.):
					ecalIsoIt += stepSize 
					continue
				hOverEIt = 0
				for d in xrange( int(len(sortedHoverECutArr)) ):
					if(hOverEIt > ( int(len(sortedHoverECutArr))-1 ) ):
						break
					if(sortedHoverECutArr[hOverEIt] > allSetsOfInitialVals[n][3] or sortedHoverECutArr[hOverEIt] < 0.):
						hOverEIt += stepSize 
						continue
					hcalIsoIt = 0
					for f in xrange( int(len(sortedHcalIsoCutArr)) ):
						if(hcalIsoIt > ( int(len(sortedHcalIsoCutArr))-1 ) ):
							break
						if(sortedHcalIsoCutArr[hcalIsoIt] > allSetsOfInitialVals[n][4] or sortedHcalIsoCutArr[hcalIsoIt] < 0.):
							hcalIsoIt += stepSize 
							continue
						#three variables to count the number of bkgnd evts, unmatched sig evts, and matched sig evts pass all five filters
						numUnmatchedSigEvts = 0.
						numMatchedSigEvts = 0.
						numBkgndEvts = 0.
						if(magnifyHcalIsoIterator):
							magnifyHcalIsoIterator = False
							increaseHcalIsoIterator = False
							hcalIsoIt += 100
						if(increaseHcalIsoIterator):
							increaseHcalIsoIterator = False
							hcalIsoIt += 20 
		
						if(hcalIsoIt > (int(len(sortedHcalIsoCutArr))-1) ):
							break
		
						#loop over all Z->ee candidate evts (where GEN and RECO matching, and GEN kinematic requirements have been met)
						for i in xrange(maxMatchedSigEvts):
							if(tupleForMatchedSigEvts[i][0] > minHltPT):
								if(tupleForMatchedSigEvts[i][1] < sortedSigmaIEIECutArr[sigmaIEIEIt]):
									if(tupleForMatchedSigEvts[i][2] < sortedEcalIsoCutArr[ecalIsoIt]):
										if(tupleForMatchedSigEvts[i][3] < sortedHoverECutArr[hOverEIt]):
											if(tupleForMatchedSigEvts[i][4] < sortedHcalIsoCutArr[hcalIsoIt]):
												numMatchedSigEvts += 1.0
		
						#end loop over matchedSigTuple entries to determine # of events with gen M_ee near Z peak which fired trigger
						#begin loop over unmatchedSigTree entries
						for j in xrange(numUnmatchedSigEvtsPassingTrig):
							if(tupleForUnmatchedSigEvts[j][0] > minHltPT):
								if(tupleForUnmatchedSigEvts[j][1] < sortedSigmaIEIECutArr[sigmaIEIEIt]):
									if(tupleForUnmatchedSigEvts[j][2] < sortedEcalIsoCutArr[ecalIsoIt]):
										if(tupleForUnmatchedSigEvts[j][3] < sortedHoverECutArr[hOverEIt]):
											if(tupleForUnmatchedSigEvts[j][4] < sortedHcalIsoCutArr[hcalIsoIt]):
												numUnmatchedSigEvts += 1.0
		
						#end loop over unmatchedSigTree entries to determine # of signal events which fired trigger
						#begin loop over bkgndTree entries
						for k in xrange(numBkgndEvtsPassingTrigger):
							if(tupleForBkgndEvtsPassingTrig[k][0] > minHltPT):
								if(tupleForBkgndEvtsPassingTrig[k][1] < sortedSigmaIEIECutArr[sigmaIEIEIt]):
									if(tupleForBkgndEvtsPassingTrig[k][2] < sortedEcalIsoCutArr[ecalIsoIt]):
										if(tupleForBkgndEvtsPassingTrig[k][3] < sortedHoverECutArr[hOverEIt]):
											if(tupleForBkgndEvtsPassingTrig[k][4] < sortedHcalIsoCutArr[hcalIsoIt]):
												numBkgndEvts += 1.0
						
						#end loop over bkgndTree entries to determine # of bkgnd events which fired trigger
						#now calculate total trigger rate.  If the calculated rate is btwn 0.8 and 1.0 times the desired rate, then calculate the Z->ee efficiency, and save
						#the values of the five cut variables, the total rate, and the Z->ee trigger efficiency
						#if(numBkgndEvts < 10):
						#	break
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
						#print 'sigmaIEIE = ', sortedSigmaIEIECutArr[b]
						#print 'ecal iso/pT = ', sortedEcalIsoCutArr[c]
						#print '(had/em)/energy = ', sortedHoverECutArr[d]
						#print 'hcal iso/pT = ', sortedHcalIsoCutArr[hcalIsoIt]
						if(totalRate > (5.0)*desiredRate):
							#print 'total rate > 5 times desiredRate'
							increaseHcalIsoIterator = True
							if(totalRate > (20.0)*desiredRate):
								#print 'total rate > 20 times desiredRate'
								magnifyHcalIsoIterator = True
						if(totalRate < minRateFraction*desiredRate):
							#print 'total rate < 89% of desired rate'
							leftHcalIso = True
							break
						if(totalRate >= minRateFraction*desiredRate and totalRate <= maxRateFraction*desiredRate):
							zEff = (numMatchedSigEvts/effDenom)
							cutsRatesAndEffs.append([minHltPT, sortedSigmaIEIECutArr[sigmaIEIEIt], sortedEcalIsoCutArr[ecalIsoIt], sortedHoverECutArr[hOverEIt], sortedHcalIsoCutArr[hcalIsoIt], totalRate, zEff, bkgndRate, numBkgndEvts, signalRate, numUnmatchedSigEvts, sigmaIEIEIt, ecalIsoIt, hOverEIt, hcalIsoIt])
							addedElementToCutsRatesEffs += 1
							#print 'increased addedElementToCutsRatesEffs by one'
						hcalIsoIt += stepSize 
					
					#end loop over sortedHcalIsoCutArr values
					if(leftHcalIso and d==0):
						#print 'd equals zero and leftHcalIso is True'
						leaveEcalIso = True
						break
					hOverEIt += stepSize 
				#end loop over sortedHoverECutArr values
				if(leaveEcalIso == True):
					if(c==0):
						#break out of loop over sortedSigmaIEIECutArr if c==0 and leaveEcalIso==True
						leaveSigmaIEIE = True
					break
				ecalIsoIt += stepSize 
			#end loop over sortedEcalIsoCutArr values
			if(leaveSigmaIEIE == True):
				break
			sigmaIEIEIt += 4 
		#end loop over sortedSigmaIEIECutArr values
	#end loop over entries in the 4D list named allSetsOfInitialVals

	#now that the 11D array named cutsRatesAndEffs is filled, I should find the values of the five cut variables which maximize the Z->ee trigger efficiency
	maxEff = 0.
	indexOfMaxEff = 0
	#print 'there are this many entries in the list cutsRatesAndEffs ', addedElementToCutsRatesEffs
	for i in xrange(addedElementToCutsRatesEffs):
		if(numEntriesInAllSets==1):
			break
		if(cutsRatesAndEffs[i][6] > maxEff):
			maxEff = 0.
			maxEff += cutsRatesAndEffs[i][6]
			indexOfMaxEff = 0
			indexOfMaxEff += i
	
	#end loop over cutsRatesAndEffs
	#totalRate, zEff, bkgndRate, numBkgndEvts, signalRate, numUnmatchedSigEvts
	
	#allSetsOfInitialVals.append([minHltPT, sortedSigmaIEIECutArr[(multiplier*r)], sortedEcalIsoCutArr[(multiplier*t)], sortedHoverECutArr[(multiplier*w)], sortedHcalIsoCutArr[(multiplier*g)], totRate, zedEff, 0., numBkgEvts, totRate, numGoodEvts, multiplier*r, multiplier*t, multiplier*w, multiplier*g] )
	
	if(numEntriesInAllSets==1):
		#move values from allSetsOfInitialVals list to cutsRatesAndEffs list
		cutsRatesAndEffs.append([allSetsOfInitialVals[0][0], allSetsOfInitialVals[0][1],allSetsOfInitialVals[0][2],allSetsOfInitialVals[0][3],allSetsOfInitialVals[0][4],allSetsOfInitialVals[0][5],allSetsOfInitialVals[0][6],allSetsOfInitialVals[0][7],allSetsOfInitialVals[0][8],allSetsOfInitialVals[0][9],allSetsOfInitialVals[0][10],allSetsOfInitialVals[0][11],allSetsOfInitialVals[0][12],allSetsOfInitialVals[0][13],allSetsOfInitialVals[0][14]])



	#now that a local maximum in Z->ee eff has been found, look in the neighborhood of the optimal cut threshold values to find a settings which
	#maximize Z->ee efficiency, and bring the calculated rate as close as possible to the desired rate
	#cutsRatesAndEffs has all the information I need, I just need to repeat the system of 4 nested for loops
	#cutsRatesAndEffs[someRow][11 to 14] contain the indexes of sigmaIEIE, ecalIso, had/em, and hcalIso list values which maximize efficiency
	numInterestingSets = 0
	refinedCutsRatesAndEffs = []
	for b in xrange(5):
		#loop over sigmaIEIE values near local max value of sigmaIEIE determined previously
		print 'starting sigmaIEIE loop number ', b+1 , ' out of 5'
		print 'found ', numInterestingSets, ' sets of interesting cut threshold values'
		for q in xrange(5):
			#loop over ecalIso values near local max value of ecalIso determined previously
			for p in xrange(5):
				#loop over hOverE values near local max value of hOverE determined previously
				for u in xrange(5):
					#loop over hcalIso values near local max value of hcalIso determined previously
					numBgEvts = 0.
					numDyEvts = 0.
					numZeeEvts = 0.

					#use these to compactify code
					sigmaIndex = cutsRatesAndEffs[indexOfMaxEff][11] - 3 + b
					ecalIndex = cutsRatesAndEffs[indexOfMaxEff][12] - 3 + q
					hOvrEmIndex = cutsRatesAndEffs[indexOfMaxEff][13] - 3 + p 
					hcalIndex = cutsRatesAndEffs[indexOfMaxEff][14] - 3 + u

					if(sigmaIndex < 0 or ecalIndex < 0 or hOvrEmIndex < 0 or hcalIndex < 0):
						continue

					#begin loop over Z->ee candidate evts (a subset of DY->ee evts) which fired the trigger with the loose trackless leg
					for i in xrange(maxMatchedSigEvts):
						if(tupleForMatchedSigEvts[i][0] > minHltPT):
							if(tupleForMatchedSigEvts[i][1] < sortedSigmaIEIECutArr[sigmaIndex]):
								if(tupleForMatchedSigEvts[i][2] < sortedEcalIsoCutArr[ecalIndex]):
									if(tupleForMatchedSigEvts[i][3] < sortedHoverECutArr[hOvrEmIndex]):
										if(tupleForMatchedSigEvts[i][4] < sortedHcalIsoCutArr[hcalIndex]):
											numZeeEvts += 1.0

					#begin loop over DY->ee evts which fired the trigger with the loose trackless leg 
					for j in xrange(numUnmatchedSigEvtsPassingTrig):
						if(tupleForUnmatchedSigEvts[j][0] > minHltPT):
							if(tupleForUnmatchedSigEvts[j][1] < sortedSigmaIEIECutArr[sigmaIndex]):
								if(tupleForUnmatchedSigEvts[j][2] < sortedEcalIsoCutArr[ecalIndex]):
									if(tupleForUnmatchedSigEvts[j][3] < sortedHoverECutArr[hOvrEmIndex]):
										if(tupleForUnmatchedSigEvts[j][4] < sortedHcalIsoCutArr[hcalIndex]):
											numDyEvts += 1.0
		
					#end loop over DY->ee evts to determine # of signal events which fired trigger
					#begin loop over minBias evts which fired the trigger with the loose trackless leg 
					for k in xrange(numBkgndEvtsPassingTrigger):
						if(tupleForBkgndEvtsPassingTrig[k][0] > minHltPT):
							if(tupleForBkgndEvtsPassingTrig[k][1] < sortedSigmaIEIECutArr[sigmaIndex]):
								if(tupleForBkgndEvtsPassingTrig[k][2] < sortedEcalIsoCutArr[ecalIndex]):
									if(tupleForBkgndEvtsPassingTrig[k][3] < sortedHoverECutArr[hOvrEmIndex]):
										if(tupleForBkgndEvtsPassingTrig[k][4] < sortedHcalIsoCutArr[hcalIndex]):
											numBgEvts += 1.0
						
					#end loop over minBias evts to determine # of bkgnd events which fired trigger
					#now calculate the total trigger rate
					refinedBkgndRate = (minBiasXSxn*peakLumi*numBgEvts)/totalBkgndEvts
					refinedSignalRate = (signalXSxn*peakLumi*numDyEvts)/totalUnmatchedSigEvts
					#print 'signal trigger rate equals ', signalRate
					#print 'num unmatched sig evts passing trig = ', numUnmatchedSigEvts
					#print 'total num unmatched sig evts analyzed = ', totalUnmatchedSigEvts
					refinedTotalRate = 0.
					refinedTotalRate += refinedSignalRate + refinedBkgndRate
					#if(b < 3 and u == 0 and p == 0):
					#	print ' '
					#	print 'sigma loop number ', b+1, ' out of 5'
					#	print 'sigmaIndex = ', sigmaIndex
					#	print 'ecalIndex = ', ecalIndex
					#	print 'hOvrEmIndex = ', hOvrEmIndex
					#	print 'hcalIndex = ', hcalIndex
					#	print 'total trigger rate = ', refinedTotalRate
					if(refinedTotalRate >= minRateFraction*desiredRate and refinedTotalRate <= maxRateFraction*desiredRate):
						refinedZeff = (numZeeEvts/effDenom)
						refinedCutsRatesAndEffs.append([minHltPT, sortedSigmaIEIECutArr[sigmaIndex], sortedEcalIsoCutArr[ecalIndex], sortedHoverECutArr[hOvrEmIndex], sortedHcalIsoCutArr[hcalIndex], refinedTotalRate, refinedZeff, refinedBkgndRate, numBgEvts, refinedSignalRate, numDyEvts, sigmaIndex, ecalIndex, hOvrEmIndex, hcalIndex])
						numInterestingSets += 1

				#end loop over relative hcalIso
			#end loop over (had/em)/energy
		#end loop over relative ecalIso
	#end loop over sigma ieta ieta
	
	#find the max Z->ee trigger efficiency in refinedCutsRatesAndEffs
	finalMaxEff = 0.
	indexOfFinalMaxEff = 0
	for e in xrange(numInterestingSets):
		if( refinedCutsRatesAndEffs[e][6] > finalMaxEff ):
			finalMaxEff = 0.
			finalMaxEff += refinedCutsRatesAndEffs[e][6]
			indexOfFinalMaxEff = 0
			indexOfFinalMaxEff += e
	#end loop over entries in refinedCutsRatesAndEffs list

	#fill a 1D array with the five optimal cut values, the trigger rate, the Z->ee trigger efficiency, the bkgnd rate, the num of bkgnd evts passing the trigger, the signal rate, and the num of signal evts passing the trigger
	optimalValues = []
	for g in xrange(11):
		optimalValues.append(refinedCutsRatesAndEffs[indexOfFinalMaxEff][g])
		if(g == 0):
			print 'optimized total rate = ', refinedCutsRatesAndEffs[indexOfFinalMaxEff][5]
			print 'optimized Z->ee trig efficiency = ', finalMaxEff
	
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
#f1 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/signal_10kevts_very_loose_trackless_leg.root")


f2 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/unmatched_signal_ALLevts_very_loose_trackless_leg.root")

#f3 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/biggest_sample_bkgnd_evts_very_loose_trackless_leg.root")
f3 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/tuples_all_bkgnd_evts.root")

f4 = ROOT.TFile("/afs/cern.ch/work/s/skalafut/public/doubleElectronHLT/biggest_signal_sample_AOD_data.root")


#tree for signal evts which fire the trigger and are matched to gen electrons from Z decay
t1 = f1.Get("demo/doubleEleTrigger")

#tree for signal evts which fire the trigger but are not matched to gen electrons
t2 = f2.Get("demo/doubleEleTrigger")

#tree for bkgnd evts which fire the trigger
t3 = f3.Get("demo/doubleEleTrigger")

#tree for signal evts with AOD data
t4 = f4.Get("demo/doubleEleTrigger")


#array vars
matchedSigTuple = []
sigEcalIso = []
sigHcalIso = []
sigHoverE = []
sigSigmaIEIE = []
sigPt = []
sigEta = []
sigHltMll = []  #hlt_mLL_ for Z->ee evts
bkgndHltMLL = []
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
		bkgndTuple.append([t3.matched_pT_, t3.matched_ecalClusterShape_SigmaIEtaIEta_, t3.matched_ecalIso_/t3.matched_pT_, t3.matched_hOverE_/(t3.matched_pT_*(math.cosh(t3.matched_eta_)) ), t3.matched_hcalIso_/t3.matched_pT_, t3.hlt_mLL_])
		numBkgndEvtsFired += 1
		bkgndHltMLL.append(t3.hlt_mLL_)
		#bkgndPt.append(t3.matched_pT_)
		#bkgndSigmaIEIE.append(t3.matched_ecalClusterShape_SigmaIEtaIEta_)
		#bkgndEcalIso.append(t3.matched_ecalIso_/t3.matched_pT_)
		#bkgndHoverE.append(t3.matched_hOverE_/(t3.matched_pT_*(math.cosh(t3.matched_eta_)) ))
		#bkgndHcalIso.append(t3.matched_hcalIso_/t3.matched_pT_)

print 'the number of minBias evts which fired the trigger = ', numBkgndEvtsFired
print 'the total number of minBias evts which were passed through the trigger = ', t3.GetEntries()

#pT, sigmaIEIE, ecal iso/pT, had/em / energy, hcal iso/pT for sig evts not matched to gen electrons which fire the very loose trigger
unmatchedSigTuple = []
numUnmatchedSigEvtsFired = 0

for q in xrange(t2.GetEntries()):
	t2.GetEntry(q)
	if(t2.matched_pT_ > 0.):
		#print 'found a DY->ee evt which fired loose double electron trigger'
		unmatchedSigTuple.append([t2.matched_pT_, t2.matched_ecalClusterShape_SigmaIEtaIEta_, t2.matched_ecalIso_/t2.matched_pT_, t2.matched_hOverE_/(t2.matched_pT_*(math.cosh(t2.matched_eta_)) ), t2.matched_hcalIso_/t2.matched_pT_, t2.hlt_mLL_])
		numUnmatchedSigEvtsFired += 1

print 'the number of DY->ee evts which fired the trigger = ', numUnmatchedSigEvtsFired
print 'the total number of DY->ee evts which were passed through the trigger = ', t2.GetEntries()

#go through TTree with AOD data and get useful quantities from Z->ee candidate signal evts
#genMLL_, reco_mLL_, pT and eta of both GEN electrons and matched reco objects (GSF electron, EE supercluster)
#in evts where genTriggeredEvent_ > 0., genMLL_ btwn 60. and 120., a reco GSF electron matched to the GEN tracked electron, and
#a reco EE supercluster is matched to the GEN trackless electron
#if reco_tracked_pT_ > 0 then there is a reco GSF electron matched to the GEN tracked electron in the event
#if reco_untracked_pT_ > 0 then there is a reco EE supercluster matched to the GEN trackless electron in the event
numAodZedPeakEvts = 0
aodTuple = []  #contains useful GEN and RECO info from Z->ee candidate signal evts
for y in xrange(t4.GetEntries()):
	t4.GetEntry(y)
	if(t4.genTriggeredEvent_ > 0. and t4.genMLL_ > 60. and t4.genMLL_ < 120. and t4.reco_tracked_pT_ > 0. and t4.reco_untracked_pT_ > 0.):
		numAodZedPeakEvts += 1
		aodTuple.append([t4.gen_trackless_pT_, t4.gen_trackless_eta_, t4.gen_tracked_pT_, t4.gen_tracked_eta_, t4.genMLL_, t4.reco_tracked_pT_, t4.reco_tracked_eta_, t4.reco_untracked_pT_, t4.reco_untracked_eta_, t4.reco_mLL_ ])


#denominator of Z->ee trigger efficiency
#equal to # of events with one untracked EE gen e- (pT > 15), one tracked gen e- (pT > 27), and GEN dilepton mass btwn 60. and 120. GeV
efficiencyDenom = 0	

analyzeThisManyEvents = t1.GetEntries() #the number of TTree entries to inspect
#eventually swap 2000 for t1.GetEntries()
for z in xrange(analyzeThisManyEvents):
	#loop over all events that were analyzed to make signal.root
	t1.GetEntry(z)
	foundMatchingAodEvt = False
	#calculate two dilepton mass values for the signal event (dy->ee)
	#one value uses GEN electron kinematics, while the other value uses RECO gsf electron and supercluster kinematics
	if(t1.genTriggeredEvent_ > 0. and t1.genMLL_ > 60. and t1.genMLL_ < 120.):
		matchingAodTupleIndex = 0	#value of c where aodTuple[c][] matches t1.GetEntry(z)
		for c in xrange(numAodZedPeakEvts):
			#see if there is an entry in aodTuple with GEN electrons which match the GEN electrons in t1.GetEntry(z)
			#the aodTuple is only filled with events where genTriggeredEvent_ > 0, genMLL_ btwn 60 and 120, and where a reco GSF electron
			#is matched to the GEN tracked electron, and a reco EE supercluster is matched to the GEN trackless electron
			if(t1.gen_trackless_pT_ == aodTuple[c][0] and t1.gen_trackless_eta_ == aodTuple[c][1] and t1.gen_tracked_pT_ == aodTuple[c][2] and t1.gen_tracked_eta_ == aodTuple[c][3]):
				foundMatchingAodEvt = True
				matchingAodTupleIndex += c
				break  #leave loop over c (aodTuple entries)
	#end filter on genTriggeredEvent_ and genMLL_
	if(foundMatchingAodEvt):
		#increment efficiency denominator
		efficiencyDenom += 1.
		genTrackedPt.append(t1.gen_tracked_pT_)
		genTracklessPt.append(t1.gen_trackless_pT_)
		if(t1.matched_pT_ > 0.):
			#fill sigEcalIso, sigPt, and other sig lists if the trigger fires in t1.GetEntry(z) 
			matchedSigTuple.append([t1.matched_pT_, t1.matched_ecalClusterShape_SigmaIEtaIEta_, t1.matched_ecalIso_/t1.matched_pT_, t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ), t1.matched_hcalIso_/t1.matched_pT_, t1.hlt_mLL_])
			sigEcalIso.append(t1.matched_ecalIso_/t1.matched_pT_)
			sigHcalIso.append(t1.matched_hcalIso_/t1.matched_pT_)
			sigHoverE.append(t1.matched_hOverE_/(t1.matched_pT_*(math.cosh(t1.matched_eta_)) ))
			sigSigmaIEIE.append(t1.matched_ecalClusterShape_SigmaIEtaIEta_)
			sigPt.append(t1.matched_pT_)
			sigEta.append(t1.matched_eta_)
			sigHltMll.append(t1.hlt_mLL_)
			#use matchingAodTupleIndex here to pull any information from the AOD TTree
			if(aodTuple[matchingAodTupleIndex][9] > 0.):
				#if reco_mLL_ > 0. then a reco GSF electron and EE supercluster matched to the two GEN electrons were found in t1.GetEntry(z)
				recoDileptonMass.append(aodTuple[matchingAodTupleIndex][9])
				recoTrackedPt.append(aodTuple[matchingAodTupleIndex][5])
				recoTrackedEta.append(aodTuple[matchingAodTupleIndex][6])
				recoUntrackedPt.append(aodTuple[matchingAodTupleIndex][7])
				recoUntrackedEta.append(aodTuple[matchingAodTupleIndex][8])
			#end if(reco_mLL_ > 0.)
		#end requirement that the trigger is fired in t1.GetEntry(z)
	#end filter on foundMatchingAodEvt
#end loop over entries in TTree t1


#matchedSigTupleLen defined here is equal to the # of events which passed the trackless leg of the trigger
matchedSigTupleLen = float(len(matchedSigTuple))
sigPtLen = int(len(sigPt))
#print 'sigPtLen equals ', sigPtLen
recoDileptonLen = int(len(recoDileptonMass))
maxEff = float(len(sigPt))*(100)/efficiencyDenom
print 'Z->ee trig eff denominator = ', efficiencyDenom
print 'max Z->ee trig eff numerator = ', len(sigPt)
print 'max Z->ee trig eff = ', maxEff

#make sorted arrays of sigPt, sigSigmaIEIE, sigEcalIso, sigHoverE, and sigHcalIso
#all arrays except sigPt and sigHltMll will be sorted from high to low (last element is smallest value)
sortedPt = sorted(sigPt)
tempSortedSigmaIEIE = sorted(sigSigmaIEIE, reverse=True)
tempSortedEcalIso = sorted(sigEcalIso, reverse=True)
tempSortedHoverE = sorted(sigHoverE, reverse=True)
tempSortedHcalIso = sorted(sigHcalIso, reverse=True)
tempSortedHltMll = sorted(sigHltMll)

#dont include very large or very small values in sorted lists
sortedSigmaIEIE = []
sortedEcalIso = []
sortedHoverE = []
sortedHcalIso = []
sortedHltMll = []

maxSigmaIEIE = 0.048
maxEcalIso = 0.31
maxHoverE = 0.11
maxHcalIso = 0.3
minHltMll = 95.

for y in xrange( int(len(sigPt)) ):
	if(tempSortedSigmaIEIE[y] < maxSigmaIEIE):
		sortedSigmaIEIE.append(tempSortedSigmaIEIE[y])
	if(tempSortedEcalIso[y] < maxEcalIso):
		sortedEcalIso.append(tempSortedEcalIso[y])
	if(tempSortedHoverE[y] < maxHoverE):
		sortedHoverE.append(tempSortedHoverE[y])
	if(tempSortedHcalIso[y] < maxHcalIso):
		sortedHcalIso.append(tempSortedHcalIso[y])
	if(tempSortedHltMll[y] > minHltMll):
		sortedHltMll.append(tempSortedHltMll[y])
#end loop over y

#returned array contains these elements in this exact order:
#pT, sigmaIEIE, ecal iso/pT, (had/em)/energy, hcal iso/pT, total rate, Z->ee efficiency, bkgnd rate, bkgnd evts passing trig, signal rate, signal evts passing trig
#the last six elements should be used to plot Z->ee efficiency as a function of total rate + uncertainty

optimalCuts = []	#a 5D array which stores the values of the 5 cut variables used in the trackless leg of the trigger
zEff = []
zEffErr = []
totalTrigRate = []
#totalTrigRateErr = []

#good values to use are targetRate <= 1.0 
#bad values to use are targetRate > 1.25
findOptimalCutValuesAndRateAndEff(1.0, efficiencyDenom, sortedPt, sortedSigmaIEIE, sortedEcalIso, sortedHoverE, sortedHcalIso, t3.GetEntries(), numBkgndEvtsFired, bkgndTuple, t2.GetEntries(), numUnmatchedSigEvtsFired, unmatchedSigTuple, int(len(sigPt)), matchedSigTuple)

#highRate = 0.95 
#incrementRate = 0.1 
#numDiffRates = 1 
#for q in xrange(numDiffRates):
#	targetRate = (highRate - q*incrementRate)
#	optimizedCutsRateAndEff = findOptimalCutValuesAndRateAndEff(targetRate, efficiencyDenom, sortedPt, sortedSigmaIEIE, sortedEcalIso, sortedHoverE, sortedHcalIso, t3.GetEntries(), numBkgndEvtsFired, bkgndTuple, t2.GetEntries(), numUnmatchedSigEvtsFired, unmatchedSigTuple, int(len(sigPt)), matchedSigTuple)
#
#	print 'q = ', q
#	optimalCuts.append([optimizedCutsRateAndEff[0], optimizedCutsRateAndEff[1], optimizedCutsRateAndEff[2], optimizedCutsRateAndEff[3], optimizedCutsRateAndEff[4] ])
#	totalTrigRate.append(optimizedCutsRateAndEff[5])
#	#bkgndRateErr = optimizedCutsRateAndEff[7]/math.sqrt(optimizedCutsRateAndEff[8])
#	#signalRateErr = optimizedCutsRateAndEff[9]/math.sqrt(optimizedCutsRateAndEff[10])
#	#totalTrigRateErr.append(math.sqrt( math.pow(bkgndRateErr,2) + math.pow(signalRateErr,2) ) )
#	zEff.append(optimizedCutsRateAndEff[6])
#	zEffErr.append(0.0)
#	print ' '
#	print 'Z->ee trig eff = ', zEff[q]
#	print 'total trig rate = ', totalTrigRate[q]
#	#print 'total trig rate err = ', totalTrigRateErr[q]
#	print 'min PT = ', optimalCuts[q][0]
#	print 'max sigmaIEIE = ', optimalCuts[q][1]
#	print 'max ecal iso/PT = ', optimalCuts[q][2]
#	print 'max had/em / Energy = ', optimalCuts[q][3]
#	print 'max hcal iso/PT = ', optimalCuts[q][4]
#	print ' '


#effVsRateGraph(zEff, zEffErr, totalTrigRate, totalTrigRateErr, "Z->ee trigger efficiency vs total trigger rate","../triggerPlots/efficiencies/optimizedZtoEE_eff_vs_trigRate_allEvts.png" )


#sigEff_EcalIso = []
#sigEff_HcalIso = []
#sigEff_HoverE = []
#sigEff_SigmaIEIE = []
#sigEff_Pt = []
#sigEff_Eta = []
#sigEff_HltMll = []
#
##for loop to fill sigEff_* arrays 
##sigPt, sigEcalIso, sigEff_* should all have the same length
#for q in xrange(int(len(sigPt)) ):
#	sigEff_EcalIso.append( calcEff(True, sigEcalIso, sigEcalIso[q], efficiencyDenom ) )
#	sigEff_HcalIso.append( calcEff(True, sigHcalIso, sigHcalIso[q], efficiencyDenom ) )
#	sigEff_HoverE.append( calcEff(True, sigHoverE, sigHoverE[q], efficiencyDenom ) )
#	sigEff_SigmaIEIE.append( calcEff(True, sigSigmaIEIE, sigSigmaIEIE[q], efficiencyDenom ) )
#	sigEff_Pt.append( calcEff(False, sigPt, sigPt[q], efficiencyDenom ) )
#	sigEff_Eta.append( calcEff(False, sigEta, sigEta[q], efficiencyDenom ) )
#	sigEff_HltMll.append( calcEff(False, sigHltMll, sigHltMll[q], efficiencyDenom ) )
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
#
#
#efficiencyGraph(sigEcalIso,sigEff_EcalIso,"canvEcalIso","Z->ee trig efficiency vs HLT EcalIso/HLT PT",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_EcalIsoGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigHcalIso,sigEff_HcalIso,"canvHcalIso","Z->ee trig efficiency vs HcalIso/HLT PT",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_HcalIsoGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigHoverE,sigEff_HoverE,"canvHoverE","Z->ee trig efficiency vs HoverE/HLT E",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_HoverEGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigSigmaIEIE,sigEff_SigmaIEIE,"canvSigmaIEIE","Efficiency vs HLT #sigma_{i#etai#eta}",True, False,"../triggerPlots/efficiencies/ZtoEE_trigEff_SigmaIEIEGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigPt,sigEff_Pt,"canvPt","Z->ee trig efficiency vs HLT PT",True, True,"../triggerPlots/efficiencies/ZtoEE_trigEff_PtGraph_low_thresholds_allEvts.png")
#efficiencyGraph(sigHltMll,sigEff_HltMll,"canvHltMll","Z->ee trig efficiency vs HLT M_{LL}",True, True,"../triggerPlots/efficiencies/ZtoEE_trigEff_HltMllGraph_low_thresholds_allEvts.png")
##efficiencyGraph(sigEta,sigEff_Eta,"canvEta","Efficiency vs HLT Eta",True, True,"../triggerPlots/efficiencies/ZtoEE_trigEff_EtaGraph_low_thresholds_allEvts.png")
#
#makeAndSaveHisto(sigEcalIso, "EcalIsoHistoCanv","EcalIso/HLT PT of trackless HLT objects in Z->ee trig events",100,-0.3,0.5, "../triggerPlots/hltObjectPlots/signal_EcalIsoHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigSigmaIEIE, "SigmaIEIEHistoCanv","#sigma_{i#etai#eta} of trackless HLT objects in Z->ee trig events",100,0.,0.2, "../triggerPlots/hltObjectPlots/signal_SigmaIEIEHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigHcalIso, "HcalIsoHistoCanv","HcalIso/HLT PT of trackless HLT objects in Z->ee trig events",100,-0.3,0.5, "../triggerPlots/hltObjectPlots/signal_HcalIsoHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigHoverE, "HoverEHistoCanv","HoverE/HLT E of trackless HLT objects in Z->ee trig events",100,0.,1, "../triggerPlots/hltObjectPlots/signal_HoverEHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigPt, "PtHistoCanv","P_{T} of trackless HLT objects in Z->ee trig events",100,0.,250., "../triggerPlots/hltObjectPlots/signal_HLT_matched_PtHisto_low_thresholds_allEvts.png")
#makeAndSaveHisto(sigHltMll, "HltMllHistoCanv","M_{LL} of HLT objects firing trigger in Z->ee events",200,0.,300., "../triggerPlots/hltObjectPlots/signal_HLT_matched_HltMllHisto_low_thresholds_allEvts.png")
#
#
#
#makeAndSaveHisto(genTracklessPt, "genTracklessPtHistoCanv","P_{T} of trackless gen electron from Z->ee decay",100,0.,150., "../triggerPlots/genParticlePlots/signal_gen_trackless_PtHisto_low_thresholds_allEvts.png")
#
#makeAndSaveHisto(genTrackedPt, "genTrackedPtHistoCanv","P_{T} of tracked gen electron from Z->ee decay",100,0.,150., "../triggerPlots/genParticlePlots/signal_gen_tracked_PtHisto_low_thresholds_allEvts.png")
#
#
#makeAndSaveHisto(recoDileptonMass, "recoMLLCanv","M_{LL} of reco Gsf Electron and EE supercluster in Z->ee triggered events",200, 0., 300., "../triggerPlots/recoPlots/recoDileptonMass_allEvts.png")
#
#makeAndSaveHisto(recoTrackedPt, "recoTrackedPtCanv","P_{T} of reco Gsf Electron in Z->ee triggered events",100, 0., 150., "../triggerPlots/recoPlots/recoTrackedPt_allEvts.png")
#
#makeAndSaveHisto(recoTrackedEta, "recoTrackedEtaCanv","eta of reco Gsf Electron in Z->ee triggered events",100, -3.5, 3.5, "../triggerPlots/recoPlots/recoTrackedEta_allEvts.png")
#
#makeAndSaveHisto(recoUntrackedPt, "recoUntrackedPtCanv","P_{T} of reco EE supercluster in Z->ee triggered events",100, 0., 150., "../triggerPlots/recoPlots/recoUntrackedPt_allEvts.png")
#
#makeAndSaveHisto(recoUntrackedEta, "recoUntrackedEtaCanv","eta of reco EE supercluster in Z->ee triggered events",100, -3.5, 3.5, "../triggerPlots/recoPlots/recoUntrackedEta_allEvts.png")
#
#makeAndSaveHisto(bkgndHltMLL, "bkgndHltMLLCanv","M_{LL} of HLT objects firing trigger in minBias events",200, 0., 300., "../triggerPlots/hltObjectPlots/bkgndHltMLL_allEvts.png")


#makeAndSaveHisto(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath)
#makeAndSaveGraph(someArray, canvName, histTitle, numBins, xmin, xmax, outFilePath)




