class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n

        for row in range(m - 1, -1, -1):
            curRow = [0] * n
            curRow [n -1] = 1
            for col in range(n - 2, -1, -1):
                curRow[col] = curRow[col + 1] + prevRow[col]
            prevRow = curRow

        return prevRow[0]
        