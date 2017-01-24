from CMGTools.BPH4L.analyzers.AutoFillTreeProducer  import * 
from CMGTools.BPH4L.analyzers.bph4lTypes  import * 
from CMGTools.BPH4L.analyzers.Skimmer  import * 
import PhysicsTools.HeppyCore.framework.config as cfg

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

MuonTreeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='MuonTreeProducer',
     vectorTree = True,
     saveTLorentzVectors = True,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     globalVariables = [
         NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"), 
         #NTupleVariable("triggersf",  lambda x : getattr(x,'trgsf',1), help="singleelectron/muon trigger sf"),
     ],
     globalObjects =  {
         #"met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, with 76X type 1 corrections"),
         #"met_miniAod" : NTupleObject("met", metType, help="PF E_{T}^{miss} stored in miniAOD"),
     },
     collections = {
         #"LL"  : NTupleCollection("Zll",LLType,5, help="Z to ll"),
         #"ElMu" : NTupleCollection("elmu",LLType,5, help="electron - muon pair for non-resonant bkg"),
         #"selectedLeptons" : NTupleCollection("lep",leptonTypeExtra, 10, help="selected leptons"),
         "selectedMuons" : NTupleCollection("mu", MuonType, 10, help="selected Muons"),
         "MuFour"        : NTupleCollection("mu4", MuFourType, 5, help="4-mu combination"),
         #"genLeptons" : NTupleCollection("genLep", genParticleType, 10, help="Generated leptons (e/mu) from W/Z decays"),
         "jets_raw"   : NTupleCollection("jet", jetType,15, help="all jets from miniAOD"),
     }
)

leptonTreeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='leptonTreeProducer',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
#     PDFWeights = PDFWeights,
#     globalVariables = susyMultilepton_globalVariables,
#     globalObjects = susyMultilepton_globalObjects,
     collections = {
            "genleps"          : NTupleCollection("gen",     genParticleWithLinksType, 10, help="Generated leptons (e/mu) from W/Z decays"),
            "inclusiveLeptons" : NTupleCollection("l",    leptonTypeExtra, 10, help="Inclusive Leptons"), 
     }
)


jetTreeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='jetTreeProducer',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     globalVariables = [
         NTupleVariable("nVert",  lambda ev: len(ev.goodVertices), int, help="Number of good vertices"), 
     ],
     globalObjects =  {
         "met" : NTupleObject("met", metType, help="PF E_{T}^{miss}, after full type 1 corrections"),
         "met_miniAod" : NTupleObject("met_raw", metType, help="PF E_{T}^{miss}, after type 1 corrections in miniAOD"),
         "met_JEC" : NTupleObject("met_JEC", metType, help="PF E_{T}^{miss}, after type 1 corrections with new 76X JEC added"),
         "met_JECUp" : NTupleObject("met_JECUp", metType, help="PF E_{T}^{miss}, after type 1 corrections with new 76X JEC up"),
         "met_JECDown" : NTupleObject("met_JECDown", metType, help="PF E_{T}^{miss}, after type 1 corrections with new 76X JEC down"),
         "met_JECJER" : NTupleObject("met_JECJER", metType, help="PF E_{T}^{miss}, after type 1 corrections with JEC+JER jets"),
         #"metNoJet" : NTupleObject("metNoJet", fourVectorType, help="PF E_{T}^{miss}, with out jet"),
         #"sumJetsInT1": NTupleObject("sumJetsInT1", jet4metType, help="sum of Delta(px, py, et) of jets used for type1METCorr"),
     },

     collections = {
         "selectedLeptons" : NTupleCollection("lep",leptonType,10, help="selected leptons"),
         "genLeptons" : NTupleCollection("genLep", genParticleType, 10, help="Generated leptons (e/mu) from W/Z decays"),
         "genZBosons" : NTupleCollection("genZ", genParticleType, 10, help="Generated V bosons"),
         "genLeptons" : NTupleCollection("genLep", genParticleType, 10, help="Generated leptons (e/mu) from W/Z decays"),
         "genZBosons" : NTupleCollection("genZ", genParticleType, 10, help="Generated V bosons"),
         "jets"  : NTupleCollection("jet_corr",JetType,15, help="all jets with new JEC for 76X applied"),
         "jets_raw"  : NTupleCollection("jet",JetType,15, help="all jets from miniAOD"),
     }
)
