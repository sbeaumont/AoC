PUZZLE_INPUT_FILE_NAME = "AoC-2017-16-input.txt"
START_DANCERS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

with open(PUZZLE_INPUT_FILE_NAME) as puzzle_input_file:
    moves = puzzle_input_file.read().split(",")


def dance(dancers):
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


one_dance = dance(START_DANCERS.copy())

print("After 1 dance: {}".format("".join(one_dance)))

for i in range(999999999):
    if i % 1000000 == 0:
        print(i)

print("After 1000000000 dance: {}".format("".join(START_DANCERS)))
