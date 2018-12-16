#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 16 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re

start = time.time()

with open("AoC-2018-16-input-1.txt") as infile:
    data = ([line.strip() for line in infile])

operations = []


def addr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] + reg_in[opcode[2]]
    return reg_out


def addi(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] + opcode[2]
    return reg_out


def mulr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] * reg_in[opcode[2]]
    return reg_out


def muli(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] * opcode[2]
    return reg_out


def banr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] & reg_in[opcode[2]]
    return reg_out


def bani(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] & opcode[2]
    return reg_out


def borr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] | reg_in[opcode[2]]
    return reg_out


def bori(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]] | opcode[2]
    return reg_out


def setr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = reg_in[opcode[1]]
    return reg_out


def seti(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = opcode[1]
    return reg_out


def gtir(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = 1 if opcode[1] > reg_in[opcode[2]] else 0
    return reg_out


def gtri(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = 1 if reg_in[opcode[1]] > opcode[2] else 0
    return reg_out


def gtrr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = 1 if reg_in[opcode[1]] > reg_in[opcode[2]] else 0
    return reg_out


def eqir(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = 1 if opcode[1] == reg_in[opcode[2]] else 0
    return reg_out


def eqri(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = 1 if reg_in[opcode[1]] == opcode[2] else 0
    return reg_out


def eqrr(reg_in, opcode):
    reg_out = reg_in[:]
    reg_out[opcode[3]] = 1 if reg_in[opcode[1]] == reg_in[opcode[2]] else 0
    return reg_out


operations.append(addr)
operations.append(addi)
operations.append(mulr)
operations.append(muli)
operations.append(banr)
operations.append(bani)
operations.append(borr)
operations.append(bori)
operations.append(setr)
operations.append(seti)
operations.append(gtir)
operations.append(gtri)
operations.append(gtrr)
operations.append(eqir)
operations.append(eqri)
operations.append(eqrr)

line_regex = re.compile(".*\[(\d+, \d+, \d+, \d+)\]")

num_opcodes = 0
more_than_three_matches = 0
for i in range(0, len(data), 4):
    before = [int(j) for j in line_regex.search(data[i]).group(1).split(",")]
    opcode = [int(j) for j in data[i+1].split(" ")]
    after = [int(j) for j in line_regex.search(data[i + 2]).group(1).split(",")]
    #print(before, opcode, after)
    num_opcodes += 1

    op_match = 0
    for op in operations:
        if op(before, opcode) == after:
            op_match += 1
            if op_match >= 3:
                more_than_three_matches += 1
                break

print(f"Total opcodes: {num_opcodes}")
print(f"Number of opcodes with 3 or more matches: {more_than_three_matches}")



print(f"{time.time() - start:.4f} seconds to run.")
