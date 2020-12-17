#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 12"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


from math import cos, sin, radians, degrees, atan2, hypot, tau


def load_file(filename):
    with open(filename) as infile:
        return [(line[0], int(line.strip()[1:])) for line in infile.readlines()]


class Ship(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint = (10, 1)

    @property
    def heading(self):
        return atan2(self.waypoint[1], self.waypoint[0])

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def turn(self, dgs):
        rotation = radians(-dgs)
        wx, wy = self.waypoint
        xx = (wx * cos(rotation)) + (wy * sin(rotation))
        yy = (-wx * sin(rotation)) + (wy * cos(rotation))
        self.waypoint = (xx, yy)

    def forward(self, dist):
        self.x += self.waypoint[0] * dist
        self.y += self.waypoint[1] * dist

    def do_instruction(self, instruction):
        command, parameter = instruction
        if command == 'F':
            self.forward(parameter)
        elif command == 'R':
            self.turn(-parameter)
        elif command == 'L':
            self.turn(parameter)
        elif command == 'N':
            self.waypoint = (self.waypoint[0], self.waypoint[1] + parameter)
        elif command == 'S':
            self.waypoint = (self.waypoint[0], self.waypoint[1] - parameter)
        elif command == 'E':
            self.waypoint = (self.waypoint[0] + parameter, self.waypoint[1])
        elif command == 'W':
            self.waypoint = (self.waypoint[0] - parameter, self.waypoint[1])
        else:
            assert False, f"Instruction {instruction} not understood."


def do(filename, verbose=False):
    instructions = load_file(filename)
    ship = Ship()
    if verbose:
        print(instructions)
    for instruction in instructions:
        ship.do_instruction(instruction)
        if verbose:
            print(ship.x, ship.y, ship.waypoint)
    return ship.x, ship.y, ship.waypoint, ship.manhattan_distance


if __name__ == '__main__':
    test_1 = do("AoC-2020-12-test-1.txt", True)
    print(test_1)
    # assert test_1 == (214, -72, (4, -10), 286)

    part_1 = do("AoC-2020-12-input.txt")
    print(part_1)
    assert part_1[-1] > 17782
