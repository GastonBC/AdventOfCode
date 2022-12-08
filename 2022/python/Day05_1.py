import Inputs


# Input = """    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2""".split("\n\n")

Input = Inputs.Day05()

stacks = {}

for line in Input[0].splitlines():
    curr_stack = 1

    for idx in range(1, len(line), 4):
        ch = line[idx]

        if ch.isdigit():
            break

        if ch != " ":
            # if list exists append character to the beginning, else create the list and append
            stacks.setdefault(curr_stack, []).insert(0, ch)

        curr_stack += 1



for instruction in Input[1].splitlines():
    qtity = instruction.split(" from ")[0]
    pos = instruction.split(" from ")[1]

    qtity = int(qtity.split(" ")[1])
    pos_init = int(pos.split(" to ")[0])
    pos_end  = int(pos.split(" to ")[1])

    for i in range(0, qtity):
        stacks[pos_end].append(stacks[pos_init][-1])
        stacks[pos_init].pop()


message = ""

for key in range(1, len(stacks)+1):
    message += stacks[key][-1]

print(message)

assert message == "LBLVVTVLP"