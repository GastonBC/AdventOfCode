import Inputs

answer = 0

# [min-max, letter:, password]
for entry in Inputs.Day02():

    entry = entry.split(" ")

    min = int(entry[0].split("-")[0])
    
    max = int(entry[0].split("-")[1])

    letter = entry[1][:-1]

    password = entry[2]

    if password.count(letter) >= min and password.count(letter) <= max:
        answer += 1

assert answer == 607