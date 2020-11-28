f = open("input.txt","r")

dirArray = []

for line in f:
    dirArray.append(line.rstrip())


f.close()
dirArray = list(map(int, dirArray))
index = 0
exited = False
travelAmt = 0
steps = 0
length = len(dirArray)

while(not exited):
    travelAmt = dirArray[index]
    if(travelAmt >= 3):
        dirArray[index] = dirArray[index] - 1
    else:
        dirArray[index] = dirArray[index] + 1
    index = index + travelAmt
    steps = steps + 1
    if(length <= index):
        exited = True

print(steps)    
