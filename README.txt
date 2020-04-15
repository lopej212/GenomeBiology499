BOTT499 Final Project Running STeps
1)run.sh

NOTE: The "run.sh" script takes care of everything from splitting the fasta files to running the quick_svm script.
If you want to RUN AGAIN, run the "clean.sh" script first, then run "run.sh" script again.
I have noticed that you will get an accuracy that moves around 0.97 (ex. 0.9705, 0.9702, 0.982, 0.9675, 0.9885). 

Alternative steps (manually running the scripts):
1)split_fasta_5.sh
2)split_fasta_c.sh
3)submit_5.sh
4)submit_c.sh
5)merge_files_5.sh
6)merge_files_c.sh
7)call_quick.svm.sh
