from collections import deque

PUZZLE_INPUT_FILE_NAME = "AoC-2017-12-input.txt"

with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    lines = [line.strip().split('<->') for line in puzzle_input_file.readlines()]
    line_dict = {int(line[0]): [int(i) for i in line[1].split(',')] for line in lines}


def breadth_first_search(graph, start):
    frontier = deque()
    frontier.append(start)
    visited = dict()
    visited[start] = True

    while not len(frontier) == 0:
        current = frontier.popleft()
        for nxt in graph[current]:
            if nxt not in visited:
                frontier.append(nxt)
                visited[nxt] = True

    return visited


vstd = breadth_first_search(line_dict, 0)
print("Part 1: there are {} nodes in the group with node 0.".format(len(vstd)))

groups = 0
while len(line_dict.keys()) > 0:
    vstd = breadth_first_search(line_dict, line_dict.keys()[0])
    for key in vstd.keys():
        del line_dict[key]
    groups += 1

print("Part 2: There are {} groups.".format(groups))
