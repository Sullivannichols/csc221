import doctest

from year import rna_strand_count

def dna(n):
    """ 
    matching strands rna strand count
    >>> rna_strand_count('AAAA', ['AA'])
    {'AA': 3}
    >>> rna_strand_count('CCC', ['CC'])
    {'CC': 2}
    >>> rna_strand_count('GG', ['GG'])
    {'GG': 1}
    >>> rna_strand_count('TTTTT', ['TT'])
    {'TT': 4}
    """
def strands(n):
    """ 
    matching strands rna strand count
    >>> rna_strand_count('  TT', ['TT'])
    {'TT': 1}
    >>> rna_strand_count('GGG', ['GG'])
    {'GG': 2}
    >>> rna_strand_count('CCCC', ['CC'])
    {'CC': 3}
    >>> rna_strand_count('U', ['UU'])
    {'UU': 0}
    """


    return True

if __name__ == "__main__": 
    doctest.testmod()
    test Pass
    
