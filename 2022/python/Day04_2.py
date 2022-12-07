import Inputs


input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines()

input = Inputs.Day04()

pairs_contained = 0

for pair in input:
    elve1, elve2 = pair.split(",")

    e1_section_start, e1_section_end = int(elve1.split("-")[0]), int(elve1.split("-")[1])
    e2_section_start, e2_section_end = int(elve2.split("-")[0]), int(elve2.split("-")[1])
    
    range_e1 = {*range(int(e1_section_start), int(e1_section_end)+1)}
    range_e2 = {*range(int(e2_section_start), int(e2_section_end)+1)}

    # if any item is contained in the other list, then it's overlapping
    if range_e1.intersection(range_e2):
        pairs_contained += 1

print(pairs_contained)

assert pairs_contained == 806