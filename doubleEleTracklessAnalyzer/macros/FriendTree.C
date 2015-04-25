{
  TString treeNameSignal="master_scanned_tree_signal";
  TString fileNameSignal="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/signal/doubleEG_22_10_master_signal_tuple.root";

  TString treeName30to80Bkg="master_scanned_tree_highPtBkgnd";
  TString fileName30to80Bkg="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_high_pt/doubleEG_22_10_master_high_pt_bkgnd_tuple.root";

  TString treeName20to30Bkg="master_scanned_tree_lowPtBkgnd";
  TString fileName20to30Bkg="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_low_pt/doubleEG_22_10_master_low_pt_bkgnd_tuple.root";

  TString treeName80to170Bkg="master_scanned_tree_veryHighPtBkgnd";
  TString fileName80to170Bkg="/eos/uscms/store/user/skalafut/doubleElectronHLT/scannedTuples/bkgnd_very_high_pt/doubleEG_22_10_master_very_high_pt_bkgnd_tuple.root";




  TChain sigbkg(treeNameSignal,"");
  sigbkg.Add(fileNameSignal);
  TChain bkg30to80(treeName30to80Bkg,"");
  bkg30to80.Add(fileName30to80Bkg);
  
  sigbkg.AddFriend(&bkg30to80, "bkg30to80");

  TChain bkg20to30(treeName20to30Bkg,"");
  bkg20to30.Add(fileName20to30Bkg);
  
  sigbkg.AddFriend(&bkg20to30, "bkg20to30");

  TChain bkg80to170(treeName80to170Bkg,"");
  bkg80to170.Add(fileName80to170Bkg);
  
  sigbkg.AddFriend(&bkg80to170, "bkg80to170");



  if(sigbkg.GetEntries()!=bkg30to80.GetEntries() || sigbkg.GetEntries()!=bkg20to30.GetEntries() || sigbkg.GetEntries()!=bkg80to170.GetEntries() ){
    std::cerr << "============================== ERROR!!!" << std::endl;
  }


}
