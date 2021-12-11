#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

MAPPING = {')': '(', ']': '[', '}': '{', '>': '<'}
SYNTAX_SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
AUTOCOMPLETE_SCORE = {'(': 1, '[': 2, '{': 3, '<': 4}


def check_line(line):
    stack = list()
    for c in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        else:
            if MAPPING[c] == stack[-1]:
                stack.pop()
            else:
                return SYNTAX_SCORE[c]
    return 0


def complete_line(line):
    stack = list()
    for c in line:
        if c in ('(', '[', '{', '<'):
            stack.append(c)
        else:
            stack.pop()
    score = 0
    stack.reverse()
    for c in stack:
        score = (score * 5) + AUTOCOMPLETE_SCORE[c]
    return score


def part_1(entries):
    score = 0
    for entry in entries:
        score += check_line(entry)
    return score


def part_2(entries):
    scores = list()
    for entry in entries:
        if check_line(entry) == 0:
            scores.append(complete_line(entry))
    return sorted(scores)[len(scores) // 2]


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "10"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 26397

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 288957

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
