#!/bin/bash

# created by Mengqing @Jan-20-2017
# command used to get the pileup distribution from data:
# check: https://twiki.cern.ch/twiki/bin/view/CMS/PileupJSONFileforData#Calculating_Your_Pileup_Distribu

pileupCalc.py -i /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON_MuonPhys.txt --inputLumiJSON /afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/PileUp/pileup_latest.txt --calcMode true --minBiasXsec 69200 --maxPileupBin 50 --numPileupBins 50 pileup_data.root | tee output.log