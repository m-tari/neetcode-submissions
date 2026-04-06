class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = [0] * (m + 1)

        for j in range(m + 1):
            dp[j] = j

        for i in range(1, n + 1):
            prevDp = dp[0]
            for j in range(1, m + 1):
                tmp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prevDp
                else:    
                    dp[j] = min(dp[j] + 1, dp[j-1] + 1,  prevDp + 1)
                prevDp = tmp
        return dp[m]  
                
