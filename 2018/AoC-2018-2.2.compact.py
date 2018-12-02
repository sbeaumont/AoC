#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 2 Part 2, compact version"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-2-input.txt") as infile:
    box_ids = sorted([line.strip() for line in infile.readlines()])

for i in range(len(box_ids)):
    if sum([1 for c1, c2 in zip(box_ids[i], box_ids[i+1]) if c1 != c2]) == 1:
        print (''.join([c1 for c1, c2 in zip(box_ids[i], box_ids[i+1]) if c1 == c2]))
        break
