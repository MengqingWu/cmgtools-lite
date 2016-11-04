
#####################
# load samples 
#####################

import PhysicsTools.HeppyCore.framework.config as cfg
import os

# Load backgrounds
from CMGTools.BPH4L.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
# Load signals
#from CMGTools.BPH4L.samples.samples_13TeV_signal80X import *
# Load Data 
from CMGTools.BPH4L.samples.samples_13TeV_DATA2016 import *
# Load triggers
from CMGTools.BPH4L.samples.triggers_13TeV_Spring16 import *


# backgrounds
backgroundSamples = []

# signals
signalSamples = []

# MC samples
mcSamples = signalSamples + backgroundSamples

# data
MuOnia=[#MuOnia_Run2016B_PromptV1,
        MuOnia_Run2016B_PromptV2,
        MuOnia_Run2016C_PromptV2,
        MuOnia_Run2016D_PromptV2,
        MuOnia_Run2016E_PromptV2,
        MuOnia_Run2016F_PromptV1,
        MuOnia_Run2016G_PromptV1,
]
Charmonium=[#Charmonium_Run2016B_PromptV1,
            Charmonium_Run2016B_PromptV2,
            Charmonium_Run2016C_PromptV2,
            Charmonium_Run2016D_PromptV2,
            Charmonium_Run2016E_PromptV2,
            Charmonium_Run2016F_PromptV1,
            Charmonium_Run2016G_PromptV1,
]

for s in MuOnia:
    #s.triggers = triggers_upsilon2mu + triggers_3mu
    s.triggers = [] 
    s.vetoTriggers = []
for s in Charmonium:
    #s.triggers = triggers_jspi2mu
    s.triggers = [] 
    #s.vetoTriggers = triggers_upsilon2mu + triggers_3mu
    s.vetoTriggers = []

dataSamples = MuOnia + Charmonium

# JSON
jsonDir='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/'

#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-273730_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274443_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276097_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276384_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-279588_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
goldenJson = 'Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt'

#run_range = (271036,279588)
run_range = (273013, 276811)

jsonFile = jsonDir + goldenJson


from CMGTools.BPH4L.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/BPH4L/data"

for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250
    comp.puFileMC=dataDir+"/pileup_MC_80x_271036-276811_68075.root"
    comp.puFileData=dataDir+"/pileup_DATA_80x_271036-276811_68075.root"
    comp.eSFinput=dataDir+"/CutBasedID_LooseWP_76X_18Feb.txt_SF2D.root"
    comp.efficiency = eff2012
    #comp.triggers=triggers_1mu_noniso+triggers_1e_noniso
    comp.triggers= []
    comp.globalTag = "Summer15_25nsV6_MC"

for comp in dataSamples:
    comp.splitFactor = 250
    comp.isMC = False
    comp.isData = True
    comp.json = jsonFile
    comp.run_range = run_range
    comp.globalTag = "Summer15_25nsV6_DATA"

