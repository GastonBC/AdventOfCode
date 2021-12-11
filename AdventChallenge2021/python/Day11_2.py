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

puz_arr = np.array(Inputs.Day11())
steps = 0
total_flashes = 0
while True:
    steps += 1
    puz_arr += 1
    
    # TODO center numbers are being affected by neighbors crashes, that shouldn't happen
    # all flashes occur at the same time
    
    # Temp solution is to ignore to_flash in the flash() func
    to_flash = np.transpose(np.nonzero(puz_arr > 9))
    flashed = []
    while len(to_flash):
        
        # find indices of elems bigger than 9
        for x, y in to_flash:
            if (x,y) not in flashed:
                box = np.s_[max(0, x - 1):x + 2, max(0, y - 1):y + 2]
                
                puz_arr[box] += 1
                flashed.append((x,y))

        to_flash = np.transpose(np.nonzero(puz_arr > 9))

        puz_arr = np.where(puz_arr <= 9, puz_arr, 0) # returns an array where the 10s are 
#                                                   # converted to 0       

    for x, y in flashed:
        puz_arr[x, y] = 0

    total_flashes+=len(flashed)
    print(f"AFTER DAY {steps}: {total_flashes} flashes")
        
    if (len(flashed) == puz_arr.size):
        print("All fish flashing at the same time!")
        break
        