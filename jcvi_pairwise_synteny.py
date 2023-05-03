# --- Shakunthala Natarajan --- #
"""
A script to perform synteny analysis with two organisms and create 
a synteny blocks file from the .lifted.anchors file
"""
import os, sys, re, subprocess

# --- end of imports --- #

def modify_lifted_anchor_file( lifted_anchor_file ):
	"""! @brief modify lifted anchor file to remove entries of empty contigs """
	
	with open( lifted_anchor_file, "r" ) as f:
		content = f.read()
	content = content.replace( "###\n###\n", "###\n" ).replace( "###\n###\n", "###\n" ).replace( "###\n###\n", "###\n" ).replace( "###\n###\n", "###\n" ).replace( "###\n###\n", "###\n" ).replace( "###\n###\n", "###\n" ).strip()
	
	with open( lifted_anchor_file, "w" ) as out:
		out.write( content )

def main( arguments ):
	"""! @brief run everything """
	
	gff_files = arguments[ arguments.index('--gff')+1 ].split(',')
	cds_files = arguments[ arguments.index('--cds')+1 ].split(',')
	feature_types = arguments[ arguments.index('--feature')+1 ].split(',')	#tag in third column
	ID_types = arguments[ arguments.index('--ID')+1 ].split(',')	#tag in last field
	spec_names = arguments[ arguments.index('--specs')+1 ].split(',') #species names appear as labels in figure
	cscore_cutoff = 0.1	#needs to be a value between 0 and 1
	number_of_matching_regions = 1	#get one corresponding region for each region in reference (needs to be increased)

	output_folder = arguments[ arguments.index('--out')+1 ]

	# --- generate output folder and set it as working directory (important, because relative paths are used!) --- #
	if not os.path.exists( output_folder ):
		os.makedirs( output_folder )
	os.chdir( output_folder )
	# --- production of bed files --- #
	bed_files = []
	for idx, filename in enumerate( gff_files ):
		bed_file = spec_names[ idx ] + ".bed"
		if not os.path.isfile( bed_file ):
			p = subprocess.Popen( args="python3 -m jcvi.formats.gff bed --type " + feature_types[ idx ] + " --key=" + ID_types[ idx ] + " " + filename + " -o " + bed_file, shell=True )
			p.communicate()
		bed_files.append( bed_file )


	# --- generate clean CDS files --- #
	clean_cds_files = []
	for idx, filename in enumerate( cds_files ):
		cds_file = spec_names[ idx ] + ".cds"
		if not os.path.isfile( cds_file ):
			p = subprocess.Popen( args="python3 -m jcvi.formats.fasta format " + filename + " " + cds_file, shell=True )
			p.communicate()
		clean_cds_files.append( cds_file )


	# --- generate one block file per species --- #
	block_file_per_spec = []
	for idx, spec in enumerate( spec_names ):
		if idx > 0:
			# --- identification of putative orthologs --- #
			anchor_file = ".".join( [ spec_names[0], spec ] ) + ".anchors "
			lifted_anchor_file = ".".join( [ spec_names[0], spec ] ) + ".lifted.anchors"
			if not os.path.isfile( lifted_anchor_file ):
				p = subprocess.Popen( args="python3 -m jcvi.compara.catalog ortholog " + " ".join( [ spec_names[0], spec ] ) + " --cscore=" + str( cscore_cutoff ) + " --no_strip_names", shell=True )
				p.communicate()

			# --- generate more succint anchors file --- #
			modify_lifted_anchor_file( lifted_anchor_file )
			block_file = ".".join( [ spec_names[0], spec ] ) + ".i" + str( number_of_matching_regions ) + ".blocks"
			if not os.path.isfile( block_file ):
				p = subprocess.Popen( args="python3 -m jcvi.compara.synteny mcscan " + bed_files[0] + " " + lifted_anchor_file + " --iter=" + str( number_of_matching_regions ) + " -o " + block_file, shell=True )
				p.communicate()
			block_file_per_spec.append( block_file )
main( sys.argv )			

