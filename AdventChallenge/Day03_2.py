import Inputs
from collections import Counter

def most_common_at_idx(idx, lst):
    idx_lst = []
    for item in lst:
        idx_lst.append(item[idx])
    return most_common(idx_lst)

def least_common_at_idx(idx, lst):
    idx_lst = []

    for item in lst:
        idx_lst.append(item[idx])
    return least_common(idx_lst)

def most_common(lst):
    data = Counter(lst)
    two_most_common = data.most_common(2)

    # draw condition
    if two_most_common[0][1] == two_most_common[1][1]:
        return '1'

    return two_most_common[0][0]

def least_common(lst):
    data = Counter(lst)
    two_least_common = data.most_common(len(lst))

    # draw condition
    if two_least_common[-1][1] == two_least_common[-2][1]:
        return '1'

    return two_least_common[-1][0]


sample = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]

power_input = sample

# o2_rating
# co2_rating
# life_rating = o2_rating*co2_rating

# start with all the values
# gets the most number each digit
o2_rating = power_input.copy()
o2_code = ""

# gets the least number each digit
co2_rating = power_input.copy()
co2_code = ""

for idx in range(0, len(power_input[0])):

    # --- o2 ---
    if len(o2_rating) == 1:
        o2_code = o2_rating[0]
        break

    char = most_common_at_idx(idx, o2_rating)
    
    for item in o2_rating.copy():
        if item[idx] != char:
            o2_rating.remove(item)

for idx in range(0, len(power_input[0])):
    # --- co2 ---
    if len(co2_rating) == 1:
        co2_code = co2_rating[0]
        break

    char = least_common_at_idx(idx, co2_rating)
    
    for item in co2_rating.copy():
        if item[idx] != char:
            co2_rating.remove(item)

print(o2_code)
print(co2_code)