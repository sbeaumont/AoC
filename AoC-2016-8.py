#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 8 part 1 and 2.

For the given input the output reads as: UPOJFLBCEZ for part 2."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import numpy as np

# Load
with open("AoC-2016-8-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

grid = np.zeros((6,50), dtype=int)

for line in lines:
    if line[:4] == 'rect':
        c, r = [int(s) for s in line.split()[1].split('x')]
        rect = np.ones((r, c), dtype=int)
        grid[0:r,0:c] = rect
    elif line[:10] == 'rotate row':
        r, by = [int(s) for s in line.split('=')[1].split('by')]
        grid[r,:] = np.roll(grid[r,:], by)
    elif line[:13] == 'rotate column':
        c, by = [int(s) for s in line.split('=')[1].split('by')]
        grid[:,c] = np.roll(grid[:,c], by)

print(grid)

print("The number of switched on lights is:", np.sum(grid))