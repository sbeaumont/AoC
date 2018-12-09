#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 3 Part 1

Dumb brute force solution, but works."""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import numpy as np
import re

EXPECTED_CLAIM_ID = 560

fabric = np.zeros((1000, 1000))
re_claim = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
with open("AoC-2018-3-input.txt") as infile:
    claims = [[int(item) for item in re_claim.match(line.strip()).groups()] for line in infile]


def layout_claims():
    for claim in claims:
        x, y, w, h = claim[1:]
        fabric[x:x+w, y:y+h] += 1


def find_non_overlapping_claim():
    def has_overlap(coords):
        x, y, w, h = coords
        for i in range(x, x+w):
            for j in range(y, y+h):
                if fabric[i, j] != 1:
                    return True
        return False

    for claim in claims:
        if not has_overlap(claim[1:]):
            return claim[0]
    return None


layout_claims()
claim_id = find_non_overlapping_claim()

print(f"Part 2: {claim_id}")

assert claim_id == EXPECTED_CLAIM_ID, f"Expected Claim ID {EXPECTED_CLAIM_ID}, got {claim_id}"
