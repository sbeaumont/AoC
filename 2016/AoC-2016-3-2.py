#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 3 part 2.

The main difference with part one is that three lines are read at a time
and transposed before they are otherwise handled as in part 1."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

# Load
with open("santa2016-3-data.txt", 'r') as content_file:
    content = content_file.read()
content = content.split('\n')

# Process
possible = 0
for i in range(0, len(content), 3):

    # Transpose
    lines = []
    for j in range(3):
        lines.append([int(s) for s in content[i+j].split()])
    lines = list(map(list, zip(*lines)))

    # Check
    for line in lines:
        line.sort()
        if line[2] < line[0] + line[1]:
            possible += 1

print("Possible triangles", possible)