'''
y
0. --------------------------------
1.
2.-----<>
3.      |
4.      |
5.      |
6.      |
7...................................x

forward affects x
up, down, y

'''
import Inputs

class Submarine(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, value):
        self.x += value

    # Up and down are backwards because its a submarine
    def up(self, value):
        self.y -= value

    def down(self, value):
        self.y += value

sub = Submarine()

for action, val in Inputs.Day02():
    if action == "forward":
        sub.forward(val)

    elif action == "down":
        sub.down(val)
    
    elif action == "up":
        sub.up(val)

print("Submarine forwards distance: {}".format(sub.x))
print("Submarine depth: {}".format(sub.y))
print("Result: {}".format(sub.x*sub.y))

'''
Submarine forwards distance: 2053
Submarine depth: 1033
Result: 2120749
'''