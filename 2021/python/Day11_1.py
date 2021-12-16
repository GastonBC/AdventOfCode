sample = [[5,4,8,3,1,4,3,2,2,3],
          [2,7,4,5,8,5,4,7,1,1],
          [5,2,6,4,5,5,6,1,7,3],
          [6,1,4,1,3,3,6,1,4,6],
          [6,3,5,7,3,8,5,4,7,8],
          [4,1,6,7,5,2,4,6,4,5],
          [2,1,7,6,8,4,1,7,2,1],
          [6,8,8,2,8,8,1,1,3,4],
          [4,8,4,6,8,4,8,5,5,4],
          [5,2,8,3,7,5,1,5,2,6]]


import numpy as np
import Inputs

puz_arr = Inputs.Day11()
steps = 101
total_flashes = 0

for i in range(1, steps):
    puz_arr += 1
    
    # Get indices of elements bigger than 9
    to_flash = np.transpose(np.nonzero(puz_arr > 9))

    # This list will be used to reset the counter of affected fishes more than once
    flashed = []

    while len(to_flash):
        for x, y in to_flash:

            # Do not add one to already affected fishes this step
            if (x,y) not in flashed:

                # Gets the 3x3 box around the element, if it's
                # a corner/edge situation, truncate the box
                box = np.s_[max(0, x - 1):x + 2, max(0, y - 1):y + 2]
                
                puz_arr[box] += 1
                flashed.append((x,y))

        to_flash = np.transpose(np.nonzero(puz_arr > 9))

        puz_arr = np.where(puz_arr <= 9, puz_arr, 0) # returns an array where the 10s are 
                                                     # converted to 0       

    # Reset the flashed fishes that have been affected more than once to 0
    for x, y in flashed:
        puz_arr[x, y] = 0

    total_flashes+=len(flashed)

print(f"AFTER DAY {i}: {total_flashes} flashes")

assert total_flashes == 1757
        
'''AFTER DAY 100: 1757 flashes'''