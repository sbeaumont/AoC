#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-1-input.txt") as infile:
    print(sum([int(line) for line in infile]))
