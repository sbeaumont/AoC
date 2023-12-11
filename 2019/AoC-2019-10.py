#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 10"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from collections import namedtuple, defaultdict
from math import hypot, atan2, degrees, pi
from functools import partial
from visualize import Visualizer, COLORS, Color


def load_input(day):
    with open(f"AoC-2019-input-{day}.txt") as infile:
        return [[y for y in x] for x in infile.readlines()]


Point = namedtuple('Point', 'x y')
Location = namedtuple('Location', 'angle distance asteroid')


def rad_to_deg(angle):
    return (degrees(angle) + 90) % 360


class Asteroid(object):
    def __init__(self, xy: Point):
        self.xy = xy
        self.visible = dict()

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
        a = atan2(delta_y, delta_x)
        return (degrees(a) + 90) % 360

    def check_visible(self, asteroids):
        visible_asteroids = dict()
        for location in self.locations_by_angle(asteroids):
            if location.angle not in visible_asteroids:
                self.visible[location.angle] = location

    def locations_by_angle(self, asteroids):
        def distance_to(one, two):
            return one.distance(two)

        curr_distance = partial(distance_to, self)

        a_by_angle = list()
        for key in sorted(asteroids, key=lambda a: curr_distance(a)):
            asteroid = asteroids[key]
            if asteroid == self:
                continue
            a_by_angle.append(Location(self.angle(asteroid), self.distance(asteroid), asteroid))

        return sorted(a_by_angle)

    def __eq__(self, other):
        return isinstance(other, type(self)) and (self.xy == other.xy)

    def __hash__(self):
        return hash(self.xy)

    def __repr__(self):
        return f"Asteroid(Point({self.x}, {self.y}))"


def init_asteroids(data):
    asteroids = dict()
    for y, row in enumerate(data):
        for x, c in enumerate(row):
            if c == '#':
                asteroids[Point(x, y)] = Asteroid(Point(x, y))
    return asteroids


def do(data):
    asteroids = init_asteroids(data)
    max_visible = 0
    result = None
    for asteroid in asteroids.values():
        asteroid.check_visible(asteroids)
        if len(asteroid.visible) > max_visible:
            max_visible = len(asteroid.visible)
            result = asteroid
    return result


def do_part_2(station, data, asteroids_max: str|int=200):
    asteroids = init_asteroids(data)

    viz = Visualizer((-1, -1, 36, 36), 20, False)
    for xy in asteroids:
        viz.draw_point(xy, COLORS[2], 4)

    grouped_by_angle = defaultdict(list)
    total_asteroids = 0
    for location in station.locations_by_angle(asteroids):
        grouped_by_angle[location.angle].append(location)
        total_asteroids += 1

    if asteroids_max == 'max':
        asteroids_max = total_asteroids

    asteroids_shot = 0
    asteroid_200 = None
    while asteroids_shot < asteroids_max:
        for angle, locations in grouped_by_angle.items():
            asteroids_shot += 1
            last_asteroid_shot = locations[0].asteroid
            viz.draw_line((station.xy, last_asteroid_shot.xy), COLORS[1], 2)
            viz.draw_point(last_asteroid_shot.xy, Color(R=255, G=0, B=0), 4)
            if asteroids_shot == asteroids_max:
                asteroid_200 = last_asteroid_shot
                break
            grouped_by_angle[angle] = locations[1:]

    viz.draw_point(station.xy, COLORS[0], 10)
    viz.show()
    return asteroid_200


if __name__ == '__main__':
    station = do(load_input(10))

    # Part 1
    # print(f"\nPart 1: {station} with {len(station.visible)} visible asteroids.")

    # Part 2
    # asteroid2 = do_part_2(station, load_input(10))
    # code = asteroid2.x * 100 + asteroid2.y
    # print(f"200th asteroid shot is: {asteroid2}: {code}")

    # The AgFx Avatar
    do_part_2(station, load_input(10), asteroids_max=277)





