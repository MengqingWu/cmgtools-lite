import PhysicsTools.HeppyCore.framework.config as cfg
import os

## according to https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD#Run2_Spring16_MiniAOD_v2_campaig 
## using  dataset=/*/RunIISpring16MiniAODv2*/*                                             
## recommended release: 8_0_12 or later

#####COMPONENT CREATOR

from CMGTools.RootTools.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

# see GenSim info:
#     https://twiki.cern.ch/twiki/bin/view/CMS/BPH-Run2-QuarkOnia
#     https://twiki.cern.ch/twiki/bin/view/CMS/BPH-Run2-TP

# prompt Jpsi -> MuMu pythia8 with FSR on, pT(Jpsi-1S) > 3GeV
# xsect * filter eff: https://cms-pdmv.cern.ch/mcm/requests?prepid=BPH-RunIISummer15GS-00008&page=0&shown=655487
# Gen Parameters: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIISummer15GS-00008
JpsiToMuMu_OniaMuFilter = kreator.makeMCComponent("JpsiToMuMu_OniaMuFilter","/JpsiToMuMu_OniaMuonFilter_TuneCUEP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 53800000*0.172, useAAA=False) #30M evts  xsect in pb

# prompt Jpsi -> MuMu pythia with FSR on, pT(Jpsi-1S) > 8 GeV
# xsect * filter eff: https://cms-pdmv.cern.ch/mcm/requests?prepid=BPH-RunIISummer15GS-00012&page=0&shown=655487
# Gen Parameters: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIISummer15GS-00012
JpsiToMuMu_Pt8 = kreator.makeMCComponent("JpsiToMuMu_Pt8","/JpsiToMuMu_JpsiPt8_TuneCUEP8M1_13TeV-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 54980000*0.003, useAAA=False) #30M evts  

# non-prompt Jpsi -> MuMu (Bu->Kstar+MuMu, i.e. filter only pp events which produce a B)
# xsect * filter eff: https://cms-pdmv.cern.ch/mcm/requests?prepid=BPH-RunIISummer15GS-00029&page=0&shown=524415
# Gen Parameters: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIIWinter15GS-00027/0
IncJpsiToMuMu_Pt3 = kreator.makeMCComponent("IncJpsiToMuMu_Pt3","/InclusiveBtoJpsitoMuMu_JpsiPt3_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 16240000000*0.000036, useAAA=False) # 9M evts

# Upsilon -> MuMu pythia8 pT(Upsilon-1S) > 6 GeV
# xsect * filter eff: https://cms-pdmv.cern.ch/mcm/requests?page=0&prepid=BPH-RunIISummer15GS-00013&shown=655487
# Gen Parameters: https://cms-pdmv.cern.ch/mcm/public/restapi/requests/get_fragment/BPH-RunIISummer15GS-00013
UpsilonToMuMu_Pt6 = kreator.makeMCComponent("UpsilonToMuMu_Pt6","/UpsilonMuMu_UpsilonPt6_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 10890000*0.0395, useAAA=False) #M evts  xsect in pb


## # B meson background:

# Bs decay from RunII Bs To Jpsi Phi analysis, DGamma=0, 80X DR needed, xsect from MCM w/ BPH-RunIISummer15GS-00072
#  twiki: https://twiki.cern.ch/twiki/bin/view/CMS/BPH-RunIISummer15GS-BsToJpsiPhi
#BsToJpsiPhi_dGamma0 = kreator.makeMCComponent("BsToJpsiPhi_dGamma0","/BsToJpsiPhi_BMuonFilter_DGamma0_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM","CMS", ".*root", 16320000000*0.00041, useAAA=False) #M evts xsect in pb

# xsect from MCM w/ BPH-RunIISummer15GS-00028:
BsToJpsiPhi = kreator.makeMCComponent("BsToJpsiPhi","/BsToJpsiPhi_BMuonFilter_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM","CMS", ".*root", 16320000000*0.00041, useAAA=False) #M evts xsect in pb

#  twiki: https://twiki.cern.ch/twiki/bin/view/CMS/BPH-RunIISummer15GS-BsToPhiMuMu
# Bs -> Phi (KK) mumu, xsect from MCM w/ BPH-RunIISummer15GS-00080
BsToMuMuPhi = kreator.makeMCComponent("BsToMuMuPhi","/BsToMuMuPhi_BMuonFilter_SoftQCDnonD_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/MINIAODSIM","CMS", ".*root", 56790000000*0.000116, useAAA=False) #M evts xsect in pb


# B0 decay, xsect from MCM w/ BPH-RunIISummer15GS-00007
BdToKstarMuMu = kreator.makeMCComponent("BdToKstarMuMu","/BdToKstarMuMu_BFilter_TuneCUEP8M1_13TeV-pythia8-evtgen/RunIISpring16MiniAODv2-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/MINIAODSIM","CMS", ".*root", 78420000000*0.0069, useAAA=False) #M evts xsect in pb


## # continuous nonresonant mumu DY background:

##    xsect from https://twiki.cern.ch/twiki/bin/viewauth/CMS/SummaryTable1G25ns#DY_Z
DYJetsToLL_M10to50 = kreator.makeMCComponent("DYJetsToLL_M10to50", "/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 18610, useAAA=False) #M evts, NLO xsect in pb

# The mll in (5,50) sample exists in 2015 only: 
DYJetsToLL_M5to50 = kreator.makeMCComponent("DYJetsToLL_M5to50", "/DYJetsToLL_M-5to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring15DR74-Asympt25ns_MCRUN2_74_V9-v1/MINIAODSIM", "CMS", ".*root", 71310, useAAA=True) #9.3M evts, LO xsect in pb

####*********************** stale from xzz2l2v ***********************####
# # Photon+Jets
# GJet_Pt_15To6000 = kreator.makeMCComponent("GJet_Pt_15To6000","/GJet_Pt-15To6000_TuneCUETP8M1-Flat_13TeV_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root",154500, useAAA=False) # 8M evt

# GJet_Pt_20to40_DoubleEMEnriched = kreator.makeMCComponent("GJet_Pt_20to40_DoubleEMEnriched", "/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM",  "CMS", ".*root", 137751, useAAA=False)   # 24M 

# GJet_Pt_40toInf_DoubleEMEnriched = kreator.makeMCComponent("GJet_Pt_40toInf_DoubleEMEnriched", "/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 16792, useAAA=True)  # 70M

# GJet_Pt_20toInf_DoubleEMEnriched = kreator.makeMCComponent("GJet_Pt_20toInf_DoubleEMEnriched","/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM",  "CMS", ".*root",154500, useAAA=True)  # 38M


# # DY HT bins:
# #https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#DY_Z
# DYJetsToLL_M50_HT100to200 = kreator.makeMCComponent("DYJetsToLL_M50_HT100to200", "/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",139.4*1.23)
# DYJetsToLL_M50_HT200to400 = kreator.makeMCComponent("DYJetsToLL_M50_HT200to400", "/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",42.75*1.23)
# DYJetsToLL_M50_HT400to600 = kreator.makeMCComponent("DYJetsToLL_M50_HT400to600", "/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",5.497*1.23)
# DYJetsToLL_M50_HT600toInf = kreator.makeMCComponent("DYJetsToLL_M50_HT600toInf", "/DYJetsToLL_M-50_HT-600toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",2.21*1.23)

# # cross-section:
# # https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
# #https://twiki.cern.ch/twiki/bin/viewauth/CMS/HowToGenXSecAnalyzer
# # DY inclusive, NLO RunIISpring16MiniAODv2 
# DYJetsToLL_M50 = kreator.makeMCComponent("DYJetsToLL_M50", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 1921.8*3, useAAA=False) 
# # 28M, x-sec recalculated using FEWZ using z_m50_nnlo_inclusive_NNPDF30_nlo_as_0118 QCD NNLO, QED NLO, including ISR, no FSR (because xsec reduction due to FSR is coming from the M50 mass cut)
# DYJetsToLL_M50_Ext = kreator.makeMCComponent("DYJetsToLL_M50_Ext", "/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext4-v1/MINIAODSIM", "CMS", ".*root", 1921.8*3)  #the "ext4" set with 129M evts 

# DYJetsToLL_M50_PtZ100 = kreator.makeMCComponent("DYJetsToLL_M50_PtZ100", "/DYJetsToLL_M-50_PtZ-100_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 86.82550)# 1.2M ~ 78M at M50  # NLO -> NNLO : 8.947e+01 * 1921.8*3/5.941e+03, where 8.947e+01 is calculated using GenXSecAnalyzer 

# DYJetsToLL_M50_MGMLM_PtZ150 = kreator.makeMCComponent("DYJetsToLL_M50_MGMLM_PtZ150", "/DYJetsToLL_M-50_Zpt-150toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 86.82550)# this xsec is wrong, need recalculate.

 

# DYJetsToLL_M50_MGMLM = kreator.makeMCComponent("DYJetsToLL_M50_MGMLM","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv1-PUFlat0to50_80X_mcRun2_asymptotic_2016_v3-v1/MINIAODSIM", "CMS", ".*root", 1921.8*3) # 9M

# DYJetsToLL_M50_MGMLM_Ext1 = kreator.makeMCComponent("DYJetsToLL_M50_MGMLM_Ext1","/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM", "CMS", ".*root", 1921.8*3) # 50M

# DY1JetsToLL_M50_MGMLM = kreator.makeMCComponent("DY1JetsToLL_M50_MGMLM","/DY1JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 1016.0) 
# DY2JetsToLL_M50_MGMLM = kreator.makeMCComponent("DY2JetsToLL_M50_MGMLM","/DY2JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 331.4) 
# DY3JetsToLL_M50_MGMLM = kreator.makeMCComponent("DY3JetsToLL_M50_MGMLM","/DY3JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 96.36) 
# DY4JetsToLL_M50_MGMLM = kreator.makeMCComponent("DY4JetsToLL_M50_MGMLM","/DY4JetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 51.4) 
# DYBJetsToLL_M50_MGMLM = kreator.makeMCComponent("DYBJetsToLL_M50_MGMLM","/DYBJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 88.2771) 

# # W+Jets
# WJetsToLNu = kreator.makeMCComponent("WJetsToLNu","/WJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 3* 20508.9)

# ### DiBosons

# # cross section from https://twiki.cern.ch/twiki/bin/view/CMS/SummaryTable1G25ns#Diboson
# WW = kreator.makeMCComponent("WW", "/WW_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 118.7)
# WZ = kreator.makeMCComponent("WZ", "/WZ_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 47.13,useAAA=False )
# ZZ = kreator.makeMCComponent("ZZ", "/ZZ_TuneCUETP8M1_13TeV-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root", 16.523 )

# ZZTo2L2Nu = kreator.makeMCComponent("ZZTo2L2Nu", "/ZZTo2L2Nu_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 0.564) # 226 files, 8.8M evts, 208GB
# ZZTo4L = kreator.makeMCComponent("ZZTo4L", "/ZZTo4L_13TeV_powheg_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 1.212,useAAA=True) #  6.7M evts
# ZZTo2L2Q = kreator.makeMCComponent("ZZTo2L2Q", "/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 3.22) # 8.6M.
# WWTo2L2Nu = kreator.makeMCComponent("WWTo2L2Nu", "/WWTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 12.178) #1.9M evts
# WWToLNuQQ = kreator.makeMCComponent("WWToLNuQQ", "/WWToLNuQQ_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 49.997) # 1.9M evts
# WWToLNuQQ_Ext1 = kreator.makeMCComponent("WWToLNuQQ_Ext1", "/WWToLNuQQ_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM", "CMS", ".*root", 49.997) # 1.9M evts
# WZTo1L1Nu2Q = kreator.makeMCComponent("WZTo1L1Nu2Q", "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 10.71) # 19.7M
# WZTo2L2Q = kreator.makeMCComponent("WZTo2L2Q", "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 5.595) # 25M
# WZTo3LNu = kreator.makeMCComponent("WZTo3LNu", "/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 4.42965) # 2M
# WZTo3LNu_AMCNLO = kreator.makeMCComponent("WZTo3LNu_AMCNLO", "/WZTo3LNu_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS",  ".*root", 5.26,useAAA=True ) # 12.5M NLO up to 1 jet in ME
# ### top

# TT = kreator.makeMCComponent("TT", "/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12_ext3-v1/MINIAODSIM", "CMS", ".*root", 831.76) # 98M, it is ext3, there others more
# TTTo2L2Nu = kreator.makeMCComponent("TTTo2L2Nu", "/TTTo2L2Nu_13TeV-powheg/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0_ext1-v1/MINIAODSIM", "CMS", ".*root", 831.76*((3*0.108)**2) ) # 5M
# TTZToLLNuNu = kreator.makeMCComponent("TTZToLLNuNu", "/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 0.2529) # s
# TTWJetsToLNu = kreator.makeMCComponent("TTWJetsToLNu", "/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 0.2043) # 250k evt

# ### gamma+jets
# ### GJets (cross sections from McM) from DAS
# GJets_HT40to100 = kreator.makeMCComponent("GJets_HT40to100", "/GJets_HT-40To100_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v2/MINIAODSIM", "CMS", ".*root",23080) #4M
# GJets_HT100to200 = kreator.makeMCComponent("GJets_HT100to200", "/GJets_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",9110) # 5 M
# GJets_HT200to400 = kreator.makeMCComponent("GJets_HT200to400", "/GJets_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",2298) # 10M 
# GJets_HT400to600 = kreator.makeMCComponent("GJets_HT400to600", "/GJets_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",273.) # 2.4M
# GJets_HT600toInf = kreator.makeMCComponent("GJets_HT600toInf", "/GJets_HT-600ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIIFall15MiniAODv2-PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/MINIAODSIM", "CMS", ".*root",94.5) # 2.45M

# ### ggZZ
# ggZZTo2e2nu = kreator.makeMCComponent("ggZZTo2e2nu", "/GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 0.00319 )  
# # xsec from McM : https://cms-pdmv.cern.ch/mcm/requests?prepid=HIG-RunIIWinter15pLHE-00083&page=0&shown=4063359
# ggZZTo2mu2nu = kreator.makeMCComponent("ggZZTo2mu2nu", "/GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8/RunIISpring16MiniAODv2-PUSpring16_80X_mcRun2_asymptotic_2016_miniAODv2_v0-v1/MINIAODSIM", "CMS", ".*root", 0.00319 )

# GJetsHT = [
# GJets_HT40to100,
# GJets_HT100to200,
# GJets_HT200to400,
# GJets_HT400to600,
# GJets_HT600toInf
# ]
  
