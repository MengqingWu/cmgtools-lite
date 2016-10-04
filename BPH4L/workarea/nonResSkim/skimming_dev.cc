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
  tree_in->SetBranchStatus("elmununu*",0);
  
  // out_tree
  TTree* tree_tmp = tree_in->CopyTree(Cuts.c_str());
  std::cout<< tree_tmp->GetEntriesFast() <<" Events processed."<< std::endl;
  TTree* tree_out = tree_tmp->CloneTree(0);

  // read branches
  Float_t  llnunu_l1_l1_phi[1], llnunu_l1_l2_phi[1],
           llnunu_l1_l1_eta[1], llnunu_l1_l2_eta[1],
           jet_corr_phi[15], jet_corr_eta[15],
           lep_phi[5],    lep_eta[5];
  tree_tmp->SetBranchAddress("llnunu_l1_l1_phi", llnunu_l1_l1_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l2_phi", llnunu_l1_l2_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l1_eta", llnunu_l1_l1_eta);
  tree_tmp->SetBranchAddress("llnunu_l1_l2_eta", llnunu_l1_l2_eta);
  tree_tmp->SetBranchAddress("lep_phi", lep_phi);
  tree_tmp->SetBranchAddress("lep_eta", lep_eta);
  tree_tmp->SetBranchAddress("jet_corr_phi", jet_corr_phi);
  tree_tmp->SetBranchAddress("jet_corr_eta", jet_corr_eta);
  
  // new added branches
  Int_t nlep_corr;
  Float_t dphi_lep[5], dphi_jet[5];
  TBranch *b_nlep_corr = tree_out->Branch("nlep_corr",&nlep_corr,"nlep_corr/I");
  TBranch *b_dphi_lep = tree_out->Branch("dphi_lep",dphi_lep,"dphi_lep/F");
  TBranch *b_dphi_jet = tree_out->Branch("dphi_jet",dphi_jet,"dphi_jet/F");
  
  // Loop to fill ---->
  for (int ientry=0; ientry<(int)tree_tmp->GetEntries(); ientry++){ 
    tree_tmp->GetEntry(ientry);

    
    // Loop all jets:
    for (int ijet=0; ijet<15; ijet++){
      if (fabs(jet_corr_eta[ijet])>10. || fabs(jet_corr_phi[ijet])>2*TMath::Pi()) continue;
      else{
	// Compute dr as TLorentzVector::DeltaR :
	Float_t deltaR2_1 = pow(jet_corr_eta[ijet] - llnunu_l1_l1_eta[0],2) + pow(TVector2::Phi_mpi_pi(jet_corr_phi[ijet] - llnunu_l1_l1_phi[0]),2);
	Float_t deltaR2_2 = pow(jet_corr_eta[ijet] - llnunu_l1_l2_eta[0],2) + pow(TVector2::Phi_mpi_pi(jet_corr_phi[ijet] - llnunu_l1_l2_phi[0]),2);
	if (deltaR2_1 < 0.4 || deltaR2_2 < 0.4) isOverlapJet[ijet] = true;
	else isOverlapJet[ijet] = false;
      }
    }



    
    if (ientry%100==0)    std::cout<<"Event "<< ientry <<std::endl;

    tree_out->Fill();
    if( ientry==200) break;
  }

  // Terminate ---->
  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



