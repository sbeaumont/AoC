#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 15"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from aocutils2021 import Matrix
from networkx import DiGraph, shortest_path
from heapq import heapify
from math import inf


def part_1(entries):
    m = Matrix(entries)
    g = DiGraph()
    g.add_node((0, 0), cost=0)
    for y in range(m.height):
        for x in range(m.width):
            for c in m.neighbors4((x, y)):
                g.add_edge((x, y), c, weight=m[c])
    p = shortest_path(g, (0, 0), (m.width-1, m.height-1), weight='weight')
    total_weight = 0
    for i in range(len(p) - 1):
        total_weight += g.edges[p[i], p[i + 1]]['weight']
    return total_weight


def part_2(entries):
    def entire_cave(original):
        large_matrix = list()
        for row in original:
            large_row = list()
            for i in range(5):
                large_row.extend(row)
                row = [(e + 1) % 9 for e in row]
            large_matrix.append(large_row)
        return large_matrix

    return part_1(entire_cave(entries))


# def part_1_b(entries):
#     cave = Matrix(entries)
#     visited = {(0, 0): [0, (0, 0)], }
#     prio_q = heapify([(0, (0, 0)), ])
#     current = (0, 0)
#
#     for n in cave.neighbours4(current):
#         weight = visited[n]
#
#     return None

# def part_1_b(entries):
#     m = Matrix(entries)
#     costs = list()
#     for line in entries:
#         cost_line = list()
#         costs.append(cost_line)
#         for c in line:
#             cost_line.append(99999)
#     costs[0][0] = 0
#     m[(0, 0)] = 0
#     for y in range(m.height):
#         for x in range(m.width):
#             if (x, y) == (0, 0):
#                 costs[y][x] = 0
#             else:
#                 costs[y][x] = min([costs[c[1]][c[0]] for c in m.neighbors4((x, y))]) + m[(x, y)]
#
#     return costs[-1][-1]


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return [[int(c) for c in line] for line in lines]


if __name__ == '__main__':
    DAY = "15"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 40

    result_part_1 = part_1(read_puzzle_data(DAY))
    print("     Part 1:", result_part_1)
    assert result_part_1 == 656

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 315
    #
    # print("     Part 2:", part_2(read_puzzle_data(DAY)))
