#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 11

Puzzle input 2568

"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import numpy as np

start = time.time()

GRID_SERIAL_NUMBER = 2568

grid = np.zeros((300, 300))

for x in range(300):
    for y in range(300):
        rack_id = x + 1 + 10
        power_level = rack_id * (y + 1)
        power_level += GRID_SERIAL_NUMBER
        power_level = power_level * rack_id
        hundreds_digit = int(str(power_level)[-3]) if len(str(power_level)) >=3 else 0
        power_level = hundreds_digit - 5
        grid[x, y] = power_level

max_top_left = None
max_power_level = -999
max_square_size = 1
for ss in range(1, 301):
    for x in range(300 - ss):
        for y in range(300 - ss):
            top_left = (x + 1, y + 1)
            square_total = 0
            for xs in range(x, x + ss):
                for ys in range(y, y + ss):
                    square_total += grid[xs, ys]
            if square_total > max_power_level:
                max_power_level = square_total
                max_top_left = top_left
                max_square_size = ss
                print(f"Found {max_top_left},{max_square_size} power level {max_power_level}")

print(f"Max power level {max_power_level} at {max_top_left},{max_square_size}")

print(f"{time.time() - start:.4f} seconds to run.")
