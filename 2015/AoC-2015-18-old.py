#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2015 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import numpy as np

start = time.time()

with open("AoC-2015-18-input.txt") as infile:
    grid = np.array([[c for c in line.strip()] for line in infile])

print(grid)


def neighbour_coords(coord):
    neighbour_deltas = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
    result = list()
    for dx, dy in neighbour_deltas:
        x = coord[0] + dx
        y = coord[1] + dy
        if (0 <= x < grid.shape[0]) and (0 <= y < grid.shape[1]):
            result.append((coord[0] + dx, coord[1] + dy))
    return result


def live_neighbours(coord):
    return [grid[c] for c in neighbour_coords(coord) if grid[c] == '#']


def num_live_neighbours(coord):
    return len(live_neighbours(coord))


print(live_neighbours((1, 1)), num_live_neighbours((1, 1)))
print(live_neighbours((0, 0)))

print(f"{time.time() - start:.4f} seconds to run.")
