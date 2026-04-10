import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        heap = []
        heapq.heappush(heap, (grid[0][0], (0, 0)))
        shortest = {}
        while heap:
            w1, n1 = heapq.heappop(heap)

            if n1 in shortest:
                continue

            r, c = n1
            shortest[n1] = w1

            if r == m - 1 and c == n - 1:
                return shortest[(m-1, n-1)]

            for dr, dc in [[1, 0], [0, 1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    heapq.heappush(heap, (w1 + grid[nr][nc], (nr, nc)))

