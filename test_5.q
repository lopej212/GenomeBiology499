#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N TEST_Manuel
#$ -cwd
#$ -o test_manuel_5.log
#$ -j y
#$ -t 1-5:1

python slicer_feature_5.py $SGE_TASK_ID
