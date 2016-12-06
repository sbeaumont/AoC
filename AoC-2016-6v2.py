#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 5 part 1.

Based on Jeroen's suggestion to use Counter."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

from collections import Counter

# Load
lines = []
with open("AoC-2016-6-data.txt", 'r') as content_file:
    for line in content_file:
        lines.append(list(line.strip('\n')))

answer = ''
part2answer = ''
# zip transposes the lists: each column is now a line.
for line in zip(*lines):
    cnt = Counter(line)
    answer += str(cnt.most_common()[0][0])
    part2answer += str(cnt.most_common()[-1][0])

print("The answer based on most frequent characters is:", answer)
print("The answer based on least frequent characters is:", part2answer)