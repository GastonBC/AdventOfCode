import statistics
import Inputs
import math
sample = [16,1,2,0,4,2,7,1,2,14]

puzzle_input = Inputs.Day07()
# puzzle_input = sample

def get_usage(puzzle, point):
    fuel_usage = 0
    for crab in puzzle:
        
        distance = abs(crab-round(point))

        fuel = sum(range(0, distance+1))

        fuel_usage += fuel
    
    return fuel_usage


# the "correct" mean will be +- 0.5 from the real mean so we'll have to test both to find the
# least fuel usage
closest_point = [statistics.mean(puzzle_input)+0.5, statistics.mean(puzzle_input)-0.5]

# +0.5
fuel_usage_1 = [round(closest_point[0]), 0]
fuel_usage_1[1] = get_usage(puzzle_input, fuel_usage_1[0])

# -0.5
fuel_usage_2 = [round(closest_point[1]), 0]
fuel_usage_2[1] = get_usage(puzzle_input, fuel_usage_2[0])

usages = [fuel_usage_1, fuel_usage_2]
min_usage = min(usages, key = lambda t: t[1])

print(f'Total fuel usage: {min_usage[1]} at {min_usage[0]}')

'''
Total fuel usage: 97164301
'''