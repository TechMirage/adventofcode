import time
from aocd import get_data

def check_valid(passport_dict : dict):
    if len(passport_dict) < 7:
        return False
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required_keys:
        if key not in passport_dict.keys():
            return False
    return True

def process(puzzle_input: str):
    valid = 0
    puzzle_input = puzzle_input.split("\n\n")
    for passport in puzzle_input:
        tmp = passport.replace('\n', ' ')
        tmp = tmp.split(' ')
        tmp = dict(x.split(':') for x in tmp)
        if check_valid(tmp):
            valid += 1
    return valid 


def main():
    puzzle_input = get_data(day=4)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
