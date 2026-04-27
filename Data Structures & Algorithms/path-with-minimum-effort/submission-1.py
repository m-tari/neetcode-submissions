import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights or not heights[0]:
            return 0

        ROWS, COLS = len(heights), len(heights[0])
        visit = set()
        heap = [[0, 0, 0]]  #  [abs(diff), r, c], diff is the effort to get to point r, c
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while heap:
            diff, r, c = heapq.heappop(heap)

            if (r, c) in visit:
                continue

            visit.add((r, c))

            if r == ROWS - 1 and c == COLS - 1:
                return diff

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                    ndiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heapq.heappush(heap, [ndiff, nr, nc])