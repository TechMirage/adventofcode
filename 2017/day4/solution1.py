import re
import math

f = open("input.txt", "r")
lineTemp = []
totalPasswords = 0

for line in f:
    lineTemp = line.split()
    okayPassword = True
    for word in lineTemp:
        i = [i for i,x in enumerate(lineTemp) if x == word]
        if(len(i) != 1):
            okayPassword = False
    if(okayPassword):
        totalPasswords = totalPasswords + 1
            
print(totalPasswords)

f.close()
