### Hanna Schilbert ###
### hschilbe@cebitec.uni-bielefeld.de ###
### version 1.0 ###

import sys

# --- end of imports --- #

__usage__ = """
	python create_primer_to_test_list.py
	--ape_file <FULL_PATH_TO_APE_FILE_CONTAINING_PRIMER_SEQUENCES>	
	--out <FULL_PATH_TO_OUTPUT_FILE>
	"""

def main( parameters ):
	
	ape_file = parameters[ parameters.index( '--ape_file' )+1 ]
	out = parameters[ parameters.index( '--out' )+1 ]
	
	primers = []

	with open ( ape_file, 'r') as f:
		line = f.readline()	
		line = f.readline()	
		line = f.readline()	
		parts = line.strip().split(' ')
		orientation = parts [4]
		line = f.readline()	
		line = f.readline()	
		line = f.readline() 
		line = f.readline()
		while line:
			parts = line.strip().replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').replace('  ', ' ').split(' ')
			primers.append( { 'seq': parts[1], 'length':  parts[3], 'gc': parts[4] , 'tm': parts[5] } )
			line = f.readline().strip()
	
	with open ( out, 'w') as out:
		for idx, primer in enumerate(primers):
			if orientation == "(5'-->3')":
				out.write('>fw__' + str(idx) + '__' + primer['length'] + 'bp_' + primer['tm'] + 'C_' + primer['gc'] +'%\n' + primer['seq'] + '\n')
			elif orientation == "(3'<--5')":
				out.write('>rv__' + str(idx) + '__' + primer['length'] + 'bp_' + primer['tm'] + 'C_' + primer['gc'] +'%\n' + primer['seq'] + '\n')
	
	
if __name__ == "__main__":
	
	if '--ape_file' in sys.argv and '--out' in sys.argv:
		main( sys.argv )
	else:
		sys.exit( __usage__ )
