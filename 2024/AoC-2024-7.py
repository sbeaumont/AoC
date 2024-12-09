#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

from itertools import product


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


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 3749,
    "Part 1": 882304362421,
    "Test 2": 11387,
    "Part 2": 145149066755184
}
