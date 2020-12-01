#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import load_input

data = [int(x) for x in load_input(1)]

total = sum([x // 3 - 2 for x in data])

print("Part 1:", total)

assert total == 3305115
