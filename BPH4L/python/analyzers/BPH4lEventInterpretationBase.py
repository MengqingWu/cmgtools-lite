import random
import math
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle
from CMGTools.BPH4L.tools.JetReCalibrator import JetReCalibrator
from CMGTools.BPH4L.tools.JetResolution import JetResolution
from PhysicsTools.HeppyCore.utils.deltar import *
import PhysicsTools.HeppyCore.framework.config as cfg
#from CMGTools.BPH4L.tools.PyJetToolbox import *
from copy import copy



class BPH4lEventInterpretationBase( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName):
        super(BPH4lEventInterpretationBase,self).__init__(cfg_ana, cfg_comp, looperName)
        # processTypes is a list of final states to be processed, can include "LLNuNu", "ElMuNuNu", "PhotonJets"
        self.processTypes = self.cfg_ana.processTypes
        
        if "LLNuNu" in self.processTypes: self.selectPairLLNuNu = self.cfg_ana.selectPairLLNuNu
        if "ElMuNuNu" in self.processTypes: self.selectPairElMuNuNu = self.cfg_ana.selectPairElMuNuNu
        if "PhotonJets" in self.processTypes: self.selectPhotonJets = self.cfg_ana.selectPhotonJets

            
            
    def declareHandles(self):
        super(BPH4lEventInterpretationBase, self).declareHandles()


    def beginLoop(self, setup):
        super(BPH4lEventInterpretationBase,self).beginLoop(setup)
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('pass llNuNu events')
        count.register('pass elmuNuNu events')
        count.register('pass PhotonJets events')


    def process(self, event):
        self.readCollections( event.input )

            

        


                
                
