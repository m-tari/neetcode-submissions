class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    res += 4
                    if 0<=r+1<m and grid[r+1][c] == 1:
                        res -= 1
                    if  0<=r-1<m and grid[r-1][c] == 1:
                        res -= 1
                    if  0<=c+1<n and grid[r][c+1] == 1:
                        res -= 1
                    if  0<=c-1<n and grid[r][c-1] == 1:
                        res -= 1

        return res
