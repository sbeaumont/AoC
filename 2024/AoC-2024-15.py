#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2024"""

__author__ = "Serge Beaumont"
__date__ = "December 2024"


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
move_directions = ('v', '>', '^', '<')

def mv(xy, direction):
    return xy[0] + direction[0], xy[1] + direction[1]

class Box(object):
    def __init__(self, x, y, environment):
        self.x = x
        self.y = y
        self.env = environment

    def set_xy(self, xy):
        self.env.remove(self)
        self.x = xy[0]
        self.y = xy[1]
        self.env.add(self)

    @property
    def xy(self):
        return self.x, self.y

    @property
    def body(self):
        return [self.xy,]

    def can_push(self, direction) -> bool:
        target_xy = mv(self.xy, direction)
        if self.env.get_obj(target_xy):
            return self.env.get_obj(target_xy).can_push(direction)
        else:
            return True

    def push(self, direction) -> bool:
        target_xy = mv(self.xy, direction)
        if self.env.get_obj(target_xy):
            if self.env.get_obj(target_xy).push(direction):
                self.set_xy(target_xy)
                return True
            else:
                return False
        else:
            self.set_xy(target_xy)
            return True

    @property
    def gps(self):
        return self.x + 100 * self.y

    @property
    def icon(self):
        return 'O'

class WideBox(Box):
    @property
    def right_side(self):
        return self.x + 1, self.y

    @property
    def body(self):
        return [self.xy, self.right_side]

    def can_push(self, direction) -> bool:
        left_obj = self.env.get_obj(mv(self.xy, direction))
        left_side_ok = right_side_ok = True
        if left_obj and left_obj is not self:
            left_side_ok = left_obj.can_push(direction)
        right_obj = self.env.get_obj(mv(self.right_side, direction))
        if right_obj and right_obj is not self and (left_obj != right_obj):
            right_side_ok = right_obj.can_push(direction)
        return left_side_ok and right_side_ok

    def push(self, direction) -> bool:
        success = self.can_push(direction)
        if success:
            left_obj = self.env.get_obj(mv(self.xy, direction))
            if left_obj and left_obj is not self:
                left_obj.push(direction)
            right_obj = self.env.get_obj(mv(self.right_side, direction))
            if right_obj and (right_obj is not self) and (left_obj != right_obj):
                right_obj.push(direction)
            self.set_xy(mv(self.xy, direction))
        return success


class Wall(Box):
    def set_xy(self, xy):
        raise Exception("Should not be calling this on a wall...?")

    def can_push(self, direction) -> bool:
        return False

    def push(self, direction):
        """Walls can't be pushed."""
        return False

    @property
    def gps(self):
        return 0

    @property
    def icon(self):
        return '#'


class WideWall(Wall):
    @property
    def body(self):
        return [self.xy, (self.x + 1, self.y)]


class Robot(Box):
    @property
    def gps(self):
        return 0

    @property
    def icon(self):
        return '@'


class Maze(object):
    def __init__(self, max_x, max_y):
        self.objs = dict()
        self.max_x = max_x
        self.max_y = max_y
        self.robot = None

    def add(self, obj):
        for xy in obj.body:
            self.objs[xy] = obj

    def add_robot(self, obj):
        self.add(obj)
        self.robot = obj

    def remove(self, obj):
        for xy in obj.body:
            del self.objs[xy]

    def get_obj(self, xy):
        return self.objs.get(xy, None)

    def icon_at(self, xy):
        return self.get_obj(xy).icon if self.get_obj(xy) else '.'

    @staticmethod
    def create_maze(entries, wide=False) -> 'Maze':
        max_x = len(entries[0])
        max_x = max_x * 2 if wide else max_x
        max_y = len(entries)
        maze = Maze(max_x, max_y)
        for y in range(len(entries)):
            for x in range(len(entries[0])):
                if entries[y][x] == "#":
                    if wide:
                        maze.add(WideWall(x*2, y, maze))
                    else:
                        maze.add(Wall(x, y, maze))
                elif entries[y][x] == "O":
                    if wide:
                        maze.add(WideBox(x*2, y, maze))
                    else:
                        maze.add(Box(x, y, maze))
                elif entries[y][x] == "@":
                    maze.add_robot(Robot(x*2 if wide else x, y, maze))
        return maze

    @property
    def score(self):
        return sum([ob.gps for ob in set(self.objs.values())])


def print_maze(maze):
    for y in range(maze.max_y):
        line = [maze.icon_at((x, y)) for x in range(maze.max_x)]
        print(''.join(line))


def part_1(entries):
    maze_input, moves = entries
    maze = Maze.create_maze(maze_input)
    # print(maze)
    # print(moves)
    for move in moves:
        # print("Moving", move)
        direction = directions[move_directions.index(move)]
        maze.robot.push(direction)
        # print_maze(maze)
    return maze.score


def part_2(entries: list[str]):
    maze_input, moves = entries
    maze = Maze.create_maze(maze_input, wide=True)

    for move in moves:
        # print_maze(maze)
        # print("Moving", move)
        direction = directions[move_directions.index(move)]
        maze.robot.push(direction)
    # print_maze(maze)
    return maze.score


def read_puzzle_data(data_file: str) -> tuple:
    with open(data_file) as infile:
        maze = list()
        moves = list()
        for line in [line.strip() for line in infile.readlines()]:
            if line.startswith("#"):
                maze.append(line)
            elif line == '':
                pass
            else:
                moves.append(line)
    return maze, ''.join(moves)


assertions = {
    "Test 1": 2028,
    "Part 1": 1471826,
    "Test 2": 1751,
    "Part 2": 1457703,
}

extra_tests = {
    "Test 1" : (
        ("AoC-2024-15-test-input-2.txt", 10092),
    ),
    "Test 2": (
        ("AoC-2024-15-test-input-3.txt", None),
        ("AoC-2024-15-test-input-2.txt", 9021),
    )
 }