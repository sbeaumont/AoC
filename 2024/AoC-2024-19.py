"""
Solution for Advent of Code challenge 2024

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"


def match_towels(to_match, towels):
    if to_match in towels:
        return True
    matching_towels = sorted([t for t in towels if to_match.startswith(t)], key=len, reverse=True)
    for towel in matching_towels:
        if match_towels(to_match[len(towel):], towels):
            return True
    return False

def count_towel_combos(to_match, towels, sub_counts=None):
    matching_towels = sorted([t for t in towels if to_match.startswith(t)], key=len, reverse=True)
    if not to_match: # Everything was consumed
        return 1
    if sub_counts and to_match in sub_counts:
        return sub_counts[to_match] + 1
    total = 0
    for towel in matching_towels:
        total += count_towel_combos(to_match[len(towel):], towels, sub_counts)
    return total

def simplify_towels(towels):
    result = list()
    for towel in towels:
        if not match_towels(towel, [t for t in towels if t != towel]):
            result.append(towel)
    return result

def count_sub_versions(towels):
    s_towels = simplify_towels(towels)
    # sub_counts = dict.fromkeys(towels, 0)
    sub_counts = dict()
    for towel in set(towels) - set(s_towels):
        sub_counts[towel] = count_towel_combos(towel, [t for t in towels if t != towel])
    return sub_counts

def part_1(entries):
    towels, designs = entries
    towels = simplify_towels(towels)
    total = 0
    for design in designs:
        if match_towels(design, towels):
            total += 1
    return total


def part_2(entries):
    towels, designs = entries
    sub_counts = count_sub_versions(towels)
    valid_designs = [d for d in designs if match_towels(d, simplify_towels(towels))]
    total = 0
    for design in valid_designs:
        combos = count_towel_combos(design, simplify_towels(towels), sub_counts)
        total += combos
        print(design, combos, total)
    return total


def read_puzzle_data(data_file: str):
    with open(data_file) as infile:
        lines = [line.strip() for line in infile.readlines()]
        return lines[0].split(', '), lines[2:]


assertions = {
    "Test 1": 6,
    "Part 1": 347,
    "Test 2": 16,
    "Part 2": None,
}
