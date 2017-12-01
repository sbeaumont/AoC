#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 18.

Can be optimised by not storing the map, but counting the safe spaces and moving on to the next row."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

# Should result in 38 safe tiles
TEST_DATA = ".^^.^.^^^^"
TEST_ROWS = 10

DATA = "^.^^^..^^...^.^..^^^^^.....^...^^^..^^^^.^^.^^^^^^^^.^^.^^^^...^^...^^^^.^.^..^^..^..^.^^.^.^......."
MAP_ROWS = 40
PART_TWO_ROWS = 400000

def generateMap(initialRow, numberOfRows):
    map = [initialRow, ]
    for row in range(numberOfRows - 1):
        extendedRow = '.{0}.'.format(map[row])
        newRow = []
        for columnset in [extendedRow[column - 1:column + 2] for column in range(1, len(initialRow) + 1)]:
            newRow.append('^' if columnset in ('.^^', '^^.', '..^', '^..') else '.')
        map.append(''.join(newRow))
    return map

def countSafeSpaces(map):
    return ''.join(map).count('.')

map = generateMap(TEST_DATA, TEST_ROWS)
print("Number of safe tiles in test map: {0}".format(countSafeSpaces(map)))

map = generateMap(DATA, MAP_ROWS)
print("Number of safe tiles in map: {0}".format(countSafeSpaces(map)))

map = generateMap(DATA, PART_TWO_ROWS)
print("Number of safe tiles in map for part 2: {0}".format(countSafeSpaces(map)))