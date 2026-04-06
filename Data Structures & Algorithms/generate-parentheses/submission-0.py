class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        perm = ""
        symb = "("  # "(" or ")" symbol
        # l number of "(" in perm
        # r number of ")" in perm

        def dfs(symb, perm, l, r):
            if len(perm) == 2*n:
                res.append("".join(perm))
                return
            perm += symb
            if l > r:
                if l < n:
                    dfs("(", perm, l+1, r)
                    dfs(")", perm, l, r+1)
                else:
                    dfs(")", perm, l, r+1)
            else:
                dfs("(", perm, l+1, r)
            

        dfs(symb, perm, 1, 0)

        return res