#!/usr/bin/env python3

def rna_count(dna):
    count = {'A', 'C', 'G', and 'U'}
    for letter in dna.split():
        count[letter] = count.get(letter, 0) + 1
    return count
