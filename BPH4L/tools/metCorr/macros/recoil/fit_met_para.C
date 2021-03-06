

std::string channel = "all";
bool doMC = true;
bool useMzCut = false;
bool useZSelec = false;
bool useZSelecLowLPt = true;
bool useEffSf = true;
bool mcTrgSf = false;
bool dtTrgSf = false;
bool dtHLT = false;

// recipe:
// 1.) useZSelecLowLPt can well reproduce the results with full cuts (useZSelec) + HLT (dtHLT or dtTrgSf or mcTrgSf) 
// 2.) for Data:  useZSelecLowLPt
// 3.) for MC : useZSelecLowLPt + useEffSf


std::string inputdir = 
  "/home/heli/XZZ/80X_20160825_light_Skim"
  //"./"
  ;
std::string filename =
  //"DYJetsToLL_M50_RecoilNoSmooth"
  //"DYJetsToLL_M50_RecoilSmooth"
  "DYJetsToLL_M50"
  //"DYJetsToLL_M50_NoRecoil"
  //"DYJetsToLL_M50_MGMLM_Ext1_NoRecoil"
  //"DYJetsToLL_M50_MGMLM_Ext1_RecoilSmooth"
  //"DYJetsToLL_M50_MGMLM_Ext1_RecoilNoSmooth"
  //"DYJetsToLL_M50_MGMLM_Ext1"
  //"SingleEMU_Run2016BCD_PromptReco"
  ;

std::string outputdir = "./recoil_out2";

char name[1000];
TCanvas* plots;
std::string tag;
std::string base_selec;
std::string lumiTag;

std::vector<Double_t> fit_min; 
std::vector<Double_t> fit_max; 
std::vector<Int_t> fit_rebin; 


int fit_slice_gaus(TH2D* h2d, TH1D** h1d, std::string& plotfile);
void do_fit_met_para(std::string& infilename, std::string& chan);

std::string base_sele;

TFile* fin;
TFile* fout;

std::string histname;
TPaveText* lumipt;
TH2D* h2d1;
TH2D* h2d2;
TH2D* h2d3;
TH2D* h2d4;
TH1D* h1d1[1000];
TH1D* h1d2[1000];
TH1D* h1d3[1000];
TH1D* h1d4[1000];
TF1* func1[1000];
TF1* func2[1000];
TF1* func3[1000];
TF1* func4[1000];

Int_t Nbins;

void fit_met_para(){

 std::vector< std::string > channels = {"all", "mu", "el"};
 std::vector< std::string > mcfiles;
 std::vector< std::string > dtfiles;

 mcfiles = {
    //"DYJetsToLL_M50", "DYJetsToLL_M50_MGMLM_Ext1"
    //"DYJetsToLL_M50_NoRecoil", "DYJetsToLL_M50_MGMLM_Ext1_NoRecoil"
    //"DYJetsToLL_M50_RecoilSmooth", "DYJetsToLL_M50_MGMLM_Ext1_RecoilSmooth"
    "DYJetsToLL_M50_RecoilNoSmooth", "DYJetsToLL_M50_MGMLM_Ext1_RecoilNoSmooth"
 };
 
 dtfiles = {
    "SingleEMU_Run2016BCD_PromptReco"
 };

 if (doMC) 
 {
   for (int i=0; i<(int)mcfiles.size(); i++)
   {   
     for (int j=0; j<(int)channels.size(); j++){
       do_fit_met_para(mcfiles.at(i), channels.at(j));
     }
   }
 }
 else 
 {
   for (int i=0; i<(int)dtfiles.size(); i++)
   {
     for (int j=0; j<(int)channels.size(); j++){
       do_fit_met_para(dtfiles.at(i), channels.at(j));
     }
   }
 }
}

void do_fit_met_para(std::string& infilename, std::string& chan) {

  filename = infilename;
  channel = chan;

  // tags
  tag = "_met_para_study";
  if (useMzCut) tag += "_MzCut";
  if (useZSelec) tag += "_ZSelec"; 
  if (useZSelecLowLPt) tag += "_ZSelecLowLPt";
  if (doMC && useEffSf) tag += "_effSf";
  if ( (doMC && mcTrgSf) || (!doMC && dtTrgSf))  tag += "_trgSf";
  if (!doMC && dtHLT) tag += "_dtHLT";
  if (channel=="el") tag += "_el";
  else if (channel=="mu") tag += "_mu";


  // define cuts
  std::string metfilter="(Flag_EcalDeadCellTriggerPrimitiveFilter&&Flag_HBHENoiseIsoFilter&&Flag_goodVertices&&Flag_HBHENoiseFilter&&Flag_CSCTightHalo2015Filter&&Flag_eeBadScFilter)";
  std::string cuts_lepaccept="((abs(llnunu_l1_l1_pdgId)==13&&abs(llnunu_l1_l2_pdgId)==13&&llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.4&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4&&(llnunu_l1_l1_highPtID==1||llnunu_l1_l2_highPtID==1))";
  cuts_lepaccept+="||(abs(llnunu_l1_l1_pdgId)==11&&abs(llnunu_l1_l2_pdgId)==11&&llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))";
  std::string cuts_lepaccept_lowlpt="((abs(llnunu_l1_l1_pdgId)==13&&abs(llnunu_l1_l2_pdgId)==13&&llnunu_l1_l1_pt>20&&abs(llnunu_l1_l1_eta)<2.4&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4&&(llnunu_l1_l1_highPtID==1||llnunu_l1_l2_highPtID==1))";
  cuts_lepaccept_lowlpt+="||(abs(llnunu_l1_l1_pdgId)==11&&abs(llnunu_l1_l2_pdgId)==11&&llnunu_l1_l1_pt>20&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.5))";
  std::string cuts_zmass="(llnunu_l1_mass>70&&llnunu_l1_mass<110)";
  std::string cuts_loose_z="("+metfilter+"&&"+cuts_lepaccept+"&&"+cuts_zmass+")";
  std::string cuts_loose_z_lowlpt="("+metfilter+"&&"+cuts_lepaccept_lowlpt+"&&"+cuts_zmass+")";

  base_selec = "(llnunu_l1_mass>50&&llnunu_l1_mass<180)";
  if (useMzCut)  base_selec = "(llnunu_l1_mass>70&&llnunu_l1_mass<110)";

  if (useZSelec) base_selec =  cuts_loose_z;
  if (useZSelecLowLPt) base_selec =  cuts_loose_z_lowlpt;

  if (channel=="el") base_selec = "("+base_selec+"&&(abs(llnunu_l1_l1_pdgId)==11&&abs(llnunu_l1_l2_pdgId)==11))";
  else if (channel=="mu") base_selec = "("+base_selec+"&&(abs(llnunu_l1_l1_pdgId)==13&&abs(llnunu_l1_l2_pdgId)==13))";

  if (!doMC && dtHLT) base_selec = "((HLT_MUv2||HLT_ELEv2)&&"+base_selec+")";


  // add weight
  std::string weight_selec = std::string("*(genWeight*ZPtWeight*puWeight68075/SumWeights*1921.8*3*12900.0)");
  // rho weight
  std::string rhoweight_selec = std::string("*(0.602*exp(-0.5*pow((rho-8.890)/6.187,2))+0.829*exp(-0.5*pow((rho-21.404)/10.866,2)))");
  // scale factors
  std::string effsf_selec = std::string("*(isosf*idsf*trksf)");

  // selec, cuts + weights
  std::string selec = base_selec;
  if (doMC) selec +=  weight_selec + rhoweight_selec;
  if (doMC && useEffSf) selec += effsf_selec;
  if ( (doMC && mcTrgSf) || (!doMC && dtTrgSf) ) selec += "*(trgsf)";
  

  // style
  gROOT->ProcessLine(".x tdrstyle.C");
  gStyle->SetOptTitle(0);

  sprintf(name, ".! mkdir -p %s", outputdir.c_str());
  gROOT->ProcessLine(name);

  // lumiTag for plotting
  lumiTag = "CMS 13 TeV 2016 L=12.9 fb^{-1}";
  if (doMC) lumiTag = "CMS 13 TeV Simulation for 2016 Data";

  lumipt = new TPaveText(0.2,0.9,0.8,0.98,"brNDC");
  lumipt->SetBorderSize(0);
  lumipt->SetTextAlign(12);
  lumipt->SetFillStyle(0);
  lumipt->SetTextFont(42);
  lumipt->SetTextSize(0.03);
  lumipt->AddText(0.15,0.3, lumiTag.c_str());

  sprintf(name, "%s/%s.root", inputdir.c_str(), filename.c_str());
  fin = new TFile(name);


  sprintf(name, "%s/%s%s.root", outputdir.c_str(), filename.c_str(), tag.c_str());
  fout = new TFile(name, "recreate");

  TTree* tree = (TTree*)fin->Get("tree");

  plots = new TCanvas("plots", "plots");

  sprintf(name, "%s/%s%s.pdf[", outputdir.c_str(),filename.c_str(), tag.c_str());
  plots->Print(name);


  // other control plots
  Double_t ZPtBins[] = {0,2,4,6,8,10,12,14,16,18,20,22,24,26,28, 30, 35, 40, 50, 60, 80, 100, 150, 250, 5000 };
  Int_t NZPtBins = sizeof(ZPtBins)/sizeof(ZPtBins[0]) - 1;
  const Int_t NMetParaBins=500;
  Double_t MetParaBins[NMetParaBins+1];
  for (int i=0; i<=NMetParaBins; i++) { MetParaBins[i] = -100.0+200.0/NMetParaBins*i; };
  const Int_t NMetPerpBins=500;
  Double_t MetPerpBins[NMetPerpBins+1];
  for (int i=0; i<=NMetPerpBins; i++) { MetPerpBins[i] = -100.0+200.0/NMetPerpBins*i; };

  h2d1 = new TH2D("h_met_para_vs_zpt", "h_met_para_vs_zpt", NZPtBins, ZPtBins, NMetParaBins, MetParaBins);
  h2d2 = new TH2D("h_met_perp_vs_zpt", "h_met_perp_vs_zpt", NZPtBins, ZPtBins, NMetPerpBins, MetPerpBins);
  h2d1->Sumw2();
  h2d2->Sumw2();
  tree->Draw("llnunu_l2_pt*cos(llnunu_l2_phi-llnunu_l1_phi):llnunu_l1_pt>>h_met_para_vs_zpt", selec.c_str(), "colz");
  tree->Draw("llnunu_l2_pt*sin(llnunu_l2_phi-llnunu_l1_phi):llnunu_l1_pt>>h_met_perp_vs_zpt", selec.c_str(), "colz");
  
  h2d1->GetXaxis()->SetTitle("P_{T}(Z) (GeV)");
  h2d1->GetYaxis()->SetTitle("MET para (GeV)");
  h2d2->GetXaxis()->SetTitle("P_{T}(Z) (GeV)");
  h2d2->GetYaxis()->SetTitle("MET para (GeV)");

  Nbins = NZPtBins;
  fit_min = { -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -25  };
  fit_max = { +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20  };
  fit_rebin = {  4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4  };
  for (int ii=0; ii<Nbins; ii++) fit_rebin[ii] = 5;
  for (int ii=0; ii<Nbins; ii++) fit_min[ii] = -16;
  for (int ii=0; ii<Nbins; ii++) fit_max[ii] = 16;

  fit_min = { -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -20, -30, -30, -30, -30  };
  fit_max = { +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +20, +30, +30, +30, +30  };

  sprintf(name, "%s/%s%s.pdf", outputdir.c_str(), filename.c_str(), tag.c_str());
  std::string plotfilename(name);
  fit_slice_gaus(h2d1, h1d1, plotfilename);
  fit_slice_gaus(h2d2, h1d2, plotfilename);



  sprintf(name, "%s/%s%s.pdf]", outputdir.c_str(), filename.c_str(), tag.c_str());
  plots->Print(name);


  fout->Close();
}

int fit_slice_gaus(TH2D* h2d, TH1D** h1d, std::string& plotfile){ 

  std::string hname = h2d->GetName();
  Double_t* xbins = (Double_t*)h2d->GetXaxis()->GetXbins()->GetArray();

  plots->cd();
  plots->Clear();
  plots->SetLogx(1);
  h2d->Draw("colz");
  lumipt->Draw();
  plots->Print(plotfile.c_str());
  plots->SetLogx(0);
  plots->Clear();
  
  fout->cd();
  h2d->Write();

  sprintf(name, "%s_mean", hname.c_str());
  TH1D* h_mean = new TH1D(name, name, Nbins, xbins);
  h_mean->Sumw2();
  h_mean->GetXaxis()->SetTitle("P_{T}(Z) (GeV)");
  h_mean->GetYaxis()->SetTitle("mean (GeV)");
  h_mean->SetLineColor(2);
  h_mean->SetMarkerColor(2);
  h_mean->SetMarkerStyle(20);
  sprintf(name, "%s_sigma", hname.c_str());
  TH1D* h_sigma = new TH1D(name, name, Nbins, xbins);
  h_sigma->Sumw2();
  h_sigma->GetXaxis()->SetTitle("P_{T}(Z) (GeV)");
  h_sigma->GetYaxis()->SetTitle("sigma (GeV)");
  h_sigma->SetLineColor(4);
  h_sigma->SetMarkerColor(4);
  h_sigma->SetMarkerStyle(20);

  for (int i=0; i<Nbins; i++){
    sprintf(name, "%s_bin%d_func", hname.c_str(), i+1);
    TF1* afunc = new TF1(name, "gaus", -100,+100);
    sprintf(name, "%s_bin%d", hname.c_str(), i+1);
    TH1D* ahist = (TH1D*)h2d->ProjectionY(name, i+1, i+1, "e");
    ahist->SetTitle(name);
    ahist->Rebin(fit_rebin[i]);
    ahist->Fit(afunc, "R", "", fit_min[i], fit_max[i]);
    double mean = afunc->GetParameter(1);
    double sigma = afunc->GetParameter(2);
    ahist->Fit(afunc, "R", "", mean-1.5*sigma, mean+1.5*sigma); 
    func1[i] = afunc;
    h1d1[i] = ahist;

    h_mean->SetBinContent(i+1, afunc->GetParameter(1));
    h_mean->SetBinError(i+1, afunc->GetParError(1));
    h_sigma->SetBinContent(i+1, afunc->GetParameter(2));
    h_sigma->SetBinError(i+1, afunc->GetParError(2));
    

    plots->cd();
    plots->Clear();
    ahist->Draw();
    lumipt->Draw();
    plots->Print(plotfile.c_str());    
    plots->Clear();    
   
    fout->cd();
    ahist->Write();
    afunc->Write();
  }


  plots->cd();
  plots->Clear();
  plots->SetLogx(1);
  h_mean->Draw();
  lumipt->Draw();
  plots->Print(plotfile.c_str());
  plots->SetLogx(0);
  plots->Clear();

  plots->cd();
  plots->Clear();
  plots->SetLogx(1);
  h_sigma->Draw();
  lumipt->Draw();
  plots->Print(plotfile.c_str());
  plots->SetLogx(0);
  plots->Clear();

  fout->cd();
  h_mean->Write();
  h_sigma->Write();


  return 0;

}
