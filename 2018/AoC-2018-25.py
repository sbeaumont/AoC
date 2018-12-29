#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 25 part 1

The solution is based on first finding all the neighbours of each point
(with a neighbour being within"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from collections import defaultdict
from itertools import combinations


def manhattan_distance(p1, p2):
    """4D Manhattan distance between p1 and p2."""
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1]) + abs(p2[2] - p1[2]) + abs(p2[3] - p1[3])


def add_to_constellation(in_range, pt, constellation):
    """Based on point pt, recursively add all points that can be reached.
    Returns a dictionary of {point: neighbours}.
    """
    for item in in_range[pt]:
        if item not in constellation:
            constellation.add(item)
            add_to_constellation(in_range, item, constellation)


def load_file(filename):
    with open(filename) as infile:
        data = ([line.strip() for line in infile])
    points = list()
    for line in data:
        points.append(tuple([int(i) for i in line.split(',')]))
    points = sorted(points)
    return points


def create_constellations(in_range):
    constellations = []
    while len(in_range) > 0:
        constellation = set()
        next_pt = next(iter(in_range.keys()))
        constellation.add(next_pt)
        add_to_constellation(in_range, next_pt, constellation)
        constellations.append(constellation)
        # Remove all the constellations that were found from the "To Do" list (in_range)
        for c in constellations:
            for p in c:
                if p in in_range:
                    del in_range[p]
    return constellations


def all_in_range_neighbours(points):
    in_range = defaultdict(set)
    for p1, p2 in combinations(points, 2):
        if manhattan_distance(p1, p2) <= 3:
            in_range[p1].add(p2)
            in_range[p2].add(p1)
    for p in [point for point in points if point not in in_range]:
        in_range[p] = set()
    return in_range


def do(filename):
    points = load_file(filename)
    in_range = all_in_range_neighbours(points)
    constellations = create_constellations(in_range)
    print(f"There are {len(constellations)} constellations.")
    return len(constellations)


if __name__ == '__main__':
    start = time.time()

    assert do("AoC-2018-25-test-0.txt") == 2
    assert do("AoC-2018-25-test-1.txt") == 4
    assert do("AoC-2018-25-test-2.txt") == 3
    assert do("AoC-2018-25-input.txt") == 390

    print(f"{time.time() - start:.4f} seconds to run.")
