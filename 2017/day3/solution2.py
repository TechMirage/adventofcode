import math

target = 330
increment = 1
curSum = 1
notFound = True
sidesAdded = 0
curCoords = [0,0]
entries = {}

def createStrCoords(curCoords):
    return str(curCoords[0]) + "," + str(curCoords[1])

# Function to calculate the entry that we're currently on.
def calculateEntry(curCoords,entries):
    sumCalc = 0
    curX = curCoords[0]
    curY = curCoords[1]
    try:
        sumCalc += entries[str(curX-1)+"," +str(curY-1)]
    except:
        pass
    
    try:
        sumCalc += entries[str(curX) + "," + str(curY-1)]
    except:
        pass
    
    try:
        sumCalc += entries[str(curX+1) +"," + str(curY-1)]
    except:
        pass
    
    try:
        sumCalc += entries[str(curX-1) + "," + str(curY)]
    except:
        pass

    try:
        sumCalc += entries[str(curX+1)+","+str(curY)]
    except:
        pass

    try:
        sumCalc += entries[str(curX-1)+","+str(curY+1)]
    except:
        pass

    try:
        sumCalc += entries[str(curX)+","+str(curY+1)]
    except:
        pass

    try:
        sumCalc += entries[str(curX+1)+","+str(curY+1)]
    except:
        pass

    return sumCalc

# Set up the first entry!
entries[createStrCoords(curCoords)] = 1

while(notFound):
    increment += .5
    for x in range(1, math.floor(increment)):
        if(sidesAdded % 4 == 1):
            curCoords[0] = curCoords[0] + 1
            curSum = calculateEntry(curCoords,entries)
            entries[createStrCoords(curCoords)] = curSum
        elif(sidesAdded % 4 == 2):
            curCoords[1] = curCoords[1] + 1
            curSum = calculateEntry(curCoords,entries)
            entries[createStrCoords(curCoords)] = curSum
        elif(sidesAdded % 4 == 3):
            curCoords[0] = curCoords[0] - 1
            curSum = calculateEntry(curCoords,entries)
            entries[createStrCoords(curCoords)] = curSum
        elif(sidesAdded % 4 == 0):
            curCoords[1] = curCoords[1] - 1
            curSum = calculateEntry(curCoords,entries)
            entries[createStrCoords(curCoords)] = curSum
    sidesAdded = sidesAdded + 1
    print(entries)
    wait = input("Pausing")        
    if (curSum > target):
        notfound = False

print(entries)
