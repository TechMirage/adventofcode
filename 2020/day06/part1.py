import time
from aocd import get_data

def count_question(group):
    question_list = []
    for char in group:
        if char not in question_list:
            question_list.append(char)
    return len(question_list)

def process(puzzle_input: str):
    groups = puzzle_input.split("\n\n")
    counts = 0
    for group in groups:
        tmp = group.replace('\n', '')
        counts += count_question(tmp)
    return counts 


def main():
    puzzle_input = get_data(day=6)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
