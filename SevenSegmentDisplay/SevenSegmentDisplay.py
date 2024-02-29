from exceptions.exceeded_length_exception import *


class SevenSegmentDisplay:

    def __init__(self, number):
        self.number = number

    segment = {
        '0': ["# # # #", "#     #", "#     #", "#     #", "#     #", "#     #", "# # # #"],
        '1': ["      #", "      #", "      #", "      #", "      #", "      #", "      #"],
        '2': ["# # # #", "      #", "      #", "# # # #", "#      ", "#      ", "# # # #"],
        '3': ["# # # #", "      #", "      #", "# # # #", "      #", "      #", "# # # #"],
        '4': ["#     #", "#     #", "#     #", "# # # #", "      #", "      #", "      #"],
        '5': ["# # # #", "#      ", "#      ", "# # # #", "      #", "      #", "# # # #"],
        '6': ["#      ", "#      ", "#      ", "# # # #", "#     #", "#     #", "# # # #"],
        '7': ["# # # #", "      #", "      #", "      #", "      #", "      #", "      #"],
        '8': ["# # # #", "#     #", "#     #", "# # # #", "#     #", "#     #", "# # # #"],
        '9': ["# # # #", "#     #", "#     #", "# # # #", "      #", "      #", "      #"]
    }

    binary_numbers = {
        '0': '11111101',
        '1': '01100001',
        '2': '11011011',
        '3': '11110011',
        '4': '01100111',
        '5': '10110111',
        '6': '10111111',
        '7': '11100001',
        '8': '11111111',
        '9': '11110111'
    }

    def check_length(self, input: str):
        if len(input) != 8:
            raise ExceededLengthException("8 characters required")

    def check_input(self, input: str):
        for character in input:
            if character not in '01':
                raise ValueError("Only Zero's and One's are permitted")

    def is_on(self):
        return self.number[-1] == '1'

    def display(self, input: str):
        self.check_length(input)
        self.check_input(input)
        if self.is_on():
            for number in self.binary_numbers:
                if input == self.binary_numbers[number]:
                    segment = number
            for asterisk in self.segment[segment]:
                print(asterisk)
        else:
            print("Display is off")




user_input = "11101111"
display = SevenSegmentDisplay(user_input)
try:
    display.display(user_input)
except UnboundLocalError:
    print("Number Combination entered doesn't exist")
