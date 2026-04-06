class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board = [["."] * n for _ in range(n)]
        res = []

        cols = set()
        mDiag = set()  # Main diagonal, r - c is constant
        aDiag = set()  # Anti diagonal, r + c is constant
            
        def backtrack(r):
            if r == n:
                cur = ["".join(row) for row in board]
                res.append(cur)
                return
            
            for c in range(n):
                if c in cols or r - c in mDiag or r + c in aDiag:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                mDiag.add(r - c)
                aDiag.add(r + c)

                backtrack(r + 1)

                board[r][c] = "."
                cols.remove(c)
                mDiag.remove(r - c)
                aDiag.remove(r + c)


        backtrack(0)
        return res

# Why It’s O(N!) (Worst Case)
# Your algorithm places one queen per row.

# At each row you try columns that are still available.

# Row	Max choices
# 0	        N
# 1	        N-1
# 2	        N-2
# ...	     ...
# N-1	  1

# So the number of permutations is roughly:

# N × (N-1) × (N-2) × ... × 1

# Which equals:
# N!


