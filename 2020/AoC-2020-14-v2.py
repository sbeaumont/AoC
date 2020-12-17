#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 13"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from itertools import product


with open("AoC-2020-14-input.txt") as infile:
    program = [line.strip() for line in infile.readlines()]

print(program)


def to_binary(i):
    return [c for c in bin(i)[2:].zfill(36)]


def to_int(bits):
    return int(bits, 2)


def mask_value(mask, value):
    result = list()
    masked_1 = [m if (m == '1') else c for m, c in zip(mask, to_binary(value))]
    if mask.count('X') > 0:
        for bts in product(range(2), repeat=mask.count('X')):
            floating = list()
            i = 0
            for m, c in zip(mask, masked_1):
                if m == 'X':
                    floating.append(str(bts[i]))
                    i += 1
                else:
                    floating.append(c)
            result.append(''.join(floating))
    else:
        result.append(''.join(masked_1))
    return result


memory = dict()
mask = '0' * 36
for line in program:
    if line[:4] == 'mask':
        mask = line.split(' = ')[1]
    else:
        addr, num = line.split(' = ')
        for mem_addr in mask_value(mask, int(addr[4:-1])):
            memory[mem_addr] = int(num)

total = 0
for value in memory.values():
    total += value

print(total)