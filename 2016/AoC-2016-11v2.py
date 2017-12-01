#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 11.

Assignment:

The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant.

Rules to implement:

As long as I'm not on the top floor:
- If two chips can move up safely, do that.
- If two generators can be brought up safely, do that. Choose generators first that have a match on the closest higher level.
- if a chip and a generator can be brought up safely, do that.
- if a pair can be brought up safely, do that.
(As long as I'm not on the lowest floor:)
- If one chip can be brought down safely, do that.
- If one generator can be brought down safely, do that.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

from AoC201611Level import Level

MAP = {
    4: [],
    3: ['TM'],
    2: ['TG', 'RG', 'RM', 'CG', 'CM'],
    1: ['SG', 'SM', 'PG', 'PM']
}

def createLevel(level):
    return Level(level)

levels = MAP.copy()

elevator = 1

def moveTwoChips(fromLevel, toLevel):
    if len(fromLevel.generators()) <= 2 and len(fromLevel.microchips()) >= 2:
        toMove = fromLevel.pairedMicrochips()
        if len(toMove) < 2:
            toMove.append(fromLevel.unpairedMicrochips()[0:3 - len(toMove)])
        newToLevel = Level(toLevel.contents + toMove)
        newFromLevel = Level(fromLevel.contents - toMove)
        return newToLevel.isSafe() and newFromLevel.isSafe()

def moveTwoGenerators(fromLevel, toLevel):
    if len(fromLevel.generators()) == 2 or len(fromLevel.microchips()) == 0:
        toMove = fromLevel.pairedMicrochips()
        if len(toMove) < 2:
            toMove.append(fromLevel.unpairedMicrochips()[0:3 - len(toMove)])
        newToLevel = Level(toLevel.contents + toMove)
        newFromLevel = Level(fromLevel.contents - toMove)
        return newToLevel.isSafe() and newFromLevel.isSafe()


for i in range(3):
    if elevator < 4:
        if moveTwoChips(levels[elevator], levels[elevator + 1]): continue
        if moveTwoGenerators(levels[elevator], levels[elevator + 1]): continue
