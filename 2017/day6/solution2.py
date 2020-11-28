import re

f = open("input.txt","r")


for line in f:
    baseList = re.split(r' +', line.rstrip('\n'))

f.close()
baseList = list(map(int, baseList))


repeatFound = False
stuffFound = []
stepsTaken = 0

while(not repeatFound):
    stepsTaken = stepsTaken + 1
    maxIndex = baseList.index(max(baseList))
    maxValue = max(baseList)
    baseList[maxIndex] = 0
    for r in range(1,maxValue + 1):
        counter = maxIndex + r
        baseList[counter % len(baseList)] = baseList[counter % len(baseList)] + 1
    try:
        if baseList in stuffFound:
            repeatFound = True
    except:
        pass
    stuffFound.append(baseList[:])

sizeLoop = stepsTaken - (stuffFound.index(baseList) + 1)
print(sizeLoop)
