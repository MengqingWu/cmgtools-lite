#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include "TVector2.h"
#include "TMath.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

Float_t dphi_0_phi(Float_t phi1, Float_t phi2){
  Float_t dphi_tmp = fabs(phi1-phi2);
  if (dphi_tmp > 3.141593) dphi_tmp=fabs(dphi_tmp-2*3.141593);
  return dphi_tmp;
}

int main(int argc, char** argv) {

  if( argc<3 ) {
     std::cout << argv[0] << ":  " << std::endl ;
     std::cout << " Functionality: skimming... "  << std::endl;
     std::cout << "                 "  << std::endl;
     std::cout << " usage: " << argv[0] << " inputfile.root outputfile.root cut_string " << std::endl ;
     exit(1) ;
  }

  // input file name
  std::string inputfile((const char*)argv[1]); 
  // output file name
  std::string outputfile((const char*)argv[2]);
  // cuts
  std::string Cuts((const char*)argv[3]);

  // initialize
  // root files
  TFile* finput = new TFile(inputfile.c_str());
  TFile* foutput = new TFile(outputfile.c_str(), "recreate");

  // tree
  TTree* tree_in = (TTree*)finput->Get("tree");
  tree_in->SetBranchStatus("genLep*",0);
  //tree_in->SetBranchStatus("elmununu_LV_*",0);
  tree_in->SetBranchStatus("llnunu_LV_*",0);
  //tree_in->SetBranchStatus("*_p4*",0);
  std::cout<<"debug: in tree entries = "<<tree_in->GetEntriesFast()<<std::endl;
  
  // out_tree
  TTree* tree_tmp = tree_in->CopyTree(Cuts.c_str());
  //TTree* tree_out = tree_tmp->CloneTree(0);
  std::cout<<"debug: out tree entries = "<<tree_tmp->GetEntriesFast()<<std::endl;
  
  tree_tmp->Write();
  //tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



