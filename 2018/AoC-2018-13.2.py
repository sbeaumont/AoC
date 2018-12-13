#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 13 part 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import numpy as np

start = time.time()

directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
cart_init = {'^': (0, '|'), '>': (1, '-'), 'v': (2, '|'), '<': (3, '-')}
cart_icons = ('^', '>', 'v', '<')

with open("AoC-2018-13-input.txt") as infile:
    data = ([list(line.rstrip('\n')) for line in infile])
    max_width = max([len(line) for line in data])
    max_height = len(data)

tracks = np.empty((max_width, max_height), dtype=str)


def init_carts():
    """Carts are ((x, y), direction, turns)"""
    result = []
    for y in range(max_height):
        for x in range(len(data[y])):
            tracks[x, y] = data[y][x]
            if tracks[x, y] in cart_init:
                init = cart_init[tracks[x, y]]
                result.append([(x, y), init[0], 0])
                tracks[x, y] = init[1]
    return result


def print_map():
    """Print map for debugging."""
    printmap = []
    for y in range(max_height):
        line = list(tracks[:, y])
        for cart in sorted(carts, key=lambda c: c[0]):
            if cart[0][1] == y:
                line[cart[0][0]] = cart_icons[cart[1] - 1]
        printmap.append(''.join(line))
    for line in printmap:
        print(line)


def turn(crt):
    """Turn cart based on underlying track"""
    changes = (-1, 0, 1)
    pos = crt[0]
    current_track = tracks[pos[0], pos[1]]
    if current_track in ('|', '-'):
        pass
    elif current_track == "\\":
        if crt[1] in (0, 2):
            crt[1] -= 1
        elif crt[1] in (1, 3):
            crt[1] += 1
    elif current_track == "/":
        if crt[1] in (0, 2):
            crt[1] += 1
        elif crt[1] in (1, 3):
            crt[1] -= 1
    elif current_track == "+":
        crt[1] = crt[1] + changes[crt[2] % 3]
        crt[2] += 1
    crt[1] = crt[1] % 4


carts = init_carts()
tick = 0
while len(carts) > 1:
    for cart in sorted(carts, key=lambda c: c[0]):
        # Calculate new position based on direction
        new_position = (cart[0][0] + directions[cart[1]][0], cart[0][1] + directions[cart[1]][1])

        # Check for crash
        for other_cart in [other for other in carts if other != cart]:
            if other_cart[0] == new_position:
                carts.remove(cart)
                carts.remove(other_cart)
                print(f"Crash at {new_position} on tick {tick}")

        # Move cart
        cart[0] = new_position

        # Turn cart (if applicable)
        turn(cart)

    tick += 1

#print_map()
print(f'Coordinates of last cart: {carts[0][0]}')

print(f"{time.time() - start:.4f} seconds to run.")
