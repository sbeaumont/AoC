#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[A Maze of Twisty Trampolines, All Alike](http://adventofcode.com/2017/day/5)"""

__author__ = "Serge Beaumont"
__date__ = "December 2017"


import time


PUZZLE_INPUT_FILE_NAME = "AoC-2017-5-input.txt"


def load_input():
    with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
        return [int(offset.strip()) for offset in puzzle_input_file.readlines()]


offsets = load_input()
steps = 0
pos = 0
while 0 <= pos < len(offsets):
    steps += 1
    new_pos = pos + offsets[pos]
    offsets[pos] += 1
    pos = new_pos

print("Part 1: It took {} steps to jump out of the list.".format(steps))


start_time = time.time()
offsets = load_input()
steps = 0
pos = 0
while 0 <= pos < len(offsets):
    steps += 1
    jump = offsets[pos]
    offsets[pos] += -1 if jump >= 3 else 1
    pos += jump
stop_time = time.time()

print("Part 2: It took {} steps in {:.2f}s to jump out of the list.".format(steps, stop_time - start_time))
