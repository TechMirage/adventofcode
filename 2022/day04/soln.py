from puzzle_input import puzzle_input, test_input
import re

pattern = re.compile(r"(.*)-(.*),(.*)-(.*)")


def part_one(sections):
    matching = 0
    for section in sections:
        results = pattern.search(section)
        first_set = set([x for x in range(int(results.group(1)), int(results.group(2)) + 1)])
        second_set = set([x for x in range(int(results.group(3)), int(results.group(4)) + 1)])
        intersection = first_set.intersection(second_set)
        if intersection == first_set or intersection == second_set:
            matching += 1
    
    print("ANS: There are this many matching pairs:", matching)


def part_two(sections):
    matching = 0
    for section in sections:
        results = pattern.search(section)
        first_set = set([x for x in range(int(results.group(1)), int(results.group(2)) + 1)])
        second_set = set([x for x in range(int(results.group(3)), int(results.group(4)) + 1)])
        intersection = first_set.intersection(second_set)
        if intersection:
            matching += 1
    
    print("ANS: The number of overlapping pairs is:", matching)


def main():
    print("--- TESTING PART ONE ---")
    sections = test_input.split('\n')
    part_one(sections)
    print("--- TESTING PART TWO ---")
    part_two(sections)    
    print("--- PART ONE SOLUTION ---")
    sections = puzzle_input.split('\n')
    part_one(sections)
    print("--- PART TWO SOLUTION ---")
    part_two(sections)

if __name__ == "__main__":
    main()