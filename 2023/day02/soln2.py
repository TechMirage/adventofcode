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

games_list = make_input(coming_in)
power_rating = 0
for id in games_list.keys():
    max_amt = dict()
    for thing in games_list[id]:
        max_amt[thing[0]] = thing[1]
    tmp = 1
    for key in max_amt.keys():
        tmp = tmp * max_amt[key]
    power_rating += tmp

print("final answer is ", power_rating)
