# Primer_design
Automatical search for unique primers in the given nucleotide database. 
Applicable for any organisms, where a blast nucleotide database is available.

How to use:

## 1.) build blast nucleotide database:
(e.g. for the A. thaliana reference genome)
```
makeblastdb \
-in TAIR10.fa \
-out AtTAIR10_nt_db \
-dbtype nucl
```
## 2.) start primer search:
```
python find_primers.py \
--ape_file primer_to_test.txt \
--out output/
```
### NOTE: all scripts need to be in the working directory. 
For an example of primer_to_test.txt see above: This file can be generated via ApE - A plasmid editor (https://jorgensen.biology.utah.edu/wayned/ape/) by selecting the sequence on which primers should be designed on and then klick on Tools --> Find Primers (set your parameters) --> OK --> save full list as .txt file and use it as input for find_primers.py.
