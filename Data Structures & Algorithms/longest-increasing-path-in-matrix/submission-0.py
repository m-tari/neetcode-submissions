class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        count = 0
        max_count = 0

        def dfs(r, c, count, prev):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                matrix[r][c] <= prev
            ):
                return 0
            
            count = 1 + max(
                dfs(r + 1, c, count, matrix[r][c]),
                dfs(r - 1, c, count, matrix[r][c]),
                dfs(r, c + 1, count, matrix[r][c]),
                dfs(r, c - 1, count, matrix[r][c])
            )

            return count

        for i in range(ROWS):
            for j in range(COLS):
                max_count = max(max_count, dfs(i, j, count, float("-inf")))

        return max_count

