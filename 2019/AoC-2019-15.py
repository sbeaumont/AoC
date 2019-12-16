from intcode_computer import Computer
from collections import namedtuple
from visualize_curses import CursesVisualizer


class Point(namedtuple('Point', 'x y')):
    __slots__ = ()

    def __add__(self, other):
        return self._replace(x=self[0] + other[0], y=self[1] + other[1])


Location = namedtuple('Location', 'type distance')
directions = {1: Point(0, 1), 2: Point(0, -1), 3: Point(-1, 0), 4: Point(1, 0)}
facings = (1, 4, 2, 3)


def manual_route():
    top_cap = '131143133131413131231231231231323242323132324232313'
    to_bottom = '23234234234234234234232424122323232323232324124223242424'
    right_cave = '143143143114142424242142424242424141413123123123231314131313232232323131131'
    finish_bottom = '313232323224231313131313413141441413413413141414242424242441414141141424141131313133131444'
    finish_top_left = '131331313323223232324432332322323112222424'
    backtrack = '3311441111441144222242444'
    explore_right = '41421421421421421421424141341341413131323233131331311414141314141414414141313313143143143143141'
    from_chimney = '31323131431431413131231231231232313131414141441411'
    t_split_left = '3131313131231231231323243234232424112224232424242424242223233232324244242342342424111122223323231'
    appendix = '232424331131331314431313131323233131331314131323131413131231232313131414141441413141424142342423232324242421141414141133'
    backtrack_to_t = '442233333311441133'
    going_up_from_t = '1113134331313413411'
    yet_another_t = '4141221133313123123123123132323242424242232342331312323131443331313232323423423423423423242'
    going_down_left = '414111222242423242412412421413344224242423232323323244323323232322232312312323131413133'
    route = top_cap + to_bottom + right_cave + finish_bottom + finish_top_left \
        + backtrack + explore_right + from_chimney + t_split_left + appendix + \
        backtrack_to_t + going_up_from_t + yet_another_t + going_down_left
    return route


def init_computer():
    with open("AoC-2019-input-15.txt") as infile:
        program = [int(x) for x in infile.read().strip().split(',')]
    return Computer(program, pause_on_output=1)


def boundaries(section):
    min_x = max_x = min_y = max_y = 0
    for pos in section.keys():
        if pos.x < min_x:
            min_x = pos.x
        elif pos.x > max_x:
            max_x = pos.x

        if pos.y < min_y:
            min_y = pos.y
        elif pos.y > max_y:
            max_y = pos.y
    return min_x, min_y, max_x, max_y


def print_section(section, robot_pos):
    min_x, min_y, max_x, max_y = boundaries(section)

    print('-' * (max_x - min_x + 1))
    for y in range(max_y, min_y - 1, -1):
        line = []
        for x in range(min_x, max_x + 1):
            pos = Point(x, y)
            if pos == (0, 0):
                line.append('+')
            elif pos == robot_pos:
                line.append('R')
            elif pos in section:
                symbols = ('\u2588', '.', 'O')
                line.append(symbols[section[pos].type])
            else:
                line.append(' ')
        print(''.join(line))
    print('-' * (max_x - min_x + 1))


def plot_section(cv: CursesVisualizer, section, robot_pos):
    min_x, min_y, max_x, max_y = boundaries(section)

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            pos = Point(x, y)
            if pos == (0, 0):
                cv.plot(pos, '+')
            elif pos == robot_pos:
                cv.plot(pos, 'R')
            elif pos in section:
                symbols = ('\u2588', '.', 'O')
                cv.plot(pos, symbols[section[pos].type])
            else:
                cv.plot(pos, ' ')
        cv.refresh()


def do_manual():
    section = dict()
    pos = Point(0, 0)
    section[pos] = Location(1, 0)
    computer = init_computer()
    for direction in [int(c) for c in manual_route()]:
        assert direction in directions
        status = computer.run_program([direction])[0]
        new_pos = pos + directions[direction]
        if status == 0:
            section[new_pos] = Location(0, 9999999999)
        elif status == 1:
            if new_pos not in section:
                section[new_pos] = Location(1, section[pos].distance + 1)
            pos = new_pos
        elif status == 2:
            section[new_pos] = Location(2, 9999999999)
            pos = new_pos
            print(f"Found oxygen system at {pos}")
            break
        else:
            print(f"Huh? Unknown status {status}")
            break
    print_section(section, pos)


def do_wall_follower():

    def turn(fc, right_left):
        return (fc + right_left) % 4

    def wall_at(dr):
        wall_direction = turn(facing, dr)
        pos_to_consider = pos + directions[facings[wall_direction]]
        if pos_to_consider in section:
            return section[pos_to_consider].type == 0
        else:
            return False

    section = dict()
    pos = Point(0, 0)
    section[pos] = Location(1, 0)
    computer = init_computer()
    facing = 0
    step = 0
    while step < 48000:
        step += 1

        direction_to_move = facings[facing]
        status = computer.run_program([direction_to_move])[0]
        new_pos = pos + directions[direction_to_move]
        if status == 0:
            section[new_pos] = Location(0, 9999999999)
        elif status == 1:
            if new_pos not in section:
                section[new_pos] = Location(1, section[pos].distance + 1)
            pos = new_pos
        elif status == 2:
            if new_pos not in section:
                section[new_pos] = Location(2, section[pos].distance + 1)
                print(f"Found oxygen system at {new_pos} at distance {section[new_pos].distance}")
                assert section[new_pos].distance == 336
                oxygen_system_pos = new_pos
            pos = new_pos
        else:
            print(f"Huh? Unknown status {status}")
            break

        wall_to_right = wall_at(1)
        wall_in_front = wall_at(0)
        wall_to_left = wall_at(-1)
        if not wall_to_right:
            facing = turn(facing, 1)
        elif wall_in_front and not wall_to_left:
            facing = turn(facing, -1)
        elif not wall_in_front:
            # Go straight
            pass
        elif wall_to_right and wall_to_left and wall_in_front:
            facing = turn(facing, 2)
        else:
            assert False, "Can't deal with situation"
    print_section(section, pos)
    return section, oxygen_system_pos


def fill_with_air(section, oxygen_system):

    def neighbours(l):
        return [l + p for p in directions.values()]

    has_oxygen = [oxygen_system]
    no_oxygen = [p for p, l in section.items() if (p not in has_oxygen) and (l.type == 1)]
    bounds = CursesVisualizer.boundaries(section.keys(), padding=1)
    with CursesVisualizer(bounds) as cv:
        plot_section(cv, section, None)
        minutes = 0
        while no_oxygen:
            minutes += 1
            getting_oxygen = list()
            for loc in has_oxygen:
                for neighbour in neighbours(loc):
                    if neighbour in no_oxygen:
                        no_oxygen.remove(neighbour)
                        getting_oxygen.append(neighbour)
                        section[neighbour] = section[neighbour]._replace(type=2)
                        cv.plot(neighbour, 'O')
                        cv.refresh()
            has_oxygen.extend(getting_oxygen)

        cv.write(cv.b_min, f"Part 2: {minutes}")
        cv.refresh()
    assert minutes != 69


if __name__ == '__main__':
    # do_manual()
    explored_section, oxygen_system = do_wall_follower()
    fill_with_air(explored_section, oxygen_system)
