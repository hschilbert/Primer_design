### Hanna Schilbert ###
### hschilbe@cebitec.uni-bielefeld.de ###
### version 1.0 ###

import sys, os

# --- end of imports --- #

__usage__ = """
	python find_primers.py
	--ape_file <FULL_PATH_TO_APE_FILE_CONTAINING_PRIMER_SEQUENCES>	
	--out <FULL_PATH_TO_OUTPUT_DIRECTORY>
	"""

def main( arguments ):
	"""! @brief run all parts of this script """
	
	ape_file = arguments[ arguments.index('--ape_file')+1 ]
	prefix = arguments[ arguments.index('--out')+1 ]
	
	print prefix
	if not prefix[-1] == "/":
		prefix += "/"
			
	db = "./AtTAIR10_nt_db"
		
	# prepare primer list for blast #
	print 'prepare primer list for blast...'
	clean_primer_list = prefix + "primer_list_to_blast.fa"
	os.popen ("python create_primer_to_test_list.py --ape_file " + ape_file + " --out " + clean_primer_list )
	
	# BLAST #
	print 'BLASTING...'
	blast_result = prefix + "blast_result_At.txt"
	os.popen ("blastn -query " + clean_primer_list + " -db " + './AtTAIR10_nt_db' + " -out " + blast_result + " -evalue 0.5 -num_threads 16 -word_size 4 -outfmt 6")
	
	#  fetch best primers #
	print 'fetch best primers...'
	final_result = prefix + "summary_results_At.txt"
	os.popen ("python fetch_best_primer_from_blast_output_table.py --blast_result_file_with_unique_primer_headers " + blast_result + " --out " + final_result )	

	
if __name__ == "__main__":
	
	if '--ape_file' in sys.argv and '--out' in sys.argv:
		main( sys.argv )
	else:
		sys.exit( __usage__ )
