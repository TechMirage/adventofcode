import re

f = open("input.txt", "r")

topOfSomething = []
allItems = []

for line in f:
    try:
        found = re.search('-> (.+)',line).group(1)
    except:
        found = ''

    if(found != ''):
        things = found.split(', ')
        for item in things:
            topOfSomething.append(item)

    intro = re.search('^(.+) \(',line).group(1)
    allItems.append(intro)


f.close()

for item in allItems:
    try:
        notImportant = topOfSomething.index(item)
    except:
        botTower= item

print(botTower)
