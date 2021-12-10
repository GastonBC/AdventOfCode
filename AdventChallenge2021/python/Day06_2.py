# This solution is instant
# Groups the fish by age in a custom dictionary all_fish { int: int }
# Then creates a new dict each day that takes the new ages and sums the count of the old dict

# At age 0, the count is moved to 8 without
# adding anything because they will be the only ones there

from collections import defaultdict
import Inputs

def get_input():
    fish = defaultdict(int)
    all_fish = Inputs.Day06()

    for f in all_fish:
        fish[int(f)] += 1
    
    return fish

def simulate(all_fish, days):
    for _ in range(days):
        new_fish = defaultdict(int)
        for age, count in all_fish.items():
            if age == 0:
                new_fish[6] += count
                new_fish[8] = count  
                                     
            
            else:
                new_fish[age-1] += count

        all_fish = new_fish
    return sum(all_fish.values())

all_fish = get_input()
print(f'Part one answer: {simulate(all_fish, 80)}')
print(f'Part one answer: {simulate(all_fish, 256)}')




'''This is my solution, runs out of memory at day 130-140'''

# import Inputs

# sample = [3,4,3,1,2]

# class Lanternfish:
#     def __init__(self, age):
#         self.age = age
    
#     def create_new_check(self):
#         if self.age < 0:
#             self.age = 6
#             return Lanternfish(8)

#         else:
#             return None

#     def day_passed(self):
#         self.age -= 1

# lanternfish_lst = [age for age in sample]

# for day_n in range(0, 80):
#     print("{} - {}".format(day_n, len(lanternfish_lst)))
#     for idx, lanternfish in enumerate(lanternfish_lst.copy()):
#         lanternfish_lst[idx] =- 1
#         if lanternfish_lst[idx] < 0:
#             lanternfish_lst[idx] = 6
#             lanternfish_lst.append(8)
            

# print(len(lanternfish_lst))

'''
sample = 5934
answer = 1604361182149
'''
