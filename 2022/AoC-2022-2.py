#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"


def part_1(entries):
    base_score = {'X': 1, 'Y': 2, 'Z': 3}
    win = (['A', 'Y'], ['B', 'Z'], ['C', 'X'])
    lose = (['A', 'Z'], ['B', 'X'], ['C', 'Y'])
    total_score = 0
    for e in entries:
        score = base_score[e[1]]
        if e in win:
            score += 6
        elif e in lose:
            score += 0
        else:
            score += 3
        total_score += score
    return total_score


def part_2(entries):
    total_score = 0
    for e in entries:
        match e[1]:
            case 'X':
                lose = {'A': 3, 'B': 1, 'C': 2}
                score = 0 + lose[e[0]]
            case 'Y':
                draw = {'A': 1, 'B': 2, 'C': 3}
                score = 3 + draw[e[0]]
            case 'Z':
                win = {'A': 2, 'B': 3, 'C': 1}
                score = 6 + win[e[0]]
        total_score += score
    return total_score


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        return [line.strip().split(' ') for line in infile.readlines()]


test_result = part_1(read_puzzle_data("2-test"))
print("Test:", test_result)
assert test_result == 15

print("Part 1:", part_1(read_puzzle_data(2)))

test_result = part_2(read_puzzle_data("2-test"))
print("Test:", test_result)
assert test_result == 12

print("Part 2:", part_2(read_puzzle_data(2)))
assert part_2(read_puzzle_data(2)) > 11851

