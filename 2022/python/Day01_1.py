import Inputs

elves = Inputs.Day01()

most_calories = 0

for elve in elves:
    calories = [int(x) for x in elve.split("\n")]
    if most_calories < sum(calories):
        most_calories = sum(calories)

print(most_calories)

assert most_calories == 70369