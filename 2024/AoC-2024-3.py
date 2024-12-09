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


def read_puzzle_data(data_file: str) -> str:
    with open(data_file) as infile:
        return infile.read()


assertions = {
    "Test 1": 161,
    "Part 1": None,
    "Test 2": 48,
    "Part 2": None
}

overrides = {
    "Test 2": {'data file': "AoC-2024-3-test-2-input.txt",}
}

