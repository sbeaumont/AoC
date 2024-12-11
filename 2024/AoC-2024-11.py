#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from collections import defaultdict


def iterate(entries, number_of_iterations):
    stones = [int(s) for s in entries[0].strip().split(' ')]
    results = {x: 1 for x in stones}
    for i in range(number_of_iterations):
        next_iteration = defaultdict(int)
        for number, nr_stones in results.items():
            ss = str(number)
            if number == 0:
                # Convert all 0's to 1's or set to 1 if it's the first.
                next_iteration[1] += nr_stones
            elif len(ss) % 2 == 0:
                # Add the same number of half-numbers as the original had.
                half = len(ss) // 2
                next_iteration[int(ss[:half])] += nr_stones
                next_iteration[int(ss[half:])] += nr_stones
            else:
                next_iteration[2024 * number] += nr_stones
        results = next_iteration
    return sum([v for v in results.values()])

def part_1(entries: list[str]):
    return iterate(entries, 25)

def part_2(entries: list[str]):
    return iterate(entries, 75)


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 55312,
    "Part 1": None,
    "Test 2": None,
    "Part 2": None,
}
