#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time

NUM_GENERATIONS = 1000
NUM_TOTAL_GENERATIONS = 50000000000

start = time.time()

initial_state = "#.......##.###.#.#..##..##..#.#.###..###..##.#.#..##....#####..##.#.....########....#....##.#..##..."

with open("AoC-2018-12-input.txt") as infile:
    notes = ([[term.strip() for term in line.split("=>")] for line in infile])

shift = -5
current_state = list('.' * abs(shift) + initial_state)
print(current_state)
for gen in range(NUM_GENERATIONS):
    # Find match in notes
    new_state = current_state[:]
    for i in range(len(current_state)):
        pots = ''.join(current_state[i - 2: i + 3])
        for note in notes:
            if pots == note[0]:
                new_state[i] = note[1]

    # This pattern grows by / moves to the right with one item per iteration
    new_state.append('.')

    # Chop left side, change shift value to match
    if new_state[0:10] == ['.'] * 10:
        new_state = new_state[5:]
        shift += 5
    current_state = new_state

# Now we "cheat" by shifting the stable pattern to where it would be after gazillion iterations.
end_shift = NUM_TOTAL_GENERATIONS - NUM_GENERATIONS + shift

sum_of_plants = 0
for i in range(len(current_state)):
    if current_state[i] == '#':
        sum_of_plants += i + end_shift

print(f"Part 2: {sum_of_plants}")

assert sum_of_plants == 3250000000956

print(f"{time.time() - start:.4f} seconds to run.")