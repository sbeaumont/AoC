"""
Solution for Advent of Code challenge 2024

1. We can represent this with a (x, y, direction) tuple,
    because we can only compare when we come in from the same direction, except for the End space.
    Example: coming in south vs west, you'll only know the cost to east when you've taken the turn south -> east
    into account. Which means that both paths come in from the same side in the east space, and we can
    compare.
2. Direction is N E S W => 0 1 2 3
3. Compare directions by subtraction:
    abs(0) is cost 1,
    abs(1) and abs(3) are cost 1001,
    abs(2) is backtracking, ignore.
"""
import math


__author__ = "Serge Beaumont"
__date__ = "December 2024"

moves = ((0, -1), (1, 0), (0, 1), (-1, 0))

def init_unvisited(entries):
    unvisited = dict()
    start = end = None
    for y, line in enumerate(entries):
        for x, char in enumerate(line):
            if char in ('S', 'E', '.'):
                unvisited[(x, y)] = math.inf
                if char == 'S':
                    start = (x, y)
                    unvisited[(x, y)] = 0
                elif char == 'E':
                    end = (x, y)
    return unvisited, start, end


def neighbours(xy):
    return [(xy[0] + move[0], xy[1] + move[1]) for move in moves]


def part_1(entries: list[str]):
    unvisited, start, end = init_unvisited(entries)
    frontier = [[(start, 1, 0),],]
    visited = set()
    while unvisited:
        for path in frontier:
            path_front = path[-1]
            front_xy, front_dir, front_weight = path_front
            for direction, nb in enumerate(neighbours(front_xy)):
                if nb in unvisited:
                    cost = 1001 if abs(front_dir - direction) in (1, 3) else 1
                    new_path = list(path + [(nb, front_dir, front_weight)])
                    frontier.append()
        print(frontier)
        print
    return None


def part_2(entries: list[str]):
    for e in entries:
        pass
    return None


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 7036,
    "Part 1": None,
    "Test 2": None,
    "Part 2": None,
}

extra_tests = {
    "Test 1" : (
        ("AoC-2024-16-test-input-2.txt", 11048),
    ),
 }