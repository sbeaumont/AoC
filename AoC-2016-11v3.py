#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 11.

Assignment:

The first floor contains a strontium generator, a strontium-compatible microchip, a plutonium generator, and a plutonium-compatible microchip.
The second floor contains a thulium generator, a ruthenium generator, a ruthenium-compatible microchip, a curium generator, and a curium-compatible microchip.
The third floor contains a thulium-compatible microchip.
The fourth floor contains nothing relevant.

Algorithm:

- If you can push up two generators, do so.
- otherwise go down with a generator (with the highest M)
- if there is no free generator push down 2M
- if there are levels at or above the lowest level of generators with 2M, push down 2M or a pair

"""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

MAP = {
    4: tuple(),
    3: ('TM'),
    2: ('TG', 'RG', 'RM', 'CG', 'CM'),
    1: ('SG', 'SM', 'PG', 'PM')
}

elevator = 1

def generators(level):
    return [g for g in level if g[-1] == 'G']

def unprotectedMicrochips(level):
    return [m for m in level if (m[-1] == 'M') and (m[0] + 'G' not in level)]

def isSafe(level):
    return not (generators(level) and unprotectedMicrochips(level))

def moveTwoGenerators():
    if elevator == len(MAP) or len(generators()) < 2:
        return False

    freeChips = unprotectedMicrochips[MAP[elevator + 1]]
    if not freeChips:

    movable =
    if ge

    nextLevel = MAP[elevator] +
    if isSafe()

for i in range(4):
    pass