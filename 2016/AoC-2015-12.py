#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2015, day 12 parts 1 and 2."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

FILE_NAME = "AoC-2015-12-data.json"

import re, json
import collections

# Load
with open(FILE_NAME, 'r') as content_file:
    content = content_file.read()

# Solution of part 1: find all numbers and add them
numbers = [int(s) for s in re.findall(r'-?\d+', content)]
print("Solution to part 1. The sum of all numbers in the file is:", sum(numbers))

# Now load it as a real data structure
data = json.loads(content)

# Used the traversal code at http://nvie.com/posts/modifying-deeply-nested-structures/
def traverse(obj):
    total = 0
    if isinstance(obj, dict):
        if "red" not in obj.values():
            total += sum([traverse(v) for k, v in obj.items()])
    elif isinstance(obj, list):
        total += sum([traverse(elem) for elem in obj])
    else:
        if isinstance(obj, int):
            total += int(obj)

    return total

print("No Red Dictionaries!", traverse(data))

