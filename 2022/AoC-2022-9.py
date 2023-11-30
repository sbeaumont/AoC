#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2022 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2022"

from numpy import sign
from pprint import pprint

def visualize(visited):
    minx = miny = maxx = maxy = 0
    for v in visited:
        minx = minx if minx <= v[0] else v[0]
        miny = miny if miny <= v[1] else v[1]
        maxx = maxx if maxx >= v[0] else v[0]
        maxy = maxy if maxy >= v[1] else v[1]

    graph = list()
    for y in range(maxy, miny - 1, -1):
        graph.append(['#' if (x, y) in visited else '.' for x in range(minx, maxx + 1)])
    for line in graph:
        print([''.join(line)])
    # pprint(graph)


def follow(leader, follower):
    dx = leader[0] - follower[0]
    dy = leader[1] - follower[1]
    if abs(dx) > 1 or abs(dy) > 1:
        follower = (follower[0] + sign(dx), follower[1] + sign(dy))
    return follower


def part_1(entries):
    visited = set()
    visited.add((0, 0))
    head = (0, 0)
    tail = (0, 0)
    for motion in [e.split() for e in entries]:
        direction = motion[0]
        steps = int(motion[1])
        for i in range(steps):
            match direction:
                case 'R': head = (head[0] + 1, head[1])
                case 'L': head = (head[0] - 1, head[1])
                case 'U': head = (head[0], head[1] + 1)
                case 'D': head = (head[0], head[1] - 1)
            tail = follow(head, tail)
            visited.add(tail)
    visualize(visited)
    return len(visited)


def part_2(entries):
    rope = [(0, 0), ] * 10
    visited = set()
    visited.add((0, 0))
    for motion in [e.split() for e in entries]:
        direction = motion[0]
        steps = int(motion[1])
        for i in range(steps):
            match direction:
                case 'R': rope[0] = (rope[0][0] + 1, rope[0][1])
                case 'L': rope[0] = (rope[0][0] - 1, rope[0][1])
                case 'U': rope[0] = (rope[0][0], rope[0][1] + 1)
                case 'D': rope[0] = (rope[0][0], rope[0][1] - 1)
            for j in range(len(rope) - 1):
                rope[j+1] = follow(rope[j], rope[j+1])
            visited.add(rope[-1])
    return len(visited)


def read_puzzle_data(file_number):
    with open(f"AoC-2022-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "9"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 13

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 1

    test_result_part_2_2 = part_2(read_puzzle_data(f"{DAY}-test-2"))
    print("Test Part 2.2:", test_result_part_2_2)
    assert test_result_part_2_2 == 36

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    # assert result_part_2 == 0