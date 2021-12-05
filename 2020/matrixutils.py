"""
Utility for working with matrices
"""


import numpy as np


class Matrix(object):
    def __init__(self, data):
        self.m = np.array(data)

    def fliplr(self):
        self.m = np.fliplr(self.m)
        return self

    def flipud(self):
        self.m = np.flipud(self.m)
        return self

    def rotate(self, rotations):
        self.m = np.rot90(self.m, k=rotations, axes=(1, 0))
        return self

    def column(self, column_nr):
        return list(self.m[:, column_nr])

    def row(self, row_nr_or_slice):
        return list(self.m[row_nr_or_slice, :])

    @property
    def edges(self):
        return [self.row(0), self.column(-1), self.row(-1), self.column(0)]

    def inner(self, border=1):
        return self.m[border:-border, border:-border]

    def __str__(self):
        return str(self.m)

    def to_str(self):
        return '\n'.join([''.join(self.row(r)) for r in range(len(self.column(0)))])


if __name__ == '__main__':
    A = Matrix(
        [[1, 4, 5, 12],
        [-5, 8, 9, 0],
        [-6, 7, 11, 19],
        [-8, -2, 25, 99]])

    print(A.flipud())
    print(A.fliplr())
    print(A.column(0))
    print(A.row(-1))
    print(A.rotate(1))
    print(A.edges)
    print(A.inner())
    print(A.m.tolist())
    print(A.to_str())

