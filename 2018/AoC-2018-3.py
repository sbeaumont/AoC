#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 3 Part 1

Dumb brute force solution, but works."""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import numpy as np
import re

fabric = np.zeros((1000, 1000))
re_claim = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
with open("AoC-2018-3-input.txt") as infile:
    claims = [[int(item) for item in re_claim.match(line.strip()).groups()] for line in infile]


def layout_claims():
    for claim in claims:
        x, y, w, h = claim[1:]
        fabric[x:x+w, y:y+h] += 1


def overlapping_fabric():
    overlap = 0
    for i in range(1000):
        for j in range(1000):
            if fabric[i, j] > 1:
                overlap += 1
    return overlap


layout_claims()
print(f"Part 1: {overlapping_fabric()}")
assert overlapping_fabric() == 112418
