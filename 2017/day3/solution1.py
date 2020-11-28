# Since we're trying to build a spiral, we're going to do it using a psuedo-Fibonacci sequence, whilst tracking how large side is, ideally.
import math
# First, we need to build the spiral itself.

# Set the target number.
target = 277678 

# The way to build the spiral is using a building block, so let's set this.
increment = .5

# Where we hold the information on what number we're currently on. 
curSum = 1

# A flag to track when we should stop the while loop.
notFound = True

# How many times have we added a side to the spiral before we found the target?
sidesAdded = 0
curCoords = [0,0]

while(notFound):
    increment += .5
    curSum += math.floor(increment)
    # After incrementing things, check to see if we've found the target number yet.
    if(curSum > target):
        notFound = False
    sidesAdded = sidesAdded + 1
    # Create a coordinate system based on the original 1 being the center of the spiral.
    if(sidesAdded % 4 == 1):
        curCoords[0] = curCoords[0] + math.floor(increment)
    elif(sidesAdded % 4 == 2):
        curCoords[1] = curCoords[1] + math.floor(increment)
    elif(sidesAdded % 4 == 3):
        curCoords[0] = curCoords[0] - math.floor(increment)
    elif(sidesAdded % 4 == 0):
        curCoords[1] = curCoords[1] - math.floor(increment)



if(sidesAdded % 4 == 1):
    curCoords[0] = curCoords[0] - (curSum - target)
elif(sidesAdded % 4 == 2):
    curCoords[1] = curCoords[1] - (curSum - target) 
elif(sidesAdded % 4 == 3):
    curCoords[0] = curCoords[0] + (curSum - target)
elif(sidesAdded % 4 == 0):
    curCoords[1] = curCoords[1] + (curSum - target)

steps = 0
steps = abs(curCoords[0]) + abs(curCoords[1])
print("Final: " + str(steps))
