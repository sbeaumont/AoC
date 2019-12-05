#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 5 part 2"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import load_input


def p_mode(opcode, pos):
    if len(opcode) == 1:
        return 0
    else:
        modes = opcode[:-2][::-1]
        return modes[pos] if pos < len(modes) else 0


def run_program(data, input_value):

    last_output = None

    def val_or_pos(n, mode):
        if int(mode):
            return n
        else:
            return data[n]

    def read_par(nr):
        return val_or_pos(data[instruction_pointer + nr], p_mode(opcode, nr - 1))

    instruction_pointer = 0
    halt_and_catch_fire = False
    while not halt_and_catch_fire:
        opcode = str(data[instruction_pointer])
        instruction = int(opcode) if len(opcode) == 1 else int(opcode[-2:])

        if instruction == 99:
            halt_and_catch_fire = True
        elif instruction in (1, 2):
            write_pos = data[instruction_pointer + 3]
            par1 = read_par(1)
            par2 = read_par(2)
            if instruction == 1:
                data[write_pos] = par1 + par2
            elif instruction == 2:
                data[write_pos] = par1 * par2
            instruction_pointer += 4
        elif instruction == 3:
            par1 = data[instruction_pointer + 1]
            data[par1] = input_value
            instruction_pointer += 2
        elif instruction == 4:
            par1 = data[instruction_pointer + 1]
            last_output = data[par1]
            instruction_pointer += 2
        elif instruction in (5, 6):
            par1 = read_par(1)
            par2 = read_par(2)
            if (instruction == 5) and (par1 != 0):
                instruction_pointer = par2
            elif (instruction == 6) and (par1 == 0):
                instruction_pointer = par2
            else:
                instruction_pointer += 3
        elif instruction in (7, 8):
            write_pos = data[instruction_pointer + 3]
            par1 = read_par(1)
            par2 = read_par(2)
            if (instruction == 7) and (par1 < par2):
                data[write_pos] = 1
            elif (instruction == 8) and (par1 == par2):
                data[write_pos] = 1
            else:
                data[write_pos] = 0
            instruction_pointer += 4
        else:
            assert False, f"Unknown instruction: {instruction} in opcode {opcode}"

    return last_output


def init_program():
    return [int(x) for x in load_input(5, readlines=False).split(',')]


if __name__ == '__main__':
    diagnostic_code_1 = run_program(init_program(), 1)
    assert diagnostic_code_1 == 11049715

    diagnostic_code_2 = run_program(init_program(), 5)
    assert diagnostic_code_2 == 2140710

    print("Part 1:", diagnostic_code_1)
    print("Part 2:", diagnostic_code_2)

