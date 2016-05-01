#!/usr/bin/env python3



def to_rna(dna):
    return ''.join(complement[nucleotide] for nucleotide in dna)
    
  """ 
     replacing each nucleotide with its complement
    >>> to_rna(G)
    C
    >>> to_rna(C)
    G
    >>> to_rna(T) 
    A
    >>> to_rna(A)
    U
    >>> to_rna(g)
    c
    >>> to_rna(c)
    g
    >>> to_rna(t) 
    a
    >>> to_rna(a)
    u
    >>> 
    """


    return True


complement = {'G': 'C',
              'C': 'G',
              'T': 'A',
              'A': 'U',
              'g': 'c',
              'c': 'g',
              't': 'a',
              'a': 'u'}
              
    
      
