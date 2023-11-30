#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"


from collections import defaultdict
import re


def create_stacks(stack_lines):
    stacks = defaultdict(list)
    for line in reversed(stack_lines):
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                stack_nr = (i // 4) + 1
                stacks[stack_nr].append(line[i])
    return stacks

def top_crates(stacks):
    return ''.join([stacks[i].pop() for i in range(1, len(stacks.keys()) + 1)])

def part_1(stack_lines, command_lines):
    stacks = create_stacks(stack_lines)
    for line in command_lines:
        command_match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        nr_moves = int(command_match.group(1))
        move_from = int(command_match.group(2))
        move_to = int(command_match.group(3))
        for i in range(nr_moves):
            stacks[move_to].append(stacks[move_from].pop())
    return top_crates(stacks)


def part_2(stack_lines, command_lines):
    stacks = create_stacks(stack_lines)
    for line in command_lines:
        command_match = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        nr_moves = int(command_match.group(1))
        move_from = int(command_match.group(2))
        move_to = int(command_match.group(3))
        moving_stack = list()
        for i in range(nr_moves):
            moving_stack.append(stacks[move_from].pop())
        for i in range(nr_moves):
            stacks[move_to].append(moving_stack.pop())
    return top_crates(stacks)


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.rstrip() for line in infile.readlines()]

    for i, line in enumerate(lines):
        if line.startswith(' 1'):
            return lines[:i], lines[i+2:]
    return None


if __name__ == '__main__':
    DAY = "5"

    test_result_part_1 = part_1(*read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 'CMZ'

    print("     Part 1:", part_1(*read_puzzle_data(DAY)))

    test_result_part_2 = part_2(*read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 'MCD'

    result_part_2 = part_2(*read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    # assert result_part_2 == 0