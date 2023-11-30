#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"

import numpy as np
import time

def rotate_left(a, nr=1):
    return np.rot90(a, k=nr, axes=(0, 1))

def rotate_right(a, nr=1):
    return np.rot90(a, k=nr, axes=(1, 0))

def sweep(a):
    result = np.ones(a.shape)
    for row_nr in range(a.shape[0]):
        highest_tree = a[row_nr, 0]
        for column_nr in range(1, a.shape[1]):
            current_tree = a[row_nr, column_nr]
            if current_tree <= highest_tree:
                result[row_nr, column_nr] = 0
            else:
                highest_tree = current_tree
    return result


def part_1(entries):
    forest = np.array(entries)
    left = sweep(forest)
    top = rotate_right(sweep(rotate_left(forest)))
    right = rotate_right(sweep(rotate_left(forest, 2)), 2)
    bottom = rotate_left(sweep(rotate_right(forest)))

    visible_trees = 0
    for y in range(forest.shape[0]):
        for x in range(forest.shape[1]):
            if left[y, x] or top[y, x] or right[y, x] or bottom[y, x]:
                visible_trees += 1

    # print(forest[:,2])
    return visible_trees


def view_sweep(a):
    vision = np.zeros(a.shape, dtype=int)
    for row_nr in range(a.shape[0]):
        for column_nr in range(1, a.shape[1]):
            current_tree_h = a[row_nr, column_nr]
            vision[row_nr, column_nr] = 1
            dx = 1
            left_tree_h = a[row_nr, column_nr - dx]
            left_tree_v = 1
            while (current_tree_h > left_tree_h) and left_tree_v > 0:
                left_tree_v = vision[row_nr, column_nr - dx]
                vision[row_nr, column_nr] += left_tree_v
                dx += left_tree_v
                left_tree_h = a[row_nr, column_nr - dx]
    return vision

def part_2(entries):
    forest = np.array(entries)
    # print(view_sweep(forest))
    left = view_sweep(forest)
    top = rotate_right(view_sweep(rotate_left(forest)))
    right = rotate_right(view_sweep(rotate_left(forest, 2)), 2)
    bottom = rotate_left(view_sweep(rotate_right(forest)))

    max_scenic_score = 0
    for y in range(forest.shape[0]):
        for x in range(forest.shape[1]):
            scenic_score = left[y, x] * top[y, x] * right[y, x] * bottom[y, x]
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return max_scenic_score


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [[int(n) for n in line.strip()] for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    st = time.time()

    DAY = "8"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 21

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 8

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 595080

    et = time.time()
    print(f"Execution time: {et - st} seconds")