import PhysicsTools.HeppyCore.framework.config as cfg
import os

## updated from Jan-20-2017
## according to https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD#MC_for_Moriond_2017
## using  dataset=/*/RunIISummer16MiniAODv2*PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6*/MINIAODSIM
## recommended release: 8_0_25 or later
#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

McMtagger="RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1"

# Chib0ToUps1SMuMu_m* (for Chi_b0 -> Y + mumu )
Chib0ToUps1SMuMu_m11 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m11","/Chib0ToUps1SMuMu_m11_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False) 
Chib0ToUps1SMuMu_m15 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m15","/Chib0ToUps1SMuMu_m15_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
Chib0ToUps1SMuMu_m18p5 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m18p5","/Chib0ToUps1SMuMu_m18p5_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False) 
Chib0ToUps1SMuMu_m25 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m25","/Chib0ToUps1SMuMu_m25_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
Chib0ToUps1SMuMu_m36 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m36","/Chib0ToUps1SMuMu_m36_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
Chib0ToUps1SMuMu_m50 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m50","/Chib0ToUps1SMuMu_m50_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)

# H0ToUps1SMuMu_m* (for H_0 -> Y + mumu )
H0ToUps1SMuMu_m11 = kreator.makeMCComponent("H0ToUps1SMuMu_m11","/H0ToUps1SMuMu_m11_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m15 = kreator.makeMCComponent("H0ToUps1SMuMu_m15","/H0ToUps1SMuMu_m15_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m18p5 = kreator.makeMCComponent("H0ToUps1SMuMu_m18p5","/H0ToUps1SMuMu_m18p5_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False) 
H0ToUps1SMuMu_m25 = kreator.makeMCComponent("H0ToUps1SMuMu_m25","/H0ToUps1SMuMu_m25_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m36 = kreator.makeMCComponent("H0ToUps1SMuMu_m36","/H0ToUps1SMuMu_m36_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m50 = kreator.makeMCComponent("H0ToUps1SMuMu_m50","/H0ToUps1SMuMu_m50_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)


### DiBosons

### ggZZ

GJetsHT = [
GJets_HT40to100,
GJets_HT100to200,
GJets_HT200to400,
GJets_HT400to600,
GJets_HT600toInf
]
