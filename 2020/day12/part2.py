import time
from aocd import get_data

class ShipPosition():
    def __init__(self, puzzle_input):
        self.directions = puzzle_input.split('\n')
        self.cur_pos = [0, 0]
        self.waypoint = [10, 1]
        
    def __call__(self):
        for direction in self.directions:
            cmd, param = self.parse_direction(direction)
            if cmd == "N":
                self.waypoint[1] += param
            elif cmd == "S":
                self.waypoint[1] -= param
            elif cmd == 'E':
                self.waypoint[0] += param
            elif cmd == 'W':
                self.waypoint[0] -= param
            elif cmd == 'R':
                for _ in range(param // 90):
                    self.waypoint = [self.waypoint[1], -self.waypoint[0]]
            elif cmd == 'L':
                for _ in range(param // 90):
                    self.waypoint = [-self.waypoint[1], self.waypoint[0]]
            elif cmd == 'F':
                self.cur_pos[1] += self.waypoint[1] * param
                self.cur_pos[0] += self.waypoint[0] * param

        return self.manhattan_distance()

    @staticmethod
    def parse_direction(direction):
        return direction[0], int(direction[1:])

    def manhattan_distance(self):
        return abs(self.cur_pos[0]) + abs(self.cur_pos[1])

def process(puzzle_input: str):
    ship_pos = ShipPosition(puzzle_input)
    return ship_pos()


def main():
    puzzle_input = get_data(day=12)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
