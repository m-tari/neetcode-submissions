class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Space optimized
        n = len(coins)
        dp = [0] * (amount + 1) 

        dp[0] = 1

        for i in range(n):
            for a in range(1, amount + 1):
                    if a- coins[i] >= 0:
                         dp[a] += dp[a - coins[i]]

        print(dp)

        return dp[amount]

#  dp[i][a] = ways using coins[0..i]

#          a
#       -------------------
#   i |
#      |
#      |
