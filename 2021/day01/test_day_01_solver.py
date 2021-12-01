import unittest

from Day01Solver import Day01Solver


class TestDay01Solver(unittest.TestCase):
    def setUp(self):
        self.solver = Day01Solver()

        with open("input.txt", "r") as f:
            test_input = f.readlines()

        for idx in range(len(test_input)):
            test_input[idx] = int(test_input[idx].strip())

        self.real_input = test_input
        self.test_input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

    def test_part1_sample(self):
        answer = self.solver.part_1(self.test_input)
        self.assertEqual(answer, 7)

    def test_part1_real(self):
        ans = self.solver.part_1(self.real_input)
        print("Part 1 answer is ", ans)

        self.assertEqual(ans, 1832)

    def test_part2_sample(self):
        answer = self.solver.part_2(self.test_input)
        self.assertEqual(answer, 5)

    def test_part2_real(self):
        ans = self.solver.part_2(self.real_input)
        print("Part 2 answer is ", ans)

        self.assertEqual(ans, 1858)
