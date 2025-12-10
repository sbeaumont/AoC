"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


def part_1(entries: list[str]):

    def max_joltage(bank: str):
        batteries = [int(b) for b in bank]
        for first in range(9, 0, -1):
            if first in batteries:
                for second in range(9, 0, -1):
                    if second in batteries[batteries.index(first) + 1:]:
                        return int(f'{first}{second}')

    return sum([max_joltage(e) for e in entries])


def part_2(entries: list[str]):

    def max_joltage(bank: str):
        """Consider the max value in the range that each battery can be in. For instance the first battery can't be
        in the last 11, so search from the first to the 12-from-last battery."""
        battery_values = list()
        batteries = [int(b) for b in bank]
        start = 0
        end = len(batteries) - 12 + 1 # Slice end is non-inclusive
        for battery in range(12):
            max_value = max(batteries[start:end])
            start = batteries[start:end].index(max_value) + start + 1
            battery_values.append(max_value)
            end += 1
        return int(''.join([str(v) for v in battery_values]))

    return sum([max_joltage(e) for e in entries])


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 357,
    "Part 1": 17535,
    "Test 2": 3121910778619,
    "Part 2": None,
}
