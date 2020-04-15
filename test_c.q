#!/bin/bash
#$ -S /bin/bash
#$ -V
#$ -N TEST_Manuel
#$ -cwd
#$ -o test_manuel_c.log
#$ -j y
#$ -t 1-5:1

python slicer_feature_c.py $SGE_TASK_ID
