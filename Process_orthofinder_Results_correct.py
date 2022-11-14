#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#script to read and write all header lines from Aburnsii.pep.fasta into a new file
with open ("/home/shlaakuntha/Downloads/project/Aburnsii.pep.fasta","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_headers","w") as out:
        line=f.readline()
        while line:
            if line[0]==">":
                out.write(line.strip('>'))
            line=f.readline()
#script to extract Aburnsii genes list containing column as a flattened list to a new file
with open ("/home/shlaakuntha/Downloads/project/Orthogroups.tsv","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_orthogroups","w") as out:
        i=int(input("Enter the column number you want to extract as flattened list"))
        f.readline()
        line=f.readline()
        data=[]
        while line:
            parts=line.strip().split("\t")
            if len(parts)<(i+1):
                pass
            else:
                linenew=parts[i]
                if len(linenew)>0:
                    if ',' in linenew:
                        newline=linenew.strip().split(',')
                        for each in newline:
                            if len(each)>0:
                                out.write(each+"\n")
                    else:
                        out.write(linenew+"\n")
            line=f.readline()
"""
Correct script to compare the gene ids in Aburnsii orthogroups file and the gene ids in Aburnsii_headers file and 
write the gene ids that are present in Aburnsii headers but not in Aburnsii orthogroups to a file named
Aburnsii_unique_genes
"""
with open ("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_headers","r") as f1:
    with open("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_orthogroups",'r')as f2:
        with open ("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_unique_genes","w")as out:
            line1=f1.readlines()
            line2=f2.readlines()
            parts1=[]
            parts2=[]
            for each1 in line1:
                parts1.append(each1.strip().split())
            for each2 in line2:
                parts2.append(each2.strip().split())
            for element in parts1:
                if element not in parts2:
                    out.write(str(element).replace('[','').replace(']','').replace("'",'')+"\n")
                

