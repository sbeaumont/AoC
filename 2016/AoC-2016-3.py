#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 3 part 1.

The main trick is to sort the triplets and compare the largest one to the sum of the other two."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

# Load
with open("AoC-2016-3-data.txt", 'r') as content_file:
    content = content_file.read()

# Process
possible = 0
for line in content.split('\n'):
    sides = [int(s) for s in line.split()]
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        possible += 1

print("Possible triangles", possible)