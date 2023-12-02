#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import operator
import functools


def draw_sets(entries: list[str]) -> dict[list]:
    games = dict()
    for e in entries:
        game, draws = e.split(':', 1)
        game_nr = int(game[5:])
        cube_sets = list()
        for draw in draws.split(';'):
            cube_sets.extend([s.strip() for s in draw.split(',')])
        games[game_nr] = cube_sets
    return games


def part_1(entries: list[str]):
    max_cubes = {'red': 12, 'green': 13, 'blue': 14}

    result = 0
    games = draw_sets(entries)
    for game_nr, cube_sets in games.items():
        valid_game = True
        for cube_set in cube_sets:
            amount, color = cube_set.split(' ')
            if max_cubes[color] < int(amount):
                valid_game = False
                break
        if valid_game:
            result += game_nr
    return result


def part_2(entries):
    result = 0
    games = draw_sets(entries)
    for cube_sets in games.values():
        color_minimum = {'red': 0, 'green': 0, 'blue': 0}
        for cube_set in cube_sets:
            amount, color = cube_set.split(' ')
            if color_minimum[color] < int(amount):
                color_minimum[color] = int(amount)
        result += functools.reduce(operator.mul, color_minimum.values())
    return result


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "2"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 8

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 2286

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 72227