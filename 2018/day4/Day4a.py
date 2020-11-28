# techmirage - Advent of Code 2018 Day 4 / Part a
import time
import re
import operator

t0 = time.time()
filepath = 'InputData.txt'
p = re.compile(r'\[\d+-(\d\d)-(\d\d) (\d\d):(\d\d)] (\w+) (\S+).+')

dataLines = []

with open(filepath) as fp:
    line = fp.readline()
    while line:
        lineGroups = p.match(line)

        lineMonth = int(lineGroups.group(1))
        lineDay = int(lineGroups.group(2))
        lineHour = int(lineGroups.group(3))
        lineMinute = int(lineGroups.group(4))
        if lineGroups.group(5) == 'Guard':
            lineID = lineGroups.group(6)
            lineID = lineID[1:]
            if lineHour == 23:
                lineDay = lineDay + 1
                lineMinute = 0
        elif lineGroups.group(5) == 'falls':
            lineID = 'F'
        else:
            lineID = 'W'

        dataLines.append([lineMonth, lineDay, lineMinute, lineID])

        line = fp.readline()

dataLines = sorted(dataLines, key=operator.itemgetter(0, 1, 2))

sleepTotalMinutes = {}
for line in dataLines:
    if line[3] not in ['W', 'F']:
        curGuard = line[3]
        if curGuard not in sleepTotalMinutes:
            sleepTotalMinutes[curGuard] = 0
    elif line[3] == 'F':
        startTime = line[2]
    else:
        sleepTotalMinutes[curGuard] += (line[2] - startTime)

maxGuardSleeping = max(sleepTotalMinutes.items(), key=operator.itemgetter(1))[0]

hourMapping = [0]*60
for line in dataLines:
    if line[3] not in ['W', 'F']:
        curGuard = line[3]
    if curGuard == maxGuardSleeping:
        if line[3] == 'F':
            startTime = line[2]
        elif line[3] == 'W':
            for i in range(startTime, line[2]):
                hourMapping[i] += 1

maxMin = hourMapping.index(max(hourMapping))

print(maxMin * int(maxGuardSleeping))
t1 = time.time()
print(t1-t0)
