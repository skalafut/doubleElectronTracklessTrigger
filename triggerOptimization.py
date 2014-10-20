import ROOT
import array


def plotVar(v):
   h = ROOT.TH1F("h", "h", 100, 0, 0.5)
   for i in v:
      h.Fill(i)

   h.Draw()
   print h.Integral(60, 100)
   print h.Integral()
   raw_input()

def fcn(npar, gin, f, par, iflag):
   global ncount, target
      
   f[0] = abs(target - func(par))
   ncount += 1

def func(par):
    global sigVar, bkgVar
    varSigCut = 0
    for val in sigVar:
        if (val < par[0]):
            varSigCut += 1.

    varBkgCut = 0
    for val in bkgVar:
        if (val < par[0]):
            varBkgCut += 1.
        
    if (varBkgCut == 0):
        value = 1000000.
    else:
        value = varSigCut/varBkgCut
    return value

def minimization(conditions):
    global ncount
    ncount = 0

    gMinuit = ROOT.TMinuit(1)
    gMinuit.SetFCN(fcn)

    arglist = array.array('d', 10*[0.])
    ierflg = ROOT.Long(1982)

    arglist[0] = 1.
    gMinuit.mnexcm("SET ERR", arglist, 1, ierflg)

    # Set starting values and step sizes for parameters
    vstart = array.array( 'd', (conditions[0],))
    step   = array.array( 'd', (conditions[1],))
    gMinuit.mnparm( 0, "a1", vstart[0], step[0], conditions[2], conditions[3], ierflg)
    
    # Now ready for minimization step
    arglist[0] = 1000
    arglist[1] = .1
    gMinuit.mnexcm("MIGRAD", arglist, 2, ierflg)
    
    val = ROOT.Double()
    err = ROOT.Double()
    gMinuit.GetParameter(0, val, err)

    return val

def efficiency(var, cut, lt=True):
   global sigTupleLen
   num = 0
   for val in var:
      if (val < cut and lt):
         num += 1.
         
   print float(num), sigTupleLen
   ratio = float(num)/sigTupleLen
   return ratio

f1 = ROOT.TFile("test_sig.root")
f2 = ROOT.TFile("test_bkg.root")

t1 = f1.Get("tree")
t2 = f2.Get("tree")

sigTuple = []
bkgTuple = []

for z in xrange(t1.GetEntries()):
   t1.GetEntry(z)
   for el in xrange(t1.npf):
      if (t1.etpf[el] > 27 and abs(t1.etapf[el])<1.479):
         # sieie, hoe, ecal, hcal, deta, dphi, tkiso, eop
         if (t1.dphipf[el] < 9999.):
            sigTuple.append([t1.sieiepf[el], t1.hoepf[el]/t1.epf[el], t1.ecalpf[el]/t1.etpf[el],
                             t1.hcalpf[el]/t1.etpf[el], t1.detapf[el], t1.dphipf[el], t1.tkisopf[el]/t1.etpf[el], t1.eoppf[el]])

for z in xrange(t2.GetEntries()):
   t2.GetEntry(z)
   for el in xrange(t2.npf):
      if (t2.etpf[el] > 27 and abs(t2.etapf[el])<1.479):
         # sieie, hoe, ecal, hcal, deta, dphi, tkiso, eop
         if (t2.dphipf[el] < 9999.):
            bkgTuple.append([t2.sieiepf[el], t2.hoepf[el]/t2.epf[el], t2.ecalpf[el]/t2.etpf[el],
                             t2.hcalpf[el]/t2.etpf[el], t2.detapf[el], t2.dphipf[el], t2.tkisopf[el]/t2.etpf[el], t2.eoppf[el]])

sob = float(len(sigTuple))/float(len(bkgTuple))
sigTupleLen = float(len(sigTuple))

sob_vs_sig = []
targets = [sob+(50*sob/100.)*float(y) for y in xrange(100)]
# sieie, hoe, ecal, hcal, deta, dphi, tkiso, eop
conditions = [[0.015, 0.00001, 0, 1.2], [0.2, 0.001, 0, 1.0],    [0.5, 0.001, 0, 1.0],
              [0.5, 0.001, 0, 1.0],    [0.03, 0.0001, 0, 1.05], [0.1,  0.001, 0, 1.2],
              [0.5, 0.001, 0, 1.0],    [0.3, 0.0001, 0, 1.0]]

previousEff = 1.0
for target in targets:
   results = []
   for v in xrange(8):
      ncount = 0
      sigVar = array.array('f', [y[v] for y in sigTuple])
      bkgVar = array.array('f', [y[v] for y in bkgTuple])
      cut = minimization(conditions[v])
      results.append((cut, efficiency(sigVar, cut)))
      
   maxCut=0.
   maxEff = 1.0
   maxVar = ""
   f = open("migrad_results.txt", "append")
   f.write("+++++++++++++++++++++++++++++\n")
   for i,r in enumerate(results):
      f.write(str(r[0])+" "+str(r[1])+ "\n")
      if ((previousEff-r[1]) < maxEff):
         maxEff = previousEff-r[1]
         maxVar = i
         maxCut = r[0]
         
   previousEff = results[maxVar][1]
   sob_vs_sig.append((previousEff, target))

   f.write("Chosen:%d\n"%maxVar)
   conditions[maxVar][0]=maxCut*0.9
   conditions[maxVar][3]=maxCut
   strFinale = " ".join(["%1.3f"%(c[3]) for c in conditions])
   f.write("Current Selection: "+strFinale)

   # pruning lists 
   newSigTuple = []
   for n in sigTuple:
      if (n[maxVar] < maxCut):
         newSigTuple.append(n)
   sigTuple = newSigTuple

        
   newBkgTuple = []
   for n in bkgTuple:
      if (n[maxVar] < maxCut):
         newBkgTuple.append(n)
   bkgTuple = newBkgTuple

   f.close()

x = array.array('f', [])
y = array.array('f', [])

for i in sob_vs_sig:
    x.append(i[0])
    y.append(i[1])

g1 = ROOT.TGraph(len(x), x, y)

g1.Draw("AP")
raw_input()

