#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 16 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re
from pprint import pprint
from collections import defaultdict

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

op_dict = {}
op_dict[2] = bori
op_dict[4] = addi
op_dict[13] = mulr
op_dict[1] = muli
op_dict[11] = addr
op_dict[8] = borr
op_dict[14] = seti
op_dict[0] = banr
op_dict[7] = gtir
op_dict[10] = bani
op_dict[3] = setr
op_dict[9] = eqri
op_dict[15] = gtrr
op_dict[12] = eqir
op_dict[6] = gtri
op_dict[5] = eqrr

opcode_matches = defaultdict(set)
opcode_fails = defaultdict(set)
for i in range(0, len(data), 4):
    before = [int(j) for j in line_regex.search(data[i]).group(1).split(",")]
    opcode = [int(j) for j in data[i+1].split(" ")]
    after = [int(j) for j in line_regex.search(data[i + 2]).group(1).split(",")]
    #print(before, opcode, after)

    if opcode[0] not in op_dict:
        op_match = 0
        for op in operations:
            if (op not in op_dict.values()) and (op(before, opcode) == after):
                opcode_matches[opcode[0]].add(op.__name__)

for code, oper in opcode_matches.items():
    print(code, oper)

print()

for code, oper in opcode_fails.items():
    print(code, oper)

print(f"{time.time() - start:.4f} seconds to run.")
