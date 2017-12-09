#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[---](http://adventofcode.com/2017/day/9)

Seriously crappy solution. Do not take seriously."""


import re


PUZZLE_INPUT_FILE_NAME = "AoC-2017-7-input.txt"

# Parse parent and children names
line_pattern = re.compile("(\w+)\s\(\d+\)(?: -> (.*))?")
with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    programs = [re.search(line_pattern, line).groups() for line in puzzle_input_file.readlines()]

# find root program by intersecting the set of parents with the set of children
parent_programs = [program[0] for program in programs]
child_programs_nested = [program[1].split(', ') for program in programs if program[1]]
child_programs = [item for sublist in child_programs_nested for item in sublist]
# intersection
unreferenced_programs = [program for program in parent_programs if program not in child_programs]

root_program = unreferenced_programs[0]

print("Part 1: The root of the program tree is program {}.".format(root_program))

# Parse
line_pattern = re.compile("(\w+)\s\((\d+)\)")
with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    weights = [re.search(line_pattern, line).groups() for line in puzzle_input_file.readlines()]
weight_dict = {p[0]: int(p[1]) for p in weights}
program_dict = {p[0]: p[1].split(', ') for p in programs if p[1]}

cumulative_weight = dict()


def calculate_weight(program_name):
    if program_name in program_dict:
        weight = weight_dict[program_name]
        child_weights = set()
        for child_name in program_dict[program_name]:
            child_weight = calculate_weight(child_name)
            weight += child_weight
            child_weights.add(child_weight)
        if len(child_weights) > 1:
            print("Program {} has unbalanced children {}".format(program_name, [(name, cumulative_weight[name]) for name in program_dict[program_name]]))
        cumulative_weight[program_name] = weight
        return weight
    else:
        cumulative_weight[program_name] = weight_dict[program_name]
        return weight_dict[program_name]


print("The weight of the root is {}".format(calculate_weight(root_program)))
print("The cumulative weights of the tree are {}".format(cumulative_weight))


def find_wrong_node(program_name):
    children_names = program_dict[program_name]
    child_weight_dict = dict()
    for child in children_names:
        if cumulative_weight[child] in child_weight_dict:
            child_weight_dict[cumulative_weight[child]] += 1
        else:
            child_weight_dict[cumulative_weight[child]] = 1
        if cumulative_weight[child] != (cumulative_weight[program_name] - weight_dict[program_name]) / len(children_names):
            print(program_name, child, cumulative_weight[child], weight_dict[program_name])


find_wrong_node(root_program)
find_wrong_node('nbyij')
find_wrong_node('tdxow')
find_wrong_node('ghwgd')
print(program_dict['ghwgd'])
for child in program_dict['ghwgd']:
    print(child, cumulative_weight[child])
print(weight_dict['ghwgd'])
print(3*274 + 370)
print(3*274 + 362)