#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 8"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
from itertools import cycle
from math import lcm

def parse_network_data(entries):
    strip_brackets = str.maketrans('()', '  ')
    network = dict()
    for e in entries[2:]:
        node, next_el = e.split('=')
        node = node.strip()
        next_el = [el.strip() for el in next_el.translate(strip_brackets).split(',')]
        network[node] = next_el
    return network


def part_1(entries):
    instructions = cycle(entries[0])
    network = parse_network_data(entries)

    steps = 0
    current = 'AAA'
    while current != 'ZZZ':
        steps += 1
        current = network[current][1 if next(instructions) == 'R' else 0]
    return steps


def part_2(entries):
    instructions = cycle(entries[0])
    network = parse_network_data(entries)

    steps = 0
    ghosts = [[node, []] for node in network.keys() if node.endswith('A')]
    done = False
    while not done:
        steps += 1
        current_instruction = 1 if next(instructions) == 'R' else 0
        for ghost in ghosts:
            ghost[0] = network[ghost[0]][current_instruction]
            if ghost[0].endswith('Z'):
                # Found out that after the first time we cycle they all keep cycling in a regular pattern
                ghost[1].append(steps)
        done = all([len(ghost[1]) for ghost in ghosts])
    return lcm(*[g[1][0] for g in ghosts])


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 2

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test-2"))
    print("Test Part 1.2:", test_result_part_1)
    assert test_result_part_1 == 6

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-3"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 6

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 14299763833181