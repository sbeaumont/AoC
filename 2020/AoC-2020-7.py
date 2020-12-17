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
    value = [' '.join(sub_bag.split()[1:3]) for sub_bag in rule.split('contain')[1].strip().split(',')]
    rules[key] = value

pprint(rules)


def outer_bags(inner_bag, bags):
    direct_outer = [k for k, v in rules.items() if inner_bag in v]
    for bag in direct_outer:
        outer_bags(bag, bags)
    bags.add(inner_bag)


# -1, don't count 'shiny gold'
shiny_gold_outers = set()
outer_bags('shiny gold', shiny_gold_outers)
shiny_gold_outers.remove('shiny gold')
print(len(shiny_gold_outers))

