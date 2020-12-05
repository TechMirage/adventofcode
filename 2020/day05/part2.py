import time
from aocd import get_data

def find_seat(find, high):
    low = 0
    for char in find[:-1]:
        if char == 'R' or char == 'B':
            low = high - ((high - low) // 2) 
        else:
            high = (high - low) // 2 + low 
    if find[-1] == 'L' or find[-1] == 'F':
        return low
    else:
        return high

def calc_id(col, row):
    return row * 8 + col

def process(puzzle_input: str):
    lines = puzzle_input.split("\n")
    id_list = []
    for line in lines:
        row = find_seat(line[:-3], 127)
        col = find_seat(line[-3:], 7)
        id_list.append(calc_id(col, row))

    id_list.sort() 
    for seat in id_list:
        if seat + 1 not in id_list:
            return seat + 1

    return -1 # Something went wrong and didn't find it.

def main():
    puzzle_input = get_data(day=5)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
