#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
from collections import Counter
import re


class SpringRow(object):
    def __init__(self, entry):
        self.entry = entry
        self.mask, groups = entry.split()
        self.groups = [int(g) for g in groups.split(',')]
        self.arrangements = 0

    @property
    def info(self):
        return self.mask, self.groups

    def shorten(self, mask):
        def remove_dots(mask):
            mask = mask[1:] if mask[0] == '.' else mask
            mask = mask[::-1]
            mask = mask[1:] if mask[0] == '.' else mask
            return mask

        # Remove .. multiples since a group only needs single .'s.
        mask = re.sub(r'(\.)+', '.', mask)
        # Remove edge .'s, because they'll never matter
        mask = remove_dots(mask)
        return mask

    def condense(self, mask):
        def remove_edge_group(mask, groups):
            if mask[0] == '#':
                mask = mask[groups[0] + 1:]
                groups = groups[1:]
            return mask, groups

    @property
    def solved(self):
        return self.arrangements > 0




def part_1(entries):
    """

    """
    rows = [SpringRow(e) for e in entries]
    for row in rows:
       print(row.shorten(), row.groups)
    return 0


def part_2(entries):
    return 0


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = 12
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    # assert test_result_part_1 == 0
    #
    print("     Part 1:", part_1(read_puzzle_data(DAY)))
    #
    # test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    # print("Test Part 2:", test_result_part_2)
    # assert test_result_part_2 == 0
    #
    # result_part_2 = part_2(read_puzzle_data(DAY))
    # print("     Part 2:", result_part_2)
    # assert result_part_2 == 0