#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2023 - Day 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2023"


class Area(object):
    def __init__(self, entries, visit_starting_location=True):
        self.entries = [[c for c in line] for line in entries]
        self.visited = self.new_visited_matrix()
        self.position = self.starting_position()
        self.direction = 0
        self.has_loop = False
        if visit_starting_location:
            self.visit()

    def starting_position(self) -> (int, int):
        """(X, Y) position from origin top left, 0-based"""
        for i in range(len(self.entries)):
            if '^' in self.entries[i]:
                return self.entries[i].index('^'), i

    def new_visited_matrix(self) -> list[list[set]]:
        return [[set() for e in line] for line in self.entries]

    def visit(self) -> None:
        if self.direction in self.visited[self.position[1]][self.position[0]]:
            self.has_loop = True
        self.visited[self.position[1]][self.position[0]].add(self.direction)

    def out_of_bounds(self, pos) -> bool:
        return (len(self.entries[0]) <= pos[0]) or (pos[0] < 0) or (len(self.entries) <= pos[1]) or (pos[1] < 0)

    def visit_count(self) -> int:
        return sum([sum([1 for e in line if e]) for line in self.visited])

    def next_position(self) -> (int, int):
        # NESW, origin top left
        directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
        return (self.position[0] + directions[self.direction][0],
                self.position[1] + directions[self.direction][1])

    def turn(self) -> None:
        self.direction = (self.direction + 1) % 4

    def guard_route(self) -> None:
        while not self.out_of_bounds(self.position) and not self.has_loop:
            np = self.next_position()
            if self.out_of_bounds(np):
                # Next position will be outside range, we're done.
                break
            elif self.entries[np[1]][np[0]] == '#':
                self.turn()
                # To update the direction this position has been visited with.
                self.visit()
            else:
                self.position = np
                self.visit()


def print_visited(visited_matrix, entries):
    print()
    for y in range(len(entries)):
        line = []
        for x in range(len(entries[0])):
            if entries[y][x] == '#':
                line.append("#")
            elif not visited_matrix[y][x]:
                line.append(".")
            elif visited_matrix[y][x] - {1, 3} == set():
                line.append("-")
            elif visited_matrix[y][x] - {0, 2} == set():
                line.append("|")
            else:
                line.append("+")
        print(''.join(line))


def part_1(entries: list[str]):
    area = Area(entries)
    area.guard_route()
    # print_visited(area.visited, area.entries)
    return area.visit_count()


def part_2(entries: list[str]):
    total = 0
    area = Area(entries, False)
    area.guard_route()
    for x in range(len(entries[0])):
        for y in range(len(entries)):
            if area.visited[y][x]:
                # print(x, y)
                loop_area = Area(entries, False)
                loop_area.entries[y][x] = '#'
                loop_area.guard_route()
                if loop_area.has_loop:
                    total += 1
    # print_visited(loop_area.visited, loop_area.entries)
    return total


def read_puzzle_data(file_number) -> list[str]:
    with open(f"AoC-2024-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)
    assert test_result == 41

    part_1_result = part_1(read_puzzle_data(puzzle_number))
    print("Part 1:", part_1_result)
    assert part_1_result == 4939

    test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 2:", test_result_2)
    assert test_result_2 == 6

    print("Part 2:", part_2(read_puzzle_data(puzzle_number)))
