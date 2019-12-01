# Taken from https://nbviewer.jupyter.org/url/norvig.com/ipython/Advent%20of%20Code.ipynb
# And then adapted to my style, tweaked not Pythonic naming etc.

# Python 3.x
import re
import numpy as np
import math
import urllib.request

from collections import Counter, defaultdict, namedtuple, deque
from functools import lru_cache
from itertools import permutations, combinations, chain, cycle, product
from heapq import heappop, heappush


def load_input(day, splitlines=True, strip=True):
    """Open this day's input file."""
    with open(f"AoC-2019-input-{day}.txt") as infile:
        if splitlines:
            data = infile.readlines()
            if strip:
                data = [line.strip() for line in data]
        else:
            data = infile.read()
            if strip:
                data = data.strip()
    return data


def transpose(matrix): return zip(*matrix)


def first(iterable): return next(iter(iterable))


def firsttrue(iterable): return first(it for it in iterable if it)


def counttrue(iterable): return sum(bool(it) for it in iterable)


cat = ''.join

Ø = frozenset()  # Empty set
inf = float('inf')
BIG = 10 ** 999
directions = ((0, -1), (1, 0), (0, 1), (-1, 0))


def grep(pattern, lines):
    """Print lines that match pattern."""
    for line in lines:
        if re.search(pattern, line):
            print(line)


def groupby(iterable, key=lambda it: it):
    """Return a dic whose keys are key(it) and whose values are all the elements of iterable with that key."""
    dic = defaultdict(list)
    for it in iterable:
        dic[key(it)].append(it)
    return dic


def powerset(iterable):
    """Yield all subsets of items."""
    items = list(iterable)
    for r in range(len(items) + 1):
        for c in combinations(items, r):
            yield c


# 2-D points implemented using (x, y) tuples
def X(point): return point[0]


def Y(point): return point[1]


def neighbors4(point):
    """The four neighbors (without diagonals)."""
    x, y = point
    return (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)


def neighbors8(point):
    """The eight neighbors (with diagonals)."""
    x, y = point
    return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
            (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1))


def cityblock_distance(p, q=(0, 0)):
    """City block distance between two points."""
    return abs(X(p) - X(q)) + abs(Y(p) - Y(q))


def euclidean_distance(p, q=(0, 0)):
    """Euclidean (hypotenuse) distance between two points."""
    return math.hypot(X(p) - X(q), Y(p) - Y(q))


def trace1(f):
    """Print a trace of the input and output of a function on one line."""

    def traced_f(*args):
        result = f(*args)
        print('{} = {}'.format(_callstr(f, args), result))
        return result

    return traced_f


def trace(f):
    """Print a trace of the call and args on one line, and the return on another."""

    def traced_f(*args):
        print(_callstr(f, args))
        trace.indent += 1
        try:
            result = f(*args)
        finally:
            trace.indent -= 1
        print('{} = {}'.format(_callstr(f, args), result))
        return result

    return traced_f


trace.indent = 0


def _callstr(f, args):
    """Return a string representing f(*args)."""
    return '{}{}({})'.format('> ' * trace.indent, f.__name__, ', '.join(map(str, args)))


def astar_search(start, h_func, move_func):
    """Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."""
    frontier = [(h_func(start), start)]  # A priority queue, ordered by path length, f = g + h
    previous = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}  # The cost of the best path to a state.
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in move_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))


def Path(previous, s):
    """Return a list of states that lead to state s, according to the previous dict."""
    return [] if (s is None) else Path(previous, previous[s]) + [s]


# ---------------------------------------------------------------------- My own stuff


def calculate_bounding_box(points):
    min_x = min([coord[0] for coord in points])
    min_y = min([coord[1] for coord in points])
    max_x = max([coord[0] for coord in points])
    max_y = max([coord[1] for coord in points])
    width = max_x - min_x
    height = max_y - min_y
    return np.array((min_x, min_y)), np.array((max_x, max_y)), width, height, width*height