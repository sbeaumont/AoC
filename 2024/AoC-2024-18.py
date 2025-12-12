"""
Solution for Advent of Code challenge 2024

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"


def part_1(entries):
    print(entries)
    for e in entries:
        pass
    return None


def part_2(entries: list[str]):
    for e in entries:
        pass
    return None


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [[int(x) for x in line.strip().split(',')] for line in infile.readlines()]



assertions = {
    "Test 1": None,
    "Part 1": None,
    "Test 2": None,
    "Part 2": None,
}
