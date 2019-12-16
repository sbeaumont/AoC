#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 12"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

import re
from collections import defaultdict


class Body(object):
    def __init__(self, x, y, z):
        self.pos = [int(x), int(y), int(z)]
        self.v = [0, 0, 0]

    @property
    def x(self):
        return self.pos[0]

    @property
    def y(self):
        return self.pos[1]

    @property
    def z(self):
        return self.pos[2]

    def move(self):
        # Best performance?
        self.pos[0] += self.v[0]
        self.pos[1] += self.v[1]
        self.pos[2] += self.v[2]

    @property
    def token(self):
        return tuple(self.pos), tuple(self.v)

    @property
    def energy(self):
        pot_energy = abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        kin_energy = abs(self.v[0]) + abs(self.v[1]) + abs(self.v[2])
        return pot_energy * kin_energy

    def __repr__(self):
        return f'Body({self.x}, {self.y}, {self.z})'


def load_input(filename):
    with open(filename) as infile:
        p = re.compile(r'x=(-?\d+), y=(-?\d+), z=(-?\d+)')
        return [Body(*p.search(line).group(1, 2, 3)) for line in infile.readlines()]


def do(data):
    for i in range(1000):
        determine_v(data)
        move_all(data)
    return data


def determine_v(data):
    for a in range(3):
        v_for_axis(data, a)
    # for b in data:
    #     print(b, b.v)


def move_all(data):
    for b in data:
        b.move()


def v_for_axis(data, axis):
    by_axis = sorted(data, key=lambda b: b.pos[axis])
    i_min = i_max = 0
    while i_max < len(by_axis):
        current_x = by_axis[i_min].pos[axis]
        i_max += 1
        while (i_max < len(by_axis)) and (by_axis[i_max].pos[axis] == current_x):
            i_max += 1
        for j in range(i_min, i_max):
            pull_negative = len(by_axis[0:i_min])
            pull_positive = len(by_axis[i_max:])
            by_axis[j].v[axis] += pull_positive - pull_negative
        i_min = i_max
    return data


def do_2(data):
    def save_state():
        return [bd.token for bd in data]

    steps = -1
    prev_states = defaultdict(list)
    found_prev = False
    while not found_prev and steps < 100:
        steps += 1
        determine_v(data)
        move_all(data)
        energy = sum([b.energy for b in data])
        if energy in prev_states:
            current_save = save_state()
            for state in prev_states[energy]:
                if current_save == state:
                    found_prev = True
                    print(f"Found prev state {energy} at {steps} steps")
                    for b in data:
                        print(b, b.v)
        prev_states[energy].append(save_state())
        print([(bp, bp.v) for bp in data])
        if steps % 100 == 0:
            print(steps)
    return steps


if __name__ == '__main__':
    # Run tests
    # test('testdata', 'testdata')

    # Check data
    print(f"Input data: {load_input('AoC-2019-input-12.txt')}\n")

    # Solve puzzle
    result = do(load_input('AoC-2019-input-12.txt'))
    for b in result:
        print(b, b.v, b.energy)
    total_energy = sum([b.energy for b in result])

    # Output
    print(f"Part 1: {total_energy}")
    assert total_energy == 7687

    test_result = do_2(load_input('AoC-2019-test-12-1.txt'))
    assert test_result == 2772, f"Expected 2772 but got {test_result}"

    # Solve puzzle
    print("Part 2", do_2(load_input('AoC-2019-input-12.txt')))
