#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time

start = time.time()

with open("AoC-2018-X-input.txt") as infile:
    data = ([line.strip() for line in infile])

print(data)

print(f"{time.time() - start:.4f} seconds to run.")
