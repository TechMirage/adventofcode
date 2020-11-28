import re

f = open("inputtest.txt", "r")

allItems = {}

for line in f:
    programName = re.search('^(.+) \((.+)\)',line).group(1)
    programWeight =  int(re.search('^(.+) \((.+)\)',line).group(2))
    allItems[programName] = programWeight

print("allItems")
print(allItems)

f.close()
