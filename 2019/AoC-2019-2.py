#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2019 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2019"

from norvigutils import load_input


def run_program(data):
    instruction_pointer = 0
    halt_and_catch_fire = False
    while not halt_and_catch_fire:
        opcode = data[instruction_pointer]
        assert opcode in (1, 2, 99), "Unknown opcode!"
        if opcode == 99:
            halt_and_catch_fire = True
        else:
            arg_pos_1 = data[instruction_pointer + 1]
            arg_pos_2 = data[instruction_pointer + 2]
            write_pos = data[instruction_pointer + 3]
            if opcode == 1:
                data[write_pos] = data[arg_pos_1] + data[arg_pos_2]
            elif opcode == 2:
                data[write_pos] = data[arg_pos_1] * data[arg_pos_2]
        instruction_pointer += 4

    return data


def init_program(noun, verb):
    data = [int(x) for x in load_input(2, readlines=False).split(',')]
    data[1] = noun
    data[2] = verb
    return data


if __name__ == '__main__':
    assert run_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_program([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    # Part 1
    data = run_program(init_program(12, 2))
    print("The value of position 0 is", data[0])
    assert data[0] == 3409710

    # Part 2
    REQUIRED_OUTPUT = 19690720

    for noun in range(0, 100):
        for verb in range(0, 100):
            data = run_program(init_program(noun, verb))
            if data[0] == REQUIRED_OUTPUT:
                print("The noun", noun, "and the verb", verb, "lead to output", REQUIRED_OUTPUT)
                print("Part 2:", noun * 100 + verb)
