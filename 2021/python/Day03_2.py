import numpy as np
import Inputs

def the_common(arr, col, least = False):
    '''Returns the most common number (1 or 0) at the given
    column. If least is true, returns the least common.'''
    rows, _ = arr.shape
    col_sum = arr.sum(axis=0)

    # More 0s than 1s
    if col_sum[col] < rows/2:
        if least: return 1
        return 0

    # More 1s than 0s
    elif col_sum[col] > rows/2:
        if least: return 0
        return 1
        
    # Equal ammount
    else:
        return -1

o2_code = Inputs.Day03()
co2_code = Inputs.Day03()

rows, cols = o2_code.shape


for col in range(cols):
    most_com = the_common(o2_code, col)
    
    if most_com == -1:
        o2_code = o2_code[np.where(o2_code[:,col] == 1)]
    
    else:
        # This 'where' keeps the rows that, at the specified column
        # have a the most common number
        o2_code = o2_code[np.where(o2_code[:,col] == most_com)]
        
    # If only one row left, thats our answer
    rows, cols = o2_code.shape
    if rows == 1:
        o2_code = o2_code.flatten()
        break
    

# Need to have two for loops because they may break at different moments
for col in range(cols):
    most_com = the_common(co2_code, col, True)
    # False return
    if most_com == -1:
        co2_code = co2_code[np.where(co2_code[:,col] == 0)]
    
    else:
        co2_code = co2_code[np.where(co2_code[:,col] == most_com)]
        
    rows, cols = co2_code.shape
    if rows == 1:
        co2_code = co2_code.flatten()
        break
    
# Remove brackets, spaces and commas
# and finally convert to base 10
o2_code = np.array2string(o2_code, separator="")[1:-1]
co2_code = np.array2string(co2_code, separator="")[1:-1]

print("o2_code in binary: {}".format(o2_code))
print("co2_code in binary: {}".format(co2_code))
print()
print("o2_code in int: {}".format(int(o2_code, 2)))
print("co2_code in int: {}".format(int(co2_code, 2)))
print()
print("Result: {}".format(int(o2_code, 2)*int(co2_code, 2)))

assert int(o2_code, 2)*int(co2_code, 2) == 5736383

'''
110111111111
011001000001
o2_code in binary: 110111111111
co2_code in binary: 011001000001

o2_code in int: 3583
co2_code in int: 1601

Result: 5736383
'''