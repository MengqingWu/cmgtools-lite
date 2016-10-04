#!/bin/sh

# selection
metFlag="(Flag_eeBadScFilter==1&&Flag_goodVertices==1&&Flag_EcalDeadCellTriggerPrimitiveFilter==1&&Flag_CSCTightHalo2015Filter==1&&Flag_HBHENoiseIsoFilter==1&&Flag_HBHENoiseFilter==1)"
#signalLep="((llnunu_l1_l1_highPtID==1&&abs(llnunu_l1_l1_pdgId)==13&&llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.4&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)||(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))"
subLep="((abs(llnunu_l1_l1_pdgId)==13&&llnunu_l1_l1_pt>20&&abs(llnunu_l1_l1_eta)<2.4&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)||(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>35&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))"
signalLep="((abs(llnunu_l1_l1_pdgId)==13&&(llnunu_l1_l1_highPtID==1||llnunu_l1_l2_highPtID==1)&&((llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.4)||(llnunu_l1_l2_pt>50&&abs(llnunu_l1_l2_eta)<2.4)))||(abs(llnunu_l1_l1_pdgId)==11&&((llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5)||(llnunu_l1_l2_pt>115&&abs(llnunu_l1_l2_eta)<2.5))))"

zzPair="(nllnunu>0)"
zWindow="(abs(llnunu_l1_mass-91.1876)<20.0)"
zptCut="(llnunu_l1_pt>100.0)"
metCut="(llnunu_l2_pt>0.0)"

#selection="(1)"
selection=$metFlag"&&"$subLep"&&"$signalLep
#selection=$metFlag"&&"$subLep"&&"$signalLep"&&"$zzPair"&&"$zWindow
#selection=$metFlag"&&"$subLep"&&"$zzPair"&&"$zWindow


# compile
g++ skimming_simple.cc -o skimming.exe `root-config --cflags` `root-config --libs`

#inputs
inputdir=./80X
outputdir=./test
#outputdir=/dataf/mewu/LooseSkim80X 
mkdir -p ${outputdir}

n=0
#/data/mewu/76X_v0.4/SingleElectron_Run2015C_25ns_16Dec/fullTreeProducer/tree.root for debugging
for infile in $inputdir/TTT*/fullTreeProducer/tree.root ;
do
  echo "+++ skimming $infile +++"
  outfile="${outputdir}/${infile/$inputdir\//}"
  outfile="${outfile/\/fullTreeProducer\/tree/}"

  inSkimFile=${infile/fullTreeProducer\/tree.root/skimAnalyzerCount\/SkimReport.txt}

  #echo $inSkimFile
  AllEvents=`grep "All Events" ${inSkimFile} | awk {'print $3'}`
  SumWeights=`grep "Sum Weights" ${inSkimFile} | awk {'print $3'}`

  if [ -z $AllEvents ]; then
    echo Fail to get All Events from file ${inSkimFile}
    continue
  fi
  if [ -z $SumWeights ]; then
    SumWeights=$AllEvents
  fi

  echo -- Input file: $infile
  echo -- Output file: $outfile
  echo -- AllEvents: $AllEvents , SumWeights: $SumWeights
  echo -- Selection: $selection

  echo "Start at " $(date)  
  ./skimming.exe $infile $outfile $AllEvents $SumWeights $selection 
  echo "End at " $(date)
  n=$(( n + 1 ))

  #if [ "$n" -gt "1" ]; then  break; fi

  # if [ "$n" -gt "4" ]; then
  #     wait
  #     n=0
  # fi

done
echo '[Info]' $n 'files processed in total.'
