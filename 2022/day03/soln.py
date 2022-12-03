from puzzle_input import puzzle_input, test_input

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_priority(char):
    return priority.rfind(char) + 1


def part_one(rucksacks):
    total_priority = 0
    found_list = []
    for sack in rucksacks:
        if sack == '':
            continue
        n = int(len(sack) / 2)
        first = sack[:n]
        second = sack[n:]
        found = 0
        for item in first:
            if item in second:
                found = item
                found_list.append(item)
                break
        if not found:
            print('This is a failed sack:', sack, len(sack))
            print('This is the first part:', first, len(first))
            print('This is the second part:', second, len(second))
        total_priority += get_priority(found)

    print("ANS: The total priority of all items in the rucksacks is:", total_priority)
    print("The total number of sacks is:", len(rucksacks))
    print("The total number of shared items is:", len(found_list))


def part_two(rucksacks):
    num_of_groups = (len(rucksacks)) // 3
    total_priority = 0
    found_list = []
    for group in range(num_of_groups):
        found = 0
        for item in rucksacks[group * 3]:
            if item in rucksacks[group * 3 + 1] and item in rucksacks[group * 3 + 2]:
                found = item
                found_list.append(item)
                break
        if not found:
            print('First in failed group', rucksacks[group * 3])
            print('Second in failed group', rucksacks[group * 3 + 1])
            print('Third in failed group', rucksacks[group * 3 + 2])
        total_priority += get_priority(found)

    print("ANS: The total priority of all items in the rucksacks is:", total_priority)
    print("The total number of groups is:", num_of_groups)
    print("The total number of shared items is:", len(found_list))


def main():
    print("--- TESTING PART ONE ---")
    rucksacks = test_input.split('\n')
    rucksacks.remove('')
    rucksacks.remove('')
    part_one(rucksacks)
    print("--- TESTING PART TWO ---")
    part_two(rucksacks)    
    print("--- PART ONE SOLUTION ---")
    rucksacks = puzzle_input.split('\n')
    rucksacks.remove('')
    rucksacks.remove('')
    part_one(rucksacks)
    print("--- PART TWO SOLUTION ---")
    part_two(rucksacks)


if __name__ == "__main__":
    main()