//--------------------------------
// no new branches added
// fast and simple to copy a tree with cuts parsed
// @ June 13th, Mengqing
//--------------------------------

#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

int main(int argc, char** argv) {

  if( argc<3 ) {
     std::cout << argv[0] << ":  " << std::endl ;
     std::cout << " Functionality: skimming... "  << std::endl;
     std::cout << "                 "  << std::endl;
     std::cout << " usage: " << argv[0] << " inputfile.root outputfile.root Nevts SumWeights cut_string " << std::endl ;
     exit(1) ;
  }

  // input file name
  std::string inputfile((const char*)argv[1]); 
  // output file name
  std::string outputfile((const char*)argv[2]);
  // cuts
  std::string Cuts((const char*)argv[3]);

  // initialize ---->
  // root files
  TFile* finput = new TFile(inputfile.c_str());
  TFile* foutput = new TFile(outputfile.c_str(), "recreate");

   // in_tree
  TTree* tree_in = (TTree*)finput->Get("tree");
  // tree_in->SetBranchStatus("dPhi_jetMet*",0);
  // tree_in->SetBranchStatus("metNoJet*",0);
  // tree_in->SetBranchStatus("sumJetsInT1*",0);
  // tree_in->SetBranchStatus("elmu_*",0);
  tree_in->SetBranchStatus("Flag_*",0);
  tree_in->SetBranchStatus("*nunu_l1_l*_c*",0);
  tree_in->SetBranchStatus("*nunu_l1_l*_d*",0);
  tree_in->SetBranchStatus("*nunu_l1_l*_*rack*",0);
  tree_in->SetBranchStatus("*nunu_l2_raw*",0);
  tree_in->SetBranchStatus("*nunu_l2_gen*",0);
  // out_tree
  TTree* tree_out = tree_in->CopyTree(Cuts.c_str());
  //TTree* tree_out = tree_in->CloneTree(0);
  std::cout<< tree_out->GetEntriesFast() <<" Events processed."<< std::endl;
    
  // Loop to fill ---->
  // for (int i=0; i<(int)tree_in->GetEntries(); i++){ 
  //   tree_in->GetEntry();
  //   tree_out->Fill();
  //   if (i%100==0) std::cout<<"Event "<<i<<std::endl;
  //   if( i==200) break;
  // }

  // Terminate ---->
  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



