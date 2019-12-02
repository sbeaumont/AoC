#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import load_input


def calc_fuel(x):
    return x // 3 - 2


data = [int(x) for x in load_input(1)]

total2 = 0
for mass in data:
    fuel_needed = calc_fuel(mass)
    while fuel_needed > 0:
        total2 += fuel_needed
        fuel_needed = calc_fuel(fuel_needed)

print("Part 2:", total2)

assert total2 == 4954799
