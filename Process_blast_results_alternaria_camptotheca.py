#!/usr/bin/env python
# coding: utf-8

# In[2]:


#PART 1
#script to obtain sequences with 100% identity to themselves in self blast of Alternaria
#the corresponding bit score will be the max bit score for each of the sequence in the file
with open ("/home/shlaakuntha/Downloads/project/alternaria_blast_v2","r") as f:
    with open("/home/shlaakuntha/Downloads/project/max_bit_score","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            if parts[0]==parts[1]:
                out.write(line)
            line=f.readline()
#PART 2
#script to create and sort the max_bit_score file with seqids and max bit score columns alone
import operator
data=[]
def header_list (file_name):
    with open (file_name,"r") as f:
        line=f.readline()
        while line:
            parts=line.strip().split()
            data.append({'qseqid':parts[0],'bitscore':parts[11]})
            line=f.readline()
    return data
data_list=header_list("/home/shlaakuntha/Downloads/project/max_bit_score")
data_sorted=sorted(data_list,key=operator.itemgetter('qseqid'))
with open("/home/shlaakuntha/Downloads/project/seq_ids","w") as out1:
    for things in data_sorted:
        out1.write(things['qseqid']+"\n")
with open("/home/shlaakuntha/Downloads/project/bit_score","w") as out2:
    for things in data_sorted:
        out2.write(things['bitscore']+"\n")
#PART 3
#Correct script to merge the contents of two different files
with open ("/home/shlaakuntha/Downloads/project/seq_ids","r") as f1:
    with open ("/home/shlaakuntha/Downloads/project/bit_score","r") as f2:
        with open ("/home/shlaakuntha/Downloads/project/max_bit_score_sorted","w")as out3:
            line=f1.readline()
            while line:
                line=line.strip("\n")
                ln=f2.readline()
                if (len(ln)!=0):
                    lines=line+"\t"+ln
                    out3.write(lines)
                else:
                    out3.write("\n"+line+".")   
                line=f1.readline()
#PART 4
"""
 alternaria_camptotheca_blast is the result file of blasting alternaria burnsii against camptotheca acuminata 
 sequences alternaria_camptotheca_blast was input into blast2best.py script to obtain best hits per query sequence 
 and the result file is stored as alter_campto_best
 Following is a script to search for gene ids in the alter_campto_best file and max_bit_score_sorted file,
 and write the contents of the alter_campto_best file along with the maximum bit score values to a new file 
 called alter_campto_with_filters
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_best_v2",'r')as f:
    with open("/home/shlaakuntha/Downloads/project/max_bit_score_sorted",'r')as f1:
        with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_with_filters",'w')as out:
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
the contents to a new file called alter_campto_top_hits
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_with_filters","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_top_hits","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            #threshold for pident=60; threshold for length=50. 
            #So all sequences having pident<60 and length<50 will be filtered out.
            if (float(parts[2])>60 and float(parts[3])>50 and (float(parts[11])/float(parts[12]))>0.3):
                out.write(line)
            line=f.readline()
#PART 6
""""
script to identify genes in the endophyte matching the CPT candidate genes in Camptotheca acuminata in the
file alter_campto_with_filters which basically has all the columns of alter_campto_best and an
additional column containing the maximum bit score for each query sequence. The results are in a file
called alter_campto_match
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_with_filters","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/camptotheca_candidate_genes",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_match_v2","w")as out:
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
script to identify genes in the endophyte matching the CPT candidate genes in Camptotheca acuminata 
from original alternaria_camptotheca_blast file. Results are in alter_campto_match_unfiltered
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alternaria_camptotheca_blast_v2","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/camptotheca_candidate_genes",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_match_unfiltered","w")as out:
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
script to find cpt candidate genes of camptotheca acuminata in the alter_campto_top_hits file. 
This is to see if there are any top hits resembling the CPT candidate genes in Camptotheca acuminata
"""
with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_top_hits","r") as f:
    with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/camptotheca_candidate_genes",'r')as f1:
        with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/cpt_candidates_alternaria","w")as out:
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
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/cpt_candidates_alternaria","r")as f2:
    lns=f2.readlines()
    parts3=[]
    for eachone in lns:
        parts3.append(eachone.strip("\t").split())
    if len(parts3)!=0:
        print("Wow the endophyte has some probable CPT genes in the top blast hit list derived Camptotheca acuminata!")
    else:
        print("Omg the endophyte has no genes in the top blast hit list matching the CPT candidate genes in Camptotheca acuminata! \n Is it producing CPT independent of plant hosts?")
        
#part 9
#script to sort alter_campto_top_hits file based on similarity score
import operator
data=[]
def header_list (file_name):
    with open (file_name,"r") as f:
        line=f.readline()
        while line:
            parts=line.strip().split()
            data.append({'top_qseqid':parts[0],'top_sseqid':parts[1],'top_similarity':parts[2]})
            line=f.readline()
    return data
data_list=header_list("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_top_hits")
data_sorted=sorted(data_list,key=operator.itemgetter('top_similarity'),reverse=True)
with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_qseqids","w") as out1:
    for things in data_sorted:
        out1.write(things['top_qseqid']+"\n")
with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_sseqids","w") as out2:
    for things in data_sorted:
        out2.write(things['top_sseqid']+"\n")
with open("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_similarities","w") as out2:
    for things in data_sorted:
        out2.write(things['top_similarity']+"\n")
#Correct script to merge the contents of two different files
#merges top qseqids and top sseqids
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_qseqids","r") as f1:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_sseqids","r") as f2:
            with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_sqseqids","w")as out3:
                line=f1.readline()
                while line:
                    line=line.strip("\n")
                    ln=f2.readline()
                    if (len(ln)!=0):
                        lines=line+"\t"+ln
                        out3.write(lines)
                    else:
                        out3.write("\n"+line+".")   
                    line=f1.readline()
#PART 10
"""
merges top sseqids, qseqids and similarity scores and shows the list on the basis of 
descending order of similarity scores. This file contains only columns of qseqids, sseqids and similarity 
scores from the alter_campto_top_hits file
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_sqseqids","r") as f3:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/ac_top_similarities","r") as f4:
            with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_top_hits_sorted","w")as out4:
                line=f3.readline()
                while line:
                    line=line.strip("\n")
                    ln=f4.readline()
                    if (len(ln)!=0):
                        lines=line+"\t"+ln
                        out4.write(lines)
                    else:
                        out4.write("\n"+line+".")   
                    line=f3.readline()
#PART 11
"""
script to add the annotations of the camptotheca sequences in the alter_campto_top_hits_sorted
file from the Camptotheca functional annotation file
"""
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_top_hits_sorted","r") as f5:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/camptotheca_annot","r") as f6:
            with open ("/home/shlaakuntha/Downloads/project/Alternaria_Camptotheca_BLASTp/alter_campto_top_hits_sorted_annot","w")as out5:
                line=f5.readline()
                ln=f6.readlines()
                parts2=[]
                for each in ln:
                    parts2.append(each.strip().split("\t"))
                while line:
                    parts1=line.strip().split("\t")
                    for i in parts2:
                        if parts1[1]==i[0]:
                            linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+i[1]
                            out5.write(str(linenew)+"\n")
                    line=f5.readline()        
        

                    


# In[8]:





# In[ ]:




