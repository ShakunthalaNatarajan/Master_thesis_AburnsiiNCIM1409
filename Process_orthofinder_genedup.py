#!/usr/bin/env python
# coding: utf-8

# In[5]:


with open ("/home/shlaakuntha/Downloads/project/Orthogroups.GeneCount.tsv","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_gene_dups","w") as out:
        f.readline()
        line=f.readline()
        while line:
            parts=line.strip().split("\t")
            if int(parts[3])>int(parts[1]) and int(parts[3])>int(parts[2]) and int(parts[3])>int(parts[4]) and int(parts[3])>int(parts[5]) and int(parts[3])>int(parts[6]):
                out.write(parts[0]+"\n")
            line=f.readline()
                
with open ("/home/shlaakuntha/Downloads/project/Orthogroups.GeneCount.tsv","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/orthofinder/Aburnsii_gene_dups_exact1","w") as out:
        f.readline()
        line=f.readline()
        while line:
            parts=line.strip().split("\t")
            if int(parts[3])-int(parts[1])==1 and int(parts[3])-int(parts[2])==1 and int(parts[3])-int(parts[4])==1 and int(parts[3])-int(parts[5])==1 and int(parts[3])-int(parts[6])==1:
                out.write(parts[0]+"\n")
            line=f.readline()           
                
            
            


# In[6]:





# In[ ]:




