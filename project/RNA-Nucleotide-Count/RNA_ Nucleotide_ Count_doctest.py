import doctest

from RNA Nucleotide Count import rna_count

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
    """
    

    return True

if __name__ == "__main__": 
    doctest.testmod()
    test Pass
