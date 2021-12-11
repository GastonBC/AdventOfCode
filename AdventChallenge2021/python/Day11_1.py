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

def neighbours(arr, idx):
    '''Returns (top, 
                topR, 
                right, 
                rightD, 
                down, 
                downL, 
                left, 
                leftT'''
    
    top = None
    topR = None
    right = None
    rightD = None
    down = None
    downL = None
    left = None
    leftT = None

    shape = np.shape(arr)
    shape = (shape[0]-1, shape[1]-1) # make zero based

    # Top
    if idx[0] != 0:
        top = arr[idx[0]-1, idx[1]]
    
    # Top right
    if idx[0] != 0 and idx[1] != shape[1]:
        topR = arr[idx[0]-1, idx[1]+1]
    
    # Right
    if idx[1] != shape[1]:
        right = arr[idx[0], idx[1]+1]
    
    # Right down
    if idx[0] != shape[0] and idx[1] != shape[1]:
        rightD = arr[idx[0]+1, idx[1]+1]
    
    # Down
    if idx[0] != shape[0]:
        down = arr[idx[0]+1, idx[1]]
    
    # Down left
    if idx[0] != shape[0] and idx[1] != 0:
        downL = arr[idx[0]+1, idx[1]-1]
    
    # Left
    if idx[1] != 0:
        left = arr[idx[0], idx[1]-1]
    
    # Left top
    if idx[0] != 0 and idx[1] != 0:
        leftT = arr[idx[0]-1, idx[1]-1]

    return (top, topR, right, rightD, down, downL, left, leftT)

import numpy as np


puz_arr = np.array(sample)
steps = 2

for i in range(steps):
    puz_arr += 1
    print(puz_arr)
    while np.any(puz_arr > 9):

        # find indices of elems bigger than 9
        for idx in np.transpose(np.nonzero(puz_arr > 9)):
            neigh = neighbours(puz_arr, idx)

            print(f"idx        {idx}")
            print(f"top        {neigh[0]}")
            print(f"top right  {neigh[1]}")
            print(f"right      {neigh[2]}")
            print(f"right down {neigh[3]}")
            print(f"down       {neigh[4]}")
            print(f"down left  {neigh[5]}")
            print(f"left       {neigh[6]}")
            print(f"left top   {neigh[7]}")


        puz_arr = np.where(puz_arr < 10, puz_arr, 0) # returns an array where the 10s are 
                                        # converted to 0

        