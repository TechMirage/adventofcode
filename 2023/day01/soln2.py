with open("./input.txt", "+r") as f:
    coming_in = f.readlines()

list_of_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
list_of_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
final_sum = 0
for line in coming_in:
    stuff_n_things = []
    tmp = 0
    idx = 0
    for num, x in zip(list_of_numbers, range(9)):
        if num in line:
            if line.index(num) != line.rindex(num):
                stuff_n_things.append([line.rindex(num), str(x+1)])
            idx = line.index(num)
            stuff_n_things.append([idx, str(x+1)])
    for num, x in zip(list_of_nums, range(9)):
        if num in line:
            if line.index(num) != line.rindex(num):
                stuff_n_things.append([line.rindex(num), str(x+1)])
            idx = line.index(num)
            stuff_n_things.append([idx, str(x+1)])
    if stuff_n_things:
        stuff_n_things = sorted(stuff_n_things)
        final_sum += int(stuff_n_things[0][1] + stuff_n_things[-1][1])
    
print("The answer is " + str(final_sum))