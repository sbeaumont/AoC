#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 8 part 2."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

FILE_NAME = "AoC-2015-8-data.txt"

import re

total = 0

f = open(FILE_NAME, "rb")
try:
    for line in f:
        convertedLine = str(line, 'utf-8').rstrip('\n')
        replacedLine = '"' + re.sub(r'\\|\"', r'\\\g<0>', convertedLine) + '"'
        total += len(replacedLine) - len(convertedLine)
finally:
    f.close()

print("Total parsed difference", total)
