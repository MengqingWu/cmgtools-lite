#!/usr/bin/env python

import optparse, os, sys
from ROOT import *


lumi=6.26



parser = optparse.OptionParser()
parser.add_option("-i","--input_tag",dest="intag", default='pileup_DATA_80x',help="input file tag")
parser.add_option("-o","--output_tag",dest="outtag", default='pileup_MC_80x',help="output files tag")
(options,args)=parser.parse_args()

gROOT.SetBatch(True)
gROOT.ProcessLine('.x tdrstyle.C')

#2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU
# https://github.com/cms-sw/cmssw/blob/CMSSW_8_0_10/SimGeneral/MixingModule/python/mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi.py

if (True): 

    intag = options.intag
    outtag = options.outtag

    pdf = [ 	0.000829312873542,
 		0.00124276120498,
 		0.00339329181587,
 		0.00408224735376,
 		0.00383036590008,
		0.00659159288946,
 		0.00816022734493,
 		0.00943640833116,
 		0.0137777376066,
 		0.017059392038,
 		0.0213193035468,
 		0.0247343174676,
 		0.0280848773878,
 		0.0323308476564,
 		0.0370394341409,
 		0.0456917721191,
 		0.0558762890594,
 		0.0576956187107,
 		0.0625325287017,
 		0.0591603758776,
 		0.0656650815128,
 		0.0678329011676,
 		0.0625142146389,
 		0.0548068448797,
 		0.0503893295063,
 		0.040209818868,
 		0.0374446988111,
 		0.0299661572042,
 		0.0272024759921,
 		0.0219328403791,
 		0.0179586571619,
 		0.0142926728247,
 		0.00839941654725,
 		0.00522366397213,
 		0.00224457976761,
 		0.000779274977993,
 		0.000197066585944,
 		7.16031761328e-05,
 		0.0,
		0.0,
		0.0,
		0.0,
		0.0,
		0.0,
		0.0,
		0.0,
		0.0,
 		0.0,
 		0.0,
		0.0]


    fdt=TFile(intag+'.root')
    pileup_dt = fdt.Get('pileup')
    nbins = pileup_dt.GetXaxis().GetNbins()
    xmin = pileup_dt.GetXaxis().GetBinLowEdge(1)
    xmax = pileup_dt.GetXaxis().GetBinUpEdge(nbins)
    pileup_dt.Scale(1.0/pileup_dt.Integral())
    fmc=TFile(outtag+'.root','recreate')
    pileup_mc=TH1F('pileup','pileup',nbins,xmin,xmax)
    pileup_mc.Sumw2()
    for i in range(nbins):
        if i< len(pdf): pileup_mc.SetBinContent(i+1,pdf[i])
        else: pileup_mc.SetBinContent(i+1, 0.0)

    pileup_mc.Scale(1.0/pileup_mc.Integral())
    gStyle.SetStatStyle(0)
    pileup_dt.SetStats(0)
    pileup_mc.SetStats(0)

    c1 = TCanvas("c1","c1",600,600)
    c1.SetLeftMargin(0.15)
    c1.SetBottomMargin(0.15)

    pileup_dt.SetLineColor(kRed)
    pileup_dt.SetMarkerColor(kRed)
    pileup_dt.SetMarkerStyle(20)
    pileup_dt.GetXaxis().SetTitle('N pileup')
    pileup_dt.GetYaxis().SetTitle('Norm.')
    pileup_mc.SetLineColor(kBlue)
    pileup_mc.SetMarkerColor(kBlue)
    pileup_mc.SetMarkerStyle(20)
    pileup_mc.SetLineWidth(2)
    pileup_mc.GetXaxis().SetTitle('N pileup')
    pileup_mc.GetYaxis().SetTitle('Norm.')

    pileup_mc.GetYaxis().SetTitleOffset(1.5)
    pileup_dt.GetYaxis().SetTitleOffset(1.5)
    lg = TLegend(0.6,0.7,0.85,0.85)
    lg.AddEntry(pileup_dt, "Data", "pl")
    lg.AddEntry(pileup_mc, "MC", "pl")

    pt = TPaveText(0.1577181,0.9562937,0.9580537,0.9947552,"brNDC")
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(42)
    pt.SetTextSize(0.03)
    text = pt.AddText(0.15,0.3,"CMS Preliminary")
    text = pt.AddText(0.55,0.3,"#sqrt{s} = 13 TeV, 2016, L = "+"{:.3}".format(float(lumi))+" fb^{-1}")


    pileup_dt.GetXaxis().SetRangeUser(0,50)
    pileup_mc.GetXaxis().SetRangeUser(0,50)
    pileup_dt.Draw()
    pileup_mc.Draw("HIST,SAME")
    lg.Draw("same")
    pt.Draw()
    c1.SaveAs(outtag+"_pileup80x.eps")
    c1.SaveAs(outtag+"_pileup80x.pdf")


    # ratio
    puweight = pileup_dt.Clone("puweight")
    puweight.Divide(pileup_mc)
    puweight.GetXaxis().SetRangeUser(0,80)
    puweight.GetYaxis().SetTitle("PU Weight")
    lg1 = TLegend(0.36,0.7,0.85,0.85)
    lg1.AddEntry(puweight, "Data/MC 2016 ", "pl")

    c2 = TCanvas("c2","c2",600,600)
    c2.SetLeftMargin(0.15)
    c2.SetBottomMargin(0.15)
    puweight.Draw()
    lg1.Draw()
    pt.Draw()
    c2.SaveAs(outtag+"_puweight80x.eps")
    c2.SaveAs(outtag+"_puweight80x.pdf")

    # print ratio 
    puwts = [puweight.GetBinContent(i+1) for i in range(50)]
    print puwts

    pileup_dt.Write('pileup_dt')
    pileup_mc.Write('pileup_mc')
    pileup_mc.Write('pileup')
    puweight.Write('puweight_dtmc')
    puweight.Write('puweight')
    fmc.Close()

#if __name__ == "__main__":
#    makePURatio()


