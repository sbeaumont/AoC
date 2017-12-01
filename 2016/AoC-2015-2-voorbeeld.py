#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 2 part 1.

Parse the lengths, calculate sides and area needed."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

DATA = """27x26x11
3x2x22
14x3x5
10x9x8"""

total = 0
for line in DATA.split():
    print("hallo")
    # Parse
    l, w, h = line.split('x')
    l = int(l)
    w = int(w)
    h = int(h)

    # Sides
    side1 = l*w
    side2 = w*h
    side3 = h*l

    # Area
    smallestSide = min(side1, side2, side3)
    areaNeeded = 2*(side1+side2+side3) + smallestSide
    total += areaNeeded

print("Total area needed: ", total)
