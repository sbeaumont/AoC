#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 16 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re
from pprint import pprint
from collections import defaultdict

start = time.time()


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


op_dict = dict()

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


with open("AoC-2018-16-input-2.txt") as infile:
    program = ([[int(i) for i in line.strip().split()] for line in infile])

registers = [0, 0, 0, 0]
for line in program:
    registers = op_dict[line[0]](registers, line)

print(registers[0])


print(f"{time.time() - start:.4f} seconds to run.")
