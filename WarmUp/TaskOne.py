class TaskOne:

    def __init__(self):
        self.string = ''

    def getString(self):
        self.string = input("enter input")

    def printString(self):
        return self.string.upper()

    def __repr__(self):
         return self.string.upper()




# class Input:
#     def __init__(self):
