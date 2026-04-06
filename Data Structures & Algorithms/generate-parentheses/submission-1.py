class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        comb = ""
        # l number of "(" in comb
        # r number of ")" in comb

        def dfs(comb, l, r):
            if len(comb) == 2*n:
                res.append("".join(comb))
                return

            if l < n:
                dfs(comb + "(", l+1, r)
            if l > r:
                dfs(comb + ")", l, r + 1)
            

        dfs(comb, 0, 0)
        return res