#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2018 - Day X part 1"""

__author__ = "Serge Beaumont"
__date__ = "December 2018"

import time
import re

# 1117 units each with 5042 hit points
# (weak to slashing; immune to fire, radiation, bludgeoning)
# with an attack that does 44 fire damage
# at initiative 15

re_units = re.compile("^(\d+) units each with (\d+) hit points")
re_weak_to = re.compile("weak to ([a-z, ]*)")
re_attack = re.compile("with an attack that does (\d+) ([a-z]+) damage")
re_immune_to = re.compile("immune to ([a-z, ]*)")
re_initiative = re.compile("initiative (\d+)")


class Units(object):
    def __init__(self, line):
        self.amount = int(re_units.search(line).group(1))
        self.hp = int(re_units.search(line).group(2))
        self.attack_damage = int(re_attack.search(line).group(1))
        self.attack_type = re_attack.search(line).group(2)
        if re_weak_to.search(line):
            self.weak_to = re_weak_to.search(line).group(1).split(", ")
        else:
            self.weak_to = list()
        if re_immune_to.search(line):
            self.immune_to = re_immune_to.search(line).group(1).split(", ")
        else:
            self.immune_to = list()
        self.initiative = int(re_initiative.search(line).group(1))

    def attack_damage_to(self, other):
        if self.attack_type in other.immune_to:
            return 0
        else:
            multiplier = 2 if self.attack_type in other.weak_to else 1
            return self.amount * self.attack_damage * multiplier

    def attack(self, other):
        other.accept_damage(self.attack_damage_to(other))

    def accept_damage(self, damage_amount):
        self.amount -= damage_amount // self.hp

    @property
    def effective_power(self):
        return self.amount * self.attack_damage

    def __lt__(self, other):
        if self.effective_power == other.effective_power:
            return self.initiative < other.initiative
        else:
            return self.effective_power < other.effective_power

    def __str__(self):
        return f"Units({self.amount}, {self.hp}, {self.attack_damage}, {self.effective_power})"


def init_army(army_data):
    return [Units(line) for line in army_data]


def select_targets(attackers, defenders):
    selection = dict()
    chosen = []
    for attacker in sorted(attackers, reverse=True):
        choice = None
        max_damage = 0
        for defender in sorted([d for d in defenders if d not in chosen], reverse=True):
            damage = attacker.attack_damage_to(defender)
            if damage > max_damage:
                choice = defender
                max_damage = damage
        if choice:
            selection[attacker] = defender
            chosen.append(defender)
    return selection


def fight():
    immune_army_target_selections = select_targets(immune_system_army, infection_army)
    infection_army_target_selections = select_targets(infection_army, immune_system_army)

    all_selections = {**immune_army_target_selections, **infection_army_target_selections}
    attack_order = sorted(all_selections, key=lambda k: k.initiative, reverse=True)
    for attacker in attack_order:
        defender = all_selections[attacker]
        if defender in (immune_system_army + infection_army):
            attacker.attack(defender)
            if defender.amount <= 0:
                if defender in infection_army:
                    infection_army.remove(defender)
                if defender in immune_system_army:
                    immune_system_army.remove(defender)
    print("\n=== Fight Round ===")
    print_armies()


def print_armies():
    print("\nImmune System Army\n")
    total_isa = 0
    for army in immune_system_army:
        print(str(army))
        total_isa += army.amount
    print(f"Total Amount: {total_isa}")

    total_ia = 0
    print("\nInfection Army\n")
    for army in infection_army:
        print(str(army))
        total_ia += army.amount
    print(f"Total Amount: {total_ia}")


if __name__ == '__main__':
    start = time.time()

    with open("AoC-2018-24-test-input.txt") as infile:
        data = ([line.strip() for line in infile])
        immune_system_data = data[1:3]
        infection_data = data[5:7]

    # with open("AoC-2018-24-input.txt") as infile:
    #     data = ([line.strip() for line in infile])
    #     immune_system_data = data[1:11]
    #     infection_data = data[13:23]

    immune_system_army = init_army(immune_system_data)
    infection_army = init_army(infection_data)

    # print(immune_system_army)
    # print(infection_army)

    while (len(immune_system_army) > 0) and (len(infection_army) > 0):
        fight()
    print_armies()

    # 5216

    print(f"{time.time() - start:.4f} seconds to run.")

# 3172 too low