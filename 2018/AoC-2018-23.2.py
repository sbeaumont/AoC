#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 23 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re
from pprint import pprint
from itertools import combinations
from collections import defaultdict

start = time.time()

regex = re.compile("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")

with open("AoC-2018-23-input.txt") as infile:
    data = ([line.strip() for line in infile])


def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) + abs(pos1[2] - pos2[2])


def intersects(bb1, bb2):
    # See https://en.wikipedia.org/wiki/Bounding_volume
    x1min, y1min, z1min = bb1[0]
    x1max, y1max, z1max = bb1[1]
    x2min, y2min, z2min = bb2[0]
    x2max, y2max, z2max = bb2[1]

    no_intersection = (x1min > x2max) or (x2min > x1max) or (y1min > y2max) or (y2min > y1max) or (z1min > z2max) or (z2min > z1max)

    return not no_intersection


def intersection(bb1, bb2):
    if not intersects(bb1, bb2):
        return None

    x1min, y1min, z1min = bb1[0]
    x1max, y1max, z1max = bb1[1]
    x2min, y2min, z2min = bb2[0]
    x2max, y2max, z2max = bb2[1]

    min_coord = (max(x1min, x2min), max(y1min, y2min), max(z1min, z2min))
    max_coord = (min(x1max, x2max), min(y1max, y2max), min(z1max, z2max))

    return min_coord, max_coord


def init_nanobots():
    bots = []
    for line in data:
        match = regex.search(line)
        bots.append({'pos': (int(match.group(1)), int(match.group(2)), int(match.group(3))), 'r': int(match.group(4))})

    for bot in bots:
        x, y, z = bot['pos']
        r = bot['r']
        min_coord = (x - r, y - r, z - r)
        max_coord = (x + r, y + r, z + r)
        bot['bounding box'] = (min_coord, max_coord)
        bot['distance'] = abs(x) + abs(y) + abs(z)

    return sorted(bots, key=lambda k: k['distance'])


def find_intersections(bots):
    intersections = list()
    num_participants = 2
    bot_combos = list(combinations(bots, 2))
    print(f"Number of combinations to consider: {len(bot_combos)} for {num_participants} participants")
    i = 0
    for bot1, bot2 in combinations(bots, 2):
        if intersects(bot1['bounding box'], bot2['bounding box']):
            i_box = intersection(bot1['bounding box'], bot2['bounding box'])
            intersections.append({'bounding box': i_box, 'participants': [bot1, bot2]})
        i += 1
        if i % 100000 == 0:
            print(i)
    return intersections


def refine_intersections(intersections, bots):
    new_intersections = []
    i = 0
    for ints in intersections:
        for bot in [bot for bot in bots if bot not in ints['participants']]:
            if intersects(ints['bounding box'], bot['bounding box']):
                i_box = intersection(ints['bounding box'], bot['bounding box'])
                participants = ints['participants'][:]
                participants.append(bot)
                new_intersections.append({'bounding_box': i_box, 'participants': participants})
        i += 1
        if i % 100000 == 0:
            print(i)
    return new_intersections

nanobots = init_nanobots()


print(f"There are {len(nanobots)} nanobots.")
intrs2 = find_intersections(nanobots)
print(f"Found {len(intrs2)} intersections for 2")
intrs3 = refine_intersections(intrs2, nanobots)
print(f"Found {len(intrs3)} intersections for 3")
intrs4 = refine_intersections(intrs3, nanobots)
print(f"Found {len(intrs4)} intersections for 4")





print(f"{time.time() - start:.4f} seconds to run.")