#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-input-1.txt") as infile:
    changes = [int(line) for line in infile.readlines()]

frequencies_seen = set()
current_frequency = 0
double_frequency_found = False

while not double_frequency_found:
    for change in changes:
        current_frequency += change
        if current_frequency in frequencies_seen:
            print("First frequency found twice: {}".format(current_frequency))
            double_frequency_found = True
            break
        else:
            frequencies_seen.add(current_frequency)
