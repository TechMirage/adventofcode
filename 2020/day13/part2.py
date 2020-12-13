import time
from aocd import get_data
from functools import reduce


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def process(puzzle_input: str):
    bus_ids = puzzle_input[0].split(',')
    for i in range(len(bus_ids)):
        if bus_ids[i] != 'x':
            bus_ids[i] = int(bus_ids[i])
    ids = []
    ans = []
    for i in range(len(bus_ids)):
        if bus_ids[i] != 'x':
            ids.append(bus_ids[i])
            ans.append(bus_ids[i] - i)
    return chinese_remainder(ids, ans)


def main():
    puzzle_input = get_data(day=13)
    puzzle_input = puzzle_input.split('\n')
    puzzle_input.pop(0)

    start_time = time.time()

    output = process(puzzle_input)

    stop_time = time.time()
    
    print("The answer is ", output)
    print("And it took about ", stop_time - start_time, " seconds to do it.")


if __name__ == "__main__":
    main()
