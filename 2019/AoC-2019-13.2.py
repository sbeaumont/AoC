from intcode_computer import Computer

MAX_X = 50
MAX_Y = 25


def init_field(max_x, max_y):
    fld = list()
    for y in range(max_y):
        listofzeroes = [0] * max_x
        fld.append(listofzeroes)
    return fld


def print_field(fld, max_y):
    icons = (' ', '#', 'X', '=', 'O')
    for row in range(max_y):
        print(''.join([icons[x] for x in fld[row]]))


def do(data):
    field = init_field(MAX_X, MAX_Y)
    computer = Computer(data, pause_on_output=3, remember_input=False)
    # Free games
    computer.program[0] = 2

    score = 0
    joystick = 0
    paddle_x = None
    ball_x = None
    while not computer.on_fire:
        result = computer.run_program([joystick])
        if not result:
            break
        x, y, tile = result
        if (x, y) == (-1, 0):
            score = tile
        else:
            field[y][x] = tile

            if tile == 4:
                # ball
                ball_x = x
            elif tile == 3:
                # paddle
                paddle_x = x

        if ball_x is not None and paddle_x is not None:
            if ball_x > paddle_x:
                joystick = 1
            elif ball_x == paddle_x:
                joystick = 0
            else:
                joystick = -1
        print_field(field, MAX_Y)
    return score


if __name__ == '__main__':
    with open("AoC-2019-input-13.txt") as f:
        data = [int(x) for x in f.read().strip().split(',')]

    score = do(data)

    print("Score =", score)

    assert score == 20940
