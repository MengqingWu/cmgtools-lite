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
#include "MagneticField/Engine/interface/MagneticField.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFitPrimitives/interface/ParticleMass.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"
#include "DataFormats/MuonReco/interface/Muon.h"
//
// ** apply 4-mu common vertex combination **
// 
/*
Based on algorithms on (associated to BPH-14-006)
https://twiki.cern.ch/twiki/bin/view/CMS/FourMuPassTwo
 */
//                                                                                                                                                          
//  Author:  Mengqing Wu                                                                                                                       
// Created:  Mon, 17 Oct 2016
//  

using namespace std;
using namespace reco;

class QuadObjFactory
{
  bool isbad4Mu;
  
public:
  QuadObjFactory() { /* empty constructor only for ROOT dictionaries */ }
  QuadObjFactory(string iName);
  //QuadObjFactory(string iNameZDat1, string iPrefix, int iSeed=0xDEADBEEF);
  ~QuadObjFactory();
  //void addMCFile  (std::string iNameMC);
  //RefCountedKinematicTree fourMuon_vertex();
  RefCountedKinematicTree fourMuon_vertex(const reco::Track & muTrk1, const reco::Track & muTrk2, const reco::Track & muTrk3, const reco::Track & muTrk4, const MagneticField* field);
  RefCountedKinematicTree diMuon_vertex(const reco::Track & muTrk1,  const reco::Track &  muTrk2, const MagneticField* field, std::pair <double, double> & diMu_mass_err2);
  
protected:
  float get4muVtxProb(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4, const MagneticField* field);
};



#endif
