#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from math import floor


def calc_fuel(x):
    return floor(x / 3) - 2


with open("AoC-2019-input-1.txt") as infile:
    data = [int(x.strip()) for x in infile.readlines()]

total = sum([calc_fuel(x) for x in data])

total2 = 0
for mass in data:
    fuel_needed = calc_fuel(mass)
    while fuel_needed > 0:
        total2 += fuel_needed
        fuel_needed = calc_fuel(fuel_needed)

print("Part 1:", total)
print("Part 2:", total2)

assert total == 3305115
assert total2 == 4954799
