import PhysicsTools.HeppyCore.framework.config as cfg
import os

## updated from Feb-09-2017
## signal samples only avaiable with RunIIFall15MiniAODv2 versionss (for 2015 data only)
#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

McMtagger="RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1"

## Tetraquark signals (from di-upsilon analysis) ##
# Chib0ToUps1SMuMu_m* (for Chi_b0 -> Y + mumu )
Chib0ToUps1SMuMu_m11 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m11","/Chib0ToUps1SMuMu_m11_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=True) 
Chib0ToUps1SMuMu_m15 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m15","/Chib0ToUps1SMuMu_m15_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
Chib0ToUps1SMuMu_m18p5 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m18p5","/Chib0ToUps1SMuMu_m18p5_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False) 
Chib0ToUps1SMuMu_m25 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m25","/Chib0ToUps1SMuMu_m25_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=True)
Chib0ToUps1SMuMu_m36 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m36","/Chib0ToUps1SMuMu_m36_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
Chib0ToUps1SMuMu_m50 = kreator.makeMCComponent("Chib0ToUps1SMuMu_m50","/Chib0ToUps1SMuMu_m50_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)

# H0ToUps1SMuMu_m* (for H_0 -> Y + mumu )
H0ToUps1SMuMu_m11 = kreator.makeMCComponent("H0ToUps1SMuMu_m11","/H0ToUps1SMuMu_m11_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m15 = kreator.makeMCComponent("H0ToUps1SMuMu_m15","/H0ToUps1SMuMu_m15_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m18p5 = kreator.makeMCComponent("H0ToUps1SMuMu_m18p5","/H0ToUps1SMuMu_m18p5_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=True) 
H0ToUps1SMuMu_m25 = kreator.makeMCComponent("H0ToUps1SMuMu_m25","/H0ToUps1SMuMu_m25_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m36 = kreator.makeMCComponent("H0ToUps1SMuMu_m36","/H0ToUps1SMuMu_m36_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=False)
H0ToUps1SMuMu_m50 = kreator.makeMCComponent("H0ToUps1SMuMu_m50","/H0ToUps1SMuMu_m50_TuneCUEP8M1_13TeV-pythia8/"+McMtagger+"/MINIAODSIM", "CMS", ".*root", 999, useAAA=True)

## ZToJpsiLL analysis signals: (xsect from MCM)
## twiki: https://twiki.cern.ch/twiki/bin/view/CMS/DoubleJpsi-13TeV
ZToJPsiMuMu = kreator.makeMCComponent("ZToJPsiMuMu","/ZToJPsiMuMu_TuneCUEP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 56790000000*0.854, useAAA=False)
ZToJPsiEE = kreator.makeMCComponent("ZToJPsiEE","/ZToJPsiEE_TuneCUEP8M1_13TeV-pythia8/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM", "CMS", ".*root", 415.9*0.87, useAAA=False)

