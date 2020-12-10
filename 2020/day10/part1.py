import time
from aocd import get_data


def process(puzzle_input: list):
    diff_three = 0
    diff_one = 0
    puzzle_input.append(0)
    puzzle_input.sort()
    puzzle_input.append(puzzle_input[-1] + 3)
    for i in range(len(puzzle_input) - 1):
        if puzzle_input[i] + 3 == puzzle_input[i + 1]:
            diff_three += 1
        if puzzle_input[i] + 1 == puzzle_input[i + 1]:
            diff_one += 1

    return diff_one * diff_three


def main():
    puzzle_input = get_data(day=10)
    puzzle_input = puzzle_input.split('\n')
    for i in range(len(puzzle_input)):
        puzzle_input[i] = int(puzzle_input[i])

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
