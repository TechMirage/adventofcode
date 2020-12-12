import time
from aocd import get_data
from copy import deepcopy


class FerrySeats():
    FLOOR = '.'
    FULL = '#'
    EMPTY = 'L'
    def __init__(self, seat_layout: str):
        self.seats = []
        seat_layout = seat_layout.split('\n')
        for row in seat_layout:
            self.seats.append([char for char in row])
    
    def __call__(self):
        stable = False
        round_count = -1
        while not stable:
            round_count += 1
            temp_seats = deepcopy(self.seats)
            for x in range(len(self.seats)):
                for y in range(len(self.seats[0])):
                    if self.seats[x][y] == '.':
                        continue
                    visible = self.get_visible(x, y)
                    if self.seats[x][y] == 'L':
                        if self.check_for_empty(visible):
                            temp_seats[x][y] = '#'
                    else:
                        if self.check_for_full(visible):
                            temp_seats[x][y] = 'L'

            if self.check_for_change(temp_seats):
                stable = True
            else:
                self.seats = temp_seats

        return self.count_occupied()
            
    def count_occupied(self):
        count = 0
        for row in self.seats:
            count += row.count('#')
        return count

    def check_for_change(self, cur_seats):
        return cur_seats == self.seats
        
    def get_visible(self, x, y):
        adjacents = []
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            try:
                if (w:=self.seats[x + a][y]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            if x - a < 0:
                break
            try:
                if (w:=self.seats[x - a][y]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            try:
                if (w:=self.seats[x][y + a]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            if y - a < 0:
                break
            try:
                if (w:=self.seats[x][y - a]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            try:
                if (w:=self.seats[x + a][y + a]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            if y - a < 0:
                break
            try:
                if (w:=self.seats[x + a][y - a]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            if x - a < 0:
                break
            try:
                if (w:=self.seats[x - a][y + a]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break
        found = False
        for a in range(1, len(self.seats)):
            if found:
                break
            if x - a < 0 or y - a < 0:
                break
            try:
                if (w:=self.seats[x - a][y - a]) != ".":
                    adjacents.append(w)
                    found = True
            except IndexError:
                break

        return adjacents

    @staticmethod
    def check_for_empty(adjacents):
        return True if adjacents.count('#') == 0 else False

    @staticmethod
    def check_for_full(adjacents):
        return True if adjacents.count('#') >= 5 else False
                        

def process(puzzle_input: str):
    ferry = FerrySeats(puzzle_input)
    return ferry()


def main():
    puzzle_input = get_data(day=11)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
