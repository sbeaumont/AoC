#!/usr/bin/env python3

"""Based on Day 5 part 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from collections import defaultdict


def p_mode(opcode, pos):
    if len(opcode) == 1:
        return 0
    else:
        modes = opcode[:-2][::-1]
        return int(modes[pos]) if pos < len(modes) else 0


class Computer(object):
    def __init__(self, program, setting=None, pause_on_output=False, debug=False):
        self.program = defaultdict(int)
        self.init_program(program)
        if setting is not None:
            self.input = [setting]
        else:
            self.input = []
        self.input_ptr = 0
        self.output = list()
        self.pause_on_output = pause_on_output
        self.i_ptr = 0
        self.r_base = 0
        self.halted = False
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
        data = self.program
        self.input.extend(input_values)

        def read_par(nr):
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

            if instruction == 99:
                self.halted = True
                self.catch_fire()
            elif instruction in (1, 2):
                par1 = read_par(1)
                par2 = read_par(2)
                if instruction == 1:
                    write(3, par1 + par2)
                elif instruction == 2:
                    write(3, par1 * par2)
                self.i_ptr += 4
            elif instruction == 3:
                write(1, self.read_input_value())
                self.i_ptr += 2
            elif instruction == 4:
                par1 = read_par(1)
                self.output.append(par1)
                self.i_ptr += 2
                if self.pause_on_output:
                    return self.output[-1]
            elif instruction in (5, 6):
                # Move pointer based on equal / not-equal zero
                par1 = read_par(1)
                par2 = read_par(2)
                if (instruction == 5) and (par1 != 0):
                    self.i_ptr = par2
                elif (instruction == 6) and (par1 == 0):
                    self.i_ptr = par2
                else:
                    self.i_ptr += 3
            elif instruction in (7, 8):
                par1 = read_par(1)
                par2 = read_par(2)
                if (instruction == 7) and (par1 < par2):
                    write(3, 1)
                elif (instruction == 8) and (par1 == par2):
                    write(3, 1)
                else:
                    write(3, 0)
                self.i_ptr += 4
            elif instruction == 9:
                par1 = read_par(1)
                self.r_base += par1
                self.i_ptr += 2
            else:
                assert False, f"Unknown instruction: {instruction} in opcode {opcode}"

        return self.last_output()
