import unittest

from SevenSegmentDisplay.SevenSegmentDisplay import SevenSegmentDisplay
from SevenSegmentDisplay.exceptions.exceeded_length_exception import ExceededLengthException


class MyTestCase(unittest.TestCase):

    def test_the_length_of_input_must_be_eight_characters__raises_exception_if_not(self):
        user_input = "123456789"
        display = SevenSegmentDisplay(user_input)
        with self.assertRaises(ExceededLengthException):
            display.check_length(user_input)

    def test_the_user_input_should_only_be_ones_and_zeros__raises_exception_if_not(self):
        user_input = "123456789"
        display = SevenSegmentDisplay(user_input)
        with self.assertRaises(ValueError):
            display.check_input(user_input)

    def test_display(self):
        user_input = "11111111"
        display = SevenSegmentDisplay(user_input)
        display.display(user_input)


    # def test_the_seven_segment_display_is_on_if_the_last_character_is_1(self):
    #     display = SevenSegmentDisplay()
    #






if __name__ == '__main__':
    unittest.main()
