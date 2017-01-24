

#####################
# load samples 
#####################

import PhysicsTools.HeppyCore.framework.config as cfg
import os

# Load backgrounds
#from CMGTools.BPH4L.samples.samples_13TeV_RunIISummer16MiniAODv2 import *
from CMGTools.BPH4L.samples.samples_13TeV_RunIISpring16MiniAODv2 import *
# Load signals
#from CMGTools.BPH4L.samples.samples_13TeV_signal80X import *
# Load Data 
from CMGTools.BPH4L.samples.samples_13TeV_DATA2016 import *
# Load triggers
from CMGTools.BPH4L.samples.triggers_13TeV_Spring16 import *


# backgrounds
backgroundSamples =[JpsiToMuMu_Pt8,
                    JpsiToMuMu_OniaMuFilter,
                    IncJpsiToMuMu_Pt3,
                    UpsilonToMuMu_Pt6,
]

# signals
signalSamples = []

# MC samples
mcSamples = signalSamples + backgroundSamples

# data
MuOnia=[MuOnia_Run2016B_ReRecoV1,
        MuOnia_Run2016B_ReRecoV2,
        MuOnia_Run2016C_ReRecoV1,
        MuOnia_Run2016D_ReRecoV1,
        MuOnia_Run2016E_ReRecoV1,
        MuOnia_Run2016F_ReRecoV1,
        MuOnia_Run2016G_ReRecoV1,
]
Charmonium=[Charmonium_Run2016B_ReRecoV1,
            Charmonium_Run2016B_ReRecoV2,
            Charmonium_Run2016C_ReRecoV1,
            Charmonium_Run2016D_ReRecoV1,
            Charmonium_Run2016E_ReRecoV1,
            Charmonium_Run2016F_ReRecoV1,
            Charmonium_Run2016G_ReRecoV1,
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
#jsonDir='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/'
jsonDir='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/'

#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-273730_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-274443_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-275783_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276097_13TeV_PromptReco_Collisions16_JSON_NoL1T_v2.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276384_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt'
#goldenJson = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-279588_13TeV_PromptReco_Collisions16_JSON_NoL1T.txt'
#goldenJson = 'Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt'
goldenJson = 'Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_MuonPhys.txt' # Luminosity: 36.63/fb 

#run_range = (271036,279588)
#run_range = (273013, 276811) # 12.9/fb
run_range = None

jsonFile = jsonDir + goldenJson


from CMGTools.BPH4L.setup.Efficiencies import *
dataDir = "$CMSSW_BASE/src/CMGTools/BPH4L/data"

for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250
    # puFile are used for pileup reweighting:
    comp.puFileMC=dataDir+"/pileup_MC_80x_271036-276811_68075.root"  # TBD: to update @Jan-24-2017
    comp.puFileData=dataDir+"/pileup_DATA_80x_271036-276811_68075.root" # TBD: to update @Jan-24-2017
    comp.eSFinput=dataDir+"/CutBasedID_LooseWP_76X_18Feb.txt_SF2D.root" # TBD: to update @Jan-24-2017
    comp.efficiency = eff2012
    #comp.triggers=triggers_1mu_noniso+triggers_1e_noniso
    comp.triggers= []
    comp.globalTag = "80X_mcRun2_asymptotic_2016_miniAODv2_v1"

for comp in dataSamples:
    comp.splitFactor = 250
    comp.isMC = False
    comp.isData = True
    comp.json = jsonFile
    comp.run_range = run_range
    #comp.globalTag = "Summer15_25nsV6_DATA"
    comp.globalTag = "80X_dataRun2_2016SeptRepro_v3"

if __name__ == "__main__":
    import sys
    if "test" in sys.argv:
        from CMGTools.RootTools.samples.ComponentCreator import testSamples
        testSamples(dataSamples)
    if "locality" in sys.argv:
        import re
        from CMGTools.Production.localityChecker import LocalityChecker
        tier2Checker = LocalityChecker("T2_CH_CERN", datasets="/*/*/MINIAOD*")
        for comp in dataSamples:
            if len(comp.files) == 0: 
                print '\033[34mE: Empty component: '+comp.name+'\033[0m'
                continue
            if not hasattr(comp,'dataset'): continue
            if not re.match("/[^/]+/[^/]+/MINIAOD(SIM)?", comp.dataset): continue
            if "/store/" not in comp.files[0]: continue
            if re.search("/store/(group|user|cmst3)/", comp.files[0]): continue
            if not tier2Checker.available(comp.dataset):
                print "\033[1;31mN: Dataset %s (%s) is not available on T2_CH_CERN\033[0m" % (comp.name,comp.dataset)
            else: print "Y: Dataset %s (%s) is available on T2_CH_CERN" % (comp.name,comp.dataset)
    if "refresh" in sys.argv:
        from CMGTools.Production.cacheChecker import CacheChecker
        checker = CacheChecker()
        datasets = dataSamples
        if len(sys.argv) > 2: 
            datasets = []
            for x in sys.argv[2:]:
                for s in dataSamples:
                    if x in s.name and s not in datasets:
                        datasets.append(s)
            datasets.sort(key = lambda d : d.name)
        for d in datasets:
            print "Checking ",d.name," aka ",d.dataset
            checker.checkComp(d, verbose=True)
    if "list" in sys.argv:
        from CMGTools.HToZZ4L.tools.configTools import printSummary
        datasets = dataSamples
        if len(sys.argv) > 2:
            datasets = []
            for x in sys.argv[2:]:
                for s in dataSamples:
                    if x in s.name and s not in datasets:
                        datasets.append(s)
            datasets.sort(key = lambda d : d.name)
        printSummary(datasets)
