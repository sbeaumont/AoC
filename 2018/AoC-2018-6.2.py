#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 6
"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import numpy as np

with open("AoC-2018-6-input.txt") as infile:
    coords = ([[int(s) for s in line.split(",")] for line in infile.readlines()])

min_x = min([coord[0] for coord in coords])
min_y = min([coord[1] for coord in coords])
max_x = max([coord[0] for coord in coords])
max_y = max([coord[1] for coord in coords])
width = max_x - min_x
height = max_y - min_y

coords = [(x - min_x, y - min_y) for x, y in coords]

print(min_x, max_x, min_y, max_y, width, height)

area = np.zeros((width, height))

safe_locations = 0
for x in range(width):
    for y in range(height):
        total_manhattan = sum([abs(x - coord[0]) + abs(y - coord[1]) for coord in coords])
        if total_manhattan < 10000:
            safe_locations += 1

print(safe_locations)