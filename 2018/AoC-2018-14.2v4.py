#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time

FIRST_RECIPES = [3, 7]
PUZZLE_INPUT = [5, 0, 5, 9, 6, 1]


def do(search_pattern):
    start = time.time()
    recipes = FIRST_RECIPES[:]
    tail_length = len(search_pattern)

    def add_digit(d):
        result = False
        recipes.append(d)
        if recipes[-tail_length:] == search_pattern:
            result = True
            answer = len(recipes[:-tail_length])
            print(f"The sequence {recipes[-tail_length:]} appears after {answer} recipes, {time.time() - start:.4f} seconds to run.")
        return result

    elf_one = 0
    elf_two = 1
    found = False
    while not found:
        new_digits = recipes[elf_one] + recipes[elf_two]
        if new_digits < 10:
            found = add_digit(new_digits)
        else:
            found = add_digit(new_digits // 10)
            if not found:
                found = add_digit(new_digits % 10)
        elf_one = (elf_one + 1 + recipes[elf_one]) % len(recipes)
        elf_two = (elf_two + 1 + recipes[elf_two]) % len(recipes)
        # if len(recipes) > 270157146:
        #     print("Eerrrrt")
        #     break

    return len(recipes[:-tail_length])


if __name__ == '__main__':
    assert do([0, 1, 2, 4, 5]) == 5
    assert do([5, 1, 5, 8, 9]) == 9
    assert do([9, 2, 5, 1, 0]) == 18
    assert do([5, 9, 4, 1, 4]) == 2018
    result = do(PUZZLE_INPUT)
    assert result < 270157146