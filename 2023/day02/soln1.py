def make_input(coming_in):
    games_list = dict()
    # example -> Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    for line in coming_in:
        tmp = line.split(":")
        x = tmp[0].split(" ")
        game_num = int(x[-1].strip())
        tmp = tmp[1].split(";")
        all_rounds = []
        for round in tmp:
            tmp2 = round.split(",")
            for specific in tmp2:
                tmp3 = specific.strip().split(" ")
                num = int(tmp3[0].strip())
                color = tmp3[-1].strip()[0]
                all_rounds.append([color, num])
        games_list[game_num] = sorted(all_rounds)
    return games_list

with open("./input.txt", "+r") as f:
    coming_in = f.readlines()

SOLN = {
    'b': 14,
    'g': 13,
    'r': 12
}

games_list = make_input(coming_in)
valid_games = []

for id in games_list.keys():
    useless = False
    for round in games_list[id]:
        if round[1] > SOLN[round[0]]:
            useless = True
            break
    if useless:
        continue
    else:
        valid_games.append(id)

final_sum = 0
for id in valid_games:
    final_sum += id

print("Final answer is", final_sum)