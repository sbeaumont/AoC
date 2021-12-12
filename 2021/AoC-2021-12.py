#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day 12"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

from networkx import Graph


def part_1(entries):
    def walk(node):
        path.append(node)
        if node == 'end':
            all_paths.append(path.copy())
        else:
            for neighbor in graph[node].keys():
                if neighbor.isupper() or neighbor not in path:
                    walk(neighbor)
        path.pop()

    graph = Graph()
    graph.add_edges_from(entries)

    path = []
    all_paths = []
    walk('start')

    return len(all_paths)


def part_2(entries):
    def has_doubled_small_cave(path):
        small_caves = [c for c in path if not c.isupper()]
        return len(small_caves) != len(set(small_caves))

    def walk(node):
        path.append(node)
        if node == 'end':
            all_paths.append(path.copy())
        else:
            for neighbor in graph[node].keys():
                if neighbor.isupper():
                    walk(neighbor)
                elif neighbor in ('start', 'end'):
                    if neighbor not in path:
                        walk(neighbor)
                elif not has_doubled_small_cave(path):
                    walk(neighbor)
                elif neighbor not in path:
                    walk(neighbor)
        path.pop()

    graph = Graph()
    graph.add_edges_from(entries)

    path = []
    all_paths = []
    walk('start')
    return len(all_paths)


def read_puzzle_data(file_number):
    with open(f"AoC-2021-{file_number}-input.txt") as infile:
        lines = [line.strip().split('-') for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = "12"

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 10

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test-2"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 19

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test-3"))
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == 226

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 36

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-2"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 103

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-3"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 3509

    print("     Part 2:", part_2(read_puzzle_data(DAY)))
