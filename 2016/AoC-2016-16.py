#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 16."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

INPUT = "11110010111001001"
FILL_LENGTH = 272
FILL_LENGTH_PART_2 = 35651584

def dragonize(s):
    reverse = ''.join(['1' if x == '0' else '0' for x in s[::-1]])
    return "{0}0{1}".format(s, reverse)

def createFiller(input, length):
    filler = input
    while len(filler) < length:
        filler = dragonize(filler)
    return filler[:length]

def checksum(input):
    result = ''.join(['1' if s[0] == s[1] else '0' for s in [input[i:i+2] for i in range(0, len(input), 2)]])
    if len(result) % 2 == 0:
        return checksum(result)
    else:
        return result

filler = createFiller(INPUT, FILL_LENGTH)
print("Part 1:", checksum(filler))

filler = createFiller(INPUT, FILL_LENGTH_PART_2)
print("Part 2:", checksum(filler))


