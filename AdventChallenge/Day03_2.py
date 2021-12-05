import Inputs
from collections import Counter

# not working, seems to be a problem when there are 2 elements remaining in a list

def most_common_at_idx(idx, lst):
    idx_lst = []
    for item in lst:
        idx_lst.append(item[idx])
    return most_common_n(idx_lst)[-1] #return -1 index to prevent the "-" from passing

def least_common_at_idx(idx, lst):
    idx_lst = []

    for item in lst:
        idx_lst.append(item[idx])

    return least_common(idx_lst)

def most_common_n(lst):
    data = Counter(lst)

    two_most_common = data.most_common(2)
    # draw condition, draw in the counting
    if two_most_common[0][1] == two_most_common[1][1]:
        return '-1'

    return two_most_common[0][0]

def least_common(lst):
    common = most_common_n(lst)

    # draw condition
    if common == "-1":
        return '0'

    elif common == "1":
        return "0"

    elif common == "0":
        return "1"

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

# power_input = Inputs.Day03()
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

    # if len(o2_rating) == 2: # TODO this is to be fixed, the filter does not remove items
    #                         # if only two items and a it's draw is left
    #     o2_code = [i for i in o2_rating if i[-1] == "1"][0]
    #     break

    char = most_common_at_idx(idx, o2_rating)
    for item in o2_rating.copy():
        if item[idx] != char:
            o2_rating.remove(item)
            

# --- co2 ---
for idx in range(0, len(power_input[0])):
    
    if len(co2_rating) == 1:
        co2_code = co2_rating[0]
        break

    char = least_common_at_idx(idx, co2_rating)

    for item in co2_rating.copy():
        if item[idx] != char:
            co2_rating.remove(item)

print(o2_rating)
print(co2_code)

print("o2_code in binary: {}".format(o2_code))
print("co2_code in binary: {}".format(co2_code))
print()
print("o2_code in int: {}".format(int(o2_code, 2)))
print("co2_code in int: {}".format(int(co2_code, 2)))
print()
print("Result: {}".format(int(o2_code, 2)*int(co2_code, 2)))