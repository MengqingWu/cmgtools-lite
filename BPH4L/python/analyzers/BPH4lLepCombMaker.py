import random
import math
from  itertools import combinations, product
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.BPH4L.tools.Pair import Pair
from CMGTools.BPH4L.tools.Quad import Quad

from ROOT import gSystem

gSystem.Load("libCMGToolsBPH4L")

from ROOT import QuadObjFactory

class BPH4lLepCombMaker( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(BPH4lLepCombMaker,self).__init__(cfg_ana, cfg_comp, looperName)
        self.selectMuMuPair = cfg_ana.selectMuMuPair
        self.selectElElPair = cfg_ana.selectElElPair
        self.selectVBoson = cfg_ana.selectVBoson

        self.doElMu = cfg_ana.doElMu if hasattr(cfg_ana, 'doElMu') else False
        self.selectElMuPair = cfg_ana.selectElMuPair if self.doElMu else None
        self.selectFakeBoson = cfg_ana.selectFakeBoson if self.doElMu else None

        self.QuadObjFactory = QuadObjFactory()

        self.printalot = True # debug print
        self.do_filter = cfg_ana.do_filter if hasattr(cfg_ana, 'do_filter') else False
        
    def declareHandles(self):
        super(BPH4lLepCombMaker, self).declareHandles()
     
    def beginLoop(self, setup):
        super(BPH4lLepCombMaker,self).beginLoop(setup)
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('pass events')
        count.register('pass 0 charge 4mu evts')

        
    def process(self, event):
        self.readCollections( event.input )
        self.counters.counter('events').inc('all events')

        #self.n_pass_el = 0
        #self.n_pass_mu = 0
        self.n_pass_emu = 0
        self.n_pass_MuFour = 0

        #LL = []
        MuFour = []
        
        # muon pair

        for l1,l2,l3,l4 in combinations(event.selectedMuons, 4):

            if l1.charge()+l2.charge()+l3.charge()+l4.charge()==0:

                quad=Quad(l1,l2,l3,l4)
                self.QuadObjFactory.set4muVtx(l1.physObj,l2.physObj,l3.physObj,l4.physObj)
                setattr(quad, 'vtxProb', self.QuadObjFactory.get4muVtxProb())
                setattr(quad, 'vtxChi2', self.QuadObjFactory.get4muVtxChi2())
                print " Chi2 test for 4-mu common vertex: ", quad.vtxProb
                
                lepP=[]
                lepN=[]
                for i in [l1,l2,l3,l4]:
                    if i.charge()>0: lepP.append(i)
                    elif i.charge()<0: lepN.append(i)
                    else: print "== weird mu with 0 charge == "

                _1a = Pair(lepP[0], lepN[0])
                _1b = Pair(lepP[1], lepN[1])
                _2a = Pair(lepP[0], lepN[1])
                _2b = Pair(lepP[1], lepN[0])
                
                for subp in [_1a, _1b, _2a, _2b]:
                    self.QuadObjFactory.set2muVtx(subp.leg1.physObj, subp.leg2.physObj)
                    setattr(subp, 'vtxProb', self.QuadObjFactory.get2muVtxProb())
                    setattr(subp, 'vtxChi2', self.QuadObjFactory.get2muVtxChi2())
                    setattr(subp, 'fitMass', self.QuadObjFactory.get2muMass())
                    setattr(subp, 'fitMassErr2', self.QuadObjFactory.get2muMassErr2())
                        
                if self.printalot: # debug:
                    #print " [info] dR(1,2,12) = %.2f, %.2f, %.2f " % (pair1.deltaR(), pair2.deltaR(), pair12.deltaR())
                    print " [info] dR(1p, 2p)  = %.2f, %.2f " % (_1a.deltaR(), _1b.deltaR())
                    print "        dz(1,2,3,4) = %.2f, %.2f, %.2f. %.2f " % (l1.physObj.track().dz(l1.associatedVertex.position()), l2.physObj.track().dz(l2.associatedVertex.position()), l3.physObj.track().dz(l3.associatedVertex.position()), l4.physObj.track().dz(l4.associatedVertex.position()))
                    print "        dxy(1,2,3,4)= %.2f, %.2f, %.2f, %.2f " % (l1.physObj.track().dxy(l1.associatedVertex.position()), l2.physObj.track().dxy(l2.associatedVertex.position()), l3.physObj.track().dxy(l3.associatedVertex.position()), l4.physObj.track().dxy(l4.associatedVertex.position()))


                MuFour.append({'quad': quad,
                               'pair1': (_1a, _1b),
                               'pair2': (_2a, _2b),
                })
                self.n_pass_MuFour += 1             

            else: # non-zero charged 4-mu, skipped
                continue  
            
        # for l1,l2 in combinations(event.selectedMuons,2):
        #     #if  (l1.pdgId() == -l2.pdgId() and l1.charge() == -l2.charge()):
        #     #if  (l1.charge() == -l2.charge()):
        #     if  (l1.pdgId() == -l2.pdgId() or l1.charge() == -l2.charge()):
        #         pair = Pair(l1,l2,23)
        #         if self.selectMuMuPair(pair):
        #             LL.append(pair)
        #             self.n_pass_mu += 1

        # select mu-mu pair
        pvalueLevel=-1 # 0.05 by default
        #event.LL = [pair for pair in LL if self.selectVBoson(pair) ]
        event.MuFour = [quad for quad in MuFour if quad['quad'].vtxProb > pvalueLevel] # select MuFour only if vtxProb > 0.05

        # filter events without 4mu comb:
        if self.do_filter:
            if self.n_pass_MuFour>0.1: 
                self.counters.counter('events').inc('pass 0 charge 4mu evts')
                self.counters.counter('events').inc('pass events') 
                return True
            else: return False
        else:
            self.counters.counter('events').inc('pass events') 
            return True


        
            

        


                
                
