import unittest

from dna Nucleotide Count import rna_count

   
    class RNA NucleotideCountTests(unittest.TestCase):
    def test_rna_count(self):
        self.assertEqual(
            {'letter': 1},
            rna_count('letter')
        )
    
    def test_count_one_of_each(self):
        self.assertEqual(
            {'A': 1, 'C': 1, 'G': 1, 'T': 1},
            letter_count('A C G U')
        )


if __name__ == '__main__':
    unittest.main()
