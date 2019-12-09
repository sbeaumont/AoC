#!/usr/bin/env python3

"""Intcode Computer used in days 5, 7, 9"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

import os
from collections import defaultdict


def p_mode(opcode, pos):
    if len(opcode) == 1:
        return 0
    else:
        modes = opcode[:-2][::-1]
        return int(modes[pos]) if pos < len(modes) else 0


def load_program_file(filename):
    assert os.path.exists(filename), f"File {filename} does not exist."
    with open(filename) as f:
        return [int(x) for x in f.read().strip().split(',')]


class Computer(object):
    @classmethod
    def from_file(cls, file_name, setting=None, pause_on_output=False, debug=False):
        return cls(load_program_file(file_name), setting, pause_on_output, debug)

    def __init__(self, program: list, setting=None, pause_on_output=False, debug=False):
        assert all(isinstance(item, int) for item in program), "Expected program to be a list of int"
        # Initialize the program instructions
        self.program = defaultdict(int)
        self.init_program(program)
        # Input and output
        self.input = [setting] if setting is not None else []
        self.input_ptr = 0
        self.output = list()
        # Instruction pointers
        self.i_ptr = 0
        self.r_base = 0
        # Halt flags
        self.halted = False
        self.pause_on_output = pause_on_output
        # Debugging and catching fire
        self.on_fire = False
        self.debug = debug

    def init_program(self, program):
        for i, instruction in enumerate(program):
            self.program[i] = instruction

    def catch_fire(self):
        self.on_fire = True

    def read_input_value(self):
        result = self.input[self.input_ptr]
        self.input_ptr += 1
        return result

    def last_output(self):
        return self.output[-1]

    def run_program(self, input_values: list):
        assert isinstance(input_values, list), f"Expected input_values to be a list, but {input_values} is type {type(input_values).__name__}"
        data = self.program
        self.input.extend(input_values)

        def read(nr):
            """Read parameter based on mode"""
            mode = int(p_mode(opcode, nr - 1))
            n = self.i_ptr + nr
            if mode == 1:
                # Direct parameter
                return data[n]
            elif mode == 2:
                # Relative parameter
                return data[self.r_base + data[n]]
            else:
                # Positional parameter
                return data[data[n]]

        def write(par_nr, value):
            """Write to the location given in the parameter"""
            mode = int(p_mode(opcode, par_nr - 1))
            write_par = data[self.i_ptr + par_nr]
            pos = self.r_base + write_par if mode == 2 else write_par
            data[pos] = value

        while not self.halted:
            opcode = str(data[self.i_ptr])
            instruction = int(opcode) if len(opcode) == 1 else int(opcode[-2:])
            if self.debug:
                print(instruction)

            if instruction == 1:
                # Addition P1 + P2 => P3
                write(3, read(1) + read(2))
                self.i_ptr += 4

            elif instruction == 2:
                # Multiply P1 * P2 => P3
                write(3, read(1) * read(2))
                self.i_ptr += 4

            elif instruction == 3:
                # Read from input
                write(1, self.read_input_value())
                self.i_ptr += 2

            elif instruction == 4:
                # Write to output
                self.output.append(read(1))
                self.i_ptr += 2
                if self.pause_on_output:
                    return self.last_output()

            elif instruction == 5:
                # Jump to P2 if P1 != 0
                self.i_ptr = read(2) if read(1) != 0 else self.i_ptr + 3

            elif instruction == 6:
                # Jump to P2 if P1 == 0
                self.i_ptr = read(2) if read(1) == 0 else self.i_ptr + 3

            elif instruction == 7:
                # Test P1 < P2
                write(3, 1 if read(1) < read(2) else 0)
                self.i_ptr += 4

            elif instruction == 8:
                # Test P1 == P2
                write(3, 1 if read(1) == read(2) else 0)
                self.i_ptr += 4

            elif instruction == 9:
                # Change relative addressing base
                self.r_base += read(1)
                self.i_ptr += 2

            elif instruction == 99:
                # Halt
                self.halted = True
                self.catch_fire()

            else:
                assert False, f"Unknown instruction: {instruction} in opcode {opcode}"

        return self.last_output()
