#!/bin/bash
echo Splitting fasta files
./split_fasta_5.sh
sleep 5s
./split_fasta_c.sh
sleep 5s
echo Submitting jobs to SGE
./submit_5.sh
sleep 2s
./submit_c.sh
echo Sleeping for 30 seconds to wait for the SGE to finish 
sleep 5s
qstat
sleep 30s
echo Merging files
./merge_files_5.sh
sleep 4s
./merge_files_c.sh
sleep 4s
echo Calling quick_svm script
./call_quick_svm.sh
