#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 11"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from intcode_computer import Computer
from collections import namedtuple, defaultdict
from visualize import Visualizer, Color


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return [int(x) for x in infile.read().strip().split(',')]


Point = namedtuple('Point', 'x y')
directions = (Point(0, 1), Point(1, 0), Point(0, -1), Point(-1, 0))
WHITE = Color(R=255, G=255, B=255)
BLACK = Color(R=0, G=0, B=0)


class Robot(object):
    def __init__(self, data, starting_panel):
        self.brain = Computer(data, starting_panel, pause_on_output=2)
        self.direction = 0
        self.pos = Point(0, 0)
        self.move_history = [self.pos]
        self.painted = dict()

    def turn(self, turn_direction):
        self.direction = (self.direction + (1 if turn_direction else -1)) % 4

    def move(self):
        move_direction = directions[self.direction]
        self.pos = Point(self.pos.x + move_direction.x, self.pos.y + move_direction.y)
        self.move_history.append(self.pos)

    def detect_color(self):
        return self.painted[self.pos] if self.pos in self.painted else 0

    def step(self):
        output = self.brain.run_program([self.detect_color()])
        if not self.brain.on_fire:
            panel_color, turn_direction = output
            self.painted[self.pos] = panel_color
            self.turn(turn_direction)
            self.move()


def do(data, starting_panel):
    robot = Robot(data, starting_panel)
    while not robot.brain.on_fire:
        robot.step()
    boundaries = Visualizer.boundaries(robot.painted.keys())
    if starting_panel == 1:
        viz = Visualizer(boundaries, 10)
        point_size = 5
    else:
        viz = Visualizer(boundaries, 100)
        point_size = 50
    for p, color in robot.painted.items():
        if color:
            viz.draw_square(p, WHITE, point_size)
    viz.show()
    return len(robot.painted)


def test(test_data, expected):
    test_result = do(test_data)
    assert test_result == expected, f"Expected {expected} but got {test_result}"


if __name__ == '__main__':
    # Check data
    print(f"Input data: {load_input(11)}\n")

    # Solve puzzle
    part1 = do(load_input(11), 0)
    print(f"Part 1: {part1}")

    # Solve puzzle
    part2 = do(load_input(11), 1)
    print(f"Part 1: {part2}")
