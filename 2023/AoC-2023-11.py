#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 11"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
from itertools import combinations


def transpose(list_of_lists):
    transposed = list(map(list, zip(*list_of_lists)))
    return [''.join(line) for line in transposed]


def expand(entries):
    return transpose(expand_vertical(transpose(expand_vertical(entries))))


def expand_vertical(entries):
    expanded = []
    for entry in entries:
        expanded.append(entry)
        if len(set(entry)) == 1:
            expanded.append(entry)
    return expanded


def find_galaxies(entries):
    galaxies = []
    for y, line in enumerate(entries):
        for x, char in enumerate(line):
            if char == '#':
                galaxies.append((x, y))
    return galaxies

def total_distance(galaxies):
    paths = list(combinations(galaxies, 2))
    total = 0
    for path in paths:
        x1, y1 = path[0]
        x2, y2 = path[1]
        total += abs(x1 - x2) + abs(y1 - y2)
    return total


def part_1(entries):
    galaxies = find_galaxies(expand(entries))
    print(galaxies)
    return total_distance(galaxies)


def expandables(galaxies, max_x, max_y):
    x_es = []
    y_s = []
    for g in galaxies:
        x_es.append(g[0])
        y_s.append(g[1])
    expand_x = sorted(set(range(0, max_x)) - set(x_es), reverse=True)
    expand_y = sorted(set(range(0, max_y)) - set(y_s), reverse=True)
    return expand_x, expand_y


def mega_expand(galaxies, max_x, max_y, factor):
    expand_x, expand_y = expandables(galaxies, max_x, max_y)
    expanded_galaxies = []
    for g in galaxies:
        left_of_g = len([x for x in expand_x if g[0] > x])
        above_g = len([y for y in expand_y if g[1] > y])
        expanded_galaxies.append((g[0] + (left_of_g * factor) - left_of_g, g[1] + (above_g * factor) - above_g))
    return expanded_galaxies


def part_2(entries, factor):
    galaxies = find_galaxies(entries)
    expanded_galaxies = mega_expand(galaxies, len(entries[0]), len(entries), factor)
    # print(galaxies)
    # print(expandables(galaxies, len(entries[0]), len(entries)))
    # print(expanded_galaxies)
    return total_distance(expanded_galaxies)


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 374

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"), 10)
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 1030

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"), 100)
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 8410

    result_part_2 = part_2(read_puzzle_data(DAY), 1000000)
    print("     Part 2:", result_part_2)
    assert result_part_2 == 857986849428