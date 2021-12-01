class Day01Solver:
    def __init__(self):
        pass

    @staticmethod
    def part_1(sonar_ranges: list) -> int:
        increase = 0
        for idx in range(1, len(sonar_ranges)):
            if sonar_ranges[idx] > sonar_ranges[idx - 1]:
                increase += 1

        return increase

    def part_2(self, sonar_ranges: list) -> int:
        new_sonar_ranges = []
        for idx in range(len(sonar_ranges) - 2):
            tmp = sonar_ranges[idx] + sonar_ranges[idx + 1] + sonar_ranges[idx + 2]
            new_sonar_ranges.append(tmp)

        ans = self.part_1(new_sonar_ranges)

        return ans
