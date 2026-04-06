class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        res = []
        rows, cols = len(heights), len(heights[0])
        dirs = [[1,0], [0,1], [-1,0], [0, -1]]
        pac_cache = set()  # cells confirmed to reach pacific
        atl_cache = set()  # cells confirmed to reach atlantic

        def dp(r, c, visit):
            atl = (r, c) in atl_cache
            pac = (r, c) in pac_cache
            if atl and pac:
                return (True, True)

            if r == 0 or c == 0:
                pac = True
            if r == rows - 1 or c == cols - 1:
                atl = True

            visit.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    nr in range(rows) and
                    nc in range(cols) and
                    (nr, nc) not in visit and
                    heights[nr][nc] <= heights[r][c]
                ):
                    a, p = dp(nr, nc, visit)
                    atl = atl or a
                    pac = pac or p
                    if atl and pac:
                        break
            visit.remove((r, c))

            # Only cache True — False might be wrong due to visit blocking paths
            if atl: atl_cache.add((r, c))
            if pac: pac_cache.add((r, c))

            return (atl, pac)

        for x in range(rows):
            for y in range(cols):
                a, p = dp(x, y, set())
                if a and p:
                    res.append([x, y])
        return res

        
