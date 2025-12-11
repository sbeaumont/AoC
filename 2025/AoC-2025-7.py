"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


from collections import defaultdict


def splitter_indexes(line: str) -> list[int]:
    indexes = list()
    for i in range(len(line)):
        if line[i] == "^":
            indexes.append(i)
    return indexes


def part_1(entries: list[str]):
    beams = {entries[0].index("S"),}
    split_happened = 0
    for e in entries[1:]:
        splitters = splitter_indexes(e)
        new_beams = set()
        for beam in beams:
            if beam in splitters:
                new_beams.add(beam + 1)
                new_beams.add(beam - 1)
                split_happened += 1
            else:
                new_beams.add(beam)
        beams = new_beams
    return split_happened


def part_2(entries: list[str]):
    """The trick is that once two timelines end up in the same spot they will lead to the same set of paths
    further down, so just add all occurences together."""
    beams = {entries[0].index("S"): 1}
    for e in entries[1:]:
        if all([c == '.' for c in e]):
            # print(' '.join([str(beams[k]).zfill(2) if k in beams else '..' for k in range(len(e))]))
            continue
        # else:
        #     print('  '.join(e))
        splitters = splitter_indexes(e)
        new_beams = dict()
        for beam, occurences in beams.items():
            if beam in splitters:
                new_beams[beam + 1] = occurences + new_beams[beam + 1] if beam + 1 in new_beams else occurences
                new_beams[beam - 1] = occurences + new_beams[beam - 1] if beam - 1 in new_beams else occurences
            else:
                new_beams[beam] = occurences + new_beams[beam] if beam in new_beams else occurences
        beams = new_beams
    return sum(beams.values())


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [line.strip() for line in infile.readlines()]


assertions = {
    "Test 1": 21,
    "Part 1": 1717,
    "Test 2": 40,
    "Part 2": 231507396180012,
}
