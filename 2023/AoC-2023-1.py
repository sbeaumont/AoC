#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import string
import re


def part_1(entries: list[str]):
    total = 0
    for e in entries:
        numbers = e.translate(str.maketrans('', '', string.ascii_letters))
        total += int(numbers[0] + numbers[-1])
    return total


def part_2(entries):
    text_numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    total = 0
    for e in entries:
        # By changing the regex from r"xxx" t0 r"(?=(xxx))" you get all overlapping matches,
        # not just the non-overlapping ones.
        match = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))", e)
        first = text_numbers.index(match[0]) if match[0] in text_numbers else int(match[0])
        last = text_numbers.index(match[-1]) if match[-1] in text_numbers else int(match[-1])
        total += (first * 10) + last
    return total


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    test_result = part_1(read_puzzle_data("1-test"))
    print("Test 1:", test_result)
    assert test_result == 142

    print("Part 1:", part_1(read_puzzle_data(1)))

    test_result = part_2(read_puzzle_data("1-test-2"))
    print("Test 2:", test_result)
    assert test_result == 281

    test_result = part_2(read_puzzle_data("1-test-3"))
    print("Test 3:", test_result)

    print("Part 2:", part_2(read_puzzle_data(1)))
    assert part_2(read_puzzle_data(1)) == 54019
