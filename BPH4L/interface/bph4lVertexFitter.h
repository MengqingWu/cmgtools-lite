#ifndef BPH4LVERTEXFITTER_H
#define BPH4LVERTEXFITTER_H

//
// ** apply 4-mu common vertex combination **
// 
/*
Based on algorithms on (associated to BPH-14-006)
https://twiki.cern.ch/twiki/bin/view/CMS/FourMuPassTwo
 */
//  Code based on cmssw/HeavyFlavorAnalysis/Onia2MuMu/interface/Onia2MuMuPAT.h
// vertex fit based on KalmanVertexFit
//  Author:  Mengqing Wu                                                                                                                       
// Created:  Fri, 10 Feb 2017
//

#include <vector>
#include <sstream>
#include <string>
#include <utility> // for std::pair

#include "TMath.h"
#include "TVector3.h"

//Headers for services and tools
#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "RecoVertex/KalmanVertexFit/interface/KalmanVertexFitter.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/MuonReco/interface/Muon.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "RecoVertex/VertexTools/interface/VertexDistanceXY.h"

#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
//#include "FWCore/Framework/interface/ESHandle.h"
#include "MagneticField/ParametrizedEngine/src/OAEParametrizedMagneticField.h"


using namespace std;
using namespace reco;
using namespace edm;

class bph4lVertexFitter
{

 public:
  bph4lVertexFitter() { /* empty constructor only for ROOT dictionaries */ }
  //bph4lVertexFitter();
  //bph4lVertexFitter(string iNameZDat1, string iPrefix, int iSeed=0xDEADBEEF);
  ~bph4lVertexFitter() {};
  //void addMCFile  (std::string iNameMC);
  //RefCountedKinematicTree fourMuon_vertex();

  static std::vector<reco::TransientTrack> addMuons(const reco::Muon & mu1, const reco::Muon & mu2);
  static std::vector<reco::TransientTrack> addMuons(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4);
 
  class KalmanVertex
  {
  public:
    KalmanVertex():
    _vChi2(-99), _vNDF(0), _vProb(-99), _ctau(-99), _cosAlpha(-99) {/* empty constructor only for ROOT dictionaries */ };
    ~KalmanVertex() {};
    KalmanVertex(const reco::Muon & mu1, const reco::Muon & mu2);
    KalmanVertex(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4);
    void Init(std::vector<reco::TransientTrack> ttks);
    
    // functions to access results:
    float Prob() const{ return _vProb; };
    float Chi2() const{ return _vChi2; };
    float NDF() const{ return _vNDF; };
    float NChi2() const{
      if (_vNDF == 0) return -99;
      else return _vChi2/_vNDF;
    };

    void ComputeCTau(const reco::Vertex &thePrimaryV);
    float ctau() { return _ctau; };
    float cosAlpha() { return _cosAlpha; };
      
  private:
    typedef Candidate::LorentzVector LorentzVector;
    
    TransientVertex myVertex;
    float _vChi2;
    float _vNDF;
    float _vProb;
    float _ctau;
    float _cosAlpha;
    float _mass;
    LorentzVector _diObj;
  };
  
 private:
  
};



#endif
