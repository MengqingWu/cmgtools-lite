import PhysicsTools.HeppyCore.framework.config as cfg
import os

## @Nov28,2016:
## 2016 B-G ReReco info: https://twiki.cern.ch/twiki/bin/view/CMS/PdmV2016Analysis#Re_reco_datasets
## -----------------------------
## twiki for news of samples (up to date):
## https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD#Run2_Spring16_MiniAOD_v1_campaig
## PromptReco changed to 23Sep2016 (data rereco) - CMSSW_8_0_20 or later for condition database
##

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

jsonFilter=False # define json via 'component.json=xxx' in loadSamples80x.py

json_dir='/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/'
##goldenJson='Cert_271036-277933_13TeV_PromptReco_Collisions16_JSON_MuonPhys.txt'
goldenJson='Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_MuonPhys.txt'
json = json_dir + goldenJson
#run_range = (273013, 276811) # used for ICHEP2016 - 12.9fb^-1
run_range = None

## note for 2016B: this acquisition era exists in 2 separate versions with no overlap in terms of run content
### ----------------------------- Run2016B ReReco v1 ----------------------------------------

#DoubleMuon_Run2016B_PromptReco     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco"    , "/DoubleMuon/Run2016B-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016B_ReRecoV1 = kreator.makeDataComponent("MuOnia_Run2016B_ReRecoV1", "/MuOnia/Run2016B-23Sep2016-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)
Charmonium_Run2016B_ReRecoV1 = kreator.makeDataComponent("Charmonium_Run2016B_ReRecoV1", "/Charmonium/Run2016B-23Sep2016-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)

### ----------------------------- Run2016B ReReco v2 ----------------------------------------

#DoubleMuon_Run2016B_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016B_PromptReco_v2"    , "/DoubleMuon/Run2016B-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016B_ReRecoV2 = kreator.makeDataComponent("MuOnia_Run2016B_ReRecoV2", "/MuOnia/Run2016B-23Sep2016-v3/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)
Charmonium_Run2016B_ReRecoV2 = kreator.makeDataComponent("Charmonium_Run2016B_ReRecoV2", "/Charmonium/Run2016B-23Sep2016-v3/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)

### ----------------------------- Run2016C ReReco v1 ----------------------------------------

#DoubleMuon_Run2016C_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016C_PromptReco_v2"    , "/DoubleMuon/Run2016C-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016C_ReRecoV1 = kreator.makeDataComponent("MuOnia_Run2016C_ReRecoV1", "/MuOnia/Run2016C-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016C_ReRecoV1 = kreator.makeDataComponent("Charmonium_Run2016C_ReRecoV1", "/Charmonium/Run2016C-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)

### ----------------------------- Run2016D ReReco v1 ----------------------------------------

#DoubleMuon_Run2016D_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016D_PromptReco_v2"    , "/DoubleMuon/Run2016D-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range) 
MuOnia_Run2016D_ReRecoV1 = kreator.makeDataComponent("MuOnia_Run2016D_ReRecoV1", "/MuOnia/Run2016D-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)
Charmonium_Run2016D_ReRecoV1 = kreator.makeDataComponent("Charmonium_Run2016D_ReRecoV1", "/Charmonium/Run2016D-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)


### ----------------------------- Run2016E ReReco v1 ----------------------------------------

#DoubleMuon_Run2016E_PromptReco_v2     = kreator.makeDataComponent("DoubleMuon_Run2016E_PromptReco_v2"    , "/DoubleMuon/Run2016E-PromptReco-v2/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016E_ReRecoV1 = kreator.makeDataComponent("MuOnia_Run2016E_ReRecoV1", "/MuOnia/Run2016E-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)
Charmonium_Run2016E_ReRecoV1 = kreator.makeDataComponent("Charmonium_Run2016E_ReRecoV1", "/Charmonium/Run2016E-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)


### ----------------------------- Run2016F ReReco v1 ----------------------------------------

#DoubleMuon_Run2016F_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016F_PromptReco_v1"    , "/DoubleMuon/Run2016F-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016F_ReRecoV1 = kreator.makeDataComponent("MuOnia_Run2016F_ReRecoV1", "/MuOnia/Run2016F-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)
Charmonium_Run2016F_ReRecoV1 = kreator.makeDataComponent("Charmonium_Run2016F_ReRecoV1", "/Charmonium/Run2016F-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range)


### ----------------------------- Run2016G ReReco v1 ----------------------------------------

#DoubleMuon_Run2016G_PromptReco_v1     = kreator.makeDataComponent("DoubleMuon_Run2016G_PromptReco_v1"    , "/DoubleMuon/Run2016G-PromptReco-v1/MINIAOD"    , "CMS", ".*root", json, run_range)
MuOnia_Run2016G_ReRecoV1 = kreator.makeDataComponent("MuOnia_Run2016G_ReRecoV1", "/MuOnia/Run2016G-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)
Charmonium_Run2016G_ReRecoV1 = kreator.makeDataComponent("Charmonium_Run2016G_ReRecoV1", "/Charmonium/Run2016G-23Sep2016-v1/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json,run_range=run_range)

### ----------------------------- Run2016H PromptReco v2 ----------------------------------------
MuOnia_Run2016H_PromptRecoV2 = kreator.makeDataComponent("MuOnia_Run2016H_PromptRecoV2", "/MuOnia/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json, run_range=run_range, useAAA=True)
Charmonium_Run2016H_PromptRecoV2 = kreator.makeDataComponent("Charmonium_Run2016H_PromptRecoV2", "/Charmonium/Run2016H-PromptReco-v2/MINIAOD", "CMS", ".*root", jsonFilter=jsonFilter, json=json,run_range=run_range, useAAA=True)

### ----------------------------- summary ----------------------------------------


### ---------------------------------------------------------------------
