
# X->J/psi+Y->2mu2l Analysis Package

Analysis package of BPH exotics search for X->Jpis+Y->2mu2l final states.
 
For 80X analysis.

For the general recipe to set up CMG Framework in CMSSW_8_0_X, [follow these instructions](https://twiki.cern.ch/twiki/bin/view/CMS/CMGToolsReleasesExperimental#CMGTools_lite_release_for_ICHEP).

## Basic setup (from the above link) is this:

#### Set up CMSSW and the base git

 CMGTools-lite release for ICHEP 2016 (CMSSW 8_0_19) 

```
cmsrel CMSSW_8_0_19
cd CMSSW_8_0_19/src
cmsenv
git cms-init
```

#### Add the central cmg-cmssw repository to get the Heppy 80X branch

```
git remote add cmg-central https://github.com/CERN-PH-CMG/cmg-cmssw.git -f  -t heppy_80X
```

#### Configure the sparse checkout, and get the base heppy packages

```
cp /afs/cern.ch/user/c/cmgtools/public/sparse-checkout_80X_heppy .git/info/sparse-checkout
git checkout -b heppy_80X cmg-central/heppy_80X
```

#### Add your mirror, and push the 80X branch to it

```
git remote add origin git@github.com:YOUR_GITHUB_REPOSITORY/cmg-cmssw.git
git push -u origin heppy_80X
```

#### Now get the CMGTools subsystem from the cmgtools-lite repository

```
git clone -o cmg-central https://github.com/CERN-PH-CMG/cmgtools-lite.git -b 80X CMGTools
cd CMGTools
```

#### Add your fork, and push the 80X branch to it

```
git remote add origin  git@github.com:YOUR_GITHUB_REPOSITORY/cmgtools-lite.git
git push -u origin 80X
```

#### Compile

```
cd $CMSSW_BASE/src
scram b -j 8
```


Instruction to run jobs 
---------------------------------
0. grid proxy init:
   
  Please always initialize your grid proxy for both locally run single job or on LSF for batch jobs in order to access reomote input datasets through AAA (xrootd) service:

  ```
  voms-proxy-init --voms cms --hours 172 --valid 172:00
  ```

1. run single job interactively

 Example configuration files are in cfg/ folder, e.g.
  
  ```
  heppy mc_test run_xzz2l2nu_80x_cfg_loose_mc.py
  ```
 this will run config file run_xzz2l2nu_80x_cfg_loose_mc.py and output to directory mc_test

 N.B. 
  There are many options to pass to the main function of Heppy,
  one useful example is to run few (e.g. 100) events test:
  ```
  heppy mc_test run_xzz2l2nu_80x_cfg_loose_mc.py -N 100
  ```
  you will have the first 100 events processed only.

2. run batch jobs on lsf

  Example scripts to submit lsf batch jobs are:
  ```
    cfg/loose_lsf_dt/sub_xzz2l2nu_80x_cfg_loose_dt.sh 
    cfg/loose_lsf_mc/sub_xzz2l2nu_80x_cfg_loose_mc.sh 
  ```
  for data and mc respectively.

  LSF jobs can only be submitted on lxplus, your local machine doesn't work. 

  One can then go to the output directory ('LSF/' in above example) to check the status:
  ```
   heppy_check.py *
  ```

  If you see some jobs are finished but not showing the results here, you can resub the jobs by running:
  ```
   heppy_check.py * -b 'bsub -q 8nh'
  ```
  which will resub the jobs with missing outputs.

  Once the jobs are all done, you can merge the outputs by running:
  ```
   heppy_hadd.py .
  ```
  this will collect all "Chunk"s of one sample and merge them into one folder.


