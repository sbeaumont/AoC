#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from aoc.utils.utils import neighbors4
from collections import defaultdict

def find_trails(topo_map, x0, y0):
    """Find all trails starting from (x0, y0) in topo_map"""
    def neighbours(x4, y4):
        return [p for p in neighbors4((x4, y4)) if (0 <= p[0] < len(topo_map[0])) and (0 <= p[1] < len(topo_map))]

    frontier = list()
    frontier.append([(x0, y0),])
    done = list()
    while frontier:
        next_frontier = list()
        for path in frontier:
            x, y = path[-1]
            for x_n, y_n in neighbours(x, y):
                if topo_map[y_n][x_n] == topo_map[y][x] + 1:
                    new_path = path[:]
                    new_path.append((x_n, y_n))
                    next_frontier.append(new_path)
        done.extend([p for p in next_frontier if len(p) == 10])
        frontier = [p for p in next_frontier if len(p) < 10]
    return done

def scan_map(topo_map):
    """Scan the whole topographical map for trails 0->9"""
    trails = defaultdict(list)
    for y in range(len(topo_map)):
        for x in range(len(topo_map[0])):
            if topo_map[y][x] == 0:
                trails_for_xy = find_trails(topo_map, x, y)
                trails[(x, y)].extend(trails_for_xy)
    return trails

def part_1(topo_map: list[str]):
    done_list = scan_map(topo_map)
    total = 0
    for xy, paths in done_list.items():
        total += len(set([p[-1] for p in paths]))
    return total

def part_2(topo_map: list[str]):
    return sum([len(paths) for paths in scan_map(topo_map).values()])

def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [[int(c) for c in line.strip()] for line in infile.readlines()]

assertions = {
    "Test 1": 36,
    "Part 1": 794,
    "Test 2": 81,
    "Part 2": 1706,
}
