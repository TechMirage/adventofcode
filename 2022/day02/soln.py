from puzzle_input import puzzle_input

def modify_guide(guide):
    for round in guide:
        # supposed to lose here.
        if round[1] == 0:
            round[1] = (round[0] - 1) % 3
        # supposed to draw here
        elif round[1] == 1:
            round[1] = (round[0]) % 3
        # supposed to win here
        elif round[1] == 2:
            round[1] = (round[0] + 1) % 3

    return guide


def round_score(round):
    # you get a certain amount of points just for playing a round
    # rock 1, paper 2, scissors 3
    score = round[1] + 1

    tmp = (round[1] - round[0]) % 3
    # first, if we draw
    if tmp == 0:
        score += 3
    # next, if we win
    elif tmp == 1:
        score += 6
    # next if we lose
    elif tmp == 2:
        score += 0

    return score


def calculate_score(guide):
    total_score = 0
    for round in guide:
        total_score += round_score(round)

    return total_score


def main():
    guide = puzzle_input
    guide = guide.replace("A", "0") 
    guide = guide.replace("B", "1")
    guide = guide.replace("C", "2")
    guide = guide.replace("X", "0")
    guide = guide.replace("Y", "1")
    guide = guide.replace("Z", "2")
    
    guide = guide.split("\n")
    tmp = []
    for step in guide:
        if step != "":
            step = step.split(" ")
            step = [int(i) for i in step]
            tmp.append(step)
    guide = tmp
    
    print("And there are this many steps in the strategy guide:", len(guide))

    total_score = calculate_score(guide)
    print("And the total score of the guide for Part 1 is:", total_score)

    guide = modify_guide(guide)
    total_score = calculate_score(guide)
    print("And the total score of the guide for Part 2 is:", total_score)



if __name__ == "__main__":
    main()