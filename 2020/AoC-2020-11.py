#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 11"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

import numpy as np
from aocutils import neighbors8, X, Y
from collections import Counter

directions = np.array(((1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)))


class Layout(object):
    @classmethod
    def load(cls, filename):
        with open(filename) as infile:
            layout = [[c for c in line.strip()] for line in infile.readlines()]
        return cls(layout)

    def __init__(self, source):
        self.seats = np.array(source)
        self.visible_map = list()
        self.init_visible_map()

    def set_seats(self, source):
        self.seats = np.array(source)

    @property
    def nr_columns(self):
        return self.seats.shape[1]

    @property
    def nr_rows(self):
        return self.seats.shape[0]

    @property
    def occupied_count(self):
        return Counter(self.seats.flatten())['#']

    def in_bounds(self, coords):
        return (0 <= X(coords) < self.nr_columns) and (0 <= Y(coords) < self.nr_rows)

    def neighbours(self, coords):
        return [self.seats[Y(n), X(n)] for n in neighbors8(coords) if self.in_bounds(n)]

    def visible_seat_counts(self, coords):
        return Counter([self.seats[Y(n), X(n)] for n in self.visible_map[Y(coords)][X(coords)]])

    def visible_seats(self, coords):
        result = []
        for d in directions:
            done = False
            distance = 1
            while not done:
                target = coords + (d * distance)
                if self.in_bounds(target):
                    if self.seats[Y(target), X(target)] == '.':
                        distance += 1
                    else:
                        result.append(target)
                        done = True
                else:
                    done = True
        return result

    def init_visible_map(self):
        for y in range(self.nr_rows):
            row = list()
            for x in range(self.nr_columns):
                row.append(self.visible_seats((x, y)))
            self.visible_map.append(row)


def do(filename):
    layout = Layout.load(filename)

    changed = True
    while changed:
        new_layout = []
        changed = False
        for y in range(layout.nr_rows):
            new_row = list()
            for x in range(layout.nr_columns):
                # In numpy axis 0 is the rows, axis 1 is the columns
                counts = Counter(layout.neighbours((x, y)))
                if (layout.seats[y, x] == 'L') and '#' not in counts.keys():
                    new_row.append('#')
                    changed = True
                elif (layout.seats[y, x] == '#') and counts.get('#', 0) >= 4:
                    new_row.append('L')
                    changed = True
                else:
                    new_row.append(layout.seats[y, x])
            new_layout.append(new_row)
        if changed:
            layout.set_seats(new_layout)
    return layout.occupied_count


def do_2(filename):
    layout = Layout.load(filename)

    changed = True
    while changed:
        new_layout = []
        changed = False
        for y in range(layout.nr_rows):
            new_row = list()
            for x in range(layout.nr_columns):
                # In numpy axis 0 is the rows, axis 1 is the columns
                counts = layout.visible_seat_counts((x, y))
                if (layout.seats[y, x] == 'L') and '#' not in counts.keys():
                    new_row.append('#')
                    changed = True
                elif (layout.seats[y, x] == '#') and counts.get('#', 0) >= 5:
                    new_row.append('L')
                    changed = True
                else:
                    new_row.append(layout.seats[y, x])
            new_layout.append(new_row)
        if changed:
            layout.set_seats(new_layout)
    return layout.occupied_count


if __name__ == '__main__':
    test1 = do("AoC-2020-11-test-1.txt")
    print(test1)
    assert test1 == 37

    result1 = do("AoC-2020-11-input.txt")
    print(result1)
    assert result1 == 2368

    test2 = do_2("AoC-2020-11-test-1.txt")
    print(test2)
    assert test2 == 26

    result2 = do_2("AoC-2020-11-input.txt")
    print(result2)
    assert result1 == 2124
