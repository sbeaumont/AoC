#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 10

This is the original version that was used to solve the challenge."""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from collections import namedtuple, defaultdict
from math import hypot, atan2, degrees, pi
from functools import partial
from visualize import Visualizer, COLORS


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return [[y for y in x] for x in infile.readlines()]


Point = namedtuple('Point', 'x y')


def distance(one, two):
    return one.distance(two)


def rad_to_deg(angle):
    # return (-angle + pi/2) % (2*pi)
    return (degrees(angle) + 90) % 360


class Asteroid(object):
    def __init__(self, xy: Point):
        self.xy = xy

    @property
    def x(self):
        return self.xy.x

    @property
    def y(self):
        return self.xy.y

    def distance(self, other):
        x_dist = abs(other.x - self.x)
        y_dist = abs(other.y - self.y)
        d = hypot(x_dist, y_dist)
        return d

    def angle(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        return atan2(delta_y, delta_x)

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.xy == other.xy)

    def __hash__(self):
        return hash(self.xy)

    def __repr__(self):
        return f"Asteroid(Point({self.x}, {self.y}))"


def init_asteroids(data):
    result = dict()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == '#':
                result[Point(x, y)] = Asteroid(Point(x, y))
    return result


def asteroids_by_angle(current, asteroids):
    curr_distance = partial(distance, current)
    sorted_keys = sorted(asteroids, key=lambda a: curr_distance(a))

    a_by_angle = list()
    for key in sorted_keys:
        asteroid = asteroids[key]
        if asteroid == current:
            continue
        a_by_angle.append((current.angle(asteroid), current.distance(asteroid), asteroid))

    return sorted(a_by_angle)


def check_visible(current, asteroids):
    a_by_angle = asteroids_by_angle(current, asteroids)

    visible_asteroids = dict()
    for a in a_by_angle:
        if a[0] not in visible_asteroids:
            visible_asteroids[a[0]] = (*a, rad_to_deg(a[0]))

    return visible_asteroids


def do(data):
    asteroids = init_asteroids(data)
    max_visible = 0
    result = None
    for asteroid in asteroids.values():
        asteroid.visible = check_visible(asteroid, asteroids)
        if len(asteroid.visible) > max_visible:
            max_visible = len(asteroid.visible)
            result = asteroid
    return result


def do_part_2(station, data):
    viz = Visualizer((0, 0, 36, 36), 20, flip_vertical=False)
    print(f"\nThe asteroid can see this:")
    asteroids = init_asteroids(data)
    asteroids_by_degrees = list()
    for a in asteroids_by_angle(station, asteroids):
        asteroids_by_degrees.append((rad_to_deg(a[0]), *a))
    # for a in sorted(asteroids_by_degrees):
    #     print(a)

    sets_by_angle = defaultdict(list)
    for a in sorted(asteroids_by_degrees):
        sets_by_angle[a[0]].append(a[3])

    for k, v in sets_by_angle.items():
        if len(v) > 0:
            print(k, len(v), v)
            for a in v:
                if a.xy == (0, 2):
                    print('^^^^^^^^')

    asteroids_shot = 0
    last_asteroid_shot = None
    while asteroids_shot < 200:
        for k, v in sets_by_angle.items():
            last_asteroid_shot = v[0]
            sets_by_angle[k] = v[1:]
            asteroids_shot += 1
            viz.draw_line((station.xy, last_asteroid_shot.xy), COLORS[1], 2)
            viz.draw_point(last_asteroid_shot.xy, COLORS[2], 4)
            print(f"Boom, shot asteroid nr. {asteroids_shot}: {last_asteroid_shot}")
            if asteroids_shot == 200:
                code = last_asteroid_shot.x * 100 + last_asteroid_shot.y
                print(f"200th asteroid shot is: {last_asteroid_shot}: {code}")
                break
    viz.draw_point(station.xy, COLORS[0], 10)
    viz.show()
    return 0


if __name__ == '__main__':
    result = do(load_input(10))

    # Part 1
    print(f"\nPart 1: {result} with {len(result.visible)} visible asteroids.")

    # Part 2
    result = do_part_2(result, load_input(10))

    # 3207 is too high
    # 2 is wrong


