from CMGTools.BPH4L.analyzers.core.AutoFillTreeProducer  import * 
import math


QuadType =  NTupleObjectType("QuadType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("vtxProb",   lambda x : x.vtxProb, float),
    NTupleVariable("vtxChi2",   lambda x : x.vtxChi2, float),
    NTupleVariable("l1_index",  lambda x : x.leg1.index, int),
    NTupleVariable("l2_index",  lambda x : x.leg2.index, int),
    NTupleVariable("l3_index",  lambda x : x.leg3.index, int),
    NTupleVariable("l4_index",  lambda x : x.leg4.index, int),  
])

DuoType = NTupleObjectType("DuoType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("vtxProb",   lambda x : x.vtxProb, float),
    NTupleVariable("vtxChi2",   lambda x : x.vtxChi2, float),
    NTupleVariable("fitMass",   lambda x : x.fitMass, float),
    NTupleVariable("fitMassErr2",   lambda x : x.fitMassErr2, float),
    NTupleVariable("l1_index",  lambda x : x.leg1.index, int),
    NTupleVariable("l2_index",  lambda x : x.leg2.index, int),
    NTupleVariable("deltaPhi",  lambda x : x.deltaPhi(), float),       
    NTupleVariable("deltaR",    lambda x : x.deltaR(), float),
    #NTupleVariable("mt",   lambda x : x.mt(), float),       
])

MuFourType =  NTupleObjectType("VVType", baseObjectTypes=[], variables = [
    NTupleSubObject("quad",  lambda x : x['quad'], QuadType),
    NTupleSubObject("1a",  lambda x : x['pair1'][0], DuoType),
    NTupleSubObject("1b",  lambda x : x['pair1'][1], DuoType),
    NTupleSubObject("2a",  lambda x : x['pair2'][0], DuoType),
    NTupleSubObject("2b",  lambda x : x['pair2'][1], DuoType),
])


leptonTypeHZZLite = NTupleObjectType("leptonHZZLite", baseObjectTypes = [ particleType ], variables = [
    NTupleVariable("charge",   lambda x : x.charge(), int),
    NTupleVariable("index",    lambda x : x.index, int),  
    # ----------------------
    NTupleVariable("softMuonId",  lambda x : x.muonID("POG_ID_Soft") if abs(x.pdgId())==13 else 1, int, help="Muon POG Soft id, 1 for electrons"),
    NTupleVariable("tightId",     lambda x : x.tightId(), int, help="POG Tight ID (for electrons it's configured in the analyzer)"),
    NTupleVariable("looseId",     lambda x : x.looseId(), int, help="POG Loose ID"),
    # ----------------------
    NTupleVariable("dxy",   lambda x : x.dxy(), help="d_{xy} with respect to PV, in cm (with sign)"),
    NTupleVariable("dz",    lambda x : x.dz() , help="d_{z} with respect to PV, in cm (with sign)"),
    NTupleVariable("edxy",  lambda x : x.edB(), help="#sigma(d_{xy}) with respect to PV, in cm"),
    NTupleVariable("edz",   lambda x : x.edz(), help="#sigma(d_{z}) with respect to PV, in cm"),
    NTupleVariable("ip3d",  lambda x : x.ip3D() , help="d_{3d} with respect to PV, in cm (absolute value)"),
    NTupleVariable("sip3d",  lambda x : x.sip3D(), help="S_{ip3d} with respect to PV (significance)"),
    # ----------------------
    NTupleVariable("ptErr",   lambda x : x.ptErr(), help="Lepton p_{T} error"),
    NTupleVariable("lostHits",    lambda x : (x.gsfTrack() if abs(x.pdgId())==11 else x.innerTrack()).hitPattern().numberOfLostHits(ROOT.reco.HitPattern.MISSING_INNER_HITS), int, help="Number of lost hits on inner track"),
    NTupleVariable("trackerLayers", lambda x : (x.track() if abs(x.pdgId())==13 else x.gsfTrack()).hitPattern().trackerLayersWithMeasurement(), int, help="Tracker Layers"),
    NTupleVariable("pixelLayers", lambda x : (x.track() if abs(x.pdgId())==13 else x.gsfTrack()).hitPattern().pixelLayersWithMeasurement(), int, help="Pixel Layers"),
    ## FIXME: commented out for muon study only:
    # NTupleVariable("etaSc", lambda x : x.superCluster().eta() if abs(x.pdgId())==11 else -100, help="Electron supercluster pseudorapidity"),
    # NTupleVariable("isGap", lambda x : x.isGap() if abs(x.pdgId())==11 else False, int, help="is this a Gap electron"),
    # NTupleVariable("r9",   lambda x : x.r9() if abs(x.pdgId())==11 else 1.0, help="electron r9"),
    # NTupleVariable("convVeto",    lambda x : x.passConversionVeto() if abs(x.pdgId())==11 else 1, int, help="Conversion veto (always true for muons)"),
    # NTupleVariable("mvaIdSpring15",   lambda lepton : lepton.mvaRun2("NonTrigSpring15MiniAOD") if abs(lepton.pdgId()) == 11 else 1, help="EGamma POG MVA ID for non-triggering electrons, Spring15 re-training; 1 for muons"),
    # ----------------------
    #NTupleVariable("relIsoAfterFSR",    lambda x : x.relIsoAfterFSR,   help="RelIso after FSR"),
    NTupleVariable("chargedHadIso03",   lambda x : x.chargedHadronIsoR(0.3),   help="PF Abs Iso, R=0.3, charged hadrons only"),
    # ----------------------
    #NTupleVariable("hasOwnFSR",  lambda x : len(x.ownFsrPhotons), int),
    #NTupleSubObject("p4WithFSR", lambda x : x.p4WithFSR(), fourVectorType),
    # ----------------------
    NTupleVariable("mcMatchId",  lambda x : getattr(x, 'mcMatchId', -99), int, mcOnly=True, help="Match to source from hard scatter (pdgId of heaviest particle in chain, 25 for H, 6 for t, 23/24 for W/Z), zero if non-prompt or fake"),
    NTupleVariable("mcMatchAny", lambda x : getattr(x, 'mcMatchAny', -99), int, mcOnly=True, help="Match to any final state leptons: 0 if unmatched, 1 if light flavour (including prompt), 4 if charm, 5 if bottom"),
    NTupleVariable("mcPt",   lambda x : x.mcLep.pt() if getattr(x,"mcLep",None) else 0., mcOnly=True, help="p_{T} of associated gen lepton"),
    NTupleVariable("mcPt1",   lambda x : x.mcMatchAny_gp.pt() if getattr(x,"mcMatchAny_gp",None) else 0., mcOnly=True, help="p_{T} of associated gen lepton (status 1)"),
    # ----------------------
    NTupleVariable("hlt1L", lambda x : getattr(x,'matchedTrgObj1El',None) != None or  getattr(x,'matchedTrgObj1Mu',None) != None, int, help="Matched to single lepton trigger"),
])

bph4lVtxType = NTupleObjectType("bph4lVtxType", baseObjectTypes=[], variables = [
    NTupleVariable("chi2",  lambda x : x.Chi2(), help="chi2 of fitted vertex"),
    NTupleVariable("ndof",  lambda x : x.NDF(), help="n degrees of freedom for chi2 test of fitted vertex"),
    NTupleVariable("prob",  lambda x : x.Prob(), help="chi2 probability of fitted vertex"),
    NTupleVariable("nchi2", lambda x : x.NChi2(), help="normalized chi2 of fitted vertex"),
    NTupleVariable("ctau",  lambda x : x.ctau(), help="lifetime ctau (wrt PV) of fitted vertex"),
    NTupleVariable("cosAlpha",  lambda x : x.cosAlpha(), help="angle between Lxy(PV, fit vtx) and Mll(Jpsi or other diObj resonance)"),
])


ZTypeLite = NTupleObjectType("ZTypeLite", baseObjectTypes=[fourVectorType], variables = [
    #NTupleVariable("hasFSR",   lambda x : x.hasFSR(), int),
    NTupleSubObject("l1",  lambda x : x.leg1,leptonTypeHZZLite),
    NTupleSubObject("l2",  lambda x : x.leg2,leptonTypeHZZLite),
    NTupleSubObject("vtx",  lambda x : x.vtx, bph4lVtxType),
    NTupleVariable("mll",  lambda x : (x.leg1.p4() + x.leg2.p4()).M(), help="Dilepton mass, without FSR"),
])

ZZType = NTupleObjectType("ZZType", baseObjectTypes=[fourVectorType], variables = [
    NTupleVariable("hasFSR",   lambda x : x.hasFSR(), int),
    NTupleSubObject("z1",  lambda x : x.leg1, ZTypeLite),
    NTupleSubObject("z2",  lambda x : x.leg2, ZTypeLite),
    NTupleVariable("mll_12",   lambda x : (x.leg1.leg1.p4()+x.leg1.leg2.p4()).M()),
    NTupleVariable("mll_13",   lambda x : (x.leg1.leg1.p4()+x.leg2.leg1.p4()).M()),
    NTupleVariable("mll_14",   lambda x : (x.leg1.leg1.p4()+x.leg2.leg2.p4()).M()),
    NTupleVariable("mll_23",   lambda x : (x.leg1.leg2.p4()+x.leg2.leg1.p4()).M()),
    NTupleVariable("mll_24",   lambda x : (x.leg1.leg2.p4()+x.leg2.leg2.p4()).M()),
    NTupleVariable("mll_34", lambda x : (x.leg2.leg1.p4()+x.leg2.leg2.p4()).M()),
])
    
#****
#**** Below are from XZZ2l2v
#****

LLType = NTupleObjectType("LLType", baseObjectTypes=[fourVectorType], variables = [
    #NTupleVariable("TuneP_usage",   lambda x : x.useTuneP, int), 
    #NTupleVariable("TuneP_pt",   lambda x : x.TuneP_pt(), float),               
    #NTupleVariable("TuneP_eta",   lambda x : x.TuneP_eta(), float),               
    #NTupleVariable("TuneP_phi",   lambda x : x.TuneP_phi(), float),               
    #NTupleVariable("TuneP_mass",   lambda x : x.TuneP_m(), float),               
    NTupleVariable("mt",   lambda x : x.mt(), float),       
    NTupleVariable("deltaPhi",   lambda x : x.deltaPhi(), float),       
    NTupleVariable("deltaR",   lambda x : x.deltaR(), float),       
    #NTupleVariable("TuneP_mt",   lambda x : x.TuneP_mt(), float),       
    #NTupleVariable("TuneP_deltaPhi",   lambda x : x.TuneP_deltaPhi(), float),       
    #NTupleVariable("TuneP_deltaR",   lambda x : x.TuneP_deltaR(), float),       
])


VVType = NTupleObjectType("VVType", baseObjectTypes=[], variables = [
  #NTupleSubObject("LV",  lambda x : x['pair'],fourVectorType),
  #NTupleVariable("TuneP_LV_pt",   lambda x : x['pair'].TuneP_pt(), float),       
  #NTupleVariable("TuneP_LV_eta",   lambda x : x['pair'].TuneP_eta(), float),       
  #NTupleVariable("TuneP_LV_phi",   lambda x : x['pair'].TuneP_phi(), float),       
  #NTupleVariable("TuneP_LV_mass",   lambda x : x['pair'].TuneP_m(), float),       
  NTupleVariable("deltaPhi",   lambda x : x['pair'].deltaPhi(), float),       
  #NTupleVariable("TuneP_deltaPhi",   lambda x : x['pair'].TuneP_deltaPhi(), float), 
  NTupleVariable("deltaR",   lambda x : x['pair'].deltaR(), float),       
  #NTupleVariable("TuneP_deltaR",   lambda x : x['pair'].TuneP_deltaR(), float),       
  NTupleVariable("mt",   lambda x : x['pair'].mt(), float),       
  #NTupleVariable("TuneP_mt",   lambda x : x['pair'].TuneP_mt(), float),       
])


LLNuNuType = NTupleObjectType("LLNuNuType", baseObjectTypes=[VVType], variables = [
    NTupleSubObject("l1",  lambda x : x['pair'].leg1,LLType),
    NTupleSubObject("l1_l1",  lambda x : x['pair'].leg1.leg1,leptonTypeExtra),
    NTupleSubObject("l1_l2",  lambda x : x['pair'].leg1.leg2,leptonTypeExtra),
    NTupleSubObject("l2",  lambda x : x['pair'].leg2,metType),
    #NTupleVariable("CosdphiZMet",   lambda x : math.cos(x['pair'].deltaPhi()), float), 
    #NTupleVariable("CosZdeltaPhi",   lambda x : math.cos(x['pair'].leg1.deltaPhi()), float), 
    #NTupleVariable("dPTPara",   lambda x : (x['pair'].leg1.pt() + x['pair'].leg2.pt() * math.cos(x['pair'].deltaPhi())), float), 
    #NTupleVariable("dPTParaRel",   lambda x : (x['pair'].leg1.pt() + x['pair'].leg2.pt() * math.cos(x['pair'].deltaPhi()))/(x['pair'].leg1.pt()), float), 
    #NTupleVariable("dPTPerp",   lambda x : (x['pair'].leg2.pt() * math.sin(x['pair'].deltaPhi())), float), 
    #NTupleVariable("dPTPerpRel",   lambda x : (x['pair'].leg2.pt() * math.sin(x['pair'].deltaPhi()))/(x['pair'].leg1.pt()), float), 
    #NTupleVariable("metOvSqSET",   lambda x : (x['pair'].leg2.pt())/math.sqrt(x['pair'].leg2.sumEt()), float), 
])

PhotonJetType = NTupleObjectType("PhotonJetType", baseObjectTypes=[], variables = [
    NTupleVariable("deltaPhi",   lambda x : x['pair'].deltaPhi(), float),
    NTupleVariable("mt",   lambda x : x['pair'].mt(), float),
    NTupleSubObject("l1",  lambda x : x['pair'].leg1,photonType),
    NTupleSubObject("l2",  lambda x : x['pair'].leg2,metType),
    NTupleVariable("CosDeltaPhi",   lambda x : math.cos(x['pair'].deltaPhi()), float),
    NTupleVariable("dPTPara",   lambda x : (x['pair'].leg1.pt() + x['pair'].leg2.pt() * math.cos(x['pair'].deltaPhi())), float),
    NTupleVariable("dPTParaRel",   lambda x : (x['pair'].leg1.pt() + x['pair'].leg2.pt() * math.cos(x['pair'].deltaPhi()))/(x['pair'].leg1.pt()), float),
    NTupleVariable("dPTPerp",   lambda x : (x['pair'].leg2.pt() * math.sin(x['pair'].deltaPhi())), float),
    NTupleVariable("dPTPerpRel",   lambda x : (x['pair'].leg2.pt() * math.sin(x['pair'].deltaPhi()))/(x['pair'].leg1.pt()), float),
    NTupleVariable("metOvSqSET",   lambda x : (x['pair'].leg2.pt())/math.sqrt(x['pair'].leg2.sumEt()), float),
])


llpairType = NTupleObjectType("llpairType", baseObjectTypes=[], variables = [
    NTupleSubObject("Z",  lambda x : x,LLType),
    NTupleSubObject("l1",  lambda x : x.leg1,leptonType),
    NTupleSubObject("l2",  lambda x : x.leg2,leptonType),
])

metCompType = NTupleObjectType("metCompType", baseObjectTypes=[], variables = [
    NTupleVariable("Px",  lambda x : x[0]),
    NTupleVariable("Py",  lambda x : x[1]),
    NTupleVariable("Et",  lambda x : x[2]),
])

jet4metType = NTupleObjectType("jet4metType", baseObjectTypes=[], variables = [
    NTupleSubObject("rawP4forT1",  lambda x : x["rawP4forT1"], metCompType),
    NTupleSubObject("type1METCorr",  lambda x : x["type1METCorr"], metCompType),
    NTupleSubObject("corrP4forT1",  lambda x : x["corrP4forT1"], metCompType),
])

JetType = NTupleObjectType("xzzJetType", baseObjectTypes=[jetType], variables = [
    NTupleVariable("id",    lambda x : x.jetID("POG_PFID") , int, mcOnly=False,help="POG Loose jet ID"),
    NTupleVariable("area",   lambda x : x.jetArea(), help="Catchment area of jet"),
    NTupleVariable("rawFactor",   lambda x : x.rawFactor(), float, help="pt/rawfactor will give you the raw pt"),
    #NTupleVariable("corr_jer",  lambda x : getattr(x, 'corrJER', -99), float, mcOnly=True, help="JER corr factor"),
    NTupleVariable("btagCSV",   lambda x : x.btag('pfCombinedInclusiveSecondaryVertexV2BJetTags'), help="CSV-IVF v2 discriminator"),
    NTupleVariable("btagCMVA",  lambda x : x.btag('pfCombinedMVABJetTags'), help="CMVA discriminator"),
    NTupleVariable("mcPt",   lambda x : x.matchedGenJet.pt() if getattr(x,"matchedGenJet",None) else 0., mcOnly=True, help="p_{T} of associated gen jet"),
    NTupleVariable("mcEta",   lambda x : x.matchedGenJet.eta() if getattr(x,"matchedGenJet",None) else 0., mcOnly=True, help="eta of associated gen jet"),
    NTupleVariable("mcPhi",   lambda x : x.matchedGenJet.phi() if getattr(x,"matchedGenJet",None) else 0., mcOnly=True, help="phi of associated gen jet"),
    NTupleVariable("mcMass",   lambda x : x.matchedGenJet.mass() if getattr(x,"matchedGenJet",None) else 0., mcOnly=True, help="mass of associated gen jet"),
    NTupleVariable("mcFlavour", lambda x : x.partonFlavour(), int,     mcOnly=True, help="parton flavour (physics definition, i.e. including b's from shower)"),
    #NTupleVariable("btag",   lambda x : x.bTag(), float),
    #NTupleVariable("nConstituents",   lambda x : len(x.constituents), int),
    #NTupleVariable("looseID",   lambda x : x.looseID, int),
    #NTupleVariable("tightID",   lambda x : x.tightID, int),
    NTupleVariable("chargedHadronEnergyFraction",   lambda x : x.chargedHadronEnergyFraction(), float,  help="for Jet ID"),
    NTupleVariable("neutralHadronEnergyFraction",   lambda x : x.neutralHadronEnergyFraction(), float, help="for Jet ID"),
    NTupleVariable("neutralEmEnergyFraction",   lambda x : x.neutralEmEnergyFraction(), float, help="for Jet ID"),
    NTupleVariable("muonEnergyFraction",   lambda x : x.muonEnergyFraction(), float, help="for Jet ID"),
    NTupleVariable("chargedEmEnergyFraction",   lambda x : x.chargedEmEnergyFraction(), float, help="for Jet ID"),
    NTupleVariable("chargedHadronMultiplicity",   lambda x : x.chargedHadronMultiplicity(), float, help="for Jet ID"),
    NTupleVariable("chargedMultiplicity",   lambda x : x.chargedMultiplicity(), float, help="for Jet ID"),
    NTupleVariable("neutralMultiplicity",   lambda x : x.neutralMultiplicity(), float, help="for Jet ID"),
])

JetTypeExtra = NTupleObjectType("xzzJetTypeExtra", baseObjectTypes=[JetType], variables = [
    NTupleVariable("photonEnergyFraction",   lambda x : x.photonEnergyFraction(), float,),
    NTupleVariable("HFHadronEnergyFraction",   lambda x : x.HFHadronEnergyFraction(), float,),
    NTupleVariable("HFEMEnergyFraction",   lambda x : x.HFEMEnergyFraction(), float),
    NTupleVariable("electronEnergyFraction",   lambda x : x.electronEnergyFraction(), float),
])

