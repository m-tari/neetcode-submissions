import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights or not heights[0]:
            return 0

        ROWS, COLS = len(heights), len(heights[0])
        visit = set()
        heap = [[0, (0, 0)]]  # pair [abs(diff), (r, c)]
        res = 0  # minimum effort requierd
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            diff, n = heapq.heappop(heap)
            r, c = n[0], n[1]
            res = max(res, diff)

            if r == ROWS - 1 and c == COLS - 1:
                return res

            visit.add(n)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                    heapq.heappush(heap, [abs(heights[r][c] - heights[nr][nc]), (nr, nc)])

        return res