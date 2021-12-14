import numpy as np
from Inputs import Day13_Instructions, Day13_Points
import matplotlib.pyplot as plt
def print_readable(arr):
    ary = np.where(arr == 0, " ", "#")
    print(ary)


def fold_vert(ary, index):
    # split arr vertically
    part_arrs = np.split(ary, [index, index+1], axis=0)

    ary1 = part_arrs[0]
    ary2 = part_arrs[-1]
    
    # mirror second array
    ary2 = np.flip(ary2, 0)

    shape1 = np.shape(ary1)
    shape2 = np.shape(ary2)

    diff = abs(shape1[0] - shape2[0])

    if ary1.size > ary2.size:
        ary1[diff:, ...] += ary2
        return ary1

    elif ary1.size < ary2.size:
        ary2[diff:, ...] += ary1
        return ary2
    else:
        return ary1 + ary2

def fold_horiz(ary, index):
    # split arr horizontally, creates 3 arrays, middle one is 
    # the cut
    part_arrs = np.split(ary, [index, index+1], axis=1)

    ary1 = part_arrs[0]
    ary2 = part_arrs[-1]
    
    # mirror second array
    ary2 = np.flip(ary2, 1)
    shape1 = np.shape(ary1)
    shape2 = np.shape(ary2)

    diff = abs(shape1[1] - shape2[1])

    # The offset to sum the values, given that there is no way to know
    # which array will be bigger
    if ary1.size > ary2.size:
        ary1[..., diff:] += ary2
        return ary1

    elif ary1.size < ary2.size:
        ary2[..., diff:] += ary1
        return ary2

    else:
        return ary1 + ary2

xlst = []
ylst = []

points = Day13_Points().splitlines()
intructions = Day13_Instructions().splitlines()

for line in points:
    y,x = line.split(',')
    xlst.append(int(x))
    ylst.append(int(y))
    
arr = np.zeros([max(xlst)+1, max(ylst)+1])


for idx in range(len(xlst)):
    arr[xlst[idx], ylst[idx]] = 1


for inst in intructions:
    fold_idx = inst.split("=")[-1]
    
    if "x" in inst:
        arr = fold_horiz(arr, int(fold_idx))

    elif "y" in inst:
        arr = fold_vert(arr, int(fold_idx))
    
    
print_readable(arr)

# visualization
non_zero = np.transpose(np.nonzero(arr))
x = non_zero[:, 0]
y = non_zero[:, 1]

# Points are reversed because it grows downwards
x = -x
plt.scatter(y, x, marker="s")
plt.margins(1, 6)
plt.show()


'''
EBLUBRFH
[['#' '#' '#' '#' ' ' '#' '#' '#' ' ' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' '#' '#' ' ' ' ' '#' '#' '#' ' ' ' ' '#' '#' '#' '#' ' ' '#' ' ' ' ' '#' ' ']
 ['#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ']
 ['#' '#' '#' ' ' ' ' '#' '#' '#' ' ' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' '#' '#' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' '#' '#' ' ' ' ' '#' '#' '#' '#' ' ']
 ['#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' '#' ' ' '#' '#' '#' ' ' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ']
 ['#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' '#' ' ' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ']
 ['#' '#' '#' '#' ' ' '#' '#' '#' ' ' ' ' '#' '#' '#' '#' ' ' ' ' '#' '#' ' ' ' ' '#' '#' '#' ' ' ' ' '#' ' ' ' ' '#' ' ' '#' ' ' ' ' ' ' ' ' '#' ' ' ' ' '#' ' ']]
 '''