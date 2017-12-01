#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 15."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import re

DATA = """Disc #1 has 13 positions; at time=0, it is at position 1.
Disc #2 has 19 positions; at time=0, it is at position 10.
Disc #3 has 3 positions; at time=0, it is at position 2.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 3.
Disc #6 has 17 positions; at time=0, it is at position 5."""

discs = []
for line in DATA.split('\n'):
    disc, positions, startPosition = re.search(r'Disc #(\d+) has (\d+) positions; at time=0, it is at position (\d+).', line).group(1, 2, 3)
    discs.append([int(disc), int(positions), int(startPosition)])

def isDropTime(time, disc):
    return (disc[2] + time + disc[0]) % disc[1] == 0

def findDropTime():
    time = 1
    found = False
    while not found:
        if False in [isDropTime(time, disc) for disc in discs]:
            time += 1
        else:
            found = True
    print("First droptime is at:", time)

if __name__ == '__main__':
    print("The discs for part 1 are", discs)
    findDropTime()

    # Add the 7th disc for part 2: 11 positions starting at position 0
    discs.append((7, 11, 0))
    print("The discs for part 2 are", discs)
    findDropTime()