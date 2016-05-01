import unittest

from year import is_leap_year

class TestStringMethods(unittest.TestCase):

  def test_is_leap_year(self):
      self.assertIs(is_leap_year(2016), True)
      self.assertFalse(is_leap_year(1994));
      self.assertIs(is_leap_year(1492), False)
      self.assertFalse(is_leap_year(1983));


if __name__ == '__main__':
     unittest.main()
