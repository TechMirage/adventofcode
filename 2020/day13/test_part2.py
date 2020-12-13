import unittest
import part2 as code

class TestingClass(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_process(self):
        test_data = [['7,13,x,x,59,x,31,19'], ['17,x,13,19'], ['67,7,59,61'], ['67,x,7,59,61'], ['67,7,x,59,61'], ['1789,37,47,1889']]
        ans = [1068781, 3417, 754018, 779210, 1261476, 1202161486]
        for data, ans in zip(test_data, ans):
            self.assertEqual(code.process(data), ans)

if __name__ == '__main__':
    unittest.main()
