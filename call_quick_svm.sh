#!/bin/bash

export R_LIBS=$R_LIBS:/local/cluster/R_Packages/3.3

class1Examples=5UTR_feat_table.all.txt
class2Examples=c_feat_table.all.txt

Rscript quick_svm.R $class1Examples $class2Examples
