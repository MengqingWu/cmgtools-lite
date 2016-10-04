#!/bin/sh


# selection
metFlag="(Flag_eeBadScFilter==1&&Flag_goodVertices==1&&Flag_EcalDeadCellTriggerPrimitiveFilter==1&&Flag_CSCTightHalo2015Filter==1&&Flag_HBHENoiseIsoFilter==1&&Flag_HBHENoiseFilter==1)"
#signalLep="((llnunu_l1_l1_highPtID==1&&abs(llnunu_l1_l1_pdgId)==13&&llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.1&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)||(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))"
#subLep="((abs(llnunu_l1_l1_pdgId)==13&&llnunu_l1_l1_pt>20&&abs(llnunu_l1_l1_eta)<2.4&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)||(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>35&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))"
signalLep="((abs(llnunu_l1_l1_pdgId)==13&&(llnunu_l1_l1_highPtID==1||llnunu_l1_l2_highPtID==1)&&((llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.1)||(llnunu_l1_l2_pt>50&&abs(llnunu_l1_l2_eta)<2.1)))||(abs(llnunu_l1_l1_pdgId)==11&&((llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5)||(llnunu_l1_l2_pt>115&&abs(llnunu_l1_l2_eta)<2.5))))"

zzPair="(nllnunu>0)"
zWindow="(abs(llnunu_l1_mass-91.1876)<20.0)"
zptCut="(llnunu_l1_pt>100.0)"
metCut="(llnunu_l2_pt>0.0)"

selection="(1)"
#selection=$metFlag"&&"$zzPair"&&"$signalLep
#selection=$metFlag"&&"$zzPair"&&"$signalLep"&&"$zWindow
#selection=$metFlag"&&"$zzPair"&&"$signalLep"&&"$zWindow"&&"$zptCut

# compile
g++ skimming.cc -o skimming.exe `root-config --cflags` `root-config --libs` # no cuts used in .cc file

#inputs
#inputdir=/afs/cern.ch/work/m/mewu/public/76X
#inputdir=/Users/mengqing/work/local_xzz2l2nu/AnalysisRegion
inputdir=./METSkim_v1
outputdir=./METSkim_v4 #v2 has bcd of all bkg, v3 has only zjets corr, #4 with 2d zjets corr
mkdir -p ${outputdir}

n=0

#for infile in $inputdir/*V3MetShiftBeforeJetNewSelV6NoMetLepAnyWayAllJetsBigSig1p4LepResSigProtect*.root ;
for infile in $inputdir/*.root ; 
do
  echo "+++ skimming $infile +++"

  outfile="${outputdir}/${infile/$inputdir\//}"
  # outfile="${outfile/_V4_doJetsCorrUseLepResPtErrSel8JetLepSigProtectV2MetShift/}"
  # outfile="${outfile/ZJetsReso/}"
  # outfile="${outfile/_ZPt/}"

  echo -- Input file: $infile
  echo -- Output file: $outfile
  echo -- Selection: $selection
  
  echo "Start at " $(date)
  ./skimming.exe $infile $outfile $selection
  echo "End at " $(date)
  n=$(( n + 1 ))

  #if [ "$n" -gt "0" ]; then break; fi
  
done
echo '[Info]' $n 'files processed in total.'
