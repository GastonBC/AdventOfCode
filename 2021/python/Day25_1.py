import numpy as np
import Inputs

def get_neighbor(val_map, index_tuple):
    '''Gets the right or down element in the array.'''
    row = index_tuple[0]
    col = index_tuple[1]

    if val_map[row, col] == '>':
        try:
            return val_map[row, col+1]

        except IndexError:
            return val_map[row, 0]

    elif val_map[row, col] == 'v':
        try:
            return val_map[row+1, col]
        except IndexError:
            return val_map[0, col]

def move(val_map, index_tuple):
    '''Performs the moving action. Right for > and down for v'''
    row = index_tuple[0]
    col = index_tuple[1]
    
    if val_map[row, col] == '>':
        try:
            val_map[row, col+1] = '>'
        except IndexError:
            val_map[row, 0] = '>'

        val_map[row, col] = '.'

    else:
        try:
            val_map[row+1, col] = 'v'
        except IndexError:
            val_map[0, col] = 'v'

        val_map[row, col] = '.'

puz_input = Inputs.Day25()

steps = 0
while True:
    steps += 1
    movements = 0

    indices_to_move = []

    # First check >. If able to move, add to list and then move all at once.
    # If I moved them here, it would not account sea cucumbers that are on the edge correctly
    for row, col in np.ndindex(puz_input.shape):
        if puz_input[row, col] == '>':
            neighbor = get_neighbor(puz_input, (row,col))

            if neighbor == '.':
                indices_to_move.append((row, col))

    # Perform the moving action
    if indices_to_move:
        for idx in indices_to_move:
            move(puz_input, idx)
            movements += 1
        
    indices_to_move.clear()


    # Repeat the process with v sea cucumbers
    for row, col in np.ndindex(puz_input.shape):
        if puz_input[row, col] == 'v':
            neighbor = get_neighbor(puz_input, (row,col))

            if neighbor == '.':
                indices_to_move.append((row, col))

    if indices_to_move:
        for idx in indices_to_move:
            move(puz_input, idx)
            movements += 1


    # Once nothing moves, break the loop
    if movements == 0:
        print(f"Answer is: {steps}")
        break

assert steps == 516
