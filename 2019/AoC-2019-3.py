#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 3

I really, really didn't want to use any algorithms stolen from the interwebs.
Math is cool. I'm not cool. :-)
"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import load_input, cityblock_distance
from PIL import Image, ImageDraw

DIRECTIONS = {'R': (1, 0), 'D': (0, -1), 'L': (-1, 0), 'U': (0, 1)}


def parse_wire_data(data):
    wire_data = list()
    for line in data:
        wire = [(c[0], int(c[1:])) for c in line.strip().split(',')]
        wire_data.append(wire)
    return wire_data


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def astuple(self):
        return self.x, self.y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line(object):
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        self.horizontal = self.p1.y == self.p2.y

    @property
    def length(self):
        if self.horizontal:
            return abs(self.max_x - self.min_x)
        else:
            return abs(self.max_y - self.min_y)

    @property
    def as_tuple(self):
        return self.p1.x, self.p1.y, self.p2.x, self.p2.y

    @property
    def min_y(self):
        return min(self.p1.y, self.p2.y)

    @property
    def max_y(self):
        return max(self.p1.y, self.p2.y)

    @property
    def min_x(self):
        return min(self.p1.x, self.p2.x)

    @property
    def max_x(self):
        return max(self.p1.x, self.p2.x)

    def transpose(self, vec: Point):
        return Line(self.p1 + vec, self.p2 + vec)

    def intersects(self, other):
        """This version can't deal with parallel but overlapping lines. Luckily not needed..."""
        if self.horizontal == other.horizontal:
            if self.horizontal:
                if (self.p1.y == other.p2.y) and \
                        ((self.min_x <= other.p1.x <= self.max_x) or \
                        (self.min_x <= other.p2.x <= self.max_x)):
                    # OMG overlap...
                    assert False
            else:
                if (self.p1.x == other.p2.x) and \
                        ((self.min_y <= other.p1.y <= self.max_y) or \
                        (self.min_y <= other.p2.y <= self.max_y)):
                    # OMG overlap...
                    assert False
        else:
            if self.horizontal:
                if (self.min_x <= other.p1.x <= self.max_x) and \
                        (other.min_y <= self.p1.y <= other.max_y):
                    return Point(other.p1.x, self.p1.y)
            else:
                if self.min_y <= other.p1.y <= self.max_y and \
                        (other.min_x <= self.p1.x <= other.max_x):
                    return Point(self.p1.x, other.p1.y)
        return None

    def __repr__(self):
        return f"Line({self.p1.x}, {self.p1.y}), ({self.p2.x}, {self.p2.y}))"


def convert_to_lines(wire_data):
    wire_paths = list()
    min_x = min_y = max_x = max_y = 0
    for wire in wire_data:
        x = y = 0
        wire_path = list()
        for step in wire:
            direction = DIRECTIONS[step[0]]
            from_node = Point(x, y)
            x += direction[0] * step[1]
            y += direction[1] * step[1]
            min_x = min(x, min_x)
            max_x = max(x, max_x)
            min_y = min(y, min_y)
            max_y = max(y, max_y)
            to_node = Point(x, y)
            wire_path.append(Line(from_node, to_node))
        wire_paths.append(wire_path)
    return wire_paths, (min_x, min_y, max_x, max_y)


def draw_wires(wire_paths, minmax, line_width=1):
    min_x, min_y, max_x, max_y = minmax
    im = Image.new('RGB', (abs(max_x - min_x), abs(max_y - min_y)), (0, 0, 0))
    draw = ImageDraw.Draw(im)
    for line in wire_paths[0]:
        draw.line(line.transpose(Point(abs(min_x), abs(min_y))).as_tuple, (255, 255, 0), width=line_width)
    for line in wire_paths[1]:
        draw.line(line.transpose(Point(abs(min_x), abs(min_y))).as_tuple, (255, 0, 255), width=line_width)
    draw.ellipse((abs(min_x) - 5, abs(min_y) - 5, abs(min_x) + 5, abs(min_y) + 5), fill=(255, 255, 255))
    im.show()


def search_crossings(wire_path_0, wire_path_1):
    crossings = list()
    wire_0_length = 0
    for line0 in wire_path_0:
        wire_1_length = 0
        for line1 in wire_path_1:
            if line0 == wire_path_0[0] and line1 == wire_path_1[0]:
                wire_1_length += line1.length
                continue
            intersection = line0.intersects(line1)
            if intersection:
                total_length = wire_0_length + line0.p1.distance(intersection) + \
                               wire_1_length + line1.p1.distance(intersection)
                crossings.append((intersection, total_length))
            wire_1_length += line1.length
        wire_0_length += line0.length

    print(crossings)
    return crossings


def closest_crossing(crossings):
    # closest_crossing = None
    closest_distance = 10000000
    for crossing in [x[0] for x in crossings]:
        if crossing == (0, 0):
            continue

        distance = cityblock_distance(crossing.astuple)
        if distance < closest_distance:
            # closest_crossing = crossing
            closest_distance = distance

    # print(closest_crossing, closest_distance)
    return closest_distance


def shortest_length(crossings):
    sorted_crossings = sorted(crossings, key=lambda x: x[1])
    return sorted_crossings[0][1]


def do(data, show=False):
    wire_data = parse_wire_data(data)
    wire_paths, minmax = convert_to_lines(wire_data)
    if show:
        draw_wires(wire_paths, minmax, 10)
    return search_crossings(wire_paths[0], wire_paths[1])


if __name__ == '__main__':
    with open("AoC-2019-test-3-0.txt") as f:
        c0 = do(f.readlines())
        assert closest_crossing(c0) == 159
        assert shortest_length(c0) == 610, f"Expected 610, got {shortest_length(c0)}"

    with open("AoC-2019-test-3-1.txt") as f:
        c1 = do(f.readlines())
        assert closest_crossing(c1) == 135
        assert shortest_length(c1) == 410, f"Expected 610, got {shortest_length(c1)}"

    crossings = do(load_input(3), True)
    d = closest_crossing(crossings)
    assert d != 76
    print(f"Part 1: {d}")
    print(f"Part 2: {shortest_length(crossings)}")
