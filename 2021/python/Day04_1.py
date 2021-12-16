import numpy as np
import Inputs

puz_input = Inputs.Day04()
number_input = puz_input[0]
game_boards = puz_input[1]

last_called_number = None
winning_board = None
winning_board_noned = None

# Create a new list of numpy arrays from the input
# the first one is going to be modified: when a number matches a number in the board
# replace it with None
boards_np = [np.array(arr) for arr in game_boards]

# This copy is going to keep the original values to be used at the end
bds_np_static = boards_np.copy()

# get the numbers from the input
for num in number_input:
    break_loop = False 
    tmp_bds = boards_np.copy()

    for idx, bd in enumerate(tmp_bds):
        boards_np[idx] = np.where(bd == num, None, bd)   # replace the value picked with None
                                                         # first board to fill a row or col with None wins
        
        if np.any(np.all(boards_np[idx] == None, 0)) == True or \
           np.any(np.all(boards_np[idx] == None, 1)) == True:

           break_loop = True

           last_called_number = num
           winning_board = bds_np_static[idx].flatten().tolist()
           winning_board_noned = boards_np[idx].flatten().tolist()
           break

    if break_loop:
        break
    
sum_winning_nums = 0

# Since winning board and winning board noned are the same lengths and with the same positions
# find the index of None values and get the real value to add in sum_winning_nums
for idx, val in enumerate(winning_board_noned):
    if val != None:
        sum_winning_nums += winning_board[idx]

print("Winning sum result: {}".format(sum_winning_nums))
print("Last called number: {}".format(last_called_number))
print("Result: {}".format(sum_winning_nums*last_called_number))

'''
Winning sum result: 899
Last called number: 99
Result: 89001
'''