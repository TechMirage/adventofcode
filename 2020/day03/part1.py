import time
from aocd import get_data

def process(line: str):
    puzzle_input = line.split("\n")
    length = len(puzzle_input[0])
    pos_counter = 0
    tree_counter = 0
    for line in puzzle_input:
        pos_counter = pos_counter % length
        if line[pos_counter] == '#':
            tree_counter += 1
        pos_counter += 3 # The slope is 3 left, 1 down.
    return tree_counter 


def main():
    puzzle_input = get_data(day=3)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
