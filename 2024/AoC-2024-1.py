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


def read_puzzle_data(file_number):
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    assert test_result == 11

    print("Part 1:", part_1(read_puzzle_data(puzzle_number)))

    test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 2:", test_result_2)
    assert test_result_2 == 31

    print("Part 2:", part_2(read_puzzle_data(puzzle_number)))
