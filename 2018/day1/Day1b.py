# techmirage - Advent of Code 2018 Day 1 / Part b
import time
t0 = time.time()
filepath = 'InputData.txt'
havenotfound = True
coordsTouched = [0]
coords = 0
while havenotfound:
    with open(filepath) as fp:
        line = fp.readline()
        while line:
            coords = coords + int(line)
            if coords in coordsTouched and havenotfound:
                havenotfound = False
                coordRepeated = coords
            else:
                coordsTouched.append(coords)
            line = fp.readline()

print(coordRepeated)
t1 = time.time()

print(t1 - t0)
