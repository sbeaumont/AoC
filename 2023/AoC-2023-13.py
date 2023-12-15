#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys


def transpose(list_of_lists):
    transposed = list(map(list, zip(*list_of_lists)))
    return [''.join(line) for line in transposed]


def parse_entries(entries):
    patterns = []
    current_pattern = []
    for entry in entries:
        if entry.strip() != '':
            current_pattern.append(entry)
        else:
            patterns.append(current_pattern)
            current_pattern = []
    patterns.append(current_pattern)
    return patterns

def mirror_pos(i, row):
    left = row[:i][::-1]
    right = row[i:]
    min_length = min(len(left), len(right))
    if left[:min_length] == right[:min_length]:
        return i
    return 0



def find_mirror_line(pattern, find_line):
    pos = find_line(pattern)
    if pos:
        return pos

    pos = find_line(transpose(pattern))
    if pos:
        return pos * 100


def find_line_part_1(pattern):
    first_row = pattern[0]
    for i in range(1, len(first_row)):
        # Check first line
        pos = mirror_pos(i, first_row)
        if pos:
            # If first line is okay, check the other lines
            mirrored = True
            for other_row in pattern[1:]:
                if not mirror_pos(i, other_row):
                    # Nope, mirror breaks
                    mirrored = False
                    break
            if mirrored:
                # All other lines are mirrored at this position as well, found the location.
                return pos
    return 0


def find_line_part_2(pattern):
    # Just find the cases with a single failing mirror line, that will be the one
    for i in range(1, len(pattern[0])):
        mirroring_lines = [mirror_pos(i, row) > 0 for row in pattern]
        if mirroring_lines.count(False) == 1:
            return i
    return 0

def part_1(entries):
    patterns = parse_entries(entries)
    total = 0
    for pattern in patterns:
        score = find_mirror_line(pattern, find_line_part_1)
        total += score
    return total


def part_2(entries):
    patterns = parse_entries(entries)
    total = 0
    for pattern in patterns:
        score = find_mirror_line(pattern, find_line_part_2)
        # for line in pattern:
        #     print(line)
        # print(score)
        total += score
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
    assert test_result_part_1 == 405

    print("     Part 1:", part_1(read_puzzle_data(DAY)))
    assert part_1(read_puzzle_data(DAY)) == 30518

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 400

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 36735