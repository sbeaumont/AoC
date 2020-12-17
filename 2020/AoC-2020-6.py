#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 6"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from collections import Counter

with open(f"AoC-2020-6-input.txt") as infile:
    forms = [set(line.replace('\n', '')) for line in infile.read().split('\n\n')]
    # print(forms)

print("Part 1: ", sum([len(f) for f in forms]))

with open(f"AoC-2020-6-input.txt") as infile:
    groups = [Counter(line) for line in infile.read().split('\n\n')]
    print(groups)

yes_answer = 0
for group in groups:
    num_people = group.get('\n', 0) + 1
    for k, v in group.items():
        if k != '\n':
            if v == num_people:
                yes_answer += 1

print("Part 2:", yes_answer)
