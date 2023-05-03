# Python_Bits
1. Upset_Plot_Orthofinder.py - Python code to create upset plots from Orthogroups.GeneCount.tsv file - an output of Orthofinder tool. But this must be edited according to the number of species given by you to orthofinder
2. UpsetPlot_Orthofinder_Genecount.py - Custom python script that constructs upset plot from Orthofinder Orthogroups.GeneCount.tsv file. No edits needed. Can be used directly on the file from orthofinder.
3. Process_orthofinder_Results_correct.py, Unique_genes_annot.py, Process_orthofinder_genedup.py - python codes written for processing orthofinder results and gaining some relevant details for my study from them (using annotation of A. burnsii without RNA-Seq support)
4. Process_blast_results_alternaria_camptotheca.py, process_blast_campto_vs_nimmo_leaf.py, process_blast_results_alternaria_nimmoniana_leaf.py, process_blast_results_alternaria_nimmoniana_root.py, process_blast_results_alternaria_nimmoniana_stem.py, process_blast_results_alternaria_nimmoniana_lrs.py, process_blast_alternaria_candidates(1).py - python codes written for analyzing and processing results of BLASTp done with host plant and endophyte
5. Statistics_gene_prediction.py - pyhton code for obtaining some information on statistics of gene prediction performed
6. avg_prot_length.py- Script to calculate the average protein sequence length in a fasta file containing peptide sequences
7. process_blast_results_v2.py - Custom script to analyze and process the BLASTp results of plant vs endophyte sequences and help investigate for the occurrence of horizontal gene transfer
8. Gene_duplications_synteny_v2.py - Custom script to find the gene duplications in A. burnsii from multiple pairwise synteny comparisons with closely related Alternaria fungi
9. CDS_finder.py - Identifies CDS candidates in a given set of sequences (transcriptome assembly, mRNAs)
10. Process_orthofinder_for_unique_genes.py - Custom python code blocks to obtain the unique genes in A. burnsii NCIM 1409 by parsing the OrthoFinder2 result file containing the orthogroup comparison detail against other fungi used in the comparative study
11. blast2best.py - Identifies the X best BLAST hit for each query
12. contig_stats.py - Calculates the assembly statistics for a given FASTA file; removal of short sequences possible
13. get_peps_from_gff3.py - Helps obtain CDS and peptide FASTA files using GFF3 and whole genome assembly FASTA files as inputs
14. jcvi_pairwise_synteny.py - Custom script to perform pairwise synteny analysis using JCVI/MCScan
15. rename_reads_for_trinity.py - Renames all reads in a FASTQ file to prepare for a Trinity de novo transcriptome assembly
16. transeq.py - Translates coding sequences into polypleptide sequences
