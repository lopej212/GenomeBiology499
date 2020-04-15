#!/bin/bash

#########
# infile: File of FASTA sequences to be split as evenly as possible
# nfiles: Number of files that should result

infile=coding_sequences.txt
nfiles=5

##########

scriptdir=scripts

outdir=$infile.dir
if [ -d $outdir ]
then
    rm -r $outdir
else
    mkdir $outdir
fi

orig=$infile.orig
mv $infile $orig

$scriptdir/fasta_multiline_to_fasta_singleseqs.pl $orig $infile
$scriptdir/split_fasta_singleseqs.pl $infile $outdir $nfiles
