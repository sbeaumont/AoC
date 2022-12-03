#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day 3"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"


def priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27


def part_1(entries):
    total_score = 0
    for e in entries:
        half = len(e) // 2
        c1 = set(e[:half])
        c2 = set(e[half:])
        odd_one_out = list(c1.intersection(c2))[0]
        total_score += priority(odd_one_out)
    return total_score


def part_2(entries):
    total_score = 0
    for i in range(0, len(entries), 3):
        packs = [set(e) for e in entries[i:i+3]]
        badge = set(packs[0]).intersection(packs[1]).intersection(packs[2]).pop()
        total_score += priority(badge)
    return total_score


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "3"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 157

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 70

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
