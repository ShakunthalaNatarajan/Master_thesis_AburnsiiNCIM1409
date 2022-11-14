#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tabulate


# In[14]:


#script to give the statistics of gene predictions from braker
from tabulate import tabulate
with open ("/home/shlaakuntha/Downloads/Aburnsii.cds.fasta","r") as f:
     with open ("/home/shlaakuntha/Downloads/alternaria_stats.txt","w") as out:
        line=f.readline()
        seq=0
        cum_len=0
        while line:
#to count the number of genes in the fasta file
            if line[0]==">":
                seq+=1
#to count the total number of bases in the fasta file(all non > lines in this file are single lines without breaks)
            elif line[0]!=">":
                cum_len+=len(line)
            line=f.readline()
#to calculate the average gene size
        avg_gene=int(cum_len/seq)
#function to return the length of the longest gene sequence in the fasta file
        def large_gene (file_name):
            with open (file_name,"r") as f1:
                ln=f1.readlines()
                ln_max=max(ln,key=len)
                max_gene=len(ln_max)
                return max_gene
#function call
        long_gene=large_gene("/home/shlaakuntha/Downloads/Aburnsii.cds.fasta")
#defining data column contents for the table
        data=[[str(seq), str(cum_len), str(avg_gene),str(long_gene)]]
#defining headers for the table columns
        col_names=["No. of predicted genes", "Total number of bases (bp)", "Average gene size (bp)","Size of longest gene (bp)"]
#writing the table into the output file  
        out.write(tabulate(data,headers=col_names,tablefmt="fancy_grid"))


# In[ ]:




