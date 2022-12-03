#!/usr/bin/env python3

"""Solution for Advent of Code challenge 2021 - Day X"""

__author__ = "Serge Beaumont"
__date__ = "December 2021"

# target area: x=20..30, y=-10..-5
TEST_TARGET_AREA = (20, 30, -10, -5)
EXPECTED_INITIAL_VELOCITY = (6, 9)
EXPECTED_TEST_RESULT = 45

# target area: x=209..238, y=-86..-59
TARGET_AREA = (209, 238, -86, -59)


def trajectory(dx, dy):
    x = y = 0
    while True:
        try:
            x += dx
            y += dy
            if dx > 0:
                dx -= 1
            elif dx < 0:
                dx += 1
            dy -= 1
            yield x, y
        except StopIteration:
            break


def find_right_velocity(x_vs, y_vs, x1, x2, y1, y2, break_on_first=False):
    all_hits = set()
    for vy in reversed(sorted(list(set(y_vs)))):
        for vx in x_vs:
            max_y = 0
            for x, y in trajectory(vx, vy):
                if y > max_y:
                    max_y = y
                if (x1 <= x <= x2) and (y1 >= y >= y2):
                    if break_on_first:
                        return vx, vy, max_y
                    else:
                        all_hits.add((vx, vy))
                if y < y2:
                    break
    return all_hits


def part_1(x1, x2, y2, y1, break_on_first=True):
    x = 0
    vx = 1
    x_vs = list()
    while x <= x2:
        x += vx
        if x1 <= x <= x2:
            x_vs.append(vx)
        vx += 1
    print(set(x_vs))

    y_vs = list()
    for vy in range(1, abs(y2) + 1):
        y = 0
        dv = -vy
        while y >= y2:
            y += dv
            if y1 >= y >= y2:
                y_vs.append(vy)
            dv -= 1
    print(set(y_vs))
    result = find_right_velocity(x_vs, y_vs, x1, x2, y1, y2, break_on_first)
    if break_on_first:
        print(f"Best velocity: ({result[0]}, {result[1]})")
        return result[2]
    else:
        print(result)
        return len(result)


def part_2(x1, x2, y1, y2):
    return part_1(x1, x2, y1, y2, False)


if __name__ == '__main__':
    test_result_part_1 = part_1(*TEST_TARGET_AREA)
    print("Test Part 1:", test_result_part_1)
    assert test_result_part_1 == EXPECTED_TEST_RESULT

    print("     Part 1:", part_1(*TARGET_AREA))

    test_result_part_2 = part_2(*TEST_TARGET_AREA)
    print("Test Part 2:", test_result_part_2)
    assert test_result_part_2 == 112

    print("     Part 2:", part_2(*TEST_TARGET_AREA))
