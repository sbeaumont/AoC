DATA = """R3, L5, R2, L2, R1, L3, R1, R3, L4, R3, L1, L1, R1, L3, R2, L3, L2, R1, R1, L1, R4, L1, L4, R3, L2, L2, R1, L1, R5, R4, R2, L5, L2, R5, R5, L2, R3, R1, R1, L3, R1, L4, L4, L190, L5, L2, R4, L5, R4, R5, L4, R1, R2, L5, R50, L2, R1, R73, R1, L2, R191, R2, L4, R1, L5, L5, R5, L3, L5, L4, R4, R5, L4, R4, R4, R5, L2, L5, R3, L4, L4, L5, R2, R2, R2, R4, L3, R4, R5, L3, R5, L2, R3, L1, R2, R2, L3, L1, R5, L3, L5, R2, R4, R1, L1, L5, R3, R2, L3, L4, L5, L1, R3, L5, L2, R2, L3, L4, L1, R1, R4, R2, R2, R4, R2, R2, L3, L3, L4, R4, L4, L4, R1, L4, L4, R1, L2, R5, R2, R3, R3, L2, L5, R3, L3, R5, L2, R3, R2, L4, L3, L1, R2, L2, L3, L5, R3, L1, L3, L4, L3"""

commands = DATA.split(', ')

deltas = ((0, 1), (1, 0), (0, -1), (-1, 0))
x = y = 0
direction = 0
history = []
iamthere = False

for command in commands:
    turn = command[0]
    distance = int(command[1:])

    direction = (direction + (1 if turn == 'R' else -1)) % 4

    for i in range(1, distance + 1):
        x += deltas[direction][0]
        y += deltas[direction][1]

        current = (x, y)

        if current in history:
            print("I was already at", current, ", which is", abs(x) + abs(y), "blocks away.")
            iamthere = True
            break
        else:
            history.append((x, y))

    if iamthere:
        break