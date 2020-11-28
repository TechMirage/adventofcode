# techmirage - Advent of Code 2018 Day 6 / Part a
import time

t0 = time.time()
filepath = 'InputTestData.txt'
with open(filepath) as fp:
    line = fp.readline()
    while line:

        line = fp.readline()

t1 = time.time()
print(t1-t0)
