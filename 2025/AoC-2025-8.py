"""
Solution for Advent of Code challenge 2025

1.
"""

__author__ = "Serge Beaumont"
__date__ = "December 2025"


from operator import itemgetter
from math import sqrt, prod, inf
from bisect import insort


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)

class Candidates:
    def __init__(self, query_point, size=10):
        self.query_point = query_point
        self.entries = list()
        self.size = size

    def add(self, candidate):
        if candidate != self.query_point:
            d = distance(self.query_point, candidate)
            insort(self.entries, (d, candidate))
            if len(self.entries) > self.size:
                self.entries.pop()

    @property
    def furthest(self) -> tuple:
        """Return the furthest candidate from the query_point."""
        return self.entries[-1]

    @property
    def threshold(self) -> float:
        """Return the distance of the furthest candidate."""
        return self.entries[-1][0]

    @property
    def is_empty(self) -> bool:
        return len(self.entries) == 0

    @property
    def all(self) -> list:
        return [(entry[0], self.query_point, entry[1]) for entry in self.entries]


class Node:
    """Implementation of a KD Tree.
    Partitions points in space by splitting them around the axes (X, Y, Z, X, Y...) into a tree structure."""
    def __init__(self, axis: int, nodes: list[tuple[int, int, int]]):
        """The init builds the tree."""
        self.axis = axis
        self.left = None
        self.right = None
        if len(nodes) == 1:
            self.median_point = nodes[0]
        else:
            sorted_nodes = sorted(nodes, key=itemgetter(axis))
            next_axis = (axis + 1) % 3
            median_index = len(sorted_nodes) // 2
            self.median_point = sorted_nodes[median_index]
            if median_index >= 1:
                self.left = Node(next_axis, sorted_nodes[:median_index])
            if median_index + 1 < len(sorted_nodes):
                self.right = Node(next_axis, sorted_nodes[median_index + 1:])

    def find_closest(self, query_point: tuple[int, int, int], best_so_far: Candidates) -> Candidates:
        """Use the KD tree to find the closest candidate to the query_point."""

        def find_in_children(this, other, best_candidate: Candidates) -> Candidates:
            if this:
                # Maybe a better candidate in "this" side?
                this.find_closest(query_point, best_candidate)

            # In the whole algorithm ignore the query point itself because that will give distance 0 and will always
            # be better than the closest other point.
            if self.median_point != query_point:
                # Is the median point of this node closer than the worst candidate we have so far?
                best_candidate.add(self.median_point)

            if other and best_candidate is not None:
                # This is the most magical bit. If the plane that we are considering is all on the far side of the
                # sphere of worst candidate you have so far then that whole other tree can be pruned since they're
                # never closer than what you have.
                perpendicular_to_plane = abs(query_point[self.axis] - self.median_point[self.axis])
                if perpendicular_to_plane < best_candidate.threshold:
                    other.find_closest(query_point, best_candidate)
            return best_candidate

        if best_so_far.is_empty and self.median_point != query_point:
            best_so_far.add(self.median_point)

        if query_point[self.axis] <= self.median_point[self.axis]:
            return find_in_children(self.left, self.right, best_so_far)
        else:
            return find_in_children(self.right, self.left, best_so_far)


def find_closest_pairs(entries: list[tuple[int, int, int]], k=10):
    """This finds all Local K: all the k nearest neighbours of each point.
    Merge all of them into a list of entries * k distance pairs."""
    # Initialize the KD tree.
    kd_tree = Node(0, entries)
    # Find the closest counterpart of each node
    closest = list()
    for e in entries:
        closest_to_e = kd_tree.find_closest(e, Candidates(e, k))
        for c in closest_to_e.all:
            if (c[0], c[2], c[1]) not in closest:
                closest.append(c)

    # Determine the two nodes with the smallest distance
    return sorted(closest, key=itemgetter(0))


def merge_circuits(entries: list[tuple[int, int, int]], closest_list: list, merges: int) -> list[set] | tuple:
    """Merge all the distance pairs into circuits based on 'merges' number of merges."""
    circuits = [{e,} for e in entries]
    for i in range(merges):
        pair = closest_list[i]
        d, left, right = pair
        new_circuits = list()
        left_circuit = None
        right_circuit = None
        for circuit in circuits:
            if left in circuit:
                left_circuit = circuit
            if right in circuit:
                right_circuit = circuit
            if left not in circuit and right not in circuit:
                new_circuits.append(circuit)
        new_circuits.append(left_circuit.union(right_circuit))

        # This bit is the return for part 2
        if len(new_circuits) == 1:
            print(f"The last two boxes to merge were {left} and {right}")
            return circuits, left, right

        circuits = new_circuits

    # This is the return for part 1
    return circuits

def part_1(entries: list[tuple[int, int, int]]):
    # The test case and the real case need different values, don't want to change the framework to pass in parameters...
    k = 5 if len(entries) < 100 else 5
    merges = 10 if len(entries) < 100 else 1000

    print(f"Comparing {len(entries)} entries with k={k} and merges={merges}")
    closest_list = find_closest_pairs(entries, k)

    circuits = merge_circuits(entries, closest_list, merges)

    sizes = [len(c) for c in circuits]
    return prod(sorted(sizes, reverse=True)[:3])


def part_2(entries: list[tuple[int, int, int]]):
    # The test case and the real case need different values, don't want to change the framework to pass in parameters...
    k = 5 if len(entries) < 100 else 5

    closest_list = find_closest_pairs(entries, k)
    merges = len(closest_list)

    print(f"Comparing {len(entries)} entries with k={k} and merges={merges}")

    circuits, left, right = merge_circuits(entries, closest_list, merges)
    return left[0] * right[0]


def read_puzzle_data(data_file: str) -> list:
    with open(data_file) as infile:
        return [tuple([int(x) for x in line.strip().split(',')]) for line in infile.readlines()]


assertions = {
    "Test 1": 40,
    "Part 1": 175500,
    "Test 2": 25272,
    "Part 2": 6934702555,
}
