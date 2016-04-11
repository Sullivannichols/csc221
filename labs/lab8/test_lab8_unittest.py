import unittest
from lab8 import (
    count_letters,
    reverse_string,
    is_palindrome,
    match_ends,
    front_x,
    sort_last,
)

class TestLab8(unittest.TestCase):
    def test_count_letter(self):
        self.assertEqual(count_letters('hello', 'l'), 2)
    def reverse_string(self):
        self.assertTrue(reverse_string('hello') == "olleh")
        self.assertEqual(reverse_string('abba'), 'abba')
    def is_palindrome(self):
        self.assertEqual(is_palindrome('hello') == False)
        self.assertEqual(is_palindrome('hello') == True)
    def match_ends(self):
        self.assertEqual(
            match_ends('hello' 'xbox' 'beeb' 'blob' 'a' 'ablf')
    def front_x(self):
        self.assertEqual(
            front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
            ['xanadu','xyz', 'aardvark', 'apple', 'mix']
    def sort_last(self)
        self.assertEqual(
            sort_last[(1, 7), (1, 3), (3, 4, 5), (2, 2)])
            [(2, 2), (1, 3), (3, 4, 5), (1, 7)]


if __name__ == '__main__':
    unittest.main()
    pass
