class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.sums = [[0] * (n+1) for _ in range(m+1)]
        self.sums[1][1] = matrix[0][0]

        for i in range(2, m+1):
            self.sums[i][1] =  self.sums[i-1][1] + matrix[i-1][0]

        for j in range(2, n+1):
            self.sums[1][j] =  self.sums[1][j-1] + matrix[0][j-1]

        for i in range(2, m+1):
            for j in range(2, n+1):
                self.sums[i][j] = self.sums[i][j-1] + self.sums[i-1][j] - self.sums[i-1][j-1]  + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        res = self.sums[row2][col2] + self.sums[row1-1][col1-1] - self.sums[row1-1][col2] - self.sums[row2][col1-1]

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)