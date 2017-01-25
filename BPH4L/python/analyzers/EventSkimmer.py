from math import *
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
import os

        
class EventSkimmer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(EventSkimmer,self).__init__(cfg_ana,cfg_comp,looperName)
        self.required = cfg_ana.required
    def declareHandles(self):
        super(EventSkimmer, self).declareHandles()
        self.counters.addCounter('events')
        count = self.counters.counter('events')
        count.register('all events')
        count.register('passed skim')

    def beginLoop(self, setup):
        super(EventSkimmer,self).beginLoop(setup)

    def process(self, event):
        self.readCollections( event.input )
        self.counters.counter('events').inc('all events')

        for col in self.required:
            if hasattr(event,col):
                if len(getattr(event,col))>0:
                    self.counters.counter('events').inc('passed skim')
                    return True
        return False    
