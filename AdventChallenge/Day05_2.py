import Inputs
import numpy as np
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_x_farther_from(self, p2):
        return self.x > p2.x

    def is_y_farther_from(self, p2):
        return self.y > p2.y

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

    def is_45deg(self):
        
        angle_rads = math.atan2(self.p2.y-self.p1.y, self.p2.x-self.p1.x)
        angle_deg = math.degrees(angle_rads)
        
        return (angle_deg%45 == 0)  # if the angle is divisible by 45, then it is 45 deg or variants
            
 
    def length(self):
        return math.sqrt((self.p1.x-self.p2.x)**2 + (self.p1.y-self.p2.y)**2)


    def all_points(self):
        points = []

        # p1 ---q------- p2
        #       p1.y = p2.y = q.y
        #       q.x = range(p1.x, p2.x)


        if self.is_ortho():
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


        if self.is_45deg():

            # normal situation
            if self.p2.x > self.p1.x and self.p2.y > self.p1.y:
                for idx, n in enumerate(range(self.p1.x, self.p2.x + 1)):
                    q = (n, self.p1.y + idx)
                    points.append(q)

            # full backwards
            elif self.p2.x < self.p1.x and self.p2.y < self.p1.y:
                for idx, n in enumerate(range(self.p2.x, self.p1.x + 1)):
                    q = (n, self.p2.y + idx)
                    points.append(q)

            # half backwards
            elif self.p2.x > self.p1.x and self.p2.y < self.p1.y:
                for idx, n in enumerate(range(self.p1.x, self.p2.x + 1)):
                    q = (n, self.p1.y - idx)
                    points.append(q)

            # half backwards
            elif self.p2.x < self.p1.x and self.p2.y > self.p1.y:
                for idx, n in enumerate(range(self.p2.x, self.p1.x + 1)):
                    q = (n, self.p2.y - idx)
                    points.append(q)

        else:
            raise InterruptedError("Possibility not taken into account")

        return points
        

'''


possibilities

okay
x2 > x1
y2 > y1

full backwards
x1 > x2
y1 > y2

half back
x1 > x1
y1 < y2

x1 < x2
y2 > y2



'''


sample = [
            ((0,9), (5,9)),
            ((8,0), (0,8)),
            ((9,4), (3,4)),
            ((2,2), (2,1)),
            ((7,0), (7,4)),
            ((6,4), (2,0)),
            ((0,9), (2,9)),
            ((3,4), (1,4)),
            ((0,0), (8,8)),
            ((5,5), (8,2))
          ]


input_lines = Inputs.Day05()
input_lines = sample
valid_lines = []



for pseudo_line in input_lines:
    p1 = Point(pseudo_line[0][0], pseudo_line[0][1])
    p2 = Point(pseudo_line[1][0], pseudo_line[1][1])

    new_line = Line(p1, p2)
    if new_line.is_45deg():
        valid_lines.append(new_line)


intercepts = 0
visited_points = []
print(f"List lenght {len(valid_lines)}")
for idx1, line1 in enumerate(valid_lines):
    points_l1 = line1.all_points()
    for idx2, line2 in enumerate(valid_lines):

        if idx1 >= idx2:
            continue

        points_l2 = line2.all_points()
        
        for p in points_l1:
            if p in points_l2 and \
                p not in visited_points:

                visited_points.append(p)
                intercepts += 1


print(intercepts)

# TODO, this works, but there has to be a faster way
# all_points_ever = [l.all_points() for l in valid_lines]

# all_points_ever = [item for sublist in all_points_ever for item in sublist] # flatten
# all_points_ever_set = set(all_points_ever)


# print(all_points_ever)
# print(list(all_points_ever_set))

# intercepts = len(all_points_ever)-len(all_points_ever_set)