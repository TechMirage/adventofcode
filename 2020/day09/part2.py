import time
from aocd import get_data

def find_range(full_list, summed):
    greater = False
    equal = False
    first, second = None, None 
    for i in range(len(full_list)):
        if greater:
            greater = False
        if equal:
            break
        cur_sum = full_list[i]
        for j in range(1, len(full_list[i:])):
            cur_sum += full_list[j + i]
            if cur_sum > summed:
                greater = True
                break
            if cur_sum == summed:
                equal = True
                first, second = i, j + i
                break

    tmp = full_list[first:second + 1]
    tmp.sort()

    return tmp[0] + tmp[-1]

def do_addition_muchly(preamble, being_checked):
    found = False 
    counter = 0
    for x in preamble:
        if found:
            break
        for y in preamble[counter + 1:]:
            if x + y == being_checked:
                found = True
                break
        counter += 1
    return found

def process(puzzle_input: str, preamble_size=25):
    puzzle_input = puzzle_input.split('\n')
    for i in range(len(puzzle_input)):
        puzzle_input[i] = int(puzzle_input[i])
    counter = preamble_size 
    for element in puzzle_input[preamble_size:]:
        if not do_addition_muchly(puzzle_input[counter - preamble_size:counter], element):
            break
        counter += 1
    return find_range(puzzle_input, element)


def main():
    puzzle_input = get_data(day=9)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
