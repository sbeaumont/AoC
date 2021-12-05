#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2020 - Day 21"""

__author__ = "Serge Beaumont"
__date__ = "December 2020"

from pprint import pprint
from itertools import chain


def load(filename):
    result = list()
    with open(filename) as infile:
        for line in [l.strip() for l in infile.readlines()]:
            ingredients, allergens = line[:-1].split(' (contains ')
            result.append((ingredients.split(' '), allergens.split(', ')))
    return result


foods = load("AoC-2020-21-input.txt")
print(foods)

all_allergens = set()
all_ingredients = set()
allergens_to_foods = dict()
for food_ingredients, food_allergens in foods:
    all_allergens.update(food_allergens)
    all_ingredients.update(food_ingredients)
    for allergen in food_allergens:
        if allergen not in allergens_to_foods:
            allergens_to_foods[allergen] = set(food_ingredients)
        else:
            allergens_to_foods[allergen].intersection_update(food_ingredients)

allergenic_ingredients = {a for a in chain(*allergens_to_foods.values())}

print(all_ingredients)
print(all_allergens)
pprint(allergens_to_foods)
print(allergenic_ingredients)

part_1 = 0
for ingredients, allergens in foods:
    part_1 += len([ingredient for ingredient in ingredients if ingredient not in allergenic_ingredients])
print("Part 1:", part_1)

final_result = dict()
while len(allergens_to_foods) > 0:
    to_be_removed = list()
    to_be_removed_keys = list()
    # Find the allergen-food combos that 1-to-1 match
    for k, v in allergens_to_foods.items():
        if len(v) == 1:
            final_result[k] = list(v)[0]
            to_be_removed.append(list(v)[0])
            to_be_removed_keys.append(k)

    for k, v in allergens_to_foods.items():
        allergens_to_foods[k] = {i for i in v if i not in to_be_removed}

    for k in to_be_removed_keys:
        del(allergens_to_foods[k])

print([(k, final_result[k]) for k in sorted(final_result.keys())])
print(','.join([final_result[k] for k in sorted(final_result.keys())]))
