class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 3)  # max advantage for a player at position i : max(sum(take1,2,or3) - max availabe score for opponent)

        for i in range(n - 1, -1, -1):
            pick1 = sum(stoneValue[i: i+1]) - dp[i+1]
            pick2 = sum(stoneValue[i: i+2]) - dp[i+2]
            pick3 = sum(stoneValue[i: i+3]) - dp[i+3]
            
            res = max(pick1, pick2, pick3)
            dp[i] = res


        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"