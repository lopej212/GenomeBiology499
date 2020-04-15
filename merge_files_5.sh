#!/bin/bash

####
# Takes an input directory name and an output file name as arguments
# Concatentaates the input files, but with only one header line at the top of the file.
# Assumes all input files have a one line header at the top of the file.
#

indir=feature_files_5
outfile=5UTR_feat_table.all.txt

./cat_dir_with_header.pl $indir $outfile
