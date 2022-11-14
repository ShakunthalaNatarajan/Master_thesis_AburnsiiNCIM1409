#!/usr/bin/env python
# coding: utf-8

# In[9]:


with open ("/home/shlaakuntha/Downloads/project/cpt_probables_alternaria_blast","r") as f:
    with open("/home/shlaakuntha/Downloads/project/max_bit_score_sorted",'r')as f1:
        with open("/home/shlaakuntha/Downloads/project/cpt_probables_alternaria_blast_with_filters",'w')as out:
            line=f.readline()
            ln=f1.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip("\t").split())
            while line:
                parts1=line.strip().split()
                for i in parts2:
                    if parts1[1]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+i[1]
                        out.write(str(linenew)+"\n")
                line=f.readline()
"""
script to filter out sequences based on percent identity, amino acid length, and normalized bit score and write
the contents to a new file called cpt_candidates_alternaria_burnsii
"""
with open ("/home/shlaakuntha/Downloads/project/cpt_probables_alternaria_blast_with_filters","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/cpt_candidates_alternaria_burnsii","w")as out1:
        line=f.readline()
        while line:
            parts=line.strip().split()
            #threshold for pident=60; threshold for length=50. 
            #So all sequences having pident<60 and length<50 will be filtered out.
            if (float(parts[2])>60and float(parts[3])>50 and (float(parts[11])/float(parts[12]))>0.3):
                out1.write(line)
            line=f.readline()
            
    


# In[ ]:




