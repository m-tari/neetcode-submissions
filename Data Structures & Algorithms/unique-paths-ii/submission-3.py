class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}

        def dfs(i, j):
            if obstacleGrid[i][j] == 1:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            for di, dj in [[1, 0], [0, 1]]:
                ni, nj = i + di, j + dj
                if (0 <= ni < m and 0 <= nj < n):
                    res += dfs(ni, nj)

            cache[(i, j)] = res
            return res

        path = dfs(0, 0)
        return path