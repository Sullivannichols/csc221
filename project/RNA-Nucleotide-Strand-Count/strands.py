#!/usr/bin/env python3

def rna_strand_count(dna,strands):
    dna = dna.replace(' ','').upper()    
    strands = strands.replace(' ','').upper()    
    first = strands[0]
    second = strands[1:]
    return {strands:len(re.findall(r'{0}(?={1})'.format(first,second),dna))}


print rna_strand_count('AAAA', ['AA']) {'AA': 3}
