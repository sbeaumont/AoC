#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 5 part 2.

Straightforward regex challenge."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re

with open("AoC-2015-5-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

twoDoublesPattern = re.compile('(?P<two>[a-z]{2}).*(?P=two)')
xyxPattern = re.compile('(?P<c>[a-z])[a-z](?P=c)')

nice = 0
for s in lines:
    if twoDoublesPattern.search(s) and xyxPattern.search(s):
        nice += 1

print("Nice strings:", nice)