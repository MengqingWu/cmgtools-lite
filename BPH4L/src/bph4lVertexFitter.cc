#include "CMGTools/BPH4L/interface/bph4lVertexFitter.h"

/*
Based on algorithms from  cmssw/HeavyFlavorAnalysis/Onia2MuMu/src/Onia2MuMuPAT.cc
 */
//  Code based on RootTools/interface/RecoilCorrector.h
//  Author:  Mengqing Wu                                                                                                                       
// Created:  Fri, 10 Feb 2017
//  

//-----------------------------------------------------------------------------------------------------------------------------------------
// bph4lVertexFitter::bph4lVertexFitter() {  
//   // ParamField example see https://github.com/CERN-PH-CMG/cmgtools-lite/blob/80X/TTHAnalysis/src/SignedImpactParameter.cc#L39
//   //paramField = new OAEParametrizedMagneticField("3_8T");
// }

// bph4lVertexFitter::~bph4lVertexFitter() {
//   delete paramField;
// }

//-----------------------------------------------------------------------------------------------------------------------------------------

std::vector<reco::TransientTrack> bph4lVertexFitter::addMuons(const reco::Muon & mu1, const reco::Muon & mu2){
  std::vector<reco::TransientTrack> _ttks;
  _ttks.clear();

  OAEParametrizedMagneticField *paramField;
  paramField = new OAEParametrizedMagneticField("3_8T");

  // ---- only fit vertex if they have tracks ----
  if (mu1.track().isNonnull() && mu2.track().isNonnull()){

    reco::TransientTrack muon1TT(*mu1.track(), paramField);
    reco::TransientTrack muon2TT(*mu2.track(), paramField);
    
    _ttks.push_back(muon1TT);
    _ttks.push_back(muon2TT);
  }
  return _ttks;
}


std::vector<reco::TransientTrack> bph4lVertexFitter::addMuons(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4){
  std::vector<reco::TransientTrack> _ttks;
  _ttks.clear();

  OAEParametrizedMagneticField *paramField;
  paramField = new OAEParametrizedMagneticField("3_8T");

  // ---- only fit vertex if they have tracks ----
  if (mu1.track().isNonnull() && mu2.track().isNonnull() && mu3.track().isNonnull() && mu4.track().isNonnull()){
    reco::TransientTrack muon1TT(*mu1.track(), paramField);
    reco::TransientTrack muon2TT(*mu2.track(), paramField);
    reco::TransientTrack muon3TT(*mu3.track(), paramField);
    reco::TransientTrack muon4TT(*mu4.track(), paramField);
    
    _ttks.push_back(muon1TT);
    _ttks.push_back(muon2TT);
    _ttks.push_back(muon3TT);
    _ttks.push_back(muon4TT);
  }
  return _ttks;
}

bph4lVertexFitter::KalmanVertex::KalmanVertex(const reco::Muon & mu1, const reco::Muon & mu2){
  std::vector<reco::TransientTrack> ttks = bph4lVertexFitter::addMuons(mu1, mu2);
  _diObj = mu1.p4() + mu2.p4();
  Init(ttks);
}

bph4lVertexFitter::KalmanVertex::KalmanVertex(const reco::Muon & mu1, const reco::Muon & mu2, const reco::Muon & mu3, const reco::Muon & mu4){
  // FIXME: no ctau available for 4-leg vertex refit @Feb14-2017
  std::vector<reco::TransientTrack> ttks = bph4lVertexFitter::addMuons(mu1, mu2, mu3, mu4);
  Init(ttks);
}

void bph4lVertexFitter::KalmanVertex::Init(std::vector<reco::TransientTrack> ttks){
  
  _vNDF = 0;
  _vChi2 = -99;
  _vProb= -99;
  
  if (ttks.empty()){
    std::cout<<"[warning] bph4lVertexFitter::KalmanVertex => invalid tracks input!"<<std::endl;
  }
  else {
    KalmanVertexFitter vtxFitter;
    //TransientVertex myVertex  = vtxFitter.vertex(ttks);
    myVertex  = vtxFitter.vertex(ttks);
    
    if (myVertex.isValid()){
      _vChi2 = myVertex.totalChiSquared();
      _vNDF = myVertex.degreesOfFreedom();
      _vProb = TMath::Prob(_vChi2,(int)_vNDF);
      
    }
    else {
      std::cout<<"[warning] bph4lVertexFitter::KalmanVertex => invalid TransientVertex!"<<std::endl;
    }
  }

}


void bph4lVertexFitter::KalmanVertex::ComputeCTau(const reco::Vertex &thePrimaryV){
  _ctau=-99;
  _cosAlpha=-99;
  // lifetime 'ctau' using PV
  if (myVertex.isValid()) {
    TVector3 vtx;
    TVector3 pvtx;
    VertexDistanceXY vdistXY;
    
    vtx.SetXYZ(myVertex.position().x(),myVertex.position().y(),0);
    pvtx.SetXYZ(thePrimaryV.position().x(),thePrimaryV.position().y(),0);
    
    TVector3 vdiff = vtx - pvtx;
    Measurement1D distXY = vdistXY.distance(Vertex(myVertex), thePrimaryV);

    TVector3 pperp(_diObj.px(), _diObj.py(), 0);
    //double ctauPV = distXY.value()*cosAlpha * _diObj.M()/pperp.Perp();
    double ctauPV = distXY.value() * _diObj.M()/pperp.Perp();
    _ctau = ctauPV;
    
    // the angle between Lxy and Mll(Jpsi or other diObj resonance)
    _cosAlpha = vdiff.Dot(pperp)/(vdiff.Perp()*pperp.Perp());
  }
  //return _ctau;
  
}
