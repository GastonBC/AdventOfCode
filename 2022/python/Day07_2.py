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


total_space = 70000000
req_space = 30000000
used_space = sizes["/"]
avail_space = total_space - used_space

resting_space = req_space - avail_space

print(resting_space)

dir_to_delete_size = req_space

for key, value in sizes.items():
    if value >= resting_space and value < dir_to_delete_size:
        dir_to_delete_size = value

print(dir_to_delete_size)

assert total_val == 8998590




