#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 7"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from pprint import pprint

with open(f"AoC-2020-7-input.txt") as infile:
    rules_file = [line.strip() for line in infile.readlines()]
    print(rules_file, '\n')

rules = dict()
for rule in rules_file:
    key = rule.split('contain')[0][:-6]
    sub_bags = rule.split('contain')[1].strip().split(',')
    if sub_bags[0] != 'no other bags.':
        value = {' '.join(sub_bag.split()[1:3]): int(sub_bag.split()[0]) for sub_bag in sub_bags}
    else:
        value = {}
    rules[key] = value


def recurse_bags(parent_bag):
    child_bags = 0
    for k, v in rules[parent_bag].items():
        child_bags += recurse_bags(k) * v
    return child_bags + 1


# -1, don't count the outer bag
print(recurse_bags('shiny gold') - 1)
