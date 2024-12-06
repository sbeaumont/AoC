#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

import re


def part_1(data: str):
    mul_statement = re.compile("mul\(([0-9]{1,3}),([0-9]{1,3})\)")
    total = 0
    for match in re.findall(mul_statement, data):
        total += int(match[0]) * int(match[1])
    return total


def part_2(data: str):
    # print(data)
    mul_statement = re.compile("(mul\(([0-9]{1,3}),([0-9]{1,3})\))|(do\(\))|(don't\(\))")
    total = 0
    enabled = True
    for match in re.findall(mul_statement, data):
        # print(match)
        if match[3] == 'do()':
            enabled = True
        elif match[4] == "don't()":
            enabled = False
        else:
            if enabled:
                total += int(match[1]) * int(match[2])
    return total


def read_puzzle_data(file_number):
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        return infile.read()


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    assert test_result == 161

    print("Part 1:", part_1(read_puzzle_data(puzzle_number)))

    test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test-2"))
    print("Test 2:", test_result_2)
    assert test_result_2 == 48

    print("Part 2:", part_2(read_puzzle_data(puzzle_number)))
