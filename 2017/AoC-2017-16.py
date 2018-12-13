import time
from collections import deque

PUZZLE_INPUT_FILE_NAME = "AoC-2017-16-input.txt"
START_DANCERS = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p")

with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    moves = puzzle_input_file.read().split(",")
    print(f"There are {len(moves)} moves.")


def dance(dancers_in):
    dancers = list(dancers_in)
    for move in moves:
        if move[0] == "x":
            p1, p2 = move[1:].split("/")
            dancers[int(p1)], dancers[int(p2)] = dancers[int(p2)], dancers[int(p1)]
        elif move[0] == "p":
            d1, d2 = move[1:].split("/")
            p1 = dancers.index(d1)
            p2 = dancers.index(d2)
            dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
        elif move[0] == "s":
            p1 = -int(move[1:])
            dancers = dancers[p1:] + dancers[:p1]
    return dancers


start = time.time()
one_dance = dance(START_DANCERS)
end = time.time()

print(f"After 1 dance: {''.join(one_dance)} at {end - start:.4f} seconds.")

# Known right answer
assert ''.join(one_dance) == 'namdgkbhifpceloj'
