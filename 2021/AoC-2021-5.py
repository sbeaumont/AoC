#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from collections import defaultdict, Counter


def part_1(entries):
    vents = defaultdict(int)

    for entry in entries:
        x1, y1 = entry[0]
        x2, y2 = entry[1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vents[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                vents[(x, y1)] += 1

    vent_counts = Counter(vents)
    return len([e for e in vent_counts.values() if e >= 2])


def part_2(entries):
    vents = defaultdict(int)

    for entry in entries:
        x1, y1 = entry[0]
        x2, y2 = entry[1]
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                vents[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                vents[(x, y1)] += 1
        elif (x1 < x2 and y1 < y2) or (y2 < y1 and x2 < x1):
            for i in range(abs(x2 - x1) + 1):
                vents[(min(x1, x2) + i, min(y1, y2) + i)] += 1
        else:
            for i in range(abs(x2 - x1) + 1):
                vents[(max(x1, x2) - i, min(y1, y2) + i)] += 1

    vent_counts = Counter(vents)
    return len([e for e in vent_counts.values() if e >= 2])


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [[[int(nr) for nr in coords.split(',')]
                  for coords in line.strip().split(' -> ')]
                 for line in infile.readlines()]

    return lines


if __name__ == '__main__':
    DAY = "5"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 5

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("\nTest Part 2:", test_result_part_2)
    assert test_result_part_2 == 12

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
