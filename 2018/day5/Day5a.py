# techmirage - Advent of Code Day 5 / part a
import time

t0 = time.time()

with open('InputData.txt') as fp:
    testStr = fp.readline()

noChangesMade = False

while not noChangesMade:
    noChangesMade = True
    for x in range(0, len(testStr) - 1):
        if not noChangesMade:
            break
        if len(testStr) == x-1:
            break
        if testStr[x].isupper() and testStr[x].lower() == testStr[x + 1]:
            testStr = testStr.replace(testStr[x:x + 2], '')
            noChangesMade = False
        elif testStr[x].islower() and testStr[x].upper() == testStr[x + 1]:
            testStr = testStr.replace(testStr[x:x + 2], '')
            noChangesMade = False

print(len(testStr))
t1 = time.time()
print(t1 - t0)
