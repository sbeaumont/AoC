"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


class Index:
    def __init__(self, index: list[tuple[int, int]]) -> None:
        self.entries = sorted(index)
        self.min = min([start for start, end in self.entries])
        self.max = max([end for start, end in self.entries])

    def __contains__(self, item: int) -> bool:
        for start, end in self.entries:
            if start <= item <= end:
                return True
        return False

def part_1(entries: tuple):
    index, ingredients = entries

    fresh = 0
    for ingredient in ingredients:
        if ingredient in index:
            fresh += 1
    return fresh


def part_2(entries: tuple):
    """Check each range and move a cursor with the currently highest checked ID.
    Depends on the index to be sorted from low to high start index."""
    index, ingredients = entries

    fresh = 0
    current = index.min
    for start, end in index.entries:
        if start <= current <= end:
            # Found a range that is partially larger
            fresh += end + 1 - current
            current = end + 1
        elif current < start:
            # Found a range that is fully larger
            fresh += end + 1 - start
            current = end + 1
        # Ignore smaller, because with the sorting that will not happen
    return fresh


def read_puzzle_data(data_file: str) -> tuple[Index, list[int]]:
    with open(data_file) as infile:
        index_entries = list()
        line = infile.readline().strip()
        while line != "":
            index_entries.append(tuple([int(x) for x in line.split("-")]))
            line = infile.readline().strip()
        index = Index(index_entries)

        ingredients = [int(line.strip()) for line in infile.readlines()]

    return index, ingredients





assertions = {
    "Test 1": 3,
    "Part 1": 739,
    "Test 2": None,
    "Part 2": None,
}
