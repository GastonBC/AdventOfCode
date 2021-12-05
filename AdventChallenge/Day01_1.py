import Inputs

measurements = Inputs.Day01()

increase_count = 0

for idx, m in enumerate(measurements):
    if idx == 0:
        continue

    if m > measurements[idx-1]:
        increase_count += 1

print(increase_count)

'''1715'''