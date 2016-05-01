#!/usr/bin/env python3

import re

def rna_strand_count(dna, strands):

    """
    >>>rna_strand_count('AAAA', 'AA')
    {'AA': 3}
    >>> rna_strand_count('CCC', 'CC')
    {'CC': 2}
    >>> rna_strand_count('GG', 'GG')
    {'GG': 1}
    >>> rna_strand_count('TTTTT', 'TT')
    {'TT': 4}
    >>> rna_strand_count('aaaa', 'aa')
    {'aa': 3}
    >>> rna_strand_count('ccc', 'cc')
    {'cc': 2}
    >>> rna_strand_count('gg', 'gg')
    {'gg': 1}
    >>> rna_strand_count('ttttt', 'tt')
    {'tt': 4}
    >>> rna_strand_count('uu', 'uu')
    {'uu': 1}
    >>> rna_strand_count('UUUUU', 'UU')
    {'UU': 4}
   >>> rna_strand_count('AAAA', 'AA'),('CCC', 'CC'),('GG', 'GG'),('TTTTT', 'TT'),('aaaa', 'aa'),('ccc', 'cc'),('gg', 'gg'),('ttttt', 'tt'),('uu', 'uu')
    ({'AA': 3},{'CC': 2},{'GG': 1},{'TT': 4},{'aa': 3},{'cc': 2},{'gg': 1},{'tt': 4},{'uu': 4})
    """

    dna.upper = dna.replace(' ','').upper()
    strands.upper = strands.replace(' ','').upper()
    first = strands[0]
    second = strands[1:]
    return {strands:len(re.findall(r'{0}(?={1})'.format(first,second),dna))}
    dna.lower = dna.replace(' ','').lower()
    strands.lower = strands.replace(' ','').lower()
