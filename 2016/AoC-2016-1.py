#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 1 part 1.

Follow directions to final destination and calculate distance."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

DATA = """R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3"""

# Initialize
deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
x = y = 0
direction = 0

# Load
commands = DATA.split(', ')

# Process
for command in commands:
    # Parse turn and distance
    turn = command[0]
    distance = int(command[1:])

    # Turn
    direction = (direction + (1 if turn == 'R' else -1)) % 4

    # Jump to next coordinate
    x += deltas[direction][0] * distance
    y += deltas[direction][1] * distance

# Result
print ("Final distance:", abs(x) + abs(y))
