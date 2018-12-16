#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day 15 part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

from collections import deque
import numpy as np

adjacent_deltas = ((0, -1), (1, 0), (0, 1), (-1, 0))


class Combatant(object):
    def __init__(self, arena, pos, race):
        self.arena = arena
        self.x, self.y = pos
        self.race = race
        self.hp = 200
        self.attack_power = 3

    def move_and_attack(self):
        if self.can_attack():
            self.attack()
        else:
            self.move()
            self.attack()

    def move(self):
        target = self.find_target()
        if target:
            self.arena.grid[self.x, self.y] = '.'
            self.pos = target
            self.arena.grid[self.x, self.y] = self.race

    def can_attack(self):
        adjacent_combatants = [self.arena.combatant_at_pos(p) for p in self.arena.neighbours(self.pos)]
        adjacent_enemies = sorted([c for c in adjacent_combatants if c in self.enemies], key=(lambda c: (c.hp, c.y, c.x)))
        if adjacent_enemies:
            return adjacent_enemies[0]
        return None

    def attack(self):
        enemy = self.can_attack()
        if enemy:
            enemy.hp -= self.attack_power

    def in_range(self):
        return self.arena.passable_neighbours(self.pos)

    def find_target(self):
        # Scan the shortest paths to all reachable locations from this combatant's perspective.
        came_from = self.breadth_first_search()
        # Get all coordinates of the "in range" (adjacent) locations to all enemies
        enemy_in_range = [j for i in [e.in_range() for e in self.enemies] for j in i]
        # Find the intersection of in range and reachable coordinates: sort by reading order
        targets = sorted([c for c in came_from if c in enemy_in_range], key=lambda c: (c[1], c[0]))
        if targets:
            # Reconstruct the paths to all the target coordinates
            target_paths = sorted([self.reconstruct_path(came_from, target) for target in targets], key=lambda p: (len(p)))
            # Filter by the shortest path length
            shortest_length = min([len(p) for p in target_paths])
            # Take the first steps of all these shortest paths adjacent to this combatant
            next_steps = [p[0] for p in target_paths if len(p) == shortest_length]
            # Take the first adjacent step in reading order
            return sorted(next_steps, key=lambda c: (c[1], c[0]))[0]

    def reconstruct_path(self, came_from, goal):
        current = goal
        path = []
        while current != self.pos:
            path.append(current)
            current = came_from[current]
        #path.append(self.pos)  # optional
        path.reverse()  # optional
        return path

    def breadth_first_search(self):
        # As always adapted from redblobgames.com's website
        frontier = deque()
        frontier.appendleft(self.pos)
        came_from = dict()
        came_from[self.pos] = None

        while len(frontier) > 0:
            current = frontier.pop()
            for nxt in self.arena.passable_neighbours(current):
                if nxt not in came_from:
                    frontier.appendleft(nxt)
                    came_from[nxt] = current
        return came_from

    @property
    def enemies(self):
        return self.arena.elves if self.race == 'G' else self.arena.goblins

    @property
    def is_alive(self):
        return self.hp > 0

    @property
    def pos(self):
        return self.x, self.y

    @pos.setter
    def pos(self, value):
        self.x = value[0]
        self.y = value[1]

    def __lt__(self, other):
        # Reading order
        return (self.y < other.y) or ((self.y == other.y) and (self.x < other.x))

    def __str__(self):
        return f"{self.race}({self.hp})@{self.pos}"

    def __repr__(self):
        return f"Combatant({self.pos}, {self.race})"


class Arena(object):
    def __init__(self, data):
        self.grid = np.empty((len(data[0]), len(data)), dtype=str)
        self.init_grid(data)
        self.combatants = []
        self.init_combatants()
        self.rounds = 0
        self.starting_elves = len(self.elves)

    def elves_have_died(self):
        return len(self.elves) < self.starting_elves

    def set_elf_attack_power(self, value):
        for elf in self.elves:
            elf.attack_power = value

    def print_grid(self):
        for y in range(self.height):
            print(''.join(self.grid[:, y]))

    def grid_to_text(self):
        result = []
        for y in range(self.height):
            result.append(''.join(self.grid[:, y]))
        return result

    def neighbours(self, pos):
        return sorted([(pos[0] + d[0], pos[1] + d[1]) for d in adjacent_deltas], key=lambda c: (c[1], c[0]))

    def passable_neighbours(self, pos):
        return [c for c in self.neighbours(pos) if self.grid[c[0], c[1]] == '.']

    def init_grid(self, data):
        for y in range(len(data)):
            self.grid[:, y] = list(data[y])

    def init_combatants(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[x, y] in ('G', 'E'):
                    self.combatants.append(Combatant(self, (x, y), self.grid[x, y]))

    def purge(self):
        for c in self.combatants:
            if not c.is_alive:
                self.grid[c.x, c.y] = '.'
        self.combatants = [c for c in self.combatants if c.is_alive]

    def combatant_at_pos(self, pos):
        for c in self.all:
            if c.pos == pos:
                return c
        return None

    @property
    def width(self):
        return len(self.grid[:, 0])

    @property
    def height(self):
        return len(self.grid[0, :])

    @property
    def all(self):
        return sorted([c for c in self.combatants if c.is_alive])

    @property
    def elves(self):
        return sorted([c for c in self.all if c.race == 'E'])

    @property
    def goblins(self):
        return sorted([c for c in self.all if c.race == 'G'])

    def is_done(self):
        return (len(self.elves) == 0) or (len(self.goblins) == 0)

    def total_hp(self):
        return sum([c.hp for c in self.all if c.is_alive])


def print_arena(arena):
    print(f"\nAfter {arena.rounds} rounds")
    if arena.is_done():
        print(f"Combat ended after {arena.rounds} full rounds")
    arena.print_grid()
    print(', '.join([str(c) for c in arena.all]))


def do(file_name, result_file=None, attack_power=3):
    print(f"\nProcessing file {file_name}")
    with open(file_name) as infile:
        data = ([line.strip() for line in infile])

    if data[0][:4] == 'test':
        test_line = data[0].split(" ")
        data = data[1:]
    else:
        test_line = None
        data = data[:]

    arena = Arena(data)
    arena.set_elf_attack_power(attack_power)

    if DEBUG:
        print_arena(arena)

    while not arena.is_done():
        combatants = arena.all
        for c in combatants[:]:
            if c.is_alive:
                c.move_and_attack()
            if c is combatants[-1]:
                arena.rounds += 1
            arena.purge()
            if arena.is_done():
                break

        # Debug printing
        if DEBUG:
            print_arena(arena)
            input("Press Enter to continue...")

    arena.print_grid()
    for c in arena.all:
        print(c)

    if result_file:
        with open(result_file) as resultfile:
            check_data = ([line.strip() for line in resultfile])
        for check_line, arena_line in zip(check_data[1:], arena.grid_to_text()):
            assert check_line == arena_line, f"{arena_line} should be {check_line}"
        for hp, c in zip([int(hp) for hp in check_data[0].split(",")], arena.all):
            assert hp == c.hp

    if test_line:
        if arena.rounds != int(test_line[1]):
            print(f"**ERROR** Expected {test_line[1]} rounds, were {arena.rounds}")
        if arena.total_hp() != int(test_line[2]):
            print(f"**ERROR** Expected {test_line[2]} HP, is {arena.total_hp()} HP")

    print(f"Battle outcome of {file_name} is {arena.rounds} * {arena.total_hp()} = {arena.rounds * arena.total_hp()}")

    return arena


if __name__ == '__main__':
    DEBUG = False

    do("AoC-2018-15-test-1.txt", "AoC-2018-15-test-1-result.txt")
    do("AoC-2018-15-test-2.txt", "AoC-2018-15-test-2-result.txt")
    do("AoC-2018-15-test-3.txt", "AoC-2018-15-test-3-result.txt")
    do("AoC-2018-15-test-4.txt", "AoC-2018-15-test-4-result.txt")
    do("AoC-2018-15-test-5.txt", "AoC-2018-15-test-5-result.txt")
    do("AoC-2018-15-test-6.txt", "AoC-2018-15-test-6-result.txt")

    # DEBUG = True

    #do("AoC-2018-15-test-0.txt")
    #do("AoC-2018-15-test-s1.txt")

    do("AoC-2018-15-input.txt")
    # 196200!!!

    # 225179 too high
    # 192430 too low
    # 195179 too low

    # Part 2: raise attack power

    power = 4
    elves_are_dying = True
    while elves_are_dying:
        print(f"Trying {power} attack power...")
        arena = do("AoC-2018-15-input.txt", attack_power=power)
        elves_are_dying = arena.elves_have_died()
        if elves_are_dying:
            power += 1
    print(f"Battle outcome is {arena.rounds} * {arena.total_hp()} = {arena.rounds * arena.total_hp()} at {power} attack power")




