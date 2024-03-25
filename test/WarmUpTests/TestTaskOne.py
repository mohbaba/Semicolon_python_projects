import unittest
from WarmUp.TaskOne import *
from WarmUp.task_two import *

import unittest



class WarmUpTest(unittest.TestCase):

    def testThatYouCanGetStringFromTheConsole(self):
        input_test = input("Enter an input: ")
        task_one = TaskOne()
        task_one.getString()
        self.assertAlmostEqual(input_test.upper(), task_one.printString())

    def testFunctionReturnsHighestOccurringNumber(self):
        user_input = [1,2,2,2,4,2]
        expected = [4,2]
        self.assertEqual(expected, get_highest_occurring(user_input))


if __name__ == '__main__':
    unittest.main()
