##########################################################
##      configuration for BPH4L 
##########################################################

import CMGTools.BPH4L.fwlite.Config as cfg
from CMGTools.BPH4L.fwlite.Config import printComps
from CMGTools.BPH4L.RootTools import *
from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption


#Load all common analyzers
from CMGTools.BPH4L.analyzers.bph4lCore_cff import *

#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.BPH4L.samples.loadSamples80x import *
selectedComponents = mcSamples+dataSamples

#-------- Analyzer
from CMGTools.BPH4L.analyzers.bph4l_Tree import *

#-------- SEQUENCE
bph4lObjSequence.remove(jetAna)
bph4lObjSequence.remove(metAna)
sequence = cfg.Sequence(bph4lPreSequence + [fastSkim2L] + bph4lObjSequence + [
    twoLeptonAnalyzerOnia, 
    #twoLeptonEventSkimmerOnia, 
    twoLeptonTreeProducerOnia,
    dumpEvents,
])

#-------- HOW TO RUN
test = 1
if test==1:
    # test a single component, using a single thread.
    #selectedComponents = dataSamples
    selectedComponents = [MuOnia_Run2016E_ReRecoV1]# MuOnia_Run2016B_ReRecoV1, MuOnia_Run2016E/F/G_ReRecoV1, MuOnia_Run2016H_PromptRecoV2]
    #selectedComponents = MuOnia
    #selectedComponents = Charmonium
    for c in selectedComponents:
        #print '[debug]:', c.files
        #c.files = c.files[:1]
        c.splitFactor = (len(c.files)/10 if len(c.files)>10 else 1)
        #c.splitFactor = 1
        #c.triggers=triggers_1mu_noniso
        #c.triggers=triggers_1e_noniso
elif test==0:
    #selectedComponents = dataSamples
    selectedComponents = MuOnia
    for c in selectedComponents:
        c.splitFactor = (len(c.files)/5 if len(c.files)>5 else 1)
else:
    print " == check your config python file mode! (test==1 or 0) == "
    exit
## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='bph4lTreeProducer/tree.root',
    option='recreate'
    )
outputService.append(output_service)

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
event_class = Events
if getHeppyOption("nofetch"):
    event_class = Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     events_class = event_class)


