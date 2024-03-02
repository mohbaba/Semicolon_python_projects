class ClassTask:
    final_list = []

    def __init__(self, *args):
        self.inputs = list(args)
        self.calculate()

    def calculate(self):
        C = 50
        H = 30
        for arg in self.inputs:
            Q = (2 * C * arg) / H
            self.final_list.append(round(Q ** 0.5))
        return self.final_list

    def __repr__(self):
        count = 0
        while count < len(self.final_list):
            count += 1
            return f'{self.final_list[count-1]},'

        # return f'{self.final_list[0]},{self.final_list[1]},{self.final_list[2]}'


task = ClassTask(100, 150, 180)
print(task)
