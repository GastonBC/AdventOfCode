import Inputs
import numpy as np
import math

sample = [((0,9), (5,9)),
          ((8,0), (0,8)),
          ((9,4), (3,4)),
          ((2,2), (2,1)),
          ((7,0), (7,4)),
          ((6,4), (2,0)),
          ((0,9), (2,9)),
          ((3,4), (1,4)),
          ((0,0), (8,8)),
          ((5,5), (8,2))]

input_lines = Inputs.Day05()
lines = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def is_ortho(self):
        if self.p1.x == self.p2.x or \
            self.p1.y == self.p2.y:
            return True
        else:
            return False

    def length(self):
        return math.sqrt((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)


    def all_points(self):
        points = []

        # p1 ---q------- p2
        #       p1.y = p2.y = q.y
        #       q.x = range(p1.x, p2.x)
        max_point = None
        min_point = None
        if self.p1.y == self.p2.y:
            max_point = max(self.p1.x, self.p2.x)
            min_point = min(self.p1.x, self.p2.x)

            for x in range(min_point, max_point + 1):
                points.append((x, self.p1.y)) 

        elif self.p1.x == self.p2.x:
            max_point = max(self.p1.y, self.p2.y)
            min_point = min(self.p1.y, self.p2.y)

            for y in range(min_point, max_point +1):
                points.append((self.p1.x, y)) 

        return points



for pseudo_line in input_lines:
    p1 = Point(pseudo_line[0][0], pseudo_line[0][1])
    p2 = Point(pseudo_line[1][0], pseudo_line[1][1])

    lines.append(Line(p1, p2))

ortho_lines = [l for l in lines if l.is_ortho()]
intercepts = 0
visited_points = []

for idx1, line1 in enumerate(ortho_lines):
    points_l1 = line1.all_points()
    for idx2, line2 in enumerate(ortho_lines):

        if idx1 >= idx2:
            continue

        points_l2 = line2.all_points()
        for p in points_l1:
            if p in points_l2 and p not in visited_points:
                visited_points.append(p)
                intercepts += 1

print(intercepts)

# TODO, this works, but there has to be a faster way

'''
6311 intercepts
'''