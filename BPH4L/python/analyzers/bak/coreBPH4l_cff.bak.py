import os
import PhysicsTools.HeppyCore.framework.config as cfg

from PhysicsTools.Heppy.analyzers.core.all import * # SkimAnalyzerCount, pileupAna and JsonAna
from PhysicsTools.Heppy.analyzers.objects.all import *  
from PhysicsTools.Heppy.analyzers.gen.all import * # GeneratorAnalyzer
from PhysicsTools.HeppyCore.utils.deltar import *

from CMGTools.BPH4L.analyzers.core.BPH4lTriggerBitFilter import *

from CMGTools.BPH4L.analyzers.Skimmer import *
from CMGTools.BPH4L.analyzers.BPH4lLepCombMaker import *
from CMGTools.BPH4L.analyzers.PackedCandidateLoader import *
#from CMGTools.BPH4L.analyzers.BPH4lMultiFinalState  import *
#from CMGTools.BPH4L.analyzers.BPH4lMultTrgEff import *
#from CMGTools.BPH4L.tools.leptonID  import *
#from CMGTools.BPH4L.analyzers.BPH4lGenAnalyzer import *
from CMGTools.BPH4L.analyzers.BPH4lLeptonAnalyzer import *
from CMGTools.BPH4L.analyzers.BPH4lVertexAnalyzer import *
#from CMGTools.BPH4L.analyzers.BPH4lMETAnalyzer import *
from CMGTools.BPH4L.analyzers.BPH4lDumpEvtList import *
from CMGTools.BPH4L.analyzers.BPH4lJetAnalyzer import *
#from CMGTools.BPH4L.analyzers.BPH4lPhotonAnalyzer import *
from CMGTools.BPH4L.analyzers.bph4l_Tree import *

from CMGTools.BPH4L.samples.triggers_13TeV_Spring16 import *

###########################
# define analyzers
###########################

skimAnalyzer = cfg.Analyzer(
    SkimAnalyzerCount, name='skimAnalyzerCount',
    useLumiBlocks = False,
    )

# Apply json file (if the dataset has one)
# which will filter evts according to the Json
jsonAna = cfg.Analyzer(
    JSONAnalyzer, name="JSONAnalyzer",
    debug="yes",
    )

# Filter using the 'triggers' and 'vetoTriggers' specified in the dataset
triggerAna = cfg.Analyzer(
    BPH4lTriggerBitFilter, name="TriggerBitFilter",
    )

# This analyzer actually does the pile-up reweighting (generic)
pileUpAna = cfg.Analyzer(
    PileUpAnalyzer, name="PileUpAnalyzer",
    true = True,  # use number of true interactions for reweighting
    makeHists=False
    )


# ## Gen Info Analyzer 
# genAna = cfg.Analyzer(
#     BPH4lGenAnalyzer, name="BPH4lGenAnalyzer",
#     # Print out debug information
#     verbose = False,
#     filter = "None",
#     )

# Gen Info Analyzer (generic):
genAna = cfg.Analyzer(
    GeneratorAnalyzer, name="GeneratorAnalyzer",
    # BSM particles that can appear with status <= 2 and should be kept
    stableBSMParticleIds = [], #[ 1000022 ],
    # Particles of which we want to save the pre-FSR momentum (a la status 3).
    # Note that for quarks and gluons the post-FSR doesn't make sense,
    # so those should always be in the list
    savePreFSRParticleIds = [], #[ 1,2,3,4,5, 11,12,13,14,15,16, 21 ],
    # Make also the list of all genParticles, for other analyzers to handle
    makeAllGenParticles = True,
    # Make also the splitted lists
    makeSplittedGenLists = True,
    allGenTaus = False,
    # Save LHE weights from LHEEventProduct
    makeLHEweights = True,
    # Print out debug information
    verbose = False,
)

# Select a list of good primary vertices (generic)
vertexAna = cfg.Analyzer(
    BPH4lVertexAnalyzer, name="VertexAnalyzer",
    allVertices = "offlineSlimmedPrimaryVertices",
    vertexWeight = None,
    fixedWeight = 1,
    verbose = False
    )

lepAna = cfg.Analyzer(
    BPH4lLeptonAnalyzer, name="leptonAnalyzer",
    muons='slimmedMuons',
    electrons='slimmedElectrons',
    packedCandidates = 'packedPFCandidates',
    muonUseTuneP = False,
    rhoMuon= 'fixedGridRhoFastjetCentralNeutral',
    rhoElectronMiniIso = 'fixedGridRhoFastjetCentralNeutral',
    rhoElectronPfIso = 'fixedGridRhoFastjetAll',
    #applyIso = False,
    applyID = True,
    do_filter=False,
    electronIDVersion = 'looseID', # can be looseID or HEEPv6
    electronIsoVersion = 'pfISO', # can be pfISO or miniISO
    mu_isoCorr = "rhoArea" ,
    ele_isoCorr = "rhoArea" ,
    mu_effectiveAreas = "Spring15_25ns_v1",
    ele_effectiveAreas = "Spring15_25ns_v1",
    miniIsolationPUCorr = None, # Allowed options: 'rhoArea' (EAs for 03 cone scaled by R^2), 'deltaBeta', 
                                     # 'raw' (uncorrected), 'weights' (delta beta weights; not validated)
                                     # Choose None to just use the individual object's PU correction
    # doMuonScaleCorrections = ( 'Kalman', {
    #     'MC': 'MC_80X_13TeV',
    #     'Data': 'DATA_80X_13TeV',
    #     'isSync': False,
    #     'smearMode': 'ebe'
    # }),
    doMuonScaleCorrections = None,
    # doElectronScaleCorrections = {
    #     'data' : 'EgammaAnalysis/ElectronTools/data/ScalesSmearings/80X_ichepV1_2016_ele',
    #     'GBRForest': ('$CMSSW_BASE/src/CMGTools/BPH4L/data/GBRForest_data_ICHEP16_combined.root',
    #                   'gedelectron_p4combination_25ns'),
    #     'isSync': False
    # },
    doElectronScaleCorrections = None,
    )

# ## Photon Analyzer (generic)
# photonAna = cfg.Analyzer(
#     BPH4lPhotonAnalyzer, name='photonAnalyzer',
#     photons='slimmedPhotons',
#     ptMin = 15,
#     etaMax = 2.5,
#     doPhotonScaleCorrections=False,
#     gammaID = "POG_SPRING15_25ns_Loose",
#     rhoPhoton = 'fixedGridRhoFastjetAll',
#     gamma_isoCorr = 'rhoArea',
#     doFootprintRemovedIsolation = True,
#     packedCandidates = 'packedPFCandidates',
#     footprintRemovedIsolationPUCorr = 'rhoArea',
#     conversionSafe_eleVeto = True,
#     do_mc_match = True,
#     do_randomCone = False,
# )


## Jets Analyzer (generic)
jetAna = cfg.Analyzer(
    BPH4lJetAnalyzer, name='jetAnalyzer',
    debug=False,
    jetCol = 'slimmedJets',
    copyJetsByValue = True,      #Whether or not to copy the input jets or to work with references (should be 'True' if JetAnalyzer is run more than once)
    genJetCol = 'slimmedGenJets',
    rho = ('fixedGridRhoFastjetAll','',''), # it was ('fixedGridRhoFastjetAll','','') 
    jetPt = 0., # default used to be 25.
    jetEta = 6.0,  #4.7,
    jetEtaCentral = 2.4,
    jetLepDR = 0.4,
    jetLepArbitration = (lambda jet,lepton : lepton), # you can decide which to keep in case of overlaps; e.g. if the jet is b-tagged you might want to keep the jet
    cleanSelectedLeptons = True, #Whether to clean 'selectedLeptons' after disambiguation. Treat with care (= 'False') if running Jetanalyzer more than once
    minLepPt = 10,
    relaxJetId = False,
    doPuId = False, # Not commissioned in 7.0.X
    recalibrateJets = False, #'MC', # True, False, 'MC', 'Data'
    applyL2L3Residual = False, # Switch to 'Data' when they will become available for Data
    recalibrationType = "AK4PFchs",
    mcGT     = "Spring16_25nsV6_MC", # txt file pattern used in 74X: 'Summer15_25nsV6_MC'
    dataGT   = "Spring16_25nsV6_DATA", #Summer15_25nsV6_DATA
    mcGT_jer    = "Spring16_25nsV6_MC", 
    dataGT_jer  = "Spring16_25nsV6_DATA", 
    jecPath = "${CMSSW_BASE}/src/CMGTools/BPH4L/data/jec2016/", #${CMSSW_BASE}/src/CMGTools/RootTools/data/jec/
    jerPath = "${CMSSW_BASE}/src/CMGTools/BPH4L/data/jer2016/", #${CMSSW_BASE}/src/CMGTools/RootTools/data/jec/
    shiftJEC = 0, # set to +1 or -1 to apply +/-1 sigma shift to the nominal jet energies
    addJECShifts = False, # if true, add  "corr", "corrJECUp", and "corrJECDown" for each jet (requires uncertainties to be available!)
    smearJets = False,
    shiftJER = 0, # set to +1 or -1 to get +/-1 sigma shifts  
    alwaysCleanPhotons = False,
    cleanGenJetsFromPhoton = False,
    cleanJetsFromFirstPhoton = False,
    cleanJetsFromTaus = False,
    cleanJetsFromIsoTracks = False,
    doQG = False,
    do_mc_match = False,
    collectionPostFix = "",
    calculateSeparateCorrections = False, # should be True if recalibrateJets is True, otherwise L1s will be inconsistent
    calculateType1METCorrection  = False,
    type1METParams = { 'jetPtThreshold':15., 'skipEMfractionThreshold':0.9, 'skipMuons':True }, # numbers for AK4CHS jets
    )

# metAna = cfg.Analyzer(
#     BPH4lMETAnalyzer, name="metAnalyzer",
#     metCollection     = "slimmedMETs",
#     noPUMetCollection = "slimmedMETs",
#     copyMETsByValue = False,
#     doTkMet = False,
#     doMetNoPU = False,
#     doMetNoMu = False,
#     doMetNoEle = False,
#     doMetNoPhoton = False,
#     recalibrate = False, # or "type1", or True, or False
#     doMetShiftFromJEC = False, # only works with recalibrate on
#     applyJetSmearing = False, # not change the final met used in multiStateAna, does nothing unless the jet smearing turned on in jetAna for MC, copy self.met for data
#     old74XMiniAODs = False, # set to True to get the correct Raw MET when running on old 74X MiniAODs
#     jetAnalyzerPostFix = "",
#     candidates='packedPFCandidates',
#     candidatesTypes='std::vector<pat::PackedCandidate>',
#     dzMax = 0.1,
#     collectionPostFix = "",
#     )

## MET Analyzer (generic):
metAna = cfg.Analyzer(
    METAnalyzer, name="metAnalyzer",
    metCollection     = "slimmedMETs",
    noPUMetCollection = "slimmedMETs",    
    copyMETsByValue = False,
    doTkMet = False,
    doMetNoPU = False,
    doMetNoMu = False,
    doMetNoEle = False,
    doMetNoPhoton = False,
    recalibrate = False, #"type1", # or "type1", or True
    applyJetSmearing = False, # does nothing unless the jet smearing is turned on in the jet analyzer
    old74XMiniAODs = False, # set to True to get the correct Raw MET when running on old 74X MiniAODs
    jetAnalyzerPostFix = "",
    candidates='packedPFCandidates',
    candidatesTypes='std::vector<pat::PackedCandidate>',
    dzMax = 0.1,
    collectionPostFix = "",
    )


lepCombAna = cfg.Analyzer(
    BPH4lLepCombMaker,
    name='lepCombMaker',
    do_filter = False,
    selectMuMuPair = (lambda x: (x.leg1.highPtID or x.leg2.highPtID) and ((x.leg1.pt()>50.0 and abs(x.leg1.eta())<2.1) or (x.leg2.pt()>50.0 and abs(x.leg2.eta())<2.1))),
    selectElElPair = (lambda x: x.leg1.pt()>115.0 or x.leg2.pt()>115.0 ),
    selectVBoson = (lambda x: x.pt()>100.0 and x.mass()>60.0 and x.mass()<120.0),
    doElMu = False, # it would save events with ElMu final states + LL final stats
    selectElMuPair = (lambda x: (x.leg1.pt()>115.0) or (x.leg2.highPtID and x.leg2.pt()>50.0 and abs(x.leg2.eta())<2.1)), # be sure to have leg1=e, leg2=mu
    selectFakeBoson = (lambda x: x.pt()>100.0 and x.mass()>30.0 and x.mass()<150.0),
    )

packedAna = cfg.Analyzer(
    PackedCandidateLoader,
    name = 'PackedCandidateLoader',
    select=lambda x: x.pt()<13000.0
    )

# multiStateAna = cfg.Analyzer(
#     BPH4lMultiFinalState,
#     name='MultiFinalStateMaker',
#     processTypes = ["LLNuNu"], # can include "LLNuNu", "ElMuNuNu", "PhotonJets" 
#     selectPairLLNuNu = (lambda x: x.leg1.pt()>20.0 and x.leg1.mass()>60.0 and x.leg1.mass()<180.0 and x.leg2.pt()>0.0),
#     selectPairElMuNuNu = (lambda x: x.leg1.pt()>20.0 and x.leg1.mass()>30.0 and x.leg1.mass()<300.0 and x.leg2.pt()>0.0),
#     selectPhotonJets = (lambda x: x.leg1.pt()>20.0 and x.leg2.pt()>50.0),
#     suffix = '',
#     )

# Create flags for MET filter bits
"""followed by the MET filters recommendations from
https://twiki.cern.ch/twiki/bin/view/CMS/MissingETOptionalFiltersRun2#MiniAOD_76X_v2_produced_with_the"""
eventFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="EventFlags",
    processName = 'PAT',
    fallbackProcessName = 'RECO',
    outprefix   = 'Flag',
    triggerBits = {
        "HBHENoiseFilter" : [ "Flag_HBHENoiseFilter" ],
        "HBHENoiseIsoFilter" : [ "Flag_HBHENoiseIsoFilter" ],
        #"CSCTightHaloFilter" : [ "Flag_CSCTightHaloFilter" ],
        "CSCTightHalo2015Filter" : [ "Flag_CSCTightHalo2015Filter" ],
        #"hcalLaserEventFilter" : [ "Flag_hcalLaserEventFilter" ],
        "EcalDeadCellTriggerPrimitiveFilter" : [ "Flag_EcalDeadCellTriggerPrimitiveFilter" ],
        "goodVertices" : [ "Flag_goodVertices" ],
        #"trackingFailureFilter" : [ "Flag_trackingFailureFilter" ],
        "eeBadScFilter" : [ "Flag_eeBadScFilter" ],
        # "ecalLaserCorrFilter" : [ "Flag_ecalLaserCorrFilter" ],
        # "trkPOGFilters" : [ "Flag_trkPOGFilters" ],
        # "trkPOG_manystripclus53X" : [ "Flag_trkPOG_manystripclus53X" ],
        # "trkPOG_toomanystripclus53X" : [ "Flag_trkPOG_toomanystripclus53X" ],
        # "trkPOG_logErrorTooManyClusters" : [ "Flag_trkPOG_logErrorTooManyClusters" ],
        "globalTightHalo2016Filter" : [ "Flag_globalTightHalo2016Filter" ],
        "METFilters" : [ "Flag_METFilters" ],
    }
    )

# Create flags for trigger bits
triggerFlagsAna = cfg.Analyzer(
    TriggerBitAnalyzer, name="TriggerFlags",
    processName = 'HLT',
    triggerBits = {
        # Onia
        "jpsi2mu" : triggers_jpsi2mu,
        "upsilon2mu" : triggers_upsilon2mu,
        # Triples
        "3mu" : triggers_3mu,
    }
    )

dumpEvents = cfg.Analyzer(
    BPH4lDumpEvtList, name="BPH4lDumpEvtList",
    )

vvSkimmer = cfg.Analyzer(
    Skimmer,
    name='vvSkimmer',
    #required = ['LLNuNu', 'ElMuNuNu']
    required = ['LLNuNu']
)

leptonSkimmer = cfg.Analyzer(
    Skimmer,
    name='leptonSkimmer',
    required = ['inclusiveLeptons']
)


###########################
# Core sequence of all common modules
###########################

bph4lPreSequence = [
    skimAnalyzer,
    jsonAna,
    triggerAna,
]

bph4lObjSequence = [
    genAna,
    pileUpAna,
    vertexAna,
    lepAna,
    jetAna,
    metAna,
    #eventFlagsAna, # for MET
    triggerFlagsAna,
]

bph4lCoreSequence = bph4lPreSequence + bph4lObjSequence + [   
    lepCombAna,
    #multiStateAna,
    #leptonSkimmer,
    MuonTreeProducer,
    #packedAna,
]

###################




