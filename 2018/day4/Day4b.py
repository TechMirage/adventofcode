# techmirage - Advent of Code 2018 Day 4 / Part b
import time
import re
import operator

t0 = time.time()
filepath = 'InputTestData.txt'
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

hourMapping = [0]*60
guardIDList = {}
hoursListed = []

for line in dataLines:
    if line[3] not in ['W', 'F']:
        curGuard = line[3]
        if curGuard not in guardIDList:
            guardIDList[curGuard] = len(guardIDList)
            hoursListed.append(hourMapping)
    elif line[3] == 'F':
        startTime = line[2]
    else:
        for i in range(startTime, line[2]):
            hoursListed[guardIDList[curGuard]][i] += 1

maxListData = [0, 0, 0]
for x in range(0, len(hoursListed)):
    for y in range(0, 60):
        if hoursListed[x][y] > maxListData[0]:
            maxListData = [hoursListed[x][y], x+1, y]

print(maxListData)
print(guardIDList)

t1 = time.time()
print(t1-t0)
