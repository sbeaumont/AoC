#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 23 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re

start = time.time()

regex = re.compile("pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)")

with open("AoC-2018-23-input.txt") as infile:
    data = ([line.strip() for line in infile])

nanobots = []
for line in data:
    match = regex.search(line)
    nanobots.append({'pos': (int(match.group(1)), int(match.group(2)), int(match.group(3))), 'r': int(match.group(4))})

print(nanobots)

max_radius = 0
max_bot = None
for bot in nanobots:
    if bot['r'] > max_radius:
        max_radius = bot['r']
        max_bot = bot

in_range = 0
max_bot_pos = max_bot['pos']
for bot in nanobots:
    bot_pos = bot['pos']
    distance = abs(max_bot_pos[0] - bot_pos[0]) + abs(max_bot_pos[1] - bot_pos[1]) + abs(max_bot_pos[2] - bot_pos[2])
    if distance <= max_radius:
        in_range += 1

print(in_range)

print(f"{time.time() - start:.4f} seconds to run.")