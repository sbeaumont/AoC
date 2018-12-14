#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time


start = time.time()

FIRST_RECIPES = 37
PUZZLE_INPUT = 505961

recipes = [int(i) for i in str(FIRST_RECIPES)]

print(recipes)

elf_one = 0
elf_two = 1
while len(recipes) < PUZZLE_INPUT + 10:
    new_digits = [int(i) for i in str(recipes[elf_one] + recipes[elf_two])]
    recipes.extend(new_digits)
    elf_one = (elf_one + 1 + recipes[elf_one]) % len(recipes)
    elf_two = (elf_two + 1 + recipes[elf_two]) % len(recipes)

answer = ''.join([str(i) for i in recipes[-10:]])

print(f"Next ten recipes are: {answer}")

print(f"{time.time() - start:.4f} seconds to run.")

assert answer != '5565666151'
assert answer != '5109181146'





