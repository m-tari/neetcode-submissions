class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = {}

        def dfs(i):
            if i > n:
                return 0
            
            if i in dp:
                return dp[i]

            pick1 = sum(stoneValue[i: i+1]) - dfs(i+1)
            pick2 = sum(stoneValue[i: i+2]) - dfs(i+2)
            pick3 = sum(stoneValue[i: i+3]) - dfs(i+3)
            
            res = max(pick1, pick2, pick3)
            dp[i] = res
            return res

        res = dfs(0)
        
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"