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

coords = [(x - min_x, y - min_y) for x,y in coords]

print(min_x, max_x, min_y, max_y, width, height)

area = np.zeros((width, height))
coord_histogram = dict()

for x in range(width):
    for y in range(height):
        lowest_distance = width + height
        coord_index = 0
        lowest_coord_index = 0
        for coord_index in range(len(coords)):
            coord = coords[coord_index]
            manh_dist = abs(x - coord[0]) + abs(y - coord[1])
            if manh_dist < lowest_distance:
                lowest_coord_index = coord_index
                lowest_distance = manh_dist
        area[x, y] = lowest_coord_index
        if lowest_coord_index in coord_histogram:
            coord_histogram[lowest_coord_index] += 1
        else:
            coord_histogram[lowest_coord_index] = 1

print(area)

edge_coords = set()
edge_coords.update(area[0, :])
edge_coords.update(area[width-1, :])
edge_coords.update(area[:, 0])
edge_coords.update(area[:, height-1])

print(edge_coords)

print(coord_histogram)
print(max(coord_histogram.values()))
print(max(coord_histogram, key=coord_histogram.get))

for key in edge_coords:
    del coord_histogram[key]
print(max(coord_histogram.values()))
print(max(coord_histogram, key=coord_histogram.get))

# 5914 too low
