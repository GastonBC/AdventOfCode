import Inputs
from collections import defaultdict

Input = Inputs.Day07()

sizes = defaultdict(int)
stack = []


for cmd in Input:
    match cmd.split():
        case [_, _, "/"]:
            pass

        case [_, _, ".."]:
            stack.pop()

        case [_, _, folder]:
            stack.append(folder)

        # directory or file
        case [a, _] if a.isdigit():
            for i in range(len(stack) + 1):
                path = "/" + "/".join(stack[:i])
                sizes[path] += int(a)

total_val = 0
for key, value in sizes.items():
    if value <= 100000:
        total_val += value

print(total_val)

assert total_val == 1667443




