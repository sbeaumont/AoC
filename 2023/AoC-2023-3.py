#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
import re


def overlaps(line_nr, pos, coord):
    return (line_nr - 1 <= coord[0] <= line_nr + 1) and (pos[0] - 1 <= coord[1] <= pos[1])

def scan_symbols(entries):
    symbols = dict()
    for i, line in enumerate(entries):
        for match in re.finditer(r'[^0-9\.]', line):
            symbols[(i, match.start())] = match.group(0)
    return symbols

def scan_numbers(entries):
    symbols = dict()
    for i, line in enumerate(entries):
        for match in re.finditer(r'[0-9]+', line):
            symbols[(i, match.span())] = int(match.group(0))
    return symbols

def part_1(entries):
    symbols = scan_symbols(entries)

    total = 0
    for i, line in enumerate(entries):
        for match in re.finditer(r'[0-9]+', line):
            for s in symbols.keys():
                if overlaps(i, match.span(), s):
                    total += int(match.group(0))
                    break
    return total


def part_2(entries):
    total = 0
    symbols = scan_symbols(entries)
    numbers = scan_numbers(entries)
    for s_coord, symbol in symbols.items():
        if symbol != '*':
            continue
        matches: list[int] = list()
        for coords, number in numbers.items():
            if overlaps(coords[0], coords[1], s_coord):
                matches.append(number)
        if len(matches) == 2:
            total += matches[0] * matches[1]
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
    assert test_result_part_1 == 4361

    print("     Part 1:", part_1(read_puzzle_data(DAY)))
    assert part_1(read_puzzle_data(DAY)) == 539590

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 467835

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 80703636