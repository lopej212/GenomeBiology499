"""
BOTT499 Final Project Spring 2018
File: Slicer_feature_C.py
Author: Jose Manuel Lopez Alcala
NOTE:This script is for the coding sequences
"""

from __future__ import division
import sys #This is for the argument from SGE number -
import os
import errno


file_number = sys.argv[1]
input_file_name = "coding_sequences.txt.dir/coding_sequences.txt." + str(file_number)
output_file_name = "feature_files_c/features_c." + str(file_number)
max_sequences = 1000

def gc_content(sequenceX, x):
    seq_count = 0
    gc_count = 0

    gc_count += sequenceX.count('G')
    #print "gc_count: " + str(gc_count) #for testing
    gc_count += sequenceX.count('C')
    #print "gc_count: " + str(gc_count )# for testing
    sequence_length = len(sequenceX)
    #print "sequence_length: " + str(sequence_length) # for testing

    gc_percent  = (gc_count/sequence_length) * 100

#print "Seq" + str(x) + " GC percent: " + str(gc_percent) # for testing

    return gc_percent


#This functino will return 1 if the sequence stars with ATG
#Zero otherwise
def starswith_atg(sequenceX,x):
    if sequenceX.startswith("ATG"):
        return 1
    return 0

#This function will return 1 if it ends with TAG, TAA, or TGA stops codons
#Zero other wise
def stop_codon(sequenceX,x):
    if sequenceX.endswith("TAG") or sequenceX.endswith("TAA") or sequenceX.endswith("TGA"):
        return 1
    return 0

#This function will return the length of the sequence
def length_of_sequence(sequenceX, x):
    return len(sequenceX)



def main():

    #Create a new directory for the file ouput
    if not os.path.exists(os.path.dirname(output_file_name)):
        try:
            os.makedirs(os.path.dirname(output_file_name))
        except OSError as exc: #guard against race condtion
            if exc.errno != errno.EEXIST:
                raise
    myfile = open(output_file_name,"w")
    myfile.write("Seq_id" + "\t" + "GC_percent" + "\t" + "Starts_ATG\t" + "Stop_Codon\t" + "Sequence_length\n")#original 
    myfile.close()


    running_string = ""
    sequences_count = 0
    writing_count = 0

    # This section of the code will open the FASTA files
    # and put all of the sequneces into a list
    with open(input_file_name, "r") as file:
        keep_reading= True
        while True:
            c = file.readline()
            #print "This is the c at the top: " + c #for testing
            if not c:
                #sequences_list.append(running_string.replace('\n', ''))
                running_string = running_string.replace('\n', '')
                #print "This is the line that was added to the list: \n" + running_string # for testing
                #print "End of Slicing"#for testing
                if  not running_string.startswith("S"):
                    writing_count += 1 #this number is the sequence nubmer of what is being written
                    #Run the analysis on the strings:
                    gc_cont = gc_content(running_string,writing_count)
                    atg_flag = starswith_atg(running_string,writing_count)
                    stop_codon_val = stop_codon(running_string,writing_count)
                    length_val = length_of_sequence(running_string,writing_count)
                    #
                    #
                    #
                    with open(output_file_name, "a") as output_file:
                        output_file.write("Seq" + str(writing_count) + "\t" + str(gc_cont) + "\t" +  str(atg_flag) + "\t" +
                        str(stop_codon_val)+ "\t" + str(length_val) + "\n") #Writing action
                break
            if c.startswith(">") or c.startswith("S"):
                sequences_count += 1
                #print "Sequences count: " + str(sequences_count) # for testing

                if sequences_count >= 2: # is this evaluates to true, it means that it has passed the first sequence
                    #print "Here" # for testing
                    #sequences_list.append(running_string.replace('\n', ''))
                    running_string = running_string.replace('\n', '')
                    #print "This is the line that was added to the list: \n" + running_string # for testing
                    if  not running_string.startswith("S"):
                        writing_count += 1 #this number is the sequence nubmer of what is being written
                        #Run the analysis on the strings:
                        gc_cont = gc_content(running_string,writing_count)
                        atg_flag = starswith_atg(running_string,writing_count)
                        stop_codon_val = stop_codon(running_string,writing_count)
                        length_val = length_of_sequence(running_string, writing_count)
                        #
                        #
                        #
                        #This is where the writing happens
                        with open(output_file_name, "a") as output_file:
                            output_file.write("Seq" + str(writing_count) + "\t" + str(gc_cont) + "\t" +  str(atg_flag) + "\t" +
                            str(stop_codon_val)+ "\t" + str(length_val) + "\n") #Writing action
                    running_string = ""

                if writing_count >= max_sequences:
                    break

                c = file.readline()
                #print "This is the c at the bottom: "  + c # for testing
            running_string += c
            #print running_string #for testing

    #print (''.join(sequences_list)) #for testing
    #print sequences_list# for testing
    #print sequences_list[0]#for testing
    print "End of Program"



main()
