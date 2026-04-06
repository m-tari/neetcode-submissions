class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * n

        obstacle = False
        for j in range(n - 1, -1, -1):
            if obstacleGrid[m-1][j] == 1:
                obstacle = True
            if not obstacle:
                dp[j] = 1

        obstacle = False
        for i in range(m - 2, -1, -1):
            if obstacleGrid[i][n-1] != 1 and not obstacle:
                dp[n-1] = 1
            else:
                dp[n-1] = 0
                obstacle = True
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    dp[j] = dp[j] + dp[j+1]
                else:
                    dp[j] = 0
        return dp[0]