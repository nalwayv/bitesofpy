""" 
Bite 31. Matrix multiplication / @ operator 
"""
from typing import List


class Matrix(object):
    def __init__(self, values: List[List[int]]):
        self.values = values

    def __repr__(self):
        return f'<Matrix values="{self.values}">'

    def _matrix(self, mat1: "Matrix", mat2: "Matrix") -> List[List[int]]:
        res = []
        for r1 in mat1.values:
            res2 = []
            for r2 in zip(*mat2.values):
                _sum = sum(a * b for a, b in zip(r1, r2))
                res2.append(_sum)
            res.append(res2)
        return res

    def __matmul__(self, other) -> "Matrix":
        if not isinstance(other, Matrix):
            raise ValueError('not a matrix')
        arr = self._matrix(self, other)
        return Matrix(arr)

    def __imatmul__(self, other) -> "Matrix":
        if not isinstance(other, Matrix):
            raise ValueError('not a matrix')
        self.values = self._matrix(self, other)
        return self

    def __rmatmul__(self, other) -> "Matrix":
        if not isinstance(other, Matrix):
            raise ValueError('not a matrix')
        arr = self._matrix(other, self)
        return Matrix(arr)


if __name__ == "__main__":
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[11, 12], [13, 14]])

    mat1 @= mat2
    print(mat1.values)
