class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)


        def dfs(i, j):
            if i < 0:
                return True
            if j < 0:
                return False

            if p[j] == "." or s[i] == p[j]:
                return dfs(i - 1, j - 1)

            if p[j] == "*":
                if p[j - 1] == ".":
                    return True
                while p[j - 1] == s[i] and i >= 0:
                    i -= 1
                return dfs(i, j - 1)
            
            return False

        return dfs(m - 1, n - 1)


