from puzzle_input import puzzle_input

def main():
    puzzle_list = puzzle_input.split("\n\n")
    print('We have elves numbering:', len(puzzle_list))
    cal_counts = []
    for elf in puzzle_list:
        elf = elf.split('\n')
        sum = 0
        for item in elf:
            if item != '':
                sum += int(item)
        cal_counts.append(sum)

    cal_counts.sort()

    print('the highest calorie count elf has this many calories:', cal_counts[-1])
    print('the second highest calorie count elf has this many calories:', cal_counts[-2])
    print('the third highest calorie count elf has this many calories:', cal_counts[-3])
    print('For a total of the top three of:', (cal_counts[-1] + cal_counts[-2] + cal_counts[-3]))


if __name__ == "__main__":
    main()