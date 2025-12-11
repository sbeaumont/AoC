"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


from math import prod


def parse_problems(entries: list) -> list:
    problems = []
    for i in range(len(entries[0])):
        problem = [line[i] for line in entries]
        operator = problem.pop()
        operands = [int(x) for x in problem]
        operands_str = [x for x in problem]
        problems.append({"operands": operands, "operands_str": operands_str, "operator": operator})
    return problems

def answer_problem(problem: dict) -> int:
    match problem["operator"]:
        case "+":
            answer = sum(problem["operands"])
        case "*":
            answer = prod(problem["operands"])
    return answer


def part_1(entries: list[str]):
    entries = [[x for x in line.strip().split()] for line in entries]
    problems = parse_problems(entries)
    return sum([answer_problem(problem) for problem in problems])


def find_column_indexes(entries: list[str]):
    indexes = list()
    for i in range(len(entries[0])):
        column_chars = [entries[j][i] for j in range(len(entries))]
        if all([c == ' ' for c in column_chars]):
            indexes.append(i)
    indexes.append(len(entries[0])) # So the last problem will also get resolved
    return indexes


def parse_column_problems(entries: list[str]):
    problems = list()
    indexes = find_column_indexes(entries)
    start = 0
    for index in indexes:
        end = index
        column_block = [line[start:end] for line in entries]
        columns_numbers = [int(''.join(column)) for column in zip(*column_block[:-1])]
        column_problem = {
            "operands": columns_numbers,
            "operator": column_block[-1].strip(),
        }
        start = end + 1
        problems.append(column_problem)
    return problems


def part_2(entries: list[str]):
    problems = parse_column_problems(entries)
    return sum([answer_problem(problem) for problem in problems])


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip('\n') for line in infile.readlines()]


assertions = {
    "Test 1": 4277556,
    "Part 1": 4693159084994,
    "Test 2": 3263827,
    "Part 2": 11643736116335,
}
