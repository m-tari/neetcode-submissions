class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)

        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0

            if s[i] != t[j]:
                return dfs(i + 1, j)

            incl = dfs(i + 1, j + 1)
            excl = dfs(i + 1, j)

            return incl +  excl

        return dfs(0, 0)