//--------------------------------
// no new branches added
// fast and simple to copy a tree with cuts parsed
// @ June 13th, Mengqing
//--------------------------------

#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
//#include "TCanvas.h"
#include "TH2D.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <string>
#include <vector>

class GetElMuTriggerEff {
  TFile *dbfile;
  TH2D *el_dt;
  TH2D *mu_dt;
  TH2D *el_mc;
  TH2D *mu_mc;
public:
  GetElMuTriggerEff(TString fname="l1l2.root");
  virtual ~GetElMuTriggerEff();
  virtual  Double_t get_eff(Float_t pt, Float_t eta, TH2D *h2);
  virtual  Float_t get_value(Float_t el_pt, Float_t el_eta, Float_t mu_pt, Float_t mu_eta);
};

GetElMuTriggerEff::GetElMuTriggerEff (TString fname) {
  dbfile = new TFile(fname);
  TH1::AddDirectory(kFALSE); 
  el_dt = (TH2D*)dbfile->Get("ell1ptetadata");
  mu_dt = (TH2D*)dbfile->Get("mul1ptetadata");
  el_mc = (TH2D*)dbfile->Get("ell1ptetamc");
  mu_mc = (TH2D*)dbfile->Get("mul1ptetamc");
  dbfile->Close();
  // TCanvas c1(1); //just for test
  // el_dt->Draw("colz");
  // c1.Print("test.pdf(");
  // el_mc->Draw("colz");
  // c1.Print("test.pdf");
  // mu_dt->Draw("colz");
  // c1.Print("test.pdf");
  // mu_mc->Draw("colz");
  // c1.Print("test.pdf)");

  return;
}
GetElMuTriggerEff::~GetElMuTriggerEff()
{
  if (!dbfile) return;
  delete dbfile; delete el_dt; delete mu_dt; delete el_mc; delete mu_mc;
}

Double_t GetElMuTriggerEff::get_eff(Float_t pt, Float_t eta, TH2D *h2){
  Int_t binx = h2->GetXaxis()->FindBin(pt);
  Int_t biny = h2->GetYaxis()->FindBin(eta);
  Double_t eff = h2->GetBinContent(binx,biny); 
  return eff;
}

Float_t GetElMuTriggerEff::get_value(Float_t el_pt, Float_t el_eta, Float_t mu_pt, Float_t mu_eta){
  if (el_eta*mu_eta<0 ) el_eta=fabs(el_eta); mu_eta=fabs(mu_eta);
  Double_t A=get_eff(el_pt,el_eta,el_dt),
    a=get_eff(el_pt,el_eta,el_mc),
    B=get_eff(mu_pt,mu_eta,mu_dt),
    b=get_eff(mu_pt,mu_eta,mu_mc);

  Float_t elmu_eff= ((A+B-A*B)==0) ? 1.0: (a+b-a*b)/(A+B-A*B); 
  if (elmu_eff==1.0) std::cout<<"[Warning] This event elmu_eff==1.0, please check: (A+B-A*B) = "<< (A+B-A*B) <<std::endl;
  
  return elmu_eff;
}

//******************************
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
  // tree_in->SetBranchStatus("Flag_*",0);
  // tree_in->SetBranchStatus("*nunu_l1_l*_c*",0);
  // tree_in->SetBranchStatus("*nunu_l1_l*_d*",0);
  // tree_in->SetBranchStatus("*nunu_l1_l*_*rack*",0);
  // tree_in->SetBranchStatus("*nunu_l2_raw*",0);
  // tree_in->SetBranchStatus("*nunu_l2_gen*",0);
  // out_tree
  TTree* tree_tmp = tree_in->CopyTree(Cuts.c_str());
  std::cout<< tree_tmp->GetEntriesFast() <<" events to process."<< std::endl;
  TTree* tree_out = tree_tmp->CloneTree(0); // clone a structure but no entry filled

  // read branches
  Float_t  elmununu_l1_l1_pt[1], elmununu_l1_l2_pt[1],
    elmununu_l1_l1_eta[1], elmununu_l1_l2_eta[1];
  Int_t nelmununu;
  //ULong64_t evt;
  tree_tmp->SetBranchAddress("elmununu_l1_l1_pt", elmununu_l1_l1_pt); // l1 is electron
  tree_tmp->SetBranchAddress("elmununu_l1_l2_pt", elmununu_l1_l2_pt);
  tree_tmp->SetBranchAddress("elmununu_l1_l1_eta", elmununu_l1_l1_eta); // l2 is muon
  tree_tmp->SetBranchAddress("elmununu_l1_l2_eta", elmununu_l1_l2_eta);
  tree_tmp->SetBranchAddress("nelmununu", &nelmununu); 
  //tree_tmp->SetBranchAddress("evt", &evt); 
  // new added branches
  Float_t triggersf_elmu;
  TBranch *b_triggersf_elmu = tree_out->Branch("triggersf_elmu",&triggersf_elmu,"triggersf_elmu/F");

  // Initialize the tool to get eff:
  GetElMuTriggerEff *effdb = new GetElMuTriggerEff();
  std::cout<<effdb->get_value(100,1.2,200,2.0) <<std::endl;
  // Loop to fill ---->
  for (int i=0; i<(int)tree_tmp->GetEntries(); i++){ 
    tree_tmp->GetEntry(i);

    // std::cout<<"debug: evt = "<<evt<< ", nelmununu = "<<nelmununu
    // 	     <<"\n        el(pt, eta) = "<< elmununu_l1_l1_pt[0]<<", "<< elmununu_l1_l1_eta[0]
    // 	     <<"\n        mu(pt, eta) = "<< elmununu_l1_l2_pt[0]<<", "<< elmununu_l1_l2_eta[0]<<std::endl;

    if (nelmununu>0){
      triggersf_elmu = effdb->get_value(elmununu_l1_l1_pt[0], fabs(elmununu_l1_l1_eta[0]),
					elmununu_l1_l2_pt[0], fabs(elmununu_l1_l2_eta[0]));
    }
    else triggersf_elmu = 1.0;
    
    tree_out->Fill();
    if (i%100==0) std::cout<<"Event "<<i<<std::endl;
    if( i==200) break;
  }

  // Terminate ---->
  foutput->cd();
  tree_out->Write();
  foutput->Close();
  finput->Close();

  return 0;

}

