################################# 
## Triggers for Run II: 2016data 
## BPH triggers: https://twiki.cern.ch/twiki/bin/view/CMS/BphTrigger
## - info from xzz2l2v:
##   Based on HLT_MC_SPRING15 and /frozen/2015/25ns14e33/v2.1/HLT/V1 and /frozen/2015/50ns_5e33/v2.1/HLT/V5
##   Names with _50ns are unprescaled at 50ns but prescaled at 25ns
##   Names with _run1 are for comparing Spring15 MC to 8 TeV data: they're the closest thing I could find to run1 triggers, they're prescaled or even excluded in data but should appear in MC.
#    https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_10/HLTrigger/Configuration/tables/GRun.txt

triggers_upsilon2mu = [ "HLT_Dimuon0_Upsilon_Muon_v*" ]
triggers_jpsi2mu = [ "HLT_Dimuon0_Jpsi_Muon_v*" ]
triggers_3mu  = [ "HLT_TripleMu_5_3_3_v*" ]

# triggers_upsilon2mu = [
#     "HLT_Dimuon0_Upsilon_Muon_v*",
#     "HLT_Dimuon13_Upsilon_v*",
#     "HLT_Dimuon8_Upsilon_Barrel_v*",
#     "HLT_Mu7p5_L2Mu2_Upsilon_v*",
#     "HLT_Mu7p5_Track2_Upsilon_v*",
#     "HLT_Mu7p5_Track3p5_Upsilon_v*",
#     "HLT_Mu7p5_Track7_Upsilon_v*",
# ]
# triggers_jpsi2mu = [
#     "HLT_Dimuon0er16_Jpsi_NoOS_NoVertexing_v*",
#     "HLT_Dimuon0er16_Jpsi_NoVertexing_v*",
#     "HLT_Dimuon10_Jpsi_Barrel_v*",
#     "HLT_Dimuon16_Jpsi_v*",
#     "HLT_Dimuon20_Jpsi_v*",
#     "HLT_Dimuon6_Jpsi_NoVertexing_v*",
#     "HLT_DoubleMu4_3_Jpsi_Displaced_v*",
#     "HLT_DoubleMu4_JpsiTrk_Displaced_v*",
#     "HLT_Mu7p5_L2Mu2_Jpsi_v*",
#     "HLT_Mu7p5_Track2_Jpsi_v*",
#     "HLT_Mu7p5_Track3p5_Jpsi_v*",
#     "HLT_Mu7p5_Track7_Jpsi_v*",
# ]
