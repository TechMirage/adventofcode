import time
from aocd import get_data

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
    return element 


def main():
    puzzle_input = get_data(day=9)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
