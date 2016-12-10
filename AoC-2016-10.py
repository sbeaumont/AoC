#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 10 part 1 and 2."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re
import operator
import functools

# Load
with open("AoC-2016-10-data.txt", 'r') as content_file:
    lines = [line.strip() for line in content_file]

botPattern = re.compile(r'(bot (\d+)) gives low to ((bot|output) (\d+)) and high to ((bot|output) (\d+))')
valuePattern = re.compile(r'value (\d+) goes to (bot (\d+))')

class Bot:
    def __init__(self, bots, name, low, high):
        self.name = name
        self.bots = bots
        self.low = low
        self.high = high
        self.chips = []

    def receiveChip(self, value):
        self.chips.append(value)
        #print("I am {0:7} and just received chip {1:3}. I now have {2}".format(self.name, value, sorted(self.chips)))
        if len(self.chips) >= 2:
            if sorted(self.chips) == [17, 61]:
                # Answer to part 1.
                print("I am {0}, and I am comparing chip 17 and 61!".format(self.name))
            self.bots[self.low].receiveChip(min(self.chips))
            self.bots[self.high].receiveChip(max(self.chips))
            self.chips = []

class Output:
    def __init__(self, name):
        self.name = name
        self.chips = []

    def receiveChip(self, value):
        self.chips.append(value)

# First initialize all the bots
bots = {}
for line in lines:
    if line.startswith('bot'):
        bot, low, high, botOrOutput1, botOrOutput2 = re.search(botPattern, line).group(1, 3, 6, 4, 7)
        bots[bot] = Bot(bots, bot, low, high)
        if botOrOutput1 == 'output':
            bots[low] = Output(low)
        if botOrOutput2 == 'output':
            bots[high] = Output(high)

# Then load all the values
for line in lines:
    if line.startswith('value'):
        value, bot = re.search(valuePattern, line).group(1, 2)
        bots[bot].receiveChip(int(value))

# For part 2 multiply outputs 0, 1 and 2
outputs = []
for i in range(3):
    outputs.extend(bots['output ' + str(i)].chips)

print("\nThe multiplied value of outputs 0-2 is:", functools.reduce(operator.mul, outputs, 1))