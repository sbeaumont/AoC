PUZZLE_INPUT_FILE_NAME = "AoC-2017-16-input.txt"
START_DANCERS = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p")

import time
start = time.time()

with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    moves = puzzle_input_file.read().split(",")
    print(f"There are {len(moves)} moves.")


def dance(dancers_in):
    dancers = list(dancers_in)
    for move in moves:
        if move[0] == "x":
            p1, p2 = [int(x) for x in move[1:].split("/")]
            dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
        elif move[0] == "p":
            d1, d2 = move[1:].split("/")
            p1 = dancers.index(d1)
            p2 = dancers.index(d2)
            dancers[p1], dancers[p2] = dancers[p2], dancers[p1]
        elif move[0] == "s":
            p1 = -int(move[1:])
            dancers = dancers[p1:] + dancers[:p1]
    return dancers


one_dance = dance(START_DANCERS)

print(f"After 1 dance: {''.join(one_dance)}")

# Known right answer
assert ''.join(one_dance) == 'namdgkbhifpceloj'

current_lineup = START_DANCERS
for i in range(9):
    print(i, ''.join(current_lineup))
    current_lineup = dance(current_lineup)

one_dance_shuffle = [START_DANCERS.index(dancer) for dancer in one_dance]
print(one_dance_shuffle)
current_lineup = START_DANCERS
for i in range(8):
    print(''.join(current_lineup))
    current_lineup = [current_lineup[idx] for idx in one_dance_shuffle]
print(f"After 1000000 dances: {''.join(current_lineup)}")

million_dance_shuffle = [START_DANCERS.index(dancer) for dancer in current_lineup]
print(million_dance_shuffle)
current_lineup = START_DANCERS
for i in range(1000):
    current_lineup = [current_lineup[idx] for idx in million_dance_shuffle]
print(f"After 1000000000 dances: {''.join(current_lineup)}")

