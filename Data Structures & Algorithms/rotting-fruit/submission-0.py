class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh +=1

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (
                        row not in range(ROWS) or
                        col not in range(COLS) or
                        grid[row][col] != 1
                    ):
                        continue
                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1

            time += 1  

        return time if fresh ==0 else -1