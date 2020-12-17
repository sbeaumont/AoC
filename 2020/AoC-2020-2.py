#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

import re

# ---------- Load

with open(f"AoC-2020-2-input.txt") as infile:
    # position 1 (3), position 2 (4), letter (l), password (vdcv)
    # 3-4 l: vdcv => ('3', '4', 'l', 'vdcv')
    pattern = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")
    entries = [pattern.search(line.strip()).groups() for line in infile.readlines()]

# ---------- Part 1

valid_1 = len([e for e in entries if int(e[0]) <= e[3].count(e[2]) <= int(e[1])])

print("Part 1:", valid_1)
assert valid_1 == 447

# ---------- Part 2

valid_2 = 0
for entry in entries:
    letter = entry[2]
    password = entry[3]
    if (password[int(entry[0]) - 1] == letter) ^ (password[int(entry[1]) - 1] == letter):
        valid_2 += 1

print("Part 2:", valid_2)
assert valid_2 == 249
