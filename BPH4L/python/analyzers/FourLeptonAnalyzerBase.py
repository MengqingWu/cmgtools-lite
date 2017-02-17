from math import *
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi, bestMatch
from PhysicsTools.HeppyCore.framework.event import *

from CMGTools.BPH4L.tools.DiObject import DiObject
from CMGTools.BPH4L.tools.DiObjectPair import DiObjectPair
from CMGTools.BPH4L.tools.OverlapCleaner import OverlapCleaner
from CMGTools.BPH4L.tools.CutFlowMaker  import CutFlowMaker

import os
import itertools
import collections
import ROOT

from ROOT import gSystem
gSystem.Load("libCMGToolsBPH4L")
from ROOT import bph4lVertexFitter

class EventBox(object):
    def __init__(self):
        pass

    def __str__(self):

        header = 'EVENT BOX ---> {type} <------ EVENT BOX'.format( type=self.__class__.__name__)
        varlines = []
        for var,value in sorted(vars(self).iteritems()):
            tmp = value
            # check for recursivity
            recursive = False
            if hasattr(value, '__getitem__'):
                if (len(value)>0 and value[0].__class__ == value.__class__):
                    recursive = True
            if isinstance( value, collections.Iterable ) and \
                   not isinstance(value, (str,unicode)) and \
                   not isinstance(value, TChain) and \
                   not recursive :
                tmp = map(str, value)
            varlines.append( '\t{var:<15}:   {value}'.format(var=var, value=tmp) )
        all = [ header ]
        all.extend(varlines)
        return '\n'.join( all )



        
class FourLeptonAnalyzerBase( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(FourLeptonAnalyzerBase,self).__init__(cfg_ana,cfg_comp,looperName)

        self.muonId = getattr(cfg_ana, "muonId", "POG_ID_Soft")
        self.electronId = getattr(cfg_ana, "electronId", "POG_MVA_ID_NonTrig")
        
        self.mode = getattr(cfg_ana, "mode", "jpsi+Y") #cfg_ana.mode
        print "[info] FourLeptonAnalyzer: running the %s mode!" % (self.mode)
        if self.mode not in [ "jpsi+Y", "jpsi+jpsi" ]: raise RuntimeError, "Unsupported mode"

        self.oniaMassMin = getattr(cfg_ana, "oniaMassMin", 2.5) # inclusive range as default
        self.oniaMassMax = getattr(cfg_ana, "oniaMassMax", 12) # inclusive range as default

        self.vtxKalman = bph4lVertexFitter.KalmanVertex
                
    def declareHandles(self):
        super(FourLeptonAnalyzerBase, self).declareHandles()

    def beginLoop(self, setup):
        super(FourLeptonAnalyzerBase,self).beginLoop(setup)

    def process(self, event):
        self.readCollections( event.input )



    def leptonID_tight(self,lepton):
        return lepton.tightId()

    def leptonID_loose(self,lepton):
        return True    

    def leptonID(self,lepton):
        if abs(lepton.pdgId())==13: return lepton.muonID(self.muonId)
        elif abs(lepton.pdgId())==11: return lepton.electronID(self.electronId)
        else: return self.leptonID_tight(lepton) # just a stale stuff from HZZ algo

    def muonIsolation(self,lepton):
        #return lepton.relIsoAfterFSR < 0.35
        # below was copied from BPH4L/python/analyzers/objects/BPH4lLeptonAnalyzer.py @Feb-2017
        return lepton.trackerIso < 0.2

    def electronIsolation(self,lepton): 
        #return lepton.relIsoAfterFSR < 0.35
        # below was copied from BPH4L/python/analyzers/objects/BPH4lLeptonAnalyzer.py @Feb-2017
        if abs(lepton.physObj.superCluster().eta())<1.479:
            lepton.looseiso=True if lepton.relIsoea03<0.0893 else False
        else:
            lepton.looseiso=True if lepton.relIsoea03<0.121 else False
        return lepton.looseiso

    def oniaMassFilter(self,twoLepton):
        return twoLepton.mll() > self.oniaMassMin and twoLepton.mll() < self.oniaMassMax

    def fourLeptonMassOnia(self, fourLepton):
        return self.oniaMassFilter(fourLepton.leg1) and self.oniaMassFilter(fourLepton.leg2)
    

    def stupidCut(self,fourLepton):
        #if not 4mu/4e  pass 
        if abs(fourLepton.leg1.leg1.pdgId())!=abs(fourLepton.leg2.leg1.pdgId()):
            return True

        #print "\nNominal, mZ1 %.3f, mZ2 %.3f: %s" % (fourLepton.leg1.M(),fourLepton.leg2.M(),fourLepton)
        leptons  = [ fourLepton.leg1.leg1, fourLepton.leg1.leg2, fourLepton.leg2.leg1, fourLepton.leg2.leg2 ]
        quads = []
        for quad in self.findOSSFQuads(leptons): 
            # skip self
            if fourLepton.leg1.leg1 == quad.leg1.leg1 and fourLepton.leg1.leg2 == quad.leg1.leg2 and fourLepton.leg2.leg1 == quad.leg2.leg1:
                continue

            # skip those that have a worse Z1 mass than the nominal
            if abs(fourLepton.leg1.M()-91.1876) < abs(quad.leg1.M()-91.1876):
                continue
            #print "Found alternate, mZ1 %.3f, mZ2 %.3f: %s" % (quad.leg1.M(),quad.leg2.M(),quad)
            quads.append(quad)
        if len(quads) == 0:
            #print "No alternates to ",fourLepton
            return True
        bestByZ1 = min(quads, key = lambda quad : abs(quad.leg1.M()-91.1876))
        #print "Best alternate, mZ1 %.3f, mZ2 %.3f: %s" % (bestByZ1.leg1.M(),bestByZ1.leg2.M(),bestByZ1)
        return bestByZ1.leg2.M() > 12.


    def fourLeptonPtThresholds(self, fourLepton):
        leading_pt = fourLepton.sortedPtLeg(0).pt() 
        subleading_pt = fourLepton.sortedPtLeg(1).pt() 
        return leading_pt>20  and subleading_pt>10
    

    def ghostSuppression(self, fourLepton):
        leptons = fourLepton.daughterLeptons()
        for l1,l2 in itertools.combinations(leptons,2):
            if deltaR(l1.eta(),l1.phi(),l2.eta(),l2.phi())<0.02:
                return False
        return True    
        
    def zSorting(self,Z1,Z2):
        return abs(Z1.M()-91.1876) <= abs(Z2.M()-91.1876)

    def findOSSFQuads(self, leptons):
        '''Make combinatorics and make permulations of four leptons
           Cut the permutations by asking Z1 nearest to Z and also 
           that plus is the first
        '''
        out = []
        for l1, l2,l3,l4 in itertools.permutations(leptons, 4):
            if (l1.pdgId()+l2.pdgId())!=0: 
                continue;
            if (l3.pdgId()+l4.pdgId())!=0:
                continue;
            if (l1.pdgId()<l2.pdgId())!=0: 
                continue;
            if (l3.pdgId()<l4.pdgId())!=0: 
                continue;

            quadObject =DiObjectPair(l1, l2,l3,l4)

            if hasattr(quadObject.leg1, "vtx") and hasattr(quadObject.leg2, "vtx"): pass
            else:
                self.attachVtxDuo(quadObject.leg1)
                self.attachVtxDuo(quadObject.leg2)
            
            if not self.zSorting(quadObject.leg1,quadObject.leg2):
                continue
            out.append(quadObject)

        return out

    def attachVtxDuo(self, diObj):
        ''' attach a fitted vertex the input diObject'''
        mu1 = diObj.leg1
        mu2 = diObj.leg2
                
        myVtx = self.vtxKalman(mu1.physObj, mu2.physObj)
        myVtx.ComputeCTau(mu1.associatedVertex)
        diObj.vtx = myVtx

        verbose = False
        if verbose:
            print "[debug]", mu1, mu2
            print "[debug] vtx (chi2 = %.2f, prob = %.2f, ndf = %.2f, nchi2 = %.2f, ctau = %.2f, cosAlpha = %.2f)" % (myVtx.Chi2(), myVtx.Prob(), myVtx.NDF(), myVtx.NChi2(), myVtx.ctau(), myVtx.cosAlpha())
            print "[debug] PV-mu1, chi2 = %.2f, ndof = %s" % (mu1.associatedVertex.chi2(), mu1.associatedVertex.ndof())
            print "[debug] PV-mu2, chi2 = %.2f, ndof = %s" % (mu2.associatedVertex.chi2(), mu2.associatedVertex.ndof())


    def attachVtxQuad(self, fourLep):
        ''' attach a fitted vertex the input diObject'''
        mu1 = fourLep.leg1.leg1
        mu2 = fourLep.leg1.leg2
        mu3 = fourLep.leg2.leg1
        mu4 = fourLep.leg2.leg2
        
        myVtx = self.vtxKalman(mu1.physObj, mu2.physObj, mu3.physObj, mu4.physObj)
        #myVtx.ComputeCTau(mu1.associatedVertex)
        fourLep.vtx = myVtx
        verbose = False
        if verbose:
            print "[debug] quad vtx (chi2 = %.2f, prob = %.2f, ndf = %.2f, nchi2 = %.2f, ctau = %.2f, cosAlpha = %.2f)" % (myVtx.Chi2(), myVtx.Prob(), myVtx.NDF(), myVtx.NChi2(), myVtx.ctau(), myVtx.cosAlpha())
            print "[debug]   mu index = %s, %s, %s, %s" % (mu1.index, mu2.index, mu3.index, mu4.index)
            print "[debug]   mu pdgId = %s, %s, %s, %s" % (mu1.pdgId(), mu2.pdgId(), mu3.pdgId(), mu4.pdgId())
            print "[debug]   mu pdgId = %s, %s, %s, %s" % (mu1.charge(), mu2.charge(), mu3.charge(), mu4.charge())
            
    ##-------- stale functions:
    def diLeptonMass(self,dilepton):
        return dilepton.M()>12.0 and dilepton.M()<120.

    def fourLeptonMassZ1Z2(self,fourLepton):
        return self.diLeptonMass(fourLepton.leg1) and self.diLeptonMass(fourLepton.leg2)

    def fourLeptonMassZ1(self,fourLepton):
        return fourLepton.leg1.M()>40.0 and fourLepton.leg1.M()<120. # usually implied in fourLeptonMassZ1Z2 but sometimes needed independently

    
    def qcdSuppression(self, fourLepton):
        return fourLepton.minPairMll(onlyOS=True)>4.0

    def fourLeptonIsolation(self,fourLepton):
        for l in fourLepton.daughterLeptons():
            if abs(l.pdgId())==11:
                if not self.electronIsolation(l):
                    return False
            if abs(l.pdgId())==13:
                if not self.muonIsolation(l):
                    return False
        return True
    
    def attachJets(self,quad,jets):
        # must clean jets from the leptons in the candidate in addition to the ones already cleaned
        leptonsAndPhotons = quad.daughterLeptons() + quad.daughterPhotons()
        quad.cleanJets = []
        quad.cleanJetIndices = [ ]
        for ij,j in enumerate(jets):
           bm, dr2 = bestMatch(j, leptonsAndPhotons)
           if dr2 < 0.4**2: 
                continue
           quad.cleanJets.append(j)
           quad.cleanJetIndices.append(ij)
