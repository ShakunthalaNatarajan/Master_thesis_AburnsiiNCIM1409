import pandas as pd
"""
creation of a dictionary from the orthofinder genecount.tsv file. Example given here has six different species in the orthofinder result. This ust be modified 
according to the number of species in your orthofinder results file.
"""
dic={'group':[],'sp1':[],'sp2':[],'sp3':[],'sp4':[],'sp5':[],'sp6':[],'total':[]} 
#opening and reading the orthofinder Genecount.tsv file
with open ("/path/to/Genecount.tsv","r") as f:
    f.readline()
    line=f.readline()
#appending contents of the genecount.tsv file under respective keys in the dictionary dic
    while line:
        parts=line.strip().split("\t")
        dic['group'].append(parts[0])
        dic['sp1'].append(parts[1])
        dic['sp2'].append(parts[2])
        dic['sp3'].append(parts[3])
        dic['sp4'].append(parts[4])
        dic['sp5'].append(parts[5])
        dic['sp6'].append(parts[6])
        dic['total'].append(parts[7])
        line=f.readline()
#converting the dictionary to a dataframe
df=pd.DataFrame(data=dic).set_index("group")
#converting the dftypes to numeric or int 
cols = df.columns[df.dtypes.eq('object')]  
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
group_dict={}
#iterate row wise over the dataframe and add the requisite values to a new dictionary
for index,row  in df.iterrows():
    for sp,count in row.items():
        if sp != "total" and count != 0:
            group_dict.setdefault(index, []).append(sp)
group_dict   
#import upset plot from UpSet module
from upsetplot import UpSet
from upsetplot import from_memberships
#convert the dictionary to upset compatible format
x=from_memberships(group_dict.values()).sort_values(ascending= False)
#plot the upset plot of the Genecount.tsv file
UpSet(x, subset_size='count',show_counts=True).plot()
