# techmirage - Advent of Code Day 5 / part b
import time

t0 = time.time()

with open('InputData.txt') as fp:
    mainStr = fp.readline()

charOptions = []
lengthOptions = []

for x in mainStr:
    x = x.lower()
    if x not in charOptions:
        charOptions.append(x)

for charRemoval in charOptions:
    testStr = mainStr.replace(charRemoval, '')
    testStr = testStr.replace(charRemoval.upper(), '')

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

    lengthOptions.append(len(testStr))

lengthOptions.sort()
print(lengthOptions[0])

t1 = time.time()
print(t1 - t0)
