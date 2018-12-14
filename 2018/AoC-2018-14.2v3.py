#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from collections import deque


start = time.time()

FIRST_RECIPES = '37'
PUZZLE_INPUT = '505961'
PUZZLE_INPUT = '59414'

recipes = FIRST_RECIPES

elf_one = 0
elf_two = 1
while recipes[-5:] != PUZZLE_INPUT:
    new_digits = str(int(recipes[elf_one]) + int(recipes[elf_two]))
    recipes += new_digits
    elf_one = (elf_one + 1 + int(recipes[elf_one])) % len(recipes)
    elf_two = (elf_two + 1 + int(recipes[elf_two])) % len(recipes)
    #print(len(recipes), elf_one, elf_two, new_digits)

answer = len(recipes) - len(PUZZLE_INPUT)

print(f"The sequence appears after {answer} recipes")

print(f"{time.time() - start:.4f} seconds to run.")





