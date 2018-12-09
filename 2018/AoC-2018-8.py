#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 8 part 1

"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-8-input.txt") as infile:
    tree = [int(node) for node in infile.read().split(' ')]


def tree_iterator():
    for node in tree:
        yield node


def process(ti):
    result = 0
    children = next(ti)
    header = next(ti)
    for i in range(children):
        result += process(ti)
    for j in range(header):
        result += next(ti)
    return result


total = process(tree_iterator())

print(f"Total is: {total}")
assert total == 45618
