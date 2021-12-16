import Inputs
from collections import Counter

power_input = Inputs.Day03()

gamma = ""
epsilon = ""


for idx in range(0, len(power_input[0])):
    count_0 = 0
    count_1 = 0

    for byt in power_input:
        if byt[idx] == "0":
            count_0 += 1

        elif byt[idx] == "1":
            count_1 += 1

    if count_0 > count_1:
        gamma += "0"
        epsilon += "1"

    elif count_0 < count_1:
        gamma += "1"
        epsilon += "0"

print("Gamma in binary: {}".format(gamma))
print("Epsilon in binary: {}".format(epsilon))
print()
print("Gamma in int: {}".format(int(gamma, 2)))
print("Epsilon in int: {}".format(int(epsilon, 2)))
print()
print("Result: {}".format(int(gamma, 2)*int(epsilon, 2)))

assert int(gamma, 2)*int(epsilon, 2) ==  3277364

'''
Gamma in bytes: 101110111100
Epsilon in bytes: 010001000011

Gamma in int: 3004
Epsilon in int: 1091

Result: 3277364
'''
    
    