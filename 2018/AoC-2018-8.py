#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 8 part 1

"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

with open("AoC-2018-8-input.txt") as infile:
    tree = [int(node) for node in [line.strip().split(" ") for line in infile.readlines()][0]]


def tree_iterator():
    for node in tree:
        yield node


def process(ti):
    total = 0
    children = next(ti)
    header = next(ti)
    for i in range(children):
        total += process(ti)
    for j in range(header):
        total += next(ti)
    return total


print("Total is: {}".format(process(tree_iterator())))
