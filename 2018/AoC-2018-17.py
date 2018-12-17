#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 17

This solution uses a frontier similar to breadth first search to emulate the waterflow.

The status of the ground and water is encoded as:

0 passable soil ("air")
1 flowing water
2 flowing water, potentially at rest
4 water at rest
9 clay ("wall")
"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re
import numpy as np
from collections import deque
from pprint import pprint

SPRING = (500, 0)


def print_grid(grid_to_print):
    print_codes = {0: '.', 1: '|', 2: '^', 4: '~', 9: '#'}
    print()
    for y in range(0, grid_to_print.shape[1]):
        print(''.join([print_codes[c] for c in grid_to_print[:, y]]))


def load_scans(file_name):
    with open(file_name) as infile:
        data = ([line.strip().split(",") for line in infile])

    regex_line = re.compile("\s*(x|y)=(\d+|\d+\.\.\d+)$")
    scans = list()
    for d1, d2 in data:
        scan = dict()
        line_match = regex_line.match(d1)
        scan[line_match.group(1)] = [int(line_match.group(2)), int(line_match.group(2))]
        line_match = regex_line.match(d2)
        scan[line_match.group(1)] = [int(i) for i in line_match.group(2).split("..")]
        scans.append(scan)

    if DEBUG:
        pprint(scans)

    return scans


def create_grid(scans):
    # One coordinate of buffer around min and max values
    min_x = min([min(c['x']) for c in scans]) - 1
    max_x = max([max(c['x']) for c in scans]) + 1

    min_y = min([min(c['y']) for c in scans])
    max_y = max([max(c['y']) for c in scans]) + 1

    if DEBUG:
        print(f"Boundaries of data are ({min_x}, {min_y}) to ({max_x}, {max_y})")

    grid = np.zeros((max_x - min_x, max_y - min_y))

    for scan in scans:
        for x in range(scan['x'][0], scan['x'][1] + 1):
            for y in range(scan['y'][0], scan['y'][1] + 1):
                grid[x - min_x, y - min_y] = 9

    return grid, (min_x, min_y)


def fill_with_water(grid, origin):
    spring = (SPRING[0] - origin[0], 0)
    frontier = deque()
    frontier.appendleft(spring)
    grid[spring] = 1

    def scan_for_still_water(from_coord, next_candidate, direction, change_to_still=False):
        """Scan water (to left or right), and if a wall is encountered change it to water in rest"""
        still_water_candidates = [from_coord]
        while grid[next_candidate] == 2:
            still_water_candidates.append(next_candidate)
            next_candidate = (next_candidate[0] + direction, next_candidate[1])
        if grid[next_candidate] == 9:
            if change_to_still:
                for coord in still_water_candidates:
                    # Put any flowing water above back into frontier
                    if grid[coord[0], coord[1] - 1] == 1:
                        frontier.appendleft((coord[0], coord[1] - 1))
                    # Change to water in rest
                    grid[coord] = 4
            return True
        return False

    while len(frontier) > 0:
        current = frontier.pop()
        under = (current[0], current[1] + 1)
        left = (current[0] - 1, current[1])
        right = (current[0] + 1, current[1])

        # Water fell below the grid
        if under[1] >= grid.shape[1]:
            continue

        if grid[under] == 0:
            # Water falls down
            frontier.appendleft(under)
            grid[under] = 1

        elif grid[under] >= 4:
            # Above water in rest or clay
            # ...therefore potentially still water
            grid[current] = 2

            # Left wall is clay
            if grid[left] == 9:
                scan_for_still_water(current, right, 1, True)

            # Right wall is clay
            if grid[right] == 9:
                scan_for_still_water(current, left, -1, True)

            # Frontiers meet in the middle
            if (grid[left] == 2) and (grid[right] == 2):
                if scan_for_still_water(current, right, 1) and scan_for_still_water(current, left, -1):
                    scan_for_still_water(current, right, 1, True)
                    scan_for_still_water(current, left, -1, True)

            # Extend frontier to the left and right
            if grid[left] == 0:
                frontier.appendleft(left)
                grid[left] = 1
            if grid[right] == 0:
                frontier.appendleft(right)
                grid[right] = 1

        if DEBUG:
            print_grid(grid)


def do(file_name):
    scans = load_scans(file_name)
    grid, origin = create_grid(scans)
    fill_with_water(grid, origin)

    unique, counts = np.unique(grid, return_counts=True)
    total = 0
    retain_total = 0
    for u, c in zip(unique, counts):
        if 0 < u < 9:
            total += c
        if u == 4:
            retain_total += c

    return grid, total, retain_total


if __name__ == '__main__':
    DEBUG = False

    start = time.time()

    grid, total, retain_total = do("AoC-2018-17-test-1.txt")
    assert total == 57
    assert retain_total == 29

    grid, total, retain_total = do("AoC-2018-17-input.txt")
    print_grid(grid)
    print(f"Total water is (Part 1) {total}, of which (Part 2) {retain_total} will be retained.")

    print(f"{time.time() - start:.4f} seconds to run.")
