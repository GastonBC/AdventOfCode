import Inputs

elves = Inputs.Day01()

top_three = 0

total_per_elve = []

for elve in elves:
    calories = [int(x) for x in elve.split("\n")]
    total_per_elve.append(sum(calories))

total_per_elve.sort(reverse=True)

top_three = sum(total_per_elve[:3])

print(top_three)

assert top_three == 203002