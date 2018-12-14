#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from collections import deque

FIRST_RECIPES = 37
PUZZLE_INPUT = 505961


def do(search_pattern):
    start = time.time()
    search_deque = deque([int(i) for i in str(search_pattern)])
    recipes = deque([int(i) for i in str(FIRST_RECIPES)])
    tail = deque(recipes, (len(search_deque)))
    elf_one = 0
    elf_two = 1
    while tail != search_deque:
        nr_one = recipes[elf_one]
        nr_two = recipes[elf_two]
        new_recipes = nr_one + nr_two
        if new_recipes >= 10:
            recipes.append(new_recipes // 10)
            tail.append(new_recipes // 10)
        recipes.append(new_recipes % 10)
        tail.append(new_recipes % 10)
        elf_one = (elf_one + 1 + nr_one) % len(recipes)
        elf_two = (elf_two + 1 + nr_two) % len(recipes)
        #print(tail)
    answer = len(recipes) - len(str(search_pattern))
    print(f"{search_pattern} appears after {answer} recipes. {time.time() - start:.4f} seconds to run.")
    return answer


assert do('01245') == 5
assert do(51589) == 9
assert do(92510) == 18
assert do(59414) == 2018
#do(PUZZLE_INPUT)








