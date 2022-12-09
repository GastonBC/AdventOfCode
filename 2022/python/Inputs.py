def Day01():
    with open(r'2022\txtfiles\day01.txt', "r") as input:
        return [x for x in input.read().splitlines()]

def Day02():
    with open(r'2022\txtfiles\day02.txt', "r") as input:
        return [x for x in input.read().splitlines()]
        
def Day03():
    with open(r'2022\txtfiles\day03.txt', "r") as input:
        return [x for x in input.read().splitlines()]

def Day04():
    with open(r'2022\txtfiles\day04.txt', "r") as input:
        return [x for x in input.read().splitlines()]

def Day05():
    with open(r'2022\txtfiles\day05.txt', "r") as input:
        return [x for x in input.read().split("\n\n")]

def Day06():
    with open(r'2022\txtfiles\day06.txt', "r") as input:
        return input.read()

def Day07():
    with open(r'2022\txtfiles\day07.txt', "r") as input:
        return input.read().splitlines()

def Day08():
    import numpy as np
    return np.genfromtxt(r"2022\txtfiles\day08.txt", delimiter=1, dtype=np.int32)
