#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


from itertools import product

with open(f"AoC-2020-1-input.txt") as infile:
    entries = [int(l) for l in infile.readlines()]

for a, b in product(entries, entries):
    if a+b == 2020:
        print(f"Part 1: Found {a}+{b}=2020, answer is {a*b}")
        break

for a, b, c in product(entries, entries, entries):
    if a+b+c == 2020:
        print(f"Part 2: Found {a}+{b}+{c}=2020, answer is {a*b*c}")
        break
