import time
import re
from aocd import get_data

def check_valid(passport_dict : dict):
    if len(passport_dict) < 7:
        return False
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for key in required_keys:
        if key not in passport_dict.keys():
            return False

    # Value checking for each field, 
    # we know it as all the keys at this point.
    tmp = int(passport_dict['byr'])
    if tmp < 1920 or tmp > 2002:
        return False
    
    tmp = int(passport_dict['iyr'])
    if tmp < 2010 or tmp > 2020:
        return False

    tmp = int(passport_dict['eyr'])
    if tmp < 2020 or tmp > 2030:
        return False
    
    tmp = passport_dict['hgt']
    x = int(tmp[:-2])
    if tmp[-2:] == 'cm':
        if x < 150 or x > 193:
            return False
    else:
        if x < 59 or x > 76:
            return False

    tmp = passport_dict['hcl']
    x = tmp[0]
    tmp = tmp[1:]
    if x != '#':
        return False
    if len(tmp) != 6:
        return False
    if not re.match(r"[0-9a-f]", tmp):
        return False
        
    tmp = passport_dict['ecl']
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if tmp not in valid_eye_colors:
        return False
        
    tmp = passport_dict['pid']
    if len(tmp) != 9:
        return False
    try:
        tmp = int(tmp)
    except:
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
