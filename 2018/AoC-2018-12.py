#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time

NUM_GENERATIONS = 20

start = time.time()

initial_state = "#.......##.###.#.#..##..##..#.#.###..###..##.#.#..##....#####..##.#.....########....#....##.#..##..."

with open("AoC-2018-12-input.txt") as infile:
    notes = ([[term.strip() for term in line.split("=>")] for line in infile])

current_state = list('.'*20 + initial_state + '.'*20)
print(current_state)
for gen in range(NUM_GENERATIONS):
    new_state = current_state[:]
    for i in range(len(current_state)):
        slice = ''.join(current_state[i - 2: i + 3])
        for note in notes:
            if slice == note[0]:
                new_state[i] = note[1]
    current_state = new_state
    print(''.join(current_state))

sum_of_plants = 0
for i in range(len(current_state)):
    if current_state[i] == '#':
        sum_of_plants += i - 20

print(f"Part 1: {sum_of_plants}")

print(f"{time.time() - start:.4f} seconds to run.")
