#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017 - Day 19 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from pprint import pprint

start = time.time()

with open("AoC-2017-19-input.txt") as infile:
    data = ([line for line in infile])

pprint(data)

print(f"{time.time() - start:.4f} seconds to run.")
