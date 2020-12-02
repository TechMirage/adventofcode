import time
from aocd import get_data
import argparse

def process(line: str):
    return ''

def parse_the_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help="the day", type=int)
    parser.add_argument('-y', help="the year, full four digits", type=int)

    args = parser.parse_args()
    return args

def main():
    args = parse_the_args()
    puzzle_input = get_data(day=1)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
