class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        self.res = 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        def backtrack(i, j):
            if i == m - 1 and j == n - 1:
                self.res += 1

            if obstacleGrid[i][j] == 1:
                return

            for di, dj in [[1, 0], [0, 1]]:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n):
                    backtrack(ni, nj)


        backtrack(0, 0)
        return self.res