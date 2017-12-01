#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 5 part 1.

Straightforward regex challenge."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re

with open("AoC-2015-5-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

vowelPattern = re.compile('[aeiou]')
doublesPattern = re.compile('(?P<c>[a-z])(?P=c)')
wrongCombosPattern = re.compile('ab|cd|pq|xy')

nice = 0
for s in lines:
    numberOfVowels = len(vowelPattern.findall(s))
    if (numberOfVowels >= 3) and doublesPattern.search(s) and not wrongCombosPattern.search(s):
        nice += 1

print("Nice strings:", nice)