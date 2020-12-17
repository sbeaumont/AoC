#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 9"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from itertools import combinations

with open(f"AoC-2020-9-input.txt") as infile:
    xmas = [int(line.strip()) for line in infile.readlines()]


def part_1():
    for i in range(25, len(xmas)):
        nr = xmas[i]
        found = False
        for combo in list(combinations(xmas[i-25:i], 2)):
            if (combo[0] != combo[1]) and (sum(combo) == nr):
                found = True
                break
        if not found:
            print("Part 1: Could not find combo for", nr, "at index", i)
            return nr


def part_2(target):
    print("Looking for sum of", target)
    i = 0
    j = 2
    there_yet = False
    while not there_yet:
        total = sum(xmas[i:j])
        if total < target:
            j += 1
        elif total > target:
            i += 1
        else:
            # Yay, found it!
            there_yet = True
            print("Part 2:", min(xmas[i:j]) + max(xmas[i:j]))


if __name__ == '__main__':
    target = part_1()
    part_2(target)
