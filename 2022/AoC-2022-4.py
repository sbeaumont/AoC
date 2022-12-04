#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day 4"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"

def split_entry(entry):
    return [[int(s) for s in a.split('-')] for a in entry.split(',')]

def contained(a1, a2):
    return ((a1[0] <= a2[0]) and (a1[1] >= a2[1])) or ((a2[0] <= a1[0]) and (a2[1] >= a1[1]))

def part_1(entries):
    fully_contained = 0
    for e in entries:
        a1, a2 = split_entry(e)
        if contained(a1, a2):
            fully_contained += 1
    return fully_contained


def part_2(entries):
    overlapping = 0
    for e in entries:
        a1, a2 = split_entry(e)
        if contained(a1, a2) or (a1[0] <= a2[0] <= a1[1]) or (a1[0] <= a2[1] <= a1[1]):
            overlapping += 1
    return overlapping


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "4"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 2

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 4

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 825
