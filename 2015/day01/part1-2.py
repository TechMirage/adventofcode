class WhereWeAre:
    def __init__(self):
        self._cur_pos = 0
        self.first_basement = None
        self._num_of_instructions = 0

    @property
    def cur_pos(self):
        return self._cur_pos

    def up_floor(self):
        self._cur_pos += 1
        self._num_of_instructions += 1
        self.check_for_basement()

    def down_floor(self):
        self._cur_pos -= 1
        self._num_of_instructions += 1
        self.check_for_basement()

    def check_for_basement(self):
        if self._cur_pos == -1 and not self.first_basement:
            self.first_basement = self._num_of_instructions


def process(line):
    where = WhereWeAre()
    for char in line:
        if char == '(':
            where.up_floor()
        elif char == ')':
            where.down_floor()

    print("we made it to floor", where.cur_pos)
    print("we found the basement on step #", where.first_basement)


def main():
    with open('input.txt') as f:
        for line in f:
            process(line)


if __name__ == "__main__":
    main()
