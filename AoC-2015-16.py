#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 4 part 1 and 2.

Pretty printed the full list of decoded rooms because they're fun."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

TICKER_DATA = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

TICKER_RANGES = {
    'cats': '>',
    'trees': '>',
    'pomeranians': '<',
    'goldfish': '<'
}

import pprint, re

ticker = {}
for line in TICKER_DATA.split('\n'):
    trait, amount = line.split(':')
    ticker[trait] = int(amount)

suePattern = re.compile(r'Sue (\d+)')
traitPattern = re.compile(r'([\w]+): (\d+)')

matchingPart1Sues = {}
matchingPart2Sues = {}
with open("AoC-2015-16-data.txt", 'r') as input_file:
    for line in input_file:
        sueNumber = re.search(suePattern, line).groups(0)[0]

        traits = {}
        matchedPart1 = 0
        matchedPart2 = 0
        for trait, amount in re.findall(traitPattern, line):
            traits[trait] = int(amount)
            if trait in TICKER_RANGES.keys():
                if (TICKER_RANGES[trait] == '<') and (int(amount) < ticker[trait]):
                    matchedPart2 += 1
                elif (TICKER_RANGES[trait] == '>') and (int(amount) > ticker[trait]):
                    matchedPart2 += 1
            elif ticker[trait] == int(amount):
                matchedPart2 += 1

            if ticker[trait] == int(amount):
                matchedPart1 += 1

        if matchedPart1 == 3:
            matchingPart1Sues[sueNumber] = traits

        if matchedPart2 == 3:
            matchingPart2Sues[sueNumber] = traits

print("Part 1 solution:", matchingPart1Sues)
print("Part 2 solution:", matchingPart2Sues)