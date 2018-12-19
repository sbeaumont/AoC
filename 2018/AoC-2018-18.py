#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2015 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import numpy as np
from collections import defaultdict


def print_grid(grid_to_print):
    print()
    for y in range(0, grid_to_print.shape[1]):
        print(''.join([c for c in grid_to_print[:, y]]))


def neighbour_coords(grid, coord):
    neighbour_deltas = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
    result = list()
    for dx, dy in neighbour_deltas:
        x = coord[0] + dx
        y = coord[1] + dy
        if (0 <= x < grid.shape[0]) and (0 <= y < grid.shape[1]):
            result.append((coord[0] + dx, coord[1] + dy))
    return result


def neighbour_counts(grid, coord):
    result = defaultdict(int)
    for c in neighbour_coords(grid, coord):
        result[grid[c]] += 1
    return result


start = time.time()


def do(num_iterations):
    first = 1
    loop_length = 1
    with open("AoC-2018-18-input.txt") as infile:
        grid = np.array([[c for c in line.strip()] for line in infile])

    previous_grid = grid.copy()
    loop_detector = dict()

    for i in range(num_iterations):
        for x in range(grid.shape[0]):
            for y in range(grid.shape[1]):
                neighbours = neighbour_counts(previous_grid, (x, y))

                # Open acre becomes trees if 3 at least three or more adjacent acres contain trees
                if (previous_grid[x, y] == '.') and (neighbours['|'] >= 3):
                    grid[x, y] = "|"
                elif (previous_grid[x, y] == '|') and (neighbours['#'] >= 3):
                    grid[x, y] = '#'
                elif previous_grid[x, y] == '#':
                    if (neighbours['#'] >= 1) and (neighbours['|'] >= 1):
                        grid[x, y] = '#'
                    else:
                        grid[x, y] = '.'
                else:
                    grid[x, y] = previous_grid[x, y]

        previous_grid = grid
        grid_hash = hash(str(grid.tostring()))
        if grid_hash in loop_detector:
            loop_length = i - loop_detector[grid_hash]
            first = loop_detector[grid_hash]
            print(f"Found loop on iteration {i} compared to iteration {first}: loop length {loop_length}")
            break
        else:
            loop_detector[grid_hash] = i
        grid = previous_grid.copy()
        # if i % 1000 == 0 and (i > 0):
        #     interval = time.time() - start
        #     print(f"It will take {1000000000 / i * interval / 3600} hours to compute")

    return grid, (1000000000 - first) % loop_length + first


print(f"{time.time() - start:.4f} seconds to run.")

if __name__ == '__main__':
    grid, run_to = do(1000000000)
    print(f"Running to iteration {run_to}")
    grid, run_to = do(run_to)

    print_grid(grid)
    unique, counts = np.unique(grid, return_counts=True)
    counts = {u: c for u, c in zip(unique, counts)}
    print(f"Total resource value is {counts['|']} * {counts['#']} = {counts['|'] * counts['#']}")
