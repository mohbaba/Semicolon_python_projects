class ComplexNumbers:

    def __init__(self,left,right):
        self.left = left
        self.right = right

    def __add__(self, other):
        return f'{self.left + other.left}j {"+"} {self.right + other}i'

    def __repr__(self):
        return f'{self.left}j {"+" if self.right > 0 else "-"} {self.right}'

    def __gt__(self, other):
        return f'{self.left + other.left} > {self.right + other.right}'

    def __lt__(self, other):
        return f'{self.left <= other} < {self.right <= other}'

    def __sub__(self, other):
        return f'{self.left - other.left}j {"-"} {self.right - other.right}'

    def __eq__(self, other):
        return self == other.left and self.right == other.right