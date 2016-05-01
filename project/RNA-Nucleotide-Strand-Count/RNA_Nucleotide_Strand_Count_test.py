import unittest

from strands import rna_strand_count


class TestStringMethods(unittest.TestCase):

  def test_rna_strand_count(self):
      self.assertEqual('AAAA', rna_strand_count['AA'])
      self.assertEqual('CCCC', rna_strand_count ['CC'])
      self.assertEqual('GGGG', rna_strand_count ['GG'])
      self.assertEqual('TTTT', rna_strand_count ['TT'])

  def test_rna_dna_count(self):
      self.assertEqual('TTT', rna_strand_count ['TT'])
      self.assertEqual('GGG', rna_strand_count ['GG'])
      self.assertEqual('CCCC', rna_strand_count ['CC'])
      self.assertEqual('UUUU', rna_strand_count ['UU'])

