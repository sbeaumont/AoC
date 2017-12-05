#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017"""

__author__ = "Serge Beaumont"
__date__ = "December 2017"


import time


with open("AoC-2017-5-input.txt") as puzzle_input_file:
    offsets = [int(offset.strip()) for offset in puzzle_input_file.readlines()]

steps = 0
pos = 0
while 0 <= pos < len(offsets):
    steps += 1
    new_pos = pos + offsets[pos]
    offsets[pos] += 1
    pos = new_pos

print("Part 1: It took {} steps to jump out of the list.".format(steps))


with open("AoC-2017-5-input.txt") as puzzle_input_file:
    offsets = [int(offset.strip()) for offset in puzzle_input_file.readlines()]

start_time = time.time()
steps = 0
pos = 0
while 0 <= pos < len(offsets):
    steps += 1
    new_pos = pos + offsets[pos]
    offsets[pos] += -1 if offsets[pos] >= 3 else 1
    pos = new_pos
stop_time = time.time()

print("Part 2: It took {} steps in {:.2f}s to jump out of the list.".format(steps, stop_time - start_time))
