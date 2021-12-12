from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = matrix

        for i in range(m):
            for j in range(n):
                matrix[i][j] += self.get(i, j - 1) + self.get(i - 1, j) - self.get(i - 1, j - 1)

    def get(self, i: int, j: int) -> int:
        if i < 0:
            return 0
        if j < 0:
            return 0
        return self.matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get(row2, col2) - self.get(row2, col1 - 1) - self.get(row1 - 1, col2) + self.get(row1 - 1, col1 - 1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
