#!/usr/bin/env python

"""Solution for the Advent of Code challenge 2016, day 12."""

__author__ = "Serge Beaumont"
__date__ = "December 2016"

DATA = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 12 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""

# Initialize.
program = DATA.split('\n')

def execute(program, registers):
    execPointer = 0
    while execPointer < len(program):
        parts = program[execPointer].split()
        command = parts[0]
        if command == 'cpy':
            registers[parts[2]] = registers[parts[1]] if parts[1] in registers.keys() else int(parts[1])
            execPointer += 1
        elif command == 'jnz':
            testValue = registers[parts[1]] if parts[1] in registers.keys() else int(parts[1])
            if testValue != 0:
                execPointer += int(parts[2])
            else:
                execPointer += 1
        elif command == 'inc':
            registers[parts[1]] += 1
            execPointer += 1
        elif command == 'dec':
            registers[parts[1]] -= 1
            execPointer += 1

# Execute part 1
registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
execute(program, registers)
print("For part 1 the answer is the value of register a:", registers)

# Reset for part 2: c starts at 1
print("Executing part 2...")
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
execute(program, registers)
print("For part 2 the answer is the value of register a:", registers)
