import unittest

from dna import to_rna


class DNATests(unittest.TestCase):

    def test_transcribes_guanine_to_cytosine(self):
        self.assertEqual('C', to_rna('G'))
        self.assertEqual('c', to_rna('g'))


    def test_transcribes_cytosine_to_guanine(self):
        self.assertEqual('G', to_rna('C'))
        self.assertEqual('g', to_rna('c'))

    def test_transcribes_thymine_to_adenine(self):
        self.assertEqual('A', to_rna('T'))
        self.assertEqual('a', to_rna('t'))

    def test_transcribes_adenine_to_uracil(self):
        self.assertEqual('U', to_rna('A'))
        self.assertEqual('u', to_rna('a'))

    def test_transcribes_all(self):
        self.assertEqual('GCTA', to_rna('CGAU'))
        self.assertEqual('gcta', to_rna('cgau'))

