#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 12"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


from math import cos, sin, radians


def load_file(filename):
    with open(filename) as infile:
        return [(line[0], int(line.strip()[1:])) for line in infile.readlines()]


class Ship(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 0

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    def turn(self, dgs):
        self.heading = (self.heading + dgs) % 360

    def forward(self, dist):
        self.x = self.x + round((cos(radians(self.heading)) * dist))
        self.y = self.y + round((sin(radians(self.heading)) * dist))

    def do_instruction(self, instruction):
        command, parameter = instruction
        if command == 'F':
            self.forward(parameter)
        elif command == 'R':
            self.turn(-parameter)
        elif command == 'L':
            self.turn(parameter)
        elif command == 'N':
            self.y += parameter
        elif command == 'S':
            self.y -= parameter
        elif command == 'E':
            self.x += parameter
        elif command == 'W':
            self.x -= parameter
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
            print(ship.x, ship.y, ship.heading)
    return ship.x, ship.y, ship.heading, ship.manhattan_distance


if __name__ == '__main__':
    test_1 = do("AoC-2020-12-test-1.txt")
    print(test_1)
    assert test_1 == (17, -8, 270, 25)

    part_1 = do("AoC-2020-12-input.txt")
    print(part_1)
    # assert part_1 == (17, -8, 270, 25)

    print("Part 1:", part_1[-1])
