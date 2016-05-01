#!/usr/bin/env python3

def rna_count(dna):

    """
    >>> rna_count('A')
    1
    >>> rna_count('CCC')
    3
    >>> rna_count('GGGG')
    4
    >>> rna_count('UU')
    2
    >>> rna_count('ACCCGGGGUU')
    rna_count({'A': 1, 'C': 3, 'G': 4, 'U': 2})
    >>> rna_count('a')
    1
    >>> rna_count('ccc')
    3
    >>> rna_count('gggg')
    4
    >>> rna_count('uu')
    2
    >>> rna_count('acccgggguu')
    rna_count({'a': 1, 'c': 3, 'g': 4, 'u': 2})
    """


    d = {}
# count occurances of character
    for w in dna:
        d[w] = dna.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))




        
