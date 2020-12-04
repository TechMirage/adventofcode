import time
from aocd import get_data

def process(line: str):
    return ""


def main():
    puzzle_input = get_data(day=1)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
