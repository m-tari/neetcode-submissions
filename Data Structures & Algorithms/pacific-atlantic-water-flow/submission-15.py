from typing import List


######################################################
# Solution for downhill approach whith cache optimization
######################################################

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # cache[r][c] is a bitmask:
        # 1 = pacific, 2 = atlantic, 3 = both, 0 = unknown
        cache = [[0] * COLS for _ in range(ROWS)]
        visiting = [[False] * COLS for _ in range(ROWS)]  # cycle guard in current path

        def dfs(r: int, c: int) -> int:
            # Out of bounds means we hit an ocean
            if r < 0 or c < 0:
                return 1  # Pacific
            if r >= ROWS or c >= COLS:
                return 2  # Atlantic

            if cache[r][c] != 0:
                return cache[r][c]

            if visiting[r][c]:
                return 0  # don't loop back in current path

            visiting[r][c] = True
            cur = heights[r][c]
            mask = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Water can flow to equal-or-lower neighbors (reverse perspective: from cell to neighbor)
                if 0 <= nr < ROWS and 0 <= nc < COLS:
                    if heights[nr][nc] <= cur:
                        mask |= dfs(nr, nc)
                else:
                    # stepping out hits an ocean
                    mask |= dfs(nr, nc)

                if mask == 3:
                    break

            visiting[r][c] = False
            cache[r][c] = mask
            return mask

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c) == 3:
                    res.append([r, c])
        return res