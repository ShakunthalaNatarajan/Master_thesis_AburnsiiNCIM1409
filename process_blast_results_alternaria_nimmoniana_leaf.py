#!/usr/bin/env python
# coding: utf-8

# In[2]:


#PART 4
"""
 alternaria_nimmoniana_leaf_blast is the result file of blasting alternaria burnsii against Nothapodytes nimmoniana
 sequences. alternaria_nimmoniana_leaf_blast was input into blast2best.py script to obtain best hits per query sequence 
 and the result file is stored as alter_nimmoL_best
 Following is a script to search for gene ids in the alter_nimmoL_best file and max_bit_score_sorted file,
 and write the contents of the alter_campto_best file along with the maximum bit score values to a new file 
 called alter_nimmoL_with_filters
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_best",'r')as f:
    with open("/home/shlaakuntha/Downloads/project/max_bit_score_sorted",'r')as f1:
        with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_with_filters",'w')as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip("\t").split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[0]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+i[1]
                        out.write(str(linenew)+"\n")
                line=f.readline()
#PART 5
"""
script to filter out sequences based on percent identity, amino acid length, and normalized bit score and write
the contents to a new file called alter_nimmoL_top_hits
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_with_filters","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_top_hits","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            #threshold for pident=60; threshold for length=50. 
            #So all sequences having pident<60 and length<50 will be filtered out.
            if (float(parts[2])>60 and float(parts[3])>50 and (float(parts[11])/float(parts[12]))>0.3):
                out.write(line)
            line=f.readline()
#A. scripts with putative cpt candidate seqs from c. acuminata
#PART 6
""""
script to identify genes in the endophyte matching the CPT candidate genes in Nothapodytes nimmoniana in the
file alter_nimmoL_with_filters which basically has all the columns of alter_nimmoL_best and an
additional column containing the maximum bit score for each query sequence. The results are in a file
called alter_nimmoL_match
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_with_filters","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_match","w")as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+parts1[12]
                        out.write(str(linenew)+"\n")
                line=f.readline()
#PART 7
"""
script to identify genes in the endophyte matching the CPT candidate genes in Nothapodytes nimmoniana
from original alternaria_nimmoniana_leaf_blast file. Results are in alter_nimmoL_match_unfiltered
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alternaria_nimmoniana_leaf_blast","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_match_unfiltered","w")as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]
                        out.write(str(linenew)+"\n")
                line=f.readline()
#PART 8
"""
script to find cpt candidate genes of Nothapodytes nimmoniana in the alter_campto_top_hits file. 
This is to see if there are any top hits resembling the CPT candidate genes in Nothapodytes nimmoniana
"""
with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_top_hits","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_candidates_alternaria_nimmoL","w")as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+parts1[12]
                        out.write(str(linenew)+"\n")
                line=f.readline()
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_candidates_alternaria_nimmoL","r")as f2:
    lns=f2.readlines()
    parts3=[]
    for eachone in lns:
        parts3.append(eachone.strip("\t").split())
    if len(parts3)!=0:
        print("Wow the endophyte has some probable CPT genes in the top blast hit list derived from Nothapodytes nimmoniana!")
    else:
        print("Omg the endophyte has no genes in the top blast hit list matching the CPT candidate genes in Nothapodytes nimmoniana! \n Is it producing CPT independent of plant hosts?")
        
#B. scripts with CPT candidate seqs collected from literature as queries
#PART 6
"""
script to find the list of CPT  candidates in N. nimmoniana leaf.  Code below is to filter out sequences based 
on percent identity, amino acid length, and normalized bit score and write the contents to a new file called 
cpt_nimmoS_top_hits
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_probables_nimmoniana_leaf_blast","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_nimmoL_top_hits","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            #threshold for pident=60; threshold for length=50. 
            #So all sequences having pident<60 and length<50 will be filtered out.
            if (float(parts[2])>60 and float(parts[3])>50):
                out.write(line)
            line=f.readline()
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_nimmoL_top_hits","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes_v2","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            out.write(parts[1]+"\n")
            line=f.readline()
#PART 6
""""
script to identify genes in the endophyte matching the CPT candidate genes in Nothapodytes nimmoniana in the
file alter_nimmoL_with_filters which basically has all the columns of alter_nimmoL_best and an
additional column containing the maximum bit score for each query sequence. The results are in a file
called alter_nimmoL_match
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_with_filters","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes_v2",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_match_v2","w")as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+parts1[12]
                        out.write(str(linenew)+"\n")
                line=f.readline()
#PART 7
"""
script to identify genes in the endophyte matching the CPT candidate genes in Nothapodytes nimmoniana
from original alternaria_nimmoniana_leaf_blast file. Results are in alter_nimmoL_match_unfiltered
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alternaria_nimmoniana_leaf_blast","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes_v2",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_match_unfiltered_v2","w")as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]
                        out.write(str(linenew)+"\n")
                line=f.readline()
#PART 8
"""
script to find cpt candidate genes of Nothapodytes nimmoniana in the alter_campto_top_hits file. 
This is to see if there are any top hits resembling the CPT candidate genes in Nothapodytes nimmoniana
"""
with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/alter_nimmoL_top_hits","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes_v2",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_candidates_alternaria_nimmoL_v2","w")as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+parts1[12]
                        out.write(str(linenew)+"\n")
                line=f.readline()
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/cpt_candidates_alternaria_nimmoL_v2","r")as f2:
    lns=f2.readlines()
    parts3=[]
    for eachone in lns:
        parts3.append(eachone.strip("\t").split())
    if len(parts3)!=0:
        print("Second try succeeded! Wow the endophyte has some probable CPT genes in the top blast hit list derived from Nothapodytes nimmoniana!")
    else:
        print("Ah again! Probably there is no horizontal gene transfer.\n Omg the endophyte has no genes in the top blast hit list matching the CPT candidate genes in Nothapodytes nimmoniana! \n Is it producing CPT independent of plant hosts?")
        


# In[ ]:




