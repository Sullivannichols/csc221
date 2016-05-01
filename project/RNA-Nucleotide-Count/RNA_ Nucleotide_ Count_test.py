import unittest

from dna Nucleotide Count import rna_count

class DNATests(unittest.TestCase):
   def test_rna_count(self):
        self.assertEqual(
            {'letter': 1},
            rna_count('letter')
        )

    def test_count_one_of_each(self):
        self.assertEqual(
            {'A': 1, 'C': 1, 'G': 1, 'U': 1,'a': 1, 'c': 1, 'g': 1, 'u': 1},
            rna_count('A C G U a c g u')
        )

