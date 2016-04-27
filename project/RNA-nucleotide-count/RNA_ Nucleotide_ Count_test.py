import unittest

from RNA Nucleotide Count import RNA_Nucleotide_Count_test.py

   
    class RNA NucleotideCountTests(unittest.TestCase):
    def test_count_one_letter(self):
        self.assertEqual(
            {'letter': 1},
            letter_Count('letter')
        )
    
    def test_count_one_of_each(self):
        self.assertEqual(
            {'C': 1, 'G': 1, 'A': 1, 'U': 1},
            letter_count('C G A U')
        )


if __name__ == '__main__':
    unittest.main()
