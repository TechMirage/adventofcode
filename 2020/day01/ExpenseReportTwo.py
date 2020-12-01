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
        self.cur_rotated_report_2 = deepcopy(self.report)

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

    def rotate(self, which_report: int):
        if which_report == 1:
            tmp = self.cur_rotated_report.pop(0)
            self.cur_rotated_report.append(tmp)
        if which_report == 2:
            tmp = self.cur_rotated_report_2.pop(0)
            self.cur_rotated_report_2.append(tmp)

    def add(self):
        tmp = []
        for (item1, item2, item3) in zip(self.cur_rotated_report, 
                                          self.report,
                                          self.cur_rotated_report_2):
            tmp.append(item1 + item2 + item3)
        return tmp

    def __call__(self):
        counter_one = 0
        while counter_one <= self.max_rotations:
            self.cur_rotated_report_2 = deepcopy(self.report)
            counter_two = 0
            while counter_two <= self.max_rotations:
                output = self.add()
                output = self.check(output)
                if output != -2:
                    return self.cur_rotated_report[output] * self.report[output] * self.cur_rotated_report_2[output]
                counter_two += 1
                self.rotate(2)
            counter_one += 1
            self.rotate(1)
        return False