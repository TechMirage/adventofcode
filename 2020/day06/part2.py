import time
from aocd import get_data

def process(puzzle_input: str):
    groups = puzzle_input.split("\n\n")
    sum_of_all = 0
    for group in groups:
        qs_for_all = set("abcdefghijklmnopqrstuvwxyz")
        tmp = group.split('\n')
        for person in tmp: 
            qs_for_all = qs_for_all.intersection(set(person))
        sum_of_all += len(qs_for_all)
    return sum_of_all


def main():
    puzzle_input = get_data(day=6)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
