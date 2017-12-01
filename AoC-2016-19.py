#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 19 part 1.

This is some butt-ugly code..."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"


PUZZLE_INPUT = 3005290

# Elf 3 should get it all
TEST_INPUT = 5

def createElves(numberOfElves):
    return [[i, 1] for i in range(1, numberOfElves + 1)]

def steal(elves):
    while len(elves) > 1:
        print("There are {0} elves.".format(len(elves)))
        stealingElf = 0
        loserElf = 1
        while stealingElf < len(elves):
            if elves[loserElf][1] > 0:
                elves[stealingElf][1] += elves[loserElf][1]
                elves[loserElf][1] = 0
                stealingElf = loserElf + 1 if loserElf > 0 else len(elves)
                loserElf = stealingElf + 1
            else:
                loserElf += 1
            # Wrap around
            if loserElf >= len(elves):
                loserElf = 0
        # Remove loser elves
        elves = [elf for elf in elves if elf[1] > 0]
    return elves[0]


elves = createElves(PUZZLE_INPUT)
winningElf = steal(elves)
print("Elf {0} gets all {1} presents!".format(winningElf[0], winningElf[1]))

# winningElf = createElves(PUZZLE_INPUT)
# # 908139 is too low
# print("Elf {0} gets all {1} presents!".format(winningElf[0], winningElf[1]))