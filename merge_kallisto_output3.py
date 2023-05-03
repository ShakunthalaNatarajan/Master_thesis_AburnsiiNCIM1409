### Boas Pucker ###
### Milan Borchert ###
### b.pucker@tu-bs.de ###
### v0.33 ###

__usage__ = """
					python3 merge_kallisto_output3.py
					--in <INPUT_FOLDER>
					--tpms <TPM_OUTPUT_FILE>
					--counts <COUNTS_OUTPUT_FILE>
					
					optional:
					--gff <GFF_FILE>
					bug reports and feature requests: bpucker@cebitec.uni-bielefeld.de
					"""


import os, sys, glob, time

# --- end of imports --- #

def load_counttable( counttable ):
	"""! @brief load data from counttable """
	
	counts = {}
	tpms = {}
	with open( counttable, "r" ) as f:
		f.readline()	#remove header
		line = f.readline()
		while line:
			parts = line.strip().split('\t')
			counts.update( { parts[0]: float( parts[3] ) } )
			tpms.update( { parts[0]: float( parts[4] ) } )
			line = f.readline()
	return counts, tpms


def generate_mapping_table( gff_file ):
	"""! @brief generate transcript to gene mapping table """
	
	transcript2gene = {}
	with open( gff_file, "r" ) as f:
		line = f.readline()
		while line:
			if line[0] != '#':
				parts = line.strip().split('\t')
				if parts[2] in [ "mRNA", "transcript" ]:
					try:
						ID = parts[-1].split(';')[0].split('=')[1]
						parent = parts[-1].split('arent=')[1]
						if ";" in parent:
							parent = parent.split(';')[0]
						transcript2gene.update( { ID: parent } )
					except:
						print(line)
			line = f.readline()
	return transcript2gene


def map_counts_to_genes( transcript2gene, counts ):
	"""! @brief map transcript counts to parent genes """
	
	error_collector = []
	gene_counts = {}
	for key in counts.keys():
		try:
			gene_counts[ transcript2gene[ key ] ] += counts[ key ]
		except KeyError:
			try:
				gene_counts.update( { transcript2gene[ key ]: counts[ key ] } )
			except KeyError:
				error_collector.append( key )
				gene_counts.update( { key: counts[ key ] } )
	if len( error_collector ) > 0:
		sys.stdout.write( "number of unmapped transcripts: " + str( len( error_collector ) ) + "\n" )
		sys.stdout.flush()
	return gene_counts


def generate_output_file( output_file, data ):
	"""! @brief generate output file for given data dictionary """
	try:
	    timestr = time.strftime("%Y_%m_%d")
	except ModuleNotFoundError:
	    timestr = ""
	samples = list( sorted( list( data.keys() ) ) )
	
	with open( output_file, "w" ) as out:
		out.write( "\t".join( [ timestr ] + samples ) + '\n' )
		for gene in list(sorted(list(data.values())[0].keys())):
			new_line = [ gene ]
			for sample in samples:
				new_line.append( data[ sample ][ gene ] )
			out.write( "\t".join( map( str, new_line ) ) + '\n' )


def main( arguments ):
	"""! @brief run everything """
	
	data_input_dir = arguments[ arguments.index( '--in' )+1 ]
	if data_input_dir[-1] != "/":
		data_input_dir += "/"
	
	try:
	    timestr = time.strftime("%Y_%m_%d_")
	except ModuleNotFoundError:
	    timestr = ""
	# Create date is added to filename for both output files 
	if '--counts' in arguments:
		counts_output_file = arguments[ arguments.index( '--counts' )+1 ]
		counts_output_file_l = counts_output_file.split("/")
		counts_output_file_l.insert(-1, timestr)
		counts_output_file = "/".join(counts_output_file_l[:-1]) + counts_output_file_l[-1]
	else:
		counts_output_file = False
	if '--tpms' in arguments:
		tpm_output_file = arguments[ arguments.index( '--tpms' )+1 ]
		tpm_output_file_l = tpm_output_file.split("/")
		tpm_output_file_l.insert(-1, timestr)
		tpm_output_file = "/".join(tpm_output_file_l[:-1]) + tpm_output_file_l[-1]
	else:
		tpm_output_file = False
	
	if '--gff' in arguments:
		gff_file = arguments[ arguments.index( '--gff' )+1 ]
		transcript2gene = generate_mapping_table( gff_file )
	else:
		transcript2gene = {}
	sys.stdout.write( "number of mapped transcripts: " + str( len( transcript2gene.keys() ) ) + "\n" )
	sys.stdout.flush()
	
	counttables = glob.glob( data_input_dir + "*.tsv" )
	sys.stdout.write( "number of detected counttables: " + str( len( counttables ) ) + "\n" )
	sys.stdout.flush()

	count_data = {}
	tpm_data = {}
	for filename in counttables:
		ID = filename.split('/')[-1].split('.')[0]
		if "_" in ID:	#only take ID if datetime string was included in file name
			ID = ID.split("_")[-1]
		counts, tpms = load_counttable( filename )
		#TPM are available and could be processed in the same way
		gene_counts = map_counts_to_genes( transcript2gene, counts )
		gene_tpms = map_counts_to_genes( transcript2gene, tpms )
		count_data.update( { ID: gene_counts } )
		tpm_data.update( { ID: gene_tpms } )
	
	if counts_output_file:
		generate_output_file( counts_output_file, count_data )
	if tpm_output_file:
		generate_output_file( tpm_output_file, tpm_data )


if '--in' in sys.argv and '--tpms' in sys.argv:
	main( sys.argv )
elif '--in' in sys.argv and '--counts' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
