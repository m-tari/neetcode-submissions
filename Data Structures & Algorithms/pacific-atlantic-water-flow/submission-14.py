class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        res = []
        rows, cols = len(heights), len(heights[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        pac, atl = set(), set()

        def dfs(r, c, visit, prevH):
            if (
                (r, c) not in visit and
                0 <= r < rows and
                0 <= c < cols and 
                heights[r][c] >= prevH
            ):
                visit.add((r, c))
                for dr, dc in dirs:
                    dfs(r + dr, c + dc, visit, heights[r][c])

        # All pacific cells
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])

        # All atlantic cells
        for c in range(cols):
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        for r in range(rows):
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])

        return res