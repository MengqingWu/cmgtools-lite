import PhysicsTools.HeppyCore.framework.config as cfg
import os

## twiki for news of samples (up to date):
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD#Run2_Spring16_MiniAOD_v1_campaig

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

jsonFilter=False # define json via 'component.json=xxx' in loadSamples80x.py

json_dir='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/'
json = json_dir + 'Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt'
run_range = (273013, 276811)

### ----------------------------- Run2016B PromptReco v1 ----------------------------------------

#DoubleMuon_Run2016B_PromptReco     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco"    , "/DoubleMuon/Run2016B-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016B_PromptV1 = kreator.makeDataComponent("MuOnia_Run2016B_PromptV1", "/MuOnia/Run2016C-PromptReco-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016B_PromptV1 = kreator.makeDataComponent("Charmonium_Run2016B_PromptV1", "/Charmonium/Run2016B-PromptReco-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)

### ----------------------------- Run2016B PromptReco v2 ----------------------------------------

#DoubleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco_v2"    , "/DoubleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016B_PromptV2 = kreator.makeDataComponent("MuOnia_Run2016B_PromptV2", "/MuOnia/Run2016B-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016B_PromptV2 = kreator.makeDataComponent("Charmonium_Run2016B_PromptV2", "/Charmonium/Run2016B-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)

### ----------------------------- Run2016C PromptReco v2 ----------------------------------------

#DoubleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016C_PromptReco_v2"    , "/DoubleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016C_PromptV2 = kreator.makeDataComponent("MuOnia_Run2016C_PromptV2", "/MuOnia/Run2016C-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016C_PromptV2 = kreator.makeDataComponent("Charmonium_Run2016C_PromptV2", "/Charmonium/Run2016C-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)

### ----------------------------- Run2016D PromptReco v2 ----------------------------------------

#DoubleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016D_PromptReco_v2"    , "/DoubleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range) 
MuOnia_Run2016D_PromptV2 = kreator.makeDataComponent("MuOnia_Run2016D_PromptV2", "/MuOnia/Run2016D-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016D_PromptV2 = kreator.makeDataComponent("Charmonium_Run2016D_PromptV2", "/Charmonium/Run2016D-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)


### ----------------------------- Run2016E PromptReco v2 ----------------------------------------

#DoubleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016E_PromptReco_v2"    , "/DoubleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016E_PromptV2 = kreator.makeDataComponent("MuOnia_Run2016E_PromptV2", "/MuOnia/Run2016E-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016E_PromptV2 = kreator.makeDataComponent("Charmonium_Run2016E_PromptV2", "/Charmonium/Run2016E-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)


### ----------------------------- Run2016F PromptReco v1 ----------------------------------------

#DoubleMuon_Run2016F_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016F_PromptReco_v1"    , "/DoubleMuon/Run2016F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016F_PromptV1 = kreator.makeDataComponent("MuOnia_Run2016F_PromptV1", "/MuOnia/Run2016F-PromptReco-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016F_PromptV1 = kreator.makeDataComponent("Charmonium_Run2016F_PromptV1", "/Charmonium/Run2016F-PromptReco-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)


### ----------------------------- Run2016G PromptReco v1 ----------------------------------------

#DoubleMuon_Run2016G_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016G_PromptReco_v1"    , "/DoubleMuon/Run2016G-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016G_PromptV1 = kreator.makeDataComponent("MuOnia_Run2016G_PromptV1", "/MuOnia/Run2016G-PromptReco-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016G_PromptV1 = kreator.makeDataComponent("Charmonium_Run2016G_PromptV1", "/Charmonium/Run2016G-PromptReco-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json,run_range=run_range)

### ----------------------------- summary ----------------------------------------


### ---------------------------------------------------------------------
