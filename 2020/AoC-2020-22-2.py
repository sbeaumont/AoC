from collections import deque


with open("AoC-2020-22-input.txt") as infile:
    lines = [line.strip() for line in infile.readlines()]
    split_index = lines.index('')
    deck_1 = deque([int(n) for n in lines[1:split_index]])
    deck_2 = deque([int(n) for n in lines[split_index + 2:]])


def recursive_combat(player_1, player_2):
    p1_scores = list()
    p2_scores = list()
    while len(player_1) > 0 and len(player_2) > 0:
        # Recursion rule: recurse if top card value == length of rest of deck
        if (player_1[0] >= (len(player_1) - 1)) and (player_2[0] >= (len(player_2) - 1)):
            # End game rule: if one player can't recurse, result is highest card
            # if (player_1[0] > len(player_1) - 1) or (player_2[0] > len(player_2) - 1):
            #     return player_1, player_2, player_1[0] > player_2[0]
            sub_game_done = True
            sub_game_p1_win = recursive_combat(deque(list(player_1)[1:]), deque(list(player_2)[1:]))[2]
        else:
            sub_game_done = False

        # Regular Combat round
        if player_1[0] > player_2[0] or (sub_game_done and sub_game_p1_win):
            player_1.append(player_1.popleft())
            player_1.append(player_2.popleft())
        else:
            player_2.append(player_2.popleft())
            player_2.append(player_1.popleft())

        # Infinite loop protection
        p1_score = hash(tuple(player_1))
        p2_score = hash(tuple(player_2))
        if (p1_score in p1_scores) and (p2_score in p2_scores):
            return player_1, player_2, True
        else:
            p1_scores.append(p1_score)
            p2_scores.append(p2_score)

    return player_1, player_2, len(player_1) > 0


def calculate_score(deck):
    factor = 1
    total = 0
    for c in list(deck)[::-1]:
        total += factor * c
        factor += 1
    return total


d1, d2, d1_last_win = recursive_combat(deck_1, deck_2)
print(d1)
print(d2)
print(calculate_score(d1), calculate_score(d2))

# assert calculate_score(d1) > 32407