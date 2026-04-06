class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return [[]]
        
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (
                i < 0 or i >= m or j < 0 or j >= n  or
                board[i][j] != "O"
            ):
                return

            board[i][j] = "#"
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if (
                    0 <= ni <= m - 1 and 0 <= nj <= n -1
                ):
                    dfs(ni, nj)


        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        return