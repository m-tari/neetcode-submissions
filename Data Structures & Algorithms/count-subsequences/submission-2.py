class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)

        # dp[i][j]:  number of ways to build distinct subsequences from s[:i] to form t[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # Use the current character in s to match with t[0...j-1]
                    incl = dp[i -1][j - 1]
                    # Skip the current character in s to match with t[0...j-1]
                    excl =  dp[i -1][j]
                    dp[i][j] = incl + excl
                else:
                    dp[i][j] =  dp[i -1][j]

        return dp[m][n]
            