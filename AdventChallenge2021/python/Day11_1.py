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


puz_arr = np.array(sample)
steps = 2

for i in range(steps):
    puz_arr += 1
    print(puz_arr)
    while np.any(puz_arr > 9):

        # find indices of elems bigger than 9
        for idx in np.transpose(np.nonzero(puz_arr > 9)):
            top = [idx[0]-1:idx[1]]
            right = None
            down = None
            left = None
            top = None
            print(f"idx {idx}, top {top}")

        puz_arr = np.where(puz_arr < 10, puz_arr, 0) # returns an array where the 10s are 
                                        # converted to 0

        