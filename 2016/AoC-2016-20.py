#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 20."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

def splitLine(line):
    start, end = line.strip().split('-')
    return (int(start), int(end))

def sortRanges(ranges):
    return sorted(ranges, key=lambda rng: rng[0])

def checkOverlap(rangeToCheck):
    "Check if there is an overlapping or connecting range in the ranges list. Assumes there is no current overlap in that list."
    for rng in ranges:
        if (rangeToCheck[0] >= (rng[0] - 1) and rangeToCheck[0] <= (rng[1] + 1)) or (rangeToCheck[1] >= (rng[0] - 1) and rangeToCheck[1] <= (rng[1] + 1)):
            return rng

# Load
with open("AoC-2016-20-data.txt", 'r') as content_file:
    lines = [splitLine(line) for line in content_file]

lines = sortRanges(lines)
ranges = []

# Parse
for line in lines:
    overlap = checkOverlap(line)
    if overlap:
        newRange = (min(overlap[0], line[0]), max(overlap[1], line[1]))
        ranges.remove(overlap)
        ranges.append(newRange)
    else:
        ranges.append(line)

# Print answer to part 1
print("Number of input ranges: {0}".format(len(lines)))
print("Number of non-overlapping ranges: {0}".format(len(ranges)))
sortedRanges = sorted(ranges, key=lambda rng: rng[0])
print(sortedRanges)
print("Lowest free IP is: {0}".format(sortedRanges[0][1] + 1))

# Answer part 2
MAX_IP = 4294967295
allowedIPs = 0
currentRange = sortedRanges[0]
for rng in sortedRanges[1:]:
    allowedIPs += rng[0] - currentRange[1] - 1
    currentRange = rng
allowedIPs += MAX_IP - sortedRanges[-1][1]
print("Number of allowed IPs: {0}".format(allowedIPs))