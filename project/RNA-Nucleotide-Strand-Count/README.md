RNA Nucleotide Strand Count

Implement a function rna_strand_count(dna, strands) that takes two parameters, dna (a string) and strands (a list of strings), and returns a dictionary whose keys are the individual strings in strands and values are the number of occurances of those strings in the RNA complement transcribed from the original DNA.

All matching strands should be counted, not just disjoint (non-overlapping) strands. E.g.

>>> rna_strand_count('AAAA', ['AA'])
{'AA': 3}
The function shall meet these conditions:

rna_count should be able to handle DNA strings in either upper or lowercase form and return the dictionary with keys in the form given
rna_count should also be robust to whitespace:
Whitespace can be assumed not to be part of a strand
For the purpose of counting strands, whitespace in the DNA string can be stripped
A complete set of unit tests for this function shall be included, using both the unittest and doctest modules.
