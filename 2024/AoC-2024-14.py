#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

import re
from functools import reduce
from operator import mul


def end_locations(robots, max_x, max_y, seconds, add_velocity=False):
    result = list()
    for e in robots:
        x = (e[0] + seconds * e[2]) % max_x
        y = (e[1] + seconds * e[3]) % max_y
        if add_velocity:
            result.append((x, y, e[2], e[3]))
        else:
            result.append((x, y))
    return result

def score(locations, max_x, max_y):
    quadrants = {0: 0, 1: 0, 2: 0, 3: 0}
    for xy in locations:
        if 0 <= xy[0] < (max_x // 2):
            # Left side
            if 0 <= xy[1] < (max_y // 2):
                # Top left
                quadrants[0] += 1
            elif (max_y // 2) < xy[1] < max_y:
                # Bottom Left
                quadrants[2] += 1
        elif (max_x // 2) < xy[0] < max_x:
            # Right side
            if 0 <= xy[1] < (max_y // 2):
                # Top right
                quadrants[1] += 1
            elif (max_y // 2) < xy[1] < max_y:
                # Bottom right
                quadrants[3] += 1
    return reduce(mul, quadrants.values())


def detect_region(locations, max_x, max_y, region_size):
    bots_in_region = 0
    for xy in locations:
        if ((max_x // 2 - region_size) < xy[0] < (max_x // 2 + region_size)) and \
                ((max_y // 2 - region_size) < xy[1] < (max_y // 2 + region_size)):
            bots_in_region += 1
    return bots_in_region


def print_area(locations, max_x, max_y):
    for y in range(max_y):
        line = ['X' if (x, y) in locations else '.' for x in range(max_x)]
        print(''.join(line))


def part_1(entries: list):
    max_x, max_y, robots = entries
    seconds = 100
    locations = end_locations(robots, max_x, max_y, seconds)
    return score(locations, max_x, max_y)

def part_2(entries: list):
    max_x, max_y, robots = entries
    elapsed_seconds = 0
    for i in range(8200):
        robots = end_locations(robots, max_x, max_y, 1, add_velocity=True)
        elapsed_seconds += 1
        locations = [(r[0], r[1]) for r in robots]
        if detect_region(locations, max_x, max_y, 20) > 200:
            # Maybe a tree?
            # print_area(locations, max_x, max_y)
            # print("Seconds", elapsed_seconds)
            break
    return elapsed_seconds

def read_puzzle_data(data_file: str):
    robots = list()
    with open(data_file) as infile:
        for line in [line.strip() for line in infile.readlines()]:
            if line.startswith("size="):
                x, y = [int(i) for i in line.split('=')[1].split(',')]
            else:
                coords = re.search(r'p=([0-9]+),([0-9]+) v=(-?[0-9]+),(-?[0-9]+)', line).groups()
                robots.append([int(x) for x in coords])
    return x, y, robots

assertions = {
    "Test 1": 12,
    "Part 1": 231852216,
    "Test 2": None,
    "Part 2": 8159,
}
