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

  if( argc<6 ) {
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


  // nevts 
  double SumEvents = atof(argv[3]);  
  // sum weights 
  double SumWeights = atof(argv[4]);  
  // cuts
  std::string Cuts((const char*)argv[5]);

  // initialize
  // root files
  TFile* finput = new TFile(inputfile.c_str());
  TFile* foutput = new TFile(outputfile.c_str(), "recreate");

  // tree
  TTree* tree_in = (TTree*)finput->Get("tree");
  tree_in->SetBranchStatus("met_*",0);
  //tree_in->SetBranchStatus("genLep*",0);
  tree_in->SetBranchStatus("elmununu_LV_*",0);
  tree_in->SetBranchStatus("llnunu_LV_*",0);
  //tree_in->SetBranchStatus("*_p4*",0);
  std::cout<<"debug: in tree entries = "<<tree_in->GetEntriesFast()<<std::endl;
  
  // out_tree
  TTree* tree_tmp = tree_in->CopyTree(Cuts.c_str());
  TTree* tree_out = tree_tmp->CloneTree(0);
  std::cout<<"debug: out tree entries = "<<tree_tmp->GetEntriesFast()<<std::endl;
  
  TBranch *b_SumEvents=tree_out->Branch("SumEvents",&SumEvents,"SumEvents/D");
  TBranch *b_SumWeights=tree_out->Branch("SumWeights",&SumWeights,"SumWeights/D");

  // read branches
  Float_t llnunu_l2_phi[1],  jet_corr_phi[15],
          jet_corr_pt[15],   jet_corr_eta[15],
          llnunu_l1_l1_phi[1], llnunu_l1_l2_phi[1],
          llnunu_l1_l1_eta[1], llnunu_l1_l2_eta[1];
  Int_t jet_corr_id[15], njet_corr;
  tree_tmp->SetBranchAddress("llnunu_l2_phi", llnunu_l2_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l1_phi", llnunu_l1_l1_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l2_phi", llnunu_l1_l2_phi);
  tree_tmp->SetBranchAddress("llnunu_l1_l1_eta", llnunu_l1_l1_eta);
  tree_tmp->SetBranchAddress("llnunu_l1_l2_eta", llnunu_l1_l2_eta);
  tree_tmp->SetBranchAddress("jet_corr_eta", jet_corr_eta);
  tree_tmp->SetBranchAddress("jet_corr_phi", jet_corr_phi);
  tree_tmp->SetBranchAddress("jet_corr_pt", jet_corr_pt);
  tree_tmp->SetBranchAddress("jet_corr_id", jet_corr_id);
  tree_tmp->SetBranchAddress("njet_corr", &njet_corr);
  
  // new added branches
  Float_t dPhi_jetMet_min, dPhi_jetMet_min_a, dPhi_jetMet_min_b;
  TBranch *b_dPhi_jetMet_min=tree_out->Branch("dPhi_jetMet_min",&dPhi_jetMet_min,"dPhi_jetMet_min/F");
  TBranch *b_dPhi_jetMet_min_a=tree_out->Branch("dPhi_jetMet_min_a",&dPhi_jetMet_min_a,"dPhi_jetMet_min_a/F");
  TBranch *b_dPhi_jetMet_min_b=tree_out->Branch("dPhi_jetMet_min_b",&dPhi_jetMet_min_b,"dPhi_jetMet_min_b/F");
  
  for (int ii=0; ii<(int)tree_tmp->GetEntries(); ii++){

    tree_tmp->GetEntry(ii);

    dPhi_jetMet_min = dPhi_jetMet_min_a = dPhi_jetMet_min_b = 3.6;
    //std::cout<< "debug: event" << ii <<" "<< njet_corr <<std::endl;
    for (int ijet=0; ijet < njet_corr; ijet++){
      //std::cout<< "debug: "<< ijet << " " << jet_corr_eta[ijet]<< " "<< jet_corr_phi[ijet] <<std::endl; 
      if (fabs(jet_corr_eta[ijet])>10. || fabs(jet_corr_phi[ijet])>2*TMath::Pi()) continue;
      else{
	// Compute dr as TLorentzVector::DeltaR :
	Float_t deltaR2_1 = pow(jet_corr_eta[ijet] - llnunu_l1_l1_eta[0],2) + pow(TVector2::Phi_mpi_pi(jet_corr_phi[ijet] - llnunu_l1_l1_phi[0]),2);
	Float_t deltaR2_2 = pow(jet_corr_eta[ijet] - llnunu_l1_l2_eta[0],2) + pow(TVector2::Phi_mpi_pi(jet_corr_phi[ijet] - llnunu_l1_l2_phi[0]),2);

	Bool_t isOverlapJet = (deltaR2_1 < 0.4 || deltaR2_2 < 0.4);
	Bool_t isLooseJet = (jet_corr_id[ijet]>0);
	Bool_t isGoodJet = (jet_corr_pt[ijet]>20.0 && fabs(jet_corr_eta[ijet])<5.0);
	
	Float_t dphi_tmp = dphi_0_phi(jet_corr_phi[ijet],llnunu_l2_phi[0]);
	if (!isOverlapJet) dPhi_jetMet_min = std::min(dphi_tmp, dPhi_jetMet_min);
	if (!isOverlapJet && isLooseJet) dPhi_jetMet_min_a = std::min(dphi_tmp, dPhi_jetMet_min_a);
	if (!isOverlapJet && isLooseJet && isGoodJet) dPhi_jetMet_min_b = std::min(dphi_tmp, dPhi_jetMet_min_b);
	
      }// veto bad reconstructed jets
    }// loop jets
    
    tree_out->Fill();
    
    if (ii%5000==0) std::cout<<"Event "<<ii<<std::endl;
    //if (ii==200) break;
  }

  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}



