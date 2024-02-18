import unittest
from main_file.single_string import *





class MyTestCase(unittest.TestCase):
    def test_single_string(self):
        string1 = 'abc'
        string2 = 'xyz'

        expected = 'xyc abz'
        self.assertEqual(expected,concatenate_swap1(string1, string2))

    def test_five_letters(self):
        string1 = 'abcde'
        string2 = 'xyz123'

        expected = 'xycde abz123'
        self.assertEqual(expected,concatenate_swap1(string1,string2))


if __name__ == '__main__':
    unittest.main()
