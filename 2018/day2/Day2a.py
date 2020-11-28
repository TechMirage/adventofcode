# techmirage - Advent of Code 2018 Day 2 / Part a
import time
from collections import Counter

t0 = time.time()
filepath = 'InputData.txt'
numTwice = 0    # How many have two repeated characters
numThrice = 0   # How many have three repeated characters
with open(filepath) as fp:
    line = fp.readline()
    while line:
        charsCounted = []
        histogram = Counter(line)
        threeCounted = False
        twoCounted = False
        for x in line:
            if x not in charsCounted:
                if histogram[x] == 3 and not threeCounted:
                    numThrice = numThrice + 1
                    threeCounted = True
                elif histogram[x] == 2 and not twoCounted:
                    numTwice = numTwice + 1
                    twoCounted = True
                charsCounted.append(x)
        line = fp.readline()

print(numTwice * numThrice)
t1 = time.time()
print(t1-t0)