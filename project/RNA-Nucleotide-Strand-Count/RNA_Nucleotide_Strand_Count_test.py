import unittest

from strands import rna_strand_count

class TestStringMethods(unittest.TestCase):

  def test_rna_strand_count(self):
      self.assertStrand('AAAA', ['AA'])
      self.assertStrand('CCCC', ['CC'])
      self.assertStrand('GGGG', ['GG'])
      self.assertStrand('TTTT', ['TT'])
      
  def test_rna_dna_count(self):
      self.assertDna('TTT', ['TT'])
      self.assertDna('GGG', ['GG'])
      self.assertDna('CCCC', ['CC'])
      self.assertDna('UUUU', ['UU'])


if __name__ == '__main__':
    unittest.main()
