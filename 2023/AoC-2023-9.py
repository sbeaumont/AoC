#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 9"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys


def parse_entries(entries):
    history = list()
    for e in entries:
        history.append([int(n) for n in e.split()])
    return history


def part_1(entries):
    total = 0
    for sequence in parse_entries(entries):
        cur_seq = sequence
        value = sequence[-1]
        while not all(v == 0 for v in cur_seq):
            next_seq = []
            for i in range(1, len(cur_seq)):
                next_seq.append(cur_seq[i] - cur_seq[i-1])
            # print(next_seq)
            value += next_seq[-1]
            cur_seq = next_seq
        total += value
    return total


def part_2(entries):
    total = 0
    for sequence in parse_entries(entries):
        beginnings = list()

        cur_seq = sequence
        # Collect the first value of each sequence
        beginnings.insert(0, sequence[0])
        while not all(v == 0 for v in cur_seq):
            # Reduce to the next sequence
            next_seq = []
            for i in range(1, len(cur_seq)):
                next_seq.append(cur_seq[i] - cur_seq[i-1])
            # ...while capturing the first values
            beginnings.insert(0, next_seq[0])
            cur_seq = next_seq

        # Calculate back up the beginnings of the sequences
        value = 0
        for v in beginnings:
            value = v - value
        total += value

    return total


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 114

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 2

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 925