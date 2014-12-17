doubleElectronTracklessTrigger
==============================

trackless double electron HLTrigger

This package of code contains the tools needed to:
1. filter GEN-SIM-RAW events through a double electron trigger.  Objects which pass each module in the trigger are
saved into a collection of HLT Trigger objects with references.
2. Study the objects which fire trigger modules, and save the attributes of these objects which are relevant to the trigger
(ECAL shower shape, ecal iso, H/E, hcal iso, pT, eta) into a TTree.  Kinematic variables of the gen level electrons matched
to these trigger objects are also saved into the same TTree.
3. Pull data from the TTree and make plots of trigger cut variables, and trigger efficiency as a function of different cut
variables.

Step 1 is accomplished by creating a GRID proxy and executing:

cmsRun hlt_tracklessDoubleElectron.py

Step 2 is accomplished by executing:

cmsRun python/ConfFile_cfg.py

Step 3 is accomplished by executing:

root -l
TPython::LoadMacro("trigOptimization.py");
