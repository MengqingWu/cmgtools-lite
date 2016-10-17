#include "CMGTools/BPH4L/interface/QuadObjFactory.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicTree.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFitPrimitives/interface/ParticleMass.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"

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
RefCountedKinematicTree QuadObjFactory::fourMuon_vertex(const reco::Track & muTk1, const reco::Track & muTk2, const reco::Track & muTk3, const reco::Track & muTk4, const MagneticField* field) {
  std::cout<<"I want a try"<<std::endl;
  // Get The four-muon information
  TransientTrack muon1TT(muTk1, field);
  TransientTrack muon2TT(muTk2, field);
  TransientTrack muon3TT(muTk3, field);
  TransientTrack muon4TT(muTk4, field);

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

//-----------------------------------------------------------------------------------------------------------------------------------------

//-----------------------------------------------------------------------------------------------------------------------------------------
