import time
from aocd import get_data

class TreeMap():
    def __init__(self, puzzle_input):
        self.tree_map = puzzle_input.split("\n")
        self.length = len(self.tree_map[0])

    def __call__(self, left, down):
        pos_counter = 0
        tree_counter = 0
        cur_line = -1
        for line in self.tree_map:
            cur_line += 1
            if cur_line % down != 0:
                continue
            pos_counter = pos_counter % self.length
            if line[pos_counter] == '#':
                tree_counter += 1 
            pos_counter += left 
        return tree_counter

def process(line: str):
    tree_map = TreeMap(line)
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)] # Slope to calculate.
    tree_count_total = 1
    for left, down in slopes:
        trees = tree_map(left, down)
        tree_count_total = tree_count_total * trees
    return tree_count_total 


def main():
    puzzle_input = get_data(day=3)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
