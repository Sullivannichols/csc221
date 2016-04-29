#!/usr/bin/env python3

print("\n")

user = int(input("Enter a dna to check\n:"))

upper = raw_input('type in something lowercase.')
lower = raw_input('type in the same thing caps lock.')
print upper.upper()
print lower.lower()


def to_rna(dna):
    return ''.join(complement[nucleotide] for nucleotide in dna)

complement = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'}

def transcribe(dna): 
     """Return dna string as rna string.""" 
     return dna.replace('A', 'U'),('G','C'),('T','A')('C','G') 
     
     print transcribe('GCTA')
     'CGAU'

      
