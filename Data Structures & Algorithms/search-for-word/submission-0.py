class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        if not board:
            return False
        
        dir = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = set()

        def backtrack(x, y, comb):
            if "".join(comb) == word:
                return True

            if  len(comb) > len(word):
                return False
            
            visited.add((x, y))

            for i, j in dir:
                r, c = x + i, y + j

                if (
                    (r, c) not in visited and
                    r < len(board) and r >= 0 and
                    c < len(board[0])  and c >= 0
                ):
                    comb.append(board[r][c])
                    visited.add((r, c))
                    if backtrack(r, c,  comb):
                        return True
                    comb.pop()
                    visited.remove((r, c))

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:  # start only if first char matches
                    res= backtrack(x, y, [board[x][y]])
                    if res:
                        return True

        return False
