class Day02Solver:
    def __init__(self):
        pass

    def part_1(self, commands: list) -> int:
        down = 0
        forward = 0
        for cmd in commands:
            direction, distance = self.parse_input(cmd)
            if direction == "forward":
                forward += distance
            elif direction == "down":
                down += distance
            elif direction == "up":
                down -= distance

        return down * forward

    def part_2(self, commands: list) -> int:
        aim = 0
        down = 0
        forward = 0
        for cmd in commands:
            direction, distance = self.parse_input(cmd)
            if direction == "down":
                aim += distance
            elif direction == "up":
                aim -= distance
            elif direction == "forward":
                forward += distance
                down += (aim * distance)

        return down * forward

    @staticmethod
    def parse_input(command: str) -> (str, int):
        cmd = command.split(" ")
        return cmd[0], int(cmd[1])
