#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 17."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

import hashlib

PUZZLE_INPUT = 'hhhxzeay'
DIRECTIONS = ('U', 'D', 'L', 'R')
DIRECTION_VECTORS = ((0, -1), (0, 1), (-1, 0), (1, 0))
STARTING_COORDINATES = (0, 0)
VAULT_LOCATION = [3, 3]

def checkDoors(input):
    "Check if (Up, Down, Left, Right) door is open or closed."
    return [True if c in ('b', 'c', 'd', 'e', 'f') else False for c in hashlib.md5(bytes(input, 'utf-8')).hexdigest()[0:4]]

def walkTo(coordinates, delta):
    return [c + d for c, d in zip(coordinates, delta)]

def checkBounds(coordinates, delta):
    for coordinate in coordinates:
        if coordinate < 0 or coordinate > 3:
            return False
    return True

def walk(coordinates, input, paths):
    if coordinates == VAULT_LOCATION:
        paths.append(input)
        print("Found vault with path: {0}".format(input))
    else:
        for isOpen, direction, delta in zip(checkDoors(input), DIRECTIONS, DIRECTION_VECTORS):
            newCoordinates = walkTo(coordinates, delta)
            if isOpen and checkBounds(newCoordinates, delta):
                walk(newCoordinates, input + direction, paths)

if __name__ == '__main__':
    paths = []
    walk(STARTING_COORDINATES, PUZZLE_INPUT, paths)
    print("Shortest path is: {0}".format(min(paths, key=len)[len(PUZZLE_INPUT):]))
    print("Longest path length is: {0}".format(len(max(paths, key=len)[len(PUZZLE_INPUT):])))