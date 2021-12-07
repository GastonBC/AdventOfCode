from decimal import ROUND_DOWN
import statistics
import Inputs
import math
sample = [16,1,2,0,4,2,7,1,2,14]

puzzle_input = Inputs.Day07()
# puzzle_input = sample




# the "correct" mean will be +- 0.5 from the real mean so will have to test both to find the
# least fuel usage
closest_point = [statistics.mean(puzzle_input)+0.5, statistics.mean(puzzle_input)-0.5]


# +0.5
fuel_usage_1 = [round(closest_point[0]), 0]
for crab in puzzle_input:

    distance = abs(crab-fuel_usage_1[0])

    fuel = sum(range(0, distance+1))
    # print(f'Crab: {crab}, distance: {distance}, fuel: {fuel}')

    fuel_usage_1[1] += fuel


# -0.5
fuel_usage_2 = [round(closest_point[1]), 0]
for crab in puzzle_input:

    distance = abs(crab-fuel_usage_2[0])

    fuel = sum(range(0, distance+1))
    # print(f'Crab: {crab}, distance: {distance}, fuel: {fuel}')

    fuel_usage_2[1] += fuel

usages = [fuel_usage_1, fuel_usage_2]

min_usage = min(usages, key = lambda t: t[1])

print(f'Total fuel usage: {min_usage[1]} at {min_usage[0]}')

'''
Total fuel usage: 97164301
'''