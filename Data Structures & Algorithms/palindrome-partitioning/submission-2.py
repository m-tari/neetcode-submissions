class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        dp = [[False] * n for _ in range(n)]

        for r in range(n):
            for l in range(r + 1):
                if s[l] == s[r] and (r - l <= 2 or dp[l - 1][r + 1]):
                    dp[l][r] = True

        def backtrack(i, cur):            
            if i == n:
                res.append(cur[:])
                return

            for j in range(i, n):
                if dp[i][j]:
                    cur.append(s[i: j + 1])
                    backtrack(j + 1, cur)
                    cur.pop()

        backtrack(0, [])
        return res

#                 ij
#        s = "abc"