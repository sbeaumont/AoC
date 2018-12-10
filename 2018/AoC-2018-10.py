#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 10"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re
import numpy as np

start = time.time()


def calculate_bounding_box(points):
    min_x = min([coord[0] for coord in points])
    min_y = min([coord[1] for coord in points])
    max_x = max([coord[0] for coord in points])
    max_y = max([coord[1] for coord in points])
    width = max_x - min_x
    height = max_y - min_y
    return np.array((min_x, min_y)), np.array((max_x, max_y)), width, height, width*height


def print_matrix(poss):
    bbox = calculate_bounding_box(poss)
    poss = [node - bbox[0] for node in poss]
    matrix = np.empty((bbox[2]+1, bbox[3]+1), dtype=str)
    matrix[:] = ' '
    for pos in poss:
        matrix[pos[0], pos[1]] = '#'

    for y in range(bbox[3]+1):
        print(''.join(matrix[:, y]))


with open("AoC-2018-10-input.txt") as infile:
    pattern = re.compile("position=<\s*?(-?\d+),\s*?(-?\d+)> velocity=<\s*?(-?\d+),\s*?(-?\d+)>")
    data = ([pattern.search(line.strip()) for line in infile])

positions = np.array([(int(v.group(1)), int(v.group(2))) for v in data])
vectors = np.array([(int(v.group(3)), int(v.group(4))) for v in data])

seconds = 0
bounding_box = calculate_bounding_box(positions)
smaller = True
while smaller:
    new_positions = [position + vector for position, vector in zip(positions, vectors)]
    new_bounding_box = calculate_bounding_box(new_positions)
    smaller = new_bounding_box[4] <= bounding_box[4]
    bounding_box = new_bounding_box
    positions = new_positions
    seconds += 1

# By stepping manually I know that we have to back up exactly one step.
positions = [position - vector for position, vector in zip(positions, vectors)]
seconds -= 1
print_matrix(positions)
print(f"\nSituation at {seconds} 'seconds'.")

print(f"\n{time.time() - start:.4f} seconds to run.")
