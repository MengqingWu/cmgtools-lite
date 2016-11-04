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
//                                                                                                                                                          
//  Author:  Mengqing Wu                                                                                                                       
// Created:  Mon, 17 Oct 2016
//  

//-----------------------------------------------------------------------------------------------------------------------------------------
QuadObjFactory::QuadObjFactory(string iName) {

//   fRandom = new TRandom3(iSeed);

//   // get fits for Z data
//   readRecoil(fF1U1Fit,fF1U1RMSSMFit,fF1U1RMS1Fit,fF1U1RMS2Fit,fF1U2Fit,fF1U2RMSSMFit,fF1U2RMS1Fit,fF1U2RMS2Fit,iNameZDat,iPrefix);
//   if(iPrefix == "PF") readCorr  (iNameZDat,fF1U1U2Corr,fF2U1U2Corr,fF1F2U1Corr,fF1F2U2Corr,fF1F2U1U2Corr,fF1F2U2U1Corr,0);
//   if(iPrefix == "TK") readCorr  (iNameZDat,fF1U1U2Corr,fF2U1U2Corr,fF1F2U1Corr,fF1F2U2Corr,fF1F2U1U2Corr,fF1F2U2U1Corr,1);  
//   fId = 0; fJet = 0;
}

QuadObjFactory::~QuadObjFactory() {

  //delete fRandom;
  
}

//-----------------------------------------------------------------------------------------------------------------------------------------
// RefCountedKinematicTree QuadObjFactory::fourMuon_vertex(){  
// }

//-----------------------------------------------------------------------------------------------------------------------------------------

//-----------------------------------------------------------------------------------------------------------------------------------------

//float QuadObjFactory::get4muVtxProb(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4, const edm::EventSetup& eventSetup){
float QuadObjFactory::get4muVtxProb(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4){
  /*
    get chi2 test p value -> 1-p_cdf;
    discriminant used to select the 0-charged 4-mu system.
   */
  // ESHandle < MagneticField > bFieldHandle;
  // eventSetup.get < IdealMagneticFieldRecord > ().get(bFieldHandle);
  // RefCountedKinematicTree fitTree=fourMuon_vertex(*mu1.track(), *mu2.track(), *mu3.track(), *mu4.track(), &(*bFieldHandle));

  paramField = new OAEParametrizedMagneticField("3_8T");
  RefCountedKinematicTree fitTree=fourMuon_vertex(*mu1.track(), *mu2.track(), *mu3.track(), *mu4.track(), paramField);

  float vtxProb = 1.;
  if (!fitTree->isValid() || fitTree->isEmpty() ){
    std::cout<<"== bad 4-mu vertex.. skip... == "<<std::endl;
  }
  else{
    vtxProb = TMath::Prob(fitTree->currentDecayVertex()->chiSquared(),int(fitTree->currentDecayVertex()->degreesOfFreedom()));
    std::cout<< "[debug] chi2 = " << fitTree->currentDecayVertex()->chiSquared()
	     << ", dof = " << fitTree->currentDecayVertex()->degreesOfFreedom() <<std::endl;
  }
  
  return vtxProb;

}
//-----------------------------------------------------------------------------------------------------------------------------------------
RefCountedKinematicTree QuadObjFactory::fourMuon_vertex(const reco::Track & muTrk1, const reco::Track & muTrk2, const reco::Track & muTrk3, const reco::Track & muTrk4, const MagneticField* field) {
  
  // std::cout<<"I want a try"<<std::endl;
  // Get The four-muon information
  TransientTrack muon1TT(muTrk1, field);
  TransientTrack muon2TT(muTrk2, field);
  TransientTrack muon3TT(muTrk3, field);
  TransientTrack muon4TT(muTrk4, field);

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
RefCountedKinematicTree QuadObjFactory::diMuon_vertex(const reco::Track & muTrk1,  const reco::Track &  muTrk2, const MagneticField* field, std::pair <double, double> & diMu_mass_err2){
  // The mass of a muon and the insignificant mass sigma
  // to avoid singularities in the covariance matrix.
  ParticleMass muon_mass = 0.10565837;    // pdg mass
  float muon_sigma = muon_mass * 1.e-6;

  // initial chi2 and ndf before kinematic fits.
  float chi = 0.;
  float ndf = 0.;
  TransientTrack muonPTT(muTrk1, field);
  TransientTrack muonMTT(muTrk2, field);
  
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
