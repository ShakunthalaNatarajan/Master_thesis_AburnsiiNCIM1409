#!/usr/bin/env python
# coding: utf-8

# In[ ]:


### Shakunthala Natarajan ###
__usage__=  """
            This script helps in identifying gene duplications in Alternaria burnsii 
            from the pairwise synteny blocks file
            
            python3 Gene_duplications_synteny.py
            
            --in <the blocks file from pairwise synteny analysis using jcvi/McScan>
            --tmp <path to temporary folder including the folder name>
            --out <path to output folder including the folder name>
            --org <name of the organism against which pairwise synteny analysis of Aburnsii was performed>
            """
######### imports #########

import os,sys

##### end of imports #####

#function to obtain the list of gene IDs, that occur twice in the fungus that is compared against Alternaria burnsii NCIM 1409
def twicegenes(input_file,tmp_dir,destination,organism):
    gr=os.path.join(tmp_dir,organism+"Genedup_references")
    grnr=os.path.join(tmp_dir,organism+"Genedup_references_no_repeats")
    out_prefile=os.path.join(tmp_dir,"Aburnsii_gene_duplications_with"+organism)
    out_file=os.path.join(destination,"Aburnsii_gene_duplications_with"+"_"+organism+"_"+"no_gene_isoforms")
    with open (input_file,"r") as f:
        line=f.readlines()
        parts=[]
        for each in line:
            partsnew=each.strip().split("\t")
            parts.append(partsnew[1])
    with open (input_file,"r") as f1:
        with open (gr,"w") as out:
            line1=f1.readline()
            while line1:
                parts1=line1.strip().split("\t")
                i=parts.count(parts1[1])
                if i==2:
                    newlist=[]
                    if newlist.count(parts1[1])==0:
                        newlist.append(parts1[1])
                        out.write(str(parts1[1])+"\n")
                line1=f1.readline()            
    """
    to obtain the list of gene IDs that occur twice in the fungus that is compared against Alternaria burnsii NCIM 1409, 
    as a compiled list containing each of these IDs only once, as we need only gene duplications in A.burnsii and for
    this we need to know the list of those genes in the other fungus twice, but must be processed to obtain a list
    where each of them is present once in the grnr file
    """
    with open (gr,"r") as f4:
        with open (grnr,"w") as out4:
            line4=f4.readlines()
            empty=[]
            for each in line4:
                empty.append(each.strip().split())
            emptynew=[]
            for each in empty:
                if emptynew.count(each)==0:
                    emptynew.append(each)
                    out4.write(str(each).replace('[','').replace(']','').replace("'",'')+"\n")
    with open (input_file,"r") as f2:
        with open (grnr,"r") as f3:
            with open (out_prefile,"w") as out1:
                line2=f2.readline()
                line3=f3.readlines()
                parts3=[]
                for each in line3:
                    parts3.append(each.strip().split())
                while line2:
                    splits=line2.strip().split("\t")
                    for k in parts3:
                        if splits[1]==str(k).replace('[','').replace(']','').replace("'",''):
                            out1.write(str(splits[0])+"\t"+str(splits[1])+"\n")
                    line2=f2.readline()
    """
    to eliminate multiple isoforms or multiple transcripts of a gene from the gene duplications list to 
    get a final list
    """
    with open (out_prefile,"r") as f5:
        line5=f5.readline()
        parts5=[]
        while line5:
            splitone=line5.strip().split("\t")
            splittwo=splitone[0].strip().split(".")
            parts5.append(str(splittwo[0]).strip().split())
            line5=f5.readline()
    with open (out_prefile,"r") as f6:
        with open (out_file,"w") as out5:
            line6=f6.readline()
            while line6:
                split6one=line6.strip().split("\t")
                split6two=split6one[0].strip().split(".")
                for each in parts5:
                    if split6two[0]==str(each).replace('[','').replace(']','').replace("'",''):
                        if parts5.count(each)!=2:
                            out5.write(str(split6one[0])+"\t"+str(split6one[1])+"\n")
                line6=f6.readline()
#to get inputs from the user in the terminal
def main( arguments ):
    input_file = arguments[arguments.index('--in')+1] 
    tmp_dir=arguments[arguments.index('--tmp')+1]
    destination = arguments[arguments.index('--out')+1]
    organism = arguments[arguments.index('--org')+1]
    if not os.path.exists( destination):
        os.makedirs(destination)
    if not os.path.exists( tmp_dir):
        os.makedirs(tmp_dir)
    
    twicegenes(input_file,tmp_dir,destination,organism)
    
#check for all mandatory arguments from terminal, if mandatory arguments are missing display  usage instructions
if '--in' in sys.argv and '--out' in sys.argv and '--tmp' in sys.argv and '--org' in sys.argv:
    main(sys.argv)
else:
    sys.exit(__usage__)

