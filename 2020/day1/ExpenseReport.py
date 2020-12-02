from copy import deepcopy

class ExpenseReport():

    def __init__(self, input: str):
        """
        Parameters
        ----------
        report : list(int)
            The original report stored on the class.
        max_rotations : int
            The maximum number of rotations before you end back to where you
            started.
        cur_rotated_report : list(int)
            The current rotation of the report. 
        num_of_rotations : int
            The number of rotations that the report currently has had.

        """
        self.report = self.format_string(input)
        self.max_rotations = len(self.report)
        self.cur_rotated_report = deepcopy(self.report)
        self.num_of_rotations = 0

    @staticmethod
    def format_string(input_string: str):
        output = [] 
        for line in input_string.splitlines():
            output.append(int(line))
        return output

    @staticmethod
    def check(input_list: list):
        if 2020 in input_list:
            return input_list.index(2020) 
        return -2 # Not a value in the list.

    def rotate(self):
        tmp = self.cur_rotated_report.pop(0)
        self.cur_rotated_report.append(tmp)
        self.num_of_rotations += 1

    def add(self):
        tmp = []
        for (item1, item2) in zip(self.cur_rotated_report, self.report):
            tmp.append(item1 + item2)
        return tmp

    def __call__(self):
        counter = 0
        while counter <= self.max_rotations:
            self.rotate()
            output = self.add()
            output = self.check(output)
            if output != -2:
                return self.cur_rotated_report[output] * self.report[output] 
            counter += 1
        return False