import Inputs
import numpy as np

power_input = Inputs.Day03()

gamma = ""
epsilon = ""
rows, cols = power_input.shape

for col in range(cols):
    gamma += str(np.bincount(power_input[:,col]).argmax())
    epsilon += str(np.bincount(power_input[:,col]).argmin())



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
    
    