class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        cache = {}  # (r, c) -> (pacific_reachable, atlantic_reachable)
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(r, c, visit):
            if (r, c) in cache:
                return cache[(r, c)]
            # mark edges
            pac = (r == 0 or c == 0)
            atl = (r == rows - 1 or c == cols - 1)

            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit:
                    if heights[nr][nc] <= heights[r][c]:
                        nr_pac, nr_atl = dfs(nr, nc, visit)
                        pac = pac or nr_pac
                        atl = atl or nr_atl
                        if pac and atl:
                           break 
            visit.remove((r, c))

            cache[(r, c)] = (pac, atl)
            return cache[(r, c)]

        res = []
        for r in range(rows):
            for c in range(cols):
                pac, atl = dfs(r, c, set())
                if pac and atl:
                    res.append([r, c])
        return res