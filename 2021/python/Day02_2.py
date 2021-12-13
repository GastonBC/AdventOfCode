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
import matplotlib.pyplot as plt

class Submarine(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0

    def forward(self, value):
        self.x += value
        self.y += self.aim*value

    # Up and down are backwards because its a submarine
    def up(self, value):
        self.aim -= value

    def down(self, value):
        self.aim += value

sub = Submarine()

old_point = (0, 0)
for action, val in Inputs.Day02():
    if action == "forward":
        sub.forward(val)

    elif action == "down":
        sub.down(val)
    
    elif action == "up":
        sub.up(val)

    plt.plot([old_point[0], sub.x], [old_point[1], -sub.y])

    old_point = (sub.x, -sub.y)

plt.show()

print("Submarine forwards distance: {}".format(sub.x))
print("Submarine depth: {}".format(sub.y))
print("Result: {}".format(sub.x*sub.y))

'''
Submarine forwards distance: 2053
Submarine depth: 1041589
Result: 2138382217
'''