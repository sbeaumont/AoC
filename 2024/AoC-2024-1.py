#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from collections import Counter


def split_and_sort(entries):
    lists = list(zip(*[[int(n) for n in e.split()] for e in entries]))
    sorted_lists = list()
    for l in lists:
        sorted_lists.append(sorted(l))
    return sorted_lists

def part_1(entries: list[str]):
    total = 0
    sorted_lists = split_and_sort(entries)
    for loc_ids in zip(*sorted_lists):
        total += abs(loc_ids[0] - loc_ids[1])
    return total


def part_2(entries):
    total = 0
    left, right = split_and_sort(entries)
    right_counts = Counter(right)
    for loc_id in left:
        total += loc_id * right_counts.get(loc_id, 0)
    return total


def read_puzzle_data(data_file: str):
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 11,
    "Part 1": 2367773,
    "Test 2": 31,
    "Part 2": 21271939
}
