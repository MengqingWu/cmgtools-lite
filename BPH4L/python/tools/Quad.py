import math
import ROOT
from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi

class Quad(object):
    def __init__(self,leg1, leg2, leg3, leg4):

        self.l1=ROOT.TLorentzVector()
        self.l1.SetPtEtaPhiM(leg1.pt(),leg1.eta(),leg1.phi(),leg1.mass())
        self.l2=ROOT.TLorentzVector()
        self.l2.SetPtEtaPhiM(leg2.p4().pt(),leg2.p4().eta(),leg2.p4().phi(),leg2.p4().mass())
        self.l3=ROOT.TLorentzVector()
        self.l3.SetPtEtaPhiM(leg3.p4().pt(),leg3.p4().eta(),leg3.p4().phi(),leg3.p4().mass())
        self.l4=ROOT.TLorentzVector()
        self.l4.SetPtEtaPhiM(leg4.p4().pt(),leg4.p4().eta(),leg4.p4().phi(),leg4.p4().mass())

        self.LV = self.l1 + self.l2 + self.l3 + self.l4

        self.leg1 = leg1
        self.leg2 = leg2
        self.leg3 = leg3
        self.leg4 = leg4

        #et1 = math.sqrt(self.l1.M()*self.l1.M()+self.l1.Pt()*self.l1.Pt())
        #et2 = math.sqrt(self.l1.M()*self.l1.M()+self.l2.Pt()*self.l2.Pt())
        #self.MT  =math.sqrt(self.l1.M()*self.l1.M()+self.l1.M()*self.l1.M()+2*(et1*et2-self.l1.Px()*self.l2.Px()-self.l1.Py()*self.l2.Py()))


    def rawP4(self):
        return self.l1+self.l2+self.l3+self.l4

    def p4(self):
        return self.LV
    
    def m(self):
        return self.LV.M()

    def mass(self):
        return self.LV.M()
    
    # def pdgId(self):
    #     return self.pdg
    
    def mt2(self):
        return self.Mt2()
        #return self.MT*self.MT

    def mt(self):
        return self.Mt()
        #return self.MT

    
    def pt(self):
        return self.LV.Pt()

    def px(self):
        return self.LV.Px()

    def py(self):
        return self.LV.Py()

    def pz(self):
        return self.LV.Pz()

    def eta(self):
        return self.LV.Eta()

    def rapidity(self):
        return self.LV.Rapidity()

    def phi(self):
        return ROOT.TVector2.Phi_mpi_pi(self.LV.Phi())

    # def AbsdeltaPhi(self):
    #     return abs(deltaPhi(self.l1.Phi(),self.l2.Phi()))

    # def AbsdeltaR(self):
    #     return abs(deltaR(self.l1.Eta(),self.l1.Phi(),self.l2.Eta(),self.l2.Phi()))

    # def deltaPhi(self):
    #     return deltaPhi(self.l1.Phi(),self.l2.Phi())

    # def deltaR(self):
    #     return deltaR(self.l1.Eta(),self.l1.Phi(),self.l2.Eta(),self.l2.Phi())

    def __getattr__(self, name):
        return getattr(self.LV,name)

