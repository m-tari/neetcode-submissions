class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board or not board[0]:
            return [[]]
        
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()

        def dfs(i, j):
            if (
                board[i][j] == "X" or
                i == 0 or i == m -1 or j == 0 or j == n - 1 or
                (i, j) in visit
            ):
                return

            visit.add((i, j))
            board[i][j] == "#"
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                dfs(ni, nj)
            visit.remove((i, j))


        for i in range(m):
            if board[i][0] == "O":
                board[i][0] = "#"
                dfs(i, 0)

        for i in range(m):
            if board[i][n - 1] == "O":
                board[i][n - 1] = "#"
                dfs(i, n - 1)

        for j in range(n):
            if board[0][j] == "O":
                board[0][j] = "#"
                dfs(0, j)

        for j in range(n):
            if board[m - 1][j] == "O":
                board[m - 1][j] = "#"
                dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        return