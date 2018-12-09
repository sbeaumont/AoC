#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2017 - Day 17"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

STEPS_PER_INSERTION = 354
printer_buffer = [0]
position = 0

for i in range(2017):
    position = (position + STEPS_PER_INSERTION) % len(printer_buffer)
    printer_buffer = printer_buffer[:position+1] + [i + 1] + printer_buffer[position+1:]
    position += 1

print(f"2017-17 Part 1: {printer_buffer[position + 1]}")
