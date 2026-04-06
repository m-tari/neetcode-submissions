class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m = len(s)
        n = len(t)

        # dp[i]:  number of ways to build distinct subsequences from s[:i] to form t[:j]
        prevDp = [0] * (n + 1)
        dp = [0] * (n + 1)

        prevDp[0] = 1
        dp[0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    # Use the current character in s to match with t[0...j-1]
                    incl = prevDp[j - 1]
                    # Skip the current character in s to match with t[0...j-1]
                    excl =  prevDp[j]
                    dp[j] = incl + excl
                else:
                    dp[j] =  prevDp[j]
            prevDp = dp[:]

        return dp[n]
            