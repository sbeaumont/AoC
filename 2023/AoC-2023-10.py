#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 10"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"

import sys
import networkx as nx


def neighbors(coords):
    """Return the neighbors of the x, y coordinates"""
    x, y = coords
    return (x-1, y), (x, y-1), (x, y+1), (x+1, y)


class Maze(object):
    def __init__(self, entries):
        self.entries = entries
        self.start = self.find_start()

    def get_pipe(self, coords):
        x, y = coords
        return self.entries[y][x]

    def neighbors_of(self, coords):
        """Return the neighbors of the pipe"""
        x, y = coords
        match self.get_pipe(coords):
            case '|':
                return (x, y-1), (x, y+1)
            case '-':
                return (x+1, y), (x-1, y)
            case 'L':
                return (x+1, y), (x, y-1)
            case 'J':
                return (x-1, y), (x, y-1)
            case '7':
                return (x-1, y), (x, y+1)
            case 'F':
                return (x+1, y), (x, y+1)
            case '.' | ' ':
                return []
            case 'S':
                return neighbors(coords)

    def find_start(self):
        """Find the starting node of the maze"""
        for y, entry in enumerate(self.entries):
            if 'S' in entry:
                return entry.index('S'), y


def pipe_of(coords, neighbors):
    x, y = coords
    if set(neighbors) == {(x, y-1), (x, y+1)}:
        return '|'
    elif set(neighbors) == {(x+1, y), (x-1, y)}:
        return '-'
    elif set(neighbors) == {(x+1, y), (x, y-1)}:
        return 'L'
    elif set(neighbors) == {(x-1, y), (x, y-1)}:
        return 'J'
    elif set(neighbors) == {(x-1, y), (x, y+1)}:
        return '7'
    elif set(neighbors) == {(x+1, y), (x, y+1)}:
        return 'F'
    raise Exception(f"Can't find pipe for {coords} with neighbors {neighbors}")


def create_frontier(G, maze):
    frontier = []
    G.add_node(maze.start)
    for nb in neighbors(maze.start):
        if maze.start in maze.neighbors_of(nb):
            frontier.append(nb)
            G.add_edge(maze.start, nb)
    return frontier


def clean_maze(maze, G, longest_path=None, for_printing=False):
    result = []
    for y, row in enumerate(maze.entries):
        line = []
        for x, cell in enumerate(row):
            coords = (x, y)
            if (coords == longest_path) and for_printing:
                line.append('*')
            elif coords in G:
                if coords == maze.start:
                    line.append(pipe_of(coords, list(G[maze.start])))
                else:
                    line.append(maze.get_pipe((x, y)))
            else:
                line.append(' ')

        if for_printing:
            if 'S' in line:
                line.append('<== S')
            if '*' in line:
                line.append('<== *')
        result.append(''.join(line))
    return result


def build_loop(maze, G):
    frontier = create_frontier(G, maze)
    while frontier:
        coords = frontier.pop()
        for neighbor in maze.neighbors_of(coords):
            if neighbor not in G.nodes:
                frontier.append(neighbor)
            G.add_edge(coords, neighbor)


def find_longest_path(maze, G):
    longest_path_length = 0
    longest_path = None
    for coords, length in nx.shortest_path_length(G, maze.start).items():
        if length > longest_path_length:
            longest_path_length = length
            longest_path = coords
    return longest_path, longest_path_length


def part_1(entries):
    maze = Maze(entries)
    G = nx.DiGraph()
    build_loop(maze, G)
    longest_path_coords, longest_path_length = find_longest_path(maze, G)
    cleaned = clean_maze(maze, G, longest_path_coords, True)
    for line in cleaned:
        print(line)
    print(f"Start: {maze.start}, Furthest: {longest_path_coords}, Distance: {longest_path_length}")
    return longest_path_length


def part_2(entries):
    """
    Based in the https://en.wikipedia.org/wiki/Point_in_polygon algorithm.
    """
    maze = Maze(entries)
    G = nx.DiGraph()
    build_loop(maze, G)
    cleaned = clean_maze(maze, G)
    filled_maze = []
    for line in cleaned:
        filled_line = []
        inside = False
        last_corner = None
        for point in line:
            if point in ('J', 'L', 'F', '7'):
                if not last_corner:
                    last_corner = point
                else:
                    above = ('L', 'J')
                    below = ('F', '7')
                    # if prev is opposite, swap. otherwise stay the same
                    if (point in above and last_corner in below) or (point in below and last_corner in above):
                        inside = not inside
            elif point in ('|', 'S'):
                inside = not inside

            if point == ' ':
                filled_line.append('I' if inside else 'O')
            else:
                filled_line.append(point)
        filled_maze.append(''.join(filled_line))

    inside_points = 0
    for line in filled_maze:
        inside_points += line.count('I')
        print(line)
    print()

    return inside_points


def read_puzzle_data(file_number):
    with open(f"AoC-2023-{file_number}-input.txt") as infile:
        lines = [line.strip() for line in infile.readlines()]
    return lines


if __name__ == '__main__':
    DAY = sys.argv[0].split('.')[0].split('-')[-1]
    print("Results for day", DAY)

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test"))
    print(f"Test Part 1: {test_result_part_1}")
    assert test_result_part_1 == 4

    test_result_part_1 = part_1(read_puzzle_data(f"{DAY}-test-2"))
    print(f"Test Part 1.2: {test_result_part_1}")
    assert test_result_part_1 == 8

    print("     Part 1:", part_1(read_puzzle_data(DAY)))

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-3"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 4

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-4"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 8

    test_result_part_2 = part_2(read_puzzle_data(f"{DAY}-test-5"))
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 10

    result_part_2 = part_2(read_puzzle_data(DAY))
    print("     Part 2:", result_part_2)
    assert result_part_2 == 104