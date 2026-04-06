class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        cache = {}

        def dfs(i, j):
            if j < 0:
                return i < 0
            if i < 0:
                if p[j] == "*":
                    return dfs(i, j - 2)
                return False
            
            if (i, j) in cache:
                return cache[(i, j)]

            res = False

            if p[j] == "." or s[i] == p[j]:
                res = dfs(i - 1, j - 1)

            if p[j] == "*":
                # Option 1: Always possible to skip the character and the asterisk
                res = dfs(i, j - 2)
                
                # Option 2: If characters match, try consuming s[i]
                if i >= 0 and (p[j-1] == s[i] or p[j-1] == '.'):
                    res = res or dfs(i - 1, j)

            cache[(i, j)] = res
            return res

        return dfs(m - 1, n - 1)


