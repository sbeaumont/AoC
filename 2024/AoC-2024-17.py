"""
Solution for Advent of Code challenge 2024

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from math import trunc

class Computer(object):
    def __init__(self, registers, program):
        self.increment_per_instruction = 2
        self.registers = registers
        self.program = program
        self.ptr = 0
        self.output = list()

    def value_of_operand(self, operand):
        match operand:
            case 0 | 1 | 2 | 3: return operand
            case 4: return self.registers['A']
            case 5: return self.registers['B']
            case 6: return self.registers['C']
            case 7: raise ValueError("7 is not a legal operand")

    def execute_opcode(self, opcode, operand) -> int:
        ptr_increment = self.increment_per_instruction
        # print(opcode, operand, self.registers)
        match opcode:
            case 0: self.adv(operand)
            case 1: self.bxl(operand)
            case 2: self.bst(operand)
            case 3: ptr_increment = self.jnz(operand)
            case 4: self.bxc(operand)
            case 5: self.out(operand)
            case 6: self.bdv(operand)
            case 7: self.cdv(operand)
        return ptr_increment


    def adv(self, operand):
        operand = self.value_of_operand(operand)
        self.registers['A'] = trunc(self.registers['A'] / 2**operand)

    def bxl(self, operand):
        self.registers['B'] = self.registers['B'] ^ operand

    def bst(self, operand):
        operand = self.value_of_operand(operand)
        self.registers['B'] = operand % 8

    def jnz(self, operand):
        if self.registers['A'] != 0:
            self.ptr = operand
            return 0
        else:
            return self.increment_per_instruction

    def bxc(self, operand):
        self.registers['B'] = self.registers['B'] ^ self.registers['C']

    def out(self, operand):
        value = self.value_of_operand(operand) % 8
        self.output.append(value)
        # print(value)

    def bdv(self, operand):
        operand = self.value_of_operand(operand)
        self.registers['B'] = int(self.registers['A'] / 2**operand)

    def cdv(self, operand):
        operand = self.value_of_operand(operand)
        self.registers['C'] = int(self.registers['A'] / 2**operand)

    def run(self):
        while self.ptr < len(self.program):
            opcode = self.program[self.ptr]
            operand = self.program[self.ptr + 1]
            inc_ptr = self.execute_opcode(opcode, operand)
            self.ptr += inc_ptr
        return ','.join([str(x) for x in self.output])



def part_1(entries):
    registers, program = entries
    # print(registers)
    # print(program)
    computer = Computer(registers, program)
    return computer.run()


def part_2(entries):
    registers, program = entries
    output = 'WRONG'
    program_txt = ','.join([str(x) for x in program])
    dec_program = int(''.join([str(x) for x in program]), 8)
    # i = 100000000000000
    # i = 89999999990000
    # i = 999999999914000
    # i = 99999997900000
    # i = -1
    i = 90900000100000
    # i = 84600
    halter = 0
    while output != program_txt:
        i += 1
        computer = Computer(registers, program)
        computer.registers['A'] = i
        output = computer.run()
        dec_output = int(''.join(output.split(',')), 8)
        if output.startswith(program_txt[:8]):
            print(i, output, program_txt, len(output), len(program_txt), dec_output, dec_program)
            halter += 1
            if halter == 20:
                i = -1
                break
    return i


def read_puzzle_data(data_file: str):
    with open(data_file) as infile:
        lines = [line.strip() for line in infile.readlines()]
        registers = {
            'A': int(lines[0].split(":")[1].strip()),
            'B': int(lines[1].split(":")[1].strip()),
            'C': int(lines[2].split(":")[1].strip())
        }
        program = [int(x) for x in lines[4].split(":")[1].strip().split(',')]
        return registers, program


assertions = {
    "Test 1": '4,6,3,5,6,3,5,2,1,0',
    "Part 1": None,
    "Test 2": 117440,
    "Part 2": None,
}

overrides = {
    "Test 2": {'data file': "AoC-2024-17-test-input-3.txt",}
}

extra_tests = {
    "Test 1" : (
        ("AoC-2024-17-test-input-2.txt", '3'),
    ),
 }