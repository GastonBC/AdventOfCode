import Inputs
import string

input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines()

input = Inputs.Day03()

# Priority starts with index 1
abc = " " + string.ascii_lowercase
ABC = string.ascii_uppercase

priority = abc + ABC

value_sum = 0

for idx in range(0, len(input), 3):
    
    contents1 = input[idx]
    contents2 = input[idx+1]
    contents3 = input[idx+2]

    common = list(set(contents1).intersection(contents2).intersection(contents3))
    
    value_sum += priority.index(common[0])
    
print(value_sum)

assert value_sum == 2569