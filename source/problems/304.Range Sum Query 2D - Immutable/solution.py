class NumMatrix:

    def get_sum(self, i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        return self.sum[i][j]

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        # For faster speed, self.sum = matrix can be used to modify the list in place
        self.sum = [[0] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.sum[i][j] = self.get_sum(i, j - 1) + self.get_sum(i - 1, j) - self.get_sum(i - 1, j - 1) + \
                                 matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.get_sum(row2, col2) - self.get_sum(row1 - 1, col2) - self.get_sum(row2, col1 - 1) + self.get_sum(
            row1 - 1, col1 - 1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)