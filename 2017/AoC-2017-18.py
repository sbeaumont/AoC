#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017 - Day 18"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from collections import defaultdict

start = time.time()

registers = defaultdict(int)


def register_or_value(term):
    if term.lstrip("-").isdigit():
        return int(term)
    else:
        return int(registers[term])


with open("AoC-2017-18-input.txt") as infile:
    program = ([line.strip().split() for line in infile])

last_sound_played = None
instruction_pointer = 0
terminate = False
while (instruction_pointer >= 0) and (instruction_pointer < len(program)):
    instruction = program[instruction_pointer]
    keyword = instruction[0]
    if keyword == 'snd':
        last_sound_played = register_or_value(instruction[1])
        instruction_pointer += 1
    elif keyword == 'set':
        registers[instruction[1]] = register_or_value(instruction[2])
        instruction_pointer += 1
    elif keyword == 'add':
        newval = registers[instruction[1]] + register_or_value(instruction[2])
        registers[instruction[1]] = newval
        instruction_pointer += 1
    elif keyword == 'mul':
        registers[instruction[1]] = registers[instruction[1]] * register_or_value(instruction[2])
        instruction_pointer += 1
    elif keyword == 'mod':
        registers[instruction[1]] = registers[instruction[1]] % register_or_value(instruction[2])
        instruction_pointer += 1
    elif keyword == 'rcv':
        if register_or_value(instruction[1]) != 0:
            print(f"Received value {last_sound_played}")
            break
        instruction_pointer += 1
    elif keyword == 'jgz':
        if register_or_value(instruction[1]) != 0:
            instruction_pointer += register_or_value(instruction[2])
        else:
            instruction_pointer += 1


print(f"{time.time() - start:.4f} seconds to run.")
