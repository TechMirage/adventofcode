import time
from aocd import get_data
from PasswordChecker import PasswordChecker

def process(lines: str):
    checker = PasswordChecker()
    for line in lines:
        checker(line)
    return checker.valid_passwords 


def main():
    puzzle_input = get_data(day=2)
    puzzle_input = puzzle_input.split("\n")

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
