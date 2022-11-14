#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
script to filter out sequences based on percent identity, amino acid length, and normalized bit score and write
the contents to a new file called campto_nimmoL_top_hits
"""
with open ("/home/shlaakuntha/Downloads/project/campto_nimmoL_blast","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/campto_nimmoL_top_hits","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            #threshold for pident=60; threshold for length=50. 
            #So all sequences having pident<60 and length<50 will be filtered out.
            if (float(parts[2])>60 and float(parts[3])>50):
                out.write(line)
            line=f.readline()
with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/campto_nimmoL_top_hits","r") as f:
    with open ("/home/shlaakuntha/Downloads/project/Alternaria_Nimmoniana_Leaf_BLASTp/nimmonianaL_cpt_candidate_genes","w")as out:
        line=f.readline()
        while line:
            parts=line.strip().split()
            out.write(parts[1]+"\n")
            line=f.readline()


# In[6]:





# In[ ]:




