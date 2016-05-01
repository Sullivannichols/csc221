#!/usr/bin/env python3



def to_rna(dna):
    return ''.join(complement[nucleotide] for nucleotide in dna)

complement = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U',
              'g': 'c',
              'c': 'g',
              't': 'a',
              'a': 'u'}



      
