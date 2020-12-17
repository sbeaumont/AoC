#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"


with open("AoC-2020-14-input.txt") as infile:
    program = [line.strip() for line in infile.readlines()]

print(program)


def to_binary(i):
    return [c for c in bin(i)[2:].zfill(36)]


def to_int(bits):
    return int(bits, 2)


def mask_value(mask, value):
    masked = [m if (m == '0') or (m == '1') else c for m, c in zip(mask, value)]
    return ''.join(masked)


memory = dict()
mask = '0' * 36
for line in program:
    if line[:4] == 'mask':
        mask = line.split(' = ')[1]
    else:
        addr, num = line.split(' = ')
        mem_addr = int(addr.strip()[4:-1])
        memory[mem_addr] = mask_value(mask, to_binary(int(num)))

total = 0
for value in memory.values():
    total += to_int(value)

print(total)