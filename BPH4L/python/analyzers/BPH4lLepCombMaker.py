import ROOT
import random
import math
from  itertools import combinations, product
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.BPH4L.tools.Pair import *


class BPH4lLepCombMaker( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(BPH4lLepCombMaker,self).__init__(cfg_ana, cfg_comp, looperName)
        self.selectMuMuPair = cfg_ana.selectMuMuPair
        self.selectElElPair = cfg_ana.selectElElPair
        self.selectVBoson = cfg_ana.selectVBoson

        self.doElMu = cfg_ana.doElMu if hasattr(cfg_ana, 'doElMu') else False
        self.selectElMuPair = cfg_ana.selectElMuPair if self.doElMu else None
        self.selectFakeBoson = cfg_ana.selectFakeBoson if self.doElMu else None

    def declareHandles(self):
        super(BPH4lLepCombMaker, self).declareHandles()


    def beginLoop(self, setup):
        super(BPH4lLepCombMaker,self).beginLoop(setup)
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('pass events')
        count.register('pass 0 charge 4mu evts')
        #count.register('pass mu events')

        
    def process(self, event):
        self.readCollections( event.input )
        self.counters.counter('events').inc('all events')

        #self.n_pass_el = 0
        self.n_pass_mu = 0
        self.n_pass_emu = 0
        self.n_pass_quadMu = 0

        LL = []
        quadMu = []
        # # electron pair
        # for l1,l2 in combinations(event.selectedElectrons,2):
        #     if  (l1.pdgId() == -l2.pdgId() or l1.charge() == -l2.charge()):
        #         pair = Pair(l1,l2,23)
        #         if self.selectElElPair(pair):
        #             LL.append(pair)
        #             self.n_pass_el += 1
        
        # muon pair

        for l1,l2,l3,l4 in combinations(event.selectedMuons, 4):
            totalCharge=1
            totalCharge=l1.charge()+l2.charge()+l3.charge()+l4.charge()
            if totalCharge==0:
                self.n_pass_quadMu += 1
                quadMu.append((l1,l2,l3,l4))
            
        for l1,l2 in combinations(event.selectedMuons,2):
            #if  (l1.pdgId() == -l2.pdgId() and l1.charge() == -l2.charge()):
            #if  (l1.charge() == -l2.charge()):
            if  (l1.pdgId() == -l2.pdgId() or l1.charge() == -l2.charge()):
                pair = Pair(l1,l2,23)
                if self.selectMuMuPair(pair):
                    LL.append(pair)
                    self.n_pass_mu += 1

        # select V boson

        event.LL = [pair for pair in LL if self.selectVBoson(pair) ]

        if self.n_pass_quadMu>0.1: 
            self.counters.counter('events').inc('pass 0 charge 4mu evts')
            self.counters.counter('events').inc('pass events') 
            return True
        else: return False
        #if self.n_pass_mu>0.1: 
            #self.counters.counter('events').inc('pass mu events')       
  
        #if len(event.LL)<=0:
            #return False
        
        #self.counters.counter('events').inc('pass events') 
        #return True



        
            

        


                
                
