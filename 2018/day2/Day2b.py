# techmirage - Advent of Code 2018 Day 2 / Part b
import time

t0 = time.time()

filepath = 'InputData.txt'
testingWords = []
with open(filepath) as fp:
    line = fp.readline()
    while line:
        testingWords.append(line)
        line = fp.readline()

with open(filepath) as fp:
    line = fp.readline()
    notFound = True
    while line and notFound:
        for place in range(0, len(testingWords)-1):
            i = 0
            differences = 0
            for i in range(0, len(line)-1):
                if line[i] != testingWords[place][i]:
                    differences = differences + 1
            if differences == 1:
                notFound = False
                trueWords = [line, testingWords[place]]
                break
        line = fp.readline()

    print(trueWords)
t1 = time.time()
print(t1-t0)