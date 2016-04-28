#!/usr/bin/env python3

def rna_count(dna):
    d = {}
# count occurances of character
    for w in dna:
        d[w] = dna.count(w)
# print the result
    for k in sorted(d):
        print (k + ': ' + str(d[k]))

dna='ACCTTTGGGCCCAAACCCCGGGUUGGAAACCCTTT'
rna_count(dna)

        
