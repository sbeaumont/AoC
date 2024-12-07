#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2015"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

class Lights(object):
    def __init__(self, entries: list[list[str]]):
        self.entries = entries
        self.grid = [[[True, 0] if lt == '#' else [False, 0] for lt in e] for e in self.entries]

        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                self.set_live_neighbours((x, y), self.count_live_neighbours((x, y)))

    def clone(self):
        return Lights(self.entries)

    def neighbour_coords(self, coord):
        boundaries = (len(self.grid[0]), len(self.grid))
        neighbour_deltas = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        result = []
        for d in neighbour_deltas:
            x = coord[0] + d[0]
            y = coord[1] + d[1]
            if (0 <= x < boundaries[0]) and (0 <= y < boundaries[1]):
                result.append((x, y))
        return result

    def light(self, xy):
        return self.grid[xy[1]][xy[0]]

    def is_live(self, xy):
        return self.light(xy)[0]

    def set_live(self, xy, value: bool):
        if not self.light(xy)[0] and value:
            # Switching on, broadcast
            self.light(xy)[0] = value
            for n_xy in self.neighbour_coords(xy):
                self.set_live_neighbours(n_xy, self.get_live_neighbours(n_xy) + 1)
            self.entries[xy[1]][xy[0]] = '#'
        elif self.light(xy)[0] and not value:
            # Switching off, broadcast
            self.light(xy)[0] = value
            for n_xy in self.neighbour_coords(xy):
                self.set_live_neighbours(n_xy, self.get_live_neighbours(n_xy) - 1)
            self.entries[xy[1]][xy[0]] = '.'

    def set_live_neighbours(self, xy, value: int):
        self.light(xy)[1] = value

    def get_live_neighbours(self, xy):
        return self.light(xy)[1]

    def count_live_neighbours(self, xy):
        result = 0
        for n_xy in self.neighbour_coords(xy):
            if 0 <= n_xy[0] < len(self.grid[0]) and 0 <= n_xy[1] < len(self.grid):
                result += 1 if self.is_live(n_xy) else 0
        return result

    def step(self):
        new_lights = self.clone()
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                live, live_nbs = self.grid[y][x]
                if live:
                    new_lights.set_live((x, y), True if live_nbs in (2, 3) else False)
                else:
                    new_lights.set_live((x, y), True if live_nbs == 3 else False)
        return new_lights

    @property
    def num_live_lights(self):
        return sum([sum([lt[0] for lt in line]) for line in self.grid])

    def print(self):
        for line in self.entries:
            print(''.join(line))


class LightsStuck(Lights):
    def __init__(self, entries: list[list[str]]):
        super().__init__(entries)
        self.stuck_lights = ((0, 0), (0, len(self.grid)-1), (len(self.grid[0])-1, 0), (len(self.grid[0])-1, len(self.grid)-1))
        for light in self.stuck_lights:
            super().set_live(light, True)

    def clone(self):
        return LightsStuck(self.entries)

    def set_live(self, xy, value: bool):
        if xy not in self.stuck_lights:
            super().set_live(xy, value)


def part_1(entries: list[str]):
    lights = Lights([list(e) for e in entries])
    for i in range(100):
        lights = lights.step()
        # print(i)
    return lights.num_live_lights


def part_2(entries: list[str]):
    lights = LightsStuck([list(e) for e in entries])
    for i in range(100):
        print(i, lights.num_live_lights)
        # lights.print()
        lights = lights.step()
    return lights.num_live_lights


def read_puzzle_data(file_number):
    with open(f"AoC-2015-{file_number}-input.txt") as infile:
        return [line.strip() for line in infile.readlines()]


if __name__ == '__main__':
    puzzle_number = int(__file__.split('.')[0].split('-')[-1])
    print(f"Day {puzzle_number}")

    test_result = part_1(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 1:", test_result)

    print("Part 1:", part_1(read_puzzle_data(puzzle_number)))

    test_result_2 = part_2(read_puzzle_data(f"{puzzle_number}-test"))
    print("Test 2:", test_result_2)

    print("Part 2:", part_2(read_puzzle_data(puzzle_number)))
