import numpy as np
import Inputs


forest = Inputs.Day08()

rows, cols = forest.shape

visible_trees = 0

for row in range(0, rows):
    for col in range(0, cols):

        up =    forest[0:row, col]
        right = forest[row, col+1:cols]
        down =  forest[row+1:rows, col]
        left =  forest[row, 0:col]

        sides = [up, right, down, left]

        try:
            if any([forest[row,col] > np.max(side) for side in sides]):
                visible_trees += 1 
        
        # edge case, always visible, exception raises because it's comparing
        # against an empty array
        except ValueError:
            visible_trees += 1 
            
print(visible_trees)