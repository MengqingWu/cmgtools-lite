#include "CMGTools/BPH4L/interface/QuadObjFactory.h"
// #include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicTree.h"
// #include "TrackingTools/TransientTrack/interface/TransientTrack.h"
// #include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
// #include "DataFormats/TrackReco/interface/Track.h"
// #include "MagneticField/Engine/interface/MagneticField.h"
// #include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
// #include "RecoVertex/KinematicFitPrimitives/interface/ParticleMass.h"
// #include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"
// #include "DataFormats/MuonReco/interface/Muon.h"
//#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

/*
Based on algorithms on (associated to BPH-14-006)
https://twiki.cern.ch/twiki/bin/view/CMS/FourMuPassTwo
 */
//  Code based on RootTools/interface/RecoilCorrector.h
//  Author:  Mengqing Wu                                                                                                                       
// Created:  Mon, 17 Oct 2016
//  

//-----------------------------------------------------------------------------------------------------------------------------------------
QuadObjFactory::QuadObjFactory() {
  
  // ParamField example see https://github.com/CERN-PH-CMG/cmgtools-lite/blob/80X/TTHAnalysis/src/SignedImpactParameter.cc#L39
  paramField = new OAEParametrizedMagneticField("3_8T");
  
}

QuadObjFactory::~QuadObjFactory() {
  delete paramField;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

//-----------------------------------------------------------------------------------------------------------------------------------------
void QuadObjFactory::set4muVtx(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4){
  _4muFitTree = fourMuon_vertex(*mu1.track(), *mu2.track(), *mu3.track(), *mu4.track());
}

//-----------------------------------------------------------------------------------------------------------------------------------------

//float QuadObjFactory::get4muVtxProb(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4, const edm::EventSetup& eventSetup){
float QuadObjFactory::get4muVtxProb(){
  /*
    get chi2 test p value -> 1-p_cdf;
    discriminant used to select the 0-charged 4-mu system.
   */
  // ESHandle < MagneticField > bFieldHandle;
  // eventSetup.get < IdealMagneticFieldRecord > ().get(bFieldHandle);
  // RefCountedKinematicTree fitTree=fourMuon_vertex(*mu1.track(), *mu2.track(), *mu3.track(), *mu4.track(), &(*bFieldHandle));


  float vtxProb = -99.;
  if (!_4muFitTree->isValid() || _4muFitTree->isEmpty() ){
    std::cout<<"== bad 4-mu vertex.. skip... == "<<std::endl;
  }
  else{
    vtxProb = TMath::Prob(_4muFitTree->currentDecayVertex()->chiSquared(),int(_4muFitTree->currentDecayVertex()->degreesOfFreedom()));
    std::cout<< "[debug] 4-mu p-value = " << vtxProb
	     << ", chi2 = " << _4muFitTree->currentDecayVertex()->chiSquared()
	     << ", dof = " << _4muFitTree->currentDecayVertex()->degreesOfFreedom() <<std::endl;
  }

  return vtxProb;
}

float QuadObjFactory::get4muVtxChi2() {
  float vtxChi2 = -99.;
   if (!_4muFitTree->isValid() || _4muFitTree->isEmpty() ){
    std::cout<<"== bad 4-mu vertex.. skip... == "<<std::endl;
  }
  else{
    vtxChi2 = _4muFitTree->currentDecayVertex()->chiSquared();
  }
   
  return vtxChi2;
}

//-----------------------------------------------------------------------------------------------------------------------------------------
RefCountedKinematicTree QuadObjFactory::fourMuon_vertex(const reco::Track & muTrk1, const reco::Track & muTrk2, const reco::Track & muTrk3, const reco::Track & muTrk4) {
  
  // std::cout<<"I want a try"<<std::endl;
  // Get The four-muon information
  TransientTrack muon1TT(muTrk1, paramField);
  TransientTrack muon2TT(muTrk2, paramField);
  TransientTrack muon3TT(muTrk3, paramField);
  TransientTrack muon4TT(muTrk4, paramField);

  KinematicParticleFactoryFromTransientTrack  pFactory;

  // The mass of a muon and the insignificant mass sigma
  // to avoid singularities in the covariance matrix.
  ParticleMass muon_mass = 0.10565837;    // pdg mass
  float muon_sigma = muon_mass * 1.e-6;

  // initial chi2 and ndf before kinematic fits.
  float chi = 0.;
  float ndf = 0.;
  vector < RefCountedKinematicParticle > muonParticles;
  muonParticles.push_back(pFactory.particle(muon1TT, muon_mass, chi, ndf, muon_sigma));
  muonParticles.push_back(pFactory.particle(muon2TT, muon_mass, chi, ndf, muon_sigma));
  muonParticles.push_back(pFactory.particle(muon3TT, muon_mass, chi, ndf, muon_sigma));
  muonParticles.push_back(pFactory.particle(muon4TT, muon_mass, chi, ndf, muon_sigma));

  KinematicParticleVertexFitter fitter;
  RefCountedKinematicTree myFourMuonVertexFitTree;
  myFourMuonVertexFitTree = fitter.fit(muonParticles);

  return myFourMuonVertexFitTree;
}

//-----------------------------------------------------------------------------------------------------------------------------------------

void QuadObjFactory::set2muVtx(const reco::Muon & mu1, const reco::Muon & mu2){
  _diMu_mass_err2 = make_pair(-1,-1);
  _2muFitTree = diMuon_vertex(*mu1.track(), *mu2.track(), _diMu_mass_err2);
}

//-----------------------------------------------------------------------------------------------------------------------------------------
float QuadObjFactory::get2muVtxProb(){
  /*
    get chi2 test p value -> 1-p_cdf;
    discriminant used to select the 0-charged 2-mu system.
   */

  float _2vtxProb = -99.;
  if (!_2muFitTree->isValid() || _2muFitTree->isEmpty() ){
    std::cout<<"== bad 2-mu vertex.. skip... == "<<std::endl;
  }
  else{
    _2vtxProb = TMath::Prob(_2muFitTree->currentDecayVertex()->chiSquared(),int(_2muFitTree->currentDecayVertex()->degreesOfFreedom()));
    std::cout<< "[debug] di-mu p-value = " << _2vtxProb
	     << ", chi2 = " << _2muFitTree->currentDecayVertex()->chiSquared()
	     << ", dof = " << _2muFitTree->currentDecayVertex()->degreesOfFreedom() <<std::endl;
  }

  return _2vtxProb;
}

float QuadObjFactory::get2muVtxChi2() {
  float _2vtxChi2 = -99.;
   if (!_2muFitTree->isValid() || _2muFitTree->isEmpty() ){
    std::cout<<"== bad 2-mu vertex.. skip... == "<<std::endl;
  }
  else{
    _2vtxChi2 = _2muFitTree->currentDecayVertex()->chiSquared();
  }
   
  return _2vtxChi2;
}

float QuadObjFactory::get2muMass() {return _diMu_mass_err2.first; }
float QuadObjFactory::get2muMassErr2() {return _diMu_mass_err2.second; }
//-----------------------------------------------------------------------------------------------------------------------------------------
RefCountedKinematicTree QuadObjFactory::diMuon_vertex(const reco::Track & muTrk1,  const reco::Track &  muTrk2, std::pair <float, float> & diMu_mass_err2){
  // The mass of a muon and the insignificant mass sigma
  // to avoid singularities in the covariance matrix.
  ParticleMass muon_mass = 0.10565837;    // pdg mass
  float muon_sigma = muon_mass * 1.e-6;

  // initial chi2 and ndf before kinematic fits.
  float chi = 0.;
  float ndf = 0.;
  TransientTrack muonPTT(muTrk1, paramField);
  TransientTrack muonMTT(muTrk2, paramField);
  
  KinematicParticleFactoryFromTransientTrack pmumuFactory;
  vector < RefCountedKinematicParticle > muonParticles;
  muonParticles.push_back(pmumuFactory.particle(muonPTT, muon_mass, chi, ndf, muon_sigma));
  muonParticles.push_back(pmumuFactory.particle(muonMTT, muon_mass, chi, ndf, muon_sigma));

  KinematicParticleVertexFitter fitter;
  RefCountedKinematicTree diMuVertexFitTree;
  diMuVertexFitTree = fitter.fit(muonParticles);

  if (diMuVertexFitTree->isValid()) {
    diMuVertexFitTree->movePointerToTheTop();
    RefCountedKinematicParticle diMu_vFit_noMC = diMuVertexFitTree->currentParticle();
    diMu_mass_err2 = make_pair(diMu_vFit_noMC->currentState().mass(), diMu_vFit_noMC->currentState().kinematicParametersError().matrix()(6,6));
  }
  return diMuVertexFitTree;
}
//-----------------------------------------------------------------------------------------------------------------------------------------

//-----------------------------------------------------------------------------------------------------------------------------------------
