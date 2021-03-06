#ifndef QUADOBJFACTORY_H
#define QUADOBJFACTORY_H


#include <vector>
#include <sstream>
#include <string>
#include <utility> // for std::pair

#include "TMath.h"

#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicTree.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
#include "DataFormats/TrackReco/interface/Track.h"
//#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFitPrimitives/interface/ParticleMass.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "MagneticField/ParametrizedEngine/src/OAEParametrizedMagneticField.h"
//
// ** apply 4-mu common vertex combination **
// 
/*
Based on algorithms on (associated to BPH-14-006)
https://twiki.cern.ch/twiki/bin/view/CMS/FourMuPassTwo
 */
//  Code based on RootTools/interface/RecoilCorrector.h
//  Author:  Mengqing Wu                                                                                                                       
// Created:  Mon, 17 Oct 2016
//  

using namespace std;
using namespace reco;
using namespace edm;

class QuadObjFactory
{

 public:
  //QuadObjFactory() { /* empty constructor only for ROOT dictionaries */ }
  QuadObjFactory();
  //QuadObjFactory(string iNameZDat1, string iPrefix, int iSeed=0xDEADBEEF);
  ~QuadObjFactory();
  //void addMCFile  (std::string iNameMC);
  //RefCountedKinematicTree fourMuon_vertex();
  void set4muVtx(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4);
  
  float get4muVtxProb();
  float get4muVtxChi2();

  void set2muVtx(const reco::Muon & mu1, const reco::Muon & mu2);

  float get2muVtxProb();
  float get2muVtxChi2();
  float get2muMass();
  float get2muMassErr2();

 private:
  //bool isbad4Mu;
  OAEParametrizedMagneticField *paramField;
  RefCountedKinematicTree _4muFitTree;
  RefCountedKinematicTree _2muFitTree;
  std::pair <float,float> _diMu_mass_err2;
  
 protected:
  RefCountedKinematicTree fourMuon_vertex(const reco::Track & muTrk1, const reco::Track & muTrk2, const reco::Track & muTrk3, const reco::Track & muTrk4);
  RefCountedKinematicTree diMuon_vertex(const reco::Track & muTrk1,  const reco::Track &  muTrk2, std::pair <float, float> & diMu_mass_err2);
 
};



#endif
