class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0  
        cols = set()
        positive = set()  #  positive diagonals, r + c = k, k=0...n
        negative = set()  #  negative diagonals, r - c = k,  k=0...n

        def backtrack(r):
            if r == n:
                self.res += 1
                return

            for c in range(n):
                if (
                    c not in cols and 
                    r + c not in positive and 
                    r - c not in negative 
                ):                
                    cols.add(c) 
                    positive.add(r + c) 
                    negative.add(r - c) 

                    backtrack(r + 1)
            
                    cols.remove(c) 
                    positive.remove(r + c) 
                    negative.remove(r - c) 


        backtrack(0)

        return self.res
