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

__author__ = "Serge Beaumont"
__date__ = "December 2024"

import math
from collections import namedtuple

# N, E, S, W
directions = (0, 1, 2, 3)

def sort_dict_by_values(d: dict) -> list:
    return [(k, v) for k, v in sorted(d.items(), key=lambda item: item[1])]


class Point(namedtuple('Point', ['x', 'y'])):
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

moves = (Point(0, -1), Point(1, 0), Point(0, 1), Point(-1, 0))

class Tile(object):
    def __init__(self, xy: Point, tile_type: str, neighbour_types: tuple):
        self.xy = xy
        self.tile_type = tile_type
        self.should_enter_from = [nb_type in ('S', '.') for nb_type in neighbour_types]
        self.visited_from = [False, False, False, False]
        self.weights = [math.inf, math.inf, math.inf, math.inf]

    @property
    def fully_visited(self) -> bool:
        return all([self.should_enter_from[i] == self.visited_from[i] for i in range(len(self.visited_from))])


def dir_diff(dir1, dir2):
    """0 = straight, 1 = turn, 2 = backtrack (u-turn)"""
    diff = abs(dir1 - dir2)
    if diff == 0:
        return 0
    elif diff == 1 or diff == 3:
        return 1
    elif diff == 2:
        return 2
    else:
        raise ValueError(f"Invalid directions: {dir1}, {dir2} => {diff}")

class Maze(object):
    def __init__(self, entries):
        self.entries = entries
        self.map = dict()
        for y in range(1, len(entries)-1):
            for x in range(1, len(entries[y])-1):
                neighbours = (entries[y-1][x], entries[y][x+1], entries[y+1][x], entries[y][x-1])
                tile = Tile(Point(x, y), entries[y][x], neighbours)
                self.map[Point(x, y)] = tile
                if tile.tile_type == 'E':
                    self.end = Point(x, y)
                elif tile.tile_type == 'S':
                    self.start = Point(x, y)

        self.unvisited = [tile_xy for tile_xy in self.map.keys()]
        self.visited = list()

    def get_type(self, xy):
        return self.map[xy]

    @property
    def next(self):
        return [t for t in sort_dict_by_values(self.map) if t in self.unvisited]

    def neighbors(self, xy):
        result = list()
        for d in directions:
            target_xy = xy + moves[d]
            if not target_xy in self.visited:
                target_tile = self.map[target_xy]
                if not target_tile.visited_from[d]:
        return [tile.xy for tile in self]


class Reindeer(object):
    def __init__(self, maze):
        self.maze = maze
        self.pos = self.maze.start
        self.direction = 1

    def find_shortest_path(self):
        current, weight = sort_dict_by_values(unvisited).pop(0)
        for i in range(3):
            for direction in directions:
                neighbour = (current[0] + moves[direction], direction)
                if neighbour not in visited:
                    neighbour_type = self.maze.get_type(neighbour[0])
                    if neighbour_type == '.':
                        dir_change = dir_diff(current[1], direction)
                        if dir_change == 0:
                            new_weight = weight + 1
                            unvisited[neighbour] = new_weight if new_weight < unvisited[neighbour] else unvisited[neighbour]
                        elif dir_change == 1:
                            new_weight = weight + 1001
                            unvisited[neighbour] = new_weight if new_weight < unvisited[neighbour] else unvisited[neighbour]
            visited[current] = weight
            unvisited.pop(current)
            print(sort_dict_by_values(unvisited))
            print(visited)
            current, weight = sort_dict_by_values(unvisited).pop(0)


        # while unvisited:
        #     for direction in directions:
        #         move = moves[direction]
        #         dir_change = dir_diff(current[:2], (self.pos[0] + move[0], self.pos[1] + move[1]))
        #         visited[self.pos] = 0



def part_1(entries: list[str]):
    maze = Maze(entries)
    reindeer = Reindeer(maze)
    reindeer.find_shortest_path()
    # print(maze.start, maze.end, reindeer.pos)
    # print(dir_diff(1, 3), dir_diff(1, 2), dir_diff(1, 1), dir_diff(0, 3))
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