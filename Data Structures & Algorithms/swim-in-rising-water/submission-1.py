import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0
            
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        heap = [[grid[0][0], (0, 0)]]  # [min time to swim from (0, 0), (i, j)]
        n = len(grid)
        shortest = {}

        while heap:
            w1, n1 = heapq.heappop(heap)
            if n1 in shortest:
                continue
            shortest[n1] = w1

            for dx, dy in dirs:
                x2, y2 = n1[0] + dx, n1[1] + dy
                if (
                    0 <= x2 < n and 0 <= y2 < n 
                ):
                    w2 = grid[x2][y2]
                    if (x2, y2) not in shortest:
                        heapq.heappush(heap, [max(w1, w2), (x2, y2)])

        return shortest[(n - 1, n - 1)]
