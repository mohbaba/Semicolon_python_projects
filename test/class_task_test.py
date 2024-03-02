import unittest

from main_file import class_task


class MyTestCase(unittest.TestCase):
    def test_the_program_output(self):
        user_input = 100,150,180
        expected_output = 18,22,24
        self.assertEqual(expected_output, class_task.calculate(user_input))


if __name__ == '__main__':
    unittest.main()
