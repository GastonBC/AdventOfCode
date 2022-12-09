import numpy as np
import Inputs


forest = Inputs.Day08()

rows, cols = forest.shape

best_score = 1

# is_negative to account for arrays that need to be reversed
def process(this_tree, sides, is_negative = False):
    score = 1
    for side in sides:
        counter = 0
        
        if is_negative: 
            side = np.flip(side)
        
        for tree in side:
            counter += 1
            if tree >= this_tree:
                break
            
        score = score*counter
    return score


for row in range(0, rows):
    for col in range(0, cols):
        
        tree_score = 1
        this_tree = forest[row, col]
        
        # up, right, down, left

        up =    forest[0:row, col]
        right = forest[row, col+1:cols]
        down =  forest[row+1:rows, col]
        left =  forest[row, 0:col]

        positive_sides = [right, down]
        negative_sides = [up, left]

        tree_score = tree_score*process(this_tree, positive_sides)
        
        tree_score = tree_score*process(this_tree, negative_sides, True)

        if tree_score > best_score:
            best_score = tree_score
            
            
print(best_score)

assert best_score == 496125