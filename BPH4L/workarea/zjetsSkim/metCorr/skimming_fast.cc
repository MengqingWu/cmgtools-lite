//--------------------------------
// no new branches added
// fast and simple to copy a tree with cuts parsed
// @ June 13th, Mengqing
//--------------------------------

#include "TFile.h"
#include "TCanvas.h"
#include "TH1.h"
#include "TMath.h"
#include "TTree.h"
#include "TBranch.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
#include <time.h>       /* clock_t, clock, CLOCKS_PER_SEC */
#include <stdio.h>      /* printf */

int main(int argc, char** argv) {
  clock_t timing;
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
  timing = clock();

  // initialize ---->
  // root files
  TFile* finput = new TFile(inputfile.c_str());
  TFile* foutput = new TFile(outputfile.c_str(), "recreate");

  // in_tree
  TTree* tree_in = (TTree*)finput->Get("tree");
  std::cout<< tree_in->GetEntriesFast() <<" Events to process."<< std::endl;
  tree_in->SetBranchStatus("met_*",0);
  tree_in->SetBranchStatus("jet_*",0);

  // out_tree
  TTree* tree_out = tree_in->CopyTree(Cuts.c_str());
  std::cout<< tree_out->GetEntriesFast() <<" Events passed the cuts."<< std::endl;

  timing=clock()-timing;
  std::printf ("It took me %d clicks (%f seconds).\n",(int)timing,((float)timing)/CLOCKS_PER_SEC);
  // Terminate ---->
  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



