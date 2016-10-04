#!/bin/sh


# selection
metFlag="(Flag_eeBadScFilter==1&&Flag_goodVertices==1&&Flag_EcalDeadCellTriggerPrimitiveFilter==1&&Flag_CSCTightHalo2015Filter==1&&Flag_HBHENoiseIsoFilter==1&&Flag_HBHENoiseFilter==1)"
#signalLep="((llnunu_l1_l1_highPtID==1&&abs(llnunu_l1_l1_pdgId)==13&&llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.1&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)||(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))"
llsubLep="((abs(llnunu_l1_l1_pdgId)==13&&llnunu_l1_l1_pt>20&&abs(llnunu_l1_l1_eta)<2.4&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)||(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>35&&abs(llnunu_l1_l1_eta)<2.5&&llnunu_l1_l2_pt>35&&abs(llnunu_l1_l2_eta)<2.5))"
llsignalLep="((abs(llnunu_l1_l1_pdgId)==13&&(llnunu_l1_l1_highPtID==1||llnunu_l1_l2_highPtID==1)&&((llnunu_l1_l1_pt>50&&abs(llnunu_l1_l1_eta)<2.1)||(llnunu_l1_l2_pt>50&&abs(llnunu_l1_l2_eta)<2.1)))||(abs(llnunu_l1_l1_pdgId)==11&&((llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5)||(llnunu_l1_l2_pt>115&&abs(llnunu_l1_l2_eta)<2.5))))"

emusubLep="(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>35&&abs(llnunu_l1_l1_eta)<2.5)&&(abs(llnunu_l1_l2_pdgId)==13&&llnunu_l1_l2_pt>20&&abs(llnunu_l1_l2_eta)<2.4)"
emusignalLep="(abs(llnunu_l1_l1_pdgId)==11&&llnunu_l1_l1_pt>115&&abs(llnunu_l1_l1_eta)<2.5)&&(abs(llnunu_l1_l2_pdgId)==13&&llnunu_l1_l2_pt>50&&abs(llnunu_l1_l2_eta)<2.1)"

zzPair="nllnunu>0"
emuPair="nelmununu>0"
zWindow="(abs(llnunu_l1_mass-91.1876)<20.0)"
zptCut="(llnunu_l1_pt>100.0)"
metCut="(llnunu_l2_pt>0.0)"

selection="(1)"
#selection="("zzPair"&&"llsubLep"&&"llsignalLep")||("emuPair"&&"emusubLep"&&"emusignalLep")"
#selection=$metFlag"&&"$subLep"&&"$signalLep"&&"$zzPair"&&"$zWindow
#selection=$metFlag"&&"$subLep"&&"$zzPair"&&"$zWindow

# compile
g++ skimming_fast.cc -o skimming.exe `root-config --cflags` `root-config --libs`

#inputs
#inputdir=/data/mewu/AnalysisRegion
inputdir=/dataf/mewu/LooseSkim_v2
#inputdir=/Users/mengqing/work/local_xzz2l2nu/AnalysisRegion
#inputdir=/dataf/mewu/nonResSkim_v1
outputdir=/dataf/mewu/nonResSkim_v1
mkdir -p ${outputdir}

n=0

if [ "$(ls -A $inputdir)" ]; then
    
    for infile in $inputdir/*.root ; do
	echo "+++ skimming $infile +++"
	
	outfile="${outputdir}/${infile/$inputdir\//}"
            #outfile="${outfile/\/fullTreeProducer\/tree/}"
	
	echo -- Input file: $infile
	echo -- Output file: $outfile
	echo -- Selection: $selection
	
	./skimming.exe $infile $outfile $selection
	
	n=$(( n + 1 ))
	#if [ "$n" -gt "0" ]; then  break; fi
    done
    
    echo '[Info]' $n 'files processed in total.'
    
else
    echo "$inputdir is Empty!"

fi