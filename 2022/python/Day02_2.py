import Inputs
'''
0 A - ROCK      - 1
1 B - PAPER     - 2
2 C - SCISSORS  - 3

X - LOSE
Y - DRAW
Z - WIN

MY WIN NUMBERS AS THE DIVISION OF ENEMY / ME
1 / 2
2 / 3
3 / 1


OUTCOME
LOSE - 0
DRAW - 3
WIN  - 6
'''


GAMES = """A Y
B X
C Z""".splitlines()

GAMES = Inputs.Day02()

win_condition = ["AB", "BC", "CA"]

dct = { "A": 1,
        "B": 2,
        "C": 3}

total_score = 0


for pairs in GAMES:
    game_score = 0

    a,b = pairs.split(" ")
    my_play = ""

    # LOSE
    if b == "X":
        game_score += 0
        for win_pair in win_condition:
            if a == win_pair[1]:
                my_play = win_pair[0]

    # DRAW
    elif b == "Y":
        game_score += 3
        my_play = a
        
        
    # WIN
    elif b == "Z":
        game_score += 6

        for win_pair in win_condition:
            if a == win_pair[0]:
                my_play = win_pair[1]

    else:
        raise Exception("What?")

    game_score += dct[my_play]
    
    total_score += game_score

print(total_score)

assert total_score == 10274