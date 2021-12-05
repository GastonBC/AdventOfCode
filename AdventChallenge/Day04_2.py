import numpy as np
import Inputs

# get the last winning table

sample_nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

sample = [
    [[22, 13, 17, 11,  0,],
    [ 8,  2, 23,  4, 24,],
    [21,  9, 14, 16,  7,],
    [ 6, 10,  3, 18,  5,],
    [ 1, 12, 20, 15, 19,]],

    [[ 3, 15,  0,  2, 22,],
    [ 9, 18, 13, 17,  5,],
    [19,  8,  7, 25, 23,],
    [20, 11, 10, 24,  4,],
    [14, 21, 16, 12,  6,]],

    [[14, 21, 17, 24,  4,],
    [10, 16, 15,  9, 19,],
    [18,  8, 23, 26, 20,],
    [22, 11, 13,  6,  5,],
    [ 2,  0, 12,  3,  7,]]
]


# number_input = sample_nums
# game_boards = sample

number_input = Inputs.Day04_Numbers()
game_boards = Inputs.Day04_Boards()

last_called_number = None
losing_board = None
losing_board_noned = None
winning_boards = []

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
        
        if (np.any(np.all(boards_np[idx] == None, 0)) == True or \
            np.any(np.all(boards_np[idx] == None, 1)) == True) and \
               idx not in [tpls[0] for tpls in winning_boards] :        # Do not add the winner multiple times

            winning_boards.append((idx, boards_np[idx].flatten().tolist())) 

            if len(winning_boards) == len(boards_np):
                losing_board = bds_np_static[idx].flatten().tolist()
                losing_board_noned = winning_boards[-1][1]
                print(losing_board)
                print(losing_board_noned)

                break_loop = True
                last_called_number = num
                break

    if break_loop:
        break
    
sum_winning_nums = 0


# Since winning board and winning board noned are the same lengths and with the same positions
# find the index of None values and get the real value to add in sum_winning_nums
for idx, val in enumerate(losing_board_noned):
    if val != None:
        sum_winning_nums += losing_board[idx]

print("Winning sum result: {}".format(sum_winning_nums))
print("Last called number: {}".format(last_called_number))
print("Result: {}".format(sum_winning_nums*last_called_number))