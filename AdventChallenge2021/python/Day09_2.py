'''
    0123456789

0   2199943210
1   3987894921
2   9856789892
3   8767896789
4   9899965678

'''
import Inputs

# ADYACENT POSITIONS AS VALUES
def val_up(val_map, row, col): # check up
    if row != 0:
        val_up = int(val_map[row-1][col])
    else:
        val_up = 10 # If it's a corner/boundary situation, it's compared
                    # to 10 so that check will pass
    return val_up

def val_right(val_map, row, col): # check right
    if len(val_map[row]) != col+1:
        val_right = int(val_map[row][col+1])
    else:
        val_right = 10
    
    return val_right

def val_down(val_map, row, col): # check down
    if len(val_map) != row + 1:
        val_down = int(val_map[row+1][col])
    else:
        val_down = 10

    return val_down
    
def val_left(val_map, row, col): # check left
    if col != 0:
        val_left = int(val_map[row][col-1])
    else:
        val_left = 10

    return val_left


# ADYACENT POSITIONS AS OBJECTS
def pos_up(val_map, row, col): # check up
    if row != 0:
        return Position(row-1, col, val_map)
    else:
        return None # If it's a corner/boundary situation, return None

def pos_right(val_map, row, col): # check right
    if len(val_map[row]) != col+1:
        return Position(row, col+1, val_map)
    else:
        return None

def pos_down(val_map, row, col): # check down
    if len(val_map) != row + 1:
        val_down = Position(row+1, col, val_map)
    else:
        val_down = None

    return val_down
    
def pos_left(val_map, row, col): # check left
    if col != 0:
        val_left = Position(row, col-1, val_map)
    else:
        val_left = None

    return val_left


class Position:
    def __init__(self, row, col, vals_map):
        self.row = row
        self.col = col
        self.value = int(vals_map[row][col])
        self.id = (row, col)

        self.up_val = val_up(vals_map, row, col)
        self.right_val = val_right(vals_map, row, col)
        self.down_val = val_down(vals_map, row, col)
        self.left_val = val_left(vals_map, row, col)

        self.ady_values = [self.up_val, self.right_val, self.down_val, self.left_val]
    
    
    def ady_positions(self, vals_map):
        return [pos_up(vals_map, self.row, self.col),
                pos_right(vals_map, self.row, self.col),
                pos_down(vals_map, self.row, self.col),
                pos_left(vals_map, self.row, self.col)]

    def is_low_point(self):
        '''Returns true if it's adyacent values are higher
        than the checked value.'''

        if all([ady > int(self.value) for ady in self.ady_values]):
            return True
        else:
            return False


    def is_basin_limit(self):
        '''Returns true if it's value is equal to 9'''
        if self.value == 9:
            return True
        else:
            return False


sample = [
            "2199943210",
            "3987894921",
            "9856789892",
            "8767896789",
            "9899965678",
         ]
         
puz_input = Inputs.Day09()
# puz_input = sample

low_points = []
basin_lst = []

# Convert list of strings to list of list of chars
for row_idx, row in enumerate(puz_input):
    lst = []
    word = puz_input[row_idx]
    lst.extend(puz_input[row_idx])
    puz_input[row_idx] = lst
    

# Make a list with the low points in the map
for row_idx, row in enumerate(puz_input):
    for col_idx, col in enumerate(row):
        pos = Position(row_idx, col_idx, puz_input)
        if pos.is_low_point():
            low_points.append(pos)


# Start crawling from the low points in the map
for low_pt in low_points:
    basin = [low_pt.id]  
    old_basin_count = 0

    n=0
    
    # clean list
    while len(basin) != old_basin_count:
        n += 1
        old_basin_count = len(basin)
        for pt_id in basin.copy():
            pt = Position(pt_id[0], pt_id[1], puz_input)

            ady_vals = pt.ady_positions(puz_input)

            for ady_val in ady_vals:
                if ady_val is not None:
                    if ady_val.value != 9 and ady_val.id not in basin:
                        basin.append(ady_val.id)
                       
    basin_lst.append(basin)

sorted_lst = sorted(basin_lst, key = len)

answer = len(sorted_lst[-1])*len(sorted_lst[-2])*len(sorted_lst[-3])

print(len(sorted_lst[-1]), len(sorted_lst[-2]), len(sorted_lst[-3]))
print(f"Answer is {answer}")

'''
119 99 97
1142757

'''