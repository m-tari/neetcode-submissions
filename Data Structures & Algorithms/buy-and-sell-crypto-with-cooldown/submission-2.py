class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0

        # dp[i][j]: what is the maximum profit to gain while using prices[0...i] 
        # while holding (j=0) the stock or not(j=1).
        # We derive how we can get the max profit to reach (i. j) state
        dp = [[0] * 2 for _ in range(n)]

        # If there is only one item
        dp[0][0] = -prices[0]
        dp[0][1] = 0

        for i in range(1, n):
            # hold or buy
            if i >= 2:
                dp[i][0] = max(dp[i - 1][0], dp[i - 2][1] -  prices[i])
            else:
                dp[i][0] = max(dp[i - 1][0], -prices[i])
            # do nothing (not holding) or sell
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])

        return  dp[n - 1][1]