def Day01():
    with open("txtfiles\day01.txt", "r") as input:
        return [int(x) for x in input.read().split()]

def Day02():
    lst = []
    with open("txtfiles\day02.txt", "r") as input:
        return input.read().split("\n")