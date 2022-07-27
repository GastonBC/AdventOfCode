def Day01():
    with open("txtfiles\day01.txt", "r") as input:
        return [int(x) for x in input.read().split()]