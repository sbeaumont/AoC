#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 6 part 1.

My own naive implementation, without collections.Counter coolness"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

# Load
with open("AoC-2016-6-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

answer = ''
part2answer = ''
# zip transposes the lists: each column is now a line.
for line in zip(*lines):
    lineString = "".join(line)

    mostFrequentCount = 0
    mostFrequent = ''
    leastFrequentCount = len(lineString)
    leastFrequent = ''

    for c in set(line):
        # Find character for part 1 solution: most frequent
        if lineString.count(c) > mostFrequentCount:
            mostFrequentCount = lineString.count(c)
            mostFrequent = c

        # Find character for part 2 solution: least frequent
        if lineString.count(c) < leastFrequentCount:
            leastFrequentCount = lineString.count(c)
            leastFrequent = c

    answer += mostFrequent
    part2answer += leastFrequent

print("The answer based on most frequent characters is:", answer)
print("The answer based on least frequent characters is:", part2answer)