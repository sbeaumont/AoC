#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from itertools import product

from norvigutils import trace


def parse_line(line):
    answer, parameters = line.split(':')
    answer = int(answer)
    parameters = [int(p) for p in parameters.split()]
    return answer, parameters


def part_1(entries: list[str], trace=False):
    total = 0
    for e in entries:
        answer, parameters = parse_line(e)
        # print(list(product(('+', '*'), repeat=len(parameters) - 1)))
        for operators in product(('+', '*'), repeat=len(parameters) - 1):
            if trace:
                print_stack = [str(parameters[0]),]
            cur_value = parameters[0]
            for i in range(len(operators)):
                if trace:
                    print_stack.append(operators[i])
                    print_stack.append(str(parameters[i+1]))
                if operators[i] == '+':
                    cur_value += parameters[i+1]
                elif operators[i] == '*':
                    cur_value *= parameters[i+1]
            if cur_value == answer:
                if trace:
                    print(f"{answer}={''.join(print_stack)}")
                total += cur_value
                break
    return total


def part_2(entries: list[str], trace=False):
    total = 0
    print_stack = []
    for e in entries:
        answer, parameters = parse_line(e)
        # print(list(product(('+', '*', '||'), repeat=len(parameters) - 1)))
        for operators in product(('+', '*', '||'), repeat=len(parameters) - 1):
            if trace:
                print_stack = [str(parameters[0]),]
            cur_value = parameters[0]
            for i in range(len(operators)):
                if trace:
                    print_stack.append(operators[i])
                    print_stack.append(str(parameters[i+1]))
                if operators[i] == '+':
                    cur_value += parameters[i+1]
                elif operators[i] == '*':
                    cur_value *= parameters[i + 1]
                elif operators[i] == '||':
                    cur_value = int(str(cur_value) + str(parameters[i + 1]))
            if cur_value == answer:
                if trace:
                    print(f"{answer}={''.join(print_stack)}")
                total += cur_value
                break
    return total


def read_puzzle_data(file_number):
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"), trace=True)
    print("Test 1:", test_result)
    assert test_result == 3749

    print("Part 1:", part_1(read_puzzle_data(puzzle_number)))

    test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test"), trace=True)
    print("Test 2:", test_result_2)
    assert test_result_2 == 11387

    print("Part 2:", part_2(read_puzzle_data(puzzle_number), trace=True))
