import Inputs
'''
0 A X - ROCK        - 1
1 B Y - PAPER       - 2
2 C Z - SCISSORS    - 3

MY WIN NUMBERS AS THE DIVISION OF ENEMY / ME
1 / 2
2 / 3
3 / 1

IF NUMBERS ARE EQUAL, DRAW
ELSE LOSE

OUTCOME
LOSE - 0
DRAW - 3
WIN  - 6
'''


GAMES = """A Y
B X
C Z"""

GAMES = Inputs.Day02()

win_condition = [1/2, 2/3, 3/1]

dct = { "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3}

total_score = 0

for pairs in GAMES:
    game_score = 0

    a,b = pairs.split(" ")
    result = dct[a] / dct[b]

    game_score += dct[b]

    if result in win_condition:
        game_score += 6
    elif result == 1:
        game_score += 3
    else:
        game_score += 0

    total_score += game_score

print(total_score)

assert total_score == 14375