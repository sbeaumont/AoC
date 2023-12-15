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
        springs, groups = entry.split()
        self.groups = [int(g) for g in groups.split(',')]
        self.original_groups = [int(g) for g in groups.split(',')] # copy
        self.mask = re.sub(r'(\.)+', '.', springs)
        self.original_mask = self.mask

    @property
    def min_length(self):
        """Springs plus the gaps in the groups"""
        return self.springs_expected + (self.groups_expected - 1 if self.groups_expected > 1 else 0)

    @property
    def groups_expected(self):
        return len(self.groups)

    @property
    def springs_expected(self):
        return sum(self.groups)

    @property
    def num_wildcards(self):
        return self.springs_counts['?']

    @property
    def springs_counts(self):
        return Counter(self.mask)


    @property
    def wiggle_room(self):
        return len(self.mask) - self.min_length

    @property
    def solved(self) -> bool:
        no_wiggle_room = self.wiggle_room == 0
        no_groups_left = len(self.groups) == 0
        return no_wiggle_room or no_groups_left

    @property
    def info(self):
        return self.wiggle_room, self.mask, self.groups, self.original_mask, self.original_groups

    def clean_sides(self):
        if self.mask:
            self.mask = self.mask[1:] if self.mask[0] == '.' else self.mask
            self.mask = self.mask[:-1] if self.mask[-1] == '.' else self.mask


    def _clean_spring_ends(self) -> int:
        chops = 0
        # Starts with #, is guaranteed first group, chop left plus spacing.
        # Keep going until consumed
        if not self.solved:
            if self.mask[0] == '#':
                chops += 1
                group_length = self.groups[0]
                self.groups = self.groups[1:] if len(self.groups) > 1 else []
                self.mask = self.mask[group_length + 1:]
                self.clean_sides()

        # Now the other side.
        if not self.solved:
            if self.mask[-1] == '#':
                chops += 1
                group_length = self.groups[-1]
                self.groups = self.groups[:-1] if len(self.groups) > 1 else []
                self.mask = self.mask[:-(group_length + 1)]
                self.clean_sides()
        return chops

    def _clean_small_ends(self) -> int:
        """Remove ends where based on the . position it could never fit."""
        chops = 0
        if not self.solved:
            if '.' in self.mask[:self.groups[0]]:
                chops += 1
                self.mask = self.mask[self.mask.index('.') + 1:]
                self.clean_sides()

        if not self.solved:
            if '.' in self.mask[-self.groups[-1]:]:
                chops += 1
                first_dot = self.mask[-self.groups[-1]:].index('.')
                self.mask = self.mask[:-(self.groups[-1] - first_dot)]
                self.clean_sides()
        return chops

    def _clean_exact_fit(self) -> int:
        """If an end has at least one # and a . at the exact fit position, then remove"""
        chops = 0
        if not self.solved:
            if '#' in self.mask[:self.groups[0]] and self.mask[self.groups[0]] == '.':
                chops += 1
                self.mask = self.mask[self.groups[0] + 1:]
                self.groups = self.groups[1:] if len(self.groups) > 1 else []
                self.clean_sides()

        if not self.solved:
            if '#' in self.mask[-self.groups[-1]:] and self.mask[-(self.groups[-1] + 1)] == '.':
                chops += 1
                self.mask = self.mask[:-(self.groups[-1] + 1)]
                self.groups = self.groups[:-1] if len(self.groups) > 1 else []
                self.clean_sides()
        return chops

    def chop(self):
        self.clean_sides()
        still_useful = True
        while still_useful:
            chops = 0
            chops += self._clean_spring_ends()
            chops += self._clean_small_ends()
            chops += self._clean_exact_fit()
            still_useful = chops > 0


def part_1(entries):
    """
    Rule 1: no wiggle room = 1 arrangement
    Rule 2: A '#' at beginning or inverted is guaranteed and can be chopped off. After chopping repeat.
    Rule 3: At beginning (or inverted) a group of exact size within size+1 ?'s is a guaranteed group and can be chopped off with . or ? after it. After chopping repeat.
    Rule 4: The first '#' must belong to first group if it's within size positions.
    Rule 5: If after chopping there are no groups left = 1 arrangement
    Rule 6: If the first . comes earlier than the size of first group, it can't fit.
    """
    rows = [SpringRow(e) for e in entries]
    # for row in rows:
    #    print(row.info)
    # print()
    for row in rows:
        row.chop()
    for info in sorted([row.info for row in rows if not row.solved]):
        print(info)
    return 0


def part_2(entries):
    return 0


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
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