from numpy import char


def Day01():
    with open("txtfiles\day01.txt", "r") as input:
        return [int(x) for x in input.read().split()]

def Day02():
    lst = []
    with open("txtfiles\day02.txt", "r") as input:
        return input.read().split("\n")

def Day03():
    import numpy as np
    return np.genfromtxt(r"2020\txtfiles\day03.txt", delimiter=1, dtype=str, comments="//")