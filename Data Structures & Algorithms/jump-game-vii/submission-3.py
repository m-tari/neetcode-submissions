class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == "1":
            return False

        dp = {n - 1: True}

        def dfs(i):
            if i in dp:
                return dp[i]

            dp[i] = False
            for j in range(min(i + maxJump, n - 1), i + minJump - 1, -1):
                if s[j] == "0" and dfs(j):
                    dp[i] = True
                    break

            return dp[i]

        return dfs(0)

#                                                        i=0
# i:        minJump    minJump+1 ...                            maxJump

# T: O((maxJump - minJump) ** n)   --> O((maxJump - minJump) * n)