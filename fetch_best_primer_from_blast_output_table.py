### Hanna Schilbert ###
### hschilbe@cebitec.uni-bielefeld.de ###
### version 1.0 ###

import sys
from collections import Counter

# --- end of imports --- #

__usage__ = """
	python fetch_best_primer_from_blast_output_table.py
	--blast_result_file_with_unique_primer_headers <FULL_PATH_TO_BLAST_RESULT_FILE>	
	--out <FULL_PATH_TO_OUTPUT_FILE>
	"""

def main( parameters ):
	
	BLAST_res = parameters[ parameters.index( '--blast_result_file_with_unique_primer_headers' )+1 ]
	out = parameters[ parameters.index( '--out' )+1 ]

	IDs = []
	counter = 0
	with open( BLAST_res, "r" ) as f:
		line = f.readline().strip().split('\t')[0]	
		while line:
			IDs.append( line.strip().split('\t')[0] )
			line = f.readline()

	with open (out , 'w') as out:
		for i, ID in enumerate(Counter(IDs).keys()):
			out.write( str(ID) + '\thas\t' + str(Counter(IDs).values()[i]) + '\thits.\n')

	
if __name__ == "__main__":
	
	if '--blast_result_file_with_unique_primer_headers' in sys.argv and '--out' in sys.argv:
		main( sys.argv )
	else:
		sys.exit( __usage__ )
