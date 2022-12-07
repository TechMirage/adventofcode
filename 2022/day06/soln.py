from puzzle_input import puzzle_input, test_input


def part_one(input_):
    group_size = 4
    for x in range(group_size - 1, len(input_)):
        tmp = input_[x - group_size + 1: x + 1]
        if len(set(tmp)) == group_size:
            break

    print("ANS: This many spaces before the first start-of-packet marker:", x + 1)


def part_two(input_):
    group_size = 14
    for x in range(group_size - 1, len(input_)):
        tmp = input_[x - group_size + 1: x + 1]
        if len(set(tmp)) == group_size:
            break

    print("ANS: This many spaces before the first start-of-message marker:", x + 1)


def main():
    print("--- TESTING PART ONE ---")
    part_one(test_input)
    print("--- TESTING PART TWO ---")
    part_two(test_input)    
    print("--- PART ONE SOLUTION ---")
    part_one(puzzle_input)
    print("--- PART TWO SOLUTION ---")
    part_two(puzzle_input)

if __name__ == "__main__":
    main()