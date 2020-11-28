# techmirage - Advent of Code 2018 / Day 1 Part a
import time

t0 = time.time()
filepath = 'InputData.txt'
with open(filepath) as fp:
    line = fp.readline()
    coords = 0
    while line:
        coords = coords + int(line)
        line = fp.readline()

    print(coords)

t1 = time.time()
print(t1 - t0)
