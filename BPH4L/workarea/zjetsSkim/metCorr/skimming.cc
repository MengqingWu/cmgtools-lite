//--------------------------------
// no new branches added
// fast and simple to copy a tree with cuts parsed
// @ June 13th, Mengqing
//--------------------------------

#include "TFile.h"
#include "TCanvas.h"
//#include "TH1.h"
#include "TH2D.h"
#include "TMath.h"
#include "TTree.h"
#include "TBranch.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>
//#include <time.h>       /* clock_t, clock, CLOCKS_PER_SEC */
#include <stdio.h>      /* printf */

int main(int argc, char** argv) {
  //clock_t timing;
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
  //timing = clock();
  TFile* zjsfFile = new TFile("ZJets_shape_correction_2d.root");
  TH2D* h2_dphi_sf_AB = (TH2D*)zjsfFile->Get("ZJstudy_regA_shiftB");
  TH2D* h2_dphi_sf_AC = (TH2D*)zjsfFile->Get("ZJstudy_regA_shiftC");
  TH2D* h2_dphi_sf_AD = (TH2D*)zjsfFile->Get("ZJstudy_regA_shiftD");

  Int_t bintest = h2_dphi_sf_AB->FindBin(0.69641, 220.0); // region B
  std::cout<< "[test] For dphi = 0.69641 (regB), met = 220 GeV, "
  	   <<" sf = " << h2_dphi_sf_AB->GetBinContent(bintest) << std::endl;

  // initialize ---->
  // root files
  TFile* finput = new TFile(inputfile.c_str());
  TFile* foutput = new TFile(outputfile.c_str(), "recreate");

  // in_tree
  TTree* tree_in = (TTree*)finput->Get("tree");
  std::cout<< tree_in->GetEntriesFast() <<" Events to process."<< std::endl;
  //tree_in->SetBranchStatus("met_*",0);
  //tree_in->SetBranchStatus("jet_*",0);
  // out_tree
  // TTree* tree_tmp = tree_in->CopyTree(Cuts.c_str());
  // std::cout<< tree_tmp->GetEntriesFast() <<" Events passed the cuts."<< std::endl;

  TTree* tree_out = tree_in->CloneTree(0);

  // read branches
  Float_t  llnunu_deltaPhi[1], llnunu_l2_pt[1];
  tree_in->SetBranchAddress("llnunu_deltaPhi", llnunu_deltaPhi); 
  tree_in->SetBranchAddress("llnunu_l2_pt", llnunu_l2_pt); 
  // new added branches
  Float_t dphi_sf;
  TBranch *b_dphi_sf = tree_out->Branch("dphi_sf",&dphi_sf,"dphi_sf/F");
  
  // Loop to fill ---->
  for (int i=0; i<(int)tree_in->GetEntries(); i++){ 
    tree_in->GetEntry(i);

    Int_t binx, biny;
    Float_t h2sf;
    std::string region;
    Float_t fabs_dphi=fabs(llnunu_deltaPhi[0]);
    if (fabs_dphi>0 && fabs_dphi<TMath::Pi()/4) {
      binx=h2_dphi_sf_AB->GetXaxis()->FindBin(fabs_dphi);
      biny=h2_dphi_sf_AB->GetYaxis()->FindBin(llnunu_l2_pt[0]);
      h2sf = h2_dphi_sf_AB->GetBinContent(binx, biny);
      region="regB";
    }
    else if (fabs_dphi> TMath::Pi()/4 && fabs_dphi< TMath::Pi()/2)   {
      binx=h2_dphi_sf_AD->GetXaxis()->FindBin(fabs_dphi);
      biny=h2_dphi_sf_AD->GetYaxis()->FindBin(llnunu_l2_pt[0]);
      h2sf = h2_dphi_sf_AD->GetBinContent(binx, biny);
      region="regD";
    }
    else if (fabs_dphi> TMath::Pi()/2 && fabs_dphi< 3*TMath::Pi()/4) {
      binx=h2_dphi_sf_AC->GetXaxis()->FindBin(fabs_dphi);
      biny=h2_dphi_sf_AC->GetYaxis()->FindBin(llnunu_l2_pt[0]);
      h2sf = h2_dphi_sf_AC->GetBinContent(binx, biny);
      region="regC";
    }
    else {h2sf=1;}

    dphi_sf = (h2sf==0) ? 1.0: h2sf;

    if (i%2000==0) {
      std::cout<< "Event "<<i<<std::endl;
      std::cout<< "[info] dphi = "<<fabs_dphi<<", met = "<< llnunu_l2_pt[0]
	       <<", I am in region "+ region+" with sf = "<< dphi_sf<<std::endl;
    }

    tree_out->Fill();
    
    //if( i==5000) break;
  }

  //timing=clock()-timing;
  //std::printf ("It took me %d clicks (%f seconds).\n",(int)timing,((float)timing)/CLOCKS_PER_SEC);
  // Terminate ---->
  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



