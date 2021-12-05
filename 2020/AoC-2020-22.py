from collections import deque

with open("AoC-2020-22-input.txt") as infile:
    lines = [line.strip() for line in infile.readlines()]
    split_index = lines.index('')
    player_1 = deque([int(n) for n in lines[1:split_index]])
    player_2 = deque([int(n) for n in lines[split_index + 2:]])

while len(player_1) > 0 and len(player_2) > 0:
    if player_1[0] > player_2[0]:
        player_1.append(player_1.popleft())
        player_1.append(player_2.popleft())
    else:
        player_2.append(player_2.popleft())
        player_2.append(player_1.popleft())

print(player_1)
print(player_2)

print(list(player_1)[::-1])

factor = 1
total = 0
for c in list(player_1)[::-1]:
    total += factor * c
    factor += 1
print(total)
