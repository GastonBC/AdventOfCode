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

for rucksack in input:
    half_len = int(len(rucksack)/2)
    contents1 = rucksack[:half_len]
    contents2 = rucksack[half_len:]

    common = list(set(contents1).intersection(contents2))
    
    value_sum += priority.index(common[0])


print(value_sum)

assert value_sum == 7763