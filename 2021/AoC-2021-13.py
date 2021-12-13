#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"


def fold(points, _fold):
    new_points = set()
    axis, n = _fold
    for point in points:
        x, y = point
        if axis == 'x':
            if x > n:
                x = x - (2 * (x - n))
        else:
            if y > n:
                y = y - (2 * (y - n))
        new_points.add((x, y))
    return new_points


def print_points(points):
    x_s, y_s = zip(*points)
    for i in range(max(y_s) + 1):
        line = [' '] * (max(x_s) + 1)
        for point in points:
            x, y = point
            if i == y:
                line[x] = '#'
        print(''.join(line))


def part_1(points_and_folds):
    points = set([tuple(xy) for xy in points_and_folds[0]])
    folds = points_and_folds[1]

    return len(fold(points, folds[0]))


def part_2(points_and_folds):
    points = set([tuple(xy) for xy in points_and_folds[0]])
    folds = points_and_folds[1]

    for f in folds:
        points = fold(points, f)

    print_points(points)


def read_puzzle_data(file_number):
    folds = list()
    lines = list()
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        for line in infile.readlines():
            if line.startswith('fold along'):
                fold_line = line.strip().split(' ')[-1].split('=')
                folds.append((fold_line[0], int(fold_line[1])))
            elif line.strip() != '':
                lines.append([int(c) for c in line.strip().split(',')])
    return lines, folds


if __name__ == '__main__':
    DAY = "13"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 17

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    print("\nTest Part 2:\n")
    part_2(read_puzzle_data(f"{DAY}-test"))

    print("\nPart 2:\n")
    part_2(read_puzzle_data(DAY))
