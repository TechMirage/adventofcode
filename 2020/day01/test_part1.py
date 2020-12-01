import unittest
from ExpenseReport import ExpenseReport

class TestingClass(unittest.TestCase):

    def setUp(self):
        test_input = "1721\n979\n366\n299\n675\n1456"
        self.expense_report = ExpenseReport(test_input)

    def test_rotation(self):
        self.expense_report.rotate()
        self.assertEqual(self.expense_report.cur_rotated_report, 
                         [979, 366, 299, 675, 1456, 1721])

    def test_add(self):
        tmp = self.expense_report.add()
        self.assertEqual(tmp[0], 
                         self.expense_report.cur_rotated_report[0] 
                         + self.expense_report.report[0])
        self.assertEqual(tmp[4], 
                         self.expense_report.cur_rotated_report[4] 
                         + self.expense_report.report[4])

    def test_check(self):
        tmp1 = [234, 256, 12, 934]
        self.assertEqual(self.expense_report.check(tmp1), -2)
        tmp2 = [2020, 450, 140]
        self.assertEqual(self.expense_report.check(tmp2), 0)

    def test_process(self):
        ans = self.expense_report()
        self.assertEqual(ans, 514579)


if __name__ == '__main__':
    unittest.main()
