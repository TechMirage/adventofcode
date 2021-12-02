import unittest

from Day02Solver import Day02Solver


class TestDay02Solver(unittest.TestCase):
    def setUp(self):
        self.solver = Day02Solver()

        with open("input.txt", "r") as f:
            test_input = f.readlines()

        for idx in range(len(test_input)):
            test_input[idx] = test_input[idx].strip()

        self.real_input = test_input
        self.test_input = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"]

    def test_part1_sample(self):
        answer = self.solver.part_1(self.test_input)
        self.assertEqual(answer, 150)

    def test_part1_real(self):
        ans = self.solver.part_1(self.real_input)
        print("Part 1 answer is ", ans)

        self.assertEqual(ans, 1962940)

    def test_part2_sample(self):
        answer = self.solver.part_2(self.test_input)
        self.assertEqual(answer, 900)

    def test_part2_real(self):
        ans = self.solver.part_2(self.real_input)
        print("Part 2 answer is ", ans)

        self.assertEqual(ans, 1813664422)
