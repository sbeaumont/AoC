#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 9 part 1 and 2."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re

# Load
with open("AoC-2016-9-data.txt", 'r') as content_file:
    lines = ''.join([line.strip() for line in content_file])

pattern = re.compile(r'(.*?)\((\d+)x(\d+)\)')

def expand(toscan):
    expandedLength = 0
    while len(toscan) > 0:
        match = re.search(pattern, toscan)

        if match:
            beforeExpansion = match.group(1)
            expansionLength = int(match.group(2))
            expansionRepeats = int(match.group(3))

            start = int(match.end(0))
            end = start + expansionLength
            expandedLength += len(beforeExpansion)
            expandedLength += expand(toscan[start:end]) * expansionRepeats

            toscan = toscan[end:]
        else:
            expandedLength += len(toscan)
            break
    return expandedLength

print(expand(lines), "expecting 102239 for part 1.")