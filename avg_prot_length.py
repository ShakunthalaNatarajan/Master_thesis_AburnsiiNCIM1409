#!/usr/bin/env python
# coding: utf-8

# In[ ]:


__usage__= """
           This script helps find the average peptide sequence length in a .pep.fasta file
           python3 avg_prot_length.py
           --in <path_to_.pep.fasta_file_including_the_file_name>
           --name <name_of_your_file_including_the_extension>
           
           """
######### imports #########

import os, sys

##### end of imports #####
def prot (file, Name):
    with open (file, 'r') as f:
        line=f.readline()
        seq=0
        cum_len=0
        while line:
            if line[0]==">":
                seq+=1
            #to count the total number of amino acids in the fasta file(all non > lines in this file are single lines without breaks)
            elif line[0]!=">":
                cum_len+=len(line)
            line=f.readline()
    #to calculate the average protein sequence length
    avg_prot=int(cum_len/seq)
    print("The average protein sequence length in your input fasta file","\t", Name, "\t","is","\t",avg_prot)    
#to get file name from the user in the terminal
def main( arguments ):
    file = arguments[arguments.index('--in')+1]
    Name= arguments[arguments.index('--name')+1]
    prot(file, Name)
#check for all mandatory arguments from terminal, if mandatory arguments are missing display  usage instructions
if '--in' in sys.argv and '--name' in sys.argv:
    main(sys.argv)
else:
    sys.exit(__usage__)

