class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        visit = set()

        def dfs(r, c, grid, visit):
            area = 0
            if (r < 0 or c < 0 or r >= rows or c >= cols
                or grid[r][c] == 0 or (r, c) in visit):
                return 0
            area += 1
            visit.add((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                area += dfs(r + dr, c + dc, grid, visit)
            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    area = dfs(row, col, grid, visit)
                    if area > max_area:
                        max_area = area
        return max_area
        