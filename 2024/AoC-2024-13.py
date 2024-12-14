#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

"""
My failed attempt at substitution...

a*a0 + b*b0 = p0
a = (p0 - b*b0) / a0

a*a1 + b*b1 = p1
b = (p1 - a*a1) / b1

a = (p0 - (((p1 - a*a1)      / b1)*b0) / a0
a = (p0 -  ((p1 - a*a1)*b0   / b1)     / a0
a = (p0 - ((p1*b0 - a*a1*b0) / b1)     / a0
a = (p0 - p1*b0/b1 - a*a1*b0/b1)       / a0
a = p0/a0 - p1*b0/b1/a0 - a*a1*b0/b1/a0
a + a*a1*b0/b1/a0 = p0/a0 - p1*b0/b1/a0
a(1 + a1*b0/b1/a0) = p0/a0 - p1*b0/b1/a0
a = (p0/a0 - p1*b0/b1/a0) / (1 + a1*b0/b1/a0)


a = (p_x - (((p_y - a*y_a) / y_b) * x_b) / x_a
a = (p_x - ((p_y - a*y_a) * x_b) / y_b) / x_a
a = (p_x - (p_y*x_b - a*y_b*x_b / y_b)) / x_a 
a = p_x/x_a - p_y*x_b/y_b/x_a - a*y_b*x_b/y_b/x_a
a + a*y_b*x_b/y_b/x_a = p_x/x_a - p_y*x_b/y_b/x_a
a(1 + y_b*x_b/y_b/x_a) = p_x/x_a - p_y*x_b/y_b/x_a
a = (p_x/x_a - p_y*x_b/y_b/x_a) / (1 + y_b*x_b/y_b/x_a)
"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"

import re

class Machine(object):
    def __init__(self, button_a, button_b, prize):
        self.a = button_a
        self.b = button_b
        self.prize = prize
        self.break_early = False

    @property
    def slope_a(self):
        return self.a[1] / self.a[0]

    @property
    def max_a(self):
        return min(self.prize[0] // self.a[0], self.prize[1] // self.a[1])

    @property
    def max_b(self):
        return min(self.prize[0] // self.b[0], self.prize[1] // self.b[1])

    @property
    def slope_b(self):
        return self.b[1] / self.b[0]

    @property
    def slope_prize(self):
        return self.prize[1] / self.prize[0]

    def xy(self, ab) -> (int, int):
        a, b = ab
        x = self.a[0] * a + self.b[0] * b
        y = self.a[1] * a + self.b[1] * b
        return x, y

    def cost(self, ab):
        return 3 * ab[0] + ab[1]

    @property
    def determinant(self):
        return self.a[0]*self.b[1] - self.a[1]*self.b[0]

    @property
    def solve_ab(self):
        a = (self.b[1]*self.prize[0] - self.b[0]*self.prize[1]) / self.determinant
        b = (-self.a[1]*self.prize[0] + self.a[0]*self.prize[1]) / self.determinant
        if int(a) == a and int(b) == b:
            return int(a), int(b)
        else:
            return None

    @property
    def ab_x_fit(self):
        return self.ab_fit(0)

    @property
    def ab_y_fit(self):
        return self.ab_fit(1)

    def ab_fit(self, x_or_y: int):
        solutions = list()
        for b in range(self.max_b, -1, -1):
            remainder = self.prize[x_or_y] - b * self.b[x_or_y]
            if remainder % self.a[x_or_y] == 0:
                a = remainder // self.a[x_or_y]
                solutions.append((a, b))
                if self.break_early:
                    break
        return solutions

    @property
    def ab_solutions(self):
        return list(set(self.ab_x_fit) & set(self.ab_y_fit))

    @property
    def cheapest_solution(self) -> (int, (int, int)):
        costs = [(self.cost(s), s) for s in self.ab_solutions]
        if costs:
            return min(costs)
        else:
            return None

    @property
    def solution_cost_2(self) -> int:
        return self.cost(self.solve_ab)

def part_1(machines: list[Machine]) -> int:
    total_tokens = 0
    for machine in machines:
        if machine.solve_ab:
            total_tokens += machine.solution_cost_2
        # cost = machine.cheapest_solution
        # print(machine.solve_a, machine.ab_solutions)
        # print(machine.solve_ab, machine.ab_solutions)
        # if cost:
        #     total_tokens += cost[0]
    return total_tokens


def part_2(machines: list[Machine]):
    move_prize = 10000000000000
    for machine in machines:
        machine.break_early = True
        machine.prize = (machine.prize[0] + move_prize, machine.prize[1] + move_prize)
    return part_1(machines)


def read_puzzle_data(data_file: str) -> list:
    button_xy = re.compile(r'X([+-][0-9]+), Y([+-][0-9]+)')
    prize_xy = re.compile(r'X=([0-9]+), Y=([0-9]+)')

    machines = list()
    with open(data_file) as infile:
        lines = [line.strip() for line in infile.readlines()]
        for i in range(0, len(lines), 4):
            b_a = button_xy.search(lines[i])
            button_a = (int(b_a.group(1)), int(b_a.group(2)))
            b_b = button_xy.search(lines[i+1])
            button_b = (int(b_b.group(1)), int(b_b.group(2)))
            b_p = prize_xy.search(lines[i+2])
            prize = (int(b_p.group(1)), int(b_p.group(2)))
            machine = Machine(button_a, button_b, prize)
            machines.append(machine)
    return machines


assertions = {
    "Test 1": 480,
    "Part 1": 31761,
    "Test 2": None,
    "Part 2": None,
}
