#ifndef QUADOBJFACTORY_H
#define QUADOBJFACTORY_H


#include <vector>
#include <sstream>
#include <string>
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicTree.h"
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/KinematicFit/interface/KinematicParticleVertexFitter.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "MagneticField/Engine/interface/MagneticField.h"
#include "RecoVertex/KinematicFitPrimitives/interface/KinematicParticleFactoryFromTransientTrack.h"
#include "RecoVertex/KinematicFitPrimitives/interface/ParticleMass.h"
#include "RecoVertex/KinematicFitPrimitives/interface/RefCountedKinematicParticle.h"
//
// ** apply 4-mu common vertex combination **
// 
//

using namespace std;
using namespace reco;
class QuadObjFactory
{
  
public:
  QuadObjFactory() { /* empty constructor only for ROOT dictionaries */ }
  QuadObjFactory(string iName);
  //QuadObjFactory(string iNameZDat1, string iPrefix, int iSeed=0xDEADBEEF);
  ~QuadObjFactory();
  //void addMCFile  (std::string iNameMC);
  //RefCountedKinematicTree fourMuon_vertex();
  RefCountedKinematicTree fourMuon_vertex(const reco::Track & muTk1, const reco::Track & muTk2, const reco::Track & muTk3, const reco::Track & muTk4, const MagneticField* field);
protected:

};



#endif
