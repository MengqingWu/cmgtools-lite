from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from CMGTools.BPH4L.tools.DiObject import DiObject

import itertools

from ROOT import gSystem
gSystem.Load("libCMGToolsBPH4L")
from ROOT import bph4lVertexFitter
#from bph4lVertexFitter import KalmanVertex
    
class TwoLeptonAnalyzer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(TwoLeptonAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.mode = cfg_ana.mode
        if self.mode not in [ "Z", "Onia" ]: raise RuntimeError, "Unsupported mode"
        self.muonId = getattr(cfg_ana, "muonId", "POG_ID_Soft")
        self.electronId = getattr(cfg_ana, "electronId", "POG_MVA_ID_NonTrig")
        self.oniaMassMin = getattr(cfg_ana, "oniaMassMin", 2.5) # inclusive range as default
        self.oniaMassMax = getattr(cfg_ana, "oniaMassMax", 12) # inclusive range as default
        #self.vtxFitter = bph4lVertexFitter()
        self.vtxKalman = bph4lVertexFitter.KalmanVertex
        
    def beginLoop(self, setup):
        super(TwoLeptonAnalyzer,self).beginLoop(setup)
        self.counters.addCounter('TwoLepton')
        count = self.counters.counter('TwoLepton')
        count.register('all events')
        count.register('all pairs')
        if self.mode == "Z":
            count.register('pass iso')
            count.register('best Z')
        elif self.mode == "Onia":
            count.register('pass onia')

    def process(self, event):
        self.readCollections( event.input )

        self.counters.counter('TwoLepton').inc('all events')
        # count leptons w/ ID required (cfg_ana):
        #tight_leptons = [ lep for lep in event.selectedLeptons if self.leptonID_tight(lep) ]
        lepCandidates = [ lep for lep in event.selectedLeptons if self.leptonID(lep)]
        
        # make dilepton pairs, possibly attach FSR photons (the latter not yet implemented)
        event.allPairs = self.findOSSFPairs(lepCandidates, []) #event.fsrPhotons)

        # count them, for the record
        for p in event.allPairs:
            self.counters.counter('TwoLepton').inc('all pairs')

        if self.mode == "Z":
            # make pairs of isolated leptons
            event.isolatedPairs = filter(self.twoLeptonIsolation, event.allPairs)
            for pair in event.isolatedPairs:
                self.counters.counter('TwoLepton').inc('pass iso')

            # get the best Z (mass closest to PDG value)
            # still a list, because if there's no isolated leptons it may be empty
            sortedIsoPairs = event.isolatedPairs[:] # make a copy
            sortedIsoPairs.sort(key = lambda dilep : abs(dilep.mass() - 91.1876))
            event.bestIsoZ = sortedIsoPairs[:1] # pick at most 1
            if len(event.bestIsoZ):
                self.counters.counter('TwoLepton').inc('best Z')
                
        elif self.mode == "Onia":
            event.onia = filter(self.oniaMassFilter, event.allPairs)
            for ionia in event.onia:
                mu1 = ionia.leg1
                mu2 = ionia.leg2
                
                myVtx = self.vtxKalman(mu1.physObj, mu2.physObj)
                myVtx.ComputeCTau(mu1.associatedVertex)
                ionia.vtx = myVtx
                print "[debug]", mu1, mu2
                print "[debug] vtx (chi2 = %.2f, prob = %.2f, ndf = %.2f, nchi2 = %.2f, ctau = %.2f, cosAlpha = %.2f)" % (myVtx.Chi2(), myVtx.Prob(), myVtx.NDF(), myVtx.NChi2(), myVtx.ctau(), myVtx.cosAlpha())
                print "[debug] PV-mu1, chi2 = %.2f, ndof = %s" % (mu1.associatedVertex.chi2(), mu1.associatedVertex.ndof())
                print "[debug] PV-mu2, chi2 = %.2f, ndof = %s" % (mu2.associatedVertex.chi2(), mu2.associatedVertex.ndof())

            if event.onia: self.counters.counter('TwoLepton').inc('pass onia')

    def leptonID(self, lepton):
        if abs(lepton.pdgId())==13: return lepton.muonID(self.muonId)
        elif abs(lepton.pdgId())==11: return lepton.electronID(self.electronId)
        else: return self.leptonID_tight(lepton)
            
    def leptonID_tight(self,lepton):
        return lepton.tightId()

    def muonIsolation(self,lepton):
        return lepton.relIsoAfterFSR < 0.35

    def electronIsolation(self,lepton):
        return lepton.relIsoAfterFSR < 0.35


    def twoLeptonIsolation(self,twoLepton):
        ##First ! attach the FSR photons of this candidate to the leptons!
        
        leptons = twoLepton.daughterLeptons()
        photons = twoLepton.daughterPhotons()

        for l in leptons:
            if abs(l.pdgId())==11:
                if not self.electronIsolation(l):
                    return False
            if abs(l.pdgId())==13:
                if not self.muonIsolation(l):
                    return False
        return True        

    def findOSSFPairs(self, leptons, photons):
        '''Make combinatorics and make permulations of two leptons
           Include FSR if in cfg file
        '''
        out = []
        for l1, l2 in itertools.permutations(leptons, 2):
            if (l1.pdgId()+l2.pdgId())!=0: 
                continue;
            if (l1.pdgId()<l2.pdgId())!=0: 
                continue;
            
            twoObject = DiObject(l1, l2)
            out.append(twoObject)

        return out

    def oniaMassFilter(self,twoLepton):
        return twoLepton.mll() > self.oniaMassMin and twoLepton.mll() < self.oniaMassMax

