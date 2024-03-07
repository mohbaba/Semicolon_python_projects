import unittest
from main_file import count_char

class MyTestCase(unittest.TestCase):
    def test_that_function_will_count_letters(self):
        sample_input = "hello world!"
        output = "LETTERS 10 DIGITS 0"
        self.assertEqual(output,count_char.count_characters(sample_input))

    def test_that_function_will_count_number(self):
        sample_input = "hello world! 123"
        output = "LETTERS 10 DIGITS 3"
        self.assertEqual(output, count_char.count_characters(sample_input))

    def test_upper_Case_and_lower_case_counter(self):
        sample_input = "Hello world!"
        output = "UPPER CASE 1 LOWER CASE 9"
        self.assertEqual(output, count_char.count_cases(sample_input ))


if __name__ == '__main__':
    unittest.main()
