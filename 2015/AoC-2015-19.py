#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

import re

def part_1(replacements, molecule):
    result = set()
    for frm, to in replacements:
        for match in re.finditer(frm, molecule):
            new_molecule = molecule[:match.span()[0]] + to + molecule[match.span()[1]:]
            result.add(new_molecule)
    return len(result)


def reduce_once(replacements, molecules):
    """Create all possible variants of a single round of reductions"""
    new_molecules = set()
    for molecule in molecules:
        for frm, to in replacements:
            for match in re.finditer(to, molecule):
                new_molecule = molecule[:match.span()[0]] + frm + molecule[match.span()[1]:]
                if ('e' in new_molecule) and (len(new_molecule) > 1):
                    continue
                if new_molecule == 'e':
                    return {'e',}
                new_molecules.add(new_molecule)
    return new_molecules


def part_2(replacements, molecule):
    """Work backward from the molecule, reducing it in a minimum number of steps to 'e'."""
    molecules = {molecule,}
    i = 0
    while 'e' not in molecules:
        i += 1
        molecules = reduce_once(replacements, molecules)
        # Remark 1: Oh what a dirty hack, but it works. I just choose the 1000 shortest results and reiterate with
        # that, assuming the right answer is amongst them. And yes, it was.
        # Remark 2: Works with 100, 50, 10, 1 as well!
        # Remark 3: So it works by just taking the shortest one... okay. That's lucky, there can be failing datasets.
        max_size = 1
        if len(molecules) > max_size:
            molecules = set(sorted(molecules, key=lambda x: len(x))[:max_size])
        # print(i, len(molecules))
        # print(molecules)
    return i

def read_puzzle_data(file_number):
    with open(f"AoC-2015-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
        empty_line_index = lines.index("")
        replacements = [r.split(' => ') for r in lines[:empty_line_index]]
        return replacements, lines[-1]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(*read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    assert test_result == 7

    result_1 = part_1(*read_puzzle_data(puzzle_number))
    print("Part 1:", result_1)
    assert result_1 == 535

    test_result_2 = part_2(*read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 2:", test_result_2)
    assert test_result_2 == 6

    result_2 = part_2(*read_puzzle_data(puzzle_number))
    print("Part 2:", result_2)
    assert result_2 == 212

