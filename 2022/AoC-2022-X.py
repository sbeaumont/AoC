#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"


def part_1(entries):
    return 0


def part_2(entries):
    return 0


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "X"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 0

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 0

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
