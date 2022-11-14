#!/usr/bin/env python
# coding: utf-8

# In[28]:


#script to extract annotations of Aburnsii unique genes (without GO and pathways columns)
with open("/home/shlaakuntha/Downloads/project/annotSRC.tsv","r") as f1:
    with open("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_unique_genes",'r')as f2:
        with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_annotations","w")as out:
            line=f1.readline()
            ln=f2.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split("\t")
                for i in parts2:
                    if parts1[0]==i[0]:
                        linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[11]+"\t"+parts1[12]
                        out.write(str(linenew)+"\n")
                line=f1.readline()


# In[32]:


#script to extract GO and pathway terms annotations of Aburnsii unique genes (Only GO and pathway columns)
with open("/home/shlaakuntha/Downloads/project/annotSRC.tsv","r") as f1:
    with open("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_unique_genes",'r')as f2:
        with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_annotations_2","w")as out:
            line=f1.readline()
            ln=f2.readlines()
            parts2=[]
            for each in ln:
                    parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split("\t")
                for i in parts2:
                    if parts1[0]==i[0]:
                        if len(parts1)<14:
                            linenew1="-"+"\t"+"-"
                            out.write(str(linenew1)+"\n")
                        else:
                            linenew2=parts1[13]+"\t"+parts1[14]
                            out.write(str(linenew2)+"\n")
                line=f1.readline()


# In[3]:


"""
script to obtain the combined annotation columns in Aburnsii_unique_genes_annotations 
and Aburnsii_uique_genes_annotations_2 into a single file Aburnsii_unique_genes_annotations_final
"""

with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_annotations","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_annotations_2","r") as f1:
        with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_annotations_final","w")as out:
            line=f.readline()
            while line:
                line=line.strip("\n")
                ln=f1.readline()
                if (len(ln)!=0):
                    lines=line+"\t"+ln
                    out.write(lines)   
                line=f.readline()


# In[2]:


"""
script to obtain list of genes from Aburnsii unique genes that don't have Interpro annotation, 
GO annotation and pathway term annotation
"""
with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_annotations_final","r")as f:
    with open ("/home/shlaakuntha/Downloads/project/Aburnsii_unique_genes_lacking_annot","w")as out:
        line=f.readline()
        while line:
            parts1=line.strip().split("\t")
            if "PR" not in parts1[10]:
                out.write(line)
            line=f.readline()
            


# In[21]:


"""
script to obtain a non-repetitive list of Aburnsii unique genes that don't have interpro annotation, GO annotation, 
and pathway annotation
"""
with open("/home/shlaakuntha/Downloads/project/annotSRC.tsv","r") as f1:
    with open("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_unique_genes",'r')as f2:
        with open ("/home/shlaakuntha/Downloads/project/ABUniqgenes_lacking_annot","w")as out:
            line=f1.readline()
            ln=f2.readlines()
            parts2=[]
            for each in ln:
                parts2.append(each.strip().split())
            while line:
                parts1=line.strip().split("\t")
                for i in parts2:
                    if parts1[0]==i[0] and "IPR" not in parts1[11]:
                        linenew=i[0]
                        out.write(str(linenew)+"\n")
                line=f1.readline()
with open ("/home/shlaakuntha/Downloads/project/ABUniqgenes_lacking_annot","r")as f3:
    with open ("/home/shlaakuntha/Downloads/project/ABuniqgenes_non_repetitive_noannot","w")as out1:
        lns=f3.readlines()
        parts3=[]
        for each in lns:
            parts3.append(each)
        data=list(set(parts3))
        for each1 in data:
            out1.write(each1)
    
        
    

        
    
                


# In[1]:





# In[16]:





# In[ ]:





# In[ ]:




