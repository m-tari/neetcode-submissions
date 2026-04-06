class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS, COLS = len(grid), len(grid[0])

        q = collections.deque()
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        dist = 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row not in range(ROWS) or
                        col not in range(COLS) or
                        grid[row][col] != 2147483647
                    ):
                        continue
                    grid[row][col] = dist
                    q.append((row, col))
            
            dist += 1

        return