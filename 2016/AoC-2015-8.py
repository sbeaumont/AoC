#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 8 part 1."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

FILE_NAME = "AoC-2015-8-data.txt"

import ast

total = 0

f = open(FILE_NAME, "rb")
try:
    for line in f:
        convertedLine = str(line, 'utf-8').rstrip('\n')
        parsedline = ast.literal_eval(convertedLine.rstrip())
        total += len(convertedLine) - len(parsedline)
finally:
    f.close()

print("Total parsed difference", total)
