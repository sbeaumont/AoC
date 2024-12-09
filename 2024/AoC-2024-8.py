#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from collections import defaultdict
from itertools import combinations


def parse_puzzle_input(puzzle_input):
    antenna = defaultdict(list)
    for y in range(len(puzzle_input)):
        for x in range(len(puzzle_input[0])):
            if puzzle_input[y][x] != '.':
                antenna[puzzle_input[y][x]].append((x, y))
    return antenna

def part_1(entries: list[str]):
    antenna = parse_puzzle_input(entries)
    x_max = len(entries[0])
    y_max = len(entries)
    antinodes = set()
    for freq, locs in antenna.items():
        for loc_pair in combinations(locs, 2):
            x0, y0 = loc_pair[0]
            x1, y1 = loc_pair[1]
            antinode_1 = (x0 + (x0 - x1), y0 + (y0 - y1))
            if 0 <= antinode_1[0] < x_max and 0 <= antinode_1[1] < y_max:
                antinodes.add(antinode_1)
            antinode_2 = (x1 + (x1 - x0), y1 + (y1 - y0))
            if 0 <= antinode_2[0] < x_max and 0 <= antinode_2[1] < y_max:
                antinodes.add(antinode_2)
    # for antinode in sorted(antinodes):
    #     print(antinode)
    return len(antinodes)


def part_2(entries: list[str]):
    antenna = parse_puzzle_input(entries)
    x_max = len(entries[0])
    y_max = len(entries)
    antinodes = set()
    for freq, locs in antenna.items():
        for loc in locs:
            antinodes.add(loc)
        for loc_pair in combinations(locs, 2):
            x0, y0 = loc_pair[0]
            x1, y1 = loc_pair[1]
            x_delta = x0 - x1
            y_delta = y0 - y1
            x = x0
            y = y0
            while 0 <= x < x_max and 0 <= y < y_max:
                x += x_delta
                y += y_delta
                if 0 <= x < x_max and 0 <= y < y_max:
                    antinodes.add((x, y))

            x_delta = x1 - x0
            y_delta = y1 - y0
            x = x1
            y = y1
            while 0 <= x < x_max and 0 <= y < y_max:
                x += x_delta
                y += y_delta
                if 0 <= x < x_max and 0 <= y < y_max:
                    antinodes.add((x, y))

    return len(antinodes)


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 14,
    "Part 1": None,
    "Test 2": 34,
    "Part 2": 905,
}
