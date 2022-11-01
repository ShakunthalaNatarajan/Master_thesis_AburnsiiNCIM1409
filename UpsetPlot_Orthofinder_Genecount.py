#!/usr/bin/env python
# coding: utf-8

# In[6]:


__usage__= """
           This script helps contruct an Upset plot from the Orthofinder Orthogroups.GeneCount.tsv file.
           python3 UpsetPlot_Orthofinder_Genecount.py\n
           --in <full path to the Orthogroups.GeneCount.tsv file including the file>\n
           --out <path for storing the Upset plot including the name of your output>\n
           The optional arguments are:
           --colour <colour in which you want the upset plot to be shown>\n default is black
           --shading <degree of shading for your upset plot colour and should be between 0 and 1>\n default is 0.15
           --orientation <horizontal or vertical> default is horizontal
           --sort <degree or cardinality> default is degree
           """
######### imports #########

import os, sys
import pandas as pd
from upsetplot import UpSet
from upsetplot import from_memberships
import matplotlib.figure
import matplotlib.pyplot as plt

##### end of imports #####

#define a function for plotting the upset plot
def upsetplot(OrthoGeneCount, OutPlot, Colourchoice, Shading, Orient, Sort):
    #read the input file and store it as a dataframe with the Orthogroup column as index
    df=pd.read_csv(OrthoGeneCount,sep="\t").set_index("Orthogroup")
    #create an empty dictionary
    group_dict={}
    #iterate row wise across each row in the dataframe
    for index,row  in df.iterrows():
        #loop to add the counts of genes in an orthogroup across species
        for sp,count in row.items():
            if sp != "Total" and count != 0:
                group_dict.setdefault(index, []).append(sp)
    group_dict  
    #convert the dictionary to upset compatible format
    x=from_memberships(group_dict.values()).sort_values(ascending= False)
    UpSet(x, subset_size='count', orientation=Orient, show_counts=True, facecolor=Colourchoice, shading_color=Shading, sort_by=Sort).plot()
    #save the upset plot to the path destination mentioned by the user
    plt.savefig(OutPlot)
    print("Your Upset plot is ready. It looks marvellous!")

#to get file name from the user in the terminal
def main( arguments ):
    OrthoGeneCount = arguments[arguments.index('--in')+1]
    OutPlot = arguments[arguments.index('--out')+1]
    if '--colour' in arguments:
        Colourchoice = str(arguments[arguments.index('--colour')+1])
    else: 
        Colourchoice = 'black'
    if '--shading' in arguments:
        Shading = float(arguments[arguments.index('--shading')+1])
    else: 
        Shading = 0.15
    if '--orientation' in arguments:
        Orient=str(arguments[arguments.index('--orientation')+1])
    else:
        Orient='horizontal'
    if '--sort' in arguments:
        Sort=str(arguments[arguments.index('--sort')+1])
    else:
        Sort='degree'
    upsetplot(OrthoGeneCount, OutPlot, Colourchoice, Shading, Orient, Sort)
#check for all mandatory arguments from terminal, if mandatory arguments are missing display  usage instructions
if '--in' in sys.argv and '--out' in sys.argv:
    main(sys.argv)
else:
    sys.exit(__usage__)







