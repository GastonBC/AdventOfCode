import Inputs

answer = 0

# [min-max, letter:, password]
for entry in Inputs.Day02():

    entry = entry.split(" ")

    min = int(entry[0].split("-")[0])
    
    max = int(entry[0].split("-")[1])

    letter = entry[1][:-1]

    password = entry[2]


    # ^ = xor operand. exclusive or, one or the other, not both
    if (password[min-1] == letter) ^ (password[max-1] == letter):
        answer += 1

print(answer)

assert answer==321