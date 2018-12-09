#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 2 Part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-2-input.txt") as infile:
    box_ids = [line.strip() for line in infile]

two_times = 0
three_times = 0
for box_id in box_ids:
    two_letter_match = False
    three_letter_match = False
    for unique_letter in set(box_id):
        if box_id.count(unique_letter) == 2:
            two_letter_match = True
        elif box_id.count(unique_letter) == 3:
            three_letter_match = True
        if two_letter_match and three_letter_match:
            break
    two_times += 1 if two_letter_match else 0
    three_times += 1 if three_letter_match else 0

print("Checksum is {}".format(two_times * three_times))

