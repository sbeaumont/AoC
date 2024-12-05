#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"


def part_1(entries: list[str]):
    for e in entries:
        pass
    return None


def part_2(entries: list[str]):
    for e in entries:
        pass
    return None


def read_puzzle_data(file_number):
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    # assert test_result == 0

    # print("Part 1:", part_1(read_puzzle_data(puzzle_number)))
    #
    # test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test"))
    # print("Test 2:", test_result_2)
    # assert test_result_2 == 31

    # print("Part 2:", part_2(read_puzzle_data(puzzle_number)))
