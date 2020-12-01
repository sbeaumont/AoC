#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 21 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time

start = time.time()

with open("AoC-2018-21-input.txt") as infile:
    program = ([line.strip().split(' ') for line in infile])

ip_register = int(program[0][1])
program = [(line[0], int(line[1]), int(line[2]), int(line[3])) for line in program[1:]]


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


def do(rng, max_instr_count, program):
    lowest_instruction_count = 999999999999
    for reg_0 in rng:
        instruction_count = 0
        registers = [reg_0, 0, 0, 0, 0, 0]
        ip = 0
        broken = False
        while 0 <= ip < len(program):
            registers[ip_register] = ip
            registers = globals()[program[ip][0]](registers, program[ip])
            print(ip, program[ip], registers)
            ip = registers[ip_register] + 1
            instruction_count += 1
            if instruction_count > max_instr_count:
                if reg_0 % 10000 == 0:
                    print(f"Breaking after {instruction_count} with r[0] = {reg_0}")
                broken = True
                break
        if not broken:
            if instruction_count < lowest_instruction_count:
                lowest_instruction_count = instruction_count
                print(f"With {reg_0} we halted after {instruction_count} instructions.")


if __name__ == '__main__':
    do(range(1), 100, program)

print(f"{time.time() - start:.4f} seconds to run.")

# 10 is wrong
