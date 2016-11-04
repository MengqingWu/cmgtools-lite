#!/bin/sh                                                                                                                                                   
heppy_batch.py -o LSF run_bph4l_80x_cfg_dt.py -b 'bsub -q 8nh < ./batchScript.sh'
