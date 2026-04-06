class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 1

        for i in range(n):
            for a in range(1, amount + 1):
                    if i > 0:
                         dp[i][a] = dp[i - 1][a]
                    if a- coins[i] >= 0:
                         dp[i][a] += dp[i][a - coins[i]]

        return dp[n - 1][amount]

#          a
#       -------------------
#   i |
#      |
#      |
