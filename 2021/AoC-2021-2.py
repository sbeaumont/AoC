#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"


def part_1(entries):
    position = 0
    depth = 0
    for e in entries:
        if e[0] == 'forward':
            position += e[1]
        elif e[0] == 'down':
            depth += e[1]
        elif e[0] == 'up':
            depth -= e[1]
    return position * depth


def part_2(entries):
    position = 0
    aim = 0
    depth = 0
    for e in entries:
        if e[0] == 'forward':
            position += e[1]
            depth += aim * e[1]
        elif e[0] == 'down':
            aim += e[1]
        elif e[0] == 'up':
            aim -= e[1]
    return position * depth


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip().split(" ") for line in infile.readlines()]
        lines = [(line[0], int(line[1])) for line in lines]
    return lines


test_result_part_1 = part_1(read_puzzle_data("2-test"))
print("Test Part 1", test_result_part_1)
assert test_result_part_1 == 150

print("Part 1", part_1(read_puzzle_data(2)))

test_result_part_2 = part_2(read_puzzle_data("2-test"))
print("Test Part 2", test_result_part_2)
assert test_result_part_2 == 900

print("Part 2", part_2(read_puzzle_data(2)))
