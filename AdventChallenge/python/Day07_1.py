import statistics
import Inputs

sample = [16,1,2,0,4,2,7,1,2,14]

puzzle_input = Inputs.Day07()
# puzzle_input = sample

closest_point = statistics.median(puzzle_input)

fuel_usage = 0
for crab in puzzle_input:
    fuel_usage += abs(crab-closest_point)

print(f'Closest point is: {closest_point}')
print(f'Total fuel usage: {fuel_usage}')

'''
Closest point is: 313.0
Total fuel usage: 344297.0
'''