#!/usr/bin/env python3

print("\n")

user = int(input("Enter a dna to check\n:"))



upper = raw_input('type in something lowercase.')
lower = raw_input('type in the same thing caps lock.')
print upper.upper()
print lower.lower()

complement = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U'}


def to_rna(dna):
    return ''.join(complement[nucleotide] for nucleotide in dna)

dna[3] 
'C' 
dna[2] 
'T' 
dna[1] 
'G' 
dna[0] 
'A' 

def transcribe(dna): 
     """Return dna string as rna string.""" 
     return dna.replace('A', 'U'),('G','C'),('T','A')('C','G') 
     
     transcribe('GCTA')
     'CGAU'

      
