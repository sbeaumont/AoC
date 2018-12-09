#!/usr/bin/env python3

"""
Solution for Advent of Code challenge 2018 - Day 9

Assignment for 463 players; last marble is worth 71787 points

This solution works well because of the efficiency of collections.deque
"""

from collections import defaultdict, deque
import time

NUM_ELVES = 463
LAST_MARBLE = 71787
INSERT_CLOCKWISE = -1 # becomes current marble
SOMETHING_ENTIRELY_DIFFERENT = 23 # keep this marble, remove cc-wise
MOVE_CC = 7 # keep marble -7, current marble is -6


def play(last_marble):
    scores = defaultdict(int)
    circle = deque([0])
    next_marble_value = 1
    current_elf = 0
    while next_marble_value <= last_marble:
        if next_marble_value % SOMETHING_ENTIRELY_DIFFERENT == 0:
            scores[current_elf] += next_marble_value
            circle.rotate(MOVE_CC)
            scores[current_elf] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(INSERT_CLOCKWISE)
            circle.append(next_marble_value)

        next_marble_value += 1
        current_elf = (current_elf + 1) % NUM_ELVES
    return max(scores.values())


print(f"Part 1: {play(LAST_MARBLE)}")

print("Calculating Part 2...")

start = time.time()
print(f"Part 2: {play(LAST_MARBLE * 100)}")
end = time.time()

print(f"Part 2 took {end - start} seconds to run.")
