from typing import Tuple, List


class Matrix(object):
    def __init__(self, list_of_lists: List[List]):
        self.rows = list_of_lists

    def __getitem__(self, item: Tuple[int, int]):
        if not (0 <= item[0] < self.width and 0 <= item[1] < self.height):
            raise KeyError(f"{item} is out of bounds.")

        return self.rows[item[1]][item[0]]

    def __setitem__(self, item: Tuple[int, int], value):
        if not (0 <= item[0] < self.width and 0 <= item[1] < self.height):
            raise KeyError(f"{item} is out of bounds.")

        self.rows[item[1]][item[0]] = value

    @property
    def width(self):
        return len(self.rows[0])

    @property
    def height(self):
        return len(self.rows)

    def neighbors4(self, point):
        """The four neighbors (without diagonals)."""
        x, y = point
        all_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [c for c in all_neighbors if (0 <= c[0] < self.width) and (0 <= c[1] < self.height)]

    def neighbors8(self, point):
        """The eight neighbors (with diagonals)."""
        x, y = point
        all_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),
                         (x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1)]
        return [c for c in all_neighbors if (0 <= c[0] < self.width) and (0 <= c[1] < self.height)]


if __name__ == '__main__':
    test_entries = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

    m = Matrix(test_entries)
    print(m[(2, 2)])
    print(m[(0, 2)])
    print(m[(2, 0)])
    print(m[(5, 0)])
