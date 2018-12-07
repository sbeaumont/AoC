#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 7

"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import itertools

# 0    1 2    3  4        5      6    7 8   9
# Step D must be finished before step L can begin.
with open("AoC-2018-7-input.txt") as infile:
    lines = [line.strip().split(" ") for line in infile.readlines()]
    instructions = [(line[1], line[7]) for line in lines]
    all_unique_nodes = set(list(itertools.chain.from_iterable(instructions)))

print("Instructions", instructions)


def create_graph(source, from_index, to_index):
    result = dict()
    for n in source:
        if n[from_index] not in result:
            result[n[from_index]] = set()
        result[n[from_index]].add(n[to_index])

    for n in all_unique_nodes:
        if n not in result:
            result[n] = []
        else:
            result[n] = sorted(list(result[n]))
    return result


graph = create_graph(instructions, 0, 1)
all_children = set(itertools.chain.from_iterable(graph.values()))
roots = sorted([node for node in graph if node not in all_children])
print("Graph", graph)
print("Roots", roots)

prerequisites = create_graph(instructions, 1, 0)
print("Preqs", prerequisites)

done = []
to_do = list(all_unique_nodes)
time = 0
working_elves = {}
while to_do or working_elves:
    available = sorted([instruction for instruction in to_do if set(prerequisites[instruction]).issubset(set(done)) or not prerequisites[instruction]])
    available = [instruction for instruction in available if instruction not in working_elves.keys()]
    # add a new elf if possible
    while len(working_elves) < 5 and available:
        working_elves[available[0]] = 60 + ord(available[0]) - 64
        to_do.remove(available[0])
        available.remove(available[0])

    # increment time and decrease elves' working time
    time += 1
    for elf in working_elves.keys():
        working_elves[elf] -= 1

    # free up done elves
    for instruction in working_elves.keys():
        if working_elves[instruction] == 0:
            del working_elves[instruction]
            done.append(instruction)

print(time)

# 1122 Too High
