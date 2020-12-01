#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 20 part 1

This is the epically bad and failed version for comedic purposes.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
from collections import defaultdict, deque


class Room(object):
    def __init__(self, coord):
        self._neighbours = dict()
        self.pos = coord

    def go_to(self, direction):
        self.open_door(direction)
        return get_room(self._neighbours[direction])

    def open_door(self, direction):
        n = get_adjacent_coord(self.pos, direction)
        self._neighbours[direction] = n
        get_room(n).open_door_inverse(direction)

    def open_door_inverse(self, direction):
        direction = inverse[direction]
        self._neighbours[direction] = get_adjacent_coord(self.pos, direction)

    def neighbours(self):
        return self._neighbours.values()

    def __repr__(self):
        return f"Room({self.pos}, {self._neighbours})"


inverse = {'W': 'E', 'E': 'W', 'N': 'S', 'S': 'N'}
rooms = {(0, 0): Room((0, 0))}


def get_room(coord):
    if coord not in rooms:
        rooms[coord] = Room(coord)
    return rooms[coord]


def get_adjacent_coord(coord, direction):
    if direction == 'W':
        new_coord = coord[0] - 1, coord[1]
    elif direction == 'E':
        new_coord = coord[0] + 1, coord[1]
    elif direction == 'N':
        new_coord = coord[0], coord[1] + 1
    elif direction == 'S':
        new_coord = coord[0], coord[1] - 1
    return new_coord


# def get_adjacent_room(coord, direction):
#     return get_room(get_adjacent_coord(coord))


def generate_paths(current, collector, path_so_far=list(), remainder=None):
    # Outer list is a (   |    |   ) alternatives
    # Inner list is a ( , , , ) concatenation
    for j in range(len(current)):
        if isinstance(current[j], list):
            for item in current[j]:
                generate_paths(item, collector, path_so_far.copy(), current[j + 1:])
        else:
            for c in current[j]:
                path_so_far.append(c)

    if remainder:
        for i in range(len(remainder)):
            if isinstance(remainder[i], list):
                for item in remainder[i]:
                    generate_paths(item, collector, path_so_far.copy(), current[j + 1:])
            else:
                for c in remainder[i]:
                    path_so_far.append(c)
    collector.append(path_so_far)


def breadth_first_search(root):
    # As always adapted from redblobgames.com's website
    frontier = deque()
    frontier.appendleft(root)
    came_from = dict()
    cost_so_far = dict()
    came_from[root] = None
    cost_so_far[root] = 0

    while len(frontier) > 0:
        current = frontier.pop()
        new_cost = cost_so_far[current] + 1
        for nxt in rooms[current].neighbours():
            if (nxt not in came_from) or (new_cost < cost_so_far[nxt]):
                frontier.appendleft(nxt)
                cost_so_far[nxt] = new_cost
                came_from[nxt] = current
    return came_from, cost_so_far


def parse_string(s):
    root = list()
    stack = list()
    stack.append(root)
    first_group = list()
    root.append(first_group)
    stack.append(first_group)
    collector = None
    for c in s:
        if c in ('W', 'S', 'N', 'E'):
            if not collector:
                collector = list()
            collector.append(c)
        elif collector:
            stack[-1].append(''.join(collector))
            collector = None

        if c == '(':
            brace = list()
            stack[-1].append(brace)
            stack.append(brace)
            sub = list()
            stack[-1].append(sub)
            stack.append(sub)
        elif c == '|':
            stack.pop()
            sub = list()
            stack[-1].append(sub)
            stack.append(sub)
        elif c == ')':
            # Pop sub
            stack.pop()
            # Pop brace
            stack.pop()
    return root


def do(s):
    print(s)
    all_paths = list()
    regex = parse_string(s)
    print(regex)
    generate_paths(regex, all_paths)

    for p in all_paths:
        print(''.join(p))

    for p in all_paths:
        current = get_room((0, 0))
        for step in p:
            current = current.go_to(step)

    graph, costs = breadth_first_search((0, 0))
    # print(graph)
    # print(costs)
    # print(max(costs, key=costs.get), max(costs.values()))
    return max(costs, key=costs.get)


if __name__ == '__main__':
    start = time.time()

    assert do("ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))") == 23
    assert do("WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))") == 31

    with open("AoC-2018-20-input.txt") as infile:
        data = infile.read().strip()[1:-1]

    do(data)


print(f"{time.time() - start:.4f} seconds to run.")

# assert max(costs.values()) != 54
