import unittest

from year import is_leap_year

class TestStringMethods(unittest.TestCase):

  def test_is_leap_year(self):
      self.assertTrue(isLeapYear(2016));
      self.assertFalse(isLeapYear(1994));

  def test_is_leap_year(self):
      self.assertTrue(isLeapYear(1492));
      self.assertFalse(isLeapYear(1983));

  
if __name__ == '__main__':
     unittest.main()





