import time
from aocd import get_data

def process(puzzle_input: str):
    puzzle_input = puzzle_input.split('\n')
    departure_time = int(puzzle_input[0])
    wait_time = departure_time + 1
    cur_bus_id = None
    bus_ids = puzzle_input[1].split(',')
    for bus_id in bus_ids:
        if bus_id == 'x':
            continue
        tmp = int(bus_id)
        if (tmp - (departure_time % tmp)) < wait_time:
            wait_time = (tmp - (departure_time % tmp))
            cur_bus_id = tmp

    return cur_bus_id * wait_time


def main():
    puzzle_input = get_data(day=13)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
