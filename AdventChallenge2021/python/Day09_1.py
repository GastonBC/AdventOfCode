'''
    0123456789

0   2199943210
1   3987894921
2   9856789892
3   8767896789
4   9899965678


'''

import Inputs
sample = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
         ]
         
puz_input = Inputs.Day09()


def is_low_point(val_map, index_tuple, value):
    '''Returns true if it's adyacent values are higher
    than the checked value.'''
    
    row = index_tuple[0]
    col = index_tuple[1]
    
    
    # check up
    if row != 0:
        val_up = int(val_map[row-1][col])
    else:
        val_up = 10 # If it's a corner/boundary situation, it's compared
                    # to 10 so that check will pass

    # check right
    if len(val_map[row]) != col+1:
        val_right = int(val_map[row][col+1])
    else:
        val_right = 10

    # check down
    if len(val_map) != row + 1:
        val_down = int(val_map[row+1][col])
    else:
        val_down = 10

    # check left
    if col != 0:
        val_left = int(val_map[row][col-1])
    else:
        val_left = 10

    ady_values = [val_up, val_right, val_down, val_left]

    if all([ady > int(value) for ady in ady_values]):
        
        return True
    else:
        return False

low_point_sum = 0

for idx_x, row in enumerate(puz_input):
    for idx_y, col in enumerate(row):
        if is_low_point(puz_input, (idx_x, idx_y), puz_input[idx_x][idx_y]):
            low_point_sum += int(puz_input[idx_x][idx_y]) + 1

print(f"Answer is: {low_point_sum}")