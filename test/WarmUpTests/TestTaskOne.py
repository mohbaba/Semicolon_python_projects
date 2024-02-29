import unittest
from WarmUp.TaskOne import *

import unittest


class WarmUpTest(unittest.TestCase):

    def testThatYouCanGetStringFromTheConsole(self):
        input_test = input("Enter an input: ")
        task_one = TaskOne()
        task_one.getString()
        self.assertAlmostEqual(input_test.upper(), task_one.printString())


if __name__ == '__main__':
    unittest.main()
