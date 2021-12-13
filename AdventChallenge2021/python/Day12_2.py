'''
rules
Current cave can not be next cave
Small caves to be visited once
If no options remaining, start again
Last cave is end
'''
import itertools
from collections import defaultdict
import Inputs

sample = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

# A dict of node: [neighbors]
puzzle = defaultdict(list)

for line in Inputs.Day12().splitlines():
    a,b = line.strip().split('-')
    puzzle[a].append(b)
    puzzle[b].append(a)
    
def dfs(node, graph, visited, twice, counter = 0):

    # Once we reach the end, we add 1 to the counter
    if node == "end": return 1

    # Recursive with all neighbors
    # This will exhaust all paths before going backwards?
    for neighbor in graph[node]:
        if neighbor.isupper():
            counter += dfs(neighbor, graph, visited, twice)
        else:
            if neighbor not in visited:
                counter += dfs(neighbor, graph, visited | {neighbor}, twice)
            
            # This is for part 2. Can visit ONE small cave up to 2 times
            elif twice and neighbor not in {"start", "end"}:
                counter += dfs(neighbor, graph, visited, False)

    return counter

print(dfs("start", puzzle, {"start"}, True))