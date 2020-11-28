# techmirage - Advent of Code 2018 Day 3 / Part b
import time
import re

t0 = time.time()
filepath = 'InputData.txt'
with open(filepath) as fp:
    line = fp.readline()
    p = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
    w = h = 1000
    cloth = [[0 for x in range(w)] for y in range(h)]
    count = 0
    while line:
        lineGroups = p.match(line)

        swatchID = int(lineGroups.group(1))
        xstart = int(lineGroups.group(2))
        ystart = int(lineGroups.group(3))
        xdist = int(lineGroups.group(4))
        ydist = int(lineGroups.group(5))

        for x in range(xstart, xstart + xdist):
            for y in range(ystart, ystart + ydist):
                cloth[x][y] += 1

        line = fp.readline()

with open(filepath) as fp:
    line = fp.readline()
    p = re.compile(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)')
    while line:
        theOne = True
        lineGroups = p.match(line)

        swatchID = int(lineGroups.group(1))
        xstart = int(lineGroups.group(2))
        ystart = int(lineGroups.group(3))
        xdist = int(lineGroups.group(4))
        ydist = int(lineGroups.group(5))

        for x in range(xstart, xstart + xdist):
            for y in range(ystart, ystart + ydist):
                if cloth[x][y] >= 2:
                    theOne = False

        if theOne:
            print(swatchID)
            break

        line = fp.readline()

t1 = time.time()
print(t1-t0)
