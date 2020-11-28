import re

f = open("input.txt", "r")

lineRe = re.compile('^(.+) (inc|dec) (.+) if (.+) ([>|<|=|\+|-|!]{0,2}) (.+)')
regValues = {}
regMax = 0

for line in f:
    regName = re.match(lineRe,line).group(1)
    regOps = re.match(lineRe,line).group(2)
    regOffset = re.match(lineRe,line).group(3)
    regReq = re.match(lineRe,line).group(4)
    regCond = re.match(lineRe,line).group(5)
    regCondReq = re.match(lineRe,line).group(6)
    if regName not in regValues:
        regValues[regName] = 0
    if regReq not in regValues:
        regValues[regReq] = 0

    doOps = False

    if(regCond == '>'):
        if(regValues[regReq] > int(regCondReq)):
            doOps = True
    elif(regCond == '>='):
        if(regValues[regReq] >= int(regCondReq)):
            doOps = True
    elif(regCond == '<'):
        if(regValues[regReq] < int(regCondReq)):
            doOps = True
    elif(regCond == '!='):
        if(regValues[regReq] != int(regCondReq)):
            doOps = True
    elif(regCond == '<='):
        if(regValues[regReq] <= int(regCondReq)):
            doOps = True
    elif(regCond == '=='):
        if(regValues[regReq] == int(regCondReq)):
            doOps = True

    if(doOps):
        if(regOps == 'inc'):
            regValues[regName] = regValues[regName] + int(regOffset)
        elif(regOps == 'dec'):
            regValues[regName] = regValues[regName] - int(regOffset)

    if(regValues[regName] > regMax):
        regMax = regValues[regName]

f.close()

print(regMax)
