class SantaTracker():
    def __init__(self):
        self.been_there = [[0, 0]]
        self.cur_pos = [0, 0]

    def move_east(self):
        self.cur_pos[0] += 1
        self.check_been_there()

    def move_west(self):
        self.cur_pos[0] -= 1
        self.check_been_there()

    def move_north(self):
        self.cur_pos[1] += 1
        self.check_been_there()

    def move_south(self):
        self.cur_pos[1] -= 1
        self.check_been_there()

    def check_been_there(self):
        if self.cur_pos not in self.been_there:
            self.been_there.append(self.cur_pos.copy())

    def process(self, line):
        for char in line:
            if char == '^':
                self.move_north()
            elif char == '>':
                self.move_east()
            elif char == '<':
                self.move_west()
            elif char == 'v':
                self.move_south()


def main():
    santa = SantaTracker()
    santa2 = SantaTracker()
    robo_santa = SantaTracker()

    s2 = []
    rs = []
    with open('input.txt') as f:
        for line in f:
            santa.process(line)
            for idx in range(len(line)):
                if idx % 2 == 0:
                    s2.append(line[idx])
                else:
                    rs.append(line[idx])
            santa2.process(s2)
            robo_santa.process(rs)

    overlap = [value for value in santa2.been_there if value in robo_santa.been_there]
    ans2 = len(santa2.been_there) + len(robo_santa.been_there) - len(overlap)

    print("Santa has visited this many houses:", len(santa.been_there))
    print("Santa and Robo-Santa have visited this many houses:", ans2)


if __name__ == "__main__":
    main()
