#!/usr/bin/env python
# coding: utf-8

# In[ ]:


__usage__= """
           This script helps process the BLAST results of plant vs endophyte studies
           python3 process_blast_results.py
           --in <path_to_self_blasted_Aburnsii_file>
           --best <path_to_blast_results_processed_with_blast2best.py_script>
           --candidates <path_to_cpt_candidates_sequences_in_the_plant_after_processing_with_blast2best.py_script>
           --annot <path_to_file_containing_plant_annotation>
           --peblast <path_to_file_containing_blast_results_of_plant_vs_endophyte>
           --tmp <path_to_temporary_folder>
           --out <path_to_output_directory>
           
           """
######### imports #########

import os, sys, operator

##### end of imports #####

def maxbitscore (self_blast,tmp_dir,destination):
#script to obtain sequences with 100% identity to themselves in self blast of Alternaria
#the corresponding bit score will be the max bit score for each of the sequence in the file
    mbs=os.path.join(tmp_dir,"max_bit_score")
    with open (self_blast,"r") as f:
        with open(mbs,"w")as out:
            line=f.readline()
            while line:
                parts=line.strip().split()
                if parts[0]==parts[1]:
                    out.write(line)
                line=f.readline()
#script to create and sort the max_bit_score file with seqids and max bit score columns alone
    data=[]
    def header_list (file_name):
        with open (file_name,"r") as f:
            line=f.readline()
            while line:
                parts=line.strip().split()
                data.append({'qseqid':parts[0],'bitscore':parts[11]})
                line=f.readline()
        return data
    data_list=header_list(mbs)
    data_sorted=sorted(data_list,key=operator.itemgetter('qseqid'))
    seq=os.path.join(tmp_dir,"seq_ids")
    bit=os.path.join(tmp_dir,"bit_score")
    with open(seq,"w") as out1:
        for things in data_sorted:
            out1.write(things['qseqid']+"\n")
    with open(bit,"w") as out2:
        for things in data_sorted:
            out2.write(things['bitscore']+"\n")
#Correct script to merge the contents of two different files
    mbss=os.path.join(destination,"max_bit_score_sorted")
    with open (seq,"r") as f1:
        with open (bit,"r") as f2:
            with open (mbss,"w")as out3:
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
    print("max bit score for aburnsii processed!")
"""
the blast result of plant and endophyte must be processed using blast2best.py script, the output file of 
which is necessary for further processing with this script
"""
def blast_best (destination, blast2best):
    mbss=os.path.join(destination,"max_bit_score_sorted")
    awf=os.path.join(destination,"alter_with_filters")
    ath=os.path.join(destination,"alter_top_hits")
    with open (blast2best,'r')as f:
        with open(mbss,'r')as f1:
            with open(awf,'w')as out:
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
    """
    script to filter out sequences based on percent identity, amino acid length, and normalized bit score and write
    the contents to a new file called alter_campto_top_hits
    """
    with open (awf,"r") as f:
        with open (ath,"w")as out:
            line=f.readline()
            while line:
                parts=line.strip().split()
                #threshold for pident=60; threshold for length=50. 
            #So all sequences having pident<60 and length<50 will be filtered out.
                if (float(parts[2])>55 and float(parts[3])>50 and (float(parts[11])/float(parts[12]))>0.2):
                    out.write(line)
                line=f.readline()
    print("blast results have been filtered!")
""""
script to identify genes in the endophyte matching the CPT candidate genes in the plant in the
file alter_with_filters which basically has all the columns of alter_best and an
additional column containing the maximum bit score for each query sequence. The results are in a file
called alter_match
"""
def match (destination, candidate_genes_blast2best, plant_endo_blast):
    awf=os.path.join(destination,"alter_with_filters")
    am=os.path.join(destination,"alter_match")
    amu=os.path.join(destination,"alter_match_unfiltered")
    ath=os.path.join(destination,"alter_top_hits")
    cca=os.path.join(destination,"cpt_candidates_alternaria")
    candidate_genes=os.path.join(destination,"plant_cpt_candidates")
    """
    script to select and consolidate cpt candidate sequences in the plant by filtering the sequences in input 
    candidates file that was obtained by processing the blast result of cpt candidate sequences and the plant 
    sequences with blast2best.py script
    """
    with open (candidate_genes_blast2best,"r") as f:
        with open (candidate_genes,"w")as out:
            line=f.readline()
            while line:
                parts=line.strip().split()
                #threshold for pident=45; 45% is chosen as similarity % threshold as post-strictosidine enzymes show less similarity in CPT producing plants (Based on similarity scores shown in Yang et al 2021 supplementary material table) threshold for length=50. 
            #So all sequences having pident<45 and length<50aa will be filtered out.
                if (float(parts[2])>45 and float(parts[3])>50):
                    out.write(line)
                line=f.readline()
    print("CPT candidates in the plant have been consolidated")
    """
    script to identify genes in the endophyte matching the CPT candidate genes in the plant
    from original alternaria_camptotheca_blast_best file obtained by processing the original blast result file with blast2best.py script. Results are in alter_match
    """
    with open (awf,"r") as f:
        with open(candidate_genes,'r')as f1:
            with open (am,"w")as out:
                line=f.readline()
                ln=f1.readlines()
                parts2=[]
                for each in ln:
                    parts2.append(each.strip().split())
                while line:
                    parts1=line.strip().split()
                    for i in parts2:
                        if parts1[1]==i[1]:
                            linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+parts1[12]
                            out.write(str(linenew)+"\n")
                    line=f.readline()
    print("A.burnsii sequences matching candidate plant cpt sequences in blast2best processed blast result file have been written to alter_match file")
    """
    script to identify genes in the endophyte matching the CPT candidate genes in the plant
    from original alternaria_camptotheca_blast file. Results are in alter_match_unfiltered
    """
    with open (plant_endo_blast,"r") as f:
        with open(candidate_genes,'r')as f1:
            with open (amu,"w")as out:
                line=f.readline()
                ln=f1.readlines()
                parts2=[]
                for each in ln:
                    parts2.append(each.strip().split())
                while line:
                    parts1=line.strip().split()
                    for i in parts2:
                        if parts1[1]==i[1]:
                            linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]
                            out.write(str(linenew)+"\n")
                    line=f.readline()
    print("A.burnsii sequences matching candidate plant cpt sequences in original unfiltered plant vs endophyte blast result file have been written to alter_match file")                
    """
    script to find cpt candidate genes of host plant in the alter_top_hits file. 
    This is to see if there are any top hits resembling the CPT candidate genes in the host plant
    """
    with open(ath,"r") as f:
        with open(candidate_genes,'r')as f1:
            with open (cca,"w")as out:
                line=f.readline()
                ln=f1.readlines()
                parts2=[]
                for each in ln:
                    parts2.append(each.strip().split())
                while line:
                    parts1=line.strip().split()
                    for i in parts2:
                        if parts1[1]==i[1]:
                            linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+parts1[3]+"\t"+parts1[4]+"\t"+parts1[5]+"\t"+parts1[6]+"\t"+parts1[7]+"\t"+parts1[8]+"\t"+parts1[9]+"\t"+parts1[10]+"\t"+parts1[11]+"\t"+parts1[12]
                            out.write(str(linenew)+"\n")
                    line=f.readline()
    with open (cca,"r")as f2:
        lns=f2.readlines()
        parts3=[]
        for eachone in lns:
            parts3.append(eachone.strip("\t").split())
        if len(parts3)!=0:
            print("Wow the endophyte has some probable CPT genes in the top blast hit list derived the plant")
        else:
            print("Omg the endophyte has no genes in the top blast hit list matching the CPT candidate genes in the plant! \n Is it producing CPT independent of plant hosts?")
"""
script to sort top hits file based on similarity, and append the corresponding annotations to these scripts if 
annotation file of the plant sequences is provided by the user
"""

def sim_sort (destination, plant_annotation,tmp_dir):
    ath=os.path.join(destination,"alter_top_hits")
    atq=os.path.join(tmp_dir,"alter_top_qseqids")
    ats=os.path.join(tmp_dir,"alter_top_sseqids")
    atsim=os.path.join(tmp_dir,"alter_top_similarities")
    atsqs=os.path.join(tmp_dir,"alter_top_sqseqids")
    aths=os.path.join(destination,"alter_top_hits_sorted")
    athsa=os.path.join(destination,"alter_top_hits_sorted_annot")
    data=[]
    def header (file):
        with open (file,"r") as f:
            line=f.readline()
            while line:
                parts=line.strip().split()
                data.append({'top_qseqid':parts[0],'top_sseqid':parts[1],'top_similarity':parts[2]})
                line=f.readline()
        return data
    data_list=header(ath)
    data_sorted=sorted(data_list,key=operator.itemgetter('top_similarity'),reverse=True)
    with open(atq,"w") as out1:
        for things in data_sorted:
            out1.write(things['top_qseqid']+"\n")
    with open(ats,"w") as out2:
        for things in data_sorted:
            out2.write(things['top_sseqid']+"\n")
    with open(atsim,"w") as out2:
        for things in data_sorted:
            out2.write(things['top_similarity']+"\n")
#Correct script to merge the contents of two different files
#merges top qseqids and top sseqids
    with open (atq,"r") as f1:
        with open (ats,"r") as f2:
            with open (atsqs,"w")as out3:
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
    """
    merges top sseqids, qseqids and similarity scores and shows the list on the basis of 
    descending order of similarity scores. This file contains only columns of qseqids, sseqids and similarity 
    scores from the top_hits file
    """
    with open (atsqs,"r") as f3:
        with open (atsim,"r") as f4:
            with open (aths,"w")as out4:
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
    """
    adds the annotations of the plant sequences in the top_hits_sorted
    file from the functional annotation file of the plant sequences
    """
    
    with open (aths,"r") as f5:
        with open (plant_annotation,"r") as f6:
            with open (athsa,"w")as out5:
                line=f5.readline()
                ln=f6.readlines()
                parts2=[]
                if len(ln)==0:
                    out5.write("You have not submitted any plant annotation files.")
                else:
                    for each in ln:
                        parts2.append(each.strip().split("\t"))
                    while line:
                        parts1=line.strip().split("\t")
                        for i in parts2:
                            if parts1[1]==i[0]:
                                linenew=parts1[0]+"\t"+parts1[1]+"\t"+parts1[2]+"\t"+i[1]
                                out5.write(str(linenew)+"\n")
                        line=f5.readline()   
    print("Done with the assessment for horizontal gene transfer between the endophyte and the plant sequences you gave!")
        
#to get file name from the user in the terminal
def main( arguments ):
    self_blast = arguments[arguments.index('--in')+1] 
    blast2best=arguments[arguments.index('--best')+1]
    candidate_genes_blast2best=arguments[arguments.index('--candidates')+1]
    plant_endo_blast=arguments[arguments.index('--peblast')+1]
    tmp_dir=arguments[arguments.index('--tmp')+1]
    destination = arguments[arguments.index('--out')+1] 
    if '--annot' in arguments:
        plant_annotation=arguments[arguments.index('--annot')+1]
    else: 
        plant_annotation="/home/shlaakuntha/Downloads/project/RNASeq_analysis/HGT_check/plant_annot_dummy"
    if not os.path.exists( destination):
        os.makedirs(destination)
    if not os.path.exists( tmp_dir):
        os.makedirs(tmp_dir)
    
    maxbitscore (self_blast,tmp_dir,destination)
    blast_best (destination, blast2best)
    match (destination, candidate_genes_blast2best, plant_endo_blast)
    sim_sort (destination, plant_annotation, tmp_dir)

#check for all mandatory arguments from terminal, if mandatory arguments are missing display  usage instructions
if '--in' in sys.argv and '--out' in sys.argv and '--best' in sys.argv and '--tmp' in sys.argv and '--candidates' in sys.argv and '--peblast' in sys.argv:
    main(sys.argv)
else:
    sys.exit(__usage__)

                    
    


