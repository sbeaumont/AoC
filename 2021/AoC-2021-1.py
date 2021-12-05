#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"


def part_1(entries):
    raised = 0
    for i in range(1, len(entries)):
        if entries[i] > entries[i-1]:
            raised += 1
    return raised


def part_2(entries):
    raised = 0
    for i in range(4, len(entries) + 1):
        slice1 = entries[i-3: i]
        slice2 = entries[i-4: i-1]
        if sum(slice1) > sum(slice2):
            raised += 1
    return raised


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        return [int(line) for line in infile.readlines()]


test_result = part_2(read_puzzle_data("1-test"))
print("Test:", test_result)
assert test_result == 5

print("Part 1:", part_1(read_puzzle_data(1)))
print("Part 2:", part_2(read_puzzle_data(1)))
