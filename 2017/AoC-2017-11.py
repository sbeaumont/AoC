#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017

[Hex Ed](http://adventofcode.com/2017/day/11)

Solution for the hex math taken from awesome article on: https://www.redblobgames.com/grids/hexagons/"""


class Hex(object):

    def __init__(self, q, r):
        self.q = q
        self.r = r
        self.s = q - r

    def __init__(self, q, r, s):
        assert q + r + s == 0
        self.q = q
        self.r = r
        self.s = s

    def __eq__(self, other):
        return self.q == other.q and self.r == other.r and self.s == other.s

    def __add__(self, other):
        return Hex(self.q + other.q, self.r + other.r, self.s + other.s)

    def __sub__(self, other):
        return Hex(self.q - other.q, self.r - other.r, self.s - other.s)

    def __mul__(self, other):
        return Hex(self.q * other.q, self.r * other.r, self.s * other.s)

    def length(self):
        return int((abs(self.q) + abs(self.r) + abs(self.s)) / 2)

    def distance_to(self, other):
        return (self - other).length()

    def __repr__(self):
        return "Hex({}, {}, {})".format(self.q, self.r, self.s)

DIR_N  = Hex(0, 1, -1)
DIR_NE = Hex(1, 0, -1)
DIR_SE = Hex(1, -1, 0)
DIR_S  = Hex(0, -1, 1)
DIR_SW = Hex(-1, 0, 1)
DIR_NW = Hex(-1, 1, 0)

HEX_DIRS = {'n': DIR_N, 'ne': DIR_NE, 'se': DIR_SE, 's': DIR_S, 'sw': DIR_SW, 'nw': DIR_NW}

ORIGIN = Hex(0, 0, 0)

current = ORIGIN
max_distance = 0
with open("AoC-2017-11-input.txt") as puzzle_input_file:
    for step in puzzle_input_file.read().split(','):
        current += HEX_DIRS[step.strip()]
        current_distance = current.distance_to(ORIGIN)
        if current_distance > max_distance:
            max_distance = current_distance

print("The distance of {} to origin is {}".format(current, current.distance_to(ORIGIN)))
print("The maximum distance during the run was {}".format(max_distance))
