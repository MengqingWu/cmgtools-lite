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
  Int_t nlep, njet_corr;
  tree_tmp->SetBranchAddress("llnunu_l1_l1_phi", llnunu_l1_l1_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l2_phi", llnunu_l1_l2_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l1_eta", llnunu_l1_l1_eta);
  tree_tmp->SetBranchAddress("llnunu_l1_l2_eta", llnunu_l1_l2_eta);
  tree_tmp->SetBranchAddress("jet_corr_phi", jet_corr_phi);
  tree_tmp->SetBranchAddress("jet_corr_eta", jet_corr_eta);
  tree_tmp->SetBranchAddress("njet_corr", &njet_corr);
  tree_tmp->SetBranchAddress("lep_phi", lep_phi);
  tree_tmp->SetBranchAddress("lep_eta", lep_eta);
  tree_tmp->SetBranchAddress("nlep", &nlep);
  
  // new added branches
  Int_t nlep_corr;
  Float_t deltaR_lep[5], deltaR_jet[5];
  TBranch *b_nlep_corr = tree_out->Branch("nlep_corr",&nlep_corr,"nlep_corr/I");
  TBranch *b_deltaR_lep = tree_out->Branch("deltaR_lep",deltaR_lep,"deltaR_lep[nlep]/F");
  TBranch *b_deltaR_jet = tree_out->Branch("deltaR_jet",deltaR_jet,"deltaR_jet[nlep]/F");
  
  // Loop to fill ---->
  for (int ientry=0; ientry<(int)tree_tmp->GetEntries(); ientry++){ 
    tree_tmp->GetEntry(ientry);

    nlep_corr=99;
    //std::cout<<"debug: event "<< ientry <<std::endl;
    for (int ilep=0; ilep<nlep; ilep++){
      deltaR_lep[ilep] = deltaR_jet[ilep] = 99.0;
      //std::cout<<"debug: looping leptons, lepton "<< ilep << std::endl;
      for (int ijet=0; ijet<njet_corr; ijet++){
	//std::cout<<"debug: looping jets, jet "<< ijet <<std::endl;
	  // Compute dr as TLorentzVector::DeltaR :
	Float_t drj_tmp = sqrt(pow(jet_corr_eta[ijet] - lep_eta[ilep],2) + pow(TVector2::Phi_mpi_pi(jet_corr_phi[ijet] - lep_phi[ilep]),2));
	deltaR_jet[ilep] = std::min(drj_tmp, deltaR_jet[ilep]);
      } // Loop over all jets

      for (int jlep=0; jlep<nlep; jlep++){
	if (jlep==ilep) continue;
	else {
	  //  std::cout<<"debug: looping other leptons, lepton "<< jlep <<std::endl;
	  // std::cout<<"debug: lep_eta["<<ilep<<"] = " << lep_eta[ilep]
	  // 	   <<"; lep_eta["<<jlep<<"] "<< lep_eta[jlep]
	  // 	   <<"; lep_phi["<<ilep<<"] "<< lep_phi[ilep]
	  // 	   <<"; lep_phi["<<jlep<<"] "<< lep_phi[jlep]
	  // 	   <<std::endl;
	  
	  Float_t drl_tmp = sqrt(pow(lep_eta[jlep] - lep_eta[ilep],2) + pow(TVector2::Phi_mpi_pi(lep_phi[jlep] - lep_phi[ilep]),2));
	  deltaR_lep[ilep] = std::min(drl_tmp, deltaR_lep[ilep]);
	} 
      }// loop over all other leptons

    }
    
    if (ientry%1000==0)    std::cout<<"Event "<< ientry <<std::endl;

    tree_out->Fill();
    //if( ientry==200) break;
  }

  // Terminate ---->
  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



