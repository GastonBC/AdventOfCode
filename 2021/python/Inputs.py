def Day01():
    with open(r"2021/txtfiles/day01.txt", "r") as input:
        return [int(x) for x in input.read().split()]
        
def Day02():
    with open("../../txtfiles/day02.txt", "r") as input:
        lst = input.read().splitlines()
        
    return [(action.split()[0], int(action.split()[1])) for action in lst]

def Day03():
    import numpy as np
    return np.genfromtxt(r"2021\txtfiles\day03.txt", delimiter=1, dtype=np.uint8)

def Day04():
    import numpy as np
    numbers = None
    boards = []
    data = None

    with open("txtfiles/day04.txt", "r") as input:
        data = input.read().split("\n\n")
    
    for block in data[1:]:
        this_block = []
        for block_line in reversed(block.splitlines()):
            nums = block_line.split()
            this_block.append([int(n) for n in nums])

        boards.append(this_block)


    numbers = [int(x) for x in data[0].split(',')]
    boards = np.array(boards)

    return (numbers, boards)

def Day05():
    out_lst = []
    with open("../../txtfiles/day05.txt", "r") as input:
        for line in input.read().splitlines():
            points = line.split(" -> ")
            p1x = int(points[0].split(',')[0])
            p1y = int(points[0].split(',')[1])

            p2x = int(points[1].split(',')[0])
            p2y = int(points[1].split(',')[1])
            out_lst.append(((p1x,p1y), (p2x,p2y)))
    return out_lst

def Day06():
    with open("../../txtfiles/day06.txt", "r") as input:
        return [int(x) for x in input.read().split(',')]

def Day07():
    with open("../../txtfiles/day07.txt", "r") as input:
        return [int(x) for x in input.read().split(',')]

def Day08():
    out_lst = []
    with open("../../txtfiles/day08.txt", "r") as input:
        
        for line in input.read().splitlines():
            parts = line.split(' | ')
            out_lst.append([parts[0].split(), parts[1].split()])
            
    return out_lst

def Day09():
    with open("../../txtfiles/day09.txt", "r") as input:
        return [x for x in input.read().split()]

def Day10():
    with open("../../txtfiles/day10.txt", "r") as input:
        return [x for x in input.read().split()]

def Day11():
    import numpy as np
    return np.genfromtxt("txtfiles/day11.txt", delimiter=1, dtype=np.uint16)


def Day12():
    with open("../../txtfiles/day12.txt", "r") as input:
        return input.read()

def Day13():
    points = None
    data = None
    with open("txtfiles/day13.txt", "r") as input:
        data = input.read().split("\n\n")
    
    points = data[0]
    instructions = data[1]
    return (points, instructions)

def Day14():
    with open("txtfiles/day14.txt", "r") as input:
        return input.read()

def Day15():
    import numpy as np
    return np.genfromtxt("txtfiles/day15.txt", delimiter=1, dtype=np.uint16)

def Day25():
    import numpy as np
    return np.genfromtxt(r"2021\txtfiles\day25.txt", delimiter=1, dtype=np.str)