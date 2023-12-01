with open("./input.txt", "+r") as f:
    coming_in = f.readlines()

final_sum = 0
for line in coming_in:
    stuff_n_things = ""
    for character in line:
        if character >= "0" and character <= "9":
            stuff_n_things += character
    output = stuff_n_things[0] + stuff_n_things[-1]
    final_sum += int(output)

print("The answer is " + str(final_sum))