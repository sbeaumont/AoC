#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day 6"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"

def find(entries, marker_length):
    for i in range(marker_length - 1, len(entries) + 1):
        last_four = entries[i - (marker_length - 1): i + 1]
        assert len(last_four) == marker_length
        if len(last_four) == len(set(last_four)):
            return i + 1
    return -1

def part_1(entries):
    return find(entries, 4)

def part_2(entries):
    return find(entries, 14)


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]

    return lines


if __name__ == '__main__':
    DAY = "6"

    test_lines = read_puzzle_data(f"{DAY}-test")
    for tl in test_lines:
        datastream, expected_result = tl.strip().split(',')
        test_result_part_1 = part_1(datastream)
        print("Test Part 1:", test_result_part_1)
        assert test_result_part_1 == int(expected_result), f"Expected {expected_result}, got {test_result_part_1}"

    print("     Part 1:", part_1(read_puzzle_data(DAY)[0]))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test")[0])
    print("Test Part 2:", test_result_part_2)
    # assert test_result_part_2 == 0

    result_part_2 = part_2(read_puzzle_data(DAY)[0])
    print("     Part 2:", result_part_2)
    # assert result_part_2 == 0