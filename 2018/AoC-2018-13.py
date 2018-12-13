#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 13 part 1

This solution is not the cleaned up version of part 2.
Shows the panic mode version of the code.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import numpy as np

start = time.time()

with open("AoC-2018-13-input.txt") as infile:
    data = ([list(line) for line in infile])
    max_width = max([len(line) for line in data])
    max_height = len(data)

print(max_width, max_height)

tracks = np.empty((max_width, max_height), dtype=str)

directions = ((0, -1), (1, 0), (0, 1), (-1, 0))


def init_carts():
    """Carts are ((x, y), direction, turns)"""
    cart_init = {'^': (1, '|'), '>': (2, '-'), 'v': (3, '|'), '<': (4, '-')}
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
    cart_icons = ('^', '>', 'v', '<')
    printmap = []
    for y in range(max_height):
        line = list(tracks[:, y])
        for cart in sorted(carts, key=lambda c: c[0]):
            if cart[0][1] == y:
                line[cart[0][0]] = cart_icons[cart[1] - 1]
        printmap.append(''.join(line))
    for line in printmap:
        print(line)


def check_turn(crt):
    changes = (-1, 0, 1)
    pos = crt[0]
    current_track = tracks[pos[0], pos[1]]
    if current_track in ('|', '-'):
        pass
    elif current_track == "\\":
        if crt[1] in (1, 3):
            crt[1] -= 1
        elif crt[1] in (2, 4):
            crt[1] += 1
    elif current_track == "/":
        if crt[1] in (1, 3):
            crt[1] += 1
        elif crt[1] in (2, 4):
            crt[1] -= 1
    elif current_track == "+":
        crt[1] = crt[1] + changes[crt[2] % 3]
        crt[2] += 1
    if crt[1] == 5:
        crt[1] = 1
    elif crt[1] == 0:
        crt[1] = 4

carts = init_carts()
crashed = False
tick = 0
while not crashed:
    for cart in sorted(carts, key=lambda c: c[0]):
        new_position = (cart[0][0] + directions[cart[1] - 1][0], cart[0][1] + directions[cart[1] - 1][1])

        # Check for crash
        for other_cart in [other for other in carts if other != cart]:
            if other_cart[0] == new_position:
                crashed = True
                print(f"Crash at {new_position} on tick {tick}")
                break

        # Move cart
        cart[0] = new_position

        # Check for turn
        check_turn(cart)

    #print_map()

    tick += 1

assert crashed
assert not cart[0] == (65, 48)

print(f"{time.time() - start:.4f} seconds to run.")
