#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 3 Part 1

Dumb brute force solution, but works."""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import numpy as np
import re

fabric = np.zeros((1000, 1000))
re_claim = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
with open("AoC-2018-3-input.txt") as infile:
    claims = [re_claim.match(line.strip()) for line in infile.readlines()]


for claim in claims:
    x = int(claim.group(2))
    y = int(claim.group(3))
    w = int(claim.group(4))
    h = int(claim.group(5))

    for i in range(x, x+w):
        for j in range(y, y+h):
            fabric[i, j] += 1

overlap = 0
for i in range(1000):
    for j in range(1000):
        if fabric[i, j] > 1:
            overlap += 1

print("Part 1: {}".format(overlap))

for claim in claims:
    x = int(claim.group(2))
    y = int(claim.group(3))
    w = int(claim.group(4))
    h = int(claim.group(5))

    no_overlap = True
    for i in range(x, x+w):
        for j in range(y, y+h):
            if fabric[i, j] != 1:
                no_overlap = False
                break
    if no_overlap:
        print("Part 2: {}".format(claim.group(1)))
