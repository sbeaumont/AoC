#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 8"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from copy import deepcopy

with open(f"AoC-2020-8-input.txt") as infile:
    program_file = [line.strip().split() for line in infile.readlines()]
    for line in program_file:
        line[1] = int(line[1])


def run_program(program):
    visited = list()
    pointer = 0
    accumulator = 0
    while pointer not in visited:
        visited.append(pointer)
        instruction = program[pointer]
        if instruction[0] == 'acc':
            accumulator += instruction[1]
            pointer += 1
        elif instruction[0] == 'nop':
            pointer += 1
        elif instruction[0] == 'jmp':
            pointer += instruction[1]
        else:
            assert False, f"Instruction {instruction} not known"

        if pointer >= len(program):
            return "normal", accumulator

    return 'looped', accumulator


if __name__ == '__main__':
    print("Part 1:", run_program(program_file)[1])

    for i in range(len(program_file)):
        operator = program_file[i][0]
        if operator in ['jmp', 'nop']:
            proggy = deepcopy(program_file)
            proggy[i][0] = 'nop' if operator == 'jmp' else 'jmp'
            result, accumulator = run_program(proggy)
            if result == 'normal':
                print("Part 2:", accumulator)
                break
